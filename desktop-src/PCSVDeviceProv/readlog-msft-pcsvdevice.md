---
Description: Reads the BMC SEL log.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 03a58db7-be7c-418b-a88f-0cd2455f4cbb
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: ReadLog method of the MSFT\_PCSVDevice class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ReadLog method of the MSFT\_PCSVDevice class

Reads the BMC SEL log.

## Syntax


```mof
uint32 ReadLog(
  [out]     MSFT_PCSVLogRecord  LogRecords[],
  [in, out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*LogRecords* \[out\]
</dt> <dd>

Streams BMC SEL entries as an array of [**MSFT\_PCSVLogRecord**](msft-pcsvlogrecord.md) instances.

</dd> <dt>

*Job* \[in, out\]
</dt> <dd>

Reference to the job spawned if the operation continues after the method returns. May be **NULL** if the task is completed.

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
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\HardwareManagement<br/>                                   |
| MOF<br/>                      | <dl> <dt>Pcsvdevice.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PCSVdevice.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_PCSVDevice**](msft-pcsvdevice.md)
</dt> </dl>

 

 




