---
title: STORAGE\_ASSOCIATION\_TYPE enumeration
description: The STORAGE\_ASSOCIATION\_TYPE enumeration indicates whether a storage descriptor identifies a device or a port.
ms.assetid: '662793e6-e97e-4140-96e6-f75f638b5bbb'
keywords: ["STORAGE_ASSOCIATION_TYPE enumeration Storage Devices", "PSTORAGE_ASSOCIATION_TYPE enumeration pointer Storage Devices"]
topic_type:
- apiref
api_name:
- STORAGE_ASSOCIATION_TYPE
api_location:
- ntddstor.h
api_type:
- HeaderDef
---

# STORAGE\_ASSOCIATION\_TYPE enumeration

The STORAGE\_ASSOCIATION\_TYPE enumeration indicates whether a storage descriptor identifies a device or a port.

## Syntax


```C++
typedef enum _STORAGE_ASSOCIATION_TYPE { 
  StorageIdAssocDevice  = 0,
  StorageIdAssocPort    = 1,
  StorageIdAssocTarget  = 2
} STORAGE_ASSOCIATION_TYPE, *PSTORAGE_ASSOCIATION_TYPE;
```



## Constants

<dl> <dt>

<span id="StorageIdAssocDevice"></span><span id="storageidassocdevice"></span><span id="STORAGEIDASSOCDEVICE"></span>**StorageIdAssocDevice**
</dt> <dd>

Indicates that the descriptor identifies a device.

</dd> <dt>

<span id="StorageIdAssocPort"></span><span id="storageidassocport"></span><span id="STORAGEIDASSOCPORT"></span>**StorageIdAssocPort**
</dt> <dd>

Indicates that the descriptor identifies a port.

</dd> <dt>

<span id="StorageIdAssocTarget"></span><span id="storageidassoctarget"></span><span id="STORAGEIDASSOCTARGET"></span>**StorageIdAssocTarget**
</dt> <dd>

Indicates that the descriptor identifies a target.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**STORAGE\_IDENTIFIER**](storage-identifier.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_ASSOCIATION_TYPE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






