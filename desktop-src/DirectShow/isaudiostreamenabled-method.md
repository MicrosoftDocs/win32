---
description: The IsAudioStreamEnabled method retrieves a value indicating whether the specified audio stream is enabled in the current title.
ms.assetid: df6c69a7-6eb0-4662-a3aa-f3f895b42cbc
title: IsAudioStreamEnabled Method
ms.topic: reference
ms.date: 05/31/2018
---

# IsAudioStreamEnabled Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `IsAudioStreamEnabled` method retrieves a value indicating whether the specified audio stream is enabled in the current title.

``` syntax
[bEnabled = ] MSWebDVD.IsAudioStreamEnabled(iStream)
```

## Parameters

<dl> <dt>

<span id="iStream"></span><span id="istream"></span><span id="ISTREAM"></span>*iStream*
</dt> <dd>

Specifies the audio stream as an Integer value from 0 through 7.

</dd> </dl>

## Return Value

Returns a Boolean value indicating whether the specified audio stream is available for the current title. True means it is available.

## Remarks

Although a disc can contain up to eight independent audio streams, each stream is not necessarily available for each title. For example, a main movie title might have three audio streams for English, Spanish, and Japanese, but the "Coming Attractions" title might have only one audio stream in English. Always verify that a stream is available for a title before setting the [**CurrentAudioStream**](currentaudiostream-property.md) property.

 

 



