---
Description: 'The getservbyname and getservbyport functions use the WSALookupServiceBegin function to query SVCID\_INET\_SERVICEBYNAME as the service class GUID.'
ms.assetid: '6d4eb1d4-1498-4367-886b-6b08e87bc4a0'
title: getservbyname and getservbyport Functions in the API
---

# getservbyname and getservbyport Functions in the API

The [**getservbyname**](getservbyname-2.md) and [**getservbyport**](getservbyport-2.md) functions use the [**WSALookupServiceBegin**](wsalookupservicebegin-2.md) function to query SVCID\_INET\_SERVICEBYNAME as the service class GUID. The *lpszServiceInstanceName* member in the [**WSAQUERYSET**](wsaqueryset-2.md) structure passed to the **WSALookupServiceBegin** function references a string to indicate the service name or service port, and (optionally) the service protocol. The formatting of the string is illustrated as FTP or TCP or 21/TCP or just FTP. The string is not case sensitive. The slash mark, if present, separates the protocol identifier from the preceding part of the string. The Ws2\_32.dll will specify LUP\_RETURN\_BLOB and the namespace provider will place a [**SERVENT**](servent-2.md) structure in the blob (using offsets instead of pointers as described above). Namespace providers should honor these other LUP\_RETURN\_\* flags as well.

| Flag              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LUP\_RETURN\_NAME | Returns the **s\_name** member from [**SERVENT**](servent-2.md) structure in *lpszServiceInstanceName*.                                                                                                                                                                                                                                                                                                                                                                                                               |
| LUP\_RETURN\_TYPE | Returns canonical GUID in *lpServiceClassId* It is understood that a service identified as FTP or 21 may be on another port according to locally established conventions. The **s\_port** parameter of the [**SERVENT**](servent-2.md) structure should indicate where the service can be contacted in the local environment. The canonical GUID returned when LUP\_RETURN\_TYPE is set should be one of the predefined GUIDs from Svcs.h that corresponds to the port number indicated in the **SERVENT** structure. |



 

## Related topics

<dl> <dt>

[Compatible Name Resolution for TCP/IP in the Windows Sockets 1.1 API](compatible-name-resolution-for-tcp-ip-in-the-windows-sockets-1-1-api-2.md)
</dt> <dt>

[Protocol-Independent Name Resolution](protocol-independent-name-resolution-2.md)
</dt> <dt>

[Registration and Name Resolution](registration-and-name-resolution-2.md)
</dt> </dl>

 

 



