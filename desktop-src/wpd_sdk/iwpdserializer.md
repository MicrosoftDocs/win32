---
description: The IWpdSerializer interface is used by the device driver to serialize IPortableDeviceValues interfaces to and from the raw data buffers used to communicate with the application.Applications do not need to use this interface, because the data is serialized and deserialized automatically when calling IPortableDevice::SendCommand.To get this interface, call CoCreateInstance and pass in IID\_IWpdSerializer.
ms.assetid: 837bd850-6e27-4f8e-a612-d16f61b92b1d
title: IWpdSerializer interface (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWpdSerializer
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IWpdSerializer interface

The **IWpdSerializer** interface is used by the device driver to serialize [**IPortableDeviceValues**](iportabledevicevalues.md) interfaces to and from the raw data buffers used to communicate with the application.

Applications do not need to use this interface, because the data is serialized and deserialized automatically when calling [**IPortableDevice::SendCommand**](/windows/desktop/api/PortableDeviceApi/nf-portabledeviceapi-iportabledevice-sendcommand).

To get this interface, call **CoCreateInstance** and pass in **IID\_IWpdSerializer**.

## Members

The **IWpdSerializer** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IWpdSerializer** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWpdSerializer** interface has these methods.



| Method                                                                                          | Description                                                                                                      |
|:------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------|
| [**GetBufferFromIPortableDeviceValues**](iwpdserializer-getbufferfromiportabledevicevalues.md) | Serializes a submitted **IPortableDeviceValues** interface to an allocated byte array.<br/>                |
| [**GetIPortableDeviceValuesFromBuffer**](iwpdserializer-getiportabledevicevaluesfrombuffer.md) | Deserializes a byte array to an **IPortableDeviceValues** interface.<br/>                                  |
| [**GetSerializedSize**](iwpdserializer-getserializedsize.md)                                   | Calculates the buffer size that is required to hold a serialized **IPortableDeviceValues** interface.<br/> |
| [**WriteIPortableDeviceValuesToBuffer**](iwpdserializer-writeiportabledevicevaluestobuffer.md) | Serializes an **IPortableDeviceValues** interface to a caller-allocated byte array.<br/>                   |



 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[**Driver Interfaces**](driver-interfaces.md)
</dt> </dl>

 

