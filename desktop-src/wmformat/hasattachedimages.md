---
title: HasAttachedImages
description: The HasAttachedImages attribute is a file-level attribute specifying whether the file is an MP3 file with attached APIC ID3 frames.
ms.assetid: 5c45f61c-3149-4b1b-b5de-f5817cc48c02
keywords:
- HasAttachedImages windows Media Format
topic_type:
- apiref
api_name:
- HasAttachedImages
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HasAttachedImages

The **HasAttachedImages** attribute is a file-level attribute specifying whether the file is an MP3 file with attached APIC ID3 frames.

## Global Constant

g\_wszWMHasAttachedImages

## Data Type

**WMT\_TYPE\_BOOL**

## Remarks

This is a coded attribute.

This attribute cannot be duplicated at the file level. If this attribute is used for an individual stream, it will be treated as custom metadata and will not convey its normal meaning to the objects of the Windows Media Format SDK.

**HasAttachedImages** was designed to inform an application that images were present so that they could be retrieved using the [**IWMImageInfo**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmimageinfo?branch=master) interface. Now that images are supported using the [**WM/Picture**](wmpicture.md) attribute, **HasAttachedImages** is no longer needed.

To determine whether a file contains images, call [**IWMHeaderInfo3::GetAttributeIndices**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo3-getattributeindices?branch=master) specifying the **WM/Picture** attribute.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




