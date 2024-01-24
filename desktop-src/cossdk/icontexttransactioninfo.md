---
description: Provides access to context object properties that relate to transactions.
ms.assetid: 3b309153-be7d-444e-be23-777887f1ee95
title: IContextTransactionInfo interface
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextTransactionInfo
api_type: 
- COM
api_location: 
---

# IContextTransactionInfo interface

Provides access to context object properties that relate to transactions.

## When to implement

You should not implement this interface. The standard implementation provides complete functionality.

## When to use

Use this interface to access context object properties that relate to transactions.

## Members

The **IContextTransactionInfo** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IContextTransactionInfo** also has these types of members:

-   [Methods](#methods)

### Methods

The **IContextTransactionInfo** interface has these methods.



| Method                                                                                         | Description                                                                                                                 |
|:-----------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------|
| [**FetchTransaction**](icontexttransactioninfo-registertransactionproxy.md)                   | Retrieves the transaction or transaction proxy that is associated with the current context, if any.<br/>              |
| [**GetTxIsolationLevelAndTimeout**](icontexttransactioninfo-gettxisolationlevelandtimeout.md) | Retrieves the isolation level and timeout value of a transaction that is hosted in the root transaction context.<br/> |
| [**RegisterTransactionProxy**](icontexttransactioninfo-fetchtransaction.md)                   | Associates an [**ITransactionProxy**](/windows/desktop/api/ComSvcs/nn-comsvcs-itransactionproxy) implementation with the current context.<br/>            |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/> |



 

