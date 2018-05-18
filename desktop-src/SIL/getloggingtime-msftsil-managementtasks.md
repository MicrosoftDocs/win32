---
title: GetLoggingTime method of the MsftSil\_ManagementTasks class
description: Gets the start time after which the Software Inventory Logging engine collects data.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '34cd5748-6c19-4456-bdea-f1cd8828a01a'
ms.prod: 'windows-server-dev'
ms.technology:
- 'software-inventory-logging'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetLoggingTime method Software Inventory Logging", "GetLoggingTime method Software Inventory Logging , MsftSil_ManagementTasks class", "MsftSil_ManagementTasks class Software Inventory Logging , GetLoggingTime method"]
topic_type:
- apiref
api_name:
- MsftSil_ManagementTasks.GetLoggingTime
api_location:
- SILProvider.dll
api_type:
- COM
---

# GetLoggingTime method of the MsftSil\_ManagementTasks class

Gets the start time after which the Software Inventory Logging engine collects data.

## Syntax


```mof
uint32 GetLoggingTime(
  [out] datetime time
);
```



## Parameters

<dl> <dt>

*time* \[out\]
</dt> <dd>

On success, contains the current logging time in Coordinated Universal Time (UTC).

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

 

 





