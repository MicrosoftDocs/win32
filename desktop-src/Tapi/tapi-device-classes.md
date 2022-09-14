---
description: Learn about TAPI device classes. A device class is a group of devices or device drivers through which applications send and receive call information or data.
ms.assetid: 859979a8-0d16-4b7b-b183-d6e30f3e034d
title: TAPI Device Classes
ms.topic: article
ms.date: 05/31/2018
---

# TAPI Device Classes

A device class is a group of related physical devices or device drivers through which applications send and receive the information or data that makes up a call. Every device class has a *device class name* that uniquely identifies the class, and provides information about the programming interface and commands that can be used to open and communicate with the devices in the class.

The Telephony Application Programming Interface (TAPI) associates devices from one or more device classes to each line or phone device. You access one of these devices by retrieving the device identifier for the device using the [**lineGetID**](/windows/desktop/api/Tapi/nf-tapi-linegetid) or [**phoneGetID**](/windows/desktop/api/Tapi/nf-tapi-phonegetid) function. You supply the device class name, and the function returns the specific port name, device name, device handle, or device identifier that you need to open and access the device. The format of the information returned depends on the device class and is described in subsequent topics of this section.

You also use device class names with the [**lineConfigDialog**](/windows/desktop/api/Tapi/nf-tapi-lineconfigdialog) and [**phoneConfigDialog**](/windows/desktop/api/Tapi/nf-tapi-phoneconfigdialog) functions to enable the user to set configuration options for the given device, with the [**lineGetIcon**](/windows/desktop/api/Tapi/nf-tapi-linegeticon) and [**phoneGetIcon**](/windows/desktop/api/Tapi/nf-tapi-phonegeticon) functions to retrieve an icon to represent the given device, and with the [**lineGetDevConfig**](/windows/desktop/api/Tapi/nf-tapi-linegetdevconfig) and [**lineSetDevConfig**](/windows/desktop/api/Tapi/nf-tapi-linesetdevconfig) functions to directly retrieve and set configuration options for the given device.

The following list shows device class names.



| Device class name                                      | Description                                       |
|--------------------------------------------------------|---------------------------------------------------|
| [comm](comm.md)                                       | Communications port.                              |
| [comm/datamodem](comm-datamodem.md)                   | Modem through a communications port.              |
| [comm/datamodem/portname](comm-datamodem-portname.md) | Name of the device to which a modem is connected. |
| [wave/in](wave-in.md)                                 | Wave audio device (input only).                   |
| [wave/out](wave-out.md)                               | Wave audio device (output only).                  |
| [wave/in/out](wave-in-out.md)                         | Wave audio device, full duplex.                   |
| [midi/in](midi-in.md)                                 | MIDI sequencer (input only).                      |
| [midi/out](midi-out.md)                               | MIDI sequencer (output only).                     |
| [tapi/line](tapi-line.md)                             | Line device.                                      |
| [tapi/phone](tapi-phone.md)                           | Phone device.                                     |
| [ndis](ndis.md)                                       | Network device.                                   |
| [tapi/terminal](tapi-terminal.md)                     | Terminal device.                                  |



 

> [!Note]  
> These names are not case sensitive; you can use any combination of uppercase and lowercase letters.

 

Additional device classes and device class names may be available on a given system. In general, if a device does not belong to one of the default device classes, the manufacturer typically defines a new device class and assigns a unique device class name. Check the documentation for the device to determine what additional device classes are available for it. Note, however, that although the device class and media type are related, they are not the same. A media type describes call information format, and a device class defines the programming interface used to manage that information. So, even if a manufacturer defines a new media type, it is not necessarily true that the manufacturer also needs to define a new device class to support the mode.

The format of the configuration data used with the [**lineSetDevConfig**](/windows/desktop/api/Tapi/nf-tapi-linesetdevconfig) and [**lineGetDevConfig**](/windows/desktop/api/Tapi/nf-tapi-linegetdevconfig) functions also depends on the device class. In general, you use **lineGetDevConfig** to save a copy of the current device configuration data and then later use **lineSetDevConfig** with the saved configuration data to restore the device configuration to the previous state. This is a convenient way to temporarily change the configuration without requiring the user to manually restore it to the previous state. Because the exact format of the device configuration data may be different with each service provider, you should not use **lineSetDevConfig** and **lineGetDevConfig** to manipulate the device configuration data directly. Some formats are provided only for information.

 

 



