---
description: Creates a generic transactional object that begins a transaction.
ms.assetid: 'efaf1468-4973-472f-af91-85957a52b7df'
title: TransactionContext class (ComSvcs.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TransactionContext
api_type: 
- COM
---

# TransactionContext class

Creates a generic transactional object that begins a transaction. By calling the methods of this class, you can compose the work of multiple COM objects in a single transaction and explicitly commit or abort the transaction.

## When to implement

This class is implemented by COM+.



| Requirement | Value |
|------------|----------------------------------------------------|
| CLSID      | CLSID\_TransactionContext                          |
| ProgID     | L"TxCTx.TransactionContext"                        |
| Interfaces | [**ITransactionContext**](/windows/desktop/api/ComSvcs/nn-comsvcs-itransactioncontext) |



 

## When to use

A non-transactional client uses this class to begin a transaction. Using the methods of this class, the client can call additional COM objects that, if configured to participate in a transaction, run within the transaction boundary of the transaction context object. Based on its business logic, the client can explicitly commit or abort the transaction.

The **TransactionContext** class limits reuse of the business logic driving the transaction. For this reason, it is recommended that objects instantiated from the **TransactionContext** class be used sparingly.

## Remarks

To create this object, call [**IObjectContext::CreateInstance**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-createinstance).

To use this class from Microsoft Visual Basic, add a reference to the COM+ Services Type Library. A TransactionContext object can be declared using "COMSVCSLib.TransactionContext" as the class name.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>ComSvcs.h</dt> </dl> |



## See also

<dl> <dt>

[Configuring Transactions](configuring-transactions.md)
</dt> <dt>

[**ITransactionContext**](/windows/desktop/api/ComSvcs/nn-comsvcs-itransactioncontext)
</dt> <dt>

[**TransactionContextEx**](transactioncontextex.md)
</dt> </dl>

 

 




