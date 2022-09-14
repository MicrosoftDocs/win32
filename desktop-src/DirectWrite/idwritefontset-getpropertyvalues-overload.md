---
title: IDWriteFontSet GetPropertyValues methods (Dwrite\_3.h)
description: Returns property values for the font set.
ms.assetid: 3c3fd5b7-88dd-d434-0b62-f365b407c379
keywords:
- GetPropertyValues methods Direct Write
topic_type:
- apiref
api_location:
- dwrite_3.h
api_type:
- HeaderDef
ms.date: 07/02/2019
ms.topic: reference
---

# IDWriteFontSet::GetPropertyValues methods

Returns property values for the font set.

### Overload list



| Method                                                                                                                                   | Description                                                                                                                                                                                                                                                                                                   |
|:-----------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetPropertyValues(DWRITE\_FONT\_PROPERTY\_ID, IDWriteStringList\*\*)**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefontset-getpropertyvalues(dwrite_font_property_id_idwritestringlist))                       | Returns all unique property values in the set, which can be used for purposes such as displaying a family list or tag cloud. All values are returned regardless of language, including all localized names. <br/>                                                                                       |
| [**GetPropertyValues(DWRITE\_FONT\_PROPERTY\_ID, const WCHAR\*, IDWriteStringList\*\*)**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefontset-getpropertyvalues(dwrite_font_property_id_wcharconst_idwritestringlist))        | Returns all unique property values in the set, which can be used for purposes such as displaying a family list or tag cloud. Values are returned in priority order according to the language list, such that if a font contains more than one localized name, the preferred one will be returned. <br/> |
| [**GetPropertyValues(UINT32, DWRITE\_FONT\_PROPERTY\_ID, BOOL\*, IDWriteLocalizedStrings\*\*)**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefontset-getpropertyvalues(dwrite_font_property_id_idwritestringlist)) | Returns the property values of a specific font item index.<br/>                                                                                                                                                                                                                                         |



## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dwrite\_3.h</dt> </dl> |



## See also

<dl> <dt>

[**IDWriteFontSet**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontset)
</dt> </dl>

�

�
