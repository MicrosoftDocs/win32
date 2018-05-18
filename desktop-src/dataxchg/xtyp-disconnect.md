---
title: XTYP\_DISCONNECT transaction
description: An application's Dynamic Data Exchange (DDE) callback function, DdeCallback, receives the XTYP\_DISCONNECT transaction when the application's partner in a conversation uses the DdeDisconnect function to terminate the conversation.
ms.assetid: '22a9ec63-8a74-4829-ad02-d07dd0e8fa9b'
keywords: ["XTYP_DISCONNECT transaction Data Exchange"]
topic_type:
- apiref
api_name:
- XTYP_DISCONNECT
api_location:
- Ddeml.h
api_type:
- HeaderDef
---

# XTYP\_DISCONNECT transaction

An application's Dynamic Data Exchange (DDE) callback function, [*DdeCallback*](ddecallback.md), receives the **XTYP\_DISCONNECT** transaction when the application's partner in a conversation uses the [**DdeDisconnect**](ddedisconnect.md) function to terminate the conversation.


```C++
#define     XCLASS_NOTIFICATION      0x8000
#define     XTYPF_NOBLOCK            0x0002
#define     XTYP_DISCONNECT         (0x00C0 | XCLASS_NOTIFICATION | XTYPF_NOBLOCK)
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

A handle to that the conversation was terminated.

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

Not used.

</dd> <dt>

*dwData2* 
</dt> <dd>

Specifies whether the partners in the conversation are the same application instance. If this parameter is 1, the partners are the same instance. If this parameter is 0, the partners are different instances.

</dd> </dl>

## Remarks

This transaction is filtered if the application specified the **CBF\_SKIP\_DISCONNECTS** flag in the [**DdeInitialize**](ddeinitialize.md) function.

The application can obtain the status of the terminated conversation by calling the [**DdeQueryConvInfo**](ddequeryconvinfo.md) function while processing this transaction. The conversation handle becomes invalid after the callback function returns.

An application cannot block this transaction type; the **CBR\_BLOCK** return code is ignored.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                   |
| Header<br/>                   | <dl> <dt>Ddeml.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**DdeDisconnect**](ddedisconnect.md)
</dt> <dt>

[**DdeInitialize**](ddeinitialize.md)
</dt> <dt>

[**DdeQueryConvInfo**](ddequeryconvinfo.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Dynamic Data Exchange Management Library](dynamic-data-exchange-management-library.md)
</dt> </dl>

 

 





