---
description: The serial devices in a virtual machine consist of serial controllers and serial ports. Each virtual machine has exactly one serial controller, and each serial controller has exactly two serial ports.
ms.assetid: BA24BD74-D80C-4C5C-891F-5F17CDED2EC6
title: Serial devices classes
ms.topic: reference
ms.date: 05/31/2018
---

# Serial devices classes

The serial devices in a virtual machine consist of serial controllers and serial ports. Each virtual machine has exactly one serial controller, and each serial controller has exactly two serial ports.

The settings for the serial controller are not configurable; therefore, there is no setting data instance associated with it. Also, you cannot add or remove serial controllers or serial ports from a virtual machine. Therefore, there are no resource pool instances for serial devices.

The following are virtualization WMI classes related to serial devices.

## In this section



| Topic                                                                                      | Description                                                                     |
|--------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| [**Msvm\_SerialController**](msvm-serialcontroller.md)<br/>                         | Represents the capabilities and management of the serial controller.<br/> |
| [**Msvm\_SerialPort**](msvm-serialport.md)<br/>                                     | Represents a serial port associated with the serial controller.<br/>      |
| [**Msvm\_SerialPortOnSerialController**](msvm-serialportonserialcontroller.md)<br/> | Associates a serial port with a serial controller.<br/>                   |



 

 

 




