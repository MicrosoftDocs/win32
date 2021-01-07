---
description: 'The PNRP Namespace Provider API uses the following structures:'
ms.assetid: 697fb99a-259f-429c-8818-0d725255bc86
title: PNRP Structures
ms.topic: article
ms.date: 05/31/2018
---

# PNRP Structures

The PNRP Namespace Provider API uses the following structures:



| Structure                                                             | Description                                                                                                                                                         |
|-----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PEER\_PNRP\_ENDPOINT\_INFO**](/windows/desktop/api/P2P/ns-p2p-peer_pnrp_endpoint_info)         | Contains the IP addresses and data associated with a peer endpoint.                                                                                                 |
| [**PEER\_PNRP\_CLOUD\_INFO**](/windows/desktop/api/P2P/ns-p2p-peer_pnrp_cloud_info)               | Contains information about a Peer Name Resolution Protocol (PNRP) cloud.                                                                                            |
| [**PEER\_PNRP\_REGISTRATION\_INFO**](/windows/desktop/api/P2P/ns-p2p-peer_pnrp_registration_info) | Contains the information provided by a peer identity when it registers with a PNRP cloud.                                                                           |
| [PNRP and BLOB](pnrp-and-blob.md)                                    | Passes data to the [**WSAQUERYSET**](winsock-nsp-reference-links.md) structure during calls to several functions.                                                  |
| [PNRP and WSAQUERYSET](pnrp-and-wsaqueryset.md)                      | Facilitates the resolving of names and the enumeration of names and clouds.                                                                                         |
| [**PNRP\_CLOUD\_ID**](/windows/desktop/api/Pnrpdef/ns-pnrpdef-pnrp_cloud_id)                              | Contains the values that define a network cloud.                                                                                                                    |
| [**PNRPCLOUDINFO**](/windows/desktop/api/Pnrpns/ns-pnrpns-pnrpcloudinfo)                                | Pointed to by the **lpBlob** member of the [**WSAQUERYSET**](winsock-nsp-reference-links.md) structure.                                                            |
| [**PNRPINFO\_V1**](/windows/desktop/api/Pnrpns/ns-pnrpns-pnrpinfo_v1)                                      | Pointed to by the **lpBlob** member of the [**WSAQUERYSET**](winsock-nsp-reference-links.md) structure                                                             |
| [**PNRPINFO\_V2**](/previous-versions/windows/desktop/legacy/aa371671(v=vs.85))                                   | Pointed to by the **lpBlob** member of the [**WSAQUERYSET**](winsock-nsp-reference-links.md) structure, and provides support for application-specific opaque data. |



 

 

 
