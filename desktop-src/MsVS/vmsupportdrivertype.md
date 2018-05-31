---
title: VMSupportDriverType enumeration
description: The VMSupportDriverType enumeration specifies the type of support driver used by Virtual Server.
ms.assetid: f12e934b-c25c-4ca9-bd44-93d51e8b5475
keywords:
- VMSupportDriverType enumeration Virtual Server
topic_type:
- apiref
api_name:
- VMSupportDriverType
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
api_location:
- VsComInterfaces.h
api_type:
- HeaderDef
---

# VMSupportDriverType enumeration

The **VMSupportDriverType** enumeration specifies the type of support driver used by Virtual Server.

## Syntax


```C++
typedef enum  { 
  vmSupportDriver_InvalidType            = -1,
  vmSupportDriver_VirtualMachineMonitor  = 0,
  vmSupportDriver_NetworkServices        = 1
} VMSupportDriverType;
```



## Constants

<dl> <dt>

<span id="vmSupportDriver_InvalidType"></span><span id="vmsupportdriver_invalidtype"></span><span id="VMSUPPORTDRIVER_INVALIDTYPE"></span>**vmSupportDriver\_InvalidType**
</dt> <dd>

Invalid driver type.

</dd> <dt>

<span id="vmSupportDriver_VirtualMachineMonitor"></span><span id="vmsupportdriver_virtualmachinemonitor"></span><span id="VMSUPPORTDRIVER_VIRTUALMACHINEMONITOR"></span>**vmSupportDriver\_VirtualMachineMonitor**
</dt> <dd>

The Virtual Machine Monitor (VMM) driver.

</dd> <dt>

<span id="vmSupportDriver_NetworkServices"></span><span id="vmsupportdriver_networkservices"></span><span id="VMSUPPORTDRIVER_NETWORKSERVICES"></span>**vmSupportDriver\_NetworkServices**
</dt> <dd>

The network services driver.

</dd> </dl>

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



 

 





