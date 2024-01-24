---
description: Supports the enumeration of IPortableDeviceConnector interfaces, representing MTP/Bluetooth devices that were paired with the PC.
ms.assetid: 99aa1e89-5e20-4f6e-82b5-acf63305eba0
title: IEnumPortableDeviceConnectors interface (Devpkey.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IEnumPortableDeviceConnectors
api_type: 
- COM
api_location: 
- PortableDeviceGuids.lib
- PortableDeviceGuids.dll
---

# IEnumPortableDeviceConnectors interface

The **IEnumPortableDeviceConnectors** interface supports the enumeration of [**IPortableDeviceConnector**](/windows/desktop/api/portabledeviceconnectapi/nn-portabledeviceconnectapi-iportabledeviceconnector) interfaces, representing MTP/Bluetooth devices that were paired with the PC. Note that this will retrieve all previously-paired devices, including devices that are paired but disconnected. To determine if a device is still connected, query the **DEVPKEY\_MTPBTH\_IsConnected** property for that device.

## Members

The **IEnumPortableDeviceConnectors** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IEnumPortableDeviceConnectors** also has these types of members:

-   [Methods](#methods)

### Methods

The **IEnumPortableDeviceConnectors** interface has these methods.



| Method                                               | Description                                                                                                                                 |
|:-----------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|
| [**Clone**](ienumportabledeviceconnectors-clone.md) | Creates a copy of the current **IEnumPortableDeviceConnectors** interface.<br/>                                                       |
| [**Next**](ienumportabledeviceconnectors-next.md)   | Retrieves the next one or more [**IPortableDeviceConnector**](/windows/desktop/api/portabledeviceconnectapi/nn-portabledeviceconnectapi-iportabledeviceconnector) objects in the enumeration sequence.<br/> |
| [**Reset**](ienumportabledeviceconnectors-reset.md) | Resets the enumeration sequence to the beginning.<br/>                                                                                |
| [**Skip**](ienumportabledeviceconnectors-skip.md)   | Skips the specified number of devices in the enumeration sequence.<br/>                                                               |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                                                                                             |
| Minimum supported server<br/> | None supported<br/>                                                                                                                                              |
| Header<br/>                   | <dl> <dt>Devpkey.h; </dt> <dt>Portabledeviceconnectapi.h</dt> </dl> |
| IDL<br/>                      | <dl> <dt>Portabledeviceconnectapi.idl</dt> </dl>                                                                |
| Library<br/>                  | <dl> <dt>PortableDeviceGuids.lib</dt> </dl>                                                                     |



 

