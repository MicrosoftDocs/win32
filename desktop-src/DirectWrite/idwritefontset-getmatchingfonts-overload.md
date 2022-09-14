---
title: IDWriteFontSet GetMatchingFonts methods
description: Returns a subset of fonts matching the specified criteria.
ms.assetid: 9f80478e-ed45-58c7-723f-8fe9bd05097b
keywords:
- GetMatchingFonts methods Direct Write
topic_type:
- apiref
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_name: 
api_location: 
---

# IDWriteFontSet::GetMatchingFonts methods

Returns a subset of fonts matching the specified criteria.

### Overload list



| Method                                                                                                                                                             | Description                                                                                 |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------|
| [**GetMatchingFonts(const WCHAR\*, DWRITE\_FONT\_WEIGHT, DWRITE\_FONT\_STRETCH, DWRITE\_FONT\_STYLE, IDWriteFontSet\*\*)**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefontset-getmatchingfonts(wcharconst_dwrite_font_weight_dwrite_font_stretch_dwrite_font_style_idwritefontset)) | Returns a list of fonts within the given WWS family prioritized by WWS distance.<br/> |
| [**GetMatchingFonts(const DWRITE\_FONT\_PROPERTY\*, UINT32, IDWriteFontSet\*\*)**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefontset-getmatchingfonts(dwrite_font_propertyconst_uint32_idwritefontset))                                          | Returns a subset of fonts filtered by the given properties.<br/>                      |



## See also

<dl> <dt>

[**IDWriteFontSet**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontset)
</dt> </dl>

 

