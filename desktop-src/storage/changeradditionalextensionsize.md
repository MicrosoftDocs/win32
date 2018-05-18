---
title: ChangerAdditionalExtensionSize function
description: ChangerAdditionalExtensionSize indicates the number of bytes the changer miniclass driver requires to store device-specific information in the device extension.
ms.assetid: 'd9bcbad5-ce2c-4968-9544-4fb024b1e933'
keywords: ["ChangerAdditionalExtensionSize function Storage Devices"]
topic_type:
- apiref
api_name:
- ChangerAdditionalExtensionSize
api_location:
- mcd.h
api_type:
- HeaderDef
---

# ChangerAdditionalExtensionSize function

**ChangerAdditionalExtensionSize** indicates the number of bytes the changer miniclass driver requires to store device-specific information in the device extension.

## Syntax


```C++
ULONG ChangerAdditionalExtensionSize(void);
```



## Parameters

This function has no parameters.

## Return value

**ChangerAdditionalExtensionSize** returns the size, in bytes, of the additional device extension space required by the changer miniclass driver.

## Remarks

The changer class driver calls **ChangerAdditionalExtensionSize** to determine the number of bytes the miniclass driver requires in the device extension for a particular changer before creating the device object to represent that changer.

The device-specific information stored by a changer miniclass driver is determined by the driver. It typically includes zero-based offsets that other miniclass driver routines can use to translate between device-specific element addresses and the zero-based element addresses used by the system. It can also include SCSI inquiry data or the non-SCSI equivalent.

## Requirements



|                            |                                                                                                                |
|----------------------------|----------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                             |
| Header<br/>          | <dl> <dt>Mcd.h (include Mcd.h or Ntddchgr.h)</dt> </dl> |
| IRQL<br/>            | PASSIVE\_LEVEL<br/>                                                                                      |



## See also

<dl> <dt>

[**ChangerInitialize**](changerinitialize.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ChangerAdditionalExtensionSize%20function%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






