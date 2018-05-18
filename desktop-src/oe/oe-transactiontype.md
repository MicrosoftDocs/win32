---
title: TRANSACTIONTYPE enumeration
description: Do not use. Specifies how a transaction affected the database.
ms.assetid: 'b818022b-d55a-45e5-a2c9-40ab62fc49ba'
keywords: ["TRANSACTIONTYPE enumeration Windows Mail (formerly Outlook Express)", "ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Directdb.idl
api_type:
- IDLDef
---

# TRANSACTIONTYPE enumeration

Do not use. Specifies how a transaction affected the database.

## Syntax


```C++
typedef enum  { 
  TRANSACTION_INSERT,
  TRANSACTION_UPDATE,
  TRANSACTION_DELETE,
  TRANSACTION_INDEX_CHANGED,
  TRANSACTION_INDEX_DELETED,
  TRANSACTION_COMPACTED
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="TRANSACTION_INSERT"></span><span id="transaction_insert"></span>**TRANSACTION\_INSERT**
</dt> <dd>

A new record was inserted into the database.

</dd> <dt>

<span id="TRANSACTION_UPDATE"></span><span id="transaction_update"></span>**TRANSACTION\_UPDATE**
</dt> <dd>

A record of the database was modified.

</dd> <dt>

<span id="TRANSACTION_DELETE"></span><span id="transaction_delete"></span>**TRANSACTION\_DELETE**
</dt> <dd>

A record of the database was deleted.

</dd> <dt>

<span id="TRANSACTION_INDEX_CHANGED"></span><span id="transaction_index_changed"></span>**TRANSACTION\_INDEX\_CHANGED**
</dt> <dd>

A database index was modified.

</dd> <dt>

<span id="TRANSACTION_INDEX_DELETED"></span><span id="transaction_index_deleted"></span>**TRANSACTION\_INDEX\_DELETED**
</dt> <dd>

A database index was deleted.

</dd> <dt>

<span id="TRANSACTION_COMPACTED"></span><span id="transaction_compacted"></span>**TRANSACTION\_COMPACTED**
</dt> <dd>

The database was compacted.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl> |



 

 





