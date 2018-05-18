---
Description: 'The PNRP Namespace Provider API uses the following structures:'
ms.assetid: '697fb99a-259f-429c-8818-0d725255bc86'
title: PNRP Structures
---

# PNRP Structures

The PNRP Namespace Provider API uses the following structures:



| Structure                                                             | Description                                                                                                                                                         |
|-----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PEER\_PNRP\_ENDPOINT\_INFO**](peer-pnrp-endpoint-info.md)         | Contains the IP addresses and data associated with a peer endpoint.                                                                                                 |
| [**PEER\_PNRP\_CLOUD\_INFO**](peer-pnrp-cloud-info.md)               | Contains information about a Peer Name Resolution Protocol (PNRP) cloud.                                                                                            |
| [**PEER\_PNRP\_REGISTRATION\_INFO**](peer-pnrp-registration-info.md) | Contains the information provided by a peer identity when it registers with a PNRP cloud.                                                                           |
| [PNRP and BLOB](pnrp-and-blob.md)                                    | Passes data to the [**WSAQUERYSET**](winsock-nsp-reference-links.md) structure during calls to several functions.                                                  |
| [PNRP and WSAQUERYSET](pnrp-and-wsaqueryset.md)                      | Facilitates the resolving of names and the enumeration of names and clouds.                                                                                         |
| [**PNRP\_CLOUD\_ID**](pnrp-cloud-id.md)                              | Contains the values that define a network cloud.                                                                                                                    |
| [**PNRPCLOUDINFO**](pnrpcloudinfo.md)                                | Pointed to by the **lpBlob** member of the [**WSAQUERYSET**](winsock-nsp-reference-links.md) structure.                                                            |
| [**PNRPINFO\_V1**](pnrpinfo.md)                                      | Pointed to by the **lpBlob** member of the [**WSAQUERYSET**](winsock-nsp-reference-links.md) structure                                                             |
| [**PNRPINFO\_V2**](pnrpinfo-v2.md)                                   | Pointed to by the **lpBlob** member of the [**WSAQUERYSET**](winsock-nsp-reference-links.md) structure, and provides support for application-specific opaque data. |



 

 

 



