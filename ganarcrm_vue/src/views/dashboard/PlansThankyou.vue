<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Thank you</h1>
            </div>

            <div class="column is-4">
                <p>Thank you for subscribing to a plan!</p>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

import { toast } from 'bulma-toast'

export default {
    name: 'PlansThankyou',
    data() {
        return {
        }
    },
    mounted() {
        axios
            .post('/api/v1/stripe/check_session/', {
                'session_id': this.$route.query.session_id
            })
            .then(response => {
                console.log(response)

                toast({
                    message: 'The plan was changed!',
                    type: 'is-success',
                    dismissible: true,
                    pauseOnHover: true,
                    duration: 2000,
                    position: 'bottom-right',
                })

                this.$store.commit('setTeam', {
                    'id': response.data.id, 
                    'name': response.data.name,
                    'plan': response.data.plan.name,
                    'max_leads': response.data.plan.max_leads,
                    'max_clients': response.data.plan.max_clients
                })
            })
            .catch(error => {
                toast({
                    message: 'Something went wrong...',
                    type: 'is-error',
                    dismissible: true,
                    pauseOnHover: true,
                    duration: 2000,
                    position: 'bottom-right',
                })

                console.log('Error', error)
            })
    },
}
</script>