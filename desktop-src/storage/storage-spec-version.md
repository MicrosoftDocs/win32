---
title: STORAGE\_SPEC\_VERSION union
description: Indicates the specification of the storage device.
ms.assetid: E7E80C4E-C002-4F00-AF7E-6B8DDA337323
keywords:
- STORAGE_SPEC_VERSION union Storage Devices
- PSTORAGE_SPEC_VERSION union pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_SPEC_VERSION
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# STORAGE\_SPEC\_VERSION union

Indicates the specification of the storage device.

## Syntax


```C++
typedef union _STORAGE_SPEC_VERSION {
  struct {
    union {
      struct {
        BYTE SubMinor;
        BYTE Minor;
      } DUMMYSTRUCTNAME;
      WORD   AsUshort;
    } MinorVersion;
    WORD  MajorVersion;
  } DUMMYSTRUCTNAME;
  DWORD  AsUlong;
} STORAGE_SPEC_VERSION, *PSTORAGE_SPEC_VERSION;
```



## Members

<dl> <dt>

**DUMMYSTRUCTNAME**
</dt> <dd>

The major and minor version of the storage specification.

<dl> <dt>

**MinorVersion**
</dt> <dd>

The minor version of the storage specification.

<dl> <dt>

**DUMMYSTRUCTNAME**
</dt> <dd>

The minor and sub-minor version of the storage specification.

<dl> <dt>

**SubMinor**
</dt> <dd>

The sub-minor version of the storage specification.

</dd> <dt>

**Minor**
</dt> <dd>

The minor version of the storage specification.

</dd> </dl> </dd> <dt>

**AsUshort**
</dt> <dd>

The combination of the **Minor** and **SubMinor** versions of the storage specification.

</dd> </dl> </dd> <dt>

**MajorVersion**
</dt> <dd>

The major version of the storage specification.

</dd> </dl> </dd> <dt>

**AsUlong**
</dt> <dd>

The combination of the **MajorVersion** and **MinorVersion** versions of the storage specification.

</dd> </dl>

## Remarks

This union allows for specifying the storage specification version, such as SBC 3, SATA 3.2, and NVMe 1.2.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_SPEC_VERSION%20union%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





