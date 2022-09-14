---
description: NLA clients can record network configuration information on a system-wide basis, enabling future queries to return the specified configuration information regardless of whether the network is active.
ms.assetid: 7e92dd8f-d3a1-4e53-885c-ebc9626fd5dc
title: Registering a Service Instance with NLA
ms.topic: article
ms.date: 05/31/2018
---

# Registering a Service Instance with NLA

NLA clients can record network configuration information on a system-wide basis, enabling future queries to return the specified configuration information regardless of whether the network is active. This capability allows NLA clients to affect a consistent network information user experience across multiple applications.

## Parameters

To register a service instance with the Network Location Awareness service provider, use the [**WSASetService**](/windows/desktop/api/Winsock2/nf-winsock2-wsasetservicea) function. In order to properly register a service instance certain parameters of the **WSASetService** function must be set with the appropriate information, as explained in this section. For quick reference, the **WSASetService** function has the following syntax:

``` syntax
INT WSASetService(
  LPWSAQUERYSET lpqsRegInfo,
  WSAESETSERVICEOP essOperation,
  DWORD dwControlFlags
);
```

For the *lpqsRegInfo* parameter, provide a [**WSAQUERYSET**](/windows/desktop/api/Winsock2/ns-winsock2-wsaquerysetw) structure from either an NLA SP query result, or constructed adhering to the requirements of an NLA SP query, as specified in [Querying NLA](querying-nla-2.md).

Operations supported for the *essOperation* parameter are the following:

<dl> <dt>

<span id="RNRSERVICE_REGISTER"></span><span id="rnrservice_register"></span>RNRSERVICE\_REGISTER
</dt> <dd>

The network defined in the [**WSAQUERYSET**](/windows/desktop/api/Winsock2/ns-winsock2-wsaquerysetw) structure provided in *lpqsRegInfo* is made persistent for the active user by storing the network instance in the registry hive for the current user, which allows impersonation.

</dd> <dt>

<span id="RNRSERVICE_DELETE"></span><span id="rnrservice_delete"></span>RNRSERVICE\_DELETE
</dt> <dd>

If the network defined in the [**WSAQUERYSET**](/windows/desktop/api/Winsock2/ns-winsock2-wsaquerysetw) structure provided in *lpqsRegInfo* is persistent, it will be removed.

</dd> </dl>

The operation specified in the *essOperation* parameter can be modified by the following options, which can be specified with binary OR logic:

<dl> <dt>

<span id="NLA_FRIENDLY_NAME"></span><span id="nla_friendly_name"></span>NLA\_FRIENDLY\_NAME
</dt> <dd>

When used with RNRSERVICE\_REGISTER, the *lpszComment* field of the network defined in *lpqsRegInfo* is checked for validity and stored persistently. When used with RNRSERVICE\_DELETE and the defined network has a friendly name, the friendly name is removed but the network entry is left intact.

</dd> <dt>

<span id="NLA_ALLUSERS_NETWORK"></span><span id="nla_allusers_network"></span>NLA\_ALLUSERS\_NETWORK
</dt> <dd>

When used with RNRSERVICE\_REGISTER, the entry is stored persistently under HKEY\_LOCAL\_MACHINE, making it available during queries to all users on the local computer. When used with RNRSERVICE\_DELETE, the specified network is removed from HKEY\_LOCAL\_MACHINE. An error is returned if the specified network is not present. In order to delete a network from the registry hive of the current user, this flag must not be specified. This flag is only valid in the security context of a local system administrator.

</dd> </dl>

NLA supports the following error codes for [**WSASetService**](/windows/desktop/api/Winsock2/nf-winsock2-wsasetservicea) function calls:

| Error             | Meaning                                                                                                                                                                    |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WSANOTINITIALISED | A successful call to the [**WSAStartup**](/windows/desktop/api/winsock/nf-winsock-wsastartup) function to initialize NLA was not performed.                                                                  |
| WSAEACCESS        | NLA\_ALLUSERS\_NETWORK was specified in *dwControlFlags* while not in the security context of a local system administrator.                                                |
| WSAEALREADY       | The specified network is already persistently stored in the requested manner, and no flags were specified in *dwControlFlags* to indicate an update to the existing entry. |
| WSAEAFNOSUPPORT   | A protocol family was specified for which there is no support. Only IP protocol families are supported in NLA.                                                             |
| WSAEPFNOSUPPORT   | A protocol was specified for which there is no support. Only IP protocol is supported in NLA.                                                                              |



 

 

 



