<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Add note</h1>
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
                        <label>Body</label>
                        <div class="control">
                            <textarea class="textarea" v-model="body"></textarea>
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
        name: 'AddNote',
        data() {
            return {
                name: '',
                body: ''
            }
        },
        methods: {
            async submitForm() {
                this.$store.commit('setIsLoading', true)

                const note = {
                    name: this.name,
                    body: this.body,
                    client_id: this.$route.params.id
                }

                await axios
                    .post('/api/v1/notes/', note)
                    .then(response => {
                        toast({
                            message: 'The note was added',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })

                        this.$router.push({ name: 'Client', params: { id: this.$route.params.id }})
                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            }
        }
    }
</script>