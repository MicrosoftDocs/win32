---
description: Releases a PCCERT\_CHAIN\_CONTEXT acquired through the ChainContext property.
ms.assetid: fa9a6171-58ff-400f-bdcc-ba32a0ae0441
title: IChainContext::FreeContext method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IChainContext.FreeContext
- ChainContext.FreeContext
api_type: 
- COM
api_location: 
- Capicom.dll
---

# IChainContext::FreeContext method

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP.\]

The **FreeContext** method releases a PCCERT\_CHAIN\_CONTEXT acquired through the [**ChainContext**](ichaincontext-chaincontext.md) property.

## Syntax


```VB
ChainContext.FreeContext()
```



## Parameters

<dl> <dt>

*pChainContext* \[in\]
</dt> <dd>

The PCCERT\_CHAIN\_CONTEXT to be released.

</dd> </dl>

## Return value

The return value is an **HRESULT**. A value of S\_OK indicates success. Any other value indicates that the operation failed.

## Remarks

This method does not release the PCCERT\_CHAIN\_CONTEXT contained within a [**Chain**](chain.md) object. It should be used only to release a PCCERT\_CHAIN\_CONTEXT acquired through the [**ChainContext**](ichaincontext-chaincontext.md) property.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**IChainContext**](ichaincontext.md)
</dt> </dl>

 

 




