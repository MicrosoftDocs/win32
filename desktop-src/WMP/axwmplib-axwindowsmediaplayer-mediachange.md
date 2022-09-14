---
title: MediaChange Event of the AxWindowsMediaPlayer Object
description: The MediaChange event occurs when a media item changes. | MediaChange Event of the AxWindowsMediaPlayer Object
ms.assetid: 0a2380ff-df50-4092-a952-812184822719
keywords:
- MediaChange Event of the AxWindowsMediaPlayer Object Windows Media Player
topic_type:
- apiref
api_name:
- MediaChange Event of the AxWindowsMediaPlayer Object
api_location:
- AxInterop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 05/31/2018
---

# MediaChange Event of the AxWindowsMediaPlayer Object

The MediaChange event occurs when a media item changes.

``` syntax
[C#]
private void player_MediaChange(
  object sender,
  _WMPOCXEvents_MediaChangeEvent e
)

[Visual Basic]
Private Sub player_MediaChange(  
  sender As Object,  
  e As _WMPOCXEvents_MediaChangeEvent
) Handles player.MediaChange
```

## Event Data

The handler associated with this event is of type **AxWMPLib.\_WMPOCXEvents\_MediaChangeEventHandler**. This handler receives an argument of type **AxWMPLib.\_WMPOCXEvents\_MediaChangeEvent**, which contains the following property related to this event.



| Property | Description                                                                                                    |
|----------|----------------------------------------------------------------------------------------------------------------|
| Item     | System.ObjectThe media item that changed. You can cast this to an IWMPMedia interface to access it.<br/> |



 

## Examples

The following example uses a label to display the name of the current media item. The code updates the text in the label with each occurrence of the MediaChange Event. The AxWMPLib.AxWindowsMediaPlayer object is represented by the variable named player.


```CSharp
// Add a delegate for the MediaChange event.
player.MediaChange += new AxWMPLib._WMPOCXEvents_MediaChangeEventHandler(player_MediaChange);

private void player_MediaChange(object sender, AxWMPLib._WMPOCXEvents_MediaChangeEvent e)
{
    // Get an interface to the changed media item that is returned in the event data. 
    WMPLib.IWMPMedia3 changedItem = (WMPLib.IWMPMedia3)e.item;

    // Display the name of the changed media item.
    mediaName.Text = changedItem.name;
}
```


```VB

Public Sub player_MediaChange(ByVal sender As Object, ByVal e As AxWMPLib._WMPOCXEvents_MediaChangeEvent) Handles player.MediaChange

    &#39; Get an interface to the changed media item that is returned in the event data.
    Dim changedItem As WMPLib.IWMPMedia3 = e.item

    &#39; Display the name of the changed media item.
    mediaName.Text = changedItem.name

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

[**IWMPMedia Interface (VB and C#)**](iwmpmedia--vb-and-c.md)
</dt> </dl>

 

 





