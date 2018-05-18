---
title: TfEditCookie
description: The TfEditCookie data type identifies an edit session that has a lock.
ms.assetid: '1de17286-5d56-4302-a144-5fe6ca7d5557'
keywords: ["TfEditCookie"]
---

# TfEditCookie

The **TfEditCookie** data type identifies an edit session that has a lock.


```C++
typedef DWORD TfEditCookie;
```



## Remarks

The **TfEditCookie** data type is supplied by the TSF manager and is used by a client (application or text service) to identify an edit session with a read-only or read/write lock in various methods.

A **TfEditCookie** value is obtained in one of the following ways.

-   The client calls [ITfDocumentMgr::CreateContext](itfdocumentmgr-createcontext.md).
-   The TSF manager calls the client [ITfEditSession::DoEditSession](itfeditsession-doeditsession.md) method.
-   The TSF manager calls the client [ITfCompositionSink::OnCompositionTerminated](itfcompositionsink-oncompositionterminated.md) method.
-   The TSF manager calls the client [ITfCleanupContextSink::OnCleanupContext](itfcleanupcontextsink-oncleanupcontext.md) method.
-   The TSF manager calls the client [ITfTextEditSink::OnEndEdit](itftexteditsink-onendedit.md) method.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                    |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                          |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                      |
| Header<br/>                   | <dl> <dt>Msctf.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msctf.idl</dt> </dl> |



## See also

<dl> <dt>

[**ITfCleanupContextSink::OnCleanupContext**](itfcleanupcontextsink-oncleanupcontext.md)
</dt> <dt>

[**ITfCompositionSink::OnCompositionTerminated**](itfcompositionsink-oncompositionterminated.md)
</dt> <dt>

[**ITfDocumentMgr::CreateContext**](itfdocumentmgr-createcontext.md)
</dt> <dt>

[**ITfEditSession::DoEditSession**](itfeditsession-doeditsession.md)
</dt> <dt>

[**ITfTextEditSink::OnEndEdit**](itftexteditsink-onendedit.md)
</dt> </dl>

 

 





