---
description: SystemConfig class - This class is the parent class for hardware configuration events. The following syntax is simplified from MOF code.
ms.assetid: 720c2366-bd68-4895-bfaf-74aa9b64ba4a
title: SystemConfig class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SystemConfig
api_type: 
- NA
api_location: 
---

# SystemConfig class

This class is the parent class for hardware configuration events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[Guid("{01853a65-418f-4f36-aefc-dc0f1d2fd235}"), EventVersion(2)]
class SystemConfig : MSNT_SystemTrace
{
};
```

## Members

The **SystemConfig** class does not define any members.

## Remarks

These events provide the hardware configuration of the computer. Unlike other NT Kernel Logger events, the kernel session automatically generates hardware configuration events; you do not enable these events when starting the NT Kernel Logger session.

For hardware configuration events on Windows XP, see the [HWConfig](hwconfig.md) class.

Event trace consumers can implement special processing for hardware configuration events by calling the [**SetTraceCallback**](/windows/win32/api/evntrace/nf-evntrace-settracecallback) function and specifying [**EventTraceConfigGuid**](nt-kernel-logger-constants.md) as the *pGuid* parameter. Use the following event types to identify the actual hardware configuration event when consuming events.



| Event type                                                                      | Description                                                                                                                                                                         |
|---------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **EVENT\_TRACE\_TYPE\_CONFIG\_CPU**(Event type value is 10)<br/>          | CPU configuration event. The [**SystemConfig\_CPU**](systemconfig-cpu.md) MOF classes defines the event data for this event.                                                       |
| **EVENT\_TRACE\_TYPE\_CONFIG\_IDECHANNEL**(Event type value is 23)<br/>   | Primary and secondary IDE channel configuration event. The [**SystemConfig\_IDEChannel**](systemconfig-idechannel.md) MOF classes MOF class defines the event data for this event. |
| **EVENT\_TRACE\_TYPE\_CONFIG\_IRQ**(Event type value is 21)<br/>          | Interrupt request (IRQ) event. The [**SystemConfig\_IRQ**](systemconfig-irq.md) MOF classes MOF class defines the event data for this event.                                       |
| **EVENT\_TRACE\_TYPE\_CONFIG\_LOGICALDISK**(Event type value is 12)<br/>  | Logical disk configuration event. The [**SystemConfig\_LogDisk**](systemconfig-logdisk.md) MOF classes MOF class defines the event data for this event.                            |
| **EVENT\_TRACE\_TYPE\_CONFIG\_NETINFO**(Event type value is 17)<br/>      | Network iformation event. The [**SystemConfig\_Network**](systemconfig-network.md) MOF class defines the event data for this event.                                                |
| **EVENT\_TRACE\_TYPE\_CONFIG\_NIC**(Event type value is 13)<br/>          | NIC configuration event. The [**SystemConfig\_NIC**](systemconfig-nic.md) MOF classes defines the event data for this event.                                                       |
| **EVENT\_TRACE\_TYPE\_CONFIG\_PHYSICALDISK**(Event type value is 11)<br/> | Physical disk configuration event. The [**SystemConfig\_PhyDisk**](systemconfig-phydisk.md) MOF classes defines the event data for this event.                                     |
| **EVENT\_TRACE\_TYPE\_CONFIG\_PNP**(Event type value is 22)<br/>          | Plug and play event. The [**SystemConfig\_PNP**](systemconfig-pnp.md) MOF classes MOF class defines the event data for this event.                                                 |
| **EVENT\_TRACE\_TYPE\_CONFIG\_POWER**(Event type value is 16)<br/>        | Power configuration event. The [**SystemConfig\_Power**](systemconfig-power.md) MOF class defines the event data for this event.                                                   |
| **EVENT\_TRACE\_TYPE\_CONFIG\_SERVICES**(Event type value is 15)<br/>     | Services configuration event. The [**SystemConfig\_Services**](systemconfig-services.md) MOF class defines the event data for this event.                                          |
| **EVENT\_TRACE\_TYPE\_CONFIG\_VIDEO**(Event type value is 14)<br/>        | Graphics adapter configuration event. The [**SystemConfig\_Video**](systemconfig-video.md) MOF class defines the event data for this event.                                        |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**MSNT\_SystemTrace**](msnt-systemtrace.md)
</dt> <dt>

[**SystemConfig\_CPU**](systemconfig-cpu.md)
</dt> <dt>

[**SystemConfig\_IDEChannel**](systemconfig-idechannel.md)
</dt> <dt>

[**SystemConfig\_IRQ**](systemconfig-irq.md)
</dt> <dt>

[**SystemConfig\_LogDisk**](systemconfig-logdisk.md)
</dt> <dt>

[**SystemConfig\_Network**](systemconfig-network.md)
</dt> <dt>

[**SystemConfig\_NIC**](systemconfig-nic.md)
</dt> <dt>

[**SystemConfig\_PhyDisk**](systemconfig-phydisk.md)
</dt> <dt>

[**SystemConfig\_PNP**](systemconfig-pnp.md)
</dt> <dt>

[**SystemConfig\_Power**](systemconfig-power.md)
</dt> <dt>

[**SystemConfig\_Services**](systemconfig-services.md)
</dt> <dt>

[**SystemConfig\_Video**](systemconfig-video.md)
</dt> <dt>

[**SystemConfig\_V0**](systemconfig-v0.md)
</dt> </dl>

 

 
