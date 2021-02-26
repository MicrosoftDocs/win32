---
title: IWMPControls pause method
description: The pause method pauses playback of the media item. | IWMPControls pause method
ms.assetid: 1d9ebaf3-84b4-458d-a393-2b685cd0dbfb
keywords:
- pause method Windows Media Player
- pause method Windows Media Player , IWMPControls interface
- IWMPControls interface Windows Media Player , pause method
topic_type:
- apiref
api_name:
- IWMPControls.pause
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPControls::pause method

The **pause** method pauses playback of the media item.

## Syntax


```CSharp
public void pause();
```


```VB

Public Sub pause()
Implements IWMPControls.pause
```





## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

When a file is paused, Windows Media Player does not give up any system resources, such as the audio device.

To determine whether a particular media type can be paused, pass the **System.String** value "pause" to the **IWMPControls.isAvailable** property (the **IWMPControls.get\_isAvailable** method in C#).

## Examples

The following example uses **pause** to pause playback of the current media item in response to the Click event of a button. The **AxWMPLib.AxWindowsMediaPlayer** object is represented by the variable named player.


```CSharp
private void pauseButton_Click(object o, System.EventArgs args)
{
    // To get all of the available functionality of the player controls, cast the
    // value returned by player.Ctlcontrols to a WMPLib.IWMPControls3 interface. 
    WMPLib.IWMPControls3 controls = (WMPLib.IWMPControls3)player.Ctlcontrols;

    // Check first to be sure the operation is valid. 
    if (controls.get_isAvailable("pause"))
    {
        controls.pause();
    }
}
```


```VB

Public Sub pauseButton_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles pauseButton.Click

    &#39; To get all of the available functionality of the player controls, Dim the
    &#39; value returned by player.Ctlcontrols as a WMPLib.IWMPControls3 interface.
    Dim controls As WMPLib.IWMPControls3 = player.Ctlcontrols

    &#39; Check first to be sure the operation is valid. 
    If (controls.isAvailable(&quot;pause&quot;)) Then

        controls.pause()

    End If

End Sub
```





## Requirements



|                      |                                                                                                                        |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPControls Interface (VB and C#)**](iwmpcontrols--vb-and-c.md)
</dt> <dt>

[**IWMPControls.isAvailable (VB and C#)**](iwmpcontrols-isavailable--vb-and-c.md)
</dt> </dl>

 

 





