---
title: What's New in Windows Filtering Platform
description: Windows 8 and Windows Server 2012 introduce new Windows Filtering Platform programming elements.
ms.assetid: 7529F155-3DBC-4C22-A780-B6311C455E85
ms.topic: article
ms.date: 05/31/2018
---

# What's New in Windows Filtering Platform

Windows 8 and Windows Server 2012 introduce new Windows Filtering Platform programming elements. New functionality includes the following:

-   *Layer 2 filtering*: Provides access to the L2 (MAC) layer, allowing filtering of traffic at that layer.
-   *vSwitch filtering*: Allows packets traversing a vSwitch to be inspected and/or modified. WFP filters or callouts can be used at the vSwitch ingress and egress.
-   *App container management*: Allows access to information about app containers and network isolation connectivity issues.
-   *IPsec updates*: Extended IPsec functionality including connection state monitoring, certificate selection, and key management.

The Windows Driver Kit also includes information on [WFP Changes for Windows 8](/windows-hardware/drivers/network/wfp-changes-for-windows-8).

## Windows 8 API updates

Many new APIs have been added for Windows 8 and Windows Server 2012.

## New functions

-   [**FWPM\_NET\_EVENT\_CALLBACK1**](/windows/desktop/api/fwpmu/nc-fwpmu-fwpm_net_event_callback1)
-   [**FwpmConnectionCreateEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmconnectioncreateenumhandle0)
-   [**FwpmConnectionDestroyEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmconnectiondestroyenumhandle0)
-   [**FwpmConnectionEnum0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmconnectionenum0)
-   [**FwpmConnectionGetById0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmconnectiongetbyid0)
-   [**FwpmConnectionGetSecurityInfo0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmconnectiongetsecurityinfo0)
-   [**FwpmConnectionSetSecurityInfo0**](/windows/desktop/api/fwpmu/nf-fwpmu-fwpmconnectionsetsecurityinfo0)
-   [**FwpmConnectionSubscribe0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmconnectionsubscribe0)
-   [**FwpmConnectionSubscriptionsGet0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmconnectionsubscriptionsget0)
-   [**FwpmConnectionUnsubscribe0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmconnectionunsubscribe0)
-   [**FwpmIPsecTunnelAdd2**](/windows/desktop/api/fwpmu/nf-fwpmu-fwpmipsectunneladd2)
-   [**FwpmNetEventEnum2**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmneteventenum2)
-   [**FwpmNetEventSubscribe1**](/windows/desktop/api/fwpmu/nf-fwpmu-fwpmneteventsubscribe1)
-   [**FwpmProviderContextAdd2**](/windows/desktop/api/fwpmu/nf-fwpmu-fwpmprovidercontextadd2)
-   [**FwpmProviderContextEnum2**](/windows/desktop/api/fwpmu/nf-fwpmu-fwpmprovidercontextenum2)
-   [**FwpmProviderContextGetById2**](/windows/desktop/api/fwpmu/nf-fwpmu-fwpmprovidercontextgetbyid2)
-   [**FwpmProviderContextGetByKey2**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmprovidercontextgetbykey2)
-   [**FwpmvSwitchEventsGetSecurityInfo0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmvswitcheventsgetsecurityinfo0)
-   [**FwpmvSwitchEventsSetSecurityInfo0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmvswitcheventssetsecurityinfo0)
-   [**FwpmvSwitchEventSubscribe0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmvswitcheventsubscribe0)
-   [**FwpmvSwitchEventUnsubscribe0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmvswitcheventunsubscribe0)
-   [**IkeextSaEnum2**](/windows/desktop/api/Fwpmu/nf-fwpmu-ikeextsaenum2)
-   [**IkeextSaGetById2**](/windows/desktop/api/Fwpmu/nf-fwpmu-ikeextsagetbyid2)
-   [**IPSEC\_KEY\_MANAGER\_KEY\_DICTATION\_CHECK0**](/windows/desktop/api/Fwpmu/nc-fwpmu-ipsec_key_manager_key_dictation_check0)
-   [**IPSEC\_KEY\_MANAGER\_DICTATE\_KEY0**](/windows/desktop/api/Fwpmu/nc-fwpmu-ipsec_key_manager_dictate_key0)
-   [**IPSEC\_KEY\_MANAGER\_NOTIFY\_KEY0**](/windows/desktop/api/fwpmu/nc-fwpmu-ipsec_key_manager_notify_key0)
-   [**IPSEC\_SA\_CONTEXT\_CALLBACK0**](/windows/win32/api/fwpmu/nc-fwpmu-ipsec_sa_context_callback0)
-   [**IPsecKeyManagerAddAndRegister0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipseckeymanageraddandregister0)
-   [**IPsecKeyManagerGetSecurityInfoByKey0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipseckeymanagergetsecurityinfobykey0)
-   [**IPsecKeyManagerSetSecurityInfoByKey0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipseckeymanagersetsecurityinfobykey0)
-   [**IPsecKeyManagersGet0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipseckeymanagersget0)
-   [**IPsecKeyManagerUnregisterAndDelete0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipseckeymanagerunregisteranddelete0)
-   [**IPsecSaContextSubscribe0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextsubscribe0)
-   [**IPsecSaContextSubscriptionsGet0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextsubscriptionsget0)
-   [**IPsecSaContextUnsubscribe0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextunsubscribe0)
-   [**NetworkIsolationDiagnoseConnectFailureAndGetInfo**](/previous-versions/windows/desktop/api/netfw/nf-netfw-networkisolationdiagnoseconnectfailureandgetinfo)
-   [**NetworkIsolationEnumAppContainers**](/previous-versions/windows/desktop/api/netfw/nf-netfw-networkisolationenumappcontainers)
-   [**NetworkIsolationEnumerateAppContainerRules**](/previous-versions/windows/desktop/api/netfw/nf-netfw-networkisolationenumerateappcontainerrules)
-   [**NetworkIsolationFreeAppContainers**](/previous-versions/windows/desktop/api/netfw/nf-netfw-networkisolationfreeappcontainers)
-   [**NetworkIsolationGetAppContainerConfig**](/windows/desktop/api/networkisolation/nf-networkisolation-networkisolationgetappcontainerconfig)
-   [**NetworkIsolationRegisterForAppContainerChanges**](/previous-versions/windows/desktop/api/netfw/nf-netfw-networkisolationregisterforappcontainerchanges)
-   [**NetworkIsolationSetAppContainerConfig**](/previous-versions/windows/desktop/api/netfw/nf-netfw-networkisolationsetappcontainerconfig)
-   [**NetworkIsolationSetupAppContainerBinaries**](/windows/desktop/api/networkisolation/nf-networkisolation-networkisolationsetupappcontainerbinaries)
-   [**PAC\_CHANGES\_CALLBACK\_FN**](/windows/desktop/api/networkisolation/nc-networkisolation-pac_changes_callback_fn)

## New structures

-   [**IKEEXT\_AUTHENTICATION\_METHOD2**](/windows/win32/api/iketypes/ns-iketypes-ikeext_authentication_method2)
-   [**IKEEXT\_CERT\_EKUS0**](/windows/win32/api/iketypes/ns-iketypes-ikeext_cert_ekus0)
-   [**IKEEXT\_CERT\_NAME0**](/windows/win32/api/iketypes/ns-iketypes-ikeext_cert_name0)
-   [**IKEEXT\_CERTIFICATE\_AUTHENTICATION2**](/windows/win32/api/iketypes/ns-iketypes-ikeext_certificate_authentication2)
-   [**IKEEXT\_CERTIFICATE\_CRITERIA0**](/windows/win32/api/iketypes/ns-iketypes-ikeext_certificate_criteria0)
-   [**IKEEXT\_EM\_POLICY2**](/windows/win32/api/iketypes/ns-iketypes-ikeext_em_policy2)
-   [**IKEEXT\_KERBEROS\_AUTHENTICATION1**](/windows/win32/api/iketypes/ns-iketypes-ikeext_kerberos_authentication1)
-   [**IKEEXT\_POLICY2**](/windows/win32/api/iketypes/ns-iketypes-ikeext_policy2)
-   [**IPSEC\_KEY\_MANAGER0**](/windows/desktop/api/ipsectypes/ns-ipsectypes-ipsec_key_manager0)
-   [**IPSEC\_KEY\_MANAGER\_CALLBACKS0**](/windows/desktop/api/fwpmu/ns-fwpmu-ipsec_key_manager_callbacks0)
-   [**IPSEC\_KEYING\_POLICY1**](/windows/win32/api/ipsectypes/ns-ipsectypes-ipsec_keying_policy1)
-   [**IPSEC\_SA\_CONTEXT\_CHANGE0**](/windows/desktop/api/Ipsectypes/ns-ipsectypes-ipsec_sa_context_change0)
-   [**IPSEC\_SA\_CONTEXT\_SUBSCRIPTION0**](/windows/desktop/api/Ipsectypes/ns-ipsectypes-ipsec_sa_context_subscription0)
-   [**IPSEC\_TRANSPORT\_POLICY2**](/windows/win32/api/ipsectypes/ns-ipsectypes-ipsec_transport_policy2)
-   [**IPSEC\_TUNNEL\_ENDPOINT0**](/windows/win32/api/ipsectypes/ns-ipsectypes-ipsec_tunnel_endpoint0)
-   [**IPSEC\_TUNNEL\_ENDPOINTS2**](/windows/win32/api/ipsectypes/ns-ipsectypes-ipsec_tunnel_endpoints2)
-   [**IPSEC\_TUNNEL\_POLICY2**](/windows/win32/api/ipsectypes/ns-ipsectypes-ipsec_tunnel_policy2)
-   [**FWPM\_CONNECTION0**](/windows/desktop/api/Fwpmtypes/ns-fwpmtypes-fwpm_connection0)
-   [**FWPM\_CONNECTION\_ENUM\_TEMPLATE0**](/windows/desktop/api/Fwpmtypes/ns-fwpmtypes-fwpm_connection_enum_template0)
-   [**FWPM\_CONNECTION\_SUBSCRIPTION0**](/windows/desktop/api/Fwpmtypes/ns-fwpmtypes-fwpm_connection_subscription0)
-   [**FWPM\_NET\_EVENT2**](/windows/desktop/api/Fwpmtypes/ns-fwpmtypes-fwpm_net_event2)
-   [**FWPM\_NET\_EVENT\_CAPABILITY\_ALLOW0**](/windows/desktop/api/Fwpmtypes/ns-fwpmtypes-fwpm_net_event_capability_allow0)
-   [**FWPM\_NET\_EVENT\_CAPABILITY\_DROP0**](/windows/desktop/api/Fwpmtypes/ns-fwpmtypes-fwpm_net_event_capability_drop0)
-   [**FWPM\_NET\_EVENT\_CLASSIFY\_ALLOW0**](/windows/desktop/api/Fwpmtypes/ns-fwpmtypes-fwpm_net_event_classify_allow0)
-   [**FWPM\_NET\_EVENT\_CLASSIFY\_DROP2**](/windows/win32/api/fwpmtypes/ns-fwpmtypes-fwpm_net_event_classify_drop2)
-   [**FWPM\_NET\_EVENT\_CLASSIFY\_DROP\_MAC0**](/windows/win32/api/fwpmtypes/ns-fwpmtypes-fwpm_net_event_classify_drop_mac0)
-   [**FWPM\_NET\_EVENT\_HEADER2**](/windows/win32/api/fwpmtypes/ns-fwpmtypes-fwpm_net_event_header2)
-   [**FWPM\_PROVIDER\_CONTEXT2**](/windows/win32/api/fwpmtypes/ns-fwpmtypes-fwpm_provider_context2)
-   [**FWPM\_VSWITCH\_EVENT0**](/windows/desktop/api/Fwpmtypes/ns-fwpmtypes-fwpm_vswitch_event0)
-   [**FWPM\_VSWITCH\_EVENT\_SUBSCRIPTION0**](/windows/desktop/api/Fwpmtypes/ns-fwpmtypes-fwpm_vswitch_event_subscription0)

## New enumerated types

-   [**FWP\_VSWITCH\_NETWORK\_TYPE**](/windows/win32/api/fwptypes/ne-fwptypes-fwp_vswitch_network_type)
-   [**FWPM\_APPC\_NETWORK\_CAPABILITY\_TYPE**](/windows/desktop/api/Fwpmtypes/ne-fwpmtypes-fwpm_appc_network_capability_type)
-   [**FWPM\_CONNECTION\_EVENT\_TYPE**](/windows/desktop/api/Fwpmtypes/ne-fwpmtypes-fwpm_connection_event_type)
-   [**FWPM\_VSWITCH\_EVENT\_TYPE**](/windows/desktop/api/Fwpmtypes/ne-fwpmtypes-fwpm_vswitch_event_type)
-   [**IKEEXT\_CERT\_CRITERIA\_NAME\_TYPE**](/windows/win32/api/iketypes/ne-iketypes-ikeext_cert_criteria_name_type)
-   [**IPSEC\_SA\_CONTEXT\_EVENT\_TYPE0**](/windows/desktop/api/Ipsectypes/ne-ipsectypes-ipsec_sa_context_event_type0)

## New filtering layer identifiers

[**Filtering Layer Identifiers:**](management-filtering-layer-identifiers-.md)

-   FWPM\_LAYER\_INBOUND\_MAC\_FRAME\_ETHERNET
-   FWPM\_LAYER\_OUTBOUND\_MAC\_FRAME\_ETHERNET
-   FWPM\_LAYER\_INBOUND\_MAC\_FRAME\_NATIVE
-   FWPM\_LAYER\_OUTBOUND\_MAC\_FRAME\_NATIVE
-   FWPM\_LAYER\_INGRESS\_VSWITCH\_ETHERNET
-   FWPM\_LAYER\_EGRESS\_VSWITCH\_ETHERNET
-   FWPM\_LAYER\_INGRESS\_VSWITCH\_TRANSPORT\_V4 / FWPM\_LAYER\_INGRESS\_VSWITCH\_TRANSPORT\_V6
-   FWPM\_LAYER\_EGRESS\_VSWITCH\_TRANSPORT\_V4 / FWPM\_LAYER\_EGRESS\_VSWITCH\_TRANSPORT\_V6

## New filtering condition identifiers

[**Filtering Condition Identifiers:**](filtering-condition-identifiers-.md)

-   FWPM\_CONDITION\_INTERFACE\_MAC\_ADDRESS
-   FWPM\_CONDITION\_MAC\_LOCAL\_ADDRESS
-   FWPM\_CONDITION\_MAC\_REMOTE\_ADDRESS
-   FWPM\_CONDITION\_ETHER\_TYPE
-   FWPM\_CONDITION\_VLAN\_ID
-   FWPM\_CONDITION\_NDIS\_PORT
-   FWPM\_CONDITION\_NDIS\_MEDIA\_TYPE
-   FWPM\_CONDITION\_NDIS\_PHYSICAL\_MEDIA\_TYPE
-   FWPM\_CONDITION\_L2\_FLAGS
-   FWPM\_CONDITION\_MAC\_LOCAL\_ADDRESS\_TYPE
-   FWPM\_CONDITION\_MAC\_REMOTE\_ADDRESS\_TYPE
-   FWPM\_CONDITION\_ALE\_PACKAGE\_ID
-   FWPM\_CONDITION\_MAC\_SOURCE\_ADDRESS
-   FWPM\_CONDITION\_MAC\_DESTINATION\_ADDRESS
-   FWPM\_CONDITION\_MAC\_SOURCE\_ADDRESS\_TYPE
-   FWPM\_CONDITION\_MAC\_DESTINATION\_ADDRESS\_TYPE
-   FWPM\_CONDITION\_IP\_SOURCE\_PORT
-   FWPM\_CONDITION\_IP\_DESTINATION\_PORT
-   FWPM\_CONDITION\_VSWITCH\_ID
-   FWPM\_CONDITION\_VSWITCH\_NETWORK\_TYPE
-   FWPM\_CONDITION\_VSWITCH\_SOURCE\_INTERFACE\_ID
-   FWPM\_CONDITION\_VSWITCH\_DESTINATION\_INTERFACE\_ID
-   FWPM\_CONDITION\_VSWITCH\_SOURCE\_VM\_ID
-   FWPM\_CONDITION\_VSWITCH\_DESTINATION\_VM\_ID
-   FWPM\_CONDITION\_VSWITCH\_SOURCE\_INTERFACE\_TYPE
-   FWPM\_CONDITION\_VSWITCH\_TENANT\_NETWORK\_ID

## New filtering condition flags

[**Filtering Condition Flags:**](filtering-condition-flags-.md)

-   FWP\_CONDITION\_FLAG\_IS\_PROXY\_CONNECTION
-   FWP\_CONDITION\_FLAG\_IS\_APPCONTAINER\_LOOPBACK
-   FWP\_CONDITION\_FLAG\_IS\_NON\_APPCONTAINER\_LOOPBACK
-   FWP\_CONDITION\_FLAG\_IS\_HONORING\_POLICY\_AUTHORIZE
-   FWP\_CONDITION\_L2\_IS\_NATIVE\_ETHERNET
-   FWP\_CONDITION\_L2\_IS\_WIFI
-   FWP\_CONDITION\_L2\_IS\_MOBILE\_BROADBAND
-   FWP\_CONDITION\_L2\_IS\_WIFI\_DIRECT\_DATA
-   FWP\_CONDITION\_L2\_IS\_VM2VM
-   FWP\_CONDITION\_L2\_IS\_MALFORMED\_PACKET
-   FWP\_CONDITION\_L2\_IS\_IP\_FRAGMENT\_GROUP
-   FWP\_CONDITION\_L2\_IF\_CONNECTOR\_PRESENT

## Windows 7 updates to the Windows Filtering Platform

The document [What's New in Windows Filtering Platform]() details many of the updates made for Windows 7. Information is also available in the Windows Driver Kit on [WFP Changes for Windows 7](/windows-hardware/drivers/network/wfp-changes-for-windows-7).

 

 