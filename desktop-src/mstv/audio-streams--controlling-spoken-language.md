---
title: Audio Streams Controlling Spoken Language
description: Audio Streams Controlling Spoken Language
ms.assetid: c440ab74-51f4-46c4-9970-0908b8411452
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Audio Streams: Controlling Spoken Language

This topic applies to Windows XP Service Pack 1 or later.

A DVD-Video disc can have up to eight audio streams, numbered zero through seven, each with up to six discrete channels. Audio streams specify a standard movie soundtrack, a director's comments soundtrack, alternate language soundtracks, or other audio features. Only one audio stream at a time can be enabled. Discs are generally authored with default audio streams, but an application can enable the user to see all the streams that are available for a given title, and select the one in the language they prefer.

Unfortunately, there is no way to determine the content of an audio stream programmatically; an audio stream may contain a simple soundtrack, director's comments, or other audio. So, for instance, there may be three audio streams listed as English language, but one may be director's comments, another may be a simple soundtrack in English, and the third may be a multi-speaker soundtrack.

Here are the basic steps to display a list of audio streams for user selection:

1.  Determine the number of streams available for a specified title.
2.  Iterate through the streams and retrieve the stream attributes for each.
3.  Check to see if the stream is enabled.
4.  Populate a **Select** box or other user interface control with valid streams to enable the user to select the preferred stream.

(Note that audio and subpicture streams are numbered from zero, whereas titles, angles, and parental levels are numbered from one.)

The following code fills a list box (*lboAudioStream*) with a list of available languages:


```C++
lboAudioStream.Clear
For i = 0 To oVidWebDVD.AudioStreamsAvailable - 1
   If oVidWebDVD.IsAudioStreamEnabled(i) Then
      lboAudioStream.AddItem oVidWebDVD.AudioLanguage(i), i
   End If
Next i
lboAudioStream.Selected(oVidWebDVD.CurrentAudioStream) = True
```



The following code changes the audio stream when the user clicks on the list box:


```C++
Private Sub lboAudioStream_Click()
   oVidWebDVD.CurrentAudioStream = lboAudioStream.ListIndex
End Sub
```



## Related topics

<dl> <dt>

[DVD Applications in Visual Basic (Video Control)](dvd-applications-in-visual-basic--video-control.md)
</dt> </dl>

 

 




