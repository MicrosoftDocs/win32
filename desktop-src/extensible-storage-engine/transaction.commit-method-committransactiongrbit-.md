---
title: Transaction.Commit method (CommitTransactionGrbit)
TOCTitle: Commit method (CommitTransactionGrbit)
ms:assetid: M:Microsoft.Isam.Esent.Interop.Transaction.Commit(Microsoft.Isam.Esent.Interop.CommitTransactionGrbit)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.transaction.commit(v=EXCHG.10)
ms:contentKeyID: 55104071
ms.date: 07/30/2014
ms.topic: reference
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.Transaction.Commit
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Transaction.Commit method (CommitTransactionGrbit)

Commit a transaction. This object should be in a transaction.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Sub Commit ( _
    grbit As CommitTransactionGrbit _
)
'Usage
Dim instance As Transaction
Dim grbit As CommitTransactionGrbit

instance.Commit(grbit)
```

``` csharp
public void Commit(
    CommitTransactionGrbit grbit
)
```

#### Parameters

  - grbit  
    Type: [Microsoft.Isam.Esent.Interop.CommitTransactionGrbit](hh564415\(v=exchg.10\).md)  
    
    JetCommitTransaction options.

## See also

#### Reference

[Transaction class](dn351174\(v=exchg.10\).md)

[Transaction members](dn351240\(v=exchg.10\).md)

[Commit overload](dn351242\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

