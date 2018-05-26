---
title: Document Manager
description: Document Manager
ms.assetid: e30087b6-524a-481e-845d-0348bac3830a
keywords:
- Text Services Framework (TSF),document manager
- TSF (Text Services Framework),document manager
- text services,document manager
- TSF-enabled applications,document manager
- document manager
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Document Manager

## Applications

To create a document manager object an application calls [ITfThreadMgr::CreateDocumentMgr](/windows/win32/Msctf/nf-msctf-itfthreadmgr-createdocumentmgr?branch=master). The application creates a separate document manager object for each individual document that the application maintains. The application uses the document manager to create edit contexts, add a context to the context stack and remove a context from the context stack.

## Text Services

A text service never creates a document manager object. Instead, the text service obtains the currently active document manager object by calling [ITfThreadMgr::GetFocus](/windows/win32/Msctf/nf-msctf-itfthreadmgr-getfocus?branch=master). A text service uses the document manager to obtain the context at the top of the stack.

A text service can also use the document manager to create its own context and add and remove it from the context stack. This is normally done when the text service must display some modal user interface, such as when a list of words is displayed to enable the user to select a word. When the list is displayed, the text service places its own context on the stack. When the word list is dismissed, the text service removes its context from the stack.

## Related topics

<dl> <dt>

[ITfDocumentMgr](/windows/win32/Msctf/nn-msctf-itfdocumentmgr?branch=master)
</dt> <dt>

[ITfThreadMgr::CreateDocumentMgr](/windows/win32/Msctf/nf-msctf-itfthreadmgr-createdocumentmgr?branch=master)
</dt> <dt>

[ITfThreadMgr::GetFocus](/windows/win32/Msctf/nf-msctf-itfthreadmgr-getfocus?branch=master)
</dt> </dl>

 

 




