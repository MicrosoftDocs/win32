---
title: Get method of the PS\_RemoteAccessHealthLocal class
description: This cmdlet is used to obtain the current health of a Remote Access deployment.
audience: developer
ms.assetid: 061c07d8-af20-4834-bf66-e7c3b60be475
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_RemoteAccessHealthLocal class
- PS_RemoteAccessHealthLocal class, Get method
topic_type:
- apiref
api_name:
- PS_RemoteAccessHealthLocal.Get
api_location:
- RAServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the PS\_RemoteAccessHealthLocal class

This cmdlet is used to obtain the current health of a Remote Access deployment.

## Syntax


```mof
uint32 Get(
  [in]  boolean                       Refresh,
  [out] RemoteAccessServerHealthLocal cmdletOutput
);
```



## Parameters

<dl> <dt>

*Refresh* \[in\]
</dt> <dd>

Specifying this parameter indicates that the health details should be recomputed.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Remote Access server health data.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_RemoteAccessHealthLocal**](ps-remoteaccesshealthlocal.md)
</dt> </dl>

 

 





