---
description: The PlayChapter method starts playback from the specified chapter within the current title.
ms.assetid: d0318a0d-4ff4-42f2-b009-996b7ff0f632
title: PlayChapter Method
ms.topic: reference
ms.date: 05/31/2018
---

# PlayChapter Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `PlayChapter` method starts playback from the specified chapter within the current title.

``` syntax
MSWebDVD.PlayChapter(iChapter)
```

## Parameters

<dl> <dt>

<span id="iChapter"></span><span id="ichapter"></span><span id="ICHAPTER"></span>*iChapter*
</dt> <dd>

Specifies the chapter index in the current title as an Integer.

</dd> </dl>

## Return Value

No return value.

## Remarks

When the end of the specified chapter is reached, this method continues playing subsequent chapters, if any exist. If you want to play only a specified chapter, use [**PlayChaptersAutoStop**](playchaptersautostop-method.md).

## See also

<dl> <dt>

[**PlayChapterInTitle**](playchapterintitle-method.md)
</dt> </dl>

 

 



