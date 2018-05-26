---
title: WFP Structures
description: The Windows Filtering Platform (WFP) API structures are as follows.
ms.assetid: e957132f-417b-40c1-afe3-5aec0e2192f7
keywords:
- Windows Filtering Platform API Enumerated Types
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WFP Structures

The Windows Filtering Platform (WFP) API structures are as follows.

Management Structures

-   [**FWPM\_ACTION0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_action0_?branch=master)
-   [**FWPM\_CALLOUT0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_callout0_?branch=master)
-   [**FWPM\_CALLOUT\_CHANGE0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_callout_change0_?branch=master)
-   [**FWPM\_CALLOUT\_ENUM\_TEMPLATE0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_callout_enum_template0_?branch=master)
-   [**FWPM\_CALLOUT\_SUBSCRIPTION0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_callout_subscription0_?branch=master)
-   [**FWPM\_CLASSIFY\_OPTION0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_classify_option0_?branch=master)
-   [**FWPM\_CLASSIFY\_OPTIONS0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_classify_options0_?branch=master)
-   [**FWPM\_CONNECTION0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_connection0_?branch=master)
-   [**FWPM\_CONNECTION\_ENUM\_TEMPLATE0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_connection_enum_template0_?branch=master)
-   [**FWPM\_CONNECTION\_SUBSCRIPTION0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_connection_subscription0_?branch=master)
-   [**FWPM\_DISPLAY\_DATA0**](/windows/win32/Fwptypes/ns-fwptypes-fwpm_display_data0_?branch=master)
-   [**FWPM\_FIELD0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_field0_?branch=master)
-   [**FWPM\_FILTER0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_filter0_?branch=master)
-   [**FWPM\_FILTER\_CHANGE0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_filter_change0_?branch=master)
-   [**FWPM\_FILTER\_CONDITION0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_filter_condition0_?branch=master)
-   [**FWPM\_FILTER\_ENUM\_TEMPLATE0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_filter_enum_template0_?branch=master)
-   [**FWPM\_FILTER\_SUBSCRIPTION0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_filter_subscription0_?branch=master)
-   [**FWPM\_LAYER0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_layer0_?branch=master)
-   [**FWPM\_LAYER\_ENUM\_TEMPLATE0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_layer_enum_template0_?branch=master)
-   [**FWPM\_LAYER\_STATISTICS0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_layer_statistics0_?branch=master)
-   FWPM\_NET\_EVENT:
    -   [**FWPM\_NET\_EVENT0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_net_event0_?branch=master) (Windows Vista)
    -   [**FWPM\_NET\_EVENT1**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_net_event1_?branch=master) (Windows 7)
    -   [**FWPM\_NET\_EVENT2**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_net_event2_?branch=master) (Windows 8)
-   [**FWPM\_NET\_EVENT\_CAPABILITY\_ALLOW0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_net_event_capability_allow0_?branch=master)
-   [**FWPM\_NET\_EVENT\_CAPABILITY\_DROP0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_net_event_capability_drop0_?branch=master)
-   [**FWPM\_NET\_EVENT\_CLASSIFY\_ALLOW0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_net_event_classify_allow0?branch=master)
-   FWPM\_NET\_EVENT\_CLASSIFY\_DROP:
    -   [**FWPM\_NET\_EVENT\_CLASSIFY\_DROP0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_net_event_classify_drop0_?branch=master) (Windows Vista)
    -   [**FWPM\_NET\_EVENT\_CLASSIFY\_DROP1**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_net_event_classify_drop1_?branch=master) (Windows 7 and later)
    -   [**FWPM\_NET\_EVENT\_CLASSIFY\_DROP2**](/windows/win32/fwpmtypes/ns-fwpmtypes-fwpm_net_event_classify_drop2_?branch=master) (Windows 8)
-   [**FWPM\_NET\_EVENT\_CLASSIFY\_DROP\_MAC0**](/windows/win32/fwpmtypes/ns-fwpmtypes-fwpm_net_event_classify_drop_mac0_?branch=master)
-   [**FWPM\_NET\_EVENT\_ENUM\_TEMPLATE0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_net_event_enum_template0_?branch=master)
-   FWPM\_NET\_EVENT\_HEADER:
    -   [**FWPM\_NET\_EVENT\_HEADER0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_net_event_header0_?branch=master) (Windows Vista)
    -   [**FWPM\_NET\_EVENT\_HEADER1**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_net_event_header1_?branch=master) (Windows 7)
    -   [**FWPM\_NET\_EVENT\_HEADER2**](/windows/win32/fwpmtypes/ns-fwpmtypes-fwpm_net_event_header2_?branch=master) (Windows 8)
-   FWPM\_NET\_EVENT\_IKEEXT\_EM\_FAILURE:
    -   [**FWPM\_NET\_EVENT\_IKEEXT\_EM\_FAILURE0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_net_event_ikeext_em_failure0_?branch=master) (Windows Vista)
    -   [**FWPM\_NET\_EVENT\_IKEEXT\_EM\_FAILURE1**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_net_event_ikeext_em_failure1_?branch=master) (Windows 7 and later)
-   FWPM\_NET\_EVENT\_IKEEXT\_MM\_FAILURE:
    -   [**FWPM\_NET\_EVENT\_IKEEXT\_MM\_FAILURE0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_net_event_ikeext_mm_failure0_?branch=master) (Windows Vista)
    -   [**FWPM\_NET\_EVENT\_IKEEXT\_MM\_FAILURE1**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_net_event_ikeext_mm_failure1_?branch=master) (Windows 7 and later)
-   [**FWPM\_NET\_EVENT\_IKEEXT\_QM\_FAILURE0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_net_event_ikeext_qm_failure0_?branch=master)
-   [**FWPM\_NET\_EVENT\_IPSEC\_DOSP\_DROP0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_net_event_ipsec_dosp_drop0_?branch=master)
-   [**FWPM\_NET\_EVENT\_IPSEC\_KERNEL\_DROP0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_net_event_ipsec_kernel_drop0_?branch=master)
-   [**FWPM\_NET\_EVENT\_SUBSCRIPTION0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_net_event_subscription0_?branch=master)
-   [**FWPM\_PROVIDER0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_provider0_?branch=master)
-   [**FWPM\_PROVIDER\_CHANGE0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_provider_change0_?branch=master)
-   FWPM\_PROVIDER\_CONTEXT:
    -   [**FWPM\_PROVIDER\_CONTEXT0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_provider_context0_?branch=master) (Windows Vista)
    -   [**FWPM\_PROVIDER\_CONTEXT1**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_provider_context1_?branch=master) (Windows 7)
    -   FWPM\_PROVIDER\_CONTEXT2 (Windows 8)
-   [**FWPM\_PROVIDER\_CONTEXT\_CHANGE0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_provider_context_change0_?branch=master)
-   [**FWPM\_PROVIDER\_CONTEXT\_ENUM\_TEMPLATE0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_provider_context_enum_template0_?branch=master)
-   [**FWPM\_PROVIDER\_CONTEXT\_SUBSCRIPTION0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_provider_context_subscription0_?branch=master)
-   [**FWPM\_PROVIDER\_ENUM\_TEMPLATE0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_provider_enum_template0_?branch=master)
-   [**FWPM\_PROVIDER\_SUBSCRIPTION0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_provider_subscription0_?branch=master)
-   [**FWPM\_SESSION0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_session0_?branch=master)
-   [**FWPM\_SESSION\_ENUM\_TEMPLATE0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_session_enum_template0_?branch=master)
-   [**FWPM\_STATISTICS0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_statistics0_?branch=master)
-   [**FWPM\_SUBLAYER0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_sublayer0_?branch=master)
-   [**FWPM\_SUBLAYER\_CHANGE0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_sublayer_change0_?branch=master)
-   [**FWPM\_SUBLAYER\_ENUM\_TEMPLATE0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_sublayer_enum_template0_?branch=master)
-   [**FWPM\_SUBLAYER\_SUBSCRIPTION0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_sublayer_subscription0_?branch=master)
-   [**FWPM\_SYSTEM\_PORTS0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_system_ports0_?branch=master)
-   [**FWPM\_SYSTEM\_PORTS\_BY\_TYPE0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_system_ports_by_type0_?branch=master)
-   [**FWPM\_VSWITCH\_EVENT0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_vswitch_event0_?branch=master)
-   [**FWPM\_VSWITCH\_EVENT\_SUBSCRIPTION0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_vswitch_event_subscription0_?branch=master)

Shared Structures

-   [**FWP\_BYTE\_ARRAY6**](/windows/win32/Fwptypes/ns-fwptypes-fwp_byte_array6_?branch=master)
-   [**FWP\_BYTE\_ARRAY16**](/windows/win32/Fwptypes/ns-fwptypes-fwp_byte_array16_?branch=master)
-   [**FWP\_BYTE\_BLOB**](/windows/win32/Fwptypes/ns-fwptypes-fwp_byte_blob_?branch=master)
-   [**FWP\_CONDITION\_VALUE0**](/windows/win32/Fwptypes/ns-fwptypes-fwp_condition_value0_?branch=master)
-   [**FWP\_RANGE0**](/windows/win32/Fwptypes/ns-fwptypes-fwp_range0_?branch=master)
-   [**FWP\_MATCH\_TYPE**](/windows/win32/Fwptypes/ne-fwptypes-fwp_match_type_?branch=master)
-   [**FWP\_V4\_ADDR\_AND\_MASK**](/windows/win32/Fwptypes/ns-fwptypes-fwp_v4_addr_and_mask_?branch=master)
-   [**FWP\_V6\_ADDR\_AND\_MASK**](/windows/win32/Fwptypes/ns-fwptypes-fwp_v6_addr_and_mask_?branch=master)
-   [**FWP\_VALUE0**](/windows/win32/Fwptypes/ns-fwptypes-fwp_value0_?branch=master)

IKE/AuthIP Structures

-   IKEEXT\_AUTHENTICATION\_METHOD:
    -   [**IKEEXT\_AUTHENTICATION\_METHOD0**](/windows/win32/Iketypes/ns-iketypes-ikeext_authentication_method0_?branch=master) (Windows Vista)
    -   [**IKEEXT\_AUTHENTICATION\_METHOD1**](/windows/win32/Iketypes/ns-iketypes-ikeext_authentication_method1_?branch=master) (Windows 7)
    -   [**IKEEXT\_AUTHENTICATION\_METHOD2**](/windows/win32/iketypes/ns-iketypes-ikeext_authentication_method2_?branch=master) (Windows 8)
-   [**IKEEXT\_CERT\_EKUS0**](/windows/win32/iketypes/ns-iketypes-ikeext_cert_ekus0_?branch=master)
-   [**IKEEXT\_CERT\_NAME0**](/windows/win32/iketypes/ns-iketypes-ikeext_cert_name0_?branch=master)
-   [**IKEEXT\_CERT\_ROOT\_CONFIG0**](/windows/win32/Iketypes/ns-iketypes-ikeext_cert_root_config0_?branch=master)
-   IKEEXT\_CERTIFICATE\_AUTHENTICATION:
    -   [**IKEEXT\_CERTIFICATE\_AUTHENTICATION0**](/windows/win32/Iketypes/ns-iketypes-ikeext_certificate_authentication0_?branch=master) (Windows Vista)
    -   [**IKEEXT\_CERTIFICATE\_AUTHENTICATION1**](/windows/win32/Iketypes/ns-iketypes-ikeext_certificate_authentication1_?branch=master) (Windows 7)
    -   [**IKEEXT\_CERTIFICATE\_AUTHENTICATION2**](/windows/win32/iketypes/ns-iketypes-ikeext_certificate_authentication2_?branch=master) (Windows 8)
-   IKEEXT\_CERTIFICATE\_CREDENTIAL:
    -   [**IKEEXT\_CERTIFICATE\_CREDENTIAL0**](/windows/win32/Iketypes/ns-iketypes-ikeext_certificate_credential0_?branch=master) (Windows Vista)
    -   [**IKEEXT\_CERTIFICATE\_CREDENTIAL1**](/windows/win32/Iketypes/ns-iketypes-ikeext_certificate_credential1_?branch=master) (Windows 7 and later)
-   [**IKEEXT\_CERTIFICATE\_CRITERIA0**](/windows/win32/iketypes/ns-iketypes-ikeext_certificate_criteria0_?branch=master)
-   [**IKEEXT\_CIPHER\_ALGORITHM0**](/windows/win32/Iketypes/ns-iketypes-ikeext_cipher_algorithm0_?branch=master)
-   IKEEXT\_COMMON\_STATISTICS:
    -   [**IKEEXT\_COMMON\_STATISTICS0**](/windows/win32/Iketypes/ns-iketypes-ikeext_common_statistics0_?branch=master) (Windows Vista)
    -   [**IKEEXT\_COMMON\_STATISTICS1**](/windows/win32/Iketypes/ns-iketypes-ikeext_common_statistics1_?branch=master) (Windows 7 and later)
-   [**IKEEXT\_COOKIE\_PAIR0**](/windows/win32/Iketypes/ns-iketypes-ikeext_cookie_pair0_?branch=master)
-   IKEEXT\_CREDENTIAL:
    -   [**IKEEXT\_CREDENTIAL0**](/windows/win32/Iketypes/ns-iketypes-ikeext_credential0_?branch=master) (Windows Vista)
    -   [**IKEEXT\_CREDENTIAL1**](/windows/win32/Iketypes/ns-iketypes-ikeext_credential1_?branch=master) (Windows 7 and later)
-   IKEEXT\_CREDENTIAL\_PAIR:
    -   [**IKEEXT\_CREDENTIAL\_PAIR0**](/windows/win32/Iketypes/ns-iketypes-ikeext_credential_pair0_?branch=master) (Windows Vista)
    -   [**IKEEXT\_CREDENTIAL\_PAIR1**](/windows/win32/Iketypes/ns-iketypes-ikeext_credential_pair1_?branch=master) (Windows 7 and later)
-   IKEEXT\_CREDENTIALS:
    -   [**IKEEXT\_CREDENTIALS0**](/windows/win32/Iketypes/ns-iketypes-ikeext_credentials0_?branch=master) (Windows Vista)
    -   [**IKEEXT\_CREDENTIALS1**](/windows/win32/Iketypes/ns-iketypes-ikeext_credentials1_?branch=master) (Windows 7 and later)
-   [**IKEEXT\_EAP\_AUTHENTICATION0**](/windows/win32/Iketypes/ns-iketypes-ikeext_eap_authentication0__?branch=master)
-   IKEEXT\_EM\_POLICY:
    -   [**IKEEXT\_EM\_POLICY0**](/windows/win32/Iketypes/ns-iketypes-ikeext_em_policy0_?branch=master) (Windows Vista)
    -   [**IKEEXT\_EM\_POLICY1**](/windows/win32/Iketypes/ns-iketypes-ikeext_em_policy1_?branch=master) (Windows 7)
    -   [**IKEEXT\_EM\_POLICY2**](/windows/win32/iketypes/ns-iketypes-ikeext_em_policy2_?branch=master) (Windows 8)
-   [**IKEEXT\_INTEGRITY\_ALGORITHM0**](/windows/win32/Iketypes/ns-iketypes-ikeext_integrity_algorithm0_?branch=master)
-   IKEEXT\_IP\_VERSION\_SPECIFIC\_COMMON\_STATISTICS:
    -   [**IKEEXT\_IP\_VERSION\_SPECIFIC\_COMMON\_STATISTICS0**](/windows/win32/Iketypes/ns-iketypes-ikeext_ip_version_specific_common_statistics0_?branch=master) (Windows Vista)
    -   [**IKEEXT\_IP\_VERSION\_SPECIFIC\_COMMON\_STATISTICS1**](/windows/win32/Iketypes/ns-iketypes-ikeext_ip_version_specific_common_statistics1_?branch=master) (Windows 7 and later)
-   IKEEXT\_IP\_VERSION\_SPECIFIC\_KEYMODULE\_STATISTICS:
    -   [**IKEEXT\_IP\_VERSION\_SPECIFIC\_KEYMODULE\_STATISTICS0**](/windows/win32/Iketypes/ns-iketypes-ikeext_ip_version_specific_keymodule_statistics0_?branch=master) (Windows Vista)
    -   [**IKEEXT\_IP\_VERSION\_SPECIFIC\_KEYMODULE\_STATISTICS1**](/windows/win32/Iketypes/ns-iketypes-ikeext_ip_version_specific_keymodule_statistics1_?branch=master) (Windows 7 and later)
-   [**IKEEXT\_IPV6\_CGA\_AUTHENTICATION0**](/windows/win32/Iketypes/ns-iketypes-ikeext_ipv6_cga_authentication0_?branch=master)
-   IKEEXT\_KEYMODULE\_STATISTICS:
    -   [**IKEEXT\_KERBEROS\_AUTHENTICATION0**](/windows/win32/Iketypes/ns-iketypes-ikeext_kerberos_authentication0__?branch=master) (Windows Vista and Windows 7)
    -   [**IKEEXT\_KERBEROS\_AUTHENTICATION1**](/windows/win32/iketypes/ns-iketypes-ikeext_kerberos_authentication1__?branch=master) (Windows 8)
-   -   IKEEXT\_KEYMODULE\_STATISTICS:
    -   [**IKEEXT\_KEYMODULE\_STATISTICS0**](/windows/win32/Iketypes/ns-iketypes-ikeext_keymodule_statistics0_?branch=master) (Windows Vista)
    -   [**IKEEXT\_KEYMODULE\_STATISTICS1**](/windows/win32/Iketypes/ns-iketypes-ikeext_keymodule_statistics1_?branch=master) (Windows 7 and later)
-   [**IKEEXT\_NAME\_CREDENTIAL0**](/windows/win32/Iketypes/ns-iketypes-ikeext_name_credential0_?branch=master)
-   [**IKEEXT\_NTLM\_V2\_AUTHENTICATION0**](/windows/win32/Iketypes/ns-iketypes-ikeext_ntlm_v2_authentication0__?branch=master)
-   IKEEXT\_POLICY:
    -   [**IKEEXT\_POLICY0**](/windows/win32/Iketypes/ns-iketypes-ikeext_policy0_?branch=master) (Windows Vista)
    -   [**IKEEXT\_POLICY1**](/windows/win32/Iketypes/ns-iketypes-ikeext_policy1_?branch=master) (Windows 7)
    -   [**IKEEXT\_POLICY2**](/windows/win32/iketypes/ns-iketypes-ikeext_policy2_?branch=master) (Windows 8)
-   IKEEXT\_PRESHARED\_KEY\_AUTHENTICATION:
    -   [**IKEEXT\_PRESHARED\_KEY\_AUTHENTICATION0**](/windows/win32/Iketypes/ns-iketypes-ikeext_preshared_key_authentication0__?branch=master) (Windows Vista)
    -   [**IKEEXT\_PRESHARED\_KEY\_AUTHENTICATION1**](/windows/win32/Iketypes/ns-iketypes-ikeext_preshared_key_authentication1__?branch=master) (Windows 7 and later)
-   [**IKEEXT\_PROPOSAL0**](/windows/win32/Iketypes/ns-iketypes-ikeext_proposal0_?branch=master)
-   [**IKEEXT\_RESERVED\_AUTHENTICATION0**](/windows/win32/Iketypes/ns-iketypes-ikeext_reserved_authentication0__?branch=master)
-   IKEEXT\_SA\_DETAILS:
    -   [**IKEEXT\_SA\_DETAILS0**](/windows/win32/Iketypes/ns-iketypes-ikeext_sa_details0_?branch=master) (Windows Vista)
    -   [**IKEEXT\_SA\_DETAILS1**](/windows/win32/Iketypes/ns-iketypes-ikeext_sa_details1_?branch=master) (Windows 7 and later)
-   [**IKEEXT\_SA\_ENUM\_TEMPLATE0**](/windows/win32/Iketypes/ns-iketypes-ikeext_sa_enum_template0_?branch=master)
-   IKEEXT\_STATISTICS:
    -   [**IKEEXT\_STATISTICS0**](/windows/win32/Iketypes/ns-iketypes-ikeext_statistics0_?branch=master) (Windows Vista)
    -   [**IKEEXT\_STATISTICS1**](/windows/win32/Iketypes/ns-iketypes-ikeext_statistics1_?branch=master) (Windows 7 and later)
-   [**IKEEXT\_TRAFFIC0**](/windows/win32/Iketypes/ns-iketypes-ikeext_traffic0_?branch=master)

IPsec Structures

-   [**IPSEC\_ADDRESS\_INFO0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_address_info0_?branch=master)
-   IPSEC\_AGGREGATE\_DROP\_PACKET\_STATISTICS:
    -   [**IPSEC\_AGGREGATE\_DROP\_PACKET\_STATISTICS0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_aggregate_drop_packet_statistics0_?branch=master) (Windows Vista)
    -   [**IPSEC\_AGGREGATE\_DROP\_PACKET\_STATISTICS1**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_aggregate_drop_packet_statistics1_?branch=master) (Windows 7 and later)
-   [**IPSEC\_AGGREGATE\_SA\_STATISTICS0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_aggregate_sa_statistics0_?branch=master)
-   [**IPSEC\_AH\_DROP\_PACKET\_STATISTICS0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_ah_drop_packet_statistics0_?branch=master)
-   [**IPSEC\_AUTH\_AND\_CIPHER\_TRANSFORM0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_auth_and_cipher_transform0_?branch=master)
-   [**IPSEC\_AUTH\_TRANSFORM0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_auth_transform0_?branch=master)
-   [**IPSEC\_AUTH\_TRANSFORM\_ID0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_auth_transform_id0_?branch=master)
-   [**IPSEC\_CIPHER\_TRANSFORM0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_cipher_transform0_?branch=master)
-   [**IPSEC\_CIPHER\_TRANSFORM\_ID0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_cipher_transform_id0_?branch=master)
-   [**IPSEC\_DOSP\_OPTIONS0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_dosp_options0_?branch=master)
-   [**IPSEC\_DOSP\_STATE0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_dosp_state0_?branch=master)
-   [**IPSEC\_DOSP\_STATE\_ENUM\_TEMPLATE0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_dosp_state_enum_template0_?branch=master)
-   [**IPSEC\_DOSP\_STATISTICS0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_dosp_statistics0_?branch=master)
-   [**IPSEC\_ESP\_DROP\_PACKET\_STATISTICS0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_esp_drop_packet_statistics0_?branch=master)
-   IPSEC\_GETSPI:
    -   [**IPSEC\_GETSPI0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_getspi0_?branch=master) (Windows Vista)
    -   [**IPSEC\_GETSPI1**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_getspi1_?branch=master) (Windows 7 and later)
-   [**IPSEC\_ID0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_id0_?branch=master)
-   [**IPSEC\_KEY\_MANAGER0**](/windows/win32/ipsectypes/ns-ipsectypes-_ipsec_key_manager0?branch=master)
-   [**IPSEC\_KEY\_MANAGER\_CALLBACKS0**](/windows/win32/fwpmu/ns-fwpmu-_ipsec_key_manager_callbacks0?branch=master)
-   IPSEC\_KEYING\_POLICY:
    -   [**IPSEC\_KEYING\_POLICY0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_keying_policy0_?branch=master) (Windows Vista and Windows 7)
    -   [**IPSEC\_KEYING\_POLICY1**](/windows/win32/ipsectypes/ns-ipsectypes-ipsec_keying_policy1_?branch=master) (Windows 8)
-   [**IPSEC\_KEYMODULE\_STATE0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_keymodule_state0_?branch=master)
-   [**IPSEC\_PROPOSAL0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_proposal0_?branch=master)
-   [**IPSEC\_SA0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_sa0_?branch=master)
-   [**IPSEC\_SA\_AUTH\_AND\_CIPHER\_INFORMATION0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_sa_auth_and_cipher_information0_?branch=master)
-   [**IPSEC\_SA\_AUTH\_INFORMATION0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_sa_auth_information0_?branch=master)
-   IPSEC\_SA\_BUNDLE:
    -   [**IPSEC\_SA\_BUNDLE0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_sa_bundle0_?branch=master) (Windows Vista)
    -   [**IPSEC\_SA\_BUNDLE1**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_sa_bundle1_?branch=master) (Windows 7 and later)
-   [**IPSEC\_SA\_CIPHER\_INFORMATION0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_sa_cipher_information0_?branch=master)
-   IPSEC\_SA\_CONTEXT:
    -   [**IPSEC\_SA\_CONTEXT0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_sa_context0_?branch=master) (Windows Vista)
    -   [**IPSEC\_SA\_CONTEXT1**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_sa_context1_?branch=master) (Windows 7 and later)
-   [**IPSEC\_SA\_CONTEXT\_CHANGE0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_sa_context_change0_?branch=master)
-   [**IPSEC\_SA\_CONTEXT ENUM\_TEMPLATE0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_sa_context_enum_template0_?branch=master)
-   [**IPSEC\_SA\_CONTEXT\_SUBSCRIPTION0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_sa_context_subscription0_?branch=master)
-   IPSEC\_SA\_DETAILS:
    -   [**IPSEC\_SA\_DETAILS0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_sa_details0_?branch=master) (Windows Vista)
    -   [**IPSEC\_SA\_DETAILS1**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_sa_details1_?branch=master) (Windows 7 and later)
-   [**IPSEC\_SA\_ENUM\_TEMPLATE0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_sa_enum_template0_?branch=master)
-   [**IPSEC\_SA\_IDLE\_TIMEOUT0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_sa_idle_timeout0_?branch=master)
-   [**IPSEC\_SA\_LIFETIME0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_sa_lifetime0_?branch=master)
-   [**IPSEC\_SA\_TRANSFORM0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_sa_transform0_?branch=master)
-   IPSEC\_STATISTICS:
    -   [**IPSEC\_STATISTICS0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_statistics0_?branch=master) (Windows Vista)
    -   [**IPSEC\_STATISTICS1**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_statistics1_?branch=master) (Windows 7 and later)
-   [**IPSEC\_TOKEN0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_token0_?branch=master)
-   IPSEC\_TRAFFIC:
    -   [**IPSEC\_TRAFFIC0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_traffic0_?branch=master) (Windows Vista)
    -   [**IPSEC\_TRAFFIC1**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_traffic1_?branch=master) (Windows 7 and later)
-   IPSEC\_TRAFFIC\_STATISTICS:
    -   [**IPSEC\_TRAFFIC\_STATISTICS0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_traffic_statistics0_?branch=master) (Windows Vista)
    -   [**IPSEC\_TRAFFIC\_STATISTICS1**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_traffic_statistics1_?branch=master) (Windows 7 and later)
-   IPSEC\_TRANSPORT\_POLICY:
    -   [**IPSEC\_TRANSPORT\_POLICY0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_transport_policy0_?branch=master) (Windows Vista)
    -   [**IPSEC\_TRANSPORT\_POLICY1**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_transport_policy1_?branch=master) (Windows 7)
    -   [**IPSEC\_TRANSPORT\_POLICY2**](/windows/win32/ipsectypes/ns-ipsectypes-ipsec_transport_policy2_?branch=master) (Windows 8)
-   [**IPSEC\_TUNNEL\_ENDPOINT0**](/windows/win32/ipsectypes/ns-ipsectypes-ipsec_tunnel_endpoint0_?branch=master)
-   IPSEC\_TUNNEL\_ENDPOINTS:
    -   [**IPSEC\_TUNNEL\_ENDPOINTS0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_tunnel_endpoints0_?branch=master) (Windows Vista)
    -   [**IPSEC\_TUNNEL\_ENDPOINTS1**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_tunnel_endpoints1_?branch=master) (Windows 7)
    -   [**IPSEC\_TUNNEL\_ENDPOINTS2**](/windows/win32/ipsectypes/ns-ipsectypes-ipsec_tunnel_endpoints2_?branch=master) (Windows 8)
-   IPSEC\_TUNNEL\_POLICY:
    -   [**IPSEC\_TUNNEL\_POLICY0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_tunnel_policy0_?branch=master) (Windows Vista)
    -   [**IPSEC\_TUNNEL\_POLICY1**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_tunnel_policy1_?branch=master) (Windows 7)
    -   [**IPSEC\_TUNNEL\_POLICY2**](/windows/win32/ipsectypes/ns-ipsectypes-ipsec_tunnel_policy2_?branch=master) (Windows 8)
-   [**IPSEC\_V4\_UDP\_ENCAPSULATION0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_v4_udp_encapsulation0_?branch=master)
-   [**IPSEC\_VIRTUAL\_IF\_TUNNEL\_INFO0**](/windows/win32/fwptypes/ns-fwptypes-ipsec_virtual_if_tunnel_info0_?branch=master)

 

 




