---
description: The PlayChaptersAutoStop method starts playback at the specified chapter in the specified title and for the number of chapters specified.
ms.assetid: ede19f02-6eda-42da-a108-06d78dc2e8a9
title: PlayChaptersAutoStop Method
ms.topic: reference
ms.date: 05/31/2018
---

# PlayChaptersAutoStop Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `PlayChaptersAutoStop` method starts playback at the specified chapter in the specified title and for the number of chapters specified.

``` syntax
MSWebDVD.PlayChaptersAutoStop(iTitle, iChapter, iChapterCount)
```

## Parameters

<dl> <dt>

<span id="iTitle"></span><span id="ititle"></span><span id="ITITLE"></span>*iTitle*
</dt> <dd>

Specifies the title as an Integer value.

</dd> <dt>

<span id="iChapter"></span><span id="ichapter"></span><span id="ICHAPTER"></span>*iChapter*
</dt> <dd>

Specifies the start chapter as an Integer value.

</dd> <dt>

<span id="iChapterCount"></span><span id="ichaptercount"></span><span id="ICHAPTERCOUNT"></span>*iChapterCount*
</dt> <dd>

Specifies the number of chapters to play as an Integer value.

</dd> </dl>

## Return Value

No return value.

## Remarks

When the last chapter has played, this method causes an [**EC\_DVD\_CHAPTER\_AUTOSTOP**](ec-dvd-chapter-autostop.md) event notification to be sent to the application.

 

 



