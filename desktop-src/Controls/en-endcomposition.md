---
title: EN_ENDCOMPOSITION notification code (Richedit.h)
description: Notifies a rich edit control parent window that the user has entered new data or has finished entering data while using IME or Text Services Framework.
ms.assetid: 3956313F-F82F-41A2-AEDA-52E63218977C
keywords:
- EN_ENDCOMPOSITION notification code Windows Controls
topic_type:
- apiref
api_name:
- EN_ENDCOMPOSITION
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EN\_ENDCOMPOSITION notification code

Notifies a rich edit control parent window that the user has entered new data or has finished entering data while using IME or [Text Services Framework](/windows/desktop/TSF/text-services-framework).


```C++
EN_ENDCOMPOSITION

     pEndComp = (ENDCOMPOSITIONNOTIFY *)lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A [**ENDCOMPOSITIONNOTIFY**](/windows/win32/api/richedit/ns-richedit-endcompositionnotify) structure that receives information about the end composition condition.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



 

