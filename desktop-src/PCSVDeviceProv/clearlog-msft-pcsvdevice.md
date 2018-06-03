---
Description: Requests that the specified log on the physical computer system be cleared of all entries.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 23437a61-e0ec-40a5-bd78-7dff423b32d5
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: ClearLog method of the MSFT\_PCSVDevice class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClearLog method of the MSFT\_PCSVDevice class

Requests that the specified log on the physical computer system be cleared of all entries.

## Syntax


```mof
uint32 ClearLog(
  [in] string LogInstanceID
);
```



## Parameters

<dl> <dt>

*LogInstanceID* \[in\]
</dt> <dd>

Specifies the log to be cleared. This parameter corresponds to the **CIM\_RecordLog**.**InstanceID** property.

</dd> </dl>

## Return value

This method returns one of the following values.

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Failed** (2)
</dt> <dt>

**DMTF Reserved** (3 32767)
</dt> <dt>

**Vendor Reserved** (32768 65535)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                         |
| Namespace<br/>                | Root\\Microsoft\\Windows\\HardwareManagement<br/>                                   |
| MOF<br/>                      | <dl> <dt>PCSVDevice.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PCSVDevice.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_PCSVDevice**](msft-pcsvdevice.md)
</dt> </dl>

 

 




