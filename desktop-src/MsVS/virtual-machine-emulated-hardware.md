---
title: Virtual Machine Emulated Hardware
description: Microsoft Virtual Server provides a standard set of emulated hardware devices for each virtual machine session.
ms.assetid: d8a6f597-6feb-431e-8a54-2cf3d5bb4ccb
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Virtual Machine Emulated Hardware

Microsoft Virtual Server provides a standard set of emulated hardware devices for each virtual machine session.

## Virtual System Processor Board

Microsoft Virtual Server emulates the following system processor board components.



| Type                   | Emulated component                                                              | COM interface                                             |
|------------------------|---------------------------------------------------------------------------------|-----------------------------------------------------------|
| Motherboard<br/> | Intel 440BX chipset<br/>                                                  | [**IVMVirtualMachine**](ivmvirtualmachine.md)<br/> |
| BIOS<br/>        | AMI BIOS<br/>                                                             | [**IVMVirtualMachine**](ivmvirtualmachine.md)<br/> |
| Processor<br/>   | The actual processor of the server used for Microsoft Virtual Server<br/> | [**IVMVirtualMachine**](ivmvirtualmachine.md)<br/> |
| Memory<br/>      | Up to 3.6 gigabytes per virtual machine session<br/>                      | [**IVMVirtualMachine**](ivmvirtualmachine.md)<br/> |



 

If Virtual Server is run on a multiprocessor hardware system, each hosted virtual machine session will only have a single CPU available to it in its emulated hardware environment. Virtual Server can distribute virtual machine sessions amongst multiple processors if available, but each session will only have a single emulated processor available to it.

The amount of memory available to any single virtual machine session depends on the actual physical memory of the hardware server running Virtual Server and the server's operating system.

## Virtual User Interface

Microsoft Virtual Server emulates the following user interface devices:



| Type                  | Emulated component                                                 | COM interface                                 |
|-----------------------|--------------------------------------------------------------------|-----------------------------------------------|
| Graphics<br/>   | S3 Trio 32/64 with 4 megabytes of video memory<br/>          | [**IVMDisplay**](ivmdisplay.md)<br/>   |
| Keyboard<br/>   | 104-key Windows compatible keyboard with PS/2 interface<br/> | [**IVMKeyboard**](ivmkeyboard.md)<br/> |
| Mouse<br/>      | Microsoft Intellimouse with PS/2 interface<br/>              | [**IVMMouse**](ivmmouse.md)<br/>       |
| Sound card<br/> | none<br/>                                                    | none<br/>                               |
| Joystick<br/>   | none<br/>                                                    | none<br/>                               |



 

The emulated graphics card is VESA 2.0 compliant and supports VGA and SVGA modes.

Virtual Server does not provide any support for sound cards or joystick interfaces. Both of these devices are available in Microsoft Virtual PC.

## Virtual I/O Devices

Microsoft Virtual Server emulates the following input/output devices.



| Type                      | Emulated component                | COM interface                                                                                                                   |
|---------------------------|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Serial ports<br/>   | Up to two serial ports<br/> | [**IVMSerialPort**](ivmserialport.md)<br/> [**IVMSerialPortCollection**](ivmserialportcollection.md)<br/>         |
| Parallel ports<br/> | One parallel port<br/>      | [**IVMParallelPort**](ivmparallelport.md)<br/> [**IVMParallelPortCollection**](ivmparallelportcollection.md)<br/> |
| USB devices<br/>    | none<br/>                   | none<br/>                                                                                                                 |



 

The emulated serial ports support mapping to the physical serial ports.

The emulated parallel port supports mapping to the physical parallel port.

Virtual Server does not provide any support for USB host controllers, USB hubs, or USB devices.

## Virtual Mass Storage Devices

Microsoft Virtual Server emulates the following mass storage devices.



| Type                                    | Emulated component                                                                                   | COM interface                                                                                                                                                                                                                                                                                                         |
|-----------------------------------------|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Floppy disk drives<br/>           | Up to two 1.44 MB floppy drives<br/>                                                           | [**IVMFloppyDrive**](ivmfloppydrive.md)<br/> [**IVMFloppyDriveCollection**](ivmfloppydrivecollection.md)<br/>                                                                                                                                                                                           |
| IDE devices<br/>                  | Up to four IDE interface devices, including hard disks, CD-ROM drives, and DVD-ROM drives<br/> | [**IVMHardDisk**](ivmharddisk.md)<br/> [**IVMHardDiskConnection**](ivmharddiskconnection.md)<br/> [**IVMHardDiskConnectionCollection**](ivmharddiskconnectioncollection.md)<br/> [**IVMDVDDrive**](ivmdvddrive.md)<br/> [**IVMDVDDriveCollection**](ivmdvddrivecollection.md)<br/> |
| SCSI host controller devices<br/> | Up to four SCSI host controllers. Adaptec 7870 SCSI controller chipset<br/>                    | [**IVMSCSIController**](ivmscsicontroller.md)<br/> [**IVMSCSIControllerCollection**](ivmscsicontrollercollection.md)<br/>                                                                                                                                                                               |
| SCSI drive devices<br/>           | Up to seven SCSI hard disks per SCSI host controller<br/>                                      | [**IVMHardDisk**](ivmharddisk.md)<br/> [**IVMHardDiskConnection**](ivmharddiskconnection.md)<br/> [**IVMHardDiskConnectionCollection**](ivmharddiskconnectioncollection.md)<br/>                                                                                                                 |



 

The emulated floppy disk devices support mapping to physical floppy drives or to virtual floppy drive images.

The emulated IDE hard disks support mapping to virtual hard disk images. Each disk image can store up to 128 gigabytes (GB), depending on the actual storage capacity of the hardware server running Virtual Server and the server's operating system.

The emulated IDE CD-ROM and DVD-ROM drives support mapping to physical CD/DVD drives or to virtual drive images. Each disk image can store up to 128 GB, depending on the actual storage capacity of the hardware server running Virtual Server and the server's operating system.

The emulated SCSI hard disks support mapping to virtual hard disk images. Each disk image can store up to 2 terabytes, depending on the actual storage capacity of the hardware server running Virtual Server and the server's operating system.

Virtual Server does not support SCSI CD-ROM or DVD-ROM drives.

## Virtual Network Devices

Microsoft Virtual Server emulates the following network interface devices:



| Type                                    | Emulated component                                                                                                | COM interface                                                                                                                                                                                                                                                                                                                                                 |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Network Interface Card (NIC)<br/> | One DEC 21140 10/100 MB multi-port Ethernet card. Supports up to four independent network connections.<br/> | [**IVMNetworkAdapter**](ivmnetworkadapter.md)<br/> [**IVMNetworkAdapterCollection**](ivmnetworkadaptercollection.md)<br/> [**IVMVirtualNetwork**](ivmvirtualnetwork.md)<br/> [**IVMVirtualNetworkCollection**](ivmvirtualnetworkcollection.md)<br/> [**IVMDHCPVirtualNetworkServer**](ivmdhcpvirtualnetworkserver.md)<br/> |



 

The emulated NICs support mapping to a physical NIC or to virtual network connection. An unlimited number of virtual network connections are supported. The emulated NIC supports all Ethernet-based networking protocols (IP, TCP/IP, IPX, NetBEUI, and so on), and can be dynamically connected to and disconnected from different virtual networks. Virtual networks are completely independent of each other, and virtual DHCP servers are available within each virtual network.

 

 





