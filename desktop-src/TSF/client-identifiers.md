---
title: Client Identifiers
description: Client Identifiers
ms.assetid: 69ff159c-9264-4958-a712-4aa50db6e48e
keywords:
- Text Services Framework (TSF),client identifiers
- TSF (Text Services Framework),client identifiers
- text services,client identifiers
- TSF-enabled applications,client identifiers
- client identifiers
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Client Identifiers

## Applications

An application obtains its client identifier by calling [ITfThreadMgr::Activate](/windows/win32/Msctf/nf-msctf-itfthreadmgr-activate?branch=master).

## Text Services

A text service obtains its client identifier when the text service [ITfTextInputProcessor::Activate](/windows/win32/Msctf/nf-msctf-itftextinputprocessor-activate?branch=master) method is called.

## Related topics

<dl> <dt>

[ITfThreadMgr::Activate](/windows/win32/Msctf/nf-msctf-itfthreadmgr-activate?branch=master)
</dt> <dt>

[ITfTextInputProcessor::Activate](/windows/win32/Msctf/nf-msctf-itftextinputprocessor-activate?branch=master)
</dt> </dl>

 

 




