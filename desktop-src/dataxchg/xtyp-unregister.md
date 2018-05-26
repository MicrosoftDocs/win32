---
title: XTYP\_UNREGISTER transaction
description: A Dynamic Data Exchange (DDE) callback function, DdeCallback, receives the XTYP\_UNREGISTER transaction whenever a Dynamic Data Exchange Management Library (DDEML) server application uses the DdeNameService function to unregister a service name, or whenever a non-DDEML application that supports the System topic is terminated.
ms.assetid: a57a5d53-7919-4698-8c84-6142dd29bb2a
keywords:
- XTYP_UNREGISTER transaction Data Exchange
topic_type:
- apiref
api_name:
- XTYP_UNREGISTER
api_location:
- Ddeml.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# XTYP\_UNREGISTER transaction

A Dynamic Data Exchange (DDE) callback function, [*DdeCallback*](ddecallback.md), receives the **XTYP\_UNREGISTER** transaction whenever a Dynamic Data Exchange Management Library (DDEML) server application uses the [**DdeNameService**](/windows/win32/Ddeml/nf-ddeml-ddenameservice?branch=master) function to unregister a service name, or whenever a non-DDEML application that supports the System topic is terminated.


```C++
#define     XCLASS_NOTIFICATION      0x8000
#define     XTYPF_NOBLOCK            0x0002
#define     XTYP_UNREGISTER         (0x00D0 | XCLASS_NOTIFICATION | XTYPF_NOBLOCK)
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

Not used.

</dd> <dt>

*hsz1* 
</dt> <dd>

A handle to the base service name being unregistered.

</dd> <dt>

*hsz2* 
</dt> <dd>

A handle to the instance-specific service name being unregistered.

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

## Remarks

This transaction is filtered if the application specified the **CBF\_SKIP\_REGISTRATIONS** flag in the [**DdeInitialize**](/windows/win32/Ddeml/nf-ddeml-ddeinitializea?branch=master) function.

A application cannot block this transaction type; the CBR\_BLOCK return code is ignored.

An application should use the *hsz1* parameter to remove the service name from the list of servers available to the user. An application should use the *hsz2* parameter to identify which application instance has terminated.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                   |
| Header<br/>                   | <dl> <dt>Ddeml.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**DdeInitialize**](/windows/win32/Ddeml/nf-ddeml-ddeinitializea?branch=master)
</dt> <dt>

[**DdeNameService**](/windows/win32/Ddeml/nf-ddeml-ddenameservice?branch=master)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Dynamic Data Exchange Management Library](dynamic-data-exchange-management-library.md)
</dt> </dl>

 

 





