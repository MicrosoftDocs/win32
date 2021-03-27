---
description: Windows Portable Devices supports the following SMS properties.
ms.assetid: d821f378-522f-4f0a-825b-6b15295e7b12
title: SMS Properties (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SMS
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# SMS Properties

Windows Portable Devices supports the following SMS properties.



| Property                   | VarType        | Description                                                                                                                                                                                                                                                                                                 |
|----------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **WPD\_SMS\_ENCODING**     | **VT\_LPWSTR** | A value that specifies how the driver will encode the text message sent by the client. This is a read-only property; the client cannot specify what encoding type a device uses to send messages. These values duplicate the [**WPD\_SMS\_ENCODING\_TYPES**](wpd-sms-encoding-types.md) enumerated values. |
| **WPD\_SMS\_MAX\_PAYLOAD** | **VT\_UI4**    | The maximum number of bytes that can be contained in a message.                                                                                                                                                                                                                                             |
| **WPD\_SMS\_PROVIDER**     | **VT\_LPWSTR** | The service provider's name.                                                                                                                                                                                                                                                                                |
| **WPD\_SMS\_TIMEOUT**      | **VT\_UI4**    | The number of milliseconds until a timeout is returned.                                                                                                                                                                                                                                                     |



 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**WPD Properties and Attributes**](properties-and-attributes.md)
</dt> </dl>

 

 




