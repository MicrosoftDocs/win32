---
title: EM_GETHANDLE message (Winuser.h)
description: Gets a handle of the memory currently allocated for a multiline edit control's text.
ms.assetid: 74271812-9715-4a46-96b3-0788134f8143
keywords:
- EM_GETHANDLE message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETHANDLE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_GETHANDLE message

Gets a handle of the memory currently allocated for a multiline edit control's text.

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

The return value is a memory handle identifying the buffer that holds the content of the edit control. If an error occurs, such as sending the message to a single-line edit control, the return value is zero.

## Remarks

If the function succeeds, the application can access the contents of the edit control by casting the return value to [**HLOCAL**](/windows/desktop/WinProg/windows-data-types) and passing it to [**LocalLock**](/windows/desktop/api/winbase/nf-winbase-locallock). **LocalLock** returns a pointer to a buffer that is a null-terminated array of **CHAR**s or **WCHAR**s, depending on whether an ANSI or Unicode function created the control. For example, if [**CreateWindowExA**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) was used the buffer is an array of **CHAR**s, but if **CreateWindowExW** was used the buffer is an array of **WCHAR**s. The application may not change the contents of the buffer. To unlock the buffer, the application calls [**LocalUnlock**](/windows/desktop/api/winbase/nf-winbase-localunlock) before allowing the edit control to receive new messages.

> [!Note]  
> For Comctl32.dll version 6, the buffer always contains an array of **WCHAR**s, regardless of whether an ANSI or Unicode function created the edit control. For more information on DLL versions, see [Common Control Versions](common-control-versions.md).

 

If your application cannot abide by the restrictions imposed by **EM\_GETHANDLE**, use the [**GetWindowTextLength**](/windows/desktop/api/winuser/nf-winuser-getwindowtextlengtha) and [**GetWindowText**](/windows/desktop/api/winuser/nf-winuser-getwindowtexta) functions to copy the contents of the edit control into an application-provided buffer.

**Rich Edit:** The **EM\_GETHANDLE** message is not supported. Rich edit controls do not store text as a simple array of characters.

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

[**EM\_SETHANDLE**](em-sethandle.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**GetWindowText**](/windows/desktop/api/winuser/nf-winuser-getwindowtexta)
</dt> <dt>

[**GetWindowTextLength**](/windows/desktop/api/winuser/nf-winuser-getwindowtextlengtha)
</dt> <dt>

[**LocalLock**](/windows/desktop/api/winbase/nf-winbase-locallock)
</dt> <dt>

[**LocalUnlock**](/windows/desktop/api/winbase/nf-winbase-localunlock)
</dt> </dl>

 

