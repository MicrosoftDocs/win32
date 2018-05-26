---
title: '\_IVMRCClientControlEvents interface'
description: Defines the outgoing event interface for the IVMRCClientControl interface.
ms.assetid: a626eedf-8f7b-40c1-802e-f8a39ec15918
keywords:
- _IVMRCClientControlEvents interface Virtual Server
- _IVMRCClientControlEvents interface Virtual Server , described
topic_type:
- apiref
api_name:
- _IVMRCClientControlEvents
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# \_IVMRCClientControlEvents interface

The **\_IVMRCClientControlEvents** interface defines the outgoing event interface for the [**IVMRCClientControl**](ivmrcclientcontrol.md) interface.

## When to implement

The client implements these methods to receive events sent from [**IVMRCClientControl**](ivmrcclientcontrol.md).

## Members

The **\_IVMRCClientControlEvents** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **\_IVMRCClientControlEvents** also has these types of members:

-   [Methods](#methods)

### Methods

The **\_IVMRCClientControlEvents** interface has these methods.



| Method                                                                   | Description                                                             |
|:-------------------------------------------------------------------------|:------------------------------------------------------------------------|
| [**OnStateChanged**](-ivmrcclientcontrolevents-onstatechanged.md)       | Called when the VMRC client connection state changes.<br/>        |
| [**OnSwitchedDisplay**](-ivmrcclientcontrolevents-onswitcheddisplay.md) | Called when the VMRC client switches to a different machine.<br/> |



 

## Remarks

This interface name begins with an underscore character (\_) so that the type library browser does not display the name of the interface in the list of interfaces for the type library.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[Virtual Machine Remote Client Interfaces](vmrc-interfaces.md)
</dt> <dt>

[\_IVMRCClientControl Methods](-ivmrcclientcontrolevents-methods.md)
</dt> </dl>

 

 





