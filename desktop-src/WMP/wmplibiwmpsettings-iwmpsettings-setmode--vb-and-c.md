---
title: IWMPSettings setMode method
description: The setMode method sets the loop mode or shuffle mode to active or inactive.
ms.assetid: e9d3765e-6edb-47a5-ac97-5e00b62498c2
keywords:
- setMode method Windows Media Player
- setMode method Windows Media Player , IWMPSettings interface
- IWMPSettings interface Windows Media Player , setMode method
topic_type:
- apiref
api_name:
- IWMPSettings.setMode
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPSettings::setMode method

The **setMode** method sets the loop mode or shuffle mode to active or inactive.

## Syntax


```CSharp
public void setMode(
  System.String bstrMode,
  System.Boolean varfMode
);
```


```VB

Public Sub setMode( _
  ByVal bstrMode As System.String, _
  ByVal varfMode As System.Boolean _
)
Implements IWMPSettings.setMode
```





## Parameters

<dl> <dt>

*bstrMode* \[in\]
</dt> <dd>

A **System.String** that is the name of the mode being changed, containing one of the following values.



| Value      | Description                                                                                      |
|------------|--------------------------------------------------------------------------------------------------|
| autoRewind | Tracks are restarted from the beginning after playing to the end.                                |
| loop       | The sequence of tracks repeats itself.                                                           |
| showFrame  | The nearest key frame is displayed when not playing. This mode is not relevant for audio tracks. |
| shuffle    | Tracks are played in random order.                                                               |



 

</dd> <dt>

*varfMode* \[in\]
</dt> <dd>

A **System.Boolean** value specifying whether the new specified mode is active.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

When the showFrame mode is active, Windows Media Player must access the track content to retrieve the video frame. Use this mode cautiously when playing content that is not local.

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

[**IWMPSettings.getMode (VB and C#)**](wmplibiwmpsettings-iwmpsettings-getmode--vb-and-c.md)
</dt> </dl>

 

 





