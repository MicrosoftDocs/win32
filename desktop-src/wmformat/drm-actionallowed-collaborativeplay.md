---
title: DRM_ActionAllowed_CollaborativePlay
description: The DRM\_ActionAllowed\_CollaborativePlay attribute indicates whether the license allows the content to be played collaboratively.
ms.assetid: 111e8fa7-ef5a-483a-b930-8a8e5b4d120a
keywords:
- DRM_ActionAllowed_CollaborativePlay windows Media Format
topic_type:
- apiref
api_name:
- DRM_ActionAllowed_CollaborativePlay
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DRM\_ActionAllowed\_CollaborativePlay

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **DRM\_ActionAllowed\_CollaborativePlay** attribute indicates whether the license allows the content to be played collaboratively.

## Global Constant

g\_wszWMDRM\_ActionAllowed\_CollaborativePlay

## Data Type

**WMT\_TYPE\_BOOL**

## Remarks

The collaborative play right applies to playing protected content as part of a collaborative session using peer-to-peer services. For example, users of MSN Messenger 2004 can play protected content in a MusicMix session. This right can only be used to contribute a protected file to a single session at one time, and all users participating in the session must be online to render the content.

This is a read-only property that is retrieved using [**IWMDRMReader::GetDRMProperty**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-getdrmproperty).

## See also

<dl> <dt>

[**DRM Properties**](drm-properties.md)
</dt> </dl>

 

 




