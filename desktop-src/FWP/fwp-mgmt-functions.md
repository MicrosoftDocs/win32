---
title: Management Functions
description: The Windows Filtering Platform (WFP) management functions for the filter engine are as follows.
ms.assetid: 983eb1bb-af6b-42cf-8148-ed3a0e3102a9
keywords:
- Windows Filtering Platform API Management Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Management Functions

The Windows Filtering Platform (WFP) management functions for the filter engine are as follows.

Callout Management

-   [**FWPM\_CALLOUT\_CHANGE\_CALLBACK0**](/windows/win32/Fwpmu/nc-fwpmu-fwpm_callout_change_callback0?branch=master)
-   [**FwpmCalloutAdd0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmcalloutadd0?branch=master)
-   [**FwpmCalloutCreateEnumHandle0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmcalloutcreateenumhandle0?branch=master)
-   [**FwpmCalloutDeleteById0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmcalloutdeletebyid0?branch=master)
-   [**FwpmCalloutDeleteByKey0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmcalloutdeletebykey0?branch=master)
-   [**FwpmCalloutDestroyEnumHandle0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmcalloutdestroyenumhandle0?branch=master)
-   [**FwpmCalloutEnum0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmcalloutenum0?branch=master)
-   [**FwpmCalloutGetById0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmcalloutgetbyid0?branch=master)
-   [**FwpmCalloutGetByKey0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmcalloutgetbykey0?branch=master)
-   [**FwpmCalloutGetSecurityInfoByKey0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmcalloutgetsecurityinfobykey0?branch=master)
-   [**FwpmCalloutSetSecurityInfoByKey0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmcalloutsetsecurityinfobykey0?branch=master)
-   [**FwpmCalloutSubscribeChanges0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmcalloutsubscribechanges0?branch=master)
-   [**FwpmCalloutSubscriptionsGet0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmcalloutsubscriptionsget0?branch=master)
-   [**FwpmCalloutUnsubscribeChanges0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmcalloutunsubscribechanges0?branch=master)

Connection Object Management

-   [**FWPM\_CONNECTION\_CALLBACK0**](/windows/win32/Fwpmu/nc-fwpmu-fwpm_connection_callback0?branch=master)
-   [**FwpmConnectionCreateEnumHandle0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmconnectioncreateenumhandle0?branch=master)
-   [**FwpmConnectionDestroyEnumHandle0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmconnectiondestroyenumhandle0?branch=master)
-   [**FwpmConnectionEnum0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmconnectionenum0?branch=master)
-   [**FwpmConnectionGetById0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmconnectiongetbyid0?branch=master)
-   [**FwpmConnectionGetSecurityInfo0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmconnectiongetsecurityinfo0?branch=master)
-   [**FwpmConnectionSetSecurityInfo0**](/windows/win32/fwpmu/nf-fwpmu-fwpmconnectionsetsecurityinfo0?branch=master)
-   [**FwpmConnectionSubscribe0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmconnectionsubscribe0?branch=master)
-   [**FwpmConnectionSubscriptionsGet0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmconnectionsubscriptionsget0?branch=master)
-   [**FwpmConnectionUnsubscribe0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmconnectionunsubscribe0?branch=master)

Event Management

-   FWPM\_NET\_EVENT\_CALLBACK:
    -   [**FWPM\_NET\_EVENT\_CALLBACK0**](/windows/win32/Fwpmu/nc-fwpmu-fwpm_net_event_callback0?branch=master) (Windows 7)
    -   [**FWPM\_NET\_EVENT\_CALLBACK1**](/windows/win32/fwpmu/nc-fwpmu-fwpm_net_event_callback1?branch=master) (Windows 8)
-   [**FwpmNetEventCreateEnumHandle0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmneteventcreateenumhandle0?branch=master)
-   [**FwpmNetEventDestroyEnumHandle0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmneteventdestroyenumhandle0?branch=master)
-   FwpmNetEventEnum:
    -   [**FwpmNetEventEnum0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmneteventenum0?branch=master) (Windows Vista)
    -   [**FwpmNetEventEnum1**](/windows/win32/Fwpmu/nf-fwpmu-fwpmneteventenum1?branch=master) (Windows 7)
    -   [**FwpmNetEventEnum2**](/windows/win32/Fwpmu/nf-fwpmu-fwpmneteventenum2?branch=master) (Windows 8)
-   [**FwpmNetEventsGetSecurityInfo0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmneteventsgetsecurityinfo0?branch=master)
-   [**FwpmNetEventsSetSecurityInfo0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmneteventssetsecurityinfo0?branch=master)
-   FwpmNetEventsSubscribe:
    -   [**FwpmNetEventSubscribe0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmneteventsubscribe0?branch=master) (Windows 7)
    -   [**FwpmNetEventSubscribe1**](/windows/win32/fwpmu/nf-fwpmu-fwpmneteventsubscribe1?branch=master) (Windows 8)
-   [**FwpmNetEventSubscriptionsGet0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmneteventsubscriptionsget0?branch=master)
-   [**FwpmNetEventUnsubscribe0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmneteventunsubscribe0?branch=master)

Filter Management

-   [**FWPM\_FILTER\_CHANGE\_CALLBACK0**](/windows/win32/Fwpmu/nc-fwpmu-fwpm_filter_change_callback0?branch=master)
-   [**FwpmFilterAdd0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmfilteradd0?branch=master)
-   [**FwpmFilterCreateEnumHandle0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmfiltercreateenumhandle0?branch=master)
-   [**FwpmFilterDeleteById0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmfilterdeletebyid0?branch=master)
-   [**FwpmFilterDeleteByKey0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmfilterdeletebykey0?branch=master)
-   [**FwpmFilterDestroyEnumHandle0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmfilterdestroyenumhandle0?branch=master)
-   [**FwpmFilterEnum0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmfilterenum0?branch=master)
-   [**FwpmFilterGetById0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmfiltergetbyid0?branch=master)
-   [**FwpmFilterGetByKey0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmfiltergetbykey0?branch=master)
-   [**FwpmFilterGetSecurityInfoByKey0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmfiltergetsecurityinfobykey0?branch=master)
-   [**FwpmFilterSetSecurityInfoByKey0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmfiltersetsecurityinfobykey0?branch=master)
-   [**FwpmFilterSubscribeChanges0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmfiltersubscribechanges0?branch=master)
-   [**FwpmFilterSubscriptionsGet0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmfiltersubscriptionsget0?branch=master)
-   [**FwpmFilterUnsubscribeChanges0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmfilterunsubscribechanges0?branch=master)
-   [**FwpmGetAppIdFromFileName0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmgetappidfromfilename0?branch=master)

Layer Management

-   [**FwpmLayerCreateEnumHandle0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmlayercreateenumhandle0?branch=master)
-   [**FwpmLayerDestroyEnumHandle0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmlayerdestroyenumhandle0?branch=master)
-   [**FwpmLayerEnum0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmlayerenum0?branch=master)
-   [**FwpmLayerGetById0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmlayergetbyid0?branch=master)
-   [**FwpmLayerGetByKey0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmlayergetbykey0?branch=master)
-   [**FwpmLayerGetSecurityInfoByKey0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmlayergetsecurityinfobykey0?branch=master)
-   [**FwpmLayerSetSecurityInfoByKey0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmlayersetsecurityinfobykey0?branch=master)

Provider Context Management

-   [**FWPM\_PROVIDER\_CONTEXT\_CHANGE\_CALLBACK0**](/windows/win32/Fwpmu/nc-fwpmu-fwpm_provider_context_change_callback0?branch=master)
-   FwpmProviderContextAdd:
    -   [**FwpmProviderContextAdd0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmprovidercontextadd0?branch=master) (Windows Vista)
    -   [**FwpmProviderContextAdd1**](/windows/win32/Fwpmu/nf-fwpmu-fwpmprovidercontextadd1?branch=master) (Windows 7)
    -   [**FwpmProviderContextAdd2**](/windows/win32/fwpmu/nf-fwpmu-fwpmprovidercontextadd2?branch=master) (Windows 8)
-   [**FwpmProviderContextCreateEnumHandle0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmprovidercontextcreateenumhandle0?branch=master)
-   [**FwpmProviderContextDeleteById0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmprovidercontextdeletebyid0?branch=master)
-   [**FwpmProviderContextDeleteByKey0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmprovidercontextdeletebykey0?branch=master)
-   [**FwpmProviderContextDestroyEnumHandle0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmprovidercontextdestroyenumhandle0?branch=master)
-   FwpmProviderContextEnum:
    -   [**FwpmProviderContextEnum0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmprovidercontextenum0?branch=master) (Windows Vista)
    -   [**FwpmProviderContextEnum1**](/windows/win32/Fwpmu/nf-fwpmu-fwpmprovidercontextenum1?branch=master) (Windows 7)
    -   [**FwpmProviderContextEnum2**](/windows/win32/fwpmu/nf-fwpmu-fwpmprovidercontextenum2?branch=master) (Windows 8)
-   FwpmProviderContextGetById:
    -   [**FwpmProviderContextGetById0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmprovidercontextgetbyid0?branch=master) (Windows Vista)
    -   [**FwpmProviderContextGetById1**](/windows/win32/Fwpmu/nf-fwpmu-fwpmprovidercontextgetbyid1?branch=master) (Windows 7)
    -   [**FwpmProviderContextGetById2**](/windows/win32/fwpmu/nf-fwpmu-fwpmprovidercontextgetbyid2?branch=master) (Windows 8)
-   FwpmProviderContextGetByKey:
    -   [**FwpmProviderContextGetByKey0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmprovidercontextgetbykey0?branch=master) (Windows Vista)
    -   [**FwpmProviderContextGetByKey1**](/windows/win32/Fwpmu/nf-fwpmu-fwpmprovidercontextgetbykey1?branch=master) (Windows 7)
    -   [**FwpmProviderContextGetByKey2**](/windows/win32/Fwpmu/nf-fwpmu-fwpmprovidercontextgetbykey2?branch=master) (Windows 8)
-   [**FwpmProviderContextGetSecurityInfoByKey0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmprovidercontextgetsecurityinfobykey0?branch=master)
-   [**FwpmProviderContextSetSecurityInfoByKey0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmprovidercontextsetsecurityinfobykey0?branch=master)
-   [**FwpmProviderContextSubscribeChanges0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmprovidercontextsubscribechanges0?branch=master)
-   [**FwpmProviderContextSubscriptionsGet0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmprovidercontextsubscriptionsget0?branch=master)
-   [**FwpmProviderContextUnsubscribeChanges0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmprovidercontextunsubscribechanges0?branch=master)

Provider Management

-   [**FWPM\_PROVIDER\_CHANGE\_CALLBACK0**](/windows/win32/Fwpmu/nc-fwpmu-fwpm_provider_change_callback0?branch=master)
-   [**FwpmProviderAdd0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmprovideradd0?branch=master)
-   [**FwpmProviderCreateEnumHandle0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmprovidercreateenumhandle0?branch=master)
-   [**FwpmProviderDeleteByKey0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmproviderdeletebykey0?branch=master)
-   [**FwpmProviderDestroyEnumHandle0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmproviderdestroyenumhandle0?branch=master)
-   [**FwpmProviderEnum0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmproviderenum0?branch=master)
-   [**FwpmProviderGetByKey0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmprovidergetbykey0?branch=master)
-   [**FwpmProviderGetSecurityInfoByKey0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmprovidergetsecurityinfobykey0?branch=master)
-   [**FwpmProviderSetSecurityInfoByKey0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmprovidersetsecurityinfobykey0?branch=master)
-   [**FwpmProviderSubscribeChanges0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmprovidersubscribechanges0?branch=master)
-   [**FwpmProviderSubscriptionsGet0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmprovidersubscriptionsget0?branch=master)
-   [**FwpmProviderUnsubscribeChanges0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmproviderunsubscribechanges0?branch=master)

Session Management

-   [**FwpmEngineClose0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmengineclose0?branch=master)
-   [**FwpmEngineGetOption0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmenginegetoption0?branch=master)
-   [**FwpmEngineGetSecurityInfo0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmenginegetsecurityinfo0?branch=master)
-   [**FwpmEngineOpen0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmengineopen0?branch=master)
-   [**FwpmEngineSetOption0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmenginesetoption0?branch=master)
-   [**FwpmEngineSetSecurityInfo0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmenginesetsecurityinfo0?branch=master)
-   [**FwpmSessionCreateEnumHandle0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmsessioncreateenumhandle0?branch=master)
-   [**FwpmSessionDestroyEnumHandle0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmsessiondestroyenumhandle0?branch=master)
-   [**FwpmSessionEnum0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmsessionenum0?branch=master)

Sublayer Management

-   [**FWPM\_SUBLAYER\_CHANGE\_CALLBACK0**](/windows/win32/Fwpmu/nc-fwpmu-fwpm_sublayer_change_callback0?branch=master)
-   [**FwpmSubLayerAdd0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmsublayeradd0?branch=master)
-   [**FwpmSubLayerCreateEnumHandle0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmsublayercreateenumhandle0?branch=master)
-   [**FwpmSubLayerDeleteByKey0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmsublayerdeletebykey0?branch=master)
-   [**FwpmSubLayerDestroyEnumHandle0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmsublayerdestroyenumhandle0?branch=master)
-   [**FwpmSubLayerEnum0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmsublayerenum0?branch=master)
-   [**FwpmSubLayerGetByKey0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmsublayergetbykey0?branch=master)
-   [**FwpmSubLayerGetSecurityInfoByKey0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmsublayergetsecurityinfobykey0?branch=master)
-   [**FwpmSubLayerSetSecurityInfoByKey0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmsublayersetsecurityinfobykey0?branch=master)
-   [**FwpmSubLayerSubscribeChanges0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmsublayersubscribechanges0?branch=master)
-   [**FwpmSubLayerSubscriptionsGet0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmsublayersubscriptionsget0?branch=master)
-   [**FwpmSubLayerUnsubscribeChanges0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmsublayerunsubscribechanges0?branch=master)

System Ports Management

-   [**FWPM\_SYSTEM\_PORTS\_CALLBACK0**](/windows/win32/Fwpmu/nc-fwpmu-fwpm_system_ports_callback0?branch=master)
-   [**FwpmSystemPortsGet0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmsystemportsget0?branch=master)
-   [**FwpmSystemPortsSubscribe0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmsystemportssubscribe0?branch=master)
-   [**FwpmSystemPortsUnsubscribe0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmsystemportsunsubscribe0?branch=master)

Transaction Management

-   [**FwpmTransactionAbort0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmtransactionabort0?branch=master)
-   [**FwpmTransactionBegin0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmtransactionbegin0?branch=master)
-   [**FwpmTransactionCommit0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmtransactioncommit0?branch=master)

vSwitch Management

-   [**FWPM\_VSWITCH\_EVENT\_CALLBACK0**](/windows/win32/Fwpmu/nc-fwpmu-fwpm_vswitch_event_callback0?branch=master)
-   [**FwpmvSwitchEventsGetSecurityInfo0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmvswitcheventsgetsecurityinfo0?branch=master)
-   [**FwpmvSwitchEventsSetSecurityInfo0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmvswitcheventssetsecurityinfo0?branch=master)
-   [**FwpmvSwitchEventSubscribe0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmvswitcheventsubscribe0?branch=master)
-   [**FwpmvSwitchEventUnsubscribe0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmvswitcheventunsubscribe0?branch=master)

 

 




