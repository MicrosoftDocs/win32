---
description: Creates an additional instance of the IEnumWiaItem2 interface and sends back a pointer to it.
ms.assetid: 0d36d555-d0d9-4a1c-ac54-de611850449c
title: IEnumWiaItem2::Clone method (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IEnumWiaItem2.Clone
api_type: 
- COM
api_location: 
- Wia.h
---

# IEnumWiaItem2::Clone method

Creates an additional instance of the [**IEnumWiaItem2**](-wia-ienumwiaitem2.md) interface and sends back a pointer to it.

## Syntax


```C++
HRESULT Clone(
  [out] IEnumWiaItem2 **ppIEnum
);
```



## Parameters

<dl> <dt>

*ppIEnum* \[out\]
</dt> <dd>

Type: **[**IEnumWiaItem2**](-wia-ienumwiaitem2.md)\*\***

Receives the address of the [**IEnumWiaItem2**](-wia-ienumwiaitem2.md) interface instance that **IEnumWiaItem2::Clone** creates.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Applications must call the [IUnknown::Release](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) method on the interface pointers they receive through the *ppIEnum* parameter.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl> |



 

 
