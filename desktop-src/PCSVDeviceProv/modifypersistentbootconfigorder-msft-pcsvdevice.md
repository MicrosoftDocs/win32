---
Description: Changes the order of boot sources for the persistent boot configuration specified by the MSFT\_PCSVDevice.PersistentBootConfigOrder property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e633bd88-47c4-4de0-baee-3455721bb8c9
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: ModifyPersistentBootConfigOrder method of the MSFT\_PCSVDevice class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ModifyPersistentBootConfigOrder method of the MSFT\_PCSVDevice class

Changes the order of boot sources for the persistent boot configuration specified by the [**MSFT\_PCSVDevice**](msft-pcsvdevice.md).**PersistentBootConfigOrder** property.

## Syntax


```mof
uint32 ModifyPersistentBootConfigOrder(
  [in]      string              StructuredBootString[],
  [in, out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*StructuredBootString* \[in\]
</dt> <dd>

Specifies the boot sources in an ordered array of strings.

</dd> <dt>

*Job* \[in, out\]
</dt> <dd>

On return contains a reference to the job, but can be null if the task is completed.

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

**Reserved** (3 4095)
</dt> <dt>

**Job Started** (4096)
</dt> <dt>

**DMTF Reserved** (4097 32767)
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

 

 




