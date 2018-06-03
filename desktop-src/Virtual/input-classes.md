---
title: Input Classes
description: The user input devices are represented by these classes. A virtual system always has one instance of each class associated with it.
ms.assetid: 36db8257-76a7-4082-987c-01c208c2e499
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Input Classes

The user input devices are represented by these classes. A virtual system always has one instance of each class associated with it. These devices may not be added or removed from the virtual system. Therefore, there are no resource pool instances for keyboard or mouse devices.

The keyboard and mouse devices are linked to the virtual system through the [**Msvm\_SystemDevice**](msvm-systemdevice.md) association. A virtual system contains both a PS2 and a synthetic mouse device. Only one pointing device is active at a time.

The following are virtualization WMI classes related to input.

## In this section



| Class                                                          | Description                                     |
|----------------------------------------------------------------|-------------------------------------------------|
| [**Msvm\_Keyboard**](msvm-keyboard.md)<br/>             | Represents a keyboard device.<br/>        |
| [**Msvm\_Ps2Mouse**](msvm-ps2mouse.md)<br/>             | Represents a PS2 mouse device.<br/>       |
| [**Msvm\_SyntheticMouse**](msvm-syntheticmouse.md)<br/> | Represents a synthetic mouse device.<br/> |



 

## Related topics

<dl> <dt>

[Virtualization WMI Classes](virtualization-wmi-classes.md)
</dt> </dl>

 

 





