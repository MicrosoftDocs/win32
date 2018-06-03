---
title: ChangerGetProductData function
description: ChangerGetProductData handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL\_CHANGER\_GET\_PRODUCT\_DATA.
ms.assetid: b2723a34-d9c2-40c9-b6c9-6441ead63d2e
keywords:
- ChangerGetProductData function Storage Devices
topic_type:
- apiref
api_name:
- ChangerGetProductData
api_location:
- mcd.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ChangerGetProductData function

**ChangerGetProductData** handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL\_CHANGER\_GET\_PRODUCT\_DATA.

## Syntax


```C++
NTSTATUS ChangerGetProductData(
  _In_ PDEVICE_OBJECT DeviceObject,
  _In_ PIRP           Irp
);
```



## Parameters

<dl> <dt>

*DeviceObject* \[in\]
</dt> <dd>

Pointer to the device object that represents the changer.

</dd> <dt>

*Irp* \[in\]
</dt> <dd>

Pointer to the IRP.

</dd> </dl>

## Return value

**ChangerGetProductData** always returns STATUS\_SUCCESS.

## Remarks

This routine is required.

**ChangerGetProductData** returns product data for a changer.

The changer class driver checks the output buffer length in the I/O stack location before calling **ChangerGetProductData**. If output buffer length is smaller than **sizeof**(CHANGER\_PRODUCT\_DATA) then the changer class driver returns with a value of STATUS\_INFO\_LENGTH\_MISMATCH

**ChangerGetProductData** fills in a [**CHANGER\_PRODUCT\_DATA**](changer-product-data.md) structure at *Irp***-&gt;AssociatedIrp.SystemBuffer** before returning to the changer class driver. If the miniclass driver cached inquiry data in the changer's device extension before returning from **ChangerInitialize**, all members except **DeviceType** can be filled in from this data.

## Requirements



|                            |                                                                                                                |
|----------------------------|----------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                             |
| Header<br/>          | <dl> <dt>Mcd.h (include Mcd.h or Ntddchgr.h)</dt> </dl> |
| IRQL<br/>            | PASSIVE\_LEVEL<br/>                                                                                      |



## See also

<dl> <dt>

[**ChangerInitialize**](changerinitialize.md)
</dt> <dt>

[**CHANGER\_PRODUCT\_DATA**](changer-product-data.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ChangerGetProductData%20function%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






