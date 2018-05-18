---
title: XTYP\_WILDCONNECT transaction
description: Enables a client to establish a conversation on each of the server's service name and topic name pairs that match the specified service name and topic name.
ms.assetid: '4651e14f-ca13-412e-853d-326a13db78e4'
keywords: ["XTYP_WILDCONNECT transaction Data Exchange"]
topic_type:
- apiref
api_name:
- XTYP_WILDCONNECT
api_location:
- Ddeml.h
api_type:
- HeaderDef
---

# XTYP\_WILDCONNECT transaction

Enables a client to establish a conversation on each of the server's service name and topic name pairs that match the specified service name and topic name. A Dynamic Data Exchange (DDE) server callback function, [*DdeCallback*](ddecallback.md), receives this transaction when a client specifies a **NULL** service name, a **NULL** topic name, or both in a call to the [**DdeConnect**](ddeconnect.md) or [**DdeConnectList**](ddeconnectlist.md) function.


```C++
#define     XCLASS_DATA              0x2000
#define     XTYPF_NOBLOCK            0x0002
#define     XTYP_WILDCONNECT        (0x00E0 | XCLASS_DATA | XTYPF_NOBLOCK)
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

A handle to the topic name. If this parameter is **NULL**, the client is requesting a conversation on all topic names that the server supports.

</dd> <dt>

*hsz2* 
</dt> <dd>

A handle to the service name. If this parameter is **NULL**, the client is requesting a conversation on all service names that the server supports.

</dd> <dt>

*hdata* 
</dt> <dd>

Not used.

</dd> <dt>

*dwData1* 
</dt> <dd>

A pointer to a [**CONVCONTEXT**](convcontext-str.md) structure that contains context information for the conversation. If the client is not a DDEML application, this parameter is set to 0.

</dd> <dt>

*dwData2* 
</dt> <dd>

Specifies whether the client is the same application instance as the server. If the parameter is 1, the client is same instance. If the parameter is 0, the client is a different instance.

</dd> </dl>

## Return value

The server should return a data handle that identifies an array of [**HSZPAIR**](hszpair.md) structures. The array should contain one structure for each service-name and topic-name pair that matches the service-name and topic-name pair requested by the client. The array must be terminated by a **NULL** string handle. The system sends the [**XTYP\_CONNECT\_CONFIRM**](xtyp-connect-confirm.md) transaction to the server to confirm each conversation and to pass the conversation handles to the server. The server will not receive these confirmations if it specified the **CBF\_SKIP\_CONNECT\_CONFIRMS** flag in the [**DdeInitialize**](ddeinitialize.md) function.

The server should return **NULL** to refuse the **XTYP\_WILDCONNECT** transaction.

## Remarks

This transaction is filtered if the server application specified the **CBF\_FAIL\_CONNECTIONS** flag in the [**DdeInitialize**](ddeinitialize.md) function.

A server cannot block this transaction type; the CBR\_BLOCK return code is ignored.

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

[**CONVCONTEXT**](convcontext-str.md)
</dt> <dt>

[**DdeConnect**](ddeconnect.md)
</dt> <dt>

[**DdeInitialize**](ddeinitialize.md)
</dt> <dt>

[**HSZPAIR**](hszpair.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Dynamic Data Exchange Management Library](dynamic-data-exchange-management-library.md)
</dt> </dl>

 

 





