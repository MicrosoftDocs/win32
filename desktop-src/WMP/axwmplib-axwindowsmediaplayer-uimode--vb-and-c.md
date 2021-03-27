---
title: AxWindowsMediaPlayer.uiMode property
description: The uiMode property gets or sets a value indicating which controls are shown in the user interface.
ms.assetid: 01034418-be70-44f3-8812-e529c747c9e4
keywords:
- uiMode property Windows Media Player
- uiMode property Windows Media Player , AxWindowsMediaPlayer class
- AxWindowsMediaPlayer class Windows Media Player , uiMode property
topic_type:
- apiref
api_name:
- AxWindowsMediaPlayer.uiMode
api_location:
- AxInterop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# AxWindowsMediaPlayer.uiMode property

The uiMode property gets or sets a value indicating which controls are shown in the user interface.

## Syntax


```CSharp
public System.String uiMode {get; set;}
```


```VB

Public Property uiMode As System.String
```





## Property value

A System.String that is one of the following values.



| Value     | Description                                                                                                                                                                                                     | Audio example                                                   | Video example                                                   |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|-----------------------------------------------------------------|
| invisible | Windows Media Player is embedded without any visible user interface (controls, video or visualization window).                                                                                                  | (Nothing is displayed.)                                         | (Nothing is displayed.)                                         |
| none      | Windows Media Player is embedded without controls, and with only the video or visualization window displayed.                                                                                                   | ![uimode = 'none' with audio](images/uimode-none-audio-v11.png) | ![uimode = 'none' with video](images/uimode-none-video-v11.png) |
| mini      | Windows Media Player is embedded with the status window, play/pause, stop, mute, and volume controls shown in addition to the video or visualization window.                                                    | ![uimode = 'mini' with audio](images/uimode-mini-audio-v11.png) | ![uimode = 'mini' with video](images/uimode-mini-video-v11.png) |
| full      | Default. Windows Media Player is embedded with the status window, seek bar, play/pause, stop, mute, next, previous, fast forward, rewind, and volume controls in addition to the video or visualization window. | ![uimode = 'full' with audio](images/uimode-full-audio-v11.png) | ![uimode = 'full' with video](images/uimode-full-video-v11.png) |
| custom    | Windows Media Player is embedded with a custom user interface. Can only be used in C++ programs.                                                                                                                | (Custom user interface is displayed.)                           | (Custom user interface is displayed.)                           |



 

## Remarks

This property specifies the appearance of the embedded Windows Media Player. When **uiMode** is set to "none", "mini", or "full", a window is present for the display of video clips and audio visualizations. This window can be hidden in mini or full mode by setting the **height** attribute of the **OBJECT** tag to 40, which is measured from the bottom, and leaves the controls portion of the user interface visible. If no embedded interface is desired, set both the **width** and **height** attributes to zero.

If **uiMode** is set to "invisible", no user interface is displayed, but space is still reserved on the page as specified by **width** and **height**. This is useful for retaining page layout when **uiMode** can change. Additionally, the reserved space is transparent, so any elements layered behind the control will be visible.

If **uiMode** is set to "full" or "mini", Windows Media Player displays transport controls in full-screen mode. If **uiMode** is set to "none", no controls are displayed in full-screen mode.

If the window is visible and audio content is being played, the visualization displayed will be the one most recently used in Windows Media Player.

If **uiMode** is set to "custom" in a C++ program that implements **IWMPRemoteMediaServices**, the skin file indicated by **IWMPRemoteMediaServices.GetCustomUIMode** is displayed.

During full-screen playback, Windows Media Player hides the mouse cursor when **enableContextMenu** equals false and **uiMode** equals "none".

## Examples

The following example creates a list box that allows the user to change the user interface mode for an embedded Windows Media Player object. The AxWMPLib.AxWindowsMediaPlayer object is represented by the variable named player.


```CSharp
// Load the list box with the four UI mode options.
uiModeOptions.Items.Add("invisible");
uiModeOptions.Items.Add("none");
uiModeOptions.Items.Add("mini");
uiModeOptions.Items.Add("full");


private void uiModeOptions_OnSelectedIndexChanged(object sender, System.EventArgs e)
{
    // Get the selected UI mode in the list box as a string.
    string newMode = (string)(((System.Windows.Forms.ListBox)sender).SelectedItem);
     
    // Set the UI mode that the user selected.
    player.uiMode = newMode;            
}
```


```VB

' Load the list box with the four UI mode options.
uiModeOptions.Items.Add(&quot;invisible&quot;)
uiModeOptions.Items.Add(&quot;none&quot;)
uiModeOptions.Items.Add(&quot;mini&quot;)
uiModeOptions.Items.Add(&quot;full&quot;)


Public Sub uiModeOptions_OnSelectedIndexChanged(ByVal sender As Object, ByVal e As System.EventArgs) Handles uiModeOptions.SelectedIndexChanged

    &#39; Get the selected UI mode in the list box as a string.
    Dim lb As System.Windows.Forms.ListBox = sender
    Dim newMode As String = lb.SelectedItem

    &#39; Set the UI mode that the user selected.
    player.uiMode = newMode

End Sub
```





## Requirements



| Requirement | Value |
|----------------------|----------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player version 7.0 or later. Windows Media Player 9 Series or later for "invisible" or "custom"<br/>   |
| Namespace<br/> | **AxWMPLib**<br/>                                                                                                    |
| Assembly<br/>  | <dl> <dt>AxInterop.WMPLib.dll (AxInterop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**AxWindowsMediaPlayer Object (VB and C#)**](axwindowsmediaplayer-object--vb-and-c.md)
</dt> <dt>

[**AxWindowsMediaPlayer.enableContextMenu (VB and C#)**](axwmplib-axwindowsmediaplayer-enablecontextmenu--vb-and-c.md)
</dt> </dl>

 

 





