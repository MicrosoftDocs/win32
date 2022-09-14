---
title: IWMPCdromBurn burnProgress property
description: The burnProgress property gets the CD burning progress as percent complete.
ms.assetid: 831cc55d-bd26-4328-a715-1a1fa48d7a40
keywords:
- burnProgress property Windows Media Player
- burnProgress property Windows Media Player , IWMPCdromBurn interface
- IWMPCdromBurn interface Windows Media Player , burnProgress property
topic_type:
- apiref
api_name:
- IWMPCdromBurn.burnProgress
- IWMPCdromBurn.get_burnProgress
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPCdromBurn::burnProgress property

The **burnProgress** property gets the CD burning progress as percent complete.

This property is read-only.

## Syntax


```CSharp
public System.Int32 burnProgress {get;}
```


```VB

Public ReadOnly Property burnProgress As System.Int32
```





## Property value

A **System.Int32** that is the progress value. Progress values range from 0 to 100.

## Remarks

The progress value represents the completed percentage of the entire burning process, including any staging operations.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 11<br/>                                                                                     |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPCdromBurn Interface (VB and C#)**](iwmpcdromburn--vb-and-c.md)
</dt> </dl>

 

 





