---
title: SetLoggingState method of the MsftSil\_ManagementTasks class
description: Enables or disables Software Inventory Logging.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e878d908-dcfa-45b0-95d3-cef693c9974e
ms.prod: windows-server-dev
ms.technology:
- software-inventory-logging
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetLoggingState method Software Inventory Logging
- SetLoggingState method Software Inventory Logging , MsftSil_ManagementTasks class
- MsftSil_ManagementTasks class Software Inventory Logging , SetLoggingState method
topic_type:
- apiref
api_name:
- MsftSil_ManagementTasks.SetLoggingState
api_location:
- SILProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetLoggingState method of the MsftSil\_ManagementTasks class

Enables or disables Software Inventory Logging.

## Syntax


```mof
uint32 SetLoggingState(
  [in] uint8 state
);
```



## Parameters

<dl> <dt>

*state* \[in\]
</dt> <dd>

A **uint8** that receives the setting to enable or disable the feature.

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
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                          |
| Namespace<br/>                | Root\\InventoryLogging<br/>                                                          |
| MOF<br/>                      | <dl> <dt>SILProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SILProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MsftSil\_ManagementTasks**](msftsil-managementtasks.md)
</dt> </dl>

 

 





