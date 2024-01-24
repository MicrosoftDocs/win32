---
title: XTYP_XACT_COMPLETE transaction (Ddeml.h)
description: A Dynamic Data Exchange (DDE) client callback function, DdeCallback, receives the XTYP\_XACT\_COMPLETE transaction when an asynchronous transaction, initiated by a call to the DdeClientTransaction function, has completed.
ms.assetid: d34a6fab-0e3c-44fe-b25f-7011228fe261
keywords:
- XTYP_XACT_COMPLETE transaction Data Exchange
topic_type:
- apiref
api_name:
- XTYP_XACT_COMPLETE
api_location:
- Ddeml.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# XTYP\_XACT\_COMPLETE transaction

A Dynamic Data Exchange (DDE) client callback function, [*DdeCallback*](/windows/win32/api/ddeml/nc-ddeml-pfncallback), receives the **XTYP\_XACT\_COMPLETE** transaction when an asynchronous transaction, initiated by a call to the [**DdeClientTransaction**](/windows/desktop/api/Ddeml/nf-ddeml-ddeclienttransaction) function, has completed.


```C++
#define     XCLASS_NOTIFICATION      0x8000
#define     XTYP_XACT_COMPLETE      (0x0080 | XCLASS_NOTIFICATION  )
```



## Parameters

<dl> <dt>

*uType* 
</dt> <dd>

The transaction type.

</dd> <dt>

*uFmt* 
</dt> <dd>

The format of the data associated with the completed transaction (if applicable) or **NULL** if no data was exchanged during the transaction.

</dd> <dt>

*hconv* 
</dt> <dd>

A handle to the conversation.

</dd> <dt>

*hsz1* 
</dt> <dd>

A handle to the topic name involved in the completed transaction.

</dd> <dt>

*hsz2* 
</dt> <dd>

A handle to the item name involved in the completed transaction.

</dd> <dt>

*hdata* 
</dt> <dd>

A handle to the data involved in the completed transaction, if applicable. If the transaction was successful but involved no data, this parameter is **TRUE**. This parameter is **NULL** if the transaction was unsuccessful.

</dd> <dt>

*dwData1* 
</dt> <dd>

The transaction identifier of the completed transaction.

</dd> <dt>

*dwData2* 
</dt> <dd>

Any applicable **DDE\_** status flags in the low word. This parameter provides support for applications dependent on **DDE\_APPSTATUS** bits. It is recommended that applications no longer use these bits   they may not be supported in future versions of the DDEML.

</dd> </dl>

## Remarks

An application must not free the data handle obtained during this transaction. An application must, however, copy the data associated with the data handle if the application must process the data after the callback function returns. An application can use the [**DdeGetData**](/windows/desktop/api/Ddeml/nf-ddeml-ddegetdata) function to copy the data.

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

[**DdeGetData**](/windows/desktop/api/Ddeml/nf-ddeml-ddegetdata)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Dynamic Data Exchange Management Library](dynamic-data-exchange-management-library.md)
</dt> </dl>

 

