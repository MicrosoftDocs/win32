---
description: NSPGetServiceClassInfo
ms.assetid: 6fbe9c0c-ac1f-4f2b-a542-eae2195b1335
title: Helper Functions in the SPI
ms.topic: article
ms.date: 05/31/2018
---

# Helper Functions in the SPI

-   [**NSPGetServiceClassInfo**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpnspgetserviceclassinfo)

The [**NSPGetServiceClassInfo**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpnspgetserviceclassinfo) function retrieves service class schema information that has been retained by a namespace provider. It is also used by the Windows Sockets 2 DLL in its implementation of [**WSAGetServiceClassNameByClassId**](/windows/desktop/api/Winsock2/nf-winsock2-wsagetserviceclassnamebyclassida).

The following macros defined in the *Svcguid.h* header file and can aid in mapping between well known service classes and these namespaces.

| Macro name                                                                              | Description                                                                                                                                        |
|-----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| **SVCID\_TCP(Port)**<br/> **SVCID\_UDP(Port)**<br/>                         | Given a TCP or UDP port for the Internet protocol, returns the GUID.                                                                               |
| **IS\_SVCID\_TCP(GUID)**<br/> **IS\_SVCID\_UDP(GUID)**<br/>                 | Returns **TRUE** if the GUID for TCP or UDP is within the allowable range.                                                                         |
| **PORT\_FROM\_SVCID\_TCP(GUID)**<br/> **PORT\_FROM\_SVCID\_UDP(GUID)**<br/> | Returns the TCP or UDP port associated with the GUID.                                                                                              |
| **SVCID\_NETWARE(SAPID)**<br/>                                                    | Given the Service Advertising Protocol (SAP) identifier, returns the GUID. This macro is used with the SAP namespace within a NetWare environment. |
| **SAPID\_FROM\_SVCID\_NETWARE(GUID)**<br/>                                        | Returns the NetWare SAP identifier associated with the GUID. This macro is used with the SAP namespace within a NetWare environment.               |
| **IS\_SVCID\_NETWARE(GUID)**<br/>                                                 | Returns **TRUE** if the GUID for NetWare is within the allowable range. This macro is used with the SAP namespace within a NetWare environment.    |



 

> [!Note]  
> The *Svcguid.h* header file is not automatically included by the *Winsock2.h* header file.

 

 

 




