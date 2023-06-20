---
title: IWMPErrorItem2 condition property
description: The condition property gets a value indicating the condition for the error.
ms.assetid: 68800d75-8341-40d1-b699-ffe27bb1f38a
keywords:
- condition property Windows Media Player
- condition property Windows Media Player , IWMPErrorItem2 interface
- IWMPErrorItem2 interface Windows Media Player , condition property
topic_type:
- apiref
api_name:
- IWMPErrorItem2.condition
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPErrorItem2::condition property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **condition** property gets a value indicating the condition for the error.

## Syntax


```CSharp
public System.Int32 condition {get; set;}
```


```VB

Public ReadOnly Property condition As System.Int32
```





## Property value

A **System.Int32** that is the condition code.

## Remarks

The condition code is a value that is used by Microsoft to provide additional information for technical support personnel.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPErrorItem2 Interface (VB and C#)**](iwmperroritem2--vb-and-c.md)
</dt> </dl>

 

 





