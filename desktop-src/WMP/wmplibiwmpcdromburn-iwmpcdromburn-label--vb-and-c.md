---
title: IWMPCdromBurn label property
description: The label property gets the CD volume label string.
ms.assetid: 46e7741c-59c5-46d8-b9ca-09892d907cd7
keywords:
- label property Windows Media Player
- label property Windows Media Player , IWMPCdromBurn interface
- IWMPCdromBurn interface Windows Media Player , label property
topic_type:
- apiref
api_name:
- IWMPCdromBurn.label
- IWMPCdromBurn.get_label
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPCdromBurn::label property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The *label* property gets the CD volume label string.

This property is read-only.

## Syntax


```CSharp
public System.String label {get;}
```


```VB

Public ReadOnly Property label As System.String
```





## Property value

A **System.String** that is the volume label string.

## Remarks

Due to the way CD labels are stored, the label of the CD may be shorter than the length of the specified volume label string. If the string is longer than the maximum length of a CD label, the text will be truncated.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 11.<br/>                                                                                    |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPCdromBurn Interface (VB and C#)**](iwmpcdromburn--vb-and-c.md)
</dt> </dl>

 

 





