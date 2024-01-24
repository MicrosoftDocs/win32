---
description: The MXDC\_S0\_PAGE\_ENUMS enumeration is used to specify types of resources that can be associated with pages in XPS documents and that can be processed, or passed unprocessed, by Microsoft XPS Document Converter (MXDC) to its output.
ms.assetid: e111d92e-5102-4b39-b311-f9ff1d1a96f1
title: MXDC_S0_PAGE_ENUMS enumeration (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MXDC_S0_PAGE_ENUMS
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# MXDC\_S0\_PAGE\_ENUMS enumeration

The **MXDC\_S0\_PAGE\_ENUMS** enumeration is used to specify types of resources that can be associated with pages in XPS documents and that can be processed, or passed unprocessed, by Microsoft XPS Document Converter (MXDC) to its output.

## Syntax


```C++
typedef enum tagMxdcS0PageEnums { 
  MXDC_RESOURCE_TTF,
  MXDC_RESOURCE_JPEG,
  MXDC_RESOURCE_PNG,
  MXDC_RESOURCE_TIFF,
  MXDC_RESOURCE_WDP,
  MXDC_RESOURCE_DICTIONARY,
  MXDC_RESOURCE_ICC_PROFILE,
  MXDC_RESOURCE_JPEG_THUMBNAIL,
  MXDC_RESOURCE_PNG_THUMBNAIL,
  MXDC_RESOURCE_MAX
} MXDC_S0_PAGE_ENUMS;
```



## Constants

<dl> <dt>

<span id="MXDC_RESOURCE_TTF"></span><span id="mxdc_resource_ttf"></span>**MXDC\_RESOURCE\_TTF**
</dt> <dd>

TrueType or OpenType font.

</dd> <dt>

<span id="MXDC_RESOURCE_JPEG"></span><span id="mxdc_resource_jpeg"></span>**MXDC\_RESOURCE\_JPEG**
</dt> <dd>

JPEG image

</dd> <dt>

<span id="MXDC_RESOURCE_PNG"></span><span id="mxdc_resource_png"></span>**MXDC\_RESOURCE\_PNG**
</dt> <dd>

PNG image.

</dd> <dt>

<span id="MXDC_RESOURCE_TIFF"></span><span id="mxdc_resource_tiff"></span>**MXDC\_RESOURCE\_TIFF**
</dt> <dd>

TIFF image.

</dd> <dt>

<span id="MXDC_RESOURCE_WDP"></span><span id="mxdc_resource_wdp"></span>**MXDC\_RESOURCE\_WDP**
</dt> <dd>

Windows Media Photo image.

</dd> <dt>

<span id="MXDC_RESOURCE_DICTIONARY"></span><span id="mxdc_resource_dictionary"></span>**MXDC\_RESOURCE\_DICTIONARY**
</dt> <dd>

Remote resource dictionary that should be passed to MXDC's output unprocessed.

</dd> <dt>

<span id="MXDC_RESOURCE_ICC_PROFILE"></span><span id="mxdc_resource_icc_profile"></span>**MXDC\_RESOURCE\_ICC\_PROFILE**
</dt> <dd>

ICC profile that should be passed to MXDC's output unprocessed.

</dd> <dt>

<span id="MXDC_RESOURCE_JPEG_THUMBNAIL"></span><span id="mxdc_resource_jpeg_thumbnail"></span>**MXDC\_RESOURCE\_JPEG\_THUMBNAIL**
</dt> <dd>

JPEG thumbnail that should be passed to MXDC's output unprocessed.

</dd> <dt>

<span id="MXDC_RESOURCE_PNG_THUMBNAIL"></span><span id="mxdc_resource_png_thumbnail"></span>**MXDC\_RESOURCE\_PNG\_THUMBNAIL**
</dt> <dd>

PNG thumbnail that should be passed to MXDC's output unprocessed.

</dd> <dt>

<span id="MXDC_RESOURCE_MAX"></span><span id="mxdc_resource_max"></span>**MXDC\_RESOURCE\_MAX**
</dt> <dd>

The maximum resource count for validation.

</dd> </dl>

## Remarks

This enumeration is primarily used as the **dwResourceType** member of the [**MXDC\_XPS\_S0PAGE\_RESOURCE\_T**](mxdcxpss0pageresource.md) structure.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |



 

 




