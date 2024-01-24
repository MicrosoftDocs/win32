---
title: Direct2D constants
description: Direct2D defines the following list of constants.
ms.assetid: 98a443af-4bb7-486d-bc87-ff34c3671bdd
topic_type:
- apiref
api_name:
- D2D1_APPEND_ALIGNED_ELEMENT
- D2D1_DEFAULT_FLATTENING_TOLERANCE
- D2D1_INVALID_PROPERTY_INDEX
- D2D1_INVALID_TAG
- D2D1_SCENE_REFERRED_SDR_WHITE_LEVEL
api_location:
- d2d1.h
- d2d1effects_2.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 09/19/2019
---

# Direct2D constants

The following constants are declared in the `d2d1effectauthor.h`, `d2d1.h`, `d2d1_1.h`, and `d2d1effects_2.h` header files.

## D2D1_APPEND_ALIGNED_ELEMENT (-1)
Used when packing input layout elements. It indicates that the elements must be packed contiguously.

## D2D1_DEFAULT_FLATTENING_TOLERANCE (0.25f)
The default tolerance for geometric flattening operations.

## D2D1_INVALID_PROPERTY_INDEX (UINT_MAX)
Defines an invalid property index.

This constant is returned from [**ID2D1Properties::GetPropertyIndex**](/windows/win32/api/d2d1_1/nf-d2d1_1-id2d1properties-getpropertyindex) to indicate that the named property that you provided doesn't have an index in the property interface.

If you pass this constant to [**ID2D1Properties::GetValue**](/windows/win32/api/d2d1_1/nf-d2d1_1-id2d1properties-getvalue(uint32_byte_uint32)) or [**ID2D1Properties::GetValueByName**](/windows/win32/api/d2d1_1/nf-d2d1_1-id2d1properties-getvaluebyname(pcwstr_byte_uint32)), then the call fails, and the output buffer is zero-filled.

## D2D1_INVALID_TAG (ULONGLONG_MAX)
Reserved; don't use.

## D2D1_SCENE_REFERRED_SDR_WHITE_LEVEL (80.0f)
The number of nits that sRGB or scRGB color space uses for SDR white, or floating point values of 1.0f. This value is constant only when the color space uses scene-referred luminance, which is true for high dynamic range (HDR) content. If the color space uses display-referred luminance instead, then the SDR white level should be queried from the display.

## Requirements

| Requirement | Value |
|-|-|
| Minimum supported client | Windows 7, Windows Vista with SP2 and Platform Update for Windows Vista \[desktop apps \| UWP apps\] |
| Minimum supported server | Windows Server 2008 R2, Windows Server 2008 with SP2 and Platform Update for Windows Server 2008 \[desktop apps \| UWP apps\] |
| Minimum supported phone | Windows Phone 8.1 \[Windows Phone Silverlight 8.1 and Windows Runtime apps\], Windows Phone 8.1 \[Windows Phone Silverlight 8.1 and Windows Runtime apps\] |
| Header | d2d1effectauthor.h, d2d1.h, d2d1_1.h, d2d1effects_2.h |
