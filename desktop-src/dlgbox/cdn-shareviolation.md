---
title: CDN\_SHAREVIOLATION notification code
description: Sent by an Explorer-style Open or Save As dialog box when the user clicks the OK button and a network sharing violation occurs for the selected file.
ms.assetid: a62ca550-0997-4379-aaaf-a5bc9414bd69
keywords:
- CDN_SHAREVIOLATION notification code Dialog Boxes
topic_type:
- apiref
api_name:
- CDN_SHAREVIOLATION
api_location:
- Commdlg.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CDN\_SHAREVIOLATION notification code

\[Starting with Windows Vista, the **Open** and **Save As** common dialog boxes have been superseded by the [Common Item Dialog](https://www.bing.com/search?q=Common+Item+Dialog). We recommended that you use the Common Item Dialog API instead of these dialog boxes from the Common Dialog Box Library.\]

Sent by an Explorer-style **Open** or **Save As** dialog box when the user clicks the **OK** button and a network sharing violation occurs for the selected file.

Your [*OFNHookProc*](https://www.bing.com/search?q=*OFNHookProc*) hook procedure receives this message in the form of a [**WM\_NOTIFY**](https://www.bing.com/search?q=**WM\_NOTIFY**) message.


```C++
#define CDN_FIRST               (0U-601U)
#define CDN_SHAREVIOLATION      (CDN_FIRST - 0x0003)
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**OFNOTIFY**](/windows/desktop/api/Commdlg/ns-commdlg-_ofnotifya) structure. The **pszFile** member of this structure is a pointer to the name of the file that had the sharing violation. The **OFNOTIFY** structure contains an [**NMHDR**](https://www.bing.com/search?q=**NMHDR**) structure whose **code** member indicates the **CDN\_SHAREVIOLATION** notification message.

</dd> </dl>

## Return value

The return value indicates how the dialog box should handle the sharing violation.

If the hook procedure returns zero, the dialog box displays the standard warning message for a sharing violation.

To prevent the display of the standard warning message, return a nonzero value from the hook procedure and call the [**SetWindowLong**](https://msdn.microsoft.com/library/windows/desktop/ms633591) function to set one of the following **DWL\_MSGRESULT** values.



| Return code/value                                                                                                                                           | Description                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**OFN\_SHAREFALLTHROUGH**</dt> <dt>2</dt> </dl> | Causes the dialog box to return the file name without warning the user about the sharing violation.<br/>  |
| <dl> <dt>**OFN\_SHARENOWARN**</dt> <dt>1</dt> </dl>      | Causes the dialog box to reject the file name without warning the user about the sharing violation. <br/> |



 

## Remarks

The system sends this notification only if the dialog box was created using the **OFN\_EXPLORER** value.

The system sends this notification only if the **OFN\_SHAREAWARE** value was not specified when the dialog box was created.

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

[*OFNHookProc*](https://www.bing.com/search?q=*OFNHookProc*)
</dt> <dt>

[**OFNOTIFY**](/windows/desktop/api/Commdlg/ns-commdlg-_ofnotifya)
</dt> <dt>

[**OPENFILENAME**](/windows/desktop/api/Commdlg/ns-commdlg-tagofna)
</dt> <dt>

[**SetWindowLong**](https://msdn.microsoft.com/library/windows/desktop/ms633591)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Common Dialog Box Library](common-dialog-box-library.md)
</dt> </dl>

 

 





