---
title: Routing Table Manager Version 2 Simple Data Types
description: The RTMv2 API defines several simple data types. The following table lists these data types.
ms.assetid: e935518e-b8d8-47fb-b2b2-c9750c2b540e
keywords:
- Routing and Remote Access Service RRAS ,Routing Table Manager Version 2,simple data types
- Routing Table Manager Version 2 RRAS ,simple data types
ms.topic: article
ms.date: 05/31/2018
---

# Routing Table Manager Version 2 Simple Data Types

The RTMv2 API defines several simple data types. The following table lists these data types.



| Data type                                                                                                                                                                                                                                                                                                                   | Description                                                                                                                                      | Typedef              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| RTM\_VIEW\_ID, \*PRTM\_VIEW\_ID                                                                                                                                                                                                                                                                                             | Identifies a particular view.                                                                                                                    | INT                  |
| DWORD RTM\_VIEW\_SET, \*PRTM\_VIEW\_SET                                                                                                                                                                                                                                                                                     | Identifies a set of views; expressed as a mask.                                                                                                  | DWORD                |
| RTM\_ENTITY\_HANDLE, \*PRTM\_ENTITY\_HANDLE, RTM\_DEST\_HANDLE, \*PRTM\_DEST\_HANDLE, RTM\_ROUTE\_HANDLE, \*PRTM\_ROUTE\_HANDLE, RTM\_NEXTHOP\_HANDLE, \*PRTM\_NEXTHOP\_HANDLE, RTM\_ENUM\_HANDLE, \*PRTM\_ENUM\_HANDLE, RTM\_ROUTE\_LIST\_HANDLE, \*PRTM\_ROUTE\_LIST\_HANDLE, RTM\_NOTIFY\_HANDLE, \*PRTM\_NOTIFY\_HANDLE | Handles pointing to RTMv2 data.                                                                                                                  | HANDLE               |
| RTM\_ENTITY\_METHOD\_TYPE, \*PRTM\_ENTITY\_METHOD\_TYPE                                                                                                                                                                                                                                                                     | Identifies methods exported by a registered client.                                                                                              | DWORD                |
| RTM\_ENTITY\_EXPORT\_METHOD, \*PRTM\_ENTITY\_EXPORT\_METHOD                                                                                                                                                                                                                                                                 | Specifies the common prototype for client methods.                                                                                               | \_ENTITY\_METHOD     |
| RTM\_ROUTE\_CHANGE\_FLAGS, \*PRTM\_ROUTE\_CHANGE\_FLAGS                                                                                                                                                                                                                                                                     | Input and output flags used to specify the state when a route is added or updated.                                                               | DWORD                |
| RTM\_NEXTHOP\_CHANGE\_FLAGS, \*PRTM\_NEXTHOP\_CHANGE\_FLAGS                                                                                                                                                                                                                                                                 | Output flags used to specify the state when a next hop is added.                                                                                 | DWORD                |
| RTM\_MATCH\_FLAGS, \*PRTM\_MATCH\_FLAGS                                                                                                                                                                                                                                                                                     | Input flags used to specify criteria when matching routes in the routing table.                                                                  | DWORD                |
| RTM\_ENUM\_FLAGS, \*PRTM\_ENUM\_FLAGS                                                                                                                                                                                                                                                                                       | Identifies enumerations.                                                                                                                         | DWORD                |
| RTM\_NOTIFY\_FLAGS, \*PRTM\_NOTIFY\_FLAGS                                                                                                                                                                                                                                                                                   | Output flags used to specify which type of notification is being issued; composed as follows: (Change Types \| Dests) a client is interested in. | DWORD                |
| RTM\_EVENT\_CALLBACK, \*PRTM\_EVENT\_CALLBACK;                                                                                                                                                                                                                                                                              | Identifies the callback used to notify clients that a change has occurred in route state or clients registered.                                  | RTM\_EVENT\_CALLBACK |



 

 

 




