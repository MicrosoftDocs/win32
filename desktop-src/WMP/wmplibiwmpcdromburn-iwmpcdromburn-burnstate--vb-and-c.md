---
title: IWMPCdromBurn burnState property
description: The burnState property gets an enumeration value that indicates the current burn state.
ms.assetid: 2bb543f9-9e4c-4425-99d6-ac89ef7f5807
keywords:
- burnState property Windows Media Player
- burnState property Windows Media Player , IWMPCdromBurn interface
- IWMPCdromBurn interface Windows Media Player , burnState property
topic_type:
- apiref
api_name:
- IWMPCdromBurn.burnState
- IWMPCdromBurn.get_burnState
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPCdromBurn::burnState property

The **burnState** property gets an enumeration value that indicates the current burn state.

This property is read-only.

## Syntax


```CSharp
public WMPBurnState burnState {get;}
```


```VB

Public ReadOnly Property burnState As WMPBurnState
```





## Property value

A **WMPLib.WMPBurnState** that is a value from the **WMPBurnState** enumeration that indicates the current state.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 11.<br/>                                                                                    |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPCdromBurn Interface (VB and C#)**](iwmpcdromburn--vb-and-c.md)
</dt> <dt>

[**WMPBurnState**](/previous-versions/windows/desktop/api/wmp/ne-wmp-wmpburnstate)
</dt> </dl>

 

 





