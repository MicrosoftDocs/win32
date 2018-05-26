---
title: CB\_GETCOMBOBOXINFO message
description: Gets information about the specified combo box.
ms.assetid: 3239dfa8-7301-48e3-ba8e-29c5d5f43b39
keywords:
- CB_GETCOMBOBOXINFO message Windows Controls
topic_type:
- apiref
api_name:
- CB_GETCOMBOBOXINFO
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CB\_GETCOMBOBOXINFO message

Gets information about the specified combo box.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* \[out\]
</dt> <dd>

A pointer to a [**COMBOBOXINFO**](/windows/win32/Winuser/ns-winuser-tagcomboboxinfo?branch=master) structure that receives the information.

</dd> </dl>

## Return value

If the function succeeds, the return value is nonzero.

If the function fails, the return value is zero. To get extended error information, call [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360).

## Remarks

This message is equivalent to [**GetComboBoxInfo**](/windows/win32/Winuser/nf-winuser-getcomboboxinfo?branch=master).

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**COMBOBOXINFO**](/windows/win32/Winuser/ns-winuser-tagcomboboxinfo?branch=master)
</dt> <dt>

[**GetComboBoxInfo**](/windows/win32/Winuser/nf-winuser-getcomboboxinfo?branch=master)
</dt> </dl>

 

 





