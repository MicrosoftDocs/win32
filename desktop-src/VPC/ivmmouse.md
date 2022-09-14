---
title: IVMMouse interface (VPCCOMInterfaces.h)
description: Controls the mouse device within a VM.
ms.assetid: 13bbf980-aafd-4c63-b1cb-60f00b738d1f
keywords:
- IVMMouse interface Virtual PC
- IVMMouse interface Virtual PC , described
topic_type:
- apiref
api_name:
- IVMMouse
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMMouse interface

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Controls the mouse device within a virtual machine (VM). The **IVMMouse** for a virtual machine can be retrieved using the [**IVMVirtualMachine::Mouse**](ivmvirtualmachine-mouse.md) property. Coordinates for the mouse device can be represented either in absolute coordinates or in delta coordinates. Use the [**UsingAbsoluteCoordinates**](ivmmouse-usingabsolutecoordinates.md) property to distinguish between the two methods of coordinate representation. Note that retrieving the current cursor position and the use of absolute coordinates are only supported if the guest operating system has the integration components installed.

## Members

The **IVMMouse** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IVMMouse** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMMouse** interface has these methods.



| Method                                  | Description                                                                        |
|:----------------------------------------|:-----------------------------------------------------------------------------------|
| [**Click**](ivmmouse-click.md)         | Simulates a mouse button click.<br/>                                         |
| [**GetButton**](ivmmouse-getbutton.md) | Retrieves the current state (up or down) of the specified mouse button.<br/> |
| [**SetButton**](ivmmouse-setbutton.md) | Sets the current state (up or down) of the specified mouse button.<br/>      |



 

### Properties

The **IVMMouse** interface has these properties.



| Property                                                                         | Access type           | Description                                                                                |
|:---------------------------------------------------------------------------------|:----------------------|:-------------------------------------------------------------------------------------------|
| [**HorizontalPosition**](ivmmouse-horizontalposition.md)<br/>             | Read/write<br/> | The absolute x-coordinate of the mouse.<br/>                                         |
| [**ScrollWheelPosition**](ivmmouse-scrollwheelposition.md)<br/>           | Write-only<br/> | The z-coordinate of the mouse (relative only).<br/>                                  |
| [**UsingAbsoluteCoordinates**](ivmmouse-usingabsolutecoordinates.md)<br/> | Read/write<br/> | Indicates whether mouse coordinates represent absolute or relative coordinates.<br/> |
| [**VerticalPosition**](ivmmouse-verticalposition.md)<br/>                 | Read/write<br/> | The absolute y-coordinate of the mouse.<br/>                                         |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMmouse is defined as ac903f6d-6346-4f29-8875-5d511a13895e<br/>                   |



 

