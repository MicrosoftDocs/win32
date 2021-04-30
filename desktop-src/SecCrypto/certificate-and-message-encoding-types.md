---
description: Many of the functions require certificate or message encoding types.
ms.assetid: 97b25435-aec2-4fdb-a4c6-89ec2e26f51d
title: Certificate and Message Encoding Types
ms.topic: article
ms.date: 05/31/2018
---

# Certificate and Message Encoding Types

Many of the functions require certificate or [*message encoding types*](../secgloss/m-gly.md). This encoding type is a **DWORD**, possibly containing both the certificate and message encoding types. The certificate encoding type is stored in the low-order word. The message encoding type is stored in the high-order word. Some functions or structure fields require only one of the encoding types, but it is always acceptable to specify both encoding types. For an example specifying both encoding types, see [\#includes and \#defines](-includes-and--defines.md).

The following parameter naming convention is used to indicate the encoding types required.



| Name                       | Comments                                                                                                                                                                                                                                                                                                                |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *dwMsgAndCertEncodingType* | Both encoding types are required.                                                                                                                                                                                                                                                                                       |
| *dwMsgEncodingType*        | Only the message encoding type is required.                                                                                                                                                                                                                                                                             |
| *dwCertEncodingType*       | Only the certificate encoding type is required.                                                                                                                                                                                                                                                                         |
| *dwEncodingType*           | Either a message or certificate encoding type is required. If the low-order word containing the certificate encoding type is nonzero, then it is used. Otherwise, the high-order word containing the message encoding type is used. If both are specified, the certificate encoding type in the low-order word is used. |



 

Currently defined encoding types are shown in the following table.



| Encoding type          | Value      |
|------------------------|------------|
| CRYPT\_ASN\_ENCODING   | 0x00000001 |
| X509\_ASN\_ENCODING    | 0x00000001 |
| PKCS\_7\_ASN\_ENCODING | 0x00010000 |



 

 

 
