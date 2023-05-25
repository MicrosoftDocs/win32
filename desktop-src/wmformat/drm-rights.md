---
title: DRM_Rights
description: The DRM\_Rights property specifies the rights that the application will require in the next attempt to open a protected file.
ms.assetid: fbf62e8d-069e-427b-9093-6c579cdaa96a
keywords:
- DRM_Rights windows Media Format
topic_type:
- apiref
api_name:
- DRM_Rights
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DRM\_Rights

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **DRM\_Rights** property specifies the rights that the application will require in the next attempt to open a protected file.

## Global Constant

g\_wszWMDRM\_Rights

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

This is a read-write property that is retrieved using [**IWMDRMReader::GetDRMProperty**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-getdrmproperty) and set using either [**IWMDRMReader::SetDRMProperty**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-setdrmproperty) or [**IWMDRMWriter::SetDRMAttribute**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmwriter-setdrmattribute).

The following table lists the supported rights.



| Right                                           | String literal      | Description                                                                                                                                                                                                          |
|-------------------------------------------------|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| g\_wszWMDRM\_RIGHT\_BACKUP                      | "Backup"            | Right to back up the license.                                                                                                                                                                                        |
| g\_wszWMDRM\_RIGHT\_COLLABORATIVE\_PLAY         | "CollaborativePlay" | Right to play the file as part of a collaborative playlist.                                                                                                                                                          |
| g\_wszWMDRM\_RIGHT\_COPY                        | "Copy"              | Right to copy the file to a device. This right supersedes the older copy rights (g\_wszWMDRM\_RIGHT\_COPY\_TO\_CD, g\_wszWMDRM\_RIGHT\_COPY\_TO\_NON\_SDMI\_DEVICE, and g\_wszWMDRM\_RIGHT\_COPY\_TO\_SDMI\_DEVICE). |
| g\_wszWMDRM\_RIGHT\_COPY\_TO\_CD                | "Print.redbook"     | Right to copy the file to a CD (Red Book format).In Windows Media DRM 10, this right is replaced by g\_wszWMDRM\_RIGHT\_COPY.<br/>                                                                             |
| g\_wszWMDRM\_RIGHT\_COPY\_TO\_NON\_SDMI\_DEVICE | "Transfer.NONSDMI"  | Right to copy the file to a non-SDMI device.In Windows Media DRM 10, this right is replaced by g\_wszWMDRM\_RIGHT\_COPY.<br/>                                                                                  |
| g\_wszWMDRM\_RIGHT\_COPY\_TO\_SDMI\_DEVICE      | "Transfer.SDMI"     | Right to copy the file to an SDMI-compliant device.In Windows Media DRM 10, this right is replaced by g\_wszWMDRM\_RIGHT\_COPY.<br/>                                                                           |
| g\_wszWMDRM\_RIGHT\_PLAYBACK                    | "Play"              | Right to play the media file.                                                                                                                                                                                        |



 

This property contains a wide-character string of one or more rights separated by semicolons, for example: L"Playback;Copy;CollaborativePlay".

## See also

<dl> <dt>

[**DRM Properties**](drm-properties.md)
</dt> </dl>

 

 





