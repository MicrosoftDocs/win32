---
title: CurrentItemChange Event of the AxWindowsMediaPlayer Object
description: The CurrentItemChange event occurs when the value of IWMPControls.currentItem changes.
ms.assetid: c5eeafd2-405b-4808-97d1-399a2344ca42
keywords:
- CurrentItemChange Event of the AxWindowsMediaPlayer Object Windows Media Player
topic_type:
- apiref
api_name:
- CurrentItemChange Event of the AxWindowsMediaPlayer Object
api_location:
- AxInterop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 05/31/2018
---

# CurrentItemChange Event of the AxWindowsMediaPlayer Object

The CurrentItemChange event occurs when the value of IWMPControls.**currentItem** changes.

``` syntax
[C#]
private void player_CurrentItemChange(
  object sender,
  _WMPOCXEvents_CurrentItemChangeEvent e
)

[Visual Basic]
Private Sub player_CurrentItemChange(  
  sender As Object,
  e As _WMPOCXEvents_CurrentItemChangeEvent
) Handles player.CurrentItemChange
```

## Event Data

The handler associated with this event is of type **AxWMPLib.\_WMPOCXEvents\_CurrentItemChangeEventHandler**. This handler receives an argument of type **AxWMPLib.\_WMPOCXEvents\_CurrentItemChangeEvent**, which contains the following property related to this event.



| Property   | Description                                                                                                   |
|------------|---------------------------------------------------------------------------------------------------------------|
| pdispMedia | System.ObjectThe new current media item. You can cast this to an IWMPMedia interface to access it.<br/> |



 

## Examples

The following example demonstrates an event handler for the CurrentItemChange event. The AxWMPLib.AxWindowsMediaPlayer object is represented by the variable named player.


```CSharp
// Add a delegate for the CurrentItemChange event
player.CurrentItemChange += new AxWMPLib._WMPOCXEvents_CurrentItemChangeEventHandler(player_CurrentItemChange);

private void player_CurrentItemChange(object sender, AxWMPLib._WMPOCXEvents_CurrentItemChangeEvent e)
{
    // Display the name of the new media item.
    mediaText.Text = player.currentMedia.name;
}
```


```VB

Public Sub player_CurrentItemChange(ByVal sender As Object, ByVal e As AxWMPLib._WMPOCXEvents_CurrentItemChangeEvent) Handles player.CurrentItemChange

    &#39; Display the name of the new media item.
    mediaText.Text = player.currentMedia.name

End Sub
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

[**IWMPControls.currentItem (VB and C#)**](wmplibiwmpcontrols-iwmpcontrols-currentitem--vb-and-c.md)
</dt> <dt>

[**IWMPMedia Interface (VB and C#)**](iwmpmedia--vb-and-c.md)
</dt> </dl>

 

 





