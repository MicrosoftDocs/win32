---
title: DSM\_VERSION structure
description: The DSM\_VERSION structure represents version information that is associated with a DSM binary or package.
ms.assetid: 1aa264fa-b552-41a0-bd43-a62f8f2b533b
keywords:
- DSM_VERSION structure Storage Devices
- PDSM_VERSION structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DSM_VERSION
api_location:
- mpiowmi.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# DSM\_VERSION structure

The DSM\_VERSION structure represents version information that is associated with a DSM binary or package. While this assumes that a DSM's version will be of the type MajorVersion.MinorVersion.ProductBuild.QfeNumber, it is not mandatory for the DSM to follow this convention. The DSM must, however, fill in zeros for the fields its does not support.

## Syntax


```C++
typedef struct _DSM_VERSION {
  ULONG MajorVersion;
  ULONG MinorVersion;
  ULONG ProductBuild;
  ULONG QfeNumber;
} DSM_VERSION, *PDSM_VERSION;
```



## Members

<dl> <dt>

**MajorVersion**
</dt> <dd>

An unsigned 32-bitfield that represents the major version portion of the version.

</dd> <dt>

**MinorVersion**
</dt> <dd>

An unsigned 32-bitfield that represents the minor version portion of the version.

</dd> <dt>

**ProductBuild**
</dt> <dd>

An unsigned 32-bitfield that represents the product build portion of the version.

</dd> <dt>

**QfeNumber**
</dt> <dd>

An unsigned 32-bitfield that represents the QFE number portion of the version.

</dd> </dl>

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mpiowmi.h (include Mpiowmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DSM_VERSION%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





