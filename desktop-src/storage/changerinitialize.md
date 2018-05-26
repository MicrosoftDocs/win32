---
title: ChangerInitialize function
description: ChangerInitialize readies the changer to receive other requests.
ms.assetid: 7cb90d35-53e5-4c73-a1f5-9fc3f99cf1b2
keywords:
- ChangerInitialize function Storage Devices
topic_type:
- apiref
api_name:
- ChangerInitialize
api_location:
- mcd.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ChangerInitialize function

**ChangerInitialize** readies the changer to receive other requests.

## Syntax


```C++
NTSTATUS ChangerInitialize(
  _In_ PDEVICE_OBJECT DeviceObject
);
```



## Parameters

<dl> <dt>

*DeviceObject* \[in\]
</dt> <dd>

Pointer to the device object created by the changer class driver to represent this changer.

</dd> </dl>

## Return value

**ChangerInitialize** returns the STATUS\_*XXX* value returned by the system port driver or one of the following values:

STATUS\_SUCCESS

STATUS\_INSUFFICIENT\_RESOURCES

## Remarks

The changer class driver calls **ChangerInitialize** during driver initialization, after creating a device object to represent a changer.

**ChangerInitialize** performs any device-specific processing required to get the changer ready to receive requests. It also typically stores device-specific information in the device extension, such as SCSI inquiry data or the non-SCSI equivalent and offsets to generate zero-based element addresses, which are used by the system to refer to changer elements.

After **ChangerInitialize** returns, the changer miniclass driver and the changer should be able to handle any other request.

## Requirements



|                            |                                                                                                                |
|----------------------------|----------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                             |
| Header<br/>          | <dl> <dt>Mcd.h (include Mcd.h or Ntddchgr.h)</dt> </dl> |
| IRQL<br/>            | PASSIVE\_LEVEL<br/>                                                                                      |



## See also

<dl> <dt>

[**ChangerAdditionalExtensionSize**](changeradditionalextensionsize.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ChangerInitialize%20function%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






