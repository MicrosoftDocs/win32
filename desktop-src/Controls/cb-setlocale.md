---
title: CB_SETLOCALE message (Winuser.h)
description: An application sends a CB\_SETLOCALE message to set the current locale of the combo box. If the combo box has the CBS\_SORT style and strings are added using CB\_ADDSTRING, the locale of a combo box affects how list items are sorted.
ms.assetid: 06f9c69d-1220-490f-bc67-6e125f696e87
keywords:
- CB_SETLOCALE message Windows Controls
topic_type:
- apiref
api_name:
- CB_SETLOCALE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_SETLOCALE message

An application sends a **CB\_SETLOCALE** message to set the current locale of the combo box. If the combo box has the [**CBS\_SORT**](combo-box-styles.md) style and strings are added using [**CB\_ADDSTRING**](cb-addstring.md), the locale of a combo box affects how list items are sorted.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the locale identifier for the combo box to use for sorting when adding text.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

The return value is the previous locale identifier. If *wParam* specifies a locale not installed on the system, the return value is CB\_ERR and the current combo box locale is not changed.

## Remarks

Use the [**MAKELCID**](/windows/desktop/api/winnt/nf-winnt-makelcid) macro to construct a locale identifier and the [**MAKELANGID**](/windows/desktop/api/winnt/nf-winnt-makelangid) macro to construct a language identifier. The language identifier is made up of a primary language identifier and a sublanguage identifier.

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

[**CB\_ADDSTRING**](cb-addstring.md)
</dt> <dt>

[**CB\_GETLOCALE**](cb-getlocale.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**MAKELANGID**](/windows/desktop/api/winnt/nf-winnt-makelangid)
</dt> <dt>

[**MAKELCID**](/windows/desktop/api/winnt/nf-winnt-makelcid)
</dt> </dl>

 

