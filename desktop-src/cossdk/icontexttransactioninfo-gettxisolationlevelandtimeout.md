---
description: Retrieves the isolation level and timeout value of a transaction that is hosted in the root transaction context.
ms.assetid: bb3ff03e-e69e-4a50-af36-4938eb4323df
title: IContextTransactionInfo::GetTxIsolationLevelAndTimeout method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextTransactionInfo.GetTxIsolationLevelAndTimeout
api_type: 
- COM
api_location: 
---

# IContextTransactionInfo::GetTxIsolationLevelAndTimeout method

Retrieves the isolation level and timeout value of a transaction that is hosted in the root transaction context.

## Syntax


```C++
HRESULT GetTxIsolationLevelAndTimeout(
  [out] ISOLEVEL *pIsoLevel,
  [out] DWORD    *dwTime
);
```



## Parameters

<dl> <dt>

*pIsoLevel* \[out\]
</dt> <dd>

The [ISOLATIONLEVEL](/previous-versions/windows/desktop/ms679234(v=vs.85)) value for the transaction.

</dd> <dt>

*dwTime* \[out\]
</dt> <dd>

The timeout of the transaction, in seconds.

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

 

