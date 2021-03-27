---
title: AxWindowsMediaPlayer.playState property
description: The playState property gets an enumeration value indicating the state of the Windows Media Player operation.
ms.assetid: ab9f1547-5c28-4289-beaf-9262f7f59b07
keywords:
- playState property Windows Media Player
- playState property Windows Media Player , AxWindowsMediaPlayer class
- AxWindowsMediaPlayer class Windows Media Player , playState property
topic_type:
- apiref
api_name:
- AxWindowsMediaPlayer.playState
api_location:
- AxInterop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# AxWindowsMediaPlayer.playState property

The playState property gets an enumeration value indicating the state of the Windows Media Player operation.

This property is read-only.

## Syntax


```CSharp
public WMPPlayState playState {get;}
```


```VB

Public ReadOnly Property playState As WMPPlayState
```





## Property value

The WMPLib.WMPPlayState enumeration value.

## Remarks

Windows Media Player states are not guaranteed to occur in any particular order. Furthermore, not every state necessarily occurs during a sequence of events. You should not write code that relies upon state order.

## Examples

The following example uses the playState property to display the current playing status of the player in a label. The AxWMPLib.AxWindowsMediaPlayer object is represented by the variable named player.


```CSharp
// Test whether Windows Media Player is in the playing state. 
if (player.playState == WMPLib.WMPPlayState.wmppsPlaying)
{
    playStateLabel.Text = "Windows Media Player is playing!";
}
else
{
    playStateLabel.Text = "Windows Media Player is NOT playing!";
}
```


```VB

' Test whether Windows Media Player is in the playing state. 
If (player.playState = WMPLib.WMPPlayState.wmppsPlaying) Then

    playStateLabel.Text = &quot;Windows Media Player is playing!&quot;

Else

    playStateLabel.Text = &quot;Windows Media Player is NOT playing!&quot;

End If
```





## Requirements



| Requirement | Value |
|----------------------|----------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                          |
| Namespace<br/> | **AxWMPLib**<br/>                                                                                                    |
| Assembly<br/>  | <dl> <dt>AxInterop.WMPLib.dll (AxInterop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**AxWindowsMediaPlayer Object (VB and C#)**](axwindowsmediaplayer-object--vb-and-c.md)
</dt> <dt>

[**AxWindowsMediaPlayer.PlayStateChange Event (VB and C#)**](axwmplib-axwindowsmediaplayer-playstatechange.md)
</dt> <dt>

[**WMPPlayState**](/previous-versions/windows/desktop/api/wmp/ne-wmp-wmpplaystate)
</dt> </dl>

 

 





