---
description: Audio Endpoint Devices
ms.assetid: 773714fb-3b00-4f03-988f-05c5835f87cf
title: Audio Endpoint Devices
ms.topic: article
ms.date: 05/31/2018
---

# Audio Endpoint Devices

The term *endpoint device* refers to a hardware device that lies at one end of a data path that originates or terminates at an application program. Examples of audio endpoint devices are speakers, headphones, microphones, and CD players. The audio data that moves along the data path might traverse a number of software and hardware components during its journey between the application and endpoint device. Although these components are essential to the operation of the endpoint device, they tend to be invisible to users. Users are more likely to think in terms of endpoint devices that they directly manipulate rather than in terms of the devices on audio adapters that the endpoint devices plug into or in terms of the software components that process the audio streams that flow to and from these adapters.

To avoid confusion with endpoint devices, this documentation refers to a device on an audio adapter as an *adapter device*.

The following diagram shows how audio endpoint devices differ from adapter devices.

![examples of audio endpoint devices and adapter devices](images/devices.jpg)

In the preceding diagram, the following are examples of endpoint devices:

-   Speakers
-   Microphone
-   Auxiliary input device

The following are examples of adapter devices:

-   Wave output device (contains digital-to-analog converter)
-   Output controls device (contains volume and mute controls)
-   Wave input device (contains analog-to-digital converter)
-   Input controls device (contains volume control and multiplexer)

Typically, the user interfaces of audio applications refer to audio endpoint devices, not to adapter devices. Windows Vista simplifies the design of user-friendly applications by directly supporting the endpoint device abstraction.

Some endpoint devices might permanently connect to an adapter device. For example, a computer might contain internal devices such as a CD player, a microphone, or speakers that are integrated into the system chassis. Typically, the user does not physically remove these endpoint devices.

Other endpoint devices might connect to an audio adapter through audio jacks. The user plugs in and unplugs these external devices. For example, an audio endpoint device such as an external microphone or headphones lies at one end of a cable whose other end plugs into a jack on an adapter device.

The adapter communicates with the system processor through a system bus (typically, PCI or PCI Express) or external bus (USB or IEEE 1394) that supports Plug and Play (PnP). During device enumeration, the Plug and Play manager identifies the devices in the audio adapter and registers those devices to make them available for use by the operating system and by applications.

Unlike the connection between an adapter and an external bus such as USB or the IEEE 1394 bus, the connection between an endpoint device and an adapter device does not support PnP device detection. However, some audio adapters support *jack-presence detection*: when a plug is inserted into or removed from a jack, the hardware generates an interrupt to notify the adapter driver of the change in the hardware configuration. The endpoint manager in Windows Vista can exploit this hardware capability to notify applications which endpoint devices are present at any time. In this way, the operation of the endpoint manager is analogous to that of the Plug and Play manager, which keeps track of the adapter devices that are present in the system.

In Windows Vista, the audio system keeps track of both endpoint devices and adapter devices. The endpoint manager registers endpoint devices and the Plug and Play manager registers adapter devices. Registering endpoint devices makes it easier for user-friendly applications to enable users to refer to the endpoint devices that users directly manipulate instead of referring to adapter devices that might be hidden inside the computer chassis. The endpoint devices that are reported by the operating system faithfully track dynamic changes in the configuration of audio hardware that has jack-presence detection. While an endpoint device remains plugged in, the system enumerates that device. When the user unplugs an endpoint device, the system ceases to enumerate it.

In earlier versions of Windows, including Windows 98, Windows Me, Windows 2000, and Windows XP, the system explicitly presents only PnP devices to applications. Thus, applications must infer the existence of endpoint devices. An operating system that lacks explicit support for endpoint devices forces client applications to do more of the work themselves. For example, an audio capture application must perform the following steps to enable capturing from an external microphone:

1.  Enumerate all the audio capture devices (these are adapter devices) that were previously registered by the PnP manager.
2.  After selecting a capture device, open a capture stream on the device by either calling the **waveInOpen** function or by using the **DirectSoundCapture** or DirectShow API.
3.  Call the mixerOpen function and use the other **mixerXxx** functions to look for a MIXERLINE\_COMPONENTTYPE\_SRC\_MICROPHONE line that corresponds to the capture device opened in step 2. This is an educated guess.
4.  Unblock the data path from the microphone. If the data path includes a mute node, then the client must disable muting of the signal from the microphone. If the capture device contains a multiplexer for selecting from among several inputs, then the client must select the microphone input.

This process is error-prone because the software that performs these operations might fail if it encounters a hardware configuration that its designers did not anticipate or for which it was not tested.

In Windows Vista, which supports endpoint devices, the process of connecting to the same endpoint device is much simpler:

1.  Select a microphone from a collection of endpoint devices.
2.  Activate an audio-capture interface on that microphone.

The operating system does all the work necessary to identify and enable the endpoint device. For example, if the data path from the microphone includes a multiplexer, the system automatically selects the microphone input to the multiplexer.

The behavior of the audio subsystem is more reliable and deterministic if applications, instead of implementing their own endpoint-identification algorithms, can relegate the task of identifying endpoint devices to the operating system. Software vendors no longer need to verify that their endpoint-identification algorithms work correctly with all available audio hardware devices and configurations—they can simply rely on the operating system for endpoint identification. Similarly, hardware vendors no longer need to verify that every relevant client application can readily identify any endpoint device that is connected to their audio adapter—they need only to verify that the operating system can identify an endpoint device that is connected to their audio adapter.

The following topics provide additional information about audio endpoint devices:

-   [About MMDevice API](mmdevice-api.md)
-   [Enumerating Audio Devices](enumerating-audio-devices.md)
-   [Endpoint ID Strings](endpoint-id-strings.md)
-   [Device Properties](device-properties.md)
-   [Device Events](device-events.md)
-   [Device Roles](device-roles.md)
-   [Device Formats](device-formats.md)

## Related topics

<dl> <dt>

[Programming Guide](programming-guide.md)
</dt> </dl>

 

 



