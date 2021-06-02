---
description: The Computer System Hardware category groups classes together that represent hardware related objects. Examples include input devices, hard disks, expansion cards, video devices, networking devices, and system power.
ms.assetid: 0b6cb410-166e-45cd-8dca-77a111b3cf62
ms.tgt_platform: multiple
title: Computer System Hardware Classes
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Computer System Hardware Classes

The Computer System Hardware category groups classes together that represent hardware related objects. Examples include input devices, hard disks, expansion cards, video devices, networking devices, and system power.

-   [Cooling Device Classes](#cooling-device-classes)
-   [Input Device Classes](#input-device-classes)
-   [Mass Storage Classes](#mass-storage-classes)
-   [Motherboard, Controller, and Port Classes](#motherboard-controller-and-port-classes)
-   [Networking Device Classes](#networking-device-classes)
-   [Power Classes](#power-classes)
-   [Printing Classes](#printing-classes)
-   [Telephony Classes](#telephony-classes)
-   [Video and Monitor Classes](#video-and-monitor-classes)
-   [Related topics](#related-topics)

## Cooling Device Classes

The Cooling Devices subcategory groups classes that represent instrumentable fans, temperature probes, and refrigeration devices.



| Class                                                     | Description                                                                 |
|-----------------------------------------------------------|-----------------------------------------------------------------------------|
| [**Win32\_Fan**](win32-fan.md)                           | Represents the properties of a fan device in the computer system.           |
| [**Win32\_HeatPipe**](win32-heatpipe.md)                 | Represents the properties of a heat pipe cooling device.                    |
| [**Win32\_Refrigeration**](win32-refrigeration.md)       | Represents the properties of a refrigeration device.                        |
| [**Win32\_TemperatureProbe**](win32-temperatureprobe.md) | Represents the properties of a temperature sensor (electronic thermometer). |



 

## Input Device Classes

The Input Devices subcategory groups classes that represent keyboards and pointing devices.



| Class                                                 | Description                                                                                                         |
|-------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [**Win32\_Keyboard**](win32-keyboard.md)             | Represents a keyboard installed on a computer system running Windows.                                               |
| [**Win32\_PointingDevice**](win32-pointingdevice.md) | Represents an input device used to point to and select regions on the display of a computer system running Windows. |



 

## Mass Storage Classes

Classes in the Mass Storage subcategory represent storage devices such as hard disk drives, CD-ROM drives, and tape drives.



| Class                                                     | Description                                                                                  |
|-----------------------------------------------------------|----------------------------------------------------------------------------------------------|
| [**Win32\_AutochkSetting**](win32-autochksetting.md)     | Represents the settings for the autocheck operation of a disk.                               |
| [**Win32\_CDROMDrive**](win32-cdromdrive.md)             | Represents a CD-ROM drive on a computer system running Windows.                              |
| [**Win32\_DiskDrive**](win32-diskdrive.md)               | Represents a physical disk drive as seen by a computer running the Windows operating system. |
| [**Win32\_FloppyDrive**](win32-floppydrive.md)           | Manages the capabilities of a floppy disk drive.                                             |
| [**Win32\_PhysicalMedia**](/previous-versions/windows/desktop/cimwin32a/win32-physicalmedia) | Represents any type of documentation or storage medium.                                      |
| [**Win32\_TapeDrive**](win32-tapedrive.md)               | Represents a tape drive on a computer system running Windows.                                |



 

## Motherboard, Controller, and Port Classes

The Motherboard, Controllers, and Ports subcategory groups classes that represent system devices. Examples include system memory, cache memory, and controllers.



| Class                                                                       | Description                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Win32\_1394Controller**](win32-1394controller.md)                       | Represents the capabilities and management of a 1394 controller.<br/>                                                                                                                                               |
| [**Win32\_1394ControllerDevice**](win32-1394controllerdevice.md)           | Relates the high-speed serial bus (IEEE 1394 Firewire) Controller and the [**CIM\_LogicalDevice**](cim-logicaldevice.md) instance connected to it.<br/>                                                            |
| [**Win32\_AllocatedResource**](win32-allocatedresource.md)                 | Relates a logical device to a system resource.<br/>                                                                                                                                                                 |
| [**Win32\_AssociatedProcessorMemory**](win32-associatedprocessormemory.md) | Relates a processor and its cache memory.<br/>                                                                                                                                                                      |
| [**Win32\_BaseBoard**](win32-baseboard.md)                                 | Represents a baseboard (also known as a motherboard or system board).<br/>                                                                                                                                          |
| [**Win32\_BIOS**](win32-bios.md)                                           | Represents the attributes of the computer system's basic input or output services (BIOS) that are installed on the computer.<br/>                                                                                   |
| [**Win32\_Bus**](win32-bus.md)                                             | Represents a physical bus as seen by a Windows operating system.<br/>                                                                                                                                               |
| [**Win32\_CacheMemory**](win32-cachememory.md)                             | Represents cache memory (internal and external) on a computer system.<br/>                                                                                                                                          |
| [**Win32\_ControllerHasHub**](/previous-versions/windows/desktop/cimwin32a/win32-controllerhashub)             | Represents the hubs downstream from the universal serial bus (USB) controller.<br/>                                                                                                                                 |
| [**Win32\_DeviceBus**](win32-devicebus.md)                                 | Relates a system bus and a logical device using the bus.<br/>                                                                                                                                                       |
| [**Win32\_DeviceMemoryAddress**](win32-devicememoryaddress.md)             | Represents a device memory address on a Windows system.<br/>                                                                                                                                                        |
| [**Win32\_DeviceSettings**](win32-devicesettings.md)                       | Relates a logical device and a setting that can be applied to it.<br/>                                                                                                                                              |
| [**Win32\_DMAChannel**](win32-dmachannel.md)                               | Represents a direct memory access (DMA) channel on a computer system running Windows.<br/>                                                                                                                          |
| [**Win32\_FloppyController**](win32-floppycontroller.md)                   | Represents the capabilities and management capacity of a floppy disk drive controller.<br/>                                                                                                                         |
| [**Win32\_IDEController**](win32-idecontroller.md)                         | Represents the capabilities of an Integrated Drive Electronics (IDE) controller device.<br/>                                                                                                                        |
| [**Win32\_IDEControllerDevice**](win32-idecontrollerdevice.md)             | Association class that relates an IDE controller and the logical device.<br/>                                                                                                                                       |
| [**Win32\_InfraredDevice**](win32-infrareddevice.md)                       | Represents the capabilities and management of an infrared device.<br/>                                                                                                                                              |
| [**Win32\_IRQResource**](win32-irqresource.md)                             | Represents an interrupt request line (IRQ) number on a Windows computer system.<br/>                                                                                                                                |
| [**Win32\_MemoryArray**](win32-memoryarray.md)                             | Represents the properties of the computer system memory array and mapped addresses.<br/>                                                                                                                            |
| [**Win32\_MemoryArrayLocation**](win32-memoryarraylocation.md)             | Relates a logical memory array and the physical memory array upon which it exists.<br/>                                                                                                                             |
| [**Win32\_MemoryDevice**](win32-memorydevice.md)                           | Represents the properties of a computer system's memory device along with its associated mapped addresses.<br/>                                                                                                     |
| [**Win32\_MemoryDeviceArray**](win32-memorydevicearray.md)                 | Relates a memory device and the memory array in which it resides.<br/>                                                                                                                                              |
| [**Win32\_MemoryDeviceLocation**](win32-memorydevicelocation.md)           | Association class that relates a memory device and the physical memory on which it exists.<br/>                                                                                                                     |
| [**Win32\_MotherboardDevice**](win32-motherboarddevice.md)                 | Represents a device that contains the central components of the computer system running Windows.<br/>                                                                                                               |
| [**Win32\_OnBoardDevice**](win32-onboarddevice.md)                         | Represents common adapter devices built into the motherboard (system board).<br/>                                                                                                                                   |
| [**Win32\_ParallelPort**](win32-parallelport.md)                           | Represents the properties of a parallel port on a computer system running Windows.<br/>                                                                                                                             |
| [**Win32\_PCMCIAController**](win32-pcmciacontroller.md)                   | Manages the capabilities of a Personal Computer Memory Card Interface Adapter (PCMCIA) controller device.<br/>                                                                                                      |
| [**Win32\_PhysicalMemory**](win32-physicalmemory.md)                       | Represents a physical memory device located on a computer as available to the operating system.<br/>                                                                                                                |
| [**Win32\_PhysicalMemoryArray**](win32-physicalmemoryarray.md)             | Represents details about the computer system's physical memory.<br/>                                                                                                                                                |
| [**Win32\_PhysicalMemoryLocation**](win32-physicalmemorylocation.md)       | Relates an array of physical memory and its physical memory.<br/>                                                                                                                                                   |
| [**Win32\_PNPAllocatedResource**](win32-pnpallocatedresource.md)           | Represents an association between logical devices and system resources.<br/>                                                                                                                                        |
| [**Win32\_PNPDevice**](win32-pnpdevice.md)                                 | Relates a device (known to Configuration Manager as a PNPEntity), and the function it performs.<br/>                                                                                                                |
| [**Win32\_PNPEntity**](win32-pnpentity.md)                                 | Represents the properties of a Plug and Play device.<br/>                                                                                                                                                           |
| [**Win32\_PortConnector**](win32-portconnector.md)                         | Represents physical connection ports, such as DB-25 pin male, Centronics, and PS/2.<br/>                                                                                                                            |
| [**Win32\_PortResource**](win32-portresource.md)                           | Represents an I/O port on a computer system running Windows.<br/>                                                                                                                                                   |
| [**Win32\_Processor**](win32-processor.md)                                 | Represents a device capable of interpreting a sequence of machine instructions on a computer system running Windows.<br/>                                                                                           |
| [**Win32\_SCSIController**](win32-scsicontroller.md)                       | Represents a small computer system interface (SCSI) controller on a computer system running Windows.<br/>                                                                                                           |
| [**Win32\_SCSIControllerDevice**](win32-scsicontrollerdevice.md)           | Relates a SCSI controller and the logical device (disk drive) connected to it.<br/>                                                                                                                                 |
| [**Win32\_SerialPort**](win32-serialport.md)                               | Represents a serial port on a computer system running Windows.<br/>                                                                                                                                                 |
| [**Win32\_SerialPortConfiguration**](win32-serialportconfiguration.md)     | Represents the settings for data transmission on a Windows serial port.<br/>                                                                                                                                        |
| [**Win32\_SerialPortSetting**](win32-serialportsetting.md)                 | Relates a serial port and its configuration settings.<br/>                                                                                                                                                          |
| [**Win32\_SMBIOSMemory**](win32-smbiosmemory.md)                           | Represents the capabilities and management of memory-related logical devices.<br/>                                                                                                                                  |
| [**Win32\_SoundDevice**](win32-sounddevice.md)                             | Represents the properties of a sound device on a computer system running Windows.<br/>                                                                                                                              |
| [**Win32\_SystemBIOS**](win32-systembios.md)                               | Relates a computer system (including data such as startup properties, time zones, boot configurations, or administrative passwords) and a system BIOS (services, languages, and system management properties).<br/> |
| [**Win32\_SystemDriverPNPEntity**](win32-systemdriverpnpentity.md)         | Relates a Plug and Play device on the Windows computer system and the driver that supports the Plug and Play device.<br/>                                                                                           |
| [**Win32\_SystemEnclosure**](win32-systemenclosure.md)                     | Represents the properties associated with a physical system enclosure.<br/>                                                                                                                                         |
| [**Win32\_SystemMemoryResource**](win32-systemmemoryresource.md)           | Represents a system memory resource on a Windows system.<br/>                                                                                                                                                       |
| [**Win32\_SystemSlot**](win32-systemslot.md)                               | Represents physical connection points including ports, motherboard slots and peripherals, and proprietary connections points.<br/>                                                                                  |
| [**Win32\_USBController**](win32-usbcontroller.md)                         | Manages the capabilities of a universal serial bus (USB) controller.<br/>                                                                                                                                           |
| [**Win32\_USBControllerDevice**](win32-usbcontrollerdevice.md)             | Relates a USB controller and the [**CIM\_LogicalDevice**](cim-logicaldevice.md) instances connected to it.<br/>                                                                                                    |
| [**Win32\_USBHub**](/previous-versions/windows/desktop/cimwin32a/win32-usbhub)                                 | Represents the management characteristics of a USB hub.<br/>                                                                                                                                                        |



 

## Networking Device Classes

The Networking Devices subcategory groups classes that represent the network interface controller, its configurations, and its settings.



| Class                                                                           | Description                                                                                                                                                                                                            |
|---------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Win32\_NetworkAdapter**](win32-networkadapter.md)                           | Represents a network adapter on a computer system running Windows.<br/>                                                                                                                                          |
| [**Win32\_NetworkAdapterConfiguration**](win32-networkadapterconfiguration.md) | Represents the attributes and behaviors of a network adapter. The class is not guaranteed to be supported after the ratification of the Distributed Management Task Force (DMTF) CIM network specification.<br/> |
| [**Win32\_NetworkAdapterSetting**](win32-networkadaptersetting.md)             | Relates a network adapter and its configuration settings.<br/>                                                                                                                                                   |



 

## Power Classes

The Power subcategory groups classes that represent power supplies, batteries, and events related to these devices.



| Class                                                             | Description                                                                                           |
|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| [**Win32\_Battery**](win32-battery.md)                           | Represents a battery connected to the computer system.<br/>                                     |
| [**Win32\_CurrentProbe**](win32-currentprobe.md)                 | Represents the properties of a current monitoring sensor (ammeter).<br/>                        |
| [**Win32\_PortableBattery**](win32-portablebattery.md)           | Represents the properties of a portable battery, such as one used for a notebook computer.<br/> |
| [**Win32\_PowerManagementEvent**](win32-powermanagementevent.md) | Represents power management events resulting from power state changes.<br/>                     |
| [**Win32\_VoltageProbe**](win32-voltageprobe.md)                 | Represents the properties of a voltage sensor (electronic voltmeter).<br/>                      |



 

## Printing Classes

The Printing subcategory groups classes that represent printers, printer configurations, and print jobs.



| Class                                                             | Description                                                                                                                              |
|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| [**Win32\_DriverForDevice**](win32-driverfordevice.md)           | Relates a printer to a printer driver.<br/>                                                                                        |
| [**Win32\_Printer**](win32-printer.md)                           | Represents a device connected to a computer system running Windows that is capable of reproducing a visual image on a medium.<br/> |
| [**Win32\_PrinterConfiguration**](win32-printerconfiguration.md) | Defines the configuration for a printer device.<br/>                                                                               |
| [**Win32\_PrinterController**](win32-printercontroller.md)       | Relates a printer and the local device to which the printer is connected.<br/>                                                     |
| [**Win32\_PrinterDriver**](win32-printerdriver.md)               | Represents the drivers for a [**Win32\_Printer**](win32-printer.md) instance.<br/>                                                |
| [**Win32\_PrinterDriverDll**](win32-printerdriverdll.md)         | Relates a local printer and its driver file (not the driver itself).<br/>                                                          |
| [**Win32\_PrinterSetting**](win32-printersetting.md)             | Relates a printer and its configuration settings.<br/>                                                                             |
| [**Win32\_PrintJob**](win32-printjob.md)                         | Represents a print job generated by a Windows-based application.<br/>                                                              |
| [**Win32\_TCPIPPrinterPort**](win32-tcpipprinterport.md)         | Represents a TCP/IP service access point.<br/>                                                                                     |



 

## Telephony Classes

The Telephony subcategory groups classes that represent "plain old telephone" modem devices and their associated serial connections.



| Class                                                               | Description                                                                                                                                |
|---------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| [**Win32\_POTSModem**](win32-potsmodem.md)                         | Represents the services and characteristics of a Plain Old Telephone Service (POTS) modem on a computer system running Windows.<br/> |
| [**Win32\_POTSModemToSerialPort**](win32-potsmodemtoserialport.md) | Relates a modem and the serial port the modem uses.<br/>                                                                             |



 

## Video and Monitor Classes

The Video and Monitors subcategory groups classes that represent monitors, video cards, and their associated settings.



| Class                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                        |
|---------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Win32\_DesktopMonitor**](win32-desktopmonitor.md)                                 | Represents the type of monitor or display device attached to the computer system.<br/>                                                                                                                                                                                                                                                                                       |
| [**Win32\_DisplayControllerConfiguration**](win32-displaycontrollerconfiguration.md) | Represents the video adapter configuration information of a computer system running Windows. This class is obsolete. In place of this class, use the properties in the [**Win32\_VideoController**](win32-videocontroller.md), [**Win32\_DesktopMonitor**](win32-desktopmonitor.md), and [CIM\_VideoControllerResolution](cim-videocontrollerresolution.md) classes.<br/> |
| [**Win32\_VideoController**](win32-videocontroller.md)                               | Represents the capabilities and management capacity of the video controller on a computer system running Windows.<br/>                                                                                                                                                                                                                                                       |
| [**Win32\_VideoSettings**](win32-videosettings.md)                                   | Relates a video controller and video settings that can be applied to it.<br/>                                                                                                                                                                                                                                                                                                |



 

## Related topics

<dl> <dt>

[Win32 Classes](/previous-versions//aa394084(v=vs.85))
</dt> </dl>

 

