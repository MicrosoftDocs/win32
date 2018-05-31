---
title: Virtual Machine Architecture
description: The virtual machine sessions running in Microsoft Virtual Server are implemented as a set of COM objects which are accessible through the Virtual Server COM API.
ms.assetid: 142e6383-6356-4abe-b6a4-a79fcff43cd3
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Virtual Machine Architecture

The virtual machine sessions running in Microsoft Virtual Server are implemented as a set of COM objects which are accessible through the Virtual Server COM API. The virtual machine sessions are isolated from each other and can be viewed as totally separate hardware environments.

A new virtual machine session is initialized when an [**IVMVirtualMachine**](ivmvirtualmachine.md) object is created using [**VMVirtualServer::CreateVirtualMachine**](ivmvirtualserver-createvirtualmachine.md). The **IVMVirtualMachine** object contains a standardized set of emulated hardware, with the exception of any virtual hard disks or networks which must be created separately and then attached to the **IVMVirtualMachine** object. A virtual machine session is the equivalent of a physical hardware system and must be viewed as a separate computer in regards to issues concerning operating system and application software installation and licensing.

The operating state of a virtual machine session is controlled through the [**IVMVirtualMachine**](ivmvirtualmachine.md)'s [**Startup**](ivmvirtualmachine-startup.md), [**TurnOff**](ivmvirtualmachine-turnoff.md), [**Reset**](ivmvirtualmachine-reset.md), [**Save**](ivmvirtualmachine-save.md), [**Pause**](ivmvirtualmachine-pause.md), and [**Resume**](ivmvirtualmachine-resume.md) methods. Access to the virtual machine's emulated hardware is through the various property values of the **IVMVirtualMachine** object, which contain either attribute values of the virtual machine or pointers to other COM objects which implement the various emulated hardware devices such as serial ports, network cards, and so on.

There is no access to a virtual machine's operating system or application software unless the Virtual Machine Additions software module is installed in the virtual machine session. Installing Additions enables most of the methods and properties of the [**IVMGuestOS**](ivmguestos.md) object associated with the virtual machine session. **IVMGuestOS** allows Virtual Server to execute application programs inside the virtual machine session, perform an orderly [**Shutdown**](ivmguestos-shutdown.md) of the virtual machine's operating system, and to generate a steady "tick" or "heartbeat" event which allows Virtual Server to monitor the operating state of the virtual machine.

## Related topics

<dl> <dt>

[Virtual Machine Emulated Hardware](virtual-machine-emulated-hardware.md)
</dt> <dt>

[Virtual Machine State Diagram](virtual-machine-state-diagram.md)
</dt> </dl>

 

 




