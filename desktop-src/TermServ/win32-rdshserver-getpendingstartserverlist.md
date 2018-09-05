---
title: GetPendingStartServerList method of the Win32_RDSHServer class
description: Retrieves a list of server waiting to start.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7af7a0e7-dc00-4e3a-8e0c-5987bd2bc3a2
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- GetPendingStartServerList method Remote Desktop Services
- GetPendingStartServerList method Remote Desktop Services , Win32_RDSHServer class
- Win32_RDSHServer class Remote Desktop Services , GetPendingStartServerList method
topic_type:
- apiref
api_name:
- Win32_RDSHServer.GetPendingStartServerList
api_location:
- RDMS.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetPendingStartServerList method of the Win32\_RDSHServer class

Retrieves a list of server waiting to start.

## Syntax


```mof
uint32 GetPendingStartServerList(
  [in]  uint32 maxServers,
  [out] string ServerFQDNs[]
);
```



## Parameters

<dl> <dt>

*maxServers* \[in\]
</dt> <dd>

The maximum number of servers to return in the list.

</dd> <dt>

*ServerFQDNs* \[out\]
</dt> <dd>

On success, contains a collection of fully-qualified domain names of the servers waiting to start.

</dd> </dl>

## Remarks

The list of servers is reset after every call, so that the next call will not get a duplicate server.

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                              |
| Namespace<br/>                | Root\\cimv2\\rdms<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>         |



## See also

<dl> <dt>

[**Win32\_RDSHServer**](win32-rdshserver.md)
</dt> </dl>

 

 





