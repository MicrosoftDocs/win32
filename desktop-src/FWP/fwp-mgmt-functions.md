---
title: Management Functions
description: The Windows Filtering Platform (WFP) management functions for the filter engine are as follows.
ms.assetid: 983eb1bb-af6b-42cf-8148-ed3a0e3102a9
keywords:
- Windows Filtering Platform API Management Functions
ms.topic: article
ms.date: 05/31/2018
---

# Management Functions

The Windows Filtering Platform (WFP) management functions for the filter engine are as follows.

Callout Management

-   [**FWPM\_CALLOUT\_CHANGE\_CALLBACK0**](/windows/win32/api/fwpmu/nc-fwpmu-fwpm_callout_change_callback0)
-   [**FwpmCalloutAdd0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmcalloutadd0)
-   [**FwpmCalloutCreateEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmcalloutcreateenumhandle0)
-   [**FwpmCalloutDeleteById0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmcalloutdeletebyid0)
-   [**FwpmCalloutDeleteByKey0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmcalloutdeletebykey0)
-   [**FwpmCalloutDestroyEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmcalloutdestroyenumhandle0)
-   [**FwpmCalloutEnum0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmcalloutenum0)
-   [**FwpmCalloutGetById0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmcalloutgetbyid0)
-   [**FwpmCalloutGetByKey0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmcalloutgetbykey0)
-   [**FwpmCalloutGetSecurityInfoByKey0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmcalloutgetsecurityinfobykey0)
-   [**FwpmCalloutSetSecurityInfoByKey0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmcalloutsetsecurityinfobykey0)
-   [**FwpmCalloutSubscribeChanges0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmcalloutsubscribechanges0)
-   [**FwpmCalloutSubscriptionsGet0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmcalloutsubscriptionsget0)
-   [**FwpmCalloutUnsubscribeChanges0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmcalloutunsubscribechanges0)

Connection Object Management

-   [**FWPM\_CONNECTION\_CALLBACK0**](/windows/win32/api/fwpmu/nc-fwpmu-fwpm_connection_callback0)
-   [**FwpmConnectionCreateEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmconnectioncreateenumhandle0)
-   [**FwpmConnectionDestroyEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmconnectiondestroyenumhandle0)
-   [**FwpmConnectionEnum0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmconnectionenum0)
-   [**FwpmConnectionGetById0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmconnectiongetbyid0)
-   [**FwpmConnectionGetSecurityInfo0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmconnectiongetsecurityinfo0)
-   [**FwpmConnectionSetSecurityInfo0**](/windows/desktop/api/fwpmu/nf-fwpmu-fwpmconnectionsetsecurityinfo0)
-   [**FwpmConnectionSubscribe0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmconnectionsubscribe0)
-   [**FwpmConnectionSubscriptionsGet0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmconnectionsubscriptionsget0)
-   [**FwpmConnectionUnsubscribe0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmconnectionunsubscribe0)

Event Management

-   FWPM\_NET\_EVENT\_CALLBACK:
    -   [**FWPM\_NET\_EVENT\_CALLBACK0**](/windows/win32/api/fwpmu/nc-fwpmu-fwpm_net_event_callback0) (Windows 7)
    -   [**FWPM\_NET\_EVENT\_CALLBACK1**](/windows/desktop/api/fwpmu/nc-fwpmu-fwpm_net_event_callback1) (Windows 8)
-   [**FwpmNetEventCreateEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmneteventcreateenumhandle0)
-   [**FwpmNetEventDestroyEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmneteventdestroyenumhandle0)
-   FwpmNetEventEnum:
    -   [**FwpmNetEventEnum0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmneteventenum0) (Windows Vista)
    -   [**FwpmNetEventEnum1**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmneteventenum1) (Windows 7)
    -   [**FwpmNetEventEnum2**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmneteventenum2) (Windows 8)
-   [**FwpmNetEventsGetSecurityInfo0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmneteventsgetsecurityinfo0)
-   [**FwpmNetEventsSetSecurityInfo0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmneteventssetsecurityinfo0)
-   FwpmNetEventsSubscribe:
    -   [**FwpmNetEventSubscribe0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmneteventsubscribe0) (Windows 7)
    -   [**FwpmNetEventSubscribe1**](/windows/desktop/api/fwpmu/nf-fwpmu-fwpmneteventsubscribe1) (Windows 8)
-   [**FwpmNetEventSubscriptionsGet0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmneteventsubscriptionsget0)
-   [**FwpmNetEventUnsubscribe0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmneteventunsubscribe0)

Filter Management

-   [**FWPM\_FILTER\_CHANGE\_CALLBACK0**](/windows/win32/api/fwpmu/nc-fwpmu-fwpm_filter_change_callback0)
-   [**FwpmFilterAdd0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmfilteradd0)
-   [**FwpmFilterCreateEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmfiltercreateenumhandle0)
-   [**FwpmFilterDeleteById0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmfilterdeletebyid0)
-   [**FwpmFilterDeleteByKey0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmfilterdeletebykey0)
-   [**FwpmFilterDestroyEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmfilterdestroyenumhandle0)
-   [**FwpmFilterEnum0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmfilterenum0)
-   [**FwpmFilterGetById0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmfiltergetbyid0)
-   [**FwpmFilterGetByKey0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmfiltergetbykey0)
-   [**FwpmFilterGetSecurityInfoByKey0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmfiltergetsecurityinfobykey0)
-   [**FwpmFilterSetSecurityInfoByKey0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmfiltersetsecurityinfobykey0)
-   [**FwpmFilterSubscribeChanges0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmfiltersubscribechanges0)
-   [**FwpmFilterSubscriptionsGet0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmfiltersubscriptionsget0)
-   [**FwpmFilterUnsubscribeChanges0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmfilterunsubscribechanges0)
-   [**FwpmGetAppIdFromFileName0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmgetappidfromfilename0)

Layer Management

-   [**FwpmLayerCreateEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmlayercreateenumhandle0)
-   [**FwpmLayerDestroyEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmlayerdestroyenumhandle0)
-   [**FwpmLayerEnum0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmlayerenum0)
-   [**FwpmLayerGetById0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmlayergetbyid0)
-   [**FwpmLayerGetByKey0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmlayergetbykey0)
-   [**FwpmLayerGetSecurityInfoByKey0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmlayergetsecurityinfobykey0)
-   [**FwpmLayerSetSecurityInfoByKey0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmlayersetsecurityinfobykey0)

Provider Context Management

-   [**FWPM\_PROVIDER\_CONTEXT\_CHANGE\_CALLBACK0**](/windows/win32/api/fwpmu/nc-fwpmu-fwpm_provider_context_change_callback0)
-   FwpmProviderContextAdd:
    -   [**FwpmProviderContextAdd0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmprovidercontextadd0) (Windows Vista)
    -   [**FwpmProviderContextAdd1**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmprovidercontextadd1) (Windows 7)
    -   [**FwpmProviderContextAdd2**](/windows/desktop/api/fwpmu/nf-fwpmu-fwpmprovidercontextadd2) (Windows 8)
-   [**FwpmProviderContextCreateEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmprovidercontextcreateenumhandle0)
-   [**FwpmProviderContextDeleteById0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmprovidercontextdeletebyid0)
-   [**FwpmProviderContextDeleteByKey0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmprovidercontextdeletebykey0)
-   [**FwpmProviderContextDestroyEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmprovidercontextdestroyenumhandle0)
-   FwpmProviderContextEnum:
    -   [**FwpmProviderContextEnum0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmprovidercontextenum0) (Windows Vista)
    -   [**FwpmProviderContextEnum1**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmprovidercontextenum1) (Windows 7)
    -   [**FwpmProviderContextEnum2**](/windows/desktop/api/fwpmu/nf-fwpmu-fwpmprovidercontextenum2) (Windows 8)
-   FwpmProviderContextGetById:
    -   [**FwpmProviderContextGetById0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmprovidercontextgetbyid0) (Windows Vista)
    -   [**FwpmProviderContextGetById1**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmprovidercontextgetbyid1) (Windows 7)
    -   [**FwpmProviderContextGetById2**](/windows/desktop/api/fwpmu/nf-fwpmu-fwpmprovidercontextgetbyid2) (Windows 8)
-   FwpmProviderContextGetByKey:
    -   [**FwpmProviderContextGetByKey0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmprovidercontextgetbykey0) (Windows Vista)
    -   [**FwpmProviderContextGetByKey1**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmprovidercontextgetbykey1) (Windows 7)
    -   [**FwpmProviderContextGetByKey2**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmprovidercontextgetbykey2) (Windows 8)
-   [**FwpmProviderContextGetSecurityInfoByKey0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmprovidercontextgetsecurityinfobykey0)
-   [**FwpmProviderContextSetSecurityInfoByKey0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmprovidercontextsetsecurityinfobykey0)
-   [**FwpmProviderContextSubscribeChanges0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmprovidercontextsubscribechanges0)
-   [**FwpmProviderContextSubscriptionsGet0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmprovidercontextsubscriptionsget0)
-   [**FwpmProviderContextUnsubscribeChanges0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmprovidercontextunsubscribechanges0)

Provider Management

-   [**FWPM\_PROVIDER\_CHANGE\_CALLBACK0**](/windows/win32/api/fwpmu/nc-fwpmu-fwpm_provider_change_callback0)
-   [**FwpmProviderAdd0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmprovideradd0)
-   [**FwpmProviderCreateEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmprovidercreateenumhandle0)
-   [**FwpmProviderDeleteByKey0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmproviderdeletebykey0)
-   [**FwpmProviderDestroyEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmproviderdestroyenumhandle0)
-   [**FwpmProviderEnum0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmproviderenum0)
-   [**FwpmProviderGetByKey0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmprovidergetbykey0)
-   [**FwpmProviderGetSecurityInfoByKey0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmprovidergetsecurityinfobykey0)
-   [**FwpmProviderSetSecurityInfoByKey0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmprovidersetsecurityinfobykey0)
-   [**FwpmProviderSubscribeChanges0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmprovidersubscribechanges0)
-   [**FwpmProviderSubscriptionsGet0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmprovidersubscriptionsget0)
-   [**FwpmProviderUnsubscribeChanges0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmproviderunsubscribechanges0)

Session Management

-   [**FwpmEngineClose0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmengineclose0)
-   [**FwpmEngineGetOption0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmenginegetoption0)
-   [**FwpmEngineGetSecurityInfo0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmenginegetsecurityinfo0)
-   [**FwpmEngineOpen0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmengineopen0)
-   [**FwpmEngineSetOption0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmenginesetoption0)
-   [**FwpmEngineSetSecurityInfo0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmenginesetsecurityinfo0)
-   [**FwpmSessionCreateEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmsessioncreateenumhandle0)
-   [**FwpmSessionDestroyEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmsessiondestroyenumhandle0)
-   [**FwpmSessionEnum0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmsessionenum0)

Sublayer Management

-   [**FWPM\_SUBLAYER\_CHANGE\_CALLBACK0**](/windows/win32/api/fwpmu/nc-fwpmu-fwpm_sublayer_change_callback0)
-   [**FwpmSubLayerAdd0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmsublayeradd0)
-   [**FwpmSubLayerCreateEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmsublayercreateenumhandle0)
-   [**FwpmSubLayerDeleteByKey0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmsublayerdeletebykey0)
-   [**FwpmSubLayerDestroyEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmsublayerdestroyenumhandle0)
-   [**FwpmSubLayerEnum0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmsublayerenum0)
-   [**FwpmSubLayerGetByKey0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmsublayergetbykey0)
-   [**FwpmSubLayerGetSecurityInfoByKey0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmsublayergetsecurityinfobykey0)
-   [**FwpmSubLayerSetSecurityInfoByKey0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmsublayersetsecurityinfobykey0)
-   [**FwpmSubLayerSubscribeChanges0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmsublayersubscribechanges0)
-   [**FwpmSubLayerSubscriptionsGet0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmsublayersubscriptionsget0)
-   [**FwpmSubLayerUnsubscribeChanges0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmsublayerunsubscribechanges0)

System Ports Management

-   [**FWPM\_SYSTEM\_PORTS\_CALLBACK0**](/windows/win32/api/fwpmu/nc-fwpmu-fwpm_system_ports_callback0)
-   [**FwpmSystemPortsGet0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmsystemportsget0)
-   [**FwpmSystemPortsSubscribe0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmsystemportssubscribe0)
-   [**FwpmSystemPortsUnsubscribe0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmsystemportsunsubscribe0)

Transaction Management

-   [**FwpmTransactionAbort0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmtransactionabort0)
-   [**FwpmTransactionBegin0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmtransactionbegin0)
-   [**FwpmTransactionCommit0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmtransactioncommit0)

vSwitch Management

-   [**FWPM\_VSWITCH\_EVENT\_CALLBACK0**](/windows/win32/api/fwpmu/nc-fwpmu-fwpm_vswitch_event_callback0)
-   [**FwpmvSwitchEventsGetSecurityInfo0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmvswitcheventsgetsecurityinfo0)
-   [**FwpmvSwitchEventsSetSecurityInfo0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmvswitcheventssetsecurityinfo0)
-   [**FwpmvSwitchEventSubscribe0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmvswitcheventsubscribe0)
-   [**FwpmvSwitchEventUnsubscribe0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmvswitcheventunsubscribe0)

 

 