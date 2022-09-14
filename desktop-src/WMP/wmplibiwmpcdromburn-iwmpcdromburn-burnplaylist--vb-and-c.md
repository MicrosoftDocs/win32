---
title: IWMPCdromBurn burnPlaylist property
description: The burnPlaylist property gets the current playlist to burn to the CD.
ms.assetid: 973032de-7249-4ccd-9909-ccc888f4490f
keywords:
- burnPlaylist property Windows Media Player
- burnPlaylist property Windows Media Player , IWMPCdromBurn interface
- IWMPCdromBurn interface Windows Media Player , burnPlaylist property
topic_type:
- apiref
api_name:
- IWMPCdromBurn.burnPlaylist
- IWMPCdromBurn.get_burnPlaylist
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPCdromBurn::burnPlaylist property

The **burnPlaylist** property gets the current playlist to burn to the CD.

This property is read-only.

## Syntax


```CSharp
public IWMPPlaylist burnPlaylist {get;}
```


```VB

Public ReadOnly Property burnPlaylist As IWMPPlaylist
```





## Property value

The **WMPLib.IWMPPlaylist** interface of the playlist to burn.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 11<br/>                                                                                     |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPCdromBurn Interface (VB and C#)**](iwmpcdromburn--vb-and-c.md)
</dt> <dt>

[**IWMPPlaylist Interface (VB and C#)**](iwmpplaylist--vb-and-c.md)
</dt> </dl>

 

 





