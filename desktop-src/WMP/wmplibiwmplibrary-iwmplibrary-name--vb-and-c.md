---
title: IWMPLibrary name property
description: The name property gets the display name of the current library.
ms.assetid: 28d8836e-fa97-4b52-9d3c-a368cb442d1a
keywords:
- name property Windows Media Player
- name property Windows Media Player , IWMPLibrary interface
- IWMPLibrary interface Windows Media Player , name property
topic_type:
- apiref
api_name:
- IWMPLibrary.name
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPLibrary::name property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **name** property gets the display name of the current library.

## Syntax


```CSharp
public System.String name {get; set;}
```


```VB

Public ReadOnly Property name As System.String
```





## Property value

A **System.String** that is the name of the current library.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 11.<br/>                                                                                    |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPLibrary Interface (VB and C#)**](iwmplibrary--vb-and-c.md)
</dt> <dt>

[**IWMPLibrary.type (VB and C#)**](wmplibiwmplibrary-iwmplibrary-type--vb-and-c.md)
</dt> </dl>

 

 





