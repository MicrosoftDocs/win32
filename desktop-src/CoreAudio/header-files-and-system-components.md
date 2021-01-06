---
description: Header Files and System Components
ms.assetid: de2776be-72e6-4391-8e6c-56694d683d57
title: Header Files and System Components
ms.topic: article
ms.date: 05/31/2018
---

# Header Files and System Components

The following table lists the header files that contain the interface definitions for the four Core Audio components.



|                                              |                              |
|----------------------------------------------|------------------------------|
| Core Audio component                         | Header file                  |
| [MMDevice API](mmdevice-api.md)             | Mmdeviceapi.h                |
| [WASAPI](wasapi.md)                         | Audioclient.h, Audiopolicy.h |
| [DeviceTopology API](devicetopology-api.md) | Devicetopology.h             |
| [EndpointVolume API](endpointvolume-api.md) | Endpointvolume.h             |



 

Another header file, Audiosessiontypes.h, defines constants that are used by WASAPI. These header files are located in the directory %MSSdk%\\include, where %MSSdk% is the root directory of the Windows SDK installation on your computer.

Each API in the preceding table consists of a set of related COM interfaces. Because some aspects of audio streaming depend on low latency and precise synchronization, the implementations of the MMDevice, WASAPI, DeviceTopology, and EndpointVolume APIs do not use the Microsoft .NET Framework or managed-execution environment.

The Core Audio APIs are implemented in the user-mode system components Audioses.dll and Mmdevapi.dll. Client applications do not access the entry points in these DLLs directly. Instead, clients call the **CoCreateInstance** or **CoCreateInstanceEx** function to obtain the [**IMMDeviceEnumerator**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immdeviceenumerator) interface of the MMDeviceEnumerator class object. This object enumerates the [audio endpoint devices](audio-endpoint-devices.md) in the system. The **IMMDeviceEnumerator** interface is part of the MMDevice API. From this interface, clients can directly or indirectly obtain the other interfaces in the MMDevice API, including the [**IMMDevice**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immdevice) interface. **IMMDevice** represents a particular audio endpoint device. Through **IMMDevice**, clients can directly or indirectly obtain the device-specific interfaces in WASAPI, the DeviceTopology API, and the EndpointVolume API. For more information about **CoCreateInstance** and **CoCreateInstanceEx**, see the Windows SDK documentation. For more information about accessing the interfaces in the Core Audio APIs, see [Enumerating Audio Devices](enumerating-audio-devices.md).

## Related topics

<dl> <dt>

[About the Windows Core Audio APIs](about-the-windows-core-audio-apis.md)
</dt> </dl>

 

 



