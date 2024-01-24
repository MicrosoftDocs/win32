---
description: Choosing a Video Codec
ms.assetid: 3a4b925a-4fb4-4189-a571-8083454fed0e
title: Choosing a Video Codec (Microsoft Media Foundation)
ms.topic: article
ms.date: 05/31/2018
---

# Choosing a Video Codec (Microsoft Media Foundation)

The Windows Media Video 9 Encoder supports three categories of encoded output: Main Profile, Advanced Profile, and Image. The Main Profile category provides general video compression for complex video content, such as movies or music videos. The features of the Main Profile provide for a wide range of encoding settings. You can use the Main Profile to create video with very low bit rates for delivery on handheld devices or, at the other end of the spectrum, you can use it to create high-definition video for digital cinema.

The emphasis of the encoding algorithms in the Main Profile is on dynamic video content, but they are suitable for other video content as well. The Main Profile should be your default category for video content. To meet specific needs, you can use the Advanced Profile category, the Image category, or a separate encoder called the Windows Media Video 9 Screen encoder. The following table lists the four options.



<table>
<thead>
<tr class="header">
<th>Purpose</th>
<th>Codec</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>General-purpose video encoding</td>
<td><a href="windowsmediavideo9encoder.md">Windows Media Video 9 Encoder</a><dl> Main Profile<br />
</dl></td>
</tr>
<tr class="even">
<td>Encoding high definition video or video that conforms to the VC-1 Advanced Profile SMPTE standard</td>
<td><a href="windowsmediavideo9encoder.md">Windows Media Video 9 Encoder</a><dl> Advanced Profile<br />
</dl></td>
</tr>
<tr class="odd">
<td>Converting bitmapped images to dynamic video</td>
<td><a href="windowsmediavideo9encoder.md">Windows Media Video 9 Encoder</a><dl> Image<br />
</dl></td>
</tr>
<tr class="even">
<td>Encoding computer-application video (screen capture) or other highly static video</td>
<td><a href="windowsmediavideo9screenencoder.md"><strong>Windows Media Video 9 Screen Encoder</strong></a></td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[Working with Video](workingwithvideo.md)
</dt> </dl>

 

 



