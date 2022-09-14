---
description: The Distributed Routing Table (DRT) API utilizes the following functions.
ms.assetid: 1ceff217-d410-47fa-99a2-8588f001859e
title: Distributed Routing Table Functions
ms.topic: article
ms.date: 05/31/2018
---

# Distributed Routing Table Functions

The Distributed Routing Table (DRT) API utilizes the following functions.

## Lifetime Management Functions



| Function                                           | Description                                                                                                    |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [**DrtOpen**](/windows/desktop/api/drt/nf-drt-drtopen)                         | Creates a local DRT instance using criteria specified by the [**DRT\_SETTINGS**](/windows/desktop/api/drt/ns-drt-drt_settings) structure.  |
| [**DrtClose**](/windows/desktop/api/drt/nf-drt-drtclose)                       | Closes and removes the local instance of the DRT.                                                              |
| [**DrtGetEventData**](/windows/desktop/api/drt/nf-drt-drtgeteventdata)         | Retrieves event data associated with a signaled event.                                                         |
| [**DrtGetEventDataSize**](/windows/desktop/api/drt/nf-drt-drtgeteventdatasize) | Returns the size of the [**DRT\_EVENT\_DATA**](/windows/desktop/api/drt/ns-drt-drt_event_data) structure associated with a signaled event. |



 

## Module Management Functions



| Function                                                                           | Description                                                                                                                           |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**DrtCreatePnrpBootstrapResolver**](/windows/desktop/api/drt/nf-drt-drtcreatepnrpbootstrapresolver)           | Creates a bootstrap resolver based on the PNRP protocol.                                                                              |
| [**DrtDeletePnrpBootstrapResolver**](/windows/desktop/api/drt/nf-drt-drtdeletepnrpbootstrapresolver)           | Deletes a bootstrap resolver based on the PNRP protocol.                                                                              |
| [**DrtCreateDnsBootstrapResolver**](/windows/desktop/api/drt/nf-drt-drtcreatednsbootstrapresolver)             | Creates a bootstrap provider that will contact a well known host by name.                                                             |
| [**DrtDeleteDnsBootstrapResolver**](/windows/desktop/api/drt/nf-drt-drtdeletednsbootstrapresolver)             | Deletes a bootstrap provider that will contact a well known host by name.                                                             |
| [**DrtCreateIpv6UdpTransport**](/windows/desktop/api/drt/nf-drt-drtcreateipv6udptransport)                     | Creates a transport based on the IPv6 UDP protocol.                                                                                   |
| [**DrtDeleteIpv6UdpTransport**](/windows/desktop/api/drt/nf-drt-drtdeleteipv6udptransport)                     | Deletes a transport based on the IPv6 UDP protocol.                                                                                   |
| [**DrtCreateDerivedKeySecurityProvider**](/windows/desktop/api/drt/nf-drt-drtcreatederivedkeysecurityprovider) | Creates a derived key security provider for the DRT.                                                                                  |
| [**DrtCreateDerivedKey**](/windows/desktop/api/drt/nf-drt-drtcreatederivedkey)                                 | Creates a key that can be utilized by [**DrtRegisterKey**](/windows/desktop/api/drt/nf-drt-drtregisterkey) when the DRT is using a derived key security provider. |
| [**DrtDeleteDerivedKeySecurityProvider**](/windows/desktop/api/drt/nf-drt-drtdeletederivedkeysecurityprovider) | Deletes a derived key security provider for the DRT.                                                                                  |
| [**DrtCreateNullSecurityProvider**](/windows/desktop/api/drt/nf-drt-drtcreatenullsecurityprovider)             | Creates a null security provider. This security provider does not require nodes to authenticate keys.                                 |
| [**DrtDeleteNullSecurityProvider**](/windows/desktop/api/drt/nf-drt-drtdeletenullsecurityprovider)             | Deletes a null security provider.                                                                                                     |



 

## Registration Functions



| Function                                     | Description                                                    |
|----------------------------------------------|----------------------------------------------------------------|
| [**DrtRegisterKey**](/windows/desktop/api/drt/nf-drt-drtregisterkey)     | Registers a key in the DRT.                                    |
| [**DrtUpdateKey**](/windows/desktop/api/drt/nf-drt-drtupdatekey)         | Updates the application data associated with a registered key. |
| [**DrtUnregisterKey**](/windows/desktop/api/drt/nf-drt-drtunregisterkey) | Deregisters a key from the DRT.                                |



 

## Search Functions



| Function                                                 | Description                                                                                                                                                                                                             |
|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DrtStartSearch**](/windows/desktop/api/drt/nf-drt-drtstartsearch)                 | Searches the DRT for a key using criteria specified in the [**DRT\_SEARCH\_INFO**](/windows/desktop/api/drt/ns-drt-drt_search_info) structure.                                                                                                      |
| [**DrtContinueSearch**](/windows/desktop/api/drt/nf-drt-drtcontinuesearch)           | Continues a DRT\_SEARCH\_RETURN\_PATH search for a key in the DRT. This function is used only when the **fIterative** flag is set to **TRUE** in the associated [**DRT\_SEARCH\_INFO**](/windows/desktop/api/drt/ns-drt-drt_search_info) structure. |
| [**DrtGetSearchResult**](/windows/desktop/api/drt/nf-drt-drtgetsearchresult)         | Retrieves the search result(s).                                                                                                                                                                                         |
| [**DrtGetSearchResultSize**](/windows/desktop/api/drt/nf-drt-drtgetsearchresultsize) | Returns the size of the next available search result.                                                                                                                                                                   |
| [**DrtGetSearchPath**](/windows/desktop/api/drt/nf-drt-drtgetsearchpath)             | Returns a list of nodes contacted during the search operation.                                                                                                                                                          |
| [**DrtGetSearchPathSize**](/windows/desktop/api/drt/nf-drt-drtgetsearchpathsize)     | Returns the size of the search path, which represents the number of nodes utilized in the search operation.                                                                                                             |
| [**DrtEndSearch**](/windows/desktop/api/drt/nf-drt-drtendsearch)                     | Cancels a search for a key in a DRT, and as a result, the return of results via [**DRT\_SEARCH\_RESULT**](/windows/desktop/api/drt/ns-drt-drt_search_result) is stopped. This API can be called at any point after a search is issued.              |



 

## Instance Name Functions



| Function                                                 | Description                                                      |
|----------------------------------------------------------|------------------------------------------------------------------|
| [**DrtGetInstanceName**](/windows/desktop/api/drt/nf-drt-drtgetinstancename)         | Gets the name associated with a DRT instance.                    |
| [**DrtGetInstanceNameSize**](/windows/desktop/api/drt/nf-drt-drtgetinstancenamesize) | Returns the size of the Distributed Routing Table instance name. |



 

## Related topics

<dl> <dt>

[Distributed Routing Table Enumerations](distributed-routing-table-enumerations.md)
</dt> <dt>

[Distributed Routing Table Structures](distributed-routing-table-structures.md)
</dt> <dt>

[Distributed Routing Table API Reference](distributed-routing-table-api-reference.md)
</dt> </dl>

 

 



