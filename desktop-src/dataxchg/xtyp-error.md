---
title: XTYP_ERROR transaction (Ddeml.h)
description: A Dynamic Data Exchange (DDE) callback function, DdeCallback, receives the XTYP\_ERROR transaction when a critical error occurs.
ms.assetid: 710daa04-ed83-42e3-a55e-6ccf891a3d52
keywords:
- XTYP_ERROR transaction Data Exchange
topic_type:
- apiref
api_name:
- XTYP_ERROR
api_location:
- Ddeml.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# XTYP\_ERROR transaction

A Dynamic Data Exchange (DDE) callback function, [*DdeCallback*](/windows/win32/api/ddeml/nc-ddeml-pfncallback), receives the **XTYP\_ERROR** transaction when a critical error occurs.


```C++
#define     XCLASS_NOTIFICATION      0x8000
#define     XTYPF_NOBLOCK            0x0002
#define     XTYP_ERROR              (0x0000 | XCLASS_NOTIFICATION | XTYPF_NOBLOCK )
```



## Parameters

<dl> <dt>

*uType* 
</dt> <dd>

The transaction type.

</dd> <dt>

*uFmt* 
</dt> <dd>

Not used.

</dd> <dt>

*hconv* 
</dt> <dd>

A handle to the conversation associated with the error. This parameter is **NULL** if the error is not associated with a conversation.

</dd> <dt>

*hsz1* 
</dt> <dd>

Not used.

</dd> <dt>

*hsz2* 
</dt> <dd>

Not used.

</dd> <dt>

*hdata* 
</dt> <dd>

Not used.

</dd> <dt>

*dwData1* 
</dt> <dd>

The error code in the low-order word. Currently, only the following error code is supported.



| Value                                                                                                                                                                      | Meaning                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| <span id="DMLERR_LOW_MEMORY"></span><span id="dmlerr_low_memory"></span><dl> <dt>**DMLERR\_LOW\_MEMORY**</dt> </dl> | Memory is low; advise, poke, or execute data may be lost, or the system may fail.<br/> |



 

</dd> <dt>

*dwData2* 
</dt> <dd>

Not used.

</dd> </dl>

## Remarks

An application cannot block this transaction type; the **CBR\_BLOCK** return code is ignored. The Dynamic Data Exchange Management Library (DDEML) attempts to free memory by removing noncritical resources. An application that has blocked conversations should unblock them.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                   |
| Header<br/>                   | <dl> <dt>Ddeml.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Dynamic Data Exchange Management Library Overview](dynamic-data-exchange-management-library.md)
</dt> </dl>

 

