---
title: PSM\_IDTOINDEX message
description: Takes the resource ID of a property sheet page and returns its zero-based index. You can send this message explicitly or use the PropSheet\_IdToIndex macro.
ms.assetid: 91420c1e-7f8a-4b1c-a1fc-6ff65ee4b1b0
keywords:
- PSM_IDTOINDEX message Windows Controls
topic_type:
- apiref
api_name:
- PSM_IDTOINDEX
api_location:
- Prsht.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PSM\_IDTOINDEX message

Takes the resource ID of a property sheet page and returns its zero-based index. You can send this message explicitly or use the [**PropSheet\_IdToIndex**](/windows/win32/Prsht/nf-prsht-propsheet_idtoindex?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Resource ID of the page.

</dd> </dl>

## Return value

Returns the zero-based index of the property sheet page specified by *lParam* if successful. Otherwise, it returns -1.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |



 

 





