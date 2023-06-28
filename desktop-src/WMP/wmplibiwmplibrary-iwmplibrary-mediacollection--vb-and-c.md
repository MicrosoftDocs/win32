---
title: IWMPLibrary mediaCollection property
description: The mediaCollection property gets an IWMPMediaCollection interface for the current library.
ms.assetid: 6ac92b0d-d634-4e99-8946-b10363d4be47
keywords:
- mediaCollection property Windows Media Player
- mediaCollection property Windows Media Player , IWMPLibrary interface
- IWMPLibrary interface Windows Media Player , mediaCollection property
topic_type:
- apiref
api_name:
- IWMPLibrary.mediaCollection
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPLibrary::mediaCollection property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **mediaCollection** property gets an **IWMPMediaCollection** interface for the current library.

## Syntax


```CSharp
public IWMPMediaCollection mediaCollection {get; set;}
```


```VB

Public ReadOnly Property mediaCollection As IWMPMediaCollection
```





## Property value

A WMPLib.IWMPMediaCollection interface for the current library.

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

[**IWMPMediaCollection Interface (VB and C#)**](iwmpmediacollection--vb-and-c.md)
</dt> </dl>

 

 





