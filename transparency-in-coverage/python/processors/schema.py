SCHEMA = {
    "root": [
        "root_hash",
        "reporting_entity_name",
        "reporting_entity_type",
        "plan_name",
        "plan_id",
        "plan_id_type",
        "plan_market_type",
        "last_updated_on",
        "version",
        "filename",
        # "url",
    ],
    "codes": [
        "code_hash",
        "negotiation_arrangement",
        "billing_code_type_version",
        "billing_code",
        "billing_code_type",
    ],
    "negotiated_prices": [
        "root_hash",
        "code_hash",
        "negotiated_price_hash",
        "billing_class",
        "negotiated_type",
        "service_code",
        "expiration_date",
        "additional_information",
        "billing_code_modifier",
        "negotiated_rate",
    ],
    "provider_groups": [
        "provider_group_hash",
        "tin_type",
        "tin_value",
        "npi_numbers",
    ],
    "provider_groups_negotiated_prices_link": [
        "provider_group_hash",
        "negotiated_price_hash",
    ]
    # "covered_services": [
    #     "root_hash_key",
    #     "in_network_hash_key",
    #     "billing_code_type_version",
    #     "description",
    #     "billing_code",
    #     "billing_code_type",
    #     "covered_services_hash_key",
    # ],
    # "bundled_codes": [
    #     "root_hash_key",
    #     "in_network_hash_key",
    #     "billing_code_type_version",
    #     "description",
    #     "billing_code",
    #     "billing_code_type",
    # ],
    # "negotiated_rates": [
    #     "root_hash_key",
    #     "in_network_hash_key",
    #     "negotiated_rates_hash_key",
    # ],
}
