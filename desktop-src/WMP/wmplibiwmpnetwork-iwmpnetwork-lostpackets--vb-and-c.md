---
title: IWMPNetwork lostPackets property
description: The lostPackets property gets the number of packets lost.
ms.assetid: 611218d3-c4d3-4d4e-835c-1e7a956b2718
keywords:
- lostPackets property Windows Media Player
- lostPackets property Windows Media Player , IWMPNetwork interface
- IWMPNetwork interface Windows Media Player , lostPackets property
topic_type:
- apiref
api_name:
- IWMPNetwork.lostPackets
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPNetwork::lostPackets property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **lostPackets** property gets the number of packets lost.

## Syntax


```CSharp
public System.Int32 lostPackets {get; set;}
```


```VB

Public ReadOnly Property lostPackets As System.Int32
```





## Property value

A **System.Int32** that is the number of lost packets.

## Remarks

This property includes streaming media packets only, and will return zero when using the HTTP protocol, which is lossless.

Packets can be lost for a number of reasons, such as the type and quality of the network connection.

Each time playback is stopped and restarted, this property is reset to zero. The value is not reset if playback is paused. This property gets valid information only during run time when the URL for playback is set by using the **AxWindowsMediaPlayer.URL** property.

## Examples

The following code example uses **lostPackets** to display the total number of packets lost during playback. The information is displayed in a label when the user clicks a button. The **AxWMPLib.AxWindowsMediaPlayer** object is represented by the variable named player.


```CSharp
private void showLostPackets_Click(object sender, System.EventArgs e)
{
    lostPacketsLabel.Text = ("Packets lost: " + player.network.lostPackets.ToString());
}
```


```VB

Public Sub showLostPackets_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles showLostPackets.Click

    lostPacketsLabel.Text = (&quot;Packets lost: &quot; + player.network.lostPackets.ToString())

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

[**IWMPNetwork Interface (VB and C#)**](iwmpnetwork--vb-and-c.md)
</dt> <dt>

[**AxWindowsMediaPlayer.URL (VB and C#)**](axwmplib-axwindowsmediaplayer-url--vb-and-c.md)
</dt> </dl>

 

 





