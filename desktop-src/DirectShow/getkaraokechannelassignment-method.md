---
description: The GetKaraokeChannelAssignment method retrieves a value that indicates how the karaoke channels are assigned to the speakers.
ms.assetid: 08e35fa6-fa1b-4f9f-8f56-d953c4422226
title: GetKaraokeChannelAssignment Method
ms.topic: reference
ms.date: 05/31/2018
---

# GetKaraokeChannelAssignment Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `GetKaraokeChannelAssignment` method retrieves a value that indicates how the karaoke channels are assigned to the speakers.

``` syntax
[ iAssignment = ] MSWebDVD.GetKaraokeChannelAssignment(iStream)
```

## Parameters

<dl> <dt>

<span id="iStream"></span><span id="istream"></span><span id="ISTREAM"></span>*iStream*
</dt> <dd>

Specifies the audio stream as an Integer.

</dd> </dl>

## Return Value

Returns an integer indicating the speaker assignment for the specified stream.



| Return code | Description                                                             |
|-------------|-------------------------------------------------------------------------|
| 2           | The stream is assigned to the left and right speakers.                  |
| 3           | The stream is assigned to the left, right, and middle speakers.         |
| 4           | The stream is assigned to the left, right, and audio1 speakers.         |
| 5           | The stream is assigned to the left, right, middle, and audio1 speakers. |
| 6           | The stream is assigned to the left, right, and audio2 speakers.         |
| 7           | The stream is assigned to the left, right, middle, and audio2 speakers. |



 

## See also

<dl> <dt>

[**KaraokeAudioPresentationMode**](karaokeaudiopresentationmode-property.md)
</dt> </dl>

 

 



