---
description: The HWConfig class is the parent class for hardware configuration events on Windows XP. The following syntax is simplified from MOF code.
ms.assetid: 47f062c0-fdf0-4beb-906d-257571324de9
title: HWConfig class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- HWConfig
api_type: 
- NA
api_location: 
---

# HWConfig class

The **HWConfig** class is the parent class for hardware configuration events on Windows XP.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[Guid("{01853a65-418f-4f36-aefc-dc0f1d2fd235}")]
class HWConfig : MSNT_SystemTrace
{
};
```

## Members

The **HWConfig** class does not define any members.

## Remarks

These events provide the hardware configuration of the computer. Unlike other NT Kernel Logger events, the kernel session automatically generates hardware configuration events; you do not enable these events when starting the NT Kernel Logger session.

**Windows 2000:** Not supported.

For hardware configuration events on Windows Vista and Windows Server 2003, see the [SystemConfig](systemconfig.md) class.

Event trace consumers can implement special processing for hardware configuration events by calling the [**SetTraceCallback**](/windows/win32/api/evntrace/nf-evntrace-settracecallback) function and specifying [**EventTraceConfigGuid**](nt-kernel-logger-constants.md) as the *pGuid* parameter. Use the following event types to identify the actual hardware configuration event when consuming events.



| Event type                                                                      | Description                                                                                                                                      |
|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| **EVENT\_TRACE\_TYPE\_CONFIG\_CPU**(Event type value is 10)<br/>          | CPU configuration event. The [**HWConfig\_CPU**](hwconfig-cpu.md) MOF classes defines the event data for this event.                            |
| **EVENT\_TRACE\_TYPE\_CONFIG\_LOGICALDISK**(Event type value is 12)<br/>  | Logical disk configuration event. The [**HWConfig\_LogDisk**](hwconfig-logdisk.md) MOF classes MOF class defines the event data for this event. |
| **EVENT\_TRACE\_TYPE\_CONFIG\_NIC**(Event type value is 13)<br/>          | NIC configuration event. The [**HWConfig\_NIC**](hwconfig-nic.md) MOF classes defines the event data for this event.                            |
| **EVENT\_TRACE\_TYPE\_CONFIG\_PHYSICALDISK**(Event type value is 11)<br/> | Physical disk configuration event. The [**HWConfig\_PhyDisk**](hwconfig-phydisk.md) MOF classes defines the event data for this event.          |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                   |



## See also

<dl> <dt>

[**MSNT\_SystemTrace**](msnt-systemtrace.md)
</dt> <dt>

[**HWConfig\_CPU**](hwconfig-cpu.md)
</dt> <dt>

[**HWConfig\_LogDisk**](hwconfig-logdisk.md)
</dt> <dt>

[**HWConfig\_NIC**](hwconfig-nic.md)
</dt> <dt>

[**HWConfig\_PhyDisk**](hwconfig-phydisk.md)
</dt> </dl>

 

 
