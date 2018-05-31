---
title: IVMMouse interface
description: The IVMMouse interface controls the mouse device within a virtual machine.
ms.assetid: e68e228d-2b7e-49c7-bf9a-d56cfc662c8c
keywords:
- IVMMouse interface Virtual Server
- IVMMouse interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMMouse
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMMouse interface

The **IVMMouse** interface controls the mouse device within a virtual machine. The **IVMMouse** for a virtual machine can be retrieved using the [**IVMVirtualMachine::Mouse**](ivmvirtualmachine-mouse.md) property. Coordinates for the mouse device can be represented either in absolute coordinates or in delta coordinates. Use the [**UsingAbsoluteCoordinates**](ivmmouse-usingabsolutecoordinates.md) property to distinguish between the two methods of coordinate representation. Note that retrieving the current cursor position and the use of absolute coordinates are only supported if the guest operating system has Additions installed.

## Members

The **IVMMouse** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMMouse** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMMouse** interface has these methods.



| Method                                  | Description                                                                                     |
|:----------------------------------------|:------------------------------------------------------------------------------------------------|
| [**Click**](ivmmouse-click.md)         | Simulates a mouse button click (press and release) using an enumerated button index.<br/> |
| [**GetButton**](ivmmouse-getbutton.md) | Retrieves the current state (up or down) of the specified mouse button.<br/>              |
| [**SetButton**](ivmmouse-setbutton.md) | Sets the current state (up or down) of the specified mouse button.<br/>                   |



 

### Properties

The **IVMMouse** interface has these properties.



| Property                                                                         | Access type           | Description                                                                                                                  |
|:---------------------------------------------------------------------------------|:----------------------|:-----------------------------------------------------------------------------------------------------------------------------|
| [**HorizontalPosition**](ivmmouse-horizontalposition.md)<br/>             | Read/write<br/> | The absolute x-coordinate of the mouse. Not valid when using delta coordinates.<br/>                                   |
| [**ScrollWheelPosition**](ivmmouse-scrollwheelposition.md)<br/>           | Write-only<br/> | The current z-coordinate of the mouse. The indicated value can only represent delta coordinates.<br/>                  |
| [**UsingAbsoluteCoordinates**](ivmmouse-usingabsolutecoordinates.md)<br/> | Read/write<br/> | Indicates whether the mouse device is set to use absolute coordinates, **FALSE** if set to use delta coordinates.<br/> |
| [**VerticalPosition**](ivmmouse-verticalposition.md)<br/>                 | Read/write<br/> | The absolute y-coordinate of the mouse. Not valid when using delta coordinates.<br/>                                   |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5)
</dt> </dl>

 

 





