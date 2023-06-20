---
description: Signals that the number of DVD menu buttons has changed, or that the button selection has changed.
ms.assetid: af6c841d-ca06-4535-b418-14409fa78c81
title: EC_DVD_BUTTON_CHANGE (Dvdevcode.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EC_DVD_BUTTON_CHANGE
api_type: 
- HeaderDef
api_location: 
- dvdevcode.h
ms.custom: UpdateFrequency5
---

# EC\_DVD\_BUTTON\_CHANGE

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Signals that the number of DVD menu buttons has changed, or that the button selection has changed.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

**DWORD** value indicating the number of available buttons.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

**DWORD** value indicating the currently selected button number. Selected button number zero implies that no button is selected.

</dd> </dl>

## Remarks

Button numbers range from 1 to 36.

The currently selected button can change automatically with a navigation command authored on the disc as well as through application control by using [**IDvdControl2**](/windows/desktop/api/Strmif/nn-strmif-idvdcontrol2) interface.

This event can signal any of the available button numbers. These numbers do not always correspond to button numbers used for [**IDvdControl2::SelectAndActivateButton**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-selectandactivatebutton) because that method can activate only a subset of buttons.

This event is raised in all domains.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dvdevcode.h (include Dshow.h)</dt> </dl> |



## See also

<dl> <dt>

[DVD Applications](dvd-applications.md)
</dt> <dt>

[DVD Event Notification Codes](dvd-notification-codes.md)
</dt> <dt>

[Event Notification in DirectShow](event-notification-in-directshow.md)
</dt> </dl>

 

 




