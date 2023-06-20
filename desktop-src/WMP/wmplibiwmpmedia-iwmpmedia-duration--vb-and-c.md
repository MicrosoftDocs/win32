---
title: IWMPMedia duration property
description: The duration property gets the duration in seconds of the current media item.
ms.assetid: f8a0bf3e-eeaf-46f5-90c8-d3b11ce4eb39
keywords:
- duration property Windows Media Player
- duration property Windows Media Player , IWMPMedia interface
- IWMPMedia interface Windows Media Player , duration property
topic_type:
- apiref
api_name:
- IWMPMedia.duration
- IWMPMedia.get_duration
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPMedia::duration property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **duration** property gets the duration in seconds of the current media item.

This property is read-only.

## Syntax


```CSharp
public System.Double duration {get;}
```


```VB

Public ReadOnly Property duration As System.Double
```





## Property value

A **System.Double** that is the duration in seconds.

## Remarks

If this property is used with a media item other than the one specified in AxWindowsMediaPlayer.currentMedia, it may not contain a valid value.

To retrieve the duration for files that are not in the user's library, you must wait for Windows Media Player to open the file; that is, the current **OpenState** must equal **MediaOpen**. You can verify this by handling the **AxWindowsMediaPlayer.\_WMPOCXEvents\_OpenStateChange** event or by periodically checking the value of **AxWindowsMediaPlayer.openState**.

For playlists, the duration of each media item can be retrieved when the individual media item is opened, rather than the when the playlist is opened.

Before using this property, you must have read access to the library. For more information, see [Library Access](library-access.md).

## Examples

The following example uses **duration** to display the time remaining in the current media item in a label. A timer updates the text in the label every second.


```CSharp
// Set the timer to fire an event every second and start the timer.
timer.Interval = 1000;
timer.Start();

// Note:  Use the AxWindowsMediaPlayer.PlayStateChange event with a switch statement to
// determine when to start and stop the timer. 

private void TimerEventProcessor(object sender, System.EventArgs e)
{
    // Subtract the current position from the duration of the current media to get
    // the time remaining. Use the Math.floor method to round the result down to the
    // nearest whole number.
    double t = Math.Floor(player.currentMedia.duration - player.Ctlcontrols.currentPosition);

    // Display the time remaining in the current media.
    timeRemaining.Text = ("Seconds remaining: " + t.ToString());        
}
```


```VB

' Set the timer to fire an event every second and start the timer.
Timer.Interval = 1000
Timer.Start()

&#39; Note:  Use the AxWindowsMediaPlayer.PlayStateChange event with a Select Case statement to
&#39; determine when to start and stop the timer. 

Public Sub TimerEventProcessor(ByVal sender As Object, ByVal e As System.EventArgs) Handles Timer.Tick

    &#39; Subtract the current position from the duration of the current media to get
    &#39; the time remaining. Use the Math.Floor method to round the result down to the
    &#39; nearest whole number.
    Dim t As Double = Math.Floor(player.currentMedia.duration - player.Ctlcontrols.currentPosition)

    &#39; Display the time remaining in the current media.
    timeRemaining.Text = (&quot;Seconds remaining: &quot; + t.ToString())

End Sub
```





## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**AxWindowsMediaPlayer.currentMedia (VB and C#)**](axwmplib-axwindowsmediaplayer-currentmedia--vb-and-c.md)
</dt> <dt>

[**AxWindowsMediaPlayer.openState (VB and C#)**](axwmplib-axwindowsmediaplayer-openstate--vb-and-c.md)
</dt> <dt>

[**AxWindowsMediaPlayer.OpenStateChange Event (VB and C#)**](axwmplib-axwindowsmediaplayer-openstatechange.md)
</dt> <dt>

[**IWMPMedia Interface (VB and C#)**](iwmpmedia--vb-and-c.md)
</dt> <dt>

[**IWMPMedia.durationString (VB and C#)**](wmplibiwmpmedia-iwmpmedia-durationstring--vb-and-c.md)
</dt> </dl>

 

 





