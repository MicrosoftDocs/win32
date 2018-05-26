---
title: Serial Devices Classes
description: The serial devices in a virtual machine consist of serial controllers and serial ports. Each virtual system has exactly one serial controller, and each serial controller has exactly two serial ports.
ms.assetid: 02282099-a930-4e10-9df6-bb5b58634344
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Serial Devices Classes

The serial devices in a virtual machine consist of serial controllers and serial ports. Each virtual system has exactly one serial controller, and each serial controller has exactly two serial ports.

The settings for the serial controller are not configurable; therefore, there is no setting data instance associated with it. Also, you cannot add or remove serial controllers or serial ports from a virtual system. Therefore, there are no resource pool instances for serial devices.

The following are virtualization WMI classes related to serial devices.

## In this section



| Class                                                                                      | Description                                                                     |
|--------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| [**Msvm\_SerialController**](msvm-serialcontroller.md)<br/>                         | Represents the capabilities and management of the serial controller.<br/> |
| [**Msvm\_SerialPort**](msvm-serialport.md)<br/>                                     | Represents a serial port associated with the serial controller.<br/>      |
| [**Msvm\_SerialPortOnSerialController**](msvm-serialportonserialcontroller.md)<br/> | Associates a serial port with a serial controller.<br/>                   |



 

## Related topics

<dl> <dt>

[Virtualization WMI Classes](virtualization-wmi-classes.md)
</dt> </dl>

 

 





