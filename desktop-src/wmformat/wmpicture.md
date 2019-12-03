---
title: WM/Picture
description: The WM/Picture attribute contains a picture related to the content.
ms.assetid: ec82dfdf-7755-4758-9771-096aac114f78
keywords:
- WM/Picture windows Media Format
topic_type:
- apiref
api_name:
- WM/Picture
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM/Picture

The **WM/Picture** attribute contains a picture related to the content.

## Global Constant

g\_wszWMPicture

## Data Type

[**WM\_PICTURE**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_picture) (**WMT\_TYPE\_BINARY**)

## Remarks

This attribute is compatible with the ID3 frame, APIC. The ID3 specification for the APIC frame stipulates that, while there may be any number of APIC frames associated with a file, only one may be of type 1 and only one may be of type 2. The specification also states that the description of the picture can be no longer than 64 characters, but can be empty.

WM/Picture attributes added with the objects of the Windows Media Format SDK are not automatically validated to conform to ID3 specifications. You must add code in your application to perform validations if you want to maintain complete compatibility with ID3.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> <dt>

[**WM\_PICTURE**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_picture)
</dt> </dl>

 

 




