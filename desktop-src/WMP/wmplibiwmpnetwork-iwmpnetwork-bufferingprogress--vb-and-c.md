---
title: IWMPNetwork bufferingProgress property
description: The bufferingProgress property gets the percentage of buffering completed.
ms.assetid: 8dc9f31e-7c34-4714-a633-d92c3da3052b
keywords:
- bufferingProgress property Windows Media Player
- bufferingProgress property Windows Media Player , IWMPNetwork interface
- IWMPNetwork interface Windows Media Player , bufferingProgress property
topic_type:
- apiref
api_name:
- IWMPNetwork.bufferingProgress
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPNetwork::bufferingProgress property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **bufferingProgress** property gets the percentage of buffering completed.

## Syntax


```CSharp
public System.Int32 bufferingProgress {get; set;}
```


```VB

Public ReadOnly Property bufferingProgress As System.Int32
```





## Property value

A **System.Int32** that is the buffering progress expressed as a percentage.

## Remarks

Each time playback is stopped and restarted, this property is reset to zero. It is not reset if playback is paused.

Buffering applies only to streaming content. This property gets valid information only during run time when the URL for playback is set using the **AxWindowsMediaPlayer.URL** property.

Use the **AxWindowsMediaPlayer.\_WMPOCXEvents\_BufferingEvent** to determine when buffering starts or stops.

## Examples

The following example uses **bufferingProgress** to display the percentage of buffering completed in a label, in response to the Buffering Event. The example uses a timer with a 1-second interval to update the display. The **AxWMPLib.AxWindowsMediaPlayer** object is represented by the variable named player.


```CSharp
// Add a delegate for the Buffering event.
player.Buffering += new AxWMPLib._WMPOCXEvents_BufferingEventHandler(player_Buffering);

// Create an event handler for the Buffering event.
private void player_Buffering(object sender, AxWMPLib._WMPOCXEvents_BufferingEvent e)
{
    // Determine whether buffering has started or stopped.
    if (e.start == true)
    {
        // Set the timer interval at one second (1000 miliseconds).
        timer.Interval = 1000;
        
        // Start the timer.
        timer.Start();
    }
    else
    {
        // Buffering is complete. Stop the timer.
        timer.Stop();
    }
}

// Update the buffering progress in a timer event handler.
private void UpdateBufferingProgress(object sender, EventArgs e)
{
    bufferingProgressLabel.Text = ("Buffering progress: " + player.network.bufferingProgress + " percent complete");
}
```


```VB

' Create an event handler for the Buffering event.
Public Sub player_Buffering(ByVal sender As Object, ByVal e As AxWMPLib._WMPOCXEvents_BufferingEvent) Handles player.Buffering

    &#39; Test whether packets may be arriving.
    Select Case e.newState

    &#39; If WMPPlayState is Stopped, Paused, ScanForward, ScanReverse, Waiting, MediaEnded
    &#39; or Transitioning then stop the timer. 
        Case 1
        Case 2
        Case 4
        Case 5
        Case 7
        Case 8
        Case 9
            timer.Stop()

        &#39; If WMPPlayState is Playing or Buffering then set the timer interval and start the timer.
        Case Else
            timer.Interval = 1000
            timer.Start()

    End Select

End Sub

&#39; Update the buffering progress in a timer event handler.
Public Sub UpdateBufferingProgress(ByVal sender As Object, ByVal e As System.EventArgs) Handles timer.Tick

    bufferingProgressLabel.Text = (&quot;Buffering progress: &quot; + player.network.bufferingProgress + &quot; percent complete&quot;)

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

[**AxWindowsMediaPlayer.URL (VB and C#)**](axwmplib-axwindowsmediaplayer-url--vb-and-c.md)
</dt> <dt>

[**AxWindowsMediaPlayer.Buffering Event (VB and C#)**](axwmplib-axwindowsmediaplayer-buffering.md)
</dt> <dt>

[**IWMPNetwork Interface (VB and C#)**](iwmpnetwork--vb-and-c.md)
</dt> </dl>

 

 





