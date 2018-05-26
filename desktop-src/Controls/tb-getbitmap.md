---
title: TB\_GETBITMAP message
description: Retrieves the index of the bitmap associated with a button in a toolbar.
ms.assetid: 64878cca-7d71-48ad-b2ed-d2bdc3067592
keywords:
- TB_GETBITMAP message Windows Controls
topic_type:
- apiref
api_name:
- TB_GETBITMAP
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

# TB\_GETBITMAP message

Retrieves the index of the bitmap associated with a button in a toolbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Command identifier of the button whose bitmap index is to be retrieved.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the index of the bitmap if successful, or zero otherwise.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





