---
Description: The getservbyname and getservbyport functions use the WSALookupServiceBegin function to query SVCID\_INET\_SERVICEBYNAME as the service class GUID.
ms.assetid: 6d4eb1d4-1498-4367-886b-6b08e87bc4a0
title: getservbyname and getservbyport Functions in the API
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# getservbyname and getservbyport Functions in the API

The [**getservbyname**](/windows/win32/winsock/nf-winsock-getservbyname?branch=master) and [**getservbyport**](/windows/win32/winsock/nf-winsock-getservbyport?branch=master) functions use the [**WSALookupServiceBegin**](/windows/win32/Winsock2/nf-winsock2-wsalookupservicebegina?branch=master) function to query SVCID\_INET\_SERVICEBYNAME as the service class GUID. The *lpszServiceInstanceName* member in the [**WSAQUERYSET**](/windows/win32/Winsock2/ns-winsock2-_wsaquerysetw?branch=master) structure passed to the **WSALookupServiceBegin** function references a string to indicate the service name or service port, and (optionally) the service protocol. The formatting of the string is illustrated as FTP or TCP or 21/TCP or just FTP. The string is not case sensitive. The slash mark, if present, separates the protocol identifier from the preceding part of the string. The Ws2\_32.dll will specify LUP\_RETURN\_BLOB and the namespace provider will place a [**SERVENT**](/windows/win32/winsock/ns-winsock-servent?branch=master) structure in the blob (using offsets instead of pointers as described above). Namespace providers should honor these other LUP\_RETURN\_\* flags as well.

| Flag              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LUP\_RETURN\_NAME | Returns the **s\_name** member from [**SERVENT**](/windows/win32/winsock/ns-winsock-servent?branch=master) structure in *lpszServiceInstanceName*.                                                                                                                                                                                                                                                                                                                                                                                                               |
| LUP\_RETURN\_TYPE | Returns canonical GUID in *lpServiceClassId* It is understood that a service identified as FTP or 21 may be on another port according to locally established conventions. The **s\_port** parameter of the [**SERVENT**](/windows/win32/winsock/ns-winsock-servent?branch=master) structure should indicate where the service can be contacted in the local environment. The canonical GUID returned when LUP\_RETURN\_TYPE is set should be one of the predefined GUIDs from Svcs.h that corresponds to the port number indicated in the **SERVENT** structure. |



 

## Related topics

<dl> <dt>

[Compatible Name Resolution for TCP/IP in the Windows Sockets 1.1 API](compatible-name-resolution-for-tcp-ip-in-the-windows-sockets-1-1-api-2.md)
</dt> <dt>

[Protocol-Independent Name Resolution](protocol-independent-name-resolution-2.md)
</dt> <dt>

[Registration and Name Resolution](registration-and-name-resolution-2.md)
</dt> </dl>

 

 



