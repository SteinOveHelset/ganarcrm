<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Add client</h1>
            </div>

            <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Name</label>
                        <div class="control">
                            <input type="text" class="input" v-model="name">
                        </div>
                    </div>

                    <div class="field">
                        <label>Contact person</label>
                        <div class="control">
                            <input type="text" class="input" v-model="contact_person">
                        </div>
                    </div>

                    <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <input type="email" class="input" v-model="email">
                        </div>
                    </div>

                    <div class="field">
                        <label>Phone</label>
                        <div class="control">
                            <input type="text" class="input" v-model="phone">
                        </div>
                    </div>

                    <div class="field">
                        <label>Website</label>
                        <div class="control">
                            <input type="text" class="input" v-model="website">
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Submit</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    import { toast } from 'bulma-toast'

    export default {
        name: 'AddClient',
        data() {
            return {
                name: '',
                contact_person: '',
                email: '',
                phone: '',
                estimated_value: 0,
                website: ''
            }
        },
        methods: {
            async submitForm() {
                this.$store.commit('setIsLoading', true)

                const client = {
                    name: this.name,
                    contact_person: this.contact_person,
                    email: this.email,
                    phone: this.phone,
                    website: this.website
                }

                await axios
                    .post('/api/v1/clients/', client)
                    .then(response => {
                        toast({
                            message: 'The client was added',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })

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