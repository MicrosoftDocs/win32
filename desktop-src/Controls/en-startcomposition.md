---
title: EN\_STARTCOMPOSITION notification code
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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EN\_STARTCOMPOSITION notification code

Notifies a rich edit control parent window that the user started typing with IME or [Text Services Framework](https://msdn.microsoft.com/library/windows/desktop/ms629032).


```C++
EN_STARTCOMPOSITION

    pStartComp = (NMDHR *) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

An [**NMHDR**](/windows/win32/richedit/ns-richedit-_nmhdr?branch=master) structure.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



 

 





