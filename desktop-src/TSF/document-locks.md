---
title: Document Locks
description: Document Locks
ms.assetid: 3c623c44-b0d3-4b03-8de9-25f1062b5726
keywords:
- Text Services Framework (TSF),document locks
- TSF (Text Services Framework),document locks
- TSF-enabled applications,document locks
- document locks
- Text Services Framework (TSF),Application Character Position (ACP)
- TSF (Text Services Framework),Application Character Position (ACP)
- TSF-enabled applications,Application Character Position (ACP)
- Application Character Position (ACP)
- ACP (Application Character Position)
- Text Services Framework (TSF),anchors
- TSF (Text Services Framework),anchors
- TSF-enabled applications,anchors
- anchors
ms.topic: article
ms.date: 05/31/2018
---

# Document Locks

## The Document Lock Protocol

To request a document lock for ACP-based applications, the TSF manager calls [ITextStoreACP::RequestLock](/windows/desktop/api/Textstor/nf-textstor-itextstoreacp-requestlock). For anchor-based applications, the TSF manager calls [ITextStoreAnchor::RequestLock](/windows/desktop/api/Textstor/nf-textstor-itextstoreanchor-requestlock). The application grants the document lock by calling [ITextStoreACPSink::OnLockGranted](/windows/desktop/api/Textstor/nf-textstor-itextstoreacpsink-onlockgranted) (ACP-based applications) or [ITextStoreAnchorSink::OnLockGranted](/windows/desktop/api/Textstor/nf-textstor-itextstoreanchorsink-onlockgranted) (anchor-based applications) inside of **RequestLock**. The lock is only valid during the **OnLockGranted** call. When **OnLockGranted** returns, the document is considered unlocked.

## Types of Document Locks

There are two types of document locks, read-only and read/write. A read-only lock enables the manager to read the text, but it cannot modify or insert text. A read/write lock enables the manager to read, modify, and insert text. A read-only lock is requested by specifying TS\_LF\_READ in *dwFlags*. A read/write lock is requested by specifying TS\_LF\_READWRITE in *dwFlags*.

## Asynchronous and Synchronous Requests

A lock request can be either synchronous or asynchronous. The manager requests a synchronous lock by using the TS\_LF\_SYNC flag in *dwFlags*. If this flag is not present, the request is asynchronous.

## Granting the Lock

When **RequestLock** is called, the application must determine if the document is currently locked. If the document is not locked, and no other reason to deny the lock exists, the application should set *phrSession* to S\_OK and return S\_OK.

If the document is locked and the lock request is synchronous, the application should set *phrSession* to TS\_E\_SYNCHRONOUS and return S\_OK. This indicates that a synchronous request cannot be granted.

If the document is locked and the lock request is asynchronous, the application should queue the request, set *phrSession* to TS\_S\_ASYNC and return S\_OK. When the document becomes available, the application should remove the request from the queue and call **OnLockGranted**. This queuing of lock requests is optional; there is one scenario that an application must support. If the document has a read-only lock, the new lock request is read/write and the request is asynchronous, the application has called into **OnLockGranted** , which has caused a reentrant call to **RequestLock**. The application should set *phrSession* to TS\_S\_ASYNC and return S\_OK. After the call to **OnLockGranted** returns, the application should process the upgrade request by calling **OnLockGranted** again with TS\_LF\_READWRITE.

## Lock Enforcement

The application must ensure that the proper type of lock exists before allowing access to the document. For example, the application should verify that a document has at least a read-only lock before allowing [ITextStoreACP::GetText](/windows/desktop/api/Textstor/nf-textstor-itextstoreacp-gettext) or [ITextStoreAnchor::GetText](/windows/desktop/api/Textstor/nf-textstor-itextstoreanchor-gettext) to proceed. If the proper lock does not exist, the application should return TF\_E\_NOLOCK.

## Related topics

<dl> <dt>

[Text Stores](text-stores.md)
</dt> <dt>

[ITextStoreACP::RequestLock](/windows/desktop/api/Textstor/nf-textstor-itextstoreacp-requestlock)
</dt> <dt>

[ITextStoreACPSink::OnLockGranted](/windows/desktop/api/Textstor/nf-textstor-itextstoreacpsink-onlockgranted)
</dt> <dt>

[ITextStoreACP::GetText](/windows/desktop/api/Textstor/nf-textstor-itextstoreacp-gettext)
</dt> <dt>

[ITextStoreAnchor::RequestLock](/windows/desktop/api/Textstor/nf-textstor-itextstoreanchor-requestlock)
</dt> <dt>

[ITextStoreAnchorSink::OnLockGranted](/windows/desktop/api/Textstor/nf-textstor-itextstoreanchorsink-onlockgranted)
</dt> <dt>

[ITextStoreAnchor::GetText](/windows/desktop/api/Textstor/nf-textstor-itextstoreanchor-gettext)
</dt> </dl>

 

 




