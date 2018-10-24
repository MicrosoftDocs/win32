---
title: EN_ENDCOMPOSITION notification code
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
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# EN\_ENDCOMPOSITION notification code

Notifies a rich edit control parent window that the user has entered new data or has finished entering data while using IME or [Text Services Framework](https://msdn.microsoft.com/library/windows/desktop/ms629032).


```C++
EN_ENDCOMPOSITION

     pEndComp = (ENDCOMPOSITIONNOTIFY *)lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A [**ENDCOMPOSITIONNOTIFY**](/windows/desktop/api/Richedit/ns-richedit-_endcomposition) structure that receives information about the end composition condition.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



 

 





