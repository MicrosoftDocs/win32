---
title: Subpicture Streams Controlling Subtitles
description: Subpicture Streams Controlling Subtitles
ms.assetid: c98cfd7a-ef62-4ac2-96bc-82ee8e30dc0d
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Subpicture Streams: Controlling Subtitles

This topic applies to Windows XP Service Pack 1 or later.

Subpictures carry visual elements in the picture, such as subtitles and button highlights. Although subpicture streams frequently carry text, it should not be confused with closed captioning, which is added as a feature (see [Creating the MSVidWebDVD Object](creating-the-msvidwebdvd-object.md) for details). Subpicture stream numbers range from 0 through 31, plus number 63 for a muted low rate bitstream.

Each subpicture stream has an associated language property. This language property is the only information that can be obtained from an arbitrary stream. You can specify subpicture stream language independently of the audio track, so you may have an English soundtrack with French subtitles, for example. Only one subpicture stream at a time can be specified.

Unfortunately, there is no way programmatically to determine the kind of information that a subpicture stream contains, beyond its language. So, for instance, there may be an English stream and a French stream, but the English stream contains audio subtitles while the French stream contains only subtitles for onscreen text.

Here are the basic steps to display a list of subpicture stream languages for user selection:

1.  Determine the number of streams available for a specified title.
2.  Iterate through the streams and retrieve the language for each.
3.  Check to see if the stream is enabled.
4.  Populate a **Select** box or other user interface control with valid streams to enable the user to select the preferred stream.

(Note that audio and subpicture streams are numbered from zero, whereas titles, angles, and parental levels are numbered from one.)

The following code fills a list box (*lboSubpicture*) with the currently available subpicture streams:


```C++
lboSubpicture.Clear
For i = 0 To oVidWebDVD.SubpictureStreamsAvailable - 1
   If oVidWebDVD.IsSubpictureStreamEnabled(i) Then
      lboSubpicture.AddItem oVidWebDVD.SubpictureLanguage(i), i
   End If
Next i
lboSubpicture.Selected(oVidWebDVD.CurrentSubpictureStream) = True
```



The following code changes the subpicture stream when the user clicks the list box:


```C++
Private Sub lboSubpicture_Click()
   oVidWebDVD.CurrentSubpictureStream = lboSubpicture.ListIndex
End Sub
```



The following text toggles the subpicture stream on and off with a checkbox.


```C++
Private Sub chkCC_Click()
   chkSubpicture.SubpictureOn = CBool(chkSubpicture)
End Sub
```



## Related topics

<dl> <dt>

[DVD Applications in Visual Basic (Video Control)](dvd-applications-in-visual-basic--video-control.md)
</dt> </dl>

 

 




