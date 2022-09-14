---
title: IWMPCdromBurn erase method
description: The erase method erases the current CD.
ms.assetid: ed0fbd7e-61a6-445a-bca5-ed2969d5cadc
keywords:
- erase method Windows Media Player
- erase method Windows Media Player , IWMPCdromBurn interface
- IWMPCdromBurn interface Windows Media Player , erase method
topic_type:
- apiref
api_name:
- IWMPCdromBurn.erase
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPCdromBurn::erase method

The **erase** method erases the current CD.

## Syntax


```CSharp
public void erase();
```


```VB

Public Sub erase()
Implements IWMPCdromBurn.erase
```





## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This method will not work if the disc in the drive is not rewritable. Use [IWMPCdromBurn.isAvailable](wmplibiwmpcdromburn-iwmpcdromburn-isavailable--vb-and-c.md) to determine whether a CD can be erased.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 11.<br/>                                                                                    |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPCdromBurn Interface (VB and C#)**](iwmpcdromburn--vb-and-c.md)
</dt> </dl>

 

 





