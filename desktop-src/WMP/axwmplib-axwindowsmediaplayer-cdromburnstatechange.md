---
title: CdromBurnStateChange Event of the AxWindowsMediaPlayer Object
description: The CdromBurnStateChange event occurs when a CD burning operation changes state.
ms.assetid: fec8a8e5-e282-454e-9713-fd9bb131df6a
keywords:
- CdromBurnStateChange Event of the AxWindowsMediaPlayer Object Windows Media Player
topic_type:
- apiref
api_name:
- CdromBurnStateChange Event of the AxWindowsMediaPlayer Object
api_location:
- AxInterop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# CdromBurnStateChange Event of the AxWindowsMediaPlayer Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The CdromBurnStateChange event occurs when a CD burning operation changes state.

``` syntax
[C#]
private void player_CdromBurnStateChange(
  object sender,
  _WMPOCXEvents_CdromBurnStateChangeEvent e
)

[Visual Basic]
Private Sub player_CdromBurnStateChange(  
  sender As Object,
  e As _WMPOCXEvents_CdromBurnStateChangeEvent
) Handles player.CdromBurnStateChange
```

## Event Data

The handler associated with this event is of type **AxWMPLib.\_WMPOCXEvents\_CdromBurnStateChangeEventHandler**. This handler receives an argument of type **AxWMPLib.\_WMPOCXEvents\_CdromBurnStateChangeEvent**, which contains the following properties related to this event.



| Property   | Description                                                                                               |
|------------|-----------------------------------------------------------------------------------------------------------|
| pCdromBurn | WMPLib.IWMPCdromBurnThe interface that represents the burning operation that raised the error.<br/> |
| wmpbs      | WMPLib.WMPBurnStateThe enumeration value that indicates the new state.<br/>                         |



 

## Requirements



| Requirement | Value |
|----------------------|----------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 11<br/>                                                                                         |
| Namespace<br/> | **AxWMPLib**<br/>                                                                                                    |
| Assembly<br/>  | <dl> <dt>AxInterop.WMPLib.dll (AxInterop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**AxWindowsMediaPlayer Object (VB and C#)**](axwindowsmediaplayer-object--vb-and-c.md)
</dt> <dt>

[**IWMPCdromBurn Interface (VB and C#)**](iwmpcdromburn--vb-and-c.md)
</dt> <dt>

[**WMPBurnState**](/previous-versions/windows/desktop/api/wmp/ne-wmp-wmpburnstate)
</dt> </dl>

 

 





