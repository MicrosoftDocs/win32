---
description: The following structures support the Distributed Routing Table (DRT) API functions.
ms.assetid: 3ff85b24-5ec0-4b26-b30e-1bf8030a575d
title: Distributed Routing Table Structures
ms.topic: article
ms.date: 05/31/2018
---

# Distributed Routing Table Structures

The following structures support the Distributed Routing Table (DRT) API functions.



| Structure                                                  | Description                                                                                                                                                                              |
|------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DRT\_DATA**](/windows/desktop/api/drt/ns-drt-drt_data)                              | Contains a data blob. This structure is used by several DRT functions.                                                                                                                   |
| [**DRT\_REGISTRATION**](/windows/desktop/api/drt/ns-drt-drt_registration)              | Contains the key registration. This is a member of the [**DRT\_SEARCH\_RESULT**](/windows/desktop/api/drt/ns-drt-drt_search_result) structure and is an argument passed to [**DrtRegisterKey**](/windows/desktop/api/drt/nf-drt-drtregisterkey). |
| [**DRT\_ADDRESS**](/windows/desktop/api/drt/ns-drt-drt_address)                        | Contains endpoint information about a DRT node that participated in a search. This information is intended for use in debugging connectivity problems.                                   |
| [**DRT\_ADDRESS\_LIST**](/windows/desktop/api/drt/ns-drt-drt_address_list)             | Contains a set of [**DRT\_ADDRESS**](/windows/desktop/api/drt/ns-drt-drt_address) structures representing the nodes contacted during a search for a key.                                                             |
| [**DRT\_SECURITY\_PROVIDER**](/windows/desktop/api/Drt/ns-drt-drt_security_provider)   | Defines the interface that must be implemented by a security provider.                                                                                                                   |
| [**DRT\_BOOTSTRAP\_PROVIDER**](/windows/desktop/api/drt/ns-drt-drt_bootstrap_provider) | Defines the interface that must be implemented by a bootstrap provider.                                                                                                                  |
| [**DRT\_SETTINGS**](/windows/desktop/api/drt/ns-drt-drt_settings)                      | Defines DRT settings at initialization. This structure is passed as an argument to [**DrtOpen**](/windows/desktop/api/drt/nf-drt-drtopen).                                                                           |
| [**DRT\_SEARCH\_INFO**](/windows/desktop/api/drt/ns-drt-drt_search_info)               | Defines a search query. This structure is passed as an argument to [**DrtStartSearch**](/windows/desktop/api/drt/nf-drt-drtstartsearch).                                                                             |
| [**DRT\_SEARCH\_RESULT**](/windows/desktop/api/drt/ns-drt-drt_search_result)           | Contains a search result. This structure is returned by [**DrtGetSearchResult**](/windows/desktop/api/drt/nf-drt-drtgetsearchresult).                                                                                |
| [**DRT\_EVENT\_DATA**](/windows/desktop/api/drt/ns-drt-drt_event_data)                 | Contains the event data returned by calling [**DrtGetEventData**](/windows/desktop/api/drt/nf-drt-drtgeteventdata) after an application receives an event signal.                                                    |



 

## Related topics

<dl> <dt>

[Distributed Routing Table Enumerations](distributed-routing-table-enumerations.md)
</dt> <dt>

[Distributed Routing Table Functions](distributed-routing-table-functions.md)
</dt> <dt>

[Distributed Routing Table API Reference](distributed-routing-table-api-reference.md)
</dt> </dl>

 

 



