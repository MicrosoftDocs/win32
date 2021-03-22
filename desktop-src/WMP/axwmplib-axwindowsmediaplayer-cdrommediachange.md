---
title: CdromMediaChange Event of the AxWindowsMediaPlayer Object
description: The CdromMediaChange event occurs when a CD or DVD is inserted into or ejected from a CD or DVD drive. | CdromMediaChange Event of the AxWindowsMediaPlayer Object
ms.assetid: 0a6378c1-59e4-4be3-8764-d5c4ab478b6c
keywords:
- CdromMediaChange Event of the AxWindowsMediaPlayer Object Windows Media Player
topic_type:
- apiref
api_name:
- CdromMediaChange Event of the AxWindowsMediaPlayer Object
api_location:
- AxInterop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 05/31/2018
---

# CdromMediaChange Event of the AxWindowsMediaPlayer Object

The **CdromMediaChange** event occurs when a CD or DVD is inserted into or ejected from a CD or DVD drive.

``` syntax
[C#]
private void player_CdromMediaChange(
  object sender,
  _WMPOCXEvents_CdromMediaChangeEvent e
)

[Visual Basic]
Private Sub player_CdromMediaChange(  
  sender As Object,
  e As _WMPOCXEvents_CdromMediaChangeEvent
) Handles player.CdromMediaChange
```

## Event Data

The handler associated with this event is of type **AxWMPLib.\_WMPOCXEvents\_CdromMediaChangeEventHandler**. This handler receives an argument of type **AxWMPLib.\_WMPOCXEvents\_CdromMediaChangeEvent**, which contains the following property related to this event.



| Property | Description                                                        |
|----------|--------------------------------------------------------------------|
| CdromNum | System.Int32Specifies the index of the CD or DVD drive.<br/> |



 

## Remarks

The index of the CD drive corresponds to the index of an IWMPCdrom interface accessible through the IWMPCdromCollection interface.

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

[**IWMPCdrom Interface (VB and C#)**](iwmpcdrom--vb-and-c.md)
</dt> <dt>

[**IWMPCdromCollection Interface (VB and C#)**](iwmpcdromcollection--vb-and-c.md)
</dt> </dl>

 

 





