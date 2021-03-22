---
title: IWMPControls currentPosition property
description: The currentPosition property gets or sets the current position in the media item in seconds from the beginning.
ms.assetid: 48f5241e-7528-485e-bf47-d655ba842af2
keywords:
- currentPosition property Windows Media Player
- currentPosition property Windows Media Player , IWMPControls interface
- IWMPControls interface Windows Media Player , currentPosition property
topic_type:
- apiref
api_name:
- IWMPControls.currentPosition
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPControls::currentPosition property

The **currentPosition** property gets or sets the current position in the media item in seconds from the beginning.

## Syntax


```CSharp
public System.Double currentPosition {get; set;}
```


```VB

Public Property currentPosition As System.Double
```





## Property value

A **System.Double** that is the current position.

## Examples

The following example uses **currentPosition** to seek to a position provided by the user. In response to a button click, **currentPosition** is set to the value entered in a text box called newPosition. The **AxWMPLib.AxWindowsMediaPlayer** object is represented by the variable named player.


```CSharp
private void setPosition_Click(object sender, System.EventArgs e)
{ 
    // ...Add code to ensure that the text box contains a valid value.
 
    // Set the current position of the media item to the position entered by the user.
    player.Ctlcontrols.currentPosition = Convert.ToDouble(newPosition.Text);
}
```


```VB

Public Sub setPosition_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles setPosition.Click

    &#39; ...Add code to ensure that the text box contains a valid value.

    &#39; Set the current position of the media item to the position entered by the user.
    player.Ctlcontrols.currentPosition = Convert.ToDouble(newPosition.Text)

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

[**IWMPControls.currentPositionString (VB and C#)**](wmplibiwmpcontrols-iwmpcontrols-currentpositionstring--vb-and-c.md)
</dt> </dl>

 

 





