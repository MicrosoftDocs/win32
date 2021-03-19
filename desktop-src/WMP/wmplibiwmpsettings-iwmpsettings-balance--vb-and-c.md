---
title: IWMPSettings balance property
description: The balance property gets or sets the current stereo balance.
ms.assetid: 6b9b6305-3bab-418d-a172-d47ca4dbaba5
keywords:
- balance property Windows Media Player
- balance property Windows Media Player , IWMPSettings interface
- IWMPSettings interface Windows Media Player , balance property
topic_type:
- apiref
api_name:
- IWMPSettings.balance
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPSettings::balance property

The **balance** property gets or sets the current stereo balance.

## Syntax


```CSharp
public System.Int32 balance {get; set;}
```


```VB

Public Property balance As System.Int32
```





## Property value

A **System.Int32** that is the balance value. This value can range from  100 to 100. The default value is zero.

## Remarks

The value zero indicates that the audio plays at equal volume on both left and right channels. A value of  100 indicates that audio plays only on the left channel. A value of 100 indicates that audio plays only on the right channel.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later.<br/>                                                                     |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPSettings Interface (VB and C#)**](iwmpsettings--vb-and-c.md)
</dt> </dl>

 

 





