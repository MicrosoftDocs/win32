---
title: FolderScanStateChange Event of the AxWindowsMediaPlayer Object
description: The FolderScanStateChange event occurs when a folder monitoring operation changes state.
ms.assetid: f68829a3-00df-417a-ae78-49dff1e6f09b
keywords:
- FolderScanStateChange Event of the AxWindowsMediaPlayer Object Windows Media Player
topic_type:
- apiref
api_name:
- FolderScanStateChange Event of the AxWindowsMediaPlayer Object
api_location:
- AxInterop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 05/31/2018
---

# FolderScanStateChange Event of the AxWindowsMediaPlayer Object

The FolderScanStateChange event occurs when a folder monitoring operation changes state.

``` syntax
[C#]
private void player_FolderScanStateChange(
  object sender,
  _WMPOCXEvents_FolderScanStateChangeEvent e
)

[Visual Basic]
Private Sub player_FolderScanStateChange( 
  sender As Object,  
  e As _WMPOCXEvents_FolderScanStateChangeEvent
) Handles player.FolderScanStateChange
```

## Event Data

The handler associated with this event is of type **AxWMPLib.\_WMPOCXEvents\_FolderScanStateChangeEventHandler**. This handler receives an argument of type **AxWMPLib.\_WMPOCXEvents\_FolderScanStateChangeEvent**, which contains the following property related to this event.



| Property | Description                                                                             |
|----------|-----------------------------------------------------------------------------------------|
| wmpfss   | WMPLib.WMPFolderScanStateThe enumeration value that indicates the new state.<br/> |



 

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

[**WMPFolderScanState**](/previous-versions/windows/desktop/api/wmp/ne-wmp-wmpfolderscanstate)
</dt> </dl>

 

 





