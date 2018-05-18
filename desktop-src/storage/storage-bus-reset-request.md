---
title: STORAGE\_BUS\_RESET\_REQUEST structure
description: The STORAGE\_BUS\_RESET\_REQUEST structure is used in conjunction with the IOCTL\_STORAGE\_RESET\_BUS request to specify the path of the bus to be reset.
ms.assetid: 'd2f2d2cc-e96b-475c-96eb-d58244a05788'
keywords: ["STORAGE_BUS_RESET_REQUEST structure Storage Devices", "PSTORAGE_BUS_RESET_REQUEST structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- STORAGE_BUS_RESET_REQUEST
api_location:
- ntddstor.h
api_type:
- HeaderDef
---

# STORAGE\_BUS\_RESET\_REQUEST structure

The STORAGE\_BUS\_RESET\_REQUEST structure is used in conjunction with the [**IOCTL\_STORAGE\_RESET\_BUS**](ioctl-storage-reset-bus.md) request to specify the path of the bus to be reset.

## Syntax


```C++
typedef struct _STORAGE_BUS_RESET_REQUEST {
  UCHAR PathId;
} STORAGE_BUS_RESET_REQUEST, *PSTORAGE_BUS_RESET_REQUEST;
```



## Members

<dl> <dt>

**PathId**
</dt> <dd>

Indicates the number of the bus to be reset.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_RESET\_BUS**](ioctl-storage-reset-bus.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_BUS_RESET_REQUEST%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






