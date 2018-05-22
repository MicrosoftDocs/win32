---
title: CB\_GETLOCALE message
description: Gets the current locale of the combo box. The locale is used to determine the correct sorting order of displayed text for combo boxes with the CBS\_SORT style and text added by using the CB\_ADDSTRING message.
ms.assetid: '57c77ce2-bad0-43f3-8325-f2a7227994ec'
keywords: ["CB_GETLOCALE message Windows Controls"]
topic_type:
- apiref
api_name:
- CB_GETLOCALE
api_location:
- Winuser.h
api_type:
- HeaderDef
---

# CB\_GETLOCALE message

Gets the current locale of the combo box. The locale is used to determine the correct sorting order of displayed text for combo boxes with the [**CBS\_SORT**](combo-box-styles.md#cbs-sort) style and text added by using the [**CB\_ADDSTRING**](cb-addstring.md) message.

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

The return value specifies the current locale of the combo box. The [**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657) contains the country/region code and the [**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659) contains the language identifier.

## Remarks

The language identifier is made up of a sublanguage identifier and a primary language identifier. The [**PRIMARYLANGID**](https://msdn.microsoft.com/library/windows/desktop/dd319102) macro obtains the primary language identifier and the [**SUBLANGID**](https://msdn.microsoft.com/library/windows/desktop/dd374066) macro obtains the sublanguage identifier.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
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

[**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657)
</dt> <dt>

[**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659)
</dt> <dt>

[**PRIMARYLANGID**](https://msdn.microsoft.com/library/windows/desktop/dd319102)
</dt> <dt>

[**SUBLANGID**](https://msdn.microsoft.com/library/windows/desktop/dd374066)
</dt> </dl>

 

 





