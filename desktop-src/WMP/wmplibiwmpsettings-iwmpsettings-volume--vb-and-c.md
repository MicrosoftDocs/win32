---
title: IWMPSettings volume property
description: The volume property gets or sets the current playback volume.
ms.assetid: cff4fe70-9ca2-4419-bfc3-d622e8c72756
keywords:
- volume property Windows Media Player
- volume property Windows Media Player , IWMPSettings interface
- IWMPSettings interface Windows Media Player , volume property
topic_type:
- apiref
api_name:
- IWMPSettings.volume
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPSettings::volume property

The **volume** property gets or sets the current playback volume.

## Syntax


```CSharp
public System.Int32 volume {get; set;}
```


```VB

Public Property volume As System.Int32
```





## Property value

A **System.Int32** that is the volume level, ranging from 0 to 100.

## Remarks

A value of zero specifies no volume (muted). A value of 100 specifies full volume. If no value is specified for this property, it defaults to the last volume setting established for Windows Media Player.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPSettings Interface (VB and C#)**](iwmpsettings--vb-and-c.md)
</dt> </dl>

 

 





