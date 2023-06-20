---
title: WM/WMShadowFileSourceDRMType (Windows Media Format 11 SDK)
description: The WM/WMShadowFileSourceDRMType attribute contains the type of rights management that is used to protect the original file that the ASF file is derived from.
ms.assetid: 58e7a383-6e80-42fc-bc75-5920dbe67a40
keywords:
- WM/WMShadowFileSourceDRMType windows Media Format
topic_type:
- apiref
api_name:
- WM/WMShadowFileSourceDRMType
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WM/WMShadowFileSourceDRMType (Windows Media Format 11 SDK)

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **WM/WMShadowFileSourceDRMType** attribute contains the type of rights management that is used to protect the original file that the ASF file is derived from.

## Global Constant

g\_wszWMWMShadowFileSourceDRMType

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

Content that exists in a file format other than ASF and is protected with some sort of rights management can be converted to a Windows Media file protected by Windows Media DRM through a process called license importing. Such an ASF file should contain this attribute as well as WM/WMShadowFileSourceFileType to track where the content came from.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




