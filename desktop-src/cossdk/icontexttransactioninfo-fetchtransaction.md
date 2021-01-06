---
description: Retrieves the transaction or transaction proxy that is associated with the current context, if any.
ms.assetid: 2f85f395-3ec5-4c5a-a6db-c902cb8f8486
title: IContextTransactionInfo::FetchTransaction method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextTransactionInfo.FetchTransaction
api_type: 
- COM
api_location: 
---

# IContextTransactionInfo::FetchTransaction method

Retrieves the transaction or transaction proxy that is associated with the current context, if any.

## Syntax


```C++
HRESULT FetchTransaction(
  [out, retval] IUnknown **pUnk
);
```



## Parameters

<dl> <dt>

*pUnk* \[out, retval\]
</dt> <dd>

The transaction or transaction proxy that is associated with the current context; otherwise, **NULL**.

</dd> </dl>

## Return value

This method can return the standard return values E\_INVALIDARG, E\_OUTOFMEMORY, E\_UNEXPECTED, and S\_OK.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**IContextTransactionInfo**](icontexttransactioninfo.md)
</dt> </dl>

 

 




