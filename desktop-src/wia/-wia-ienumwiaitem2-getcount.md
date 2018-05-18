---
Description: 'Returns the number of elements stored by this enumerator.'
ms.assetid: 'd374ec81-0bd5-4b5d-8002-e3b53476421a'
title: 'IEnumWiaItem2::GetCount method'
---

# IEnumWiaItem2::GetCount method

Returns the number of elements stored by this enumerator.

## Syntax


```C++
HRESULT GetCount(
  [out] ULONG *cElt
);
```



## Parameters

<dl> <dt>

*cElt* \[out\]
</dt> <dd>

Type: **ULONG\***

Receives a pointer to a **ULONG** that receives the number of elements in the enumeration.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl> |



 

 




