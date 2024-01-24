---
title: IWMPMedia2 Error property
description: The Error property gets an IWMPErrorItem interface if the media item has an error condition.
ms.assetid: 57dc8aef-5f22-43da-87bc-fdc0c8ebe49b
keywords:
- Error property Windows Media Player
- Error property Windows Media Player , IWMPMedia2 interface
- IWMPMedia2 interface Windows Media Player , Error property
topic_type:
- apiref
api_name:
- IWMPMedia2.Error
- IWMPMedia2.get_Error
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPMedia2::Error property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **Error** property gets an **IWMPErrorItem** interface if the media item has an error condition.

This property is read-only.

## Syntax


```CSharp
public IWMPErrorItem Error {get;}
```


```VB

Public ReadOnly Property Error As IWMPErrorItem
```





## Property value

A **WMPLib.IWMPErrorItem** interface that provides access to information about the error condition.

## Remarks

If the media item cannot be played, this property gets an **IWMPErrorItem** interface that contains information about the problem encountered.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPErrorItem (VB and C#)**](iwmperroritem--vb-and-c.md)
</dt> <dt>

[**IWMPMedia2 Interface (VB and C#)**](iwmpmedia2--vb-and-c.md)
</dt> </dl>

 

 





