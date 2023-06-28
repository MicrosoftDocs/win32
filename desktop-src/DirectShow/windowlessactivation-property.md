---
description: The WindowlessActivation property initializes the MSWebDVD object at design time for either windowed or windowless mode.
ms.assetid: 290a9459-154a-4ec7-a013-d696e6b27341
title: WindowlessActivation Property
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WindowlessActivation Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `WindowlessActivation` property initializes the **MSWebDVD** object at design time for either windowed or windowless mode.

``` syntax
[ bWindowless = ] MSWebDVD.WindowlessActivation
```

## Return Value

Returns whether the object is in windowed mode as a Boolean.

## Remarks

This property is read/write with a default value of true. Therefore, you only need to set this property if you are running the **MSWebDVD** object in a windowed container. When contained in a Web page in Microsoft® Internet Explorer, **MSWebDVD** is always in windowless mode, and you don't need to set this property.

 

 



