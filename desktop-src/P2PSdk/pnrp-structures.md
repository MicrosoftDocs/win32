---
Description: The PNRP Namespace Provider API uses the following structures
ms.assetid: 697fb99a-259f-429c-8818-0d725255bc86
title: PNRP Structures
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PNRP Structures

The PNRP Namespace Provider API uses the following structures:



| Structure                                                             | Description                                                                                                                                                         |
|-----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PEER\_PNRP\_ENDPOINT\_INFO**](/windows/win32/P2P/ns-p2p-peer_pnrp_endpoint_info_tag?branch=master)         | Contains the IP addresses and data associated with a peer endpoint.                                                                                                 |
| [**PEER\_PNRP\_CLOUD\_INFO**](/windows/win32/P2P/ns-p2p-peer_pnrp_cloud_info_tag?branch=master)               | Contains information about a Peer Name Resolution Protocol (PNRP) cloud.                                                                                            |
| [**PEER\_PNRP\_REGISTRATION\_INFO**](/windows/win32/P2P/ns-p2p-peer_pnrp_registration_info_tag?branch=master) | Contains the information provided by a peer identity when it registers with a PNRP cloud.                                                                           |
| [PNRP and BLOB](pnrp-and-blob.md)                                    | Passes data to the [**WSAQUERYSET**](winsock-nsp-reference-links.md) structure during calls to several functions.                                                  |
| [PNRP and WSAQUERYSET](pnrp-and-wsaqueryset.md)                      | Facilitates the resolving of names and the enumeration of names and clouds.                                                                                         |
| [**PNRP\_CLOUD\_ID**](/windows/win32/Pnrpdef/ns-pnrpdef-_pnrp_cloud_id?branch=master)                              | Contains the values that define a network cloud.                                                                                                                    |
| [**PNRPCLOUDINFO**](/windows/win32/Pnrpns/ns-pnrpns-_pnrpcloudinfo?branch=master)                                | Pointed to by the **lpBlob** member of the [**WSAQUERYSET**](winsock-nsp-reference-links.md) structure.                                                            |
| [**PNRPINFO\_V1**](/windows/win32/Pnrpns/ns-pnrpns-_pnrpinfo_v1?branch=master)                                      | Pointed to by the **lpBlob** member of the [**WSAQUERYSET**](winsock-nsp-reference-links.md) structure                                                             |
| [**PNRPINFO\_V2**](/windows/win32/Pnrpns/?branch=master)                                   | Pointed to by the **lpBlob** member of the [**WSAQUERYSET**](winsock-nsp-reference-links.md) structure, and provides support for application-specific opaque data. |



 

 

 



