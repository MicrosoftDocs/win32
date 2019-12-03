---
title: CDN_FILEOK notification code (Commdlg.h)
description: Sent by an Explorer-style Open or Save As dialog box when the user specifies a file name and clicks the OK button.
ms.assetid: 7f3de96f-68d8-4f40-b74f-304835f9def2
keywords:
- CDN_FILEOK notification code Dialog Boxes
topic_type:
- apiref
api_name:
- CDN_FILEOK
api_location:
- Commdlg.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CDN\_FILEOK notification code

Sent by an Explorer-style **Open** or **Save As** dialog box when the user specifies a file name and clicks the **OK** button.

Your [*OFNHookProc*](https://msdn.microsoft.com/en-us/library/ms646931(v=VS.85).aspx) hook procedure receives this message in the form of a [**WM\_NOTIFY**](https://msdn.microsoft.com/library/Bb775583(v=VS.85).aspx) message.


```C++
#define CDN_FIRST               (0U-601U)
#define CDN_FILEOK              (CDN_FIRST - 0x0005)
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**OFNOTIFY**](/windows/desktop/api/Commdlg/ns-commdlg-ofnotifya) structure.

The [**OFNOTIFY**](/windows/desktop/api/Commdlg/ns-commdlg-ofnotifya) structure contains an [**NMHDR**](https://msdn.microsoft.com/library/Bb775514(v=VS.85).aspx) structure whose **code** member indicates the **CDN\_FILEOK** notification message.

The [**OFNOTIFY**](/windows/desktop/api/Commdlg/ns-commdlg-ofnotifya) structure also contains a pointer to an [**OPENFILENAME**](/windows/win32/api/commdlg/ns-commdlg-openfilenamea) structure whose **lpstrFile** member specifies the address of the selected file name.

</dd> </dl>

## Return value

If the hook procedure returns zero, the dialog box accepts the specified file name and closes.

To reject the specified file name and force the dialog box to remain open, return a nonzero value from the hook procedure and call the [**SetWindowLong**](https://docs.microsoft.com/windows/desktop/api/winuser/nf-winuser-setwindowlonga) function to set a nonzero **DWL\_MSGRESULT** value.

## Remarks

The system sends this notification only if the dialog box was created using the **OFN\_EXPLORER** value.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Commdlg.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**GetOpenFileName**](/windows/desktop/api/Commdlg/nf-commdlg-getopenfilenamea)
</dt> <dt>

[**GetSaveFileName**](/windows/desktop/api/Commdlg/nf-commdlg-getsavefilenamea)
</dt> <dt>

[*OFNHookProc*](https://msdn.microsoft.com/en-us/library/ms646931(v=VS.85).aspx)
</dt> <dt>

[**OFNOTIFY**](/windows/desktop/api/Commdlg/ns-commdlg-ofnotifya)
</dt> <dt>

[**OPENFILENAME**](/windows/win32/api/commdlg/ns-commdlg-openfilenamea)
</dt> <dt>

[**SetWindowLong**](https://docs.microsoft.com/windows/desktop/api/winuser/nf-winuser-setwindowlonga)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Common Dialog Box Library](common-dialog-box-library.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**WM\_NOTIFY**](https://msdn.microsoft.com/library/Bb775583(v=VS.85).aspx)
</dt> </dl>

 

 





