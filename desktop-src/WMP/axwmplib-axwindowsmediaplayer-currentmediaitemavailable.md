---
title: CurrentMediaItemAvailable Event of the AxWindowsMediaPlayer Object
description: The CurrentMediaItemAvailable event occurs when a graphic metadata item in the current media item becomes available. | CurrentMediaItemAvailable Event of the AxWindowsMediaPlayer Object
ms.assetid: 7db62e6a-5f20-441a-801f-147ac386c5f8
keywords:
- CurrentMediaItemAvailable Event of the AxWindowsMediaPlayer Object Windows Media Player
topic_type:
- apiref
api_name:
- CurrentMediaItemAvailable Event of the AxWindowsMediaPlayer Object
api_location:
- AxInterop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 05/31/2018
---

# CurrentMediaItemAvailable Event of the AxWindowsMediaPlayer Object

The CurrentMediaItemAvailable event occurs when a graphic metadata item in the current media item becomes available.

``` syntax
[C#]
private void player_CurrentMediaItemAvailable(
  object sender,
  _WMPOCXEvents_CurrentMediaItemAvailableEvent e
)

[Visual Basic]
Private Sub player_CurrentMediaItemAvailable(
  sender As Object,  
  e As _WMPOCXEvents_CurrentMediaItemAvailableEvent
) Handles player.CurrentMediaItemAvailable
```

## Event Data

The handler associated with this event is of type **AxWMPLib.\_WMPOCXEvents\_CurrentMediaItemAvailableEventHandler**. This handler receives an argument of type **AxWMPLib.\_WMPOCXEvents\_CurrentMediaItemAvailableEvent**, which contains the following property related to this event.



| Property     | Description                                                 |
|--------------|-------------------------------------------------------------|
| bstrItemName | System.StringThe name of the current media item.<br/> |



 

## Remarks

Because playback can begin before a media item is fully downloaded, any metadata graphics contained in the media item (such as album cover art) may not be available when it starts to play. This event alerts you when a metadata graphic item is finished downloading. You can then retrieve the **IWMPMedia** interface by passing the value of **bstrItemName** to the *IWMPMediaCollection*.**getByName** method, after which you can access the metadata graphic item by using *IWMPMedia3*.**getItemInfoByType** and specifying **WM/Picture** for the attribute name.

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
</dt> <dt>

[**IWMPMedia3.getItemInfoByType (VB and C#)**](wmplibiwmpmedia3-iwmpmedia3-getiteminfobytype--vb-and-c.md)
</dt> <dt>

[**IWMPMediaCollection.getByName (VB and C#)**](wmplibiwmpmediacollection-iwmpmediacollection-getbyname--vb-and-c.md)
</dt> </dl>

 

 





