---
title: XTYP\_CONNECT transaction
description: A client uses the XTYP\_CONNECT transaction to establish a conversation.
ms.assetid: 74f43b10-f7ac-4370-9caa-7b9ddf3413ed
keywords:
- XTYP_CONNECT transaction Data Exchange
topic_type:
- apiref
api_name:
- XTYP_CONNECT
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

# XTYP\_CONNECT transaction

A client uses the **XTYP\_CONNECT** transaction to establish a conversation. A Dynamic Data Exchange (DDE) server callback function, [*DdeCallback*](ddecallback.md), receives this transaction when a client specifies a service name that the server supports (and a topic name that is not **NULL**) in a call to the [**DdeConnect**](/windows/win32/Ddeml/nf-ddeml-ddeconnect?branch=master) function.


```C++
#define     XCLASS_BOOL              0x1000
#define     XTYPF_NOBLOCK            0x0002
#define     XTYP_CONNECT            (0x0060 | XCLASS_BOOL | XTYPF_NOBLOCK)
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

A handle to the topic name.

</dd> <dt>

*hsz2* 
</dt> <dd>

A handle to the service name.

</dd> <dt>

*hdata* 
</dt> <dd>

Not used.

</dd> <dt>

*dwData1* 
</dt> <dd>

A pointer to a [**CONVCONTEXT**](/windows/win32/Ddeml/ns-ddeml-tagconvcontext?branch=master) structure that contains context information for the conversation. If the client is not a DDEML application, this parameter is 0.

</dd> <dt>

*dwData2* 
</dt> <dd>

Specifies whether the client is the same application instance as the server. If the parameter is 1, the client is the same instance. If the parameter is 0, the client is a different instance.

</dd> </dl>

## Return value

A server callback function should return **TRUE** to allow the client to establish a conversation on the specified service name and topic name pair, or the function should return **FALSE** to deny the conversation. If the callback function returns **TRUE** and a conversation is successfully established, the system passes the conversation handle to the server by issuing an [**XTYP\_CONNECT\_CONFIRM**](xtyp-connect-confirm.md) transaction to the server's callback function (unless the server specified the **CBF\_SKIP\_CONNECT\_CONFIRMS** flag in the [**DdeInitialize**](/windows/win32/Ddeml/nf-ddeml-ddeinitializea?branch=master) function).

## Remarks

This transaction is filtered if the server application specified the **CBF\_FAIL\_CONNECTIONS** flag in the [**DdeInitialize**](/windows/win32/Ddeml/nf-ddeml-ddeinitializea?branch=master) function.

A server cannot block this transaction type; the **CBR\_BLOCK** return code is ignored.

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

[**CONVCONTEXT**](/windows/win32/Ddeml/ns-ddeml-tagconvcontext?branch=master)
</dt> <dt>

[**DdeConnect**](/windows/win32/Ddeml/nf-ddeml-ddeconnect?branch=master)
</dt> <dt>

[**DdeInitialize**](/windows/win32/Ddeml/nf-ddeml-ddeinitializea?branch=master)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Dynamic Data Exchange Management Library](dynamic-data-exchange-management-library.md)
</dt> </dl>

 

 





