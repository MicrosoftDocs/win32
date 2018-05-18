---
title: WM/ContainerFormat
description: The WM/ContainerFormat attribute specifies the type of file that is loaded in the calling object.
ms.assetid: 'fea5b2e4-f10d-4482-a7b3-7dabf58df085'
keywords: ["WM/ContainerFormat windows Media Format"]
topic_type:
- apiref
api_name:
- WM/ContainerFormat
api_type:
- NA
---

# WM/ContainerFormat

The **WM/ContainerFormat** attribute specifies the type of file that is loaded in the calling object.

## Global Constant

g\_wszWMContainerFormat

## Data Type

[**WMT\_STORAGE\_FORMAT**](wmt-storage-format.md) (**WMT\_TYPE\_BINARY**)

## Remarks

This attribute is used in place of **IWMProfile3::GetStorageFormat** and **IWMProfile3::SetStorageFormat**, which are no longer supported.

This is a coded attribute.

This attribute cannot be duplicated at the file level. If this attribute is used for an individual stream, it will be treated as custom metadata and will not convey its normal meaning to the objects of the Windows Media Format SDK.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




