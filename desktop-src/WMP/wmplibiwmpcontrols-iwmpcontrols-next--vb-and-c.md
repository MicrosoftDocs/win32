---
title: IWMPControls next method
description: The next method sets the next item in the playlist as the current item.
ms.assetid: 3f82ef25-a1e0-4845-b0ed-dd6463719577
keywords:
- next method Windows Media Player
- next method Windows Media Player , IWMPControls interface
- IWMPControls interface Windows Media Player , next method
topic_type:
- apiref
api_name:
- IWMPControls.next
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPControls::next method

The **next** method sets the next item in the playlist as the current item.

## Syntax


```CSharp
public void next();
```


```VB

Public Sub next()
Implements IWMPControls.next
```





## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

If the playlist is on the last entry when **next** is invoked, the first entry in the playlist will become the current one.

For server-side playlists, this method skips to the next item in the server-side playlist, not the client playlist.

When playing a DVD, this method skips to the next logical chapter in the playback sequence, which may not be the next chapter in the playlist. When playing DVD still images, this method skips to the next image.

## Examples

The following example uses **next** to move to the next item in the current playlist in response to the Click event of a button. The **AxWMPLib.AxWindowsMediaPlayer** object is represented by the variable named player.


```CSharp
private void nextButton_Click(object o, System.EventArgs args)
{
    // To get all of the available functionality of the player controls, cast the
    // value returned by player.Ctlcontrols to a WMPLib.IWMPControls3 interface. 
    WMPLib.IWMPControls3 controls = (WMPLib.IWMPControls3)player.Ctlcontrols;

    // Check first to be sure the operation is valid.
    if (controls.get_isAvailable("next"))
    {
        controls.next();
    }
}
```


```VB

Public Sub nextButton_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles nextButton.Click

    &#39; To get all of the available functionality of the player controls, Dim the
    &#39; value returned by player.Ctlcontrols as a WMPLib.IWMPControls3 interface.
    Dim controls As WMPLib.IWMPControls3 = player.Ctlcontrols

    &#39; Check first to be sure the operation is valid.
    If (controls.isAvailable(&quot;next&quot;)) Then

        controls.next()

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

[**IWMPControls Interface (VB and C#)**](iwmpcontrols--vb-and-c.md)
</dt> <dt>

[**IWMPControls.previous (VB and C#)**](wmplibiwmpcontrols-iwmpcontrols-previous--vb-and-c.md)
</dt> <dt>

[**IWMPControls.stop (VB and C#)**](wmplibiwmpcontrols-iwmpcontrols-stop--vb-and-c.md)
</dt> </dl>

 

 





