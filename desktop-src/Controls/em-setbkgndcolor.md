---
title: EM\_SETBKGNDCOLOR message
description: The EM\_SETBKGNDCOLOR message sets the background color for a rich edit control.
ms.assetid: 0ad191cd-6370-493e-bfe2-5aa8d81ed999
keywords:
- EM_SETBKGNDCOLOR message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETBKGNDCOLOR
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

# EM\_SETBKGNDCOLOR message

The **EM\_SETBKGNDCOLOR** message sets the background color for a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies whether to use the system color. If this parameter is a nonzero value, the background is set to the window background system color. Otherwise, the background is set to the specified color.

</dd> <dt>

*lParam* 
</dt> <dd>

A [**COLORREF**](https://msdn.microsoft.com/library/windows/desktop/dd183449) structure specifying the color if *wParam* is zero. To generate a **COLORREF**, use the [**RGB**](https://msdn.microsoft.com/library/windows/desktop/dd162937) macro.

</dd> </dl>

## Return value

This message returns the original background color.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

**Other Resources**
</dt> <dt>

[**COLORREF**](https://msdn.microsoft.com/library/windows/desktop/dd183449)
</dt> <dt>

[**RGB**](https://msdn.microsoft.com/library/windows/desktop/dd162937)
</dt> </dl>

 

 





