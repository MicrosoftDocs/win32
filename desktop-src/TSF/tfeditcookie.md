---
title: TfEditCookie
description: The TfEditCookie data type identifies an edit session that has a lock.
ms.assetid: 1de17286-5d56-4302-a144-5fe6ca7d5557
keywords:
- TfEditCookie
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TfEditCookie

The **TfEditCookie** data type identifies an edit session that has a lock.


```C++
typedef DWORD TfEditCookie;
```



## Remarks

The **TfEditCookie** data type is supplied by the TSF manager and is used by a client (application or text service) to identify an edit session with a read-only or read/write lock in various methods.

A **TfEditCookie** value is obtained in one of the following ways.

-   The client calls [ITfDocumentMgr::CreateContext](/windows/win32/Msctf/nf-msctf-itfdocumentmgr-createcontext?branch=master).
-   The TSF manager calls the client [ITfEditSession::DoEditSession](/windows/win32/Msctf/nf-msctf-itfeditsession-doeditsession?branch=master) method.
-   The TSF manager calls the client [ITfCompositionSink::OnCompositionTerminated](/windows/win32/Msctf/nf-msctf-itfcompositionsink-oncompositionterminated?branch=master) method.
-   The TSF manager calls the client [ITfCleanupContextSink::OnCleanupContext](/windows/win32/Msctf/nf-msctf-itfcleanupcontextsink-oncleanupcontext?branch=master) method.
-   The TSF manager calls the client [ITfTextEditSink::OnEndEdit](/windows/win32/Msctf/nf-msctf-itftexteditsink-onendedit?branch=master) method.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                    |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                          |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                      |
| Header<br/>                   | <dl> <dt>Msctf.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msctf.idl</dt> </dl> |



## See also

<dl> <dt>

[**ITfCleanupContextSink::OnCleanupContext**](/windows/win32/Msctf/nf-msctf-itfcleanupcontextsink-oncleanupcontext?branch=master)
</dt> <dt>

[**ITfCompositionSink::OnCompositionTerminated**](/windows/win32/Msctf/nf-msctf-itfcompositionsink-oncompositionterminated?branch=master)
</dt> <dt>

[**ITfDocumentMgr::CreateContext**](/windows/win32/Msctf/nf-msctf-itfdocumentmgr-createcontext?branch=master)
</dt> <dt>

[**ITfEditSession::DoEditSession**](/windows/win32/Msctf/nf-msctf-itfeditsession-doeditsession?branch=master)
</dt> <dt>

[**ITfTextEditSink::OnEndEdit**](/windows/win32/Msctf/nf-msctf-itftexteditsink-onendedit?branch=master)
</dt> </dl>

 

 





