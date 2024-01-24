---
title: LBSELCHSTRING message (Commdlg.h)
description: An Open or Save As dialog box sends the LBSELCHSTRING registered message to your hook procedure when the selection changes in any of the list boxes or combo boxes of the dialog box.
ms.assetid: 3a8ebc63-b324-43ed-bb6f-34779f6043e7
keywords:
- LBSELCHSTRING message Dialog Boxes
topic_type:
- apiref
api_name:
- LBSELCHSTRING
- LBSELCHSTRINGA
- LBSELCHSTRINGW
api_location:
- Commdlg.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LBSELCHSTRING message

\[Starting with Windows Vista, the **Open** and **Save As** common dialog boxes have been superseded by the [Common Item Dialog](../shell/common-file-dialog.md). We recommended that you use the Common Item Dialog API instead of these dialog boxes from the Common Dialog Box Library.\]

An **Open** or **Save As** dialog box sends the **LBSELCHSTRING** registered message to your hook procedure when the selection changes in any of the list boxes or combo boxes of the dialog box.


```C++
#define LBSELCHSTRING TEXT("commdlg_LBSelChangedNotify")
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The identifier of the list box or combo box in which the selection changed.

</dd> <dt>

*lParam* 
</dt> <dd>

The low-order word specifies the item number of the selected string in the list box or combo box. The high-order word specifies the type of selection change. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                       | Meaning                                                                            |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <span id="CD_LBSELCHANGE"></span><span id="cd_lbselchange"></span><dl> <dt>**CD\_LBSELCHANGE**</dt> <dt>0</dt> </dl>     | The item is the only item selected in a single-selection list box.<br/>      |
| <span id="CD_LBSELADD"></span><span id="cd_lbseladd"></span><dl> <dt>**CD\_LBSELADD**</dt> <dt>2</dt> </dl>              | The item is one of the items selected in a multiple-selection list box.<br/> |
| <span id="CD_LBSELSUB"></span><span id="cd_lbselsub"></span><dl> <dt>**CD\_LBSELSUB**</dt> <dt>1</dt> </dl>              | The item is no longer selected in a multiple-selection list box.<br/>        |
| <span id="CD_LBSELNOITEMS"></span><span id="cd_lbselnoitems"></span><dl> <dt>**CD\_LBSELNOITEMS**</dt> <dt>-1</dt> </dl> | No items exist in a multiple-selection list box.<br/>                        |



 

</dd> </dl>

## Return value

This message has no return value.

## Remarks

The hook procedure must specify the **LBSELCHSTRING** constant in a call to the [**RegisterWindowMessage**](/windows/desktop/api/winuser/nf-winuser-registerwindowmessagea) function to get the identifier for the message sent by the dialog box.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Commdlg.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **LBSELCHSTRINGW** (Unicode) and **LBSELCHSTRINGA** (ANSI)<br/>                                    |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**CDN\_SELCHANGE**](cdn-selchange.md)
</dt> <dt>

[**CDN\_TYPECHANGE**](cdn-typechange.md)
</dt> <dt>

[**RegisterWindowMessage**](/windows/desktop/api/winuser/nf-winuser-registerwindowmessagea)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Common Dialog Box Library](common-dialog-box-library.md)
</dt> </dl>

