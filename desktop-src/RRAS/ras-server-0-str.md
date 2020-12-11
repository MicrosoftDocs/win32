---
title: RAS_SERVER_0 structure (Rassapi.h)
description: The RAS\_SERVER\_0 structure is used by the RasAdminServerGetInfo function to return information about the ports configured on a RAS server.
ms.assetid: 8818ad68-b528-45fe-9ff4-eea194259f25
keywords:
- RAS_SERVER_0 structure RAS
- PRAS_SERVER_0 structure pointer RAS
topic_type:
- apiref
api_name:
- RAS_SERVER_0
api_location:
- Rassapi.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# RAS\_SERVER\_0 structure

\[The **RAS\_SERVER\_0** structure is not supported as of Windows Vista.\]

The **RAS\_SERVER\_0** structure is used by the [**RasAdminServerGetInfo**](rasadminservergetinfo.md) function to return information about the ports configured on a RAS server.

## Syntax


```C++
typedef struct _RAS_SERVER_0 {
  WORD  TotalPorts;
  WORD  PortsInUse;
  DWORD RasVersion;
} RAS_SERVER_0, *PRAS_SERVER_0;
```



## Members

<dl> <dt>

**TotalPorts**
</dt> <dd>

Specifies the total number of ports configured on the RAS server that are available for remote clients to connect to. For example, if the total number of ports configured for dialing in to a server is four, but one of the ports is currently in use for dialing out, **TotalPorts** is three.

</dd> <dt>

**PortsInUse**
</dt> <dd>

Specifies the number of ports currently in use by remote clients.

</dd> <dt>

**RasVersion**
</dt> <dd>

Specifies the version of the RAS server. Use this information to take version-specific action. This member is one of the following values.



| Value                                                                                                                                                                  | Meaning                                                                         |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| <span id="RASDOWNLEVEL"></span><span id="rasdownlevel"></span><dl> <dt>**RASDOWNLEVEL**</dt> </dl>              | Indicates a LAN Manager version 1.0 RAS server.<br/>                      |
| <span id="RASADMIN_35"></span><span id="rasadmin_35"></span><dl> <dt>**RASADMIN\_35**</dt> </dl>                | Indicates a Windows NT Server 3.51 and earlier RAS server or client.<br/> |
| <span id="RASADMIN_CURRENT"></span><span id="rasadmin_current"></span><dl> <dt>**RASADMIN\_CURRENT**</dt> </dl> | Indicates a Windows NT 4.0 RAS server or client.<br/>                     |



 

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

[**RasAdminServerGetInfo**](rasadminservergetinfo.md)
</dt> </dl>

 

 





