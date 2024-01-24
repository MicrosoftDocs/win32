---
description: Specifies whether the Source Reader passes through video samples backed by the system memory to internal MFTs without automatically copying them into a DirectX texture.
title: MF_SOURCE_READER_PASSTHROUGH_MODE attribute
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_SOURCE\_READER\_PASSTHROUGH\_MODE attribute

When this attribute is set, the [Source Reader](source-reader.md) passes through video samples backed by the system memory to internal MFTs without automatically copying them into a DirectX texture, even if a Direct3D device manager is present.

## Data type

**BOOL** stored as **UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).


## Remarks

The constant **MF_SOURCE_READER_PASSTHROUGH_MODE** is not defined in a Windows SDK header file so the caller must specify the GUID value to reference the attribute.

| Attribute | Value |
|-----------|-------|
| MF_SOURCE_READER_PASSTHROUGH_MODE | 043FF126-FE2C-4708-A09B-DA2AB435CED9 |


## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 build 19041<br/>                                        |




## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Source Reader](source-reader.md)
</dt> <dt>

[Source Reader Attributes](source-reader-attributes.md)
</dt> </dl>

 

 




