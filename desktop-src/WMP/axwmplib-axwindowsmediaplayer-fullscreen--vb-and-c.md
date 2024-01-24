---
title: AxWindowsMediaPlayer.fullScreen property
description: The fullScreen property gets or sets a value indicating whether video content is played in full-screen mode.
ms.assetid: 6c48a54a-e0f1-4bf5-8a53-7ccc78fc76ad
keywords:
- fullScreen property Windows Media Player
- fullScreen property Windows Media Player , AxWindowsMediaPlayer class
- AxWindowsMediaPlayer class Windows Media Player , fullScreen property
topic_type:
- apiref
api_name:
- AxWindowsMediaPlayer.fullScreen
api_location:
- AxInterop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AxWindowsMediaPlayer.fullScreen property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The fullScreen property gets or sets a value indicating whether video content is played in full-screen mode.

## Syntax


```CSharp
public System.Boolean fullScreen {get; set;}
```


```VB

Public Property fullScreen As System.Boolean
```





## Property value

A System.Boolean value that indicates whether content is played in full-screen mode. The default value is false.

## Remarks

For full-screen mode to work properly when embedding the Windows Media Player control, the video display area must have a height and width of at least one pixel. If **uiMode** is set to "mini" or "full", the height of the control itself must be 65 or greater to accommodate the video display area in addition to the user interface.

If **uiMode** is set to "invisible", then setting this property to true raises an error and does not affect the behavior of the control.

During full-screen playback, Windows Media Player hides the mouse cursor when [enableContextMenu](axwmplib-axwindowsmediaplayer-enablecontextmenu--vb-and-c.md) equals false and **uiMode** equals "none".

If **uiMode** is set to "full" or "mini", Windows Media Player displays transport controls in full-screen mode when the mouse cursor moves. After a brief interval of no mouse movement, the transport controls are hidden. If **uiMode** is set to "none", no controls are displayed in full-screen mode.

> [!Note]  
> Displaying transport controls in full-screen mode requires the Windows XP operating system.

 

If transport controls are not displayed in full-screen mode, then Windows Media Player automatically exits full-screen mode when playback stops.

## Examples

The following example creates a button that uses the fullScreen property to switch an embedded player object to full-screen mode. The AxWMPLib.AxWindowsMediaPlayer object is represented by the variable named player.


```CSharp
private void fullScreen_Click(object sender, System.EventArgs e)
{
    // If the player is playing, switch to full screen. 
    if (player.playState == WMPLib.WMPPlayState.wmppsPlaying)
    {
        player.fullScreen = true;
    }
}
```


```VB

Public Sub fullScreen_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles fullScreen.Click

    &#39; If the player is playing, switch to full screen. 
    If (player.playState = WMPLib.WMPPlayState.wmppsPlaying) Then

        player.fullScreen = True

    End If

End Sub
```





## Requirements



| Requirement | Value |
|----------------------|--------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                  |
| Namespace<br/> | **AxWMPLib**<br/>                                                                                            |
| Assembly<br/>  | <dl> <dt>AxInterop.WMPLib (AxInterop.WMPLib.dll)</dt> </dl> |



## See also

<dl> <dt>

[**AxWindowsMediaPlayer Object (VB and C#)**](axwindowsmediaplayer-object--vb-and-c.md)
</dt> <dt>

[**AxWindowsMediaPlayer.uiMode (VB and C#)**](axwmplib-axwindowsmediaplayer-uimode--vb-and-c.md)
</dt> </dl>

 

 





