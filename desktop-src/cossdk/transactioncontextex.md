---
description: Creates a generic transactional object that begins a transaction. By calling the methods of this class, you can compose the work of multiple COM objects in a single transaction and explicitly commit or abort the transaction.
ms.assetid: '5f3f83e0-33fc-4c43-9327-59485c0d8bd3'
title: TransactionContextEx class (ComSvcs.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TransactionContextEx
api_type: 
- COM
---

# TransactionContextEx class

Creates a generic transactional object that begins a transaction. By calling the methods of this class, you can compose the work of multiple COM objects in a single transaction and explicitly commit or abort the transaction.

## When to implement

This class is implemented by COM+.



| Requirement | Value |
|------------|--------------------------------------------------------|
| CLSID      | CLSID\_TransactionContextEx                            |
| ProgID     | L"TxCTx.TransactionContextEx"                          |
| Interfaces | [**ITransactionContextEx**](/windows/desktop/api/ComSvcs/nn-comsvcs-itransactioncontextex) |



 

## When to use

A non-transactional client uses this class to begin a transaction. Using the methods of this class, the client can call additional COM objects that, if configured to participate in a transaction, run within the transaction boundary of the transaction context object. Based on its business logic, the client can explicitly commit or abort the transaction.

The **TransactionContextEx** class limits reuse of the business logic driving the transaction. For this reason, it is recommended that objects instantiated from the **TransactionContextEx** class be used sparingly.

## Remarks

To create this object, call [**IObjectContext::CreateInstance**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-createinstance).

The **TransactionContextEx** class was not designed to be used in Visual Basic. Use the [**TransactionContext**](transactioncontext.md) class instead.

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

[**ITransactionContextEx**](/windows/desktop/api/ComSvcs/nn-comsvcs-itransactioncontextex)
</dt> <dt>

[**TransactionContext**](transactioncontext.md)
</dt> </dl>

 

 




