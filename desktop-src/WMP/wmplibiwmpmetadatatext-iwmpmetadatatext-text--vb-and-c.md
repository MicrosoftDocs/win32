---
title: IWMPMetadataText text property
description: The text property gets the metadata text.
ms.assetid: 9e91178a-219a-4b0c-a410-9b4feb84e9e3
keywords:
- text property Windows Media Player
- text property Windows Media Player , IWMPMetadataText interface
- IWMPMetadataText interface Windows Media Player , text property
topic_type:
- apiref
api_name:
- IWMPMetadataText.text
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPMetadataText::text property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `text` property gets the metadata text.

## Syntax


```CSharp
public System.String text {get; set;}
```


```VB

Public ReadOnly Property text As System.String
```





## Property value

A **System.String** that is the metadata text.

## Remarks

Before using this property, you must have read access to the library. For more information, see [Library Access](library-access.md).

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPMetadataText Interface (VB and C#)**](iwmpmetadatatext--vb-and-c.md)
</dt> </dl>

 

 





