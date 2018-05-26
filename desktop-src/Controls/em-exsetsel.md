---
title: EM\_EXSETSEL message
description: Selects a range of characters or Component Object Model (COM) objects in a Microsoft Rich Edit control.
ms.assetid: 85a0d1d4-1826-4ac5-b823-de81a051441d
keywords:
- EM_EXSETSEL message Windows Controls
topic_type:
- apiref
api_name:
- EM_EXSETSEL
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

# EM\_EXSETSEL message

Selects a range of characters or Component Object Model (COM) objects in a Microsoft Rich Edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used; it must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

A [**CHARRANGE**](/windows/win32/Richedit/ns-richedit-_charrange?branch=master) structure that specifies the selection range.

</dd> </dl>

## Return value

The return value is the selection that is actually set.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



 

 





