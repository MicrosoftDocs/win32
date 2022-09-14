---
title: Is_Trusted
description: The Is\_Trusted attribute is a file-level attribute specifying whether the license acquisition URL in the file is trusted.
ms.assetid: 7b383b45-e992-4a07-af0b-9ef220ddd9af
keywords:
- Is_Trusted windows Media Format
topic_type:
- apiref
api_name:
- Is_Trusted
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Is\_Trusted

The **Is\_Trusted** attribute is a file-level attribute specifying whether the license acquisition URL in the file is trusted.

## Global Constant

g\_wszWMTrusted

## Data Type

**WMT\_TYPE\_BOOL**

## Remarks

This is a coded attribute.

Before navigating to a license acquisition URL contained in a DRM-protected file, an application should first verify that this property is true. If it is false, the application should notify the user that the URL has possibly been tampered with.

This attribute cannot be duplicated at the file level. If this attribute is used for an individual stream, it will be treated as custom metadata and will not convey its normal meaning to the objects of the Windows Media Format SDK.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




