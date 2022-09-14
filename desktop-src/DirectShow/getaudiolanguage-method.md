---
description: The GetAudioLanguage method retrieves a string indicating which language is available on the specified audio stream.
ms.assetid: 5ff12058-eb00-4a2c-8d39-88282f68f001
title: GetAudioLanguage Method
ms.topic: reference
ms.date: 05/31/2018
---

# GetAudioLanguage Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `GetAudioLanguage` method retrieves a string indicating which language is available on the specified audio stream.

``` syntax
[ slang = ] MSWebDVD.GetAudioLanguage(iStream)
```

## Parameters

<dl> <dt>

<span id="iStream"></span><span id="istream"></span><span id="ISTREAM"></span>*iStream*
</dt> <dd>

Specifies the audio stream number in the current title as an Integer.

</dd> </dl>

## Return Value

Returns a human-readable string identifying the language of the audio stream in the current title.

 

 



