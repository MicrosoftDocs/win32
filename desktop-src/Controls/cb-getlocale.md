---
title: CB_GETLOCALE message (Winuser.h)
description: Gets the current locale of the combo box. The locale is used to determine the correct sorting order of displayed text for combo boxes with the CBS\_SORT style and text added by using the CB\_ADDSTRING message.
ms.assetid: 57c77ce2-bad0-43f3-8325-f2a7227994ec
keywords:
- CB_GETLOCALE message Windows Controls
topic_type:
- apiref
api_name:
- CB_GETLOCALE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_GETLOCALE message

Gets the current locale of the combo box. The locale is used to determine the correct sorting order of displayed text for combo boxes with the [**CBS\_SORT**](combo-box-styles.md) style and text added by using the [**CB\_ADDSTRING**](cb-addstring.md) message.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Not used; must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Not used; must be zero.

</dd> </dl>

## Return value

The return value specifies the current locale of the combo box. The [**HIWORD**](../winmsg/hiword.md) contains the country/region code and the [**LOWORD**](../winmsg/loword.md) contains the language identifier.

## Remarks

The language identifier is made up of a sublanguage identifier and a primary language identifier. The [**PRIMARYLANGID**](/windows/desktop/api/winnt/nf-winnt-primarylangid) macro obtains the primary language identifier and the [**SUBLANGID**](/windows/desktop/api/winnt/nf-winnt-sublangid) macro obtains the sublanguage identifier.

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

[**CB\_SETLOCALE**](cb-setlocale.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**HIWORD**](../winmsg/hiword.md)
</dt> <dt>

[**LOWORD**](../winmsg/loword.md)
</dt> <dt>

[**PRIMARYLANGID**](/windows/desktop/api/winnt/nf-winnt-primarylangid)
</dt> <dt>

[**SUBLANGID**](/windows/desktop/api/winnt/nf-winnt-sublangid)
</dt> </dl>

 

