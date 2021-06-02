---
description: The PlayChapterInTitle method plays the specified chapter in the specified title.
ms.assetid: 784b0612-133b-465c-b1da-d9dac26e1b20
title: PlayChapterInTitle Method
ms.topic: reference
ms.date: 05/31/2018
---

# PlayChapterInTitle Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `PlayChapterInTitle` method plays the specified chapter in the specified title.

``` syntax
MSWebDVD.PlayChapterInTitle(iTitle, iChapter)
```

## Parameters

<dl> <dt>

<span id="iTitle"></span><span id="ititle"></span><span id="ITITLE"></span>*iTitle*
</dt> <dd>

Specifies the title as an Integer value.

</dd> <dt>

<span id="iChapter"></span><span id="ichapter"></span><span id="ICHAPTER"></span>*iChapter*
</dt> <dd>

Specifies the chapter as an Integer value.

</dd> </dl>

## Return Value

No return value.

## Remarks

This method starts playback at the specified chapter and then continues playing indefinitely. If you want to play only a particular chapter, use [**PlayChaptersAutoStop**](playchaptersautostop-method.md).

 

 



