---
title: GetTargetUri method of the MsftSil\_ManagementTasks class
description: Retrieves and optionally specifies the URI to which the Software Inventory Logging stream provider publishes data.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ec65cb83-e8bf-41b1-a6f8-f22d98599d18
ms.prod: windows-server-dev
ms.technology:
- software-inventory-logging
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetTargetUri method Software Inventory Logging
- GetTargetUri method Software Inventory Logging , MsftSil_ManagementTasks class
- MsftSil_ManagementTasks class Software Inventory Logging , GetTargetUri method
topic_type:
- apiref
api_name:
- MsftSil_ManagementTasks.GetTargetUri
api_location:
- SILProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetTargetUri method of the MsftSil\_ManagementTasks class

Retrieves and optionally specifies the URI to which the Software Inventory Logging stream provider publishes data.

## Syntax


```mof
uint32 GetTargetUri(
  [out] string uri,
  [out] string certificateThumbprint
);
```



## Parameters

<dl> <dt>

*uri* \[out\]
</dt> <dd>

A string that receives the URI of the resource.

</dd> <dt>

*certificateThumbprint* \[out\]
</dt> <dd>

On success, returns a string that contains the certificate thumb print of the resource.

</dd> </dl>

## Return value

If this method succeeds, it returns 0. If this method fails, it returns 1. For a complete list of return values, see [**MI\_Result**](https://msdn.microsoft.com/library/hh437490) enumeration.

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                          |
| Namespace<br/>                | Root\\InventoryLogging<br/>                                                          |
| MOF<br/>                      | <dl> <dt>SILProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SILProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MsftSil\_ManagementTasks**](msftsil-managementtasks.md)
</dt> </dl>

 

 





