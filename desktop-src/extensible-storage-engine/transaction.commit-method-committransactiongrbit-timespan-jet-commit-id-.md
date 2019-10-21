---
title: Transaction.Commit method (CommitTransactionGrbit, TimeSpan, JET_COMMIT_ID)
TOCTitle: Commit method (CommitTransactionGrbit, TimeSpan, JET_COMMIT_ID)
ms:assetid: M:Microsoft.Isam.Esent.Interop.Transaction.Commit(Microsoft.Isam.Esent.Interop.CommitTransactionGrbit,System.TimeSpan,Microsoft.Isam.Esent.Interop.Windows8.JET_COMMIT_ID@)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.transaction.commit(v=EXCHG.10)
ms:contentKeyID: 55104166
ms.date: 07/30/2014
ms.topic: article
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.Transaction.Commit
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Transaction.Commit method (CommitTransactionGrbit, TimeSpan, JET_COMMIT_ID)

Commit a transaction. This object should be in a transaction.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Sub Commit ( _
    grbit As CommitTransactionGrbit, _
    durableCommit As TimeSpan, _
    <OutAttribute> ByRef commitId As JET_COMMIT_ID _
)
'Usage
Dim instance As Transaction
Dim grbit As CommitTransactionGrbit
Dim durableCommit As TimeSpan
Dim commitId As JET_COMMIT_ID

instance.Commit(grbit, durableCommit, _
    commitId)
```

``` csharp
public void Commit(
    CommitTransactionGrbit grbit,
    TimeSpan durableCommit,
    out JET_COMMIT_ID commitId
)
```

#### Parameters

  - grbit  
    Type: [Microsoft.Isam.Esent.Interop.CommitTransactionGrbit](hh564415\(v=exchg.10\).md)  
    
    JetCommitTransaction options.

<!-- end list -->

  - durableCommit  
    Type: [System.TimeSpan](https://docs.microsoft.com/dotnet/api/system.timespan?redirectedfrom=MSDN)  
    
    Duration for committing lazy transactions.

<!-- end list -->

  - commitId  
    Type: [Microsoft.Isam.Esent.Interop.Windows8.JET_COMMIT_ID](dn335448\(v=exchg.10\).md)  
    
    Commit-id for this commit record.

## See also

#### Reference

[Transaction class](dn351174\(v=exchg.10\).md)

[Transaction members](dn351240\(v=exchg.10\).md)

[Commit overload](dn351242\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

