---
Description: The Distributed Routing Table (DRT) API utilizes the following functions.
ms.assetid: 1ceff217-d410-47fa-99a2-8588f001859e
title: Distributed Routing Table Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Distributed Routing Table Functions

The Distributed Routing Table (DRT) API utilizes the following functions.

## Lifetime Management Functions



| Function                                           | Description                                                                                                    |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [**DrtOpen**](/windows/win32/drt/nf-drt-drtopen?branch=master)                         | Creates a local DRT instance using criteria specified by the [**DRT\_SETTINGS**](/windows/win32/drt/ns-drt-drt_settings_tag?branch=master) structure.  |
| [**DrtClose**](/windows/win32/drt/nf-drt-drtclose?branch=master)                       | Closes and removes the local instance of the DRT.                                                              |
| [**DrtGetEventData**](/windows/win32/drt/nf-drt-drtgeteventdata?branch=master)         | Retrieves event data associated with a signaled event.                                                         |
| [**DrtGetEventDataSize**](/windows/win32/drt/nf-drt-drtgeteventdatasize?branch=master) | Returns the size of the [**DRT\_EVENT\_DATA**](/windows/win32/drt/ns-drt-drt_event_data_tag?branch=master) structure associated with a signaled event. |



 

## Module Management Functions



| Function                                                                           | Description                                                                                                                           |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**DrtCreatePnrpBootstrapResolver**](/windows/win32/drt/nf-drt-drtcreatepnrpbootstrapresolver?branch=master)           | Creates a bootstrap resolver based on the PNRP protocol.                                                                              |
| [**DrtDeletePnrpBootstrapResolver**](/windows/win32/drt/nf-drt-drtdeletepnrpbootstrapresolver?branch=master)           | Deletes a bootstrap resolver based on the PNRP protocol.                                                                              |
| [**DrtCreateDnsBootstrapResolver**](/windows/win32/drt/nf-drt-drtcreatednsbootstrapresolver?branch=master)             | Creates a bootstrap provider that will contact a well known host by name.                                                             |
| [**DrtDeleteDnsBootstrapResolver**](/windows/win32/drt/nf-drt-drtdeletednsbootstrapresolver?branch=master)             | Deletes a bootstrap provider that will contact a well known host by name.                                                             |
| [**DrtCreateIpv6UdpTransport**](/windows/win32/drt/nf-drt-drtcreateipv6udptransport?branch=master)                     | Creates a transport based on the IPv6 UDP protocol.                                                                                   |
| [**DrtDeleteIpv6UdpTransport**](/windows/win32/drt/nf-drt-drtdeleteipv6udptransport?branch=master)                     | Deletes a transport based on the IPv6 UDP protocol.                                                                                   |
| [**DrtCreateDerivedKeySecurityProvider**](/windows/win32/drt/nf-drt-drtcreatederivedkeysecurityprovider?branch=master) | Creates a derived key security provider for the DRT.                                                                                  |
| [**DrtCreateDerivedKey**](/windows/win32/drt/nf-drt-drtcreatederivedkey?branch=master)                                 | Creates a key that can be utilized by [**DrtRegisterKey**](/windows/win32/drt/nf-drt-drtregisterkey?branch=master) when the DRT is using a derived key security provider. |
| [**DrtDeleteDerivedKeySecurityProvider**](/windows/win32/drt/nf-drt-drtdeletederivedkeysecurityprovider?branch=master) | Deletes a derived key security provider for the DRT.                                                                                  |
| [**DrtCreateNullSecurityProvider**](/windows/win32/drt/nf-drt-drtcreatenullsecurityprovider?branch=master)             | Creates a null security provider. This security provider does not require nodes to authenticate keys.                                 |
| [**DrtDeleteNullSecurityProvider**](/windows/win32/drt/nf-drt-drtdeletenullsecurityprovider?branch=master)             | Deletes a null security provider.                                                                                                     |



 

## Registration Functions



| Function                                     | Description                                                    |
|----------------------------------------------|----------------------------------------------------------------|
| [**DrtRegisterKey**](/windows/win32/drt/nf-drt-drtregisterkey?branch=master)     | Registers a key in the DRT.                                    |
| [**DrtUpdateKey**](/windows/win32/drt/nf-drt-drtupdatekey?branch=master)         | Updates the application data associated with a registered key. |
| [**DrtUnregisterKey**](/windows/win32/drt/nf-drt-drtunregisterkey?branch=master) | Deregisters a key from the DRT.                                |



 

## Search Functions



| Function                                                 | Description                                                                                                                                                                                                             |
|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DrtStartSearch**](/windows/win32/drt/nf-drt-drtstartsearch?branch=master)                 | Searches the DRT for a key using criteria specified in the [**DRT\_SEARCH\_INFO**](/windows/win32/drt/ns-drt-drt_search_info_tag?branch=master) structure.                                                                                                      |
| [**DrtContinueSearch**](/windows/win32/drt/nf-drt-drtcontinuesearch?branch=master)           | Continues a DRT\_SEARCH\_RETURN\_PATH search for a key in the DRT. This function is used only when the **fIterative** flag is set to **TRUE** in the associated [**DRT\_SEARCH\_INFO**](/windows/win32/drt/ns-drt-drt_search_info_tag?branch=master) structure. |
| [**DrtGetSearchResult**](/windows/win32/drt/nf-drt-drtgetsearchresult?branch=master)         | Retrieves the search result(s).                                                                                                                                                                                         |
| [**DrtGetSearchResultSize**](/windows/win32/drt/nf-drt-drtgetsearchresultsize?branch=master) | Returns the size of the next available search result.                                                                                                                                                                   |
| [**DrtGetSearchPath**](/windows/win32/drt/nf-drt-drtgetsearchpath?branch=master)             | Returns a list of nodes contacted during the search operation.                                                                                                                                                          |
| [**DrtGetSearchPathSize**](/windows/win32/drt/nf-drt-drtgetsearchpathsize?branch=master)     | Returns the size of the search path, which represents the number of nodes utilized in the search operation.                                                                                                             |
| [**DrtEndSearch**](/windows/win32/drt/nf-drt-drtendsearch?branch=master)                     | Cancels a search for a key in a DRT, and as a result, the return of results via [**DRT\_SEARCH\_RESULT**](/windows/win32/drt/ns-drt-drt_search_result_tag?branch=master) is stopped. This API can be called at any point after a search is issued.              |



 

## Instance Name Functions



| Function                                                 | Description                                                      |
|----------------------------------------------------------|------------------------------------------------------------------|
| [**DrtGetInstanceName**](/windows/win32/drt/nf-drt-drtgetinstancename?branch=master)         | Gets the name associated with a DRT instance.                    |
| [**DrtGetInstanceNameSize**](/windows/win32/drt/nf-drt-drtgetinstancenamesize?branch=master) | Returns the size of the Distributed Routing Table instance name. |



 

## Related topics

<dl> <dt>

[Distributed Routing Table Enumerations](distributed-routing-table-enumerations.md)
</dt> <dt>

[Distributed Routing Table Structures](distributed-routing-table-structures.md)
</dt> <dt>

[Distributed Routing Table API Reference](distributed-routing-table-api-reference.md)
</dt> </dl>

 

 



