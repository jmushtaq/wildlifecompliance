var site_url = location.origin

module.exports = {
    person_org_lookup: '/api/person_org_lookup',
    organisations: '/api/organisations/',
    organisations_paginated: '/api/organisations_paginated/',
    organisation_requests: '/api/organisation_requests/',
    organisation_requests_paginated: '/api/organisation_requests_paginated/',
    organisation_contacts: '/api/organisation_contacts/',
    organisation_access_group_members: '/api/organisation_access_group_members/',
    users: '/api/users/',
    users_paginated: '/api/users_paginated/',
    my_user_details: '/api/my_user_details/',
    assessor_group:'/api/assessor_group/',
    emailidentities: '/api/emailidentities/',
    profiles: '/api/profiles/',
    my_profiles: '/api/my_profiles/',
    assessment:'/api/assessment/',
    assessment_paginated:'/api/assessment_paginated/',
    amendment:'/api/amendment/',
    is_new_user: '/api/is_new_user/',
    user_profile_completed: '/api/user_profile_completed/',
    //countries: "https://restcountries.eu/rest/v1/?fullText=true/",
    countries: '/api/countries',
    is_compliance_management_callemail_readonly_user: '/api/is_compliance_management_callemail_readonly_user',
    application_type:"/api/application_type/",
    applications:"/api/application/",
    application_selected_activity:"/api/application_selected_activity/",
    applications_paginated:"/api/application_paginated/",
    licences:"/api/licences/",
    licences_paginated:"/api/licences_paginated/",
    returns:"/api/returns/",
    returns_paginated:"/api/returns_paginated/",
    application_standard_conditions:"/api/application_standard_conditions/",
    return_types:"/api/return_types/",
    application_conditions:"/api/application_conditions/",
    discard_application:function (id) {
      return `/api/application/${id}/`;
    },
    site_url: site_url,
    system_name: 'Wildlife Licensing System',
    call_email: "/api/call_email/",
    offence: "/api/offence/",
    sanction_outcome: "/api/sanction_outcome/",
    sanction_outcome_paginated: "/api/sanction_outcome_paginated/",
    remediation_action: "/api/remediation_action/",
    classification: "/api/classification/",
    report_types: "/api/report_types/",
    referrers: "/api/referrers/",
    location: "/api/location/",
    compliancepermissiongroup: '/api/compliancepermissiongroup/',
    region_district: '/api/region_district/',
    case_priorities: '/api/case_priorities/',
    inspection_types: '/api/inspection_types/',
    call_email_paginated: '/api/call_email_paginated/',
    inspection: '/api/inspection/',
    temporary_document: '/api/temporary_document/',
    compliance_management_users: '/api/compliance_management_users/',
    legal_case: '/api/legal_case/',
    legal_case_priorities: '/api/legal_case_priorities/',
    //document_artifact_types: '/api/document_artifact_types/',
    document_artifact_types: '/api/document_artifact/document_type_choices/',
    physical_artifact_types: '/api/physical_artifact_types/',
    artifact: '/api/artifact/',
    physical_artifact: '/api/physical_artifact/',
    document_artifact: '/api/document_artifact/',
    department_users: '/api/department_users',
    disposal_methods: '/api/disposal_methods',
    geocoding_address_search_token: '/api/geocoding_address_search_token/',
    geocoding_address_search: `https://api.mapbox.com/geocoding/v5/mapbox.places/`,
    system_preference: '/api/system_preference/',
    /*
    geocoding_address_search: async function() {
        //const token = await Vue.http.get('/api/geocoding_address_search_token');
        const token = await $.ajax({url: '/api/geocoding_address_search_token/'});
        console.log(token)
        return `https://api.mapbox.com/geocoding/v5/mapbox.places?access_token=${token}`;
    }
    */
    schema_masterlist:"/api/schema_masterlist/",
    schema_masterlist_paginated:"/api/schema_masterlist_paginated/",
    schema_purpose:"/api/schema_purpose/",
    schema_purpose_paginated:"/api/schema_purpose_paginated/",
    schema_group:"/api/schema_group/",
    schema_group_paginated:"/api/schema_group_paginated/",
    schema_question:"/api/schema_question/",
    schema_question_paginated:"/api/schema_question_paginated/",
}

