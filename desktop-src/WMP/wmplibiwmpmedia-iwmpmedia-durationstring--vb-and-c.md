---
title: IWMPMedia durationString property
description: The durationString property gets a string indicating the duration of the current media item in HH MM SS format.
ms.assetid: de33c737-d73e-41f0-9c1b-944279194738
keywords:
- durationString property Windows Media Player
- durationString property Windows Media Player , IWMPMedia interface
- IWMPMedia interface Windows Media Player , durationString property
topic_type:
- apiref
api_name:
- IWMPMedia.durationString
- IWMPMedia.get_durationString
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPMedia::durationString property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **durationString** property gets a string indicating the duration of the current media item in HH:MM:SS format.

This property is read-only.

## Syntax


```CSharp
public System.String durationString {get;}
```


```VB

Public ReadOnly Property durationString As System.String
```





## Property value

A **System.String** that is the duration.

## Remarks

If this property is used with a media item other than the one specified in AxWindowsMediaPlayer.currentMedia, it may not contain a valid value. If the media item is less than an hour long, the hours portion of the return value is omitted.

Before using this property, you must have read access to the library. For more information, see [Library Access](library-access.md).

## Examples

The following example uses **durationString** to display the duration of the current media item as formatted text in a label. The **AxWMPLib.AxWindowsMediaPlayer** object is represented by the variable named player.


```CSharp
// Create an event handler for the OpenStateChange event.
private void player_OpenStateChange(object sender, AxWMPLib._WMPOCXEvents_OpenStateChangeEvent e)
{
    // Test whether the current media item is open.
    if (e.newState == (int)WMPLib.WMPOpenState.wmposMediaOpen)
    {
         // Display the formatted duration string in the label.
         mediaDuration.Text = player.currentMedia.durationString;
    }
}
```


```VB

' Create an event handler for the OpenStateChange event.
Public Sub player_OpenStateChange(ByVal sender As Object, ByVal e As AxWMPLib._WMPOCXEvents_OpenStateChangeEvent) Handles player.OpenStateChange

    &#39; Test whether the current media item is open.
    If (e.newState = 13) Then

        &#39; Display the formatted duration string in the label.
        mediaDuration.Text = player.currentMedia.durationString

    End If

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

[**IWMPMedia Interface (VB and C#)**](iwmpmedia--vb-and-c.md)
</dt> <dt>

[**IWMPMedia.duration (VB and C#)**](wmplibiwmpmedia-iwmpmedia-duration--vb-and-c.md)
</dt> </dl>

 

 





