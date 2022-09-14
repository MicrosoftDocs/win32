---
title: IVMDisplay interface (VPCCOMInterfaces.h)
description: Controls the display settings of a virtual machine. The IVMDisplay interface for a virtual machine can be retrieved using the IVMVirtualMachine Display property.
ms.assetid: b2eafd86-459c-4807-aa77-8b9125bce53e
keywords:
- IVMDisplay interface Virtual PC
- IVMDisplay interface Virtual PC , described
topic_type:
- apiref
api_name:
- IVMDisplay
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMDisplay interface

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Controls the display settings of a virtual machine. The **IVMDisplay** interface for a virtual machine can be retrieved using the [**IVMVirtualMachine::Display**](ivmvirtualmachine-display.md) property.

## Members

The **IVMDisplay** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IVMDisplay** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMDisplay** interface has these methods.



| Method                                                       | Description                                                                                             |
|:-------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------|
| [**\_GenerateThumbnail**](ivmdisplay--generatethumbnail.md) | Retrieves an array of pixels representing a thumbnail image of the virtual machine's screen.<br/> |
| [**SetDimensions**](ivmdisplay-setdimensions.md)            | Sets the height and width of the virtual machine's display, in pixels.<br/>                       |



 

### Properties

The **IVMDisplay** interface has these properties.



| Property                                             | Access type          | Description                                                                                   |
|:-----------------------------------------------------|:---------------------|:----------------------------------------------------------------------------------------------|
| [**CanResize**](ivmdisplay-canresize.md)<br/> | Read-only<br/> | Indicates whether the Guest allows resolution changes.<br/>                             |
| [**Height**](ivmdisplay-height.md)<br/>       | Read-only<br/> | The height of the virtual machine's display, in pixels.<br/>                            |
| [**Thumbnail**](ivmdisplay-thumbnail.md)<br/> | Read-only<br/> | An array of pixels representing a thumbnail image of the virtual machine's screen.<br/> |
| [**VideoMode**](ivmdisplay-videomode.md)<br/> | Read-only<br/> | The current video mode (Text, VGA, SVGA, and so on).<br/>                               |
| [**Width**](ivmdisplay-width.md)<br/>         | Read-only<br/> | The width of the virtual machine's display, in pixels.<br/>                             |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMDisplay is defined as 960895e9-f743-4498-96aa-261f867e7fc5<br/>                 |



 

