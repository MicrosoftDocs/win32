---
title: ModeChange Event of the AxWindowsMediaPlayer Object
description: The ModeChange event occurs when a mode of Windows Media Player is changed. | ModeChange Event of the AxWindowsMediaPlayer Object
ms.assetid: 56308425-dce5-4691-8970-c0807744abef
keywords:
- ModeChange Event of the AxWindowsMediaPlayer Object Windows Media Player
topic_type:
- apiref
api_name:
- ModeChange Event of the AxWindowsMediaPlayer Object
api_location:
- AxInterop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 05/31/2018
---

# ModeChange Event of the AxWindowsMediaPlayer Object

The ModeChange event occurs when a mode of Windows Media Player is changed.

``` syntax
[C#]
private void player_ModeChange(
  object sender,
  _WMPOCXEvents_ModeChangeEvent e
)

[Visual Basic]
Private Sub player_ModeChange( 
  sender As Object,
  e As _WMPOCXEvents_ModeChangeEvent
) Handles player.ModeChange
```

## Event Data

The handler associated with this event is of type **AxWMPLib.\_WMPOCXEvents\_ModeChangeEventHandler**. This handler receives an argument of type **AxWMPLib.\_WMPOCXEvents\_ModeChangeEvent**, which contains the following properties related to this event.



| Property | Description                                                                                    |
|----------|------------------------------------------------------------------------------------------------|
| modeName | System.StringIndicates the mode that was changed. For possible values, see Remarks.<br/> |
| newValue | System.BooleanIndicates the new state of the specified mode.<br/>                        |



 

## Remarks

The following table shows the possible values for the modeName property.



| String  | Description                                         |
|---------|-----------------------------------------------------|
| shuffle | Tracks are played in random order.                  |
| loop    | The entire sequence of tracks is played repeatedly. |



 

## Requirements



|                      |                                                                                                                            |
|----------------------|----------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                          |
| Namespace<br/> | **AxWMPLib**<br/>                                                                                                    |
| Assembly<br/>  | <dl> <dt>AxInterop.WMPLib.dll (AxInterop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**AxWindowsMediaPlayer Object (VB and C#)**](axwindowsmediaplayer-object--vb-and-c.md)
</dt> <dt>

[**IWMPSettings.getMode (VB and C#)**](wmplibiwmpsettings-iwmpsettings-getmode--vb-and-c.md)
</dt> <dt>

[**IWMPSettings.setMode (VB and C#)**](wmplibiwmpsettings-iwmpsettings-setmode--vb-and-c.md)
</dt> </dl>

 

 





