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
ms.topic: article
ms.date: 05/31/2018
---

# Client Identifiers

## Applications

An application obtains its client identifier by calling [ITfThreadMgr::Activate](/windows/desktop/api/Msctf/nf-msctf-itfthreadmgr-activate).

## Text Services

A text service obtains its client identifier when the text service [ITfTextInputProcessor::Activate](/windows/desktop/api/Msctf/nf-msctf-itftextinputprocessor-activate) method is called.

## Related topics

<dl> <dt>

[ITfThreadMgr::Activate](/windows/desktop/api/Msctf/nf-msctf-itfthreadmgr-activate)
</dt> <dt>

[ITfTextInputProcessor::Activate](/windows/desktop/api/Msctf/nf-msctf-itftextinputprocessor-activate)
</dt> </dl>

 

 




