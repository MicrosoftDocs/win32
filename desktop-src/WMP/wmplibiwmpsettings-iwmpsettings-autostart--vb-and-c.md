---
title: IWMPSettings autoStart property
description: The autoStart property gets or sets a value indicating whether the current media item begins playing automatically.
ms.assetid: 01a1cb78-9951-478a-8ea3-1ae06164beab
keywords:
- autoStart property Windows Media Player
- autoStart property Windows Media Player , IWMPSettings interface
- IWMPSettings interface Windows Media Player , autoStart property
topic_type:
- apiref
api_name:
- IWMPSettings.autoStart
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPSettings::autoStart property

The **autoStart** property gets or sets a value indicating whether the current media item begins playing automatically.

## Syntax


```CSharp
public System.Boolean autoStart {get; set;}
```


```VB

Public Property autoStart As System.Boolean
```





## Property value

A **System.Boolean** value that indicates whether the current media item begins playing automatically. The default is **true**.

## Remarks

If **autoStart** is set to **true**, the media item will begin playing when **AxWindowsMediaPlayer.URL**, **AxWindowsMediaPlayer.currentPlaylist**, or **AxWindowsMediaPlayer.currentMedia** is set. Otherwise, the media item will not start playing until the **IWMPControls.play** method is called.

Unless you set **autoStart** to **true** immediately before specifying a media item, you should not rely on this setting as a substitute for using the **IWMPControls.play** method.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**AxWindowsMediaPlayer.currentMedia (VB and C#)**](axwmplib-axwindowsmediaplayer-currentmedia--vb-and-c.md)
</dt> <dt>

[**AxWindowsMediaPlayer.currentPlaylist (VB and C#)**](axwmplib-axwindowsmediaplayer-currentplaylist--vb-and-c.md)
</dt> <dt>

[**AxWindowsMediaPlayer.URL (VB and C#)**](axwmplib-axwindowsmediaplayer-url--vb-and-c.md)
</dt> <dt>

[**IWMPControls.play (VB and C#)**](wmplibiwmpcontrols-iwmpcontrols-play--vb-and-c.md)
</dt> <dt>

[**IWMPSettings Interface (VB and C#)**](iwmpsettings--vb-and-c.md)
</dt> </dl>

 

 





