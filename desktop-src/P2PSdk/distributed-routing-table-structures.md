---
Description: 'The following structures support the Distributed Routing Table (DRT) API functions.'
ms.assetid: '3ff85b24-5ec0-4b26-b30e-1bf8030a575d'
title: Distributed Routing Table Structures
---

# Distributed Routing Table Structures

The following structures support the Distributed Routing Table (DRT) API functions.



| Structure                                                  | Description                                                                                                                                                                              |
|------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DRT\_DATA**](drt-data.md)                              | Contains a data blob. This structure is used by several DRT functions.                                                                                                                   |
| [**DRT\_REGISTRATION**](drt-registration.md)              | Contains the key registration. This is a member of the [**DRT\_SEARCH\_RESULT**](drt-search-result.md) structure and is an argument passed to [**DrtRegisterKey**](drtregisterkey.md). |
| [**DRT\_ADDRESS**](drt-address.md)                        | Contains endpoint information about a DRT node that participated in a search. This information is intended for use in debugging connectivity problems.                                   |
| [**DRT\_ADDRESS\_LIST**](drt-address-list.md)             | Contains a set of [**DRT\_ADDRESS**](drt-address.md) structures representing the nodes contacted during a search for a key.                                                             |
| [**DRT\_SECURITY\_PROVIDER**](drt-security-provider.md)   | Defines the interface that must be implemented by a security provider.                                                                                                                   |
| [**DRT\_BOOTSTRAP\_PROVIDER**](drt-bootstrap-provider.md) | Defines the interface that must be implemented by a bootstrap provider.                                                                                                                  |
| [**DRT\_SETTINGS**](drt-settings.md)                      | Defines DRT settings at initialization. This structure is passed as an argument to [**DrtOpen**](drtopen.md).                                                                           |
| [**DRT\_SEARCH\_INFO**](drt-search-info.md)               | Defines a search query. This structure is passed as an argument to [**DrtStartSearch**](drtstartsearch.md).                                                                             |
| [**DRT\_SEARCH\_RESULT**](drt-search-result.md)           | Contains a search result. This structure is returned by [**DrtGetSearchResult**](drtgetsearchresult.md).                                                                                |
| [**DRT\_EVENT\_DATA**](drt-event-data.md)                 | Contains the event data returned by calling [**DrtGetEventData**](drtgeteventdata.md) after an application receives an event signal.                                                    |



 

## Related topics

<dl> <dt>

[Distributed Routing Table Enumerations](distributed-routing-table-enumerations.md)
</dt> <dt>

[Distributed Routing Table Functions](distributed-routing-table-functions.md)
</dt> <dt>

[Distributed Routing Table API Reference](distributed-routing-table-api-reference.md)
</dt> </dl>

 

 



