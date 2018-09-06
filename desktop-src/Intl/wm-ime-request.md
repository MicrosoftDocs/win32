---
Description: Sent to an application to provide commands and request information. A window receives this message through its WindowProc function.
ms.assetid: c5e9f256-eed2-46cb-bb33-0e640a975f1f
title: WM_IME_REQUEST message
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WM\_IME\_REQUEST message

Sent to an application to provide commands and request information. A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/library/ms633573(v=VS.85).aspx) function.


```C++
LRESULT CALLBACK WindowProc(
  HWND  hwnd,       
  WM_IME_REQUEST,  
  WPARAM wParam,   
  LPARAM lParam    
);
```



## Parameters

<dl> <dt>

*hwnd* 
</dt> <dd>

A handle to window.

</dd> <dt>

*wParam* 
</dt> <dd>

Command. This parameter can have one of the following values:

<dl> <dd>[IMR\_CANDIDATEWINDOW](imr-candidatewindow.md)</dd> <dd>[IMR\_COMPOSITIONFONT](imr-compositionfont.md)</dd> <dd>[IMR\_COMPOSITIONWINDOW](imr-compositionwindow.md)</dd> <dd>[IMR\_CONFIRMRECONVERTSTRING](imr-confirmreconvertstring.md)</dd> <dd>[IMR\_DOCUMENTFEED](imr-documentfeed.md)</dd> <dd>[IMR\_QUERYCHARPOSITION](imr-querycharposition.md)</dd> <dd>[IMR\_RECONVERTSTRING](imr-reconvertstring.md)</dd> </dl> </dd> <dt>

*lParam* 
</dt> <dd>

Command-specific data. For more information, see the description for each command.

</dd> </dl>

## Return value

Returns a command-specific value.

## Requirements



|                                     |                                                                                                                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                                                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                                                                      |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h); </dt> <dt>Imm.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Input Method Manager](input-method-manager.md)
</dt> <dt>

[Input Method Manager Messages](input-method-manager-messages.md)
</dt> <dt>

[IMR\_CANDIDATEWINDOW](imr-candidatewindow.md)
</dt> <dt>

[IMR\_COMPOSITIONFONT](imr-compositionfont.md)
</dt> <dt>

[IMR\_COMPOSITIONWINDOW](imr-compositionwindow.md)
</dt> <dt>

[IMR\_CONFIRMRECONVERTSTRING](imr-confirmreconvertstring.md)
</dt> <dt>

[IMR\_DOCUMENTFEED](imr-documentfeed.md)
</dt> <dt>

[IMR\_QUERYCHARPOSITION](imr-querycharposition.md)
</dt> <dt>

[IMR\_RECONVERTSTRING](imr-reconvertstring.md)
</dt> </dl>

 

 




