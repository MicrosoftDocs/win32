---
description: Associates an ITransactionProxy implementation with the current context.
ms.assetid: 64009632-b536-41fb-95ac-b23e2cbf18da
title: IContextTransactionInfo::RegisterTransactionProxy method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextTransactionInfo.RegisterTransactionProxy
api_type: 
- COM
api_location: 
---

# IContextTransactionInfo::RegisterTransactionProxy method

Associates an [**ITransactionProxy**](/windows/desktop/api/ComSvcs/nn-comsvcs-itransactionproxy) implementation with the current context.

## Syntax


```C++
HRESULT RegisterTransactionProxy(
  [in]  ITransactionProxy *pProxy,
  [out] GUID              *pGuid
);
```



## Parameters

<dl> <dt>

*pProxy* \[in\]
</dt> <dd>

An [**ITransactionProxy**](/windows/desktop/api/ComSvcs/nn-comsvcs-itransactionproxy) implementation to associate with the current context.

</dd> <dt>

*pGuid* \[out\]
</dt> <dd>

A GUID that identifies the transaction proxy. COM+ uses this GUID when calling [**ITransactionProxy::Commit**](/windows/desktop/api/ComSvcs/nf-comsvcs-itransactionproxy-commit) on the transaction proxy.

</dd> </dl>

## Return value

This method can return the standard return values E\_INVALIDARG, E\_OUTOFMEMORY, and E\_UNEXPECTED, as well as the following values.



| Return code                                                                                                     | Description                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                            | The method completed successfully.<br/>                                                                           |
| <dl> <dt>**CONTEXT\_E\_ALREADYINTRANSACTION**</dt> </dl> | The current context already has an associated [**ITransactionProxy**](/windows/desktop/api/ComSvcs/nn-comsvcs-itransactionproxy) implementation.<br/> |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>                       | The current context is hosting a Bring Your Own Transaction (BYOT) transaction or a non-root transaction.<br/>    |



 

## Remarks

The **RegisterTransactionProxy** method can only be called if the current context is a root transaction context. It cannot be called if the context is hosting a BYOT transaction or a non-root transaction.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**IContextTransactionInfo**](icontexttransactioninfo.md)
</dt> </dl>

 

 




