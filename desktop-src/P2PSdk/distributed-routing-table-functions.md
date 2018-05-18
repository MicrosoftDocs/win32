---
Description: 'The Distributed Routing Table (DRT) API utilizes the following functions.'
ms.assetid: '1ceff217-d410-47fa-99a2-8588f001859e'
title: Distributed Routing Table Functions
---

# Distributed Routing Table Functions

The Distributed Routing Table (DRT) API utilizes the following functions.

## Lifetime Management Functions



| Function                                           | Description                                                                                                    |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [**DrtOpen**](drtopen.md)                         | Creates a local DRT instance using criteria specified by the [**DRT\_SETTINGS**](drt-settings.md) structure.  |
| [**DrtClose**](drtclose.md)                       | Closes and removes the local instance of the DRT.                                                              |
| [**DrtGetEventData**](drtgeteventdata.md)         | Retrieves event data associated with a signaled event.                                                         |
| [**DrtGetEventDataSize**](drtgeteventdatasize.md) | Returns the size of the [**DRT\_EVENT\_DATA**](drt-event-data.md) structure associated with a signaled event. |



 

## Module Management Functions



| Function                                                                           | Description                                                                                                                           |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**DrtCreatePnrpBootstrapResolver**](drtcreatepnrpbootstrapresolver.md)           | Creates a bootstrap resolver based on the PNRP protocol.                                                                              |
| [**DrtDeletePnrpBootstrapResolver**](drtdeletepnrpbootstrapresolver.md)           | Deletes a bootstrap resolver based on the PNRP protocol.                                                                              |
| [**DrtCreateDnsBootstrapResolver**](drtcreatednsbootstrapresolver.md)             | Creates a bootstrap provider that will contact a well known host by name.                                                             |
| [**DrtDeleteDnsBootstrapResolver**](drtdeletednsbootstrapresolver.md)             | Deletes a bootstrap provider that will contact a well known host by name.                                                             |
| [**DrtCreateIpv6UdpTransport**](drtcreateipv6udptransport.md)                     | Creates a transport based on the IPv6 UDP protocol.                                                                                   |
| [**DrtDeleteIpv6UdpTransport**](drtdeleteipv6udptransport.md)                     | Deletes a transport based on the IPv6 UDP protocol.                                                                                   |
| [**DrtCreateDerivedKeySecurityProvider**](drtcreatederivedkeysecurityprovider.md) | Creates a derived key security provider for the DRT.                                                                                  |
| [**DrtCreateDerivedKey**](drtcreatederivedkey.md)                                 | Creates a key that can be utilized by [**DrtRegisterKey**](drtregisterkey.md) when the DRT is using a derived key security provider. |
| [**DrtDeleteDerivedKeySecurityProvider**](drtdeletederivedkeysecurityprovider.md) | Deletes a derived key security provider for the DRT.                                                                                  |
| [**DrtCreateNullSecurityProvider**](drtcreatenullsecurityprovider.md)             | Creates a null security provider. This security provider does not require nodes to authenticate keys.                                 |
| [**DrtDeleteNullSecurityProvider**](drtdeletenullsecurityprovider.md)             | Deletes a null security provider.                                                                                                     |



 

## Registration Functions



| Function                                     | Description                                                    |
|----------------------------------------------|----------------------------------------------------------------|
| [**DrtRegisterKey**](drtregisterkey.md)     | Registers a key in the DRT.                                    |
| [**DrtUpdateKey**](drtupdatekey.md)         | Updates the application data associated with a registered key. |
| [**DrtUnregisterKey**](drtunregisterkey.md) | Deregisters a key from the DRT.                                |



 

## Search Functions



| Function                                                 | Description                                                                                                                                                                                                             |
|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DrtStartSearch**](drtstartsearch.md)                 | Searches the DRT for a key using criteria specified in the [**DRT\_SEARCH\_INFO**](drt-search-info.md) structure.                                                                                                      |
| [**DrtContinueSearch**](drtcontinuesearch.md)           | Continues a DRT\_SEARCH\_RETURN\_PATH search for a key in the DRT. This function is used only when the **fIterative** flag is set to **TRUE** in the associated [**DRT\_SEARCH\_INFO**](drt-search-info.md) structure. |
| [**DrtGetSearchResult**](drtgetsearchresult.md)         | Retrieves the search result(s).                                                                                                                                                                                         |
| [**DrtGetSearchResultSize**](drtgetsearchresultsize.md) | Returns the size of the next available search result.                                                                                                                                                                   |
| [**DrtGetSearchPath**](drtgetsearchpath.md)             | Returns a list of nodes contacted during the search operation.                                                                                                                                                          |
| [**DrtGetSearchPathSize**](drtgetsearchpathsize.md)     | Returns the size of the search path, which represents the number of nodes utilized in the search operation.                                                                                                             |
| [**DrtEndSearch**](drtendsearch.md)                     | Cancels a search for a key in a DRT, and as a result, the return of results via [**DRT\_SEARCH\_RESULT**](drt-search-result.md) is stopped. This API can be called at any point after a search is issued.              |



 

## Instance Name Functions



| Function                                                 | Description                                                      |
|----------------------------------------------------------|------------------------------------------------------------------|
| [**DrtGetInstanceName**](drtgetinstancename.md)         | Gets the name associated with a DRT instance.                    |
| [**DrtGetInstanceNameSize**](drtgetinstancenamesize.md) | Returns the size of the Distributed Routing Table instance name. |



 

## Related topics

<dl> <dt>

[Distributed Routing Table Enumerations](distributed-routing-table-enumerations.md)
</dt> <dt>

[Distributed Routing Table Structures](distributed-routing-table-structures.md)
</dt> <dt>

[Distributed Routing Table API Reference](distributed-routing-table-api-reference.md)
</dt> </dl>

 

 



