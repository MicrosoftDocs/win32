---
title: WM/WMShadowFileSourceDRMType (Windows Media Player SDK)
description: The WM/WMShadowFileSourceDRMType is the digital rights management system used to protect the file contained in the shadow file.
ms.assetid: f670752d-0490-411e-b4f1-a8c782ad9fcc
keywords:
- WM/WMShadowFileSourceDRMType Windows Media Player
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

# WM/WMShadowFileSourceDRMType (Windows Media Player SDK)

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **WM/WMShadowFileSourceDRMType** is the digital rights management system used to protect the file contained in the shadow file.

## Remarks

A shadow file can be a wrapper for a source file. This attribute is a string that identifies the DRM type for the source file.

The shadow file is specified by using the [ShadowFilePath](shadowfilepath-attribute.md) attribute.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------|
| Version<br/> | Windows Media Player 11<br/> |



## See also

<dl> <dt>

[**About Conversion Plug-ins**](about-conversion-plug-ins.md)
</dt> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





