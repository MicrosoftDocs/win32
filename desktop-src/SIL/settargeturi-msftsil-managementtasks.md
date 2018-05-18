---
title: SetTargetUri method of the MsftSil\_ManagementTasks class
description: Specifies the URI to which the Software Inventory Logging stream provider publishes data.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f7edd008-b057-4c94-b991-c02414ca504c'
ms.prod: 'windows-server-dev'
ms.technology:
- 'software-inventory-logging'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetTargetUri method Software Inventory Logging", "SetTargetUri method Software Inventory Logging , MsftSil_ManagementTasks class", "MsftSil_ManagementTasks class Software Inventory Logging , SetTargetUri method"]
topic_type:
- apiref
api_name:
- MsftSil_ManagementTasks.SetTargetUri
api_location:
- SILProvider.dll
api_type:
- COM
---

# SetTargetUri method of the MsftSil\_ManagementTasks class

Specifies the URI to which the Software Inventory Logging stream provider publishes data.

## Syntax


```mof
uint32 SetTargetUri(
  [in] string uri,
  [in] string certificateThumbprint
);
```



## Parameters

<dl> <dt>

*uri* \[in\]
</dt> <dd>

The URI of the resource.

</dd> <dt>

*certificateThumbprint* \[in\]
</dt> <dd>

The certificate thumb print of the resource.

</dd> </dl>

## Return value

If this method succeeds, it returns 0. If this method fails, it returns 1. For a complete list of return values, see [**MI\_Result**](https://msdn.microsoft.com/library/hh437490) enumeration.

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                          |
| Namespace<br/>                | Root\\InventoryLogging<br/>                                                          |
| MOF<br/>                      | <dl> <dt>SILProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SILProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MsftSil\_ManagementTasks**](msftsil-managementtasks.md)
</dt> </dl>

 

 





