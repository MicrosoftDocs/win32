---
Description: The following structures support the Distributed Routing Table (DRT) API functions.
ms.assetid: 3ff85b24-5ec0-4b26-b30e-1bf8030a575d
title: Distributed Routing Table Structures
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Distributed Routing Table Structures

The following structures support the Distributed Routing Table (DRT) API functions.



| Structure                                                  | Description                                                                                                                                                                              |
|------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DRT\_DATA**](/windows/win32/drt/ns-drt-drt_data_tag?branch=master)                              | Contains a data blob. This structure is used by several DRT functions.                                                                                                                   |
| [**DRT\_REGISTRATION**](/windows/win32/drt/ns-drt-drt_registration_tag?branch=master)              | Contains the key registration. This is a member of the [**DRT\_SEARCH\_RESULT**](/windows/win32/drt/ns-drt-drt_search_result_tag?branch=master) structure and is an argument passed to [**DrtRegisterKey**](/windows/win32/drt/nf-drt-drtregisterkey?branch=master). |
| [**DRT\_ADDRESS**](/windows/win32/drt/ns-drt-_drt_address?branch=master)                        | Contains endpoint information about a DRT node that participated in a search. This information is intended for use in debugging connectivity problems.                                   |
| [**DRT\_ADDRESS\_LIST**](/windows/win32/drt/ns-drt-_drt_address_list?branch=master)             | Contains a set of [**DRT\_ADDRESS**](/windows/win32/drt/ns-drt-_drt_address?branch=master) structures representing the nodes contacted during a search for a key.                                                             |
| [**DRT\_SECURITY\_PROVIDER**](/windows/win32/Drt/ns-drt-drt_security_provider_tag?branch=master)   | Defines the interface that must be implemented by a security provider.                                                                                                                   |
| [**DRT\_BOOTSTRAP\_PROVIDER**](/windows/win32/drt/ns-drt-drt_bootstrap_provider_tag?branch=master) | Defines the interface that must be implemented by a bootstrap provider.                                                                                                                  |
| [**DRT\_SETTINGS**](/windows/win32/drt/ns-drt-drt_settings_tag?branch=master)                      | Defines DRT settings at initialization. This structure is passed as an argument to [**DrtOpen**](/windows/win32/drt/nf-drt-drtopen?branch=master).                                                                           |
| [**DRT\_SEARCH\_INFO**](/windows/win32/drt/ns-drt-drt_search_info_tag?branch=master)               | Defines a search query. This structure is passed as an argument to [**DrtStartSearch**](/windows/win32/drt/nf-drt-drtstartsearch?branch=master).                                                                             |
| [**DRT\_SEARCH\_RESULT**](/windows/win32/drt/ns-drt-drt_search_result_tag?branch=master)           | Contains a search result. This structure is returned by [**DrtGetSearchResult**](/windows/win32/drt/nf-drt-drtgetsearchresult?branch=master).                                                                                |
| [**DRT\_EVENT\_DATA**](/windows/win32/drt/ns-drt-drt_event_data_tag?branch=master)                 | Contains the event data returned by calling [**DrtGetEventData**](/windows/win32/drt/nf-drt-drtgeteventdata?branch=master) after an application receives an event signal.                                                    |



 

## Related topics

<dl> <dt>

[Distributed Routing Table Enumerations](distributed-routing-table-enumerations.md)
</dt> <dt>

[Distributed Routing Table Functions](distributed-routing-table-functions.md)
</dt> <dt>

[Distributed Routing Table API Reference](distributed-routing-table-api-reference.md)
</dt> </dl>

 

 



