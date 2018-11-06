---
Description: A device class is a group of related physical devices or device drivers through which applications send and receive the information or data that makes up a call.
ms.assetid: b29ea789-d017-4e35-b77a-c0d54ac54c66
title: TSPI Device Classes
ms.topic: article
ms.date: 05/31/2018
---

# TSPI Device Classes

A *device class* is a group of related physical devices or device drivers through which applications send and receive the information or data that makes up a call. Every device class has a *device class name* that uniquely identifies the class and provides information about the programming interface and commands that can be used to open and communicate with the devices in the class.

The Telephony Application Programming Interface (TAPI) associates devices from one or more device classes to each line or phone device. You access one of these devices by retrieving the device identifier for the device using the [**lineGetID**](https://msdn.microsoft.com/en-us/library/ms735751(v=VS.85).aspx) or [**phoneGetID**](https://msdn.microsoft.com/en-us/library/ms736640(v=VS.85).aspx) function. You supply the device class name, and the function returns the specific port name, device name, device handle, or device identifier that you need to open and access the device. The format of the returned information depends on the device class and is described in this section.

You also use device class names with the [**lineConfigDialog**](https://msdn.microsoft.com/en-us/library/ms735582(v=VS.85).aspx) and [**phoneConfigDialog**](https://msdn.microsoft.com/en-us/library/ms736606(v=VS.85).aspx) functions to enable the user to set configuration options for the given device; with the [**lineGetIcon**](https://msdn.microsoft.com/en-us/library/ms735746(v=VS.85).aspx) and [**phoneGetIcon**](https://msdn.microsoft.com/en-us/library/ms736636(v=VS.85).aspx) functions to retrieve an icon to represent the given device; and with the [**lineGetDevConfig**](https://msdn.microsoft.com/en-us/library/ms735739(v=VS.85).aspx) and [**lineSetDevConfig**](https://msdn.microsoft.com/en-us/library/ms736096(v=VS.85).aspx) functions to directly retrieve and set configuration options for the given device.

Following are the default device class names.



| Device class name                                       | Description                                      |
|---------------------------------------------------------|--------------------------------------------------|
| [comm](https://msdn.microsoft.com/library/ms725177)                                       | Communications port                              |
| [comm/datamodem](https://msdn.microsoft.com/library/ms725178)                   | Modem through a communications port              |
| [comm/datamodem/portname](https://msdn.microsoft.com/library/ms725179) | Name of the device to which a modem is connected |
| [wave/in](https://msdn.microsoft.com/library/ms725990)                                 | Wave audio device (input only)                   |
| [wave/out](https://msdn.microsoft.com/library/ms725992)                               | Wave audio device (output only)                  |
| [wave/in/out](https://msdn.microsoft.com/library/ms725991)                         | Wave audio device, full duplex                   |
| [midi/in](https://msdn.microsoft.com/library/ms725244)                                 | MIDI sequencer (input only)                      |
| [midi/out](https://msdn.microsoft.com/library/ms725245)                               | MIDI sequencer (output only)                     |
| [tapi/line](https://msdn.microsoft.com/library/ms725511)                             | Line device                                      |
| [tapi/phone](https://msdn.microsoft.com/library/ms725512)                           | Phone device                                     |
| [ndis](https://msdn.microsoft.com/library/ms725247)                                       | Network device                                   |
| [tapi/terminal](https://msdn.microsoft.com/library/ms725515)                     | Terminal device                                  |



 

These names are not case sensitive, so you can use any combination of uppercase and lowercase letters.

Additional device classes and device class names may be available on a given system. In general, if a device does not belong to one of the default device classes, the manufacturer typically defines a new device class and assigns a unique device class name. You must check the documentation for the device to determine what additional device classes are available for it. Note, however, that although the device class and media type are related, they are not the same. A *media type* describes a format of information on a call, and a *device class* defines the programming interface used to manage that information. So, even if a manufacturer defines a new media type, it may not be true that the manufacturer must also define a new device class to support the mode.

The format of the configuration data used with the [**lineSetDevConfig**](https://msdn.microsoft.com/en-us/library/ms736096(v=VS.85).aspx) and [**lineGetDevConfig**](https://msdn.microsoft.com/en-us/library/ms735739(v=VS.85).aspx) functions also depends on the device class. In general, you use **lineGetDevConfig** to save a copy of the current device configuration data and then later use **lineSetDevConfig** with the saved configuration data to restore the device configuration to the previous state. This is a convenient way to temporarily change the configuration without requiring the user to manually restore it to the previous state. Because the exact format of the device configuration data may be different with each service provider, do not use **lineSetDevConfig** and **lineGetDevConfig** to manipulate the device configuration data directly. Some formats are provided for information only.

 

 



