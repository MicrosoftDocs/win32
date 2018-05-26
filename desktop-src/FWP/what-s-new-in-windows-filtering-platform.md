---
title: Whats New in Windows Filtering Platform
description: Windows 8 and Windows Server 2012 introduce new Windows Filtering Platform programming elements.
ms.assetid: 7529F155-3DBC-4C22-A780-B6311C455E85
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# What's New in Windows Filtering Platform

Windows 8 and Windows Server 2012 introduce new Windows Filtering Platform programming elements. New functionality includes the following:

-   *Layer 2 filtering*: Provides access to the L2 (MAC) layer, allowing filtering of traffic at that layer.
-   *vSwitch filtering*: Allows packets traversing a vSwitch to be inspected and/or modified. WFP filters or callouts can be used at the vSwitch ingress and egress.
-   *App container management*: Allows access to information about app containers and network isolation connectivity issues.
-   *IPsec updates*: Extended IPsec functionality including connection state monitoring, certificate selection, and key management.

The Windows Driver Kit also includes information on [WFP Changes for Windows 8](http://go.microsoft.com/fwlink/p/?LinkId=262707).

## Windows 8 API updates

Many new APIs have been added for Windows 8 and Windows Server 2012.

## New functions

-   [**FWPM\_NET\_EVENT\_CALLBACK1**](/windows/win32/fwpmu/nc-fwpmu-fwpm_net_event_callback1?branch=master)
-   [**FwpmConnectionCreateEnumHandle0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmconnectioncreateenumhandle0?branch=master)
-   [**FwpmConnectionDestroyEnumHandle0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmconnectiondestroyenumhandle0?branch=master)
-   [**FwpmConnectionEnum0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmconnectionenum0?branch=master)
-   [**FwpmConnectionGetById0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmconnectiongetbyid0?branch=master)
-   [**FwpmConnectionGetSecurityInfo0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmconnectiongetsecurityinfo0?branch=master)
-   [**FwpmConnectionSetSecurityInfo0**](/windows/win32/fwpmu/nf-fwpmu-fwpmconnectionsetsecurityinfo0?branch=master)
-   [**FwpmConnectionSubscribe0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmconnectionsubscribe0?branch=master)
-   [**FwpmConnectionSubscriptionsGet0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmconnectionsubscriptionsget0?branch=master)
-   [**FwpmConnectionUnsubscribe0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmconnectionunsubscribe0?branch=master)
-   [**FwpmIPsecTunnelAdd2**](/windows/win32/fwpmu/nf-fwpmu-fwpmipsectunneladd2?branch=master)
-   [**FwpmNetEventEnum2**](/windows/win32/Fwpmu/nf-fwpmu-fwpmneteventenum2?branch=master)
-   [**FwpmNetEventSubscribe1**](/windows/win32/fwpmu/nf-fwpmu-fwpmneteventsubscribe1?branch=master)
-   [**FwpmProviderContextAdd2**](/windows/win32/fwpmu/nf-fwpmu-fwpmprovidercontextadd2?branch=master)
-   [**FwpmProviderContextEnum2**](/windows/win32/fwpmu/nf-fwpmu-fwpmprovidercontextenum2?branch=master)
-   [**FwpmProviderContextGetById2**](/windows/win32/fwpmu/nf-fwpmu-fwpmprovidercontextgetbyid2?branch=master)
-   [**FwpmProviderContextGetByKey2**](/windows/win32/Fwpmu/nf-fwpmu-fwpmprovidercontextgetbykey2?branch=master)
-   [**FwpmvSwitchEventsGetSecurityInfo0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmvswitcheventsgetsecurityinfo0?branch=master)
-   [**FwpmvSwitchEventsSetSecurityInfo0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmvswitcheventssetsecurityinfo0?branch=master)
-   [**FwpmvSwitchEventSubscribe0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmvswitcheventsubscribe0?branch=master)
-   [**FwpmvSwitchEventUnsubscribe0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmvswitcheventunsubscribe0?branch=master)
-   [**IkeextSaEnum2**](/windows/win32/Fwpmu/nf-fwpmu-ikeextsaenum2?branch=master)
-   [**IkeextSaGetById2**](/windows/win32/Fwpmu/nf-fwpmu-ikeextsagetbyid2?branch=master)
-   [**IPSEC\_KEY\_MANAGER\_KEY\_DICTATION\_CHECK0**](/windows/win32/Fwpmu/nc-fwpmu-ipsec_key_manager_key_dictation_check0?branch=master)
-   [**IPSEC\_KEY\_MANAGER\_DICTATE\_KEY0**](/windows/win32/Fwpmu/nc-fwpmu-ipsec_key_manager_dictate_key0?branch=master)
-   [**IPSEC\_KEY\_MANAGER\_NOTIFY\_KEY0**](/windows/win32/fwpmu/nc-fwpmu-ipsec_key_manager_notify_key0?branch=master)
-   [**IPSEC\_SA\_CONTEXT\_CALLBACK0**](/windows/win32/fwpmu/nc-fwpmu-ipsec_sa_context_callback0?branch=master)
-   [**IPsecKeyManagerAddAndRegister0**](/windows/win32/Fwpmu/nf-fwpmu-ipseckeymanageraddandregister0?branch=master)
-   [**IPsecKeyManagerGetSecurityInfoByKey0**](/windows/win32/Fwpmu/nf-fwpmu-ipseckeymanagergetsecurityinfobykey0?branch=master)
-   [**IPsecKeyManagerSetSecurityInfoByKey0**](/windows/win32/Fwpmu/nf-fwpmu-ipseckeymanagersetsecurityinfobykey0?branch=master)
-   [**IPsecKeyManagersGet0**](/windows/win32/Fwpmu/nf-fwpmu-ipseckeymanagersget0?branch=master)
-   [**IPsecKeyManagerUnregisterAndDelete0**](/windows/win32/Fwpmu/nf-fwpmu-ipseckeymanagerunregisteranddelete0?branch=master)
-   [**IPsecSaContextSubscribe0**](/windows/win32/Fwpmu/nf-fwpmu-ipsecsacontextsubscribe0?branch=master)
-   [**IPsecSaContextSubscriptionsGet0**](/windows/win32/Fwpmu/nf-fwpmu-ipsecsacontextsubscriptionsget0?branch=master)
-   [**IPsecSaContextUnsubscribe0**](/windows/win32/Fwpmu/nf-fwpmu-ipsecsacontextunsubscribe0?branch=master)
-   [**NetworkIsolationDiagnoseConnectFailureAndGetInfo**](https://msdn.microsoft.com/library/windows/desktop/hh780507)
-   [**NetworkIsolationEnumAppContainers**](https://msdn.microsoft.com/library/windows/desktop/hh447479)
-   [**NetworkIsolationEnumerateAppContainerRules**](https://msdn.microsoft.com/library/windows/desktop/hh780508)
-   [**NetworkIsolationFreeAppContainers**](https://msdn.microsoft.com/library/windows/desktop/hh447480)
-   [**NetworkIsolationGetAppContainerConfig**](https://msdn.microsoft.com/library/windows/desktop/hh447481)
-   [**NetworkIsolationRegisterForAppContainerChanges**](https://msdn.microsoft.com/library/windows/desktop/hh447482)
-   [**NetworkIsolationSetAppContainerConfig**](https://msdn.microsoft.com/library/windows/desktop/hh447483)
-   [**NetworkIsolationSetupAppContainerBinaries**](https://msdn.microsoft.com/library/windows/desktop/hh447484)
-   [**PAC\_CHANGES\_CALLBACK\_FN**](https://msdn.microsoft.com/library/windows/desktop/hh447487)

## New structures

-   [**IKEEXT\_AUTHENTICATION\_METHOD2**](/windows/win32/iketypes/ns-iketypes-ikeext_authentication_method2_?branch=master)
-   [**IKEEXT\_CERT\_EKUS0**](/windows/win32/iketypes/ns-iketypes-ikeext_cert_ekus0_?branch=master)
-   [**IKEEXT\_CERT\_NAME0**](/windows/win32/iketypes/ns-iketypes-ikeext_cert_name0_?branch=master)
-   [**IKEEXT\_CERTIFICATE\_AUTHENTICATION2**](/windows/win32/iketypes/ns-iketypes-ikeext_certificate_authentication2_?branch=master)
-   [**IKEEXT\_CERTIFICATE\_CRITERIA0**](/windows/win32/iketypes/ns-iketypes-ikeext_certificate_criteria0_?branch=master)
-   [**IKEEXT\_EM\_POLICY2**](/windows/win32/iketypes/ns-iketypes-ikeext_em_policy2_?branch=master)
-   [**IKEEXT\_KERBEROS\_AUTHENTICATION1**](/windows/win32/iketypes/ns-iketypes-ikeext_kerberos_authentication1__?branch=master)
-   [**IKEEXT\_POLICY2**](/windows/win32/iketypes/ns-iketypes-ikeext_policy2_?branch=master)
-   [**IPSEC\_KEY\_MANAGER0**](/windows/win32/ipsectypes/ns-ipsectypes-_ipsec_key_manager0?branch=master)
-   [**IPSEC\_KEY\_MANAGER\_CALLBACKS0**](/windows/win32/fwpmu/ns-fwpmu-_ipsec_key_manager_callbacks0?branch=master)
-   [**IPSEC\_KEYING\_POLICY1**](/windows/win32/ipsectypes/ns-ipsectypes-ipsec_keying_policy1_?branch=master)
-   [**IPSEC\_SA\_CONTEXT\_CHANGE0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_sa_context_change0_?branch=master)
-   [**IPSEC\_SA\_CONTEXT\_SUBSCRIPTION0**](/windows/win32/Ipsectypes/ns-ipsectypes-ipsec_sa_context_subscription0_?branch=master)
-   [**IPSEC\_TRANSPORT\_POLICY2**](/windows/win32/ipsectypes/ns-ipsectypes-ipsec_transport_policy2_?branch=master)
-   [**IPSEC\_TUNNEL\_ENDPOINT0**](/windows/win32/ipsectypes/ns-ipsectypes-ipsec_tunnel_endpoint0_?branch=master)
-   [**IPSEC\_TUNNEL\_ENDPOINTS2**](/windows/win32/ipsectypes/ns-ipsectypes-ipsec_tunnel_endpoints2_?branch=master)
-   [**IPSEC\_TUNNEL\_POLICY2**](/windows/win32/ipsectypes/ns-ipsectypes-ipsec_tunnel_policy2_?branch=master)
-   [**FWPM\_CONNECTION0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_connection0_?branch=master)
-   [**FWPM\_CONNECTION\_ENUM\_TEMPLATE0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_connection_enum_template0_?branch=master)
-   [**FWPM\_CONNECTION\_SUBSCRIPTION0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_connection_subscription0_?branch=master)
-   [**FWPM\_NET\_EVENT2**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_net_event2_?branch=master)
-   [**FWPM\_NET\_EVENT\_CAPABILITY\_ALLOW0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_net_event_capability_allow0_?branch=master)
-   [**FWPM\_NET\_EVENT\_CAPABILITY\_DROP0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_net_event_capability_drop0_?branch=master)
-   [**FWPM\_NET\_EVENT\_CLASSIFY\_ALLOW0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_net_event_classify_allow0?branch=master)
-   [**FWPM\_NET\_EVENT\_CLASSIFY\_DROP2**](/windows/win32/fwpmtypes/ns-fwpmtypes-fwpm_net_event_classify_drop2_?branch=master)
-   [**FWPM\_NET\_EVENT\_CLASSIFY\_DROP\_MAC0**](/windows/win32/fwpmtypes/ns-fwpmtypes-fwpm_net_event_classify_drop_mac0_?branch=master)
-   [**FWPM\_NET\_EVENT\_HEADER2**](/windows/win32/fwpmtypes/ns-fwpmtypes-fwpm_net_event_header2_?branch=master)
-   [**FWPM\_PROVIDER\_CONTEXT2**](/windows/win32/fwpmtypes/ns-fwpmtypes-fwpm_provider_context2_?branch=master)
-   [**FWPM\_VSWITCH\_EVENT0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_vswitch_event0_?branch=master)
-   [**FWPM\_VSWITCH\_EVENT\_SUBSCRIPTION0**](/windows/win32/Fwpmtypes/ns-fwpmtypes-fwpm_vswitch_event_subscription0_?branch=master)

## New enumerated types

-   [**FWP\_VSWITCH\_NETWORK\_TYPE**](/windows/win32/fwptypes/ne-fwptypes-fwp_vswitch_network_type_?branch=master)
-   [**FWPM\_APPC\_NETWORK\_CAPABILITY\_TYPE**](/windows/win32/Fwpmtypes/ne-fwpmtypes-fwpm_appc_network_capability_type_?branch=master)
-   [**FWPM\_CONNECTION\_EVENT\_TYPE**](/windows/win32/Fwpmtypes/ne-fwpmtypes-fwpm_connection_event_type_?branch=master)
-   [**FWPM\_VSWITCH\_EVENT\_TYPE**](/windows/win32/Fwpmtypes/ne-fwpmtypes-fwpm_vswitch_event_type_?branch=master)
-   [**IKEEXT\_CERT\_CRITERIA\_NAME\_TYPE**](/windows/win32/iketypes/ne-iketypes-ikeext_cert_criteria_name_type_?branch=master)
-   [**IPSEC\_SA\_CONTEXT\_EVENT\_TYPE0**](/windows/win32/Ipsectypes/ne-ipsectypes-ipsec_sa_context_event_type0_?branch=master)

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

The document [What's New in Windows Filtering Platform](http://go.microsoft.com/fwlink/p/?LinkId=140050) details many of the updates made for Windows 7. Information is also available in the Windows Driver Kit on [WFP Changes for Windows 7](http://go.microsoft.com/fwlink/p/?LinkId=262711).

 

 




