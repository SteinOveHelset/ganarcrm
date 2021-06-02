<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">{{ team.name }}</h1>

                <hr>

                <p><strong>Plan: </strong>{{ $store.state.team.plan }}</p>
                <p><strong>Max clients: </strong>{{ $store.state.team.max_clients }}</p>
                <p><strong>Max leads: </strong>{{ $store.state.team.max_leads }}</p>
                <p v-if="$store.state.team.plan !== 'Free'"><strong>Plan end date: </strong>{{ team.plan_end_date }}</p>

                <p>
                    <router-link :to="{'name': 'Plans'}">Change plan</router-link>
                </p>

                <hr>

                <template v-if="team.created_by.id === parseInt($store.state.user.id)">
                    <router-link :to="{'name': 'AddMember'}" class="button is-primary">Add member</router-link>
                </template>
            </div>

            <div class="column is-12">
                <h2 class="subtitle">Members</h2>

                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Username</th>
                            <th>Full name</th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr
                            v-for="member in team.members"
                            v-bind:key="member.id"
                        >
                            <td>{{ member.username }}</td>
                            <td>{{ member.first_name }} {{ member.last_name }}</td>
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
                members: [],
                created_by: {}
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