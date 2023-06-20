---
description: The ReadyStateChange event is sent when the ReadyState property of the MSWebDVD control has changed.
ms.assetid: 814a09e1-2e85-4ea3-9135-8377dc2acf64
title: ReadyStateChange
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# ReadyStateChange

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `ReadyStateChange` event is sent when the **ReadyState** property of the MSWebDVD control has changed.

``` syntax
ReadyStateChange(ReadyState)
```

## Parameters

<dl> <dt>

<span id="ReadyState"></span><span id="readystate"></span><span id="READYSTATE"></span>*ReadyState*
</dt> <dd>

Specifies the new value of the [**ReadyState**](readystate-property.md) property.



| Value | Description               |
|-------|---------------------------|
| 0     | READYSTATE\_UNINITIALIZED |
| 1     | READYSTATE\_LOADING       |
| 2     | READYSTATE\_LOADED        |
| 3     | READYSTATE\_INTERACTIVE   |
| 4     | READYSTATE\_COMPLETE      |



 

</dd> </dl>

 

 



