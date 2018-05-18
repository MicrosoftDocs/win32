---
title: IOCTL\_STORAGE\_FIND\_NEW\_DEVICES control code
description: Determines whether another device that the driver supports has been connected to the I/O bus, either since the system was booted or since the driver last processed this request.
ms.assetid: '359169a3-602d-4910-badf-c777c1a804e7'
keywords: ["IOCTL_STORAGE_FIND_NEW_DEVICES control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_STORAGE_FIND_NEW_DEVICES
api_location:
- Ntddstor.h
api_type:
- HeaderDef
---

# IOCTL\_STORAGE\_FIND\_NEW\_DEVICES control code

Determines whether another device that the driver supports has been connected to the I/O bus, either since the system was booted or since the driver last processed this request.

This IOCTL is obsolete in the Plug and Play environment. Plug and Play class drivers handle this request by calling [**IoInvalidateDeviceRelations**](https://msdn.microsoft.com/library/windows/hardware/ff549353) with the device relations type **BusRelations**. If a new device is found, the class driver's *AddDevice* routine will be called.

Legacy class drivers can continue to handle this IOCTL without modifications. If a new device is found, the driver sets up any necessary system objects and resources to handle I/O requests for its new device. It also initializes the device on receipt of this request dynamically, that is, without requiring the machine to be rebooted. Such a driver is assumed to support devices connected on a dynamically configurable I/O bus.

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Information** field is set to zero. The **Status** field can be set to STATUS\_SUCCESS or to any other value returned by a Plug and Play driver's **IoInvalidateDeviceRelations** call or a legacy driver's (re)initialization code.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_STORAGE_FIND_NEW_DEVICES%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





