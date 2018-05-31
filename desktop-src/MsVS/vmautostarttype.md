---
title: VMAutoStartType enumeration
description: The VMAutoStartType enumeration specifies how a virtual machine should be automatically started when Virtual Server is started.
ms.assetid: 458ab025-f598-439d-840d-e1c75935ed89
keywords:
- VMAutoStartType enumeration Virtual Server
topic_type:
- apiref
api_name:
- VMAutoStartType
api_location:
- VsComInterfaces.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# VMAutoStartType enumeration

The **VMAutoStartType** enumeration specifies how a virtual machine should be automatically started when Virtual Server is started.

## Syntax


```C++
typedef enum  { 
  vmAutoStart_Never            = 0,
  vmAutoStart_Always           = 1,
  vmAutoStart_IfRunningAtQuit  = 2
} VMAutoStartType;
```



## Constants

<dl> <dt>

<span id="vmAutoStart_Never"></span><span id="vmautostart_never"></span><span id="VMAUTOSTART_NEVER"></span>**vmAutoStart\_Never**
</dt> <dd>

Never automatically start the virtual machine.

</dd> <dt>

<span id="vmAutoStart_Always"></span><span id="vmautostart_always"></span><span id="VMAUTOSTART_ALWAYS"></span>**vmAutoStart\_Always**
</dt> <dd>

Always automatically start the virtual machine.

</dd> <dt>

<span id="vmAutoStart_IfRunningAtQuit"></span><span id="vmautostart_ifrunningatquit"></span><span id="VMAUTOSTART_IFRUNNINGATQUIT"></span>**vmAutoStart\_IfRunningAtQuit**
</dt> <dd>

Automatically start the virtual machine if it was running when Virtual Server was last stopped.

</dd> </dl>

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



 

 





