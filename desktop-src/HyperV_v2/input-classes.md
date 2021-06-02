---
description: The user input devices are represented by these classes. A virtual machine always has one instance of each class associated with it.
ms.assetid: FFCA890D-6102-47BB-B499-4B9D77D75E9B
title: Input classes
ms.topic: reference
ms.date: 05/31/2018
---

# Input classes

The user input devices are represented by these classes. A virtual machine always has one instance of each class associated with it. These devices may not be added or removed from the virtual machine. Therefore, there are no resource pool instances for keyboard or mouse devices.

The keyboard and mouse devices are linked to the virtual machine through the [**Msvm\_SystemDevice**](msvm-systemdevice.md) association. A virtual machine contains both a PS2 and a synthetic mouse device. Only one pointing device is active at a time.

The following are virtualization WMI classes related to input.

## In this section



| Topic                                                          | Description                                     |
|----------------------------------------------------------------|-------------------------------------------------|
| [**Msvm\_Keyboard**](msvm-keyboard.md)<br/>             | Represents a keyboard device.<br/>        |
| [**Msvm\_Ps2Mouse**](msvm-ps2mouse.md)<br/>             | Represents a PS2 mouse device.<br/>       |
| [**Msvm\_SyntheticMouse**](msvm-syntheticmouse.md)<br/> | Represents a synthetic mouse device.<br/> |



 

 

 




