---
title: CHANGER\_PRODUCT\_DATA structure
description: The CHANGER\_PRODUCT\_DATA structure is used in conjunction with the IOCTL\_CHANGER\_GET\_PRODUCT\_DATA request to retrieve product data for a device.
ms.assetid: '18e5b394-b0ea-481c-b634-83a2ebec4784'
keywords: ["CHANGER_PRODUCT_DATA structure Storage Devices", "PCHANGER_PRODUCT_DATA structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- CHANGER_PRODUCT_DATA
api_location:
- ntddchgr.h
api_type:
- HeaderDef
---

# CHANGER\_PRODUCT\_DATA structure

The CHANGER\_PRODUCT\_DATA structure is used in conjunction with the [**IOCTL\_CHANGER\_GET\_PRODUCT\_DATA**](ioctl-changer-get-product-data.md) request to retrieve product data for a device.

## Syntax


```C++
typedef struct _CHANGER_PRODUCT_DATA {
  UCHAR VendorId[VENDOR_ID_LENGTH];
  UCHAR ProductId[PRODUCT_ID_LENGTH];
  UCHAR Revision[REVISION_LENGTH];
  UCHAR SerialNumber[SERIAL_NUMBER_LENGTH];
  UCHAR DeviceType;
} CHANGER_PRODUCT_DATA, *PCHANGER_PRODUCT_DATA;
```



## Members

<dl> <dt>

**VendorId**
</dt> <dd>

Specifies the name of the device manufacturer.

</dd> <dt>

**ProductId**
</dt> <dd>

Specifies the product identification as defined by the vendor.

</dd> <dt>

**Revision**
</dt> <dd>

Specifies the product revision as defined by the vendor.

</dd> <dt>

**SerialNumber**
</dt> <dd>

Specifies the value defined by the vendor to identify this device. Serial numbers are unique for all changers of a given type, but are not necessarily unique across vendor and product lines. For a SCSI changer, this value might be from Vital Product Data. If **SerialNumber** is not unique, the miniclass driver should not set the CHANGER\_SERIAL\_NUMBER\_VALID flag in the **Features0** member of the [**GET\_CHANGER\_PARAMETERS**](get-changer-parameters.md) structure.

</dd> <dt>

**DeviceType**
</dt> <dd>

Specifies the device type of the changer. This member must be MEDIUM\_CHANGER.

</dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddchgr.h</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_CHANGER\_GET\_PRODUCT\_DATA**](ioctl-changer-get-product-data.md)
</dt> <dt>

[**ChangerGetProductData**](changergetproductdata.md)
</dt> <dt>

[**GET\_CHANGER\_PARAMETERS**](get-changer-parameters.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CHANGER_PRODUCT_DATA%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






