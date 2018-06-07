---
title: STORAGE\_IDENTIFIER\_CODE\_SET enumeration
description: The STORAGE\_IDENTIFIER\_CODE\_SET enumeration specifies the code set used by a SCSI identification descriptor (STORAGE\_IDENTIFIER) to identify a logical unit.
ms.assetid: 84829b4d-4929-4607-8c0c-0859a183752d
keywords:
- STORAGE_IDENTIFIER_CODE_SET enumeration Storage Devices
- PSTORAGE_IDENTIFIER_CODE_SET enumeration pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_IDENTIFIER_CODE_SET
api_location:
- ntddstor.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# STORAGE\_IDENTIFIER\_CODE\_SET enumeration

The STORAGE\_IDENTIFIER\_CODE\_SET enumeration specifies the code set used by a SCSI identification descriptor ([**STORAGE\_IDENTIFIER**](storage-identifier.md)) to identify a logical unit.

## Syntax


```C++
typedef enum _STORAGE_IDENTIFIER_CODE_SET { 
  StorageIdCodeSetReserved  = 0,
  StorageIdCodeSetBinary    = 1,
  StorageIdCodeSetAscii     = 2,
  StorageIdCodeSetUtf8      = 3
} STORAGE_IDENTIFIER_CODE_SET, *PSTORAGE_IDENTIFIER_CODE_SET;
```



## Constants

<dl> <dt>

<span id="StorageIdCodeSetReserved"></span><span id="storageidcodesetreserved"></span><span id="STORAGEIDCODESETRESERVED"></span>**StorageIdCodeSetReserved**
</dt> <dd>

Reserved.

</dd> <dt>

<span id="StorageIdCodeSetBinary"></span><span id="storageidcodesetbinary"></span><span id="STORAGEIDCODESETBINARY"></span>**StorageIdCodeSetBinary**
</dt> <dd>

Indicates that the identification descriptor contains a binary representation of the identifier.

</dd> <dt>

<span id="StorageIdCodeSetAscii"></span><span id="storageidcodesetascii"></span><span id="STORAGEIDCODESETASCII"></span>**StorageIdCodeSetAscii**
</dt> <dd>

Indicates that the identification descriptor contains an ASCII representation of the identifier.

</dd> <dt>

<span id="StorageIdCodeSetUtf8"></span><span id="storageidcodesetutf8"></span><span id="STORAGEIDCODESETUTF8"></span>**StorageIdCodeSetUtf8**
</dt> <dd>

Indicates that the identification descriptor contains a UTF8 representation of the identifier.

</dd> </dl>

## Remarks

This field is intended to be an aid to software that displays the identifier field. Every device identification page (page code 0x83) of SCSI vital product data contains a series of identification descriptors, each of which contains an identifier.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**STORAGE\_IDENTIFIER**](storage-identifier.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_IDENTIFIER_CODE_SET%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






