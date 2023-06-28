---
description: The PlayState property retrieves the current state of the MSWebDVD object.
ms.assetid: ffe71c3f-f8c2-45cc-84bf-e937cfbbe7b9
title: PlayState Property
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PlayState Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `PlayState` property retrieves the current state of the **MSWebDVD** object.

``` syntax
[ iState = ] MSWebDVD.PlayState
```

## Return Value

Returns an Integer value representing the current state of the DVD Navigator.



| Return code | Description   |
|-------------|---------------|
| -2          | Undefined     |
| -1          | Uninitialized |
| 0           | Stopped       |
| 1           | Paused        |
| 2           | Running       |



 

## Remarks

This property is read-only with no default value.

The **MSWebDVD** object controls the DirectShow DVD Navigator filter, which does the actual work of DVD navigation. It is actually the state of the DVD Navigator that this property refers to. The DVD Navigator can be in one of several states, as described above. The `PlayState` property can be useful as a diagnostic tool, but generally there should be no reason for a scripting application to monitor the state of the DVD Navigator.

 

 



