<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Clients</h1>

                <router-link to="/dashboard/clients/add">Add client</router-link>
            </div>

            <div class="column is-12">
                <template v-if="clients.length">
                    <table class="table is-fullwidth">
                        <thead>
                            <tr>
                                <th>Name</th>
                                <th>Contact person</th>
                                <th></th>
                            </tr>
                        </thead>

                        <tbody>
                            <tr
                                v-for="client in clients"
                                v-bind:key="client.id"
                            >
                                    <td>{{ client.name }}</td>
                                    <td>{{ client.contact_person }}</td>
                                    <td>
                                        <router-link :to="{ name: 'Client', params: { id: client.id }}">Details</router-link>
                                    </td>
                            </tr>
                        </tbody>
                    </table>
                </template>

                <template v-else>
                    <p>You don't have any clients yet...</p>
                </template>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: 'Clents',
        data() {
            return {
                clients: []
            }
        },
        mounted() {
            this.getClients()
        },
        methods: {
            async getClients() {
                this.$store.commit('setIsLoading', true)

                await axios
                    .get('/api/v1/clients/')
                    .then(response => {
                        this.clients = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            }
        }
    }
</script>