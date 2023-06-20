---
title: WM/ContainerFormat
description: The WM/ContainerFormat attribute specifies the type of file that is loaded in the calling object.
ms.assetid: fea5b2e4-f10d-4482-a7b3-7dabf58df085
keywords:
- WM/ContainerFormat windows Media Format
topic_type:
- apiref
api_name:
- WM/ContainerFormat
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WM/ContainerFormat

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **WM/ContainerFormat** attribute specifies the type of file that is loaded in the calling object.

## Global Constant

g\_wszWMContainerFormat

## Data Type

[**WMT\_STORAGE\_FORMAT**](/previous-versions/windows/desktop/api/wmsdkidl/ne-wmsdkidl-wmt_storage_format) (**WMT\_TYPE\_BINARY**)

## Remarks

This attribute is used in place of **IWMProfile3::GetStorageFormat** and **IWMProfile3::SetStorageFormat**, which are no longer supported.

This is a coded attribute.

This attribute cannot be duplicated at the file level. If this attribute is used for an individual stream, it will be treated as custom metadata and will not convey its normal meaning to the objects of the Windows Media Format SDK.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




