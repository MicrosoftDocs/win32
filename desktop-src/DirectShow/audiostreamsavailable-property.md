---
description: The AudioStreamsAvailable property retrieves the number of audio streams available in the current title.
ms.assetid: 4359ec30-920a-4b34-8e27-4cf1d9452aa8
title: AudioStreamsAvailable Property
ms.topic: reference
ms.date: 05/31/2018
---

# AudioStreamsAvailable Property

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `AudioStreamsAvailable` property retrieves the number of audio streams available in the current title.

``` syntax
[ iStreams = ] MSWebDVD.AudioStreamsAvailable
```

## Return Value

Returns an integer value from 1 through 8 representing the number of audio streams available in the current title.

## Remarks

This property is read-only with no default value. The primary use of multiple audio streams is to provide movie soundtracks in more than one language. Typically, not every title on a disc has all audio streams enabled. For example, the feature movie might have soundtracks in three different languages, but the trailers might have only an English soundtrack. Before a user can select a stream, the application must determine which streams are available within the current title. Note that particular streams are identified by an index from zero through 7.

Discs generally present a menu showing the available soundtracks, enabling the user to select the audio stream to enable.

## See also

<dl> <dt>

[**GetAudioLanguage**](getaudiolanguage-method.md)
</dt> </dl>

 

 



