<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">{{ lead.company }}</h1>

                <router-link :to="{ name: 'EditLead', params: { id: lead.id }}" class="button is-light">Edit</router-link>
            </div>

            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle">Details</h2>

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
            async getLead() {
                this.$store.commit('setIsLoading', true)

                const leadID = this.$route.params.id

                axios
                    .get(`/api/v1/leads/${leadID}/`)
                    .then(response => {
                        this.lead = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            }
        }
    }
</script>