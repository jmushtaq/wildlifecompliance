import ExternalDashboard from '../dashboard.vue'
import Proposal from '../proposal.vue'
import ProposalApply from '../proposal_apply.vue'
import ProposalSubmit from '../proposal_submit.vue'
import Organisation from '../organisations/manage.vue'
export default
{
    path: '/external',
    component:
    {
        render(c)
        {
            return c('router-view')
        }
    },
    children: [
        {
            path: '/',
            component: ExternalDashboard,
            name: 'external-proposals-dash' 
        },
        {
            path: 'organisations/manage/:org_id',
            component: Organisation
        },
        {
            path: 'proposal',
            component:
            {
                render(c)
                {
                    return c('router-view')
                }
            },
            children: [
                {
                    path: '/',
                    component: ProposalApply,
                    name:"apply_proposal"
                },
                {
                    path: 'submit',
                    component: ProposalSubmit,
                    name:"submit_proposal"
                },
                {
                    path: ':proposal_id',
                    component: Proposal,
                    name:"draft_proposal"
                },
            ]
        }
    ]
}
