---
title: EN_STARTCOMPOSITION notification code (Richedit.h)
description: Notifies a rich edit control parent window that the user started typing with IME or Text Services Framework.
ms.assetid: 755C0C5F-061B-44AF-98A5-776AEE1B7AF8
keywords:
- EN_STARTCOMPOSITION notification code Windows Controls
topic_type:
- apiref
api_name:
- EN_STARTCOMPOSITION
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EN\_STARTCOMPOSITION notification code

Notifies a rich edit control parent window that the user started typing with IME or [Text Services Framework](/windows/desktop/TSF/text-services-framework).


```C++
EN_STARTCOMPOSITION

    pStartComp = (NMDHR *) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

An [**NMHDR**](/windows/desktop/api/richedit/ns-richedit-nmhdr) structure.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



 

