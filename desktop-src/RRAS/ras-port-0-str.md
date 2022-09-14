---
title: RAS_PORT_0 structure (Rassapi.h)
description: The RAS\_PORT\_0 structure contains information that describes a RAS port.
ms.assetid: 750fc705-0770-427b-b7d6-7876b8b9118a
keywords:
- RAS_PORT_0 structure RAS
- PRAS_PORT_0 structure pointer RAS
topic_type:
- apiref
api_name:
- RAS_PORT_0
api_location:
- Rassapi.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# RAS\_PORT\_0 structure

\[This version of the **RAS\_PORT\_0** structure is not supported as of Windows Vista. Use the newer [**RAS\_PORT\_0**](/windows/desktop/api/Mprapi/ns-mprapi-ras_port_0) defined in mprapi.h instead.\]

The **RAS\_PORT\_0** structure contains information that describes a RAS port.

## Syntax


```C++
typedef struct _RAS_PORT_0 {
  WCHAR wszPortName[RASSAPI_MAX_PORT_NAME];
  WCHAR wszDeviceType[RASSAPI_MAX_DEVICETYPE_NAME];
  WCHAR wszDeviceName[RASSAPI_MAX_DEVICE_NAME];
  WCHAR wszMediaName[RASSAPI_MAX_MEDIA_NAME];
  DWORD reserved;
  DWORD Flags;
  WCHAR wszUserName[UNLEN + 1];
  WCHAR wszComputer[NETBIOS_NAME_LEN];
  DWORD dwStartSessionTime;
  WCHAR wszLogonDomain[DNLEN + 1];
  BOOL  fAdvancedServer;
} RAS_PORT_0, *PRAS_PORT_0;
```



## Members

<dl> <dt>

**wszPortName**
</dt> <dd>

A null-terminated Unicode string that specifies the name of the port, such as "COM1".

</dd> <dt>

**wszDeviceType**
</dt> <dd>

A null-terminated Unicode string that specifies the type of the device on which the connection was made, such as Modem or ISDN. The list of device types that might be specified in this member includes all the device types installed on the server, including third-party devices.

</dd> <dt>

**wszDeviceName**
</dt> <dd>

A null-terminated Unicode string that specifies the name of the device on which the connection was made, such as "Hayes 9600" or "PCIMACISDN1".

</dd> <dt>

**wszMediaName**
</dt> <dd>

Specifies a null-terminated Unicode string that specifies the name of the media used for the connection, such as *rasser* or *rastapi*.

</dd> <dt>

**reserved**
</dt> <dd>

Reserved.

</dd> <dt>

**Flags**
</dt> <dd>

Specifies a set of bit flags that specify the nature of the connection made on this port. This member can be a combination of the following flags.



| Value                                                                                                                                                                        | Meaning                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GATEWAY_ACTIVE"></span><span id="gateway_active"></span><dl> <dt>**GATEWAY\_ACTIVE**</dt> </dl>             | If this flag is set, the NetBIOS gateway is active on the server.<br/>                                                                                                                                                                                                                                                                                                               |
| <span id="MESSENGER_PRESENT"></span><span id="messenger_present"></span><dl> <dt>**MESSENGER\_PRESENT**</dt> </dl>    | If this flag is set, the messenger service is running on the remote client.<br/>                                                                                                                                                                                                                                                                                                     |
| <span id="PORT_MULTILINKED"></span><span id="port_multilinked"></span><dl> <dt>**PORT\_MULTILINKED**</dt> </dl>       | If this flag is set, the port is multilinked with other ports. Use this information to display the connection status as a multilinked port. <br/> For a multilinked port, the [**RAS\_PORT\_STATISTICS**](ras-port-statistics-str.md) structure contains two sets of statistics: one for the port alone, and another for the combined ports in the multilink connection.<br/> |
| <span id="PPP_CLIENT"></span><span id="ppp_client"></span><dl> <dt>**PPP\_CLIENT**</dt> </dl>                         | If this flag is set, the remote client connected using PPP. If this flag is not set, the remote client connected using the AMB protocol.<br/>                                                                                                                                                                                                                                        |
| <span id="REMOTE_LISTEN"></span><span id="remote_listen"></span><dl> <dt>**REMOTE\_LISTEN**</dt> </dl>                | If this flag is set, the RemoteListen parameter of the NetBIOS gateway is set to 1 on the server.<br/>                                                                                                                                                                                                                                                                               |
| <span id="USER_AUTHENTICATED"></span><span id="user_authenticated"></span><dl> <dt>**USER\_AUTHENTICATED**</dt> </dl> | If this flag is set, a remote client is connected to the server and the user has been authenticated. Check this flag to ensure that a client is actually connected to a port.<br/>                                                                                                                                                                                                   |



 

If the MESSENGER\_PRESENT, GATEWAY\_ACTIVE, and REMOTE\_LISTEN flags are set, use the messenger service to send an administrative message to the remote client. If MESSENGER\_PRESENT and REMOTE\_LISTEN are set, but GATEWAY\_ACTIVE is not, send messages to the client only from the RAS server to which the client is connected.

</dd> <dt>

**wszUserName**
</dt> <dd>

A null-terminated Unicode string that specifies the name of the remote user connected to this port.

</dd> <dt>

**wszComputer**
</dt> <dd>

A null-terminated Unicode string that specifies the name of the remote client computer.

</dd> <dt>

**dwStartSessionTime**
</dt> <dd>

Specifies the time, in seconds from January 1, 1970, that the client connected to the RAS server on this port. Use the standard time functions to format this value for display.

</dd> <dt>

**wszLogonDomain**
</dt> <dd>

Specifies a null-terminated Unicode string that specifies the name of the domain on which the remote user was authenticated. This string is the domain name only, with no "\\\\" prefix.

</dd> <dt>

**fAdvancedServer**
</dt> <dd>

Specifies a flag that is nonzero if the RAS server associated with this port is an advanced server such as Windows 2000 Advanced Server. Use this information to determine the name of the server that has the user account database. If the RAS server is an advanced server, get the name of the user account server by concatenating the prefix "\\\\" to the name returned in the **wszLogonDomain** member. This is because for an advanced server the local logon domain name is the same as the server name. If the RAS server is a workstation, use the [**RasAdminGetUserAccountServer**](rasadmingetuseraccountserver.md) function to get the name of the user account server.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows XP<br/>                                                                |
| End of server support<br/>    | Windows Server 2003<br/>                                                       |
| Header<br/>                   | <dl> <dt>Rassapi.h</dt> </dl> |



## See also

<dl> <dt>

[Remote Access Service (RAS) Overview](about-remote-access-service.md)
</dt> <dt>

[RAS Server Administration Structures](ras-server-administration-structures.md)
</dt> <dt>

[**RAS\_PORT\_1**](ras-port-1-str.md)
</dt> <dt>

[**RAS\_PORT\_STATISTICS**](ras-port-statistics-str.md)
</dt> <dt>

[**RasAdminGetUserAccountServer**](rasadmingetuseraccountserver.md)
</dt> <dt>

[**RasAdminPortEnum**](rasadminportenum.md)
</dt> </dl>

 

 





