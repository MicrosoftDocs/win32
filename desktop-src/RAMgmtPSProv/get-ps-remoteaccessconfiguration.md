---
title: Get method of the PS\_RemoteAccessConfiguration class
description: Retrieves a remote access configuration.
audience: developer
ms.assetid: 4bca8d34-12af-4f7c-8888-b0466a745704
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_RemoteAccessConfiguration class
- PS_RemoteAccessConfiguration class, Get method
topic_type:
- apiref
api_name:
- PS_RemoteAccessConfiguration.Get
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the PS\_RemoteAccessConfiguration class

Retrieves a remote access configuration.

## Syntax


```mof
static uint32 Get(
  [out] RemoteAccessConfiguration cmdletOutput
);
```



## Parameters

<dl> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The [**RemoteAccessConfiguration**](remoteaccessconfiguration.md) object that receives the retrieved remote access configuration information.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_RemoteAccessConfiguration**](ps-remoteaccessconfiguration.md)
</dt> </dl>

 

 





