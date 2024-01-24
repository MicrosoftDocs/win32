---
title: IWMPSettings getMode method
description: The getMode method returns a value indicating whether loop mode or shuffle mode is active.
ms.assetid: a2e4bf74-017f-4c54-a3a1-a03b75a87a59
keywords:
- getMode method Windows Media Player
- getMode method Windows Media Player , IWMPSettings interface
- IWMPSettings interface Windows Media Player , getMode method
topic_type:
- apiref
api_name:
- IWMPSettings.getMode
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPSettings::getMode method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **getMode** method returns a value indicating whether loop mode or shuffle mode is active.

## Syntax


```CSharp
public System.Boolean getMode(
  System.String bstrMode
);
```


```VB

Public Function getMode( _
  ByVal bstrMode As System.String _
) As System.Boolean
Implements IWMPSettings.getMode
```





## Parameters

<dl> <dt>

*bstrMode* \[in\]
</dt> <dd>

A **System.String** that is one of the following values.



| Value      | Description                                                                                      |
|------------|--------------------------------------------------------------------------------------------------|
| autoRewind | Tracks are restarted from the beginning after playing to the end.                                |
| loop       | The sequence of tracks repeats itself.                                                           |
| showFrame  | The nearest key frame is displayed when not playing. This mode is not relevant for audio tracks. |
| shuffle    | Tracks are played in random order.                                                               |



 

</dd> </dl>

## Return value

A **System.Boolean** value indicating whether the specified mode is active.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPSettings Interface (VB and C#)**](iwmpsettings--vb-and-c.md)
</dt> <dt>

[**IWMPSettings.setMode (VB and C#)**](wmplibiwmpsettings-iwmpsettings-setmode--vb-and-c.md)
</dt> </dl>

 

 





