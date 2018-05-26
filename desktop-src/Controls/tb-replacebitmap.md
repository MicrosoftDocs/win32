---
title: TB\_REPLACEBITMAP message
description: Replaces an existing bitmap with a new bitmap.
ms.assetid: abad5c7a-ebdd-46b5-a465-fe64ff8eb127
keywords:
- TB_REPLACEBITMAP message Windows Controls
topic_type:
- apiref
api_name:
- TB_REPLACEBITMAP
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TB\_REPLACEBITMAP message

Replaces an existing bitmap with a new bitmap.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**TBREPLACEBITMAP**](/windows/win32/Commctrl/ns-commctrl-tbreplacebitmap?branch=master) structure that contains the information of the bitmap to be replaced and the new bitmap.

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





