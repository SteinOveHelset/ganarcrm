<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">{{ team.name }}</h1>

                <router-link :to="{'name': 'AddMember'}" class="button is-primary">Add member</router-link>
            </div>

            <div class="column is-12">
                <h2 class="subtitle">Members</h2>

                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Name</th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr
                            v-for="member in team.members"
                            v-bind:key="member.id"
                        >
                            <td>{{ member.username }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Team',
    data() {
        return {
            team: {
                members: []
            }
        }
    },
    mounted() {
        this.getTeam()
    },
    methods: {
        async getTeam() {
            this.$store.commit('setIsLoading', true)

            await axios
                .get('/api/v1/teams/get_my_team/')
                .then(response => {
                    this.team = response.data
                })
                .catch(error => {
                    console.log(error)
                })
            
            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>