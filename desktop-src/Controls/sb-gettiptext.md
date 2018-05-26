---
title: SB\_GETTIPTEXT message
description: Retrieves the tooltip text for a part in a status bar. The status bar must be created with the SBT\_TOOLTIPS style to enable tooltips.
ms.assetid: a3936830-a855-4ef6-b179-3aa3730cd0b8
keywords:
- SB_GETTIPTEXT message Windows Controls
topic_type:
- apiref
api_name:
- SB_GETTIPTEXT
- SB_GETTIPTEXTA
- SB_GETTIPTEXTW
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

# SB\_GETTIPTEXT message

Retrieves the tooltip text for a part in a status bar. The status bar must be created with the [**SBT\_TOOLTIPS**](status-bar-styles.md#sbt-tooltips) style to enable tooltips.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The [**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659) specifies the zero-based index of the part that receives the tooltip text. The [**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657) specifies the size of the buffer at *lParam*, in characters.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a character buffer that receives the tooltip text.

</dd> </dl>

## Return value

The return value is not used.

## Remarks

**Security Warning:** Using this message incorrectly can cause problems for your application. For example, if the text is too large for the *lParam* buffer, it could cause a buffer overflow. You should review the [Security Considerations: Microsoft Windows Controls](sec-comctls.md) before continuing.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **SB\_GETTIPTEXTW** (Unicode) and **SB\_GETTIPTEXTA** (ANSI)<br/>               |



 

 





