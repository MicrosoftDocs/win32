---
title: Can_Skip_Backward
description: The Can\_Skip\_Backward attribute is a file-level attribute indicating whether you can skip to the previous item in the server-side playlist.
ms.assetid: 91a8cfee-ccb6-4e0e-90f0-2e134fee56d1
keywords:
- Can_Skip_Backward windows Media Format
topic_type:
- apiref
api_name:
- Can_Skip_Backward
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Can\_Skip\_Backward

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **Can\_Skip\_Backward** attribute is a file-level attribute indicating whether you can skip to the previous item in the server-side playlist.

## Global Constant

g\_wszWMSkipBackward

## Data Type

**WMT\_TYPE\_BOOL**

## Remarks

This is a coded attribute.

This attribute cannot be duplicated at the file level. If this attribute is used for an individual stream, it will be treated as custom metadata and will not convey its normal meaning to the objects of the Windows Media Format SDK.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




