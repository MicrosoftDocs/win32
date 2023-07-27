---
description: Sent by the WM ASF Reader filter when it reads ASF files protected by digital rights management (DRM).
ms.assetid: ac6ea7a1-238e-42ae-9f10-e1db60381357
title: EC_WMT_EVENT (Dshow.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# EC_WMT_EVENT (Dshow.h)

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Sent by the [WM ASF Reader](wm-asf-reader-filter.md) filter when it reads ASF files protected by digital rights management (DRM).

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

One of the following **WMT\_STATUS** values:



| Value                         | Description                                                                                                       |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------|
| WMT\_ACQUIRE\_LICENSE         | Sent when the DRM component has completed the license acquisition process, either successfully or unsuccessfully. |
| WMT\_INDIVIDUALIZE            | The security upgrade process has completed, either successfully or unsuccessfully.                                |
| WMT\_NEEDS\_INDIVIDUALIZATION | The file requires that an application receive a security upgrade before performing the requested action.          |
| WMT\_NO\_RIGHTS               | The application has no rights to perform he requested action on a file protected by DRM version 1.                |
| WMT\_NO\_RIGHTS\_EX           | The application has no rights to perform he requested action on a file protected by DRM version 7.                |



 

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

Pointer to an [**AM\_WMT\_EVENT\_DATA**](/previous-versions/windows/desktop/api/evcode/ns-evcode-am_wmt_event_data) structure that contains information about the event, or **NULL**. The **pData** member of this structure points to additional data, whose type depends on the value of **lParam1**, as shown in the following table.



| lParam1                       | AM\_WMT\_EVENT\_DATA.pData                                                                                                                       |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| WMT\_ACQUIRE\_LICENSE         | Pointer to a [**WM\_GET\_LICENSE\_DATA**](/windows/desktop/wmformat/wm-get-license-data) structure. This structure is documented in the Windows Media Format SDK. |
| WMT\_INDIVIDUALIZE            | Pointer to a [**WM\_INDIVIDUALIZE\_STATUS**](/windows/desktop/wmformat/wm-individualize-status) structure.                                                        |
| WMT\_NEEDS\_INDIVIDUALIZATION | **NULL**.                                                                                                                                        |
| WMT\_NO\_RIGHTS               | Pointer to a wide-character string containing a challenge URL.                                                                                   |
| WMT\_NO\_RIGHTS\_EX           | Pointer to a [**WM\_GET\_LICENSE\_DATA**](/windows/desktop/wmformat/wm-get-license-data) structure.                                                               |



 

The value of *lParam2* might be **NULL**. Check the value before dereferencing the pointer.

</dd> </dl>

## Remarks

See the Windows Media Format SDK documentation for more information on enabling playback of DRM-protected files.

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dshow.h</dt> </dl> |



## See also

<dl> <dt>

[Event Notification Codes](event-notification-codes.md)
</dt> <dt>

[Event Notification in DirectShow](event-notification-in-directshow.md)
</dt> </dl>

 

