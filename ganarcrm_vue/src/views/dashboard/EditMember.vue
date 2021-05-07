<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Edit member</h1>
            </div>

            <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>First name</label>
                        <div class="control">
                            <input type="text" class="input" v-model="user.first_name">
                        </div>
                    </div>

                    <div class="field">
                        <label>Last name</label>
                        <div class="control">
                            <input type="text" class="input" v-model="user.last_name">
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Update</button>
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
        name: 'EditMember',
        data() {
            return {
                user: {}
            }
        },
        mounted() {
            this.getUser()
        },
        methods: {
            async getUser() {
                this.$store.commit('setIsLoading', true)

                const userID = this.$route.params.id

                await axios
                    .get(`/api/v1/teams/member/${userID}/`)
                    .then(response => {
                        this.user = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            },
            async submitForm() {
                this.$store.commit('setIsLoading', true)

                const userID = this.$route.params.id

                await axios
                    .put(`/api/v1/teams/member/${userID}/`, this.user)
                    .then(response => {
                        toast({
                            message: 'The user was updated',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })

                        this.$router.push({ name: 'MyAccount' })
                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            }
        }
    }
</script>