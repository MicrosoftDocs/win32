---
title: SetLoggingTime method of the MsftSil\_ManagementTasks class
description: Configures the start time after which the Software Inventory Logging engine collects data.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '3ccedb22-a6f6-4190-b366-098a9199d062'
ms.prod: 'windows-server-dev'
ms.technology:
- 'software-inventory-logging'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetLoggingTime method Software Inventory Logging", "SetLoggingTime method Software Inventory Logging , MsftSil_ManagementTasks class", "MsftSil_ManagementTasks class Software Inventory Logging , SetLoggingTime method"]
topic_type:
- apiref
api_name:
- MsftSil_ManagementTasks.SetLoggingTime
api_location:
- SILProvider.dll
api_type:
- COM
---

# SetLoggingTime method of the MsftSil\_ManagementTasks class

Configures the start time after which the Software Inventory Logging engine collects data.

## Syntax


```mof
uint32 SetLoggingTime(
  [in] datetime time
);
```



## Parameters

<dl> <dt>

*time* \[in\]
</dt> <dd>

The new logging time in Coordinated Universal Time (UTC).

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

 

 





