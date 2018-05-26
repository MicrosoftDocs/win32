---
title: STORAGE\_IDENTIFIER\_TYPE enumeration
description: The STORAGE\_IDENTIFIER\_TYPE enumeration specifies the type of storage identifier.
ms.assetid: 1f909dc3-732d-4ade-a2b7-fd60b1f09de7
keywords:
- STORAGE_IDENTIFIER_TYPE enumeration Storage Devices
- PSTORAGE_IDENTIFIER_TYPE enumeration pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_IDENTIFIER_TYPE
api_location:
- ntddstor.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# STORAGE\_IDENTIFIER\_TYPE enumeration

The STORAGE\_IDENTIFIER\_TYPE enumeration specifies the type of storage identifier.

## Syntax


```C++
typedef enum _STORAGE_IDENTIFIER_TYPE { 
  StorageIdTypeVendorSpecific            = 0,
  StorageIdTypeVendorId                  = 1,
  StorageIdTypeEUI64                     = 2,
  StorageIdTypeFCPHName                  = 3,
  StorageIdTypePortRelative              = 4,
  StorageIdTypeTargetPortGroup           = 5,
  StorageIdTypeLogicalUnitGroup          = 6,
  StorageIdTypeMD5LogicalUnitIdentifier  = 7,
  StorageIdTypeScsiNameString            = 8
} STORAGE_IDENTIFIER_TYPE, *PSTORAGE_IDENTIFIER_TYPE;
```



## Constants

<dl> <dt>

<span id="StorageIdTypeVendorSpecific"></span><span id="storageidtypevendorspecific"></span><span id="STORAGEIDTYPEVENDORSPECIFIC"></span>**StorageIdTypeVendorSpecific**
</dt> <dd>

Indicates that the vendor created the identifier without reference to an assignment authority, and consequently there is no guarantee that the identifier is globally unique

</dd> <dt>

<span id="StorageIdTypeVendorId"></span><span id="storageidtypevendorid"></span><span id="STORAGEIDTYPEVENDORID"></span>**StorageIdTypeVendorId**
</dt> <dd>

Indicates a vendor identifier strings assigned by the SCSI-3 specification to the vendor.

</dd> <dt>

<span id="StorageIdTypeEUI64"></span><span id="storageidtypeeui64"></span><span id="STORAGEIDTYPEEUI64"></span>**StorageIdTypeEUI64**
</dt> <dd>

Indicates a 64-bit IEEE extended unique

identifier (EUI-64).

</dd> <dt>

<span id="StorageIdTypeFCPHName"></span><span id="storageidtypefcphname"></span><span id="STORAGEIDTYPEFCPHNAME"></span>**StorageIdTypeFCPHName**
</dt> <dd>

Indicates a 64-bit FC-PH name identifier

as defined in the *X3.230-1994* specification.

</dd> <dt>

<span id="StorageIdTypePortRelative"></span><span id="storageidtypeportrelative"></span><span id="STORAGEIDTYPEPORTRELATIVE"></span>**StorageIdTypePortRelative**
</dt> <dd>

Indicates that the identifier type depends on the port.

</dd> <dt>

<span id="StorageIdTypeTargetPortGroup"></span><span id="storageidtypetargetportgroup"></span><span id="STORAGEIDTYPETARGETPORTGROUP"></span>**StorageIdTypeTargetPortGroup**
</dt> <dd></dd> <dt>

<span id="StorageIdTypeLogicalUnitGroup"></span><span id="storageidtypelogicalunitgroup"></span><span id="STORAGEIDTYPELOGICALUNITGROUP"></span>**StorageIdTypeLogicalUnitGroup**
</dt> <dd></dd> <dt>

<span id="StorageIdTypeMD5LogicalUnitIdentifier"></span><span id="storageidtypemd5logicalunitidentifier"></span><span id="STORAGEIDTYPEMD5LOGICALUNITIDENTIFIER"></span>**StorageIdTypeMD5LogicalUnitIdentifier**
</dt> <dd></dd> <dt>

<span id="StorageIdTypeScsiNameString"></span><span id="storageidtypescsinamestring"></span><span id="STORAGEIDTYPESCSINAMESTRING"></span>**StorageIdTypeScsiNameString**
</dt> <dd>

Indicates that the identifier type is specified by a Scsi name string.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**STORAGE\_IDENTIFIER**](storage-identifier.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_IDENTIFIER_TYPE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






