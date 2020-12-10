---
title: XTYP_REQUEST transaction (Ddeml.h)
description: A client uses the XTYP\_REQUEST transaction to request data from a server. A Dynamic Data Exchange (DDE) server callback function, DdeCallback, receives this transaction when a client specifies XTYP\_REQUEST in the DdeClientTransaction function.
ms.assetid: e776b995-6a64-4398-9e29-c151f3ef4c1d
keywords:
- XTYP_REQUEST transaction Data Exchange
topic_type:
- apiref
api_name:
- XTYP_REQUEST
api_location:
- Ddeml.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# XTYP\_REQUEST transaction

A client uses the **XTYP\_REQUEST** transaction to request data from a server. A Dynamic Data Exchange (DDE) server callback function, [*DdeCallback*](/windows/win32/api/ddeml/nc-ddeml-pfncallback), receives this transaction when a client specifies **XTYP\_REQUEST** in the [**DdeClientTransaction**](/windows/desktop/api/Ddeml/nf-ddeml-ddeclienttransaction) function.


```C++
#define     XCLASS_DATA              0x2000
#define     XTYP_REQUEST            (0x00B0 | XCLASS_DATA          )
```



## Parameters

<dl> <dt>

*uType* 
</dt> <dd>

The transaction type.

</dd> <dt>

*uFmt* 
</dt> <dd>

The format in which the server should submit data to the client.

</dd> <dt>

*hconv* 
</dt> <dd>

A handle to the conversation.

</dd> <dt>

*hsz1* 
</dt> <dd>

A handle to the topic name.

</dd> <dt>

*hsz2* 
</dt> <dd>

A handle to the item name.

</dd> <dt>

*hdata* 
</dt> <dd>

Not used.

</dd> <dt>

*dwData1* 
</dt> <dd>

Not used.

</dd> <dt>

*dwData2* 
</dt> <dd>

Not used.

</dd> </dl>

## Return value

The server should call the [**DdeCreateDataHandle**](/windows/desktop/api/Ddeml/nf-ddeml-ddecreatedatahandle) function to create a data handle that identifies the data and then return the handle. The server should return **NULL** if it is unable to complete the transaction. If the server returns **NULL**, the client will receive a DDE\_FNOTPROCESSED flag.

## Remarks

This transaction is filtered if the server application specified the **CBF\_FAIL\_REQUESTS** flag in the [**DdeInitialize**](/windows/desktop/api/Ddeml/nf-ddeml-ddeinitializea) function.

If responding to this transaction requires lengthy processing, the server can return the CBR\_BLOCK return code to suspend future transactions on the current conversation and then process the transaction asynchronously. When the server has finished and the data is ready to pass to the client, the server can call the [**DdeEnableCallback**](/windows/desktop/api/Ddeml/nf-ddeml-ddeenablecallback) function to resume the conversation.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                   |
| Header<br/>                   | <dl> <dt>Ddeml.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**DdeClientTransaction**](/windows/desktop/api/Ddeml/nf-ddeml-ddeclienttransaction)
</dt> <dt>

[**DdeCreateDataHandle**](/windows/desktop/api/Ddeml/nf-ddeml-ddecreatedatahandle)
</dt> <dt>

[**DdeEnableCallback**](/windows/desktop/api/Ddeml/nf-ddeml-ddeenablecallback)
</dt> <dt>

[**DdeInitialize**](/windows/desktop/api/Ddeml/nf-ddeml-ddeinitializea)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Dynamic Data Exchange Management Library](dynamic-data-exchange-management-library.md)
</dt> </dl>

 

