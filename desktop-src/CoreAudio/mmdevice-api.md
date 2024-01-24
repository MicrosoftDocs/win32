---
description: About MMDevice API
ms.assetid: 3a8fd734-0761-4b5b-ba04-677c7c040988
title: About MMDevice API
ms.topic: article
ms.date: 05/31/2018
---

# About MMDevice API

The Windows Multimedia Device (MMDevice) API enables audio clients to discover [audio endpoint devices](audio-endpoint-devices.md), determine their capabilities, and create driver instances for those devices.

Header file Mmdeviceapi.h defines the interfaces in the MMDevice API.

The MMDevice API consists of several interfaces. The first of these is the [**IMMDeviceEnumerator**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immdeviceenumerator) interface. To access the interfaces in the MMDevice API, a client obtains a reference to the **IMMDeviceEnumerator** interface of a device-enumerator object by calling the [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) function, as shown in the following code fragment:


```C++
  const CLSID CLSID_MMDeviceEnumerator = __uuidof(MMDeviceEnumerator);
  const IID IID_IMMDeviceEnumerator = __uuidof(IMMDeviceEnumerator);
  hr = CoCreateInstance(
         CLSID_MMDeviceEnumerator, NULL,
         CLSCTX_ALL, IID_IMMDeviceEnumerator,
         (void**)&pEnumerator);
```



In the preceding code fragment, CLSID\_MMDeviceEnumerator and IID\_IMMDeviceEnumerator are the GUID values that are attached as attributes to the **MMDeviceEnumerator** class object and to the [**IMMDeviceEnumerator**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immdeviceenumerator) interface. The [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) call passes these values by reference. Variable `hr` is of type **HRESULT**, and variable `pEnumerator` is a pointer to the **IMMDeviceEnumerator** interface of a device-enumerator object. **IMMDeviceEnumerator** provides methods for enumerating audio endpoint devices. For information about the **\_\_uuidof** operator, the **CoCreateInstance** function, and the CLSCTX\_*Xxx* constants, see the Windows SDK documentation.

Through the [**IMMDeviceEnumerator**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immdeviceenumerator) interface, the client can obtain references to the other interfaces in the MMDevice API. The MMDevice API implements the following interfaces.



| Interface                                          | Description                                     |
|----------------------------------------------------|-------------------------------------------------|
| [**IMMDevice**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immdevice)                     | Represents an audio device.                     |
| [**IMMDeviceCollection**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immdevicecollection) | Represents a collection of audio devices.       |
| [**IMMDeviceEnumerator**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immdeviceenumerator) | Provides methods for enumerating audio devices. |
| [**IMMEndpoint**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immendpoint)                 | Represents an audio endpoint device.            |



 

In addition, clients of the MMDevice API that require notification of status changes in audio endpoint devices should implement the following interface.



| Interface                                              | Description                                                                                                                                                                                    |
|--------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IMMNotificationClient**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immnotificationclient) | Provides notifications when an audio endpoint device is added or removed, when the state or properties of a device change, or when there is a change in the default role assigned to a device. |



 

## Related topics

<dl> <dt>

[Audio Endpoint Devices](audio-endpoint-devices.md)
</dt> <dt>

[**Programming Reference**](programming-reference.md)
</dt> </dl>

 

 
