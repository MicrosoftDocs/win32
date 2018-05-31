---
title: IVMDisplay interface
description: The IVMDisplay interface controls the display settings of a virtual machine. The IVMDisplay for a virtual machine can be retrieved using the IVMVirtualMachine Display property.
ms.assetid: 75557ea5-f3dd-424f-bf15-8b2545cdeb05
keywords:
- IVMDisplay interface Virtual Server
- IVMDisplay interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMDisplay
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IVMDisplay interface

The **IVMDisplay** interface controls the display settings of a virtual machine. The **IVMDisplay** for a virtual machine can be retrieved using the [**IVMVirtualMachine::Display**](ivmvirtualmachine-display.md) property.

## When to use

Use the **IVMDisplay** interface to access and manipulate the display settings of a virtual machine.

## Members

The **IVMDisplay** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMDisplay** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMDisplay** interface has these methods.



| Method                                                       | Description                                                                                             |
|:-------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------|
| [**\_GenerateThumbnail**](ivmdisplay--generatethumbnail.md) | Retrieves an array of pixels representing a thumbnail image of the virtual machine's screen.<br/> |
| [**SetDimensions**](ivmdisplay-setdimensions.md)            | Sets the height and width, in pixels, of the virtual machine's display.<br/>                      |



 

### Properties

The **IVMDisplay** interface has these properties.



| Property                                             | Access type          | Description                                                                                   |
|:-----------------------------------------------------|:---------------------|:----------------------------------------------------------------------------------------------|
| [**Height**](ivmdisplay-height.md)<br/>       | Read-only<br/> | The current height, in pixels, of the virtual machine's display.<br/>                   |
| [**Thumbnail**](ivmdisplay-thumbnail.md)<br/> | Read-only<br/> | An array of pixels representing a thumbnail image of the virtual machine's screen.<br/> |
| [**VideoMode**](ivmdisplay-videomode.md)<br/> | Read-only<br/> | The current video mode of the guest operating system (Text, VGA, SVGA, and so on).<br/> |
| [**Width**](ivmdisplay-width.md)<br/>         | Read-only<br/> | The current width, in pixels, of the virtual machine's display.<br/>                    |



 

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

 

 





