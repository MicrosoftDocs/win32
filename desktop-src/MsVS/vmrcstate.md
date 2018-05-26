---
title: VMRCState enumeration
description: The VMRCState enumeration specifies the state of the IVMRCClientControl object.
ms.assetid: 14d61129-a8cc-40ea-b236-b43c4957918f
keywords:
- VMRCState enumeration Virtual Server
topic_type:
- apiref
api_name:
- VMRCState
api_location:
- VMRCClientControl.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# VMRCState enumeration

The **VMRCState** enumeration specifies the state of the [**IVMRCClientControl**](ivmrcclientcontrol.md) object.

## Syntax


```C++
typedef enum  { 
  vmrcState_NotConnected      = 0,
  vmrcState_Connecting        = 1,
  vmrcState_Authenticating    = 2,
  vmrcState_Connected         = 3,
  vmrcState_ConnectionFailed  = 4
} VMRCState;
```



## Constants

<dl> <dt>

<span id="vmrcState_NotConnected"></span><span id="vmrcstate_notconnected"></span><span id="VMRCSTATE_NOTCONNECTED"></span>**vmrcState\_NotConnected**
</dt> <dd>

The client control is not connected.

</dd> <dt>

<span id="vmrcState_Connecting"></span><span id="vmrcstate_connecting"></span><span id="VMRCSTATE_CONNECTING"></span>**vmrcState\_Connecting**
</dt> <dd>

The client control is attempting to connect to the VMRC server.

</dd> <dt>

<span id="vmrcState_Authenticating"></span><span id="vmrcstate_authenticating"></span><span id="VMRCSTATE_AUTHENTICATING"></span>**vmrcState\_Authenticating**
</dt> <dd>

The client control is validating the user credentials with the VMRC server.

</dd> <dt>

<span id="vmrcState_Connected"></span><span id="vmrcstate_connected"></span><span id="VMRCSTATE_CONNECTED"></span>**vmrcState\_Connected**
</dt> <dd>

The client control is connected to the VMRC server.

</dd> <dt>

<span id="vmrcState_ConnectionFailed"></span><span id="vmrcstate_connectionfailed"></span><span id="VMRCSTATE_CONNECTIONFAILED"></span>**vmrcState\_ConnectionFailed**
</dt> <dd>

The client control failed to connect to the VMRC server.

</dd> </dl>

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VMRCClientControl.h</dt> </dl>    |



 

 





