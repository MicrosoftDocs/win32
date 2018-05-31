---
title: VMShutdownAction enumeration
description: The VMShutdownAction enumeration specifies how to shut down a virtual machine.
ms.assetid: 53fedb71-3cee-43fe-b98c-b3ffe3e12711
keywords:
- VMShutdownAction enumeration Virtual Server
topic_type:
- apiref
api_name:
- VMShutdownAction
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

# VMShutdownAction enumeration

The **VMShutdownAction** enumeration specifies how to shut down a virtual machine.

## Syntax


```C++
typedef enum  { 
  vmShutdownAction_Save      = 0,
  vmShutdownAction_TurnOff   = 1,
  vmShutdownAction_Shutdown  = 2
} VMShutdownAction;
```



## Constants

<dl> <dt>

<span id="vmShutdownAction_Save"></span><span id="vmshutdownaction_save"></span><span id="VMSHUTDOWNACTION_SAVE"></span>**vmShutdownAction\_Save**
</dt> <dd>

Save the virtual machine state.

</dd> <dt>

<span id="vmShutdownAction_TurnOff"></span><span id="vmshutdownaction_turnoff"></span><span id="VMSHUTDOWNACTION_TURNOFF"></span>**vmShutdownAction\_TurnOff**
</dt> <dd>

Turn off the virtual machine without undoing the drives.

</dd> <dt>

<span id="vmShutdownAction_Shutdown"></span><span id="vmshutdownaction_shutdown"></span><span id="VMSHUTDOWNACTION_SHUTDOWN"></span>**vmShutdownAction\_Shutdown**
</dt> <dd>

Shut down the guest operating system on the virtual machine without undoing the drives. This action requires the Additions feature.

</dd> </dl>

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



 

 





