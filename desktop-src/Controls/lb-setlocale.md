---
title: LB_SETLOCALE message (Winuser.h)
description: Sets the current locale of the list box. You can use the locale to determine the correct sorting order of displayed text (for list boxes with the LBS\_SORT style) and of text added by the LB\_ADDSTRING message.
ms.assetid: e9503124-de9f-4b92-a59e-ec9320864ae7
keywords:
- LB_SETLOCALE message Windows Controls
topic_type:
- apiref
api_name:
- LB_SETLOCALE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LB\_SETLOCALE message

Sets the current locale of the list box. You can use the locale to determine the correct sorting order of displayed text (for list boxes with the [**LBS\_SORT**](list-box-styles.md) style) and of text added by the [**LB\_ADDSTRING**](lb-addstring.md) message.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the locale identifier that the list box will use for sorting when adding text.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

The return value is the previous locale identifier. If the *wParam* parameter specifies a locale that is not installed on the system, the return value is LB\_ERR and the current list box locale is not changed.

## Remarks

Use the [**MAKELCID**](/windows/desktop/api/winnt/nf-winnt-makelcid) macro to construct a locale identifier.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**LB\_ADDSTRING**](lb-addstring.md)
</dt> <dt>

[**LB\_GETLOCALE**](lb-getlocale.md)
</dt> </dl>

 

