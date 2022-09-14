---
title: DomainChange Event of the AxWindowsMediaPlayer Object
description: The DomainChange event occurs when the DVD domain changes. | DomainChange Event of the AxWindowsMediaPlayer Object
ms.assetid: a080082e-1ba4-4080-b39c-b84292ecacb0
keywords:
- DomainChange Event of the AxWindowsMediaPlayer Object Windows Media Player
topic_type:
- apiref
api_name:
- DomainChange Event of the AxWindowsMediaPlayer Object
api_location:
- AxInterop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 05/31/2018
---

# DomainChange Event of the AxWindowsMediaPlayer Object

The DomainChange event occurs when the DVD domain changes.

``` syntax
[C#]
private void player_DomainChange(
  object sender,
  _WMPOCXEvents_DomainChangeEvent e
)

[Visual Basic]
Private Sub player_DomainChange(  
  sender As Object,
  e As _WMPOCXEvents_DomainChangeEvent
) Handles player.DomainChange
```

## Event Data

The handler associated with this event is of type **AxWMPLib.\_WMPOCXEvents\_DomainChangeEventHandler**. This handler receives an argument of type **AxWMPLib.\_WMPOCXEvents\_DomainChangeEvent**, which contains the following property related to this event.



| Property  | Description                                                                                     |
|-----------|-------------------------------------------------------------------------------------------------|
| strDomain | System.StringIndicates the new domain. For possible values, see the Remarks section.<br/> |



 

## Remarks

The following table shows the possible values for the strDomain property.



| String            | Description                                                          |
|-------------------|----------------------------------------------------------------------|
| firstPlay         | Performing default initialization of a DVD disc.                     |
| videoManagerMenu  | Displaying menus for whole disc. Also known as Root Menu or topMenu. |
| videoTitleSetMenu | Displaying menus for current title set. Also known as titleMenu.     |
| title             | Displaying the current title.                                        |
| stop              | The DVD Navigator is in the DVD Stop domain.                         |



 

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

[**IWMPDVD Interface (VB and C#)**](iwmpdvd--vb-and-c.md)
</dt> </dl>

 

 





