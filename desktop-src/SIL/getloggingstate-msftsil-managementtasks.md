---
title: GetLoggingState method of the MsftSil\_ManagementTasks class
description: Verifies whether Software Inventory Logging is enabled, and optionally enables or disables the feature.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '27b8557d-fd79-4865-904e-8206b51f2fb1'
ms.prod: 'windows-server-dev'
ms.technology:
- 'software-inventory-logging'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetLoggingState method Software Inventory Logging", "GetLoggingState method Software Inventory Logging , MsftSil_ManagementTasks class", "MsftSil_ManagementTasks class Software Inventory Logging , GetLoggingState method"]
topic_type:
- apiref
api_name:
- MsftSil_ManagementTasks.GetLoggingState
api_location:
- SILProvider.dll
api_type:
- COM
---

# GetLoggingState method of the MsftSil\_ManagementTasks class

Verifies whether Software Inventory Logging is enabled, and optionally enables or disables the feature.

## Syntax


```mof
uint32 GetLoggingState(
  [out] uint8 state
);
```



## Parameters

<dl> <dt>

*state* \[out\]
</dt> <dd>

On success, returns an **uint8** that contains the setting to enable or disable the feature.

<dt>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>

**Stopped** (0)


</dt> <dd></dd> <dt>

<span id="Running"></span><span id="running"></span><span id="RUNNING"></span>

**Running** (1)


</dt> <dd></dd> </dl> </dd> </dl>

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

 

 





