---
title: IWMPErrorItem errorContext property
description: The errorContext property gets a value indicating the context of the error.
ms.assetid: e9ebd636-e611-49c6-9533-a02ff74db7bc
keywords:
- errorContext property Windows Media Player
- errorContext property Windows Media Player , IWMPErrorItem interface
- IWMPErrorItem interface Windows Media Player , errorContext property
topic_type:
- apiref
api_name:
- IWMPErrorItem.errorContext
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPErrorItem::errorContext property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **errorContext** property gets a value indicating the context of the error.

## Syntax


```CSharp
public System.Object errorContext {get; set;}
```


```VB

Public ReadOnly Property errorContext As System.Object
```





## Property value

A **System.Object** that is the error context.

## Remarks

The error context is information that is used by Microsoft to provide additional information for technical support personnel.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPErrorItem Interface (VB and C#)**](iwmperroritem--vb-and-c.md)
</dt> </dl>

 

 





