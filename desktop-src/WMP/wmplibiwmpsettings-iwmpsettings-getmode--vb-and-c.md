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
ms.date: 05/31/2018
---

# IWMPSettings::getMode method

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

 

 





