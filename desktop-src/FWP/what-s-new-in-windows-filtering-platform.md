---
title: What's New in Windows Filtering Platform
description: Windows 8 and Windows Server 2012 introduce new Windows Filtering Platform programming elements.
ms.assetid: '7529F155-3DBC-4C22-A780-B6311C455E85'
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

-   [**FWPM\_NET\_EVENT\_CALLBACK1**](fwpm-net-event-callback1.md)
-   [**FwpmConnectionCreateEnumHandle0**](fwpmconnectioncreateenumhandle0.md)
-   [**FwpmConnectionDestroyEnumHandle0**](fwpmconnectiondestroyenumhandle0.md)
-   [**FwpmConnectionEnum0**](fwpmconnectionenum0.md)
-   [**FwpmConnectionGetById0**](fwpmconnectiongetbyid0.md)
-   [**FwpmConnectionGetSecurityInfo0**](fwpmconnectiongetsecurityinfo0.md)
-   [**FwpmConnectionSetSecurityInfo0**](fwpmconnectionsetsecurityinfo0.md)
-   [**FwpmConnectionSubscribe0**](fwpmconnectionsubscribe0.md)
-   [**FwpmConnectionSubscriptionsGet0**](fwpmconnectionsubscriptionsget0.md)
-   [**FwpmConnectionUnsubscribe0**](fwpmconnectionunsubscribe0.md)
-   [**FwpmIPsecTunnelAdd2**](fwpmipsectunneladd2.md)
-   [**FwpmNetEventEnum2**](fwpmneteventenum2.md)
-   [**FwpmNetEventSubscribe1**](fwpmneteventsubscribe1.md)
-   [**FwpmProviderContextAdd2**](fwpmprovidercontextadd2.md)
-   [**FwpmProviderContextEnum2**](fwpmprovidercontextenum2.md)
-   [**FwpmProviderContextGetById2**](fwpmprovidercontextgetbyid2.md)
-   [**FwpmProviderContextGetByKey2**](fwpmprovidercontextgetbykey2.md)
-   [**FwpmvSwitchEventsGetSecurityInfo0**](fwpmvswitcheventsgetsecurityinfo0.md)
-   [**FwpmvSwitchEventsSetSecurityInfo0**](fwpmvswitcheventssetsecurityinfo0.md)
-   [**FwpmvSwitchEventSubscribe0**](fwpmvswitcheventsubscribe0.md)
-   [**FwpmvSwitchEventUnsubscribe0**](fwpmvswitcheventunsubscribe0.md)
-   [**IkeextSaEnum2**](ikeextsaenum2.md)
-   [**IkeextSaGetById2**](ikeextsagetbyid2.md)
-   [**IPSEC\_KEY\_MANAGER\_KEY\_DICTATION\_CHECK0**](ipsec-key-manager-key-dictation-check0.md)
-   [**IPSEC\_KEY\_MANAGER\_DICTATE\_KEY0**](ipsec-key-manager-dictate-key0.md)
-   [**IPSEC\_KEY\_MANAGER\_NOTIFY\_KEY0**](ipsec-key-manager-notify-key0.md)
-   [**IPSEC\_SA\_CONTEXT\_CALLBACK0**](ipsec-sa-context-callback0.md)
-   [**IPsecKeyManagerAddAndRegister0**](ipseckeymanageraddandregister0.md)
-   [**IPsecKeyManagerGetSecurityInfoByKey0**](ipseckeymanagergetsecurityinfobykey0.md)
-   [**IPsecKeyManagerSetSecurityInfoByKey0**](ipseckeymanagersetsecurityinfobykey0.md)
-   [**IPsecKeyManagersGet0**](ipseckeymanagersget0.md)
-   [**IPsecKeyManagerUnregisterAndDelete0**](ipseckeymanagerunregisteranddelete0.md)
-   [**IPsecSaContextSubscribe0**](ipsecsacontextsubscribe0.md)
-   [**IPsecSaContextSubscriptionsGet0**](ipsecsacontextsubscriptionsget0.md)
-   [**IPsecSaContextUnsubscribe0**](ipsecsacontextunsubscribe0.md)
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

-   [**IKEEXT\_AUTHENTICATION\_METHOD2**](ikeext-authentication-method2.md)
-   [**IKEEXT\_CERT\_EKUS0**](ikeext-cert-ekus0.md)
-   [**IKEEXT\_CERT\_NAME0**](ikeext-cert-name0.md)
-   [**IKEEXT\_CERTIFICATE\_AUTHENTICATION2**](ikeext-certificate-authentication2.md)
-   [**IKEEXT\_CERTIFICATE\_CRITERIA0**](ikeext-certificate-criteria0.md)
-   [**IKEEXT\_EM\_POLICY2**](ikeext-em-policy2.md)
-   [**IKEEXT\_KERBEROS\_AUTHENTICATION1**](ikeext-kerberos-authentication1.md)
-   [**IKEEXT\_POLICY2**](ikeext-policy2.md)
-   [**IPSEC\_KEY\_MANAGER0**](ipsec-key-manager0.md)
-   [**IPSEC\_KEY\_MANAGER\_CALLBACKS0**](ipsec-key-manager-callbacks0.md)
-   [**IPSEC\_KEYING\_POLICY1**](ipsec-keying-policy1.md)
-   [**IPSEC\_SA\_CONTEXT\_CHANGE0**](ipsec-sa-context-change0.md)
-   [**IPSEC\_SA\_CONTEXT\_SUBSCRIPTION0**](ipsec-sa-context-subscription0.md)
-   [**IPSEC\_TRANSPORT\_POLICY2**](ipsec-transport-policy2.md)
-   [**IPSEC\_TUNNEL\_ENDPOINT0**](ipsec-tunnel-endpoint0.md)
-   [**IPSEC\_TUNNEL\_ENDPOINTS2**](ipsec-tunnel-endpoints2.md)
-   [**IPSEC\_TUNNEL\_POLICY2**](ipsec-tunnel-policy2.md)
-   [**FWPM\_CONNECTION0**](fwpm-connection0.md)
-   [**FWPM\_CONNECTION\_ENUM\_TEMPLATE0**](fwpm-connection-enum-template0.md)
-   [**FWPM\_CONNECTION\_SUBSCRIPTION0**](fwpm-connection-subscription0.md)
-   [**FWPM\_NET\_EVENT2**](fwpm-net-event2.md)
-   [**FWPM\_NET\_EVENT\_CAPABILITY\_ALLOW0**](fwpm-net-event-capability-allow0.md)
-   [**FWPM\_NET\_EVENT\_CAPABILITY\_DROP0**](fwpm-net-event-capability-drop0.md)
-   [**FWPM\_NET\_EVENT\_CLASSIFY\_ALLOW0**](fwpm-net-event-classify-allow0.md)
-   [**FWPM\_NET\_EVENT\_CLASSIFY\_DROP2**](fwpm-net-event-classify-drop2.md)
-   [**FWPM\_NET\_EVENT\_CLASSIFY\_DROP\_MAC0**](fwpm-net-event-classify-drop-mac0.md)
-   [**FWPM\_NET\_EVENT\_HEADER2**](fwpm-net-event-header2.md)
-   [**FWPM\_PROVIDER\_CONTEXT2**](fwpm-provider-context2.md)
-   [**FWPM\_VSWITCH\_EVENT0**](fwpm-vswitch-event0.md)
-   [**FWPM\_VSWITCH\_EVENT\_SUBSCRIPTION0**](fwpm-vswitch-event-subscription0.md)

## New enumerated types

-   [**FWP\_VSWITCH\_NETWORK\_TYPE**](fwp-vswitch-network-type.md)
-   [**FWPM\_APPC\_NETWORK\_CAPABILITY\_TYPE**](fwpm-appc-network-capability-type.md)
-   [**FWPM\_CONNECTION\_EVENT\_TYPE**](fwpm-connection-event-type.md)
-   [**FWPM\_VSWITCH\_EVENT\_TYPE**](fwpm-vswitch-event-type.md)
-   [**IKEEXT\_CERT\_CRITERIA\_NAME\_TYPE**](ikeext-cert-criteria-name-type.md)
-   [**IPSEC\_SA\_CONTEXT\_EVENT\_TYPE0**](ipsec-sa-context-event-type0.md)

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

 

 




