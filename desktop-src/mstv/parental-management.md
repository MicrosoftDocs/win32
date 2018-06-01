---
title: Parental Management
description: Parental Management
ms.assetid: b3bf0a8d-4399-45db-b48f-41d9865fccd9
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Parental Management

This topic applies to Windows XP Service Pack 1 or later.

Any title or portion of a title on a disc allows eight parental management levels (PMLs), one through eight, with eight being the most restrictive. The idea is to provide a way of preventing children from viewing certain content without adult consent. However, there is no requirement that these levels be accurately set, nor is there any direct correlation between these values and the Motion Picture Association of America (MPAA) film ratings, and you cannot rely on DVDs to have parental levels set predictably or accurately.

Disc parental permissions may also be set dynamically, in which case the application must have enabled notification of parental level change using [**NotifyParentalLevelChange**](https://www.bing.com/search?q=**NotifyParentalLevelChange**). Enable notification immediately upon running the movie, as parental levels are sometimes changed during the FBI warning section of the disc.

DVD authors have two ways to set the parental levels on a disc. One is through the video title set information. This automatically stops playback without allowing the user to override the settings if a more restrictive parental level is encountered.

The second method sends parental level change notifications to the application, which must then decide what to do. The DVD Navigator filter sends an **EC\_DVD\_PARENTAL\_LEVEL\_CHANGE** message when it encounters PMLs on the disc. By default, it does nothing else. However, if [**NotifyParentalLevelChange**](https://www.bing.com/search?q=**NotifyParentalLevelChange**) has been set to **True**, playback will be halted until [**AcceptParentalLevelChange**](https://www.bing.com/search?q=**AcceptParentalLevelChange**) is called to accept or reject the new level. For more information on handling disc events, see [MSVidWebDVD Events](https://www.bing.com/search?q=MSVidWebDVD Events).

Parental level is returned by the player as a two-byte value consisting of a series of bit flags indicating whether or not a DVD is playable by a particular parental level. The low byte of the return value is ignored, so the value 1111111100000000 would become 11111111. As an example, a return value of 11100000 (after the low byte has been removed) indicates a disc is playable by a parental level 6 and above. It is possible for all bits to be set to zero, in which case parental levels must be disabled using [**SelectParentalLevel**](https://www.bing.com/search?q=**SelectParentalLevel**) to watch the movie.

The following code illustrates a message box popup that handles a temporary parental management level message. It is part of the **Select Case** block that handles [**DVDNotify**](https://www.bing.com/search?q=**DVDNotify**) event messages, and assumes [**NotifyParentalLevelChange**](https://www.bing.com/search?q=**NotifyParentalLevelChange**) has been set to **True**.


```C++
Private Sub ovidwebdvd_DVDNotify(ByVal lEventCode As Long, _
                ByVal lParam1 As Variant, ByVal lParam2 As Variant)
   Select Case lEventCode
      If Not (2 ^ (oVidWebDVD.PlayerParentalLevel + 7) And lParam1) Then
         Dim strPassword As String
         strPassword = InputBox("The disc has encountered restricted_
             material. Please enter your password", "Restricted title")
         oVidWebDVD.AcceptParentalLevelChange True, "", strPassword
      End If
   End Select
End Sub
```



## Related topics

<dl> <dt>

[DVD Applications in Visual Basic (Video Control)](dvd-applications-in-visual-basic--video-control.md)
</dt> </dl>

 

 




