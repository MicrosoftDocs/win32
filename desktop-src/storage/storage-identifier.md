---
title: STORAGE\_IDENTIFIER structure
description: The STORAGE\_IDENTIFIER structure represents a SCSI identification descriptor.
ms.assetid: 'f2b0610a-dffa-48fb-bc5a-355fa9f05770'
keywords: ["STORAGE_IDENTIFIER structure Storage Devices", "PSTORAGE_IDENTIFIER structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- STORAGE_IDENTIFIER
api_location:
- ntddstor.h
api_type:
- HeaderDef
---

# STORAGE\_IDENTIFIER structure

The STORAGE\_IDENTIFIER structure represents a SCSI identification descriptor.

## Syntax


```C++
typedef struct _STORAGE_IDENTIFIER {
  STORAGE_IDENTIFIER_CODE_SET CodeSet;
  STORAGE_IDENTIFIER_TYPE     Type;
  USHORT                      IdentifierSize;
  USHORT                      NextOffset;
  STORAGE_ASSOCIATION_TYPE    Association;
  UCHAR                       Identifier[1];
} STORAGE_IDENTIFIER, *PSTORAGE_IDENTIFIER;
```



## Members

<dl> <dt>

**CodeSet**
</dt> <dd>

Specifies the code set used by a SCSI identification descriptor to identify a logical unit.

</dd> <dt>

**Type**
</dt> <dd>

Contains an enumerator value of type [**STORAGE\_IDENTIFIER\_TYPE**](storage-identifier-type.md) that indicates the identifier type.

</dd> <dt>

**IdentifierSize**
</dt> <dd>

Specifies the size in bytes of the identifier.

</dd> <dt>

**NextOffset**
</dt> <dd>

Specifies the offset in bytes from the current descriptor to the next descriptor.

</dd> <dt>

**Association**
</dt> <dd>

Contains an enumerator value of type [**STORAGE\_ASSOCIATION\_TYPE**](storage-association-type.md) that indicates whether the descriptor identifies a device or a port.

</dd> <dt>

**Identifier**
</dt> <dd>

Contains the identifier associated with this descriptor.

</dd> </dl>

## Remarks

Every device identification page (page code 0x83) of SCSI vital product data contains a series of identification descriptors. The STORAGE\_IDENTIFIER structure represents a SCSI identification descriptor.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**STORAGE\_ASSOCIATION\_TYPE**](storage-association-type.md)
</dt> <dt>

[**STORAGE\_IDENTIFIER\_TYPE**](storage-identifier-type.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_IDENTIFIER%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






