---
title: IWMPLibrary type property
description: The type property gets a value that indicates the library type.
ms.assetid: 869eab74-e793-4b04-b634-079feac8cf7b
keywords:
- type property Windows Media Player
- type property Windows Media Player , IWMPLibrary interface
- IWMPLibrary interface Windows Media Player , type property
topic_type:
- apiref
api_name:
- IWMPLibrary.type
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPLibrary::type property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **type** property gets a value that indicates the library type.

## Syntax


```CSharp
public WMPLibraryType type {get; set;}
```


```VB

Public ReadOnly Property type As WMPLibraryType
```





## Property value

A **WMPLib.WMPLibraryType** that is a value from the **WMPLibraryType** enumeration that indicates the library type.

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

[**IWMPLibrary.name (VB and C#)**](wmplibiwmplibrary-iwmplibrary-name--vb-and-c.md)
</dt> <dt>

[**WMPLibraryType**](/previous-versions/windows/desktop/api/wmp/ne-wmp-wmplibrarytype)
</dt> </dl>

 

 





