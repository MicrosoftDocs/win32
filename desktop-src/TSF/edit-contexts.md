---
title: Edit Contexts
description: Edit Contexts
ms.assetid: cf8bbe66-d2ad-49b3-9e7c-246e4ca50149
keywords:
- Text Services Framework (TSF),edit contexts
- TSF (Text Services Framework),edit contexts
- text services,edit contexts
- TSF-enabled applications,edit contexts
- edit contexts
- Text Services Framework (TSF),edit cookies
- TSF (Text Services Framework),edit cookies
- text services,edit cookies
- TSF-enabled applications,edit cookies
- edit cookies
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Edit Contexts

## Applications

To create an edit context, an application calls [ITfDocumentMgr::CreateContext](/windows/win32/Msctf/nf-msctf-itfdocumentmgr-createcontext?branch=master).

## Text Services

A text service often uses the currently active edit context. The currently active edit context is the edit context at the top of the stack of the active document manager. To obtain the currently active context, a text service calls [ITfThreadMgr::GetFocus](/windows/win32/Msctf/nf-msctf-itfthreadmgr-getfocus?branch=master) to obtain the active document manager and then calls [ITfDocumentMgr::GetTop](/windows/win32/Msctf/nf-msctf-itfdocumentmgr-gettop?branch=master) to obtain the edit context at the top of the stack.

In some cases, a text service requires its own edit context. To create an edit context, a text service calls **ITfDocumentMgr::CreateContext**.

## Edit Cookies

Many methods, such as [ITfRange::SetText](/windows/win32/Msctf/nf-msctf-itfrange-settext?branch=master), require a way to identify an edit context that has a read-only or read/write [document lock](document-locks.md). A document lock is obtained through a negotiation between the TSF manager and the application. A text service cannot perform this negotiation directly. A text service can only obtain a lock by requesting an [edit session](edit-sessions.md) with a specific context and read-only or read/write access. When the edit session is granted, the text service is supplied with an *edit cookie* that identifies the edit context with the requested access. This cookie is then passed to the method to identify the edit context with the proper access.

**ITfDocumentMgr::CreateContext** also supplies an edit cookie to the context creator. This cookie has read-only access and there is no way to modify the access level. In truth, the TSF manager does not negotiate a document lock for this edit cookie. The cookie is internally marked read-only, but the document is not actually locked. For example, if the context creator calls [ITfContext::GetSelection](/windows/win32/Msctf/nf-msctf-itfcontext-getselection?branch=master) with the edit cookie returned by **ITfDocumentMgr::CreateContext** , this results in the application's [ITextStoreACP::GetSelection](/windows/win32/Textstor/nf-textstor-itextstoreacp-getselection?branch=master) or [ITextStoreAnchor::GetSelection](/windows/win32/Textstor/nf-textstor-itextstoreanchor-getselection?branch=master) being called. Before obtaining the selection, the application will determine if a document lock exists. Because no lock exists, the application will fail with TS\_E\_NOLOCK. That is, if an application calls a method with this cookie that results in one of the application's text store methods being called, it must handle this case internally because the application will not actually have a document lock.

If the context creator requires an edit cookie with read/write access, it must establish its own edit session.

## Related topics

<dl> <dt>

[ITfContext](/windows/win32/Msctf/nn-msctf-itfcontext?branch=master)
</dt> <dt>

[ITfDocumentMgr::CreateContext](/windows/win32/Msctf/nf-msctf-itfdocumentmgr-createcontext?branch=master)
</dt> <dt>

[ITfThreadMgr::GetFocus](/windows/win32/Msctf/nf-msctf-itfthreadmgr-getfocus?branch=master)
</dt> <dt>

[ITfDocumentMgr::GetTop](/windows/win32/Msctf/nf-msctf-itfdocumentmgr-gettop?branch=master)
</dt> <dt>

[ITfRange::SetText](/windows/win32/Msctf/nf-msctf-itfrange-settext?branch=master)
</dt> <dt>

[Document Locks](document-locks.md)
</dt> <dt>

[Edit Sessions](edit-sessions.md)
</dt> <dt>

[ITfContext::GetSelection](/windows/win32/Msctf/nf-msctf-itfcontext-getselection?branch=master)
</dt> <dt>

[ITextStoreACP::GetSelection](/windows/win32/Textstor/nf-textstor-itextstoreacp-getselection?branch=master)
</dt> <dt>

[ITextStoreAnchor::GetSelection](/windows/win32/Textstor/nf-textstor-itextstoreanchor-getselection?branch=master)
</dt> </dl>

 

 




