---
title: AudioLanguageChange Event of the AxWindowsMediaPlayer Object
description: The AudioLanguageChange event occurs when the current audio language changes. | AudioLanguageChange Event of the AxWindowsMediaPlayer Object
ms.assetid: 35e4ff82-fc59-4d28-b7fc-1527fb46b960
keywords:
- AudioLanguageChange Event of the AxWindowsMediaPlayer Object Windows Media Player
topic_type:
- apiref
api_name:
- AudioLanguageChange Event of the AxWindowsMediaPlayer Object
api_location:
- AxInterop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 05/31/2018
---

# AudioLanguageChange Event of the AxWindowsMediaPlayer Object

The AudioLanguageChange event occurs when the current audio language changes.

``` syntax
[C#]
private void player_AudioLanguageChange(
  object sender,
  _WMPOCXEvents_AudioLanguageChangeEvent e
)

[Visual Basic]
Private Sub player_AudioLanguageChange(
  sender As Object,
  e As _WMPOCXEvents_AudioLanguageChangeEvent
) Handles player.AudioLanguageChange
```

## Event Data

The handler associated with this event is of type **AxWMPLib.\_WMPOCXEvents\_AudioLanguageChangeEventHandler**. This handler receives an argument of type **AxWMPLib.\_WMPOCXEvents\_AudioLanguageChangeEvent**, which contains the following property related to this event.



| Property   | Description                                                                                    |
|------------|------------------------------------------------------------------------------------------------|
| **langID** | **System.Int32**Uniquely identifies a particular language dialect, called a locale.<br/> |



 

## Remarks

A locale identifier (LCID) uniquely identifies a particular language dialect, called a locale.

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

[**IWMPControls3.currentAudioLanguage (VB and C#)**](wmplibiwmpcontrols3-iwmpcontrols3-currentaudiolanguage--vb-and-c.md)
</dt> </dl>

 

 





