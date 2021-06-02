<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">{{ lead.company }}</h1>

                <div class="buttons">
                    <router-link :to="{ name: 'EditLead', params: { id: lead.id }}" class="button is-light">Edit</router-link>
                    <button @click="convertToClient" class="button is-info">Convert to client</button>
                    <button @click="deleteLead" class="button is-danger">Delete</button>
                </div>
            </div>

            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle">Details</h2>

                    <template v-if="lead.assigned_to">
                        <p><strong>Assigned to: </strong>{{ lead.assigned_to.first_name }} {{ lead.assigned_to.last_name }}</p>
                    </template>
                    <p><strong>Status: </strong>{{ lead.status }}</p>
                    <p><strong>Priority: </strong>{{ lead.priority }}</p>
                    <p><strong>Confidence: </strong>{{ lead.confidence }}</p>
                    <p><strong>Estimated value: </strong>{{ lead.estimated_value }}</p>
                    <p><strong>Created at: </strong>{{ lead.created_at }}</p>
                    <p><strong>Modified at: </strong>{{ lead.modified_at }}</p>
                </div>
            </div>

            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle">Contact information</h2>

                    <p><strong>Contact person: </strong>{{ lead.contact_person }}</p>
                    <p><strong>Email: </strong>{{ lead.email }}</p>
                    <p><strong>Phone: </strong>{{ lead.phone }}</p>
                    <p><strong>Website: </strong>{{ lead.website }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: 'Lead',
        data() {
            return {
                lead: {}
            }
        },
        mounted() {
            this.getLead()
        },
        methods: {
            async deleteLead() {
                this.$store.commit('setIsLoading', true)

                const leadID = this.$route.params.id

                await axios
                    .post(`/api/v1/leads/delete_lead/${leadID}/`)
                    .then(response => {
                        console.log(response.data)

                        this.$router.push('/dashboard/leads')
                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            },
            async getLead() {
                this.$store.commit('setIsLoading', true)

                const leadID = this.$route.params.id

                await axios
                    .get(`/api/v1/leads/${leadID}/`)
                    .then(response => {
                        this.lead = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            },
            async convertToClient() {
                this.$store.commit('setIsLoading', true)

                const leadID = this.$route.params.id
                const data = {
                    lead_id: leadID
                }

                await axios
                    .post(`/api/v1/convert_lead_to_client/`, data)
                    .then(response => {
                        console.log('converted to client')

                        this.$router.push('/dashboard/clients')
                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            }
        }
    }
</script>