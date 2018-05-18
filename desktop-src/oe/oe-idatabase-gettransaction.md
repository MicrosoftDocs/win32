---
title: IDatabase GetTransaction method
description: Retrieves the specified transaction and the records associated with that transaction.
ms.assetid: 'baafeba5-203c-42f1-aa4a-49842ff25e6a'
keywords: ["GetTransaction method Windows Mail (formerly Outlook Express)", "GetTransaction method Windows Mail (formerly Outlook Express) , IDatabase interface", "IDatabase interface Windows Mail (formerly Outlook Express) , GetTransaction method"]
topic_type:
- apiref
api_name:
- IDatabase.GetTransaction
api_location:
- Directdb.dll
api_type:
- COM
---

# IDatabase::GetTransaction method

\[**GetTransaction** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves the specified transaction and the records associated with that transaction. Also will retrieve the HTRANSACTION of the next available transaction.

## Syntax


```C++
HRESULT GetTransaction(
  [in, out] LPHTRANSACTION     phTransaction,
  [out]     LPHTRANSACTIONTYPE ptyTransaction,
  [in]      LPVOID             pRecord1,
  [in]      LPVOID             pRecord2,
  [in, out] LPINDEXORDINAL     piIndex,
  [in]      LPORDINALLIST      pOrdinals
);
```



## Parameters

<dl> <dt>

*phTransaction* \[in, out\]
</dt> <dd>

Type: **LPHTRANSACTION**

Specifies the transaction to retrieve. On return, will contain the handle to the next transaction available.

</dd> <dt>

*ptyTransaction* \[out\]
</dt> <dd>

Type: **LPHTRANSACTIONTYPE**

Receives the transaction's type.

</dd> <dt>

*pRecord1* \[in\]
</dt> <dd>

Type: **LPVOID**

Optional. Receives the first record involved in the transaction.

</dd> <dt>

*pRecord2* \[in\]
</dt> <dd>

Type: **LPVOID**

Optional. Receives the second record involved in the transaction if there was one.

</dd> <dt>

*piIndex* \[in, out\]
</dt> <dd>

Type: **LPINDEXORDINAL**

Returns the index involved with this transaction.

</dd> <dt>

*pOrdinals* \[in\]
</dt> <dd>

Type: **LPORDINALLIST**

Returns the ordinals involved with this transaction.

</dd> </dl>

## Return value

Type: **HRESULT**

Use the SUCCEEDED macro to determine whether the operation succeeded.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





