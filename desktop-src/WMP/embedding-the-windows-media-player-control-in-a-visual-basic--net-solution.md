---
title: Embedding the Windows Media Player Control in a Visual Basic .NET Solution
description: Embedding the Windows Media Player Control in a Visual Basic .NET Solution
ms.assetid: e6428b42-5d8b-48ef-9f7a-c90a4625b745
keywords:
- Windows Media Player,embedding ActiveX control
- Windows Media Player object model,embedding ActiveX control
- object model,embedding ActiveX control
- Windows Media Player Mobile,embedding ActiveX control
- Windows Media Player ActiveX control,embedding
- Windows Media Player Mobile ActiveX control,embedding
- ActiveX control,embedding
- Windows Media Player,Visual Basic .NET
- Windows Media Player object model,Visual Basic .NET
- object model,Visual Basic .NET
- Windows Media Player Mobile,Visual Basic .NET
- Windows Media Player ActiveX control,Visual Basic .NET
- Windows Media Player Mobile ActiveX control,Visual Basic .NET
- ActiveX control,Visual Basic .NET
- embedding,Visual Basic .NET programs
- Visual Basic .NET program embedding
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Embedding the Windows Media Player Control in a Visual Basic .NET Solution

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

To use the functionality of Windows Media Player 9 Series or later in a Visual Basic .NET application, first add the component to a form as described in [Using the Windows Media Player Control with Microsoft Visual Studio](using-the-windows-media-player-control-with-microsoft-visual-studio.md)

This section describes how to create an application that plays video and has custom play and stop buttons.

## Add the Video Window

Add the Windows Media Player control to a form. Resize the control, and then place it where you want the video window to appear.

Select the Windows Media Player control, then change the **uiMode** property to "none". This setting hides the UI controls. When the user plays a video, it will appear in the window. For audio-only content, a visualization will appear.

## Add Two Buttons and Adjust the Form

Now add two buttons to the form. Select the first button and change the **Text** property to "Play". Select the second button and change its **Text** property to "Stop".

## Add the Play Code

Double-click the **Play** button to reveal the Code window. The following code is displayed:


```VB
Private Sub Button1_Click(ByVal sender As System.Object, _
        ByVal e As System.EventArgs) Handles Button1.Click

End Sub
```



Add this line to the subroutine:


```VB
AxWindowsMediaPlayer1.URL = "c:\mediafile.wmv"
```



In the preceding code example, "axWindowsMediaPlayer1" is the default name of the Windows Media Player control and "c:\\mediafile.wmv" is a placeholder for the name of the media you want to play.

If you have added the digital media content from the Windows Media Player SDK to the library in Windows Media Player, you can use this code instead:


```VB
axWindowsMediaPlayer1.currentPlaylist = _
    axWindowsMediaPlayer1.mediaCollection.getByName("mediafile")

```



Because the **autoStart** property is true by default, Windows Media Player will start playing when you set the **currentPlaylist** or **URL** property.

## Add the Stop Code

Double-click the **Stop** button to reveal the Code window. The following code is displayed:


```VB
Private Sub Button2_Click(ByVal sender As System.Object, _
        ByVal e As System.EventArgs) Handles Button1.Click

End Sub

```



Add this line to the subroutine:


```VB
AxWindowsMediaPlayer1.Ctlcontrols.stop()

```



> [!Note]  
> The managed-code wrapper for the Windows Media Player control exposes the **Controls** object as **Ctlcontrols** to avoid collision with the **Controls** property inherited from **System.Windows.Forms.Control**.

 

## Add Error-handling

The Windows Media Player control does not raise an exception when it encounters an error such as an invalid URL. Instead, the control signals an event. Your application should handle error events sent by the Player.

To create an event handler, open the code window for your form class. From the drop-down list at the top of the window, select the Windows Media Player control. A list of events appears in the drop-down list to the right. From that list, select [**MediaError**](axwmplib-axwindowsmediaplayer-mediaerror.md). The following code is displayed:


```VB
Private Sub AxWindowsMediaPlayer1_MediaError(ByVal sender As Object, _
    ByVal e As _WMPOCXEvents_MediaErrorEvent) Handles AxWindowsMediaPlayer1.MediaError

End Sub

```



The following code could be inserted in the subroutine to provide minimal error-handling capability. Note that information about the error can be retrieved from the **\_WMPOCXEvents\_MediaErrorEvent** argument.


```VB
Try
    ' If the file is corrupt or missing, show the 
    ' hexadecimal error code and URL.
    Dim errSource As WMPLib.IWMPMedia2 = e.pMediaObject
    Dim errorItem As WMPLib.IWMPErrorItem = errSource.Error
    MessageBox.Show("Media error " + errorItem.errorCode.ToString("X") _
                    + " in " + errSource.sourceURL)
Catch ex As InvalidCastException
    ' In case pMediaObject is not an IWMPMedia item.
    MessageBox.Show("Player error.")
End Try

```



## Related topics

<dl> <dt>

[**Embedding the Windows Media Player Control in a .NET Framework Solution**](using-the-windows-media-player-control-in-a--net-framework-solution.md)
</dt> </dl>

 

 




