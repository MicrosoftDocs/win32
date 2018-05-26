---
Description: Applications using the Unicode and character set API functions generally use the same window class. The operating system transparently translates messages between windows of different classes.
ms.assetid: 68e9839b-39f8-411a-8ae4-4a627c667cae
title: Automatic Message Translation
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Automatic Message Translation

Applications using the Unicode and character set API functions generally use the same window class. The operating system transparently translates messages between windows of different classes.

A window function is implemented to receive messages in Unicode or Windows code page format. The window function can send messages or call functions of either type.

The following messages have text arguments and are subject to automatic text translation. For information about automatic translation, see [Subclassing and Automatic Message Translation](subclassing-and-automatic-message-translation.md).

<dl>

[CB\_ADDSTRING](_win32_cb_addstring_cpp)  
[CB\_DIR](_win32_cb_dir_cpp)  
[CB\_FINDSTRING](_win32_cb_findstring_cpp)  
[CB\_GETLBTEXT](_win32_cb_getlbtext_cpp)  
[CB\_INSERTSTRING](_win32_cb_insertstring_cpp)  
[CB\_SELECTSTRING](_win32_cb_selectstring_cpp)  
[EM\_GETLINE](_win32_em_getline_cpp)  
[EM\_REPLACESEL](_win32_em_replacesel_cpp)  
[EM\_SETPASSWORDCHAR](_win32_em_setpasswordchar_cpp)  
[LB\_ADDFILE](_win32_lb_addfile_cpp)  
[LB\_ADDSTRING](_win32_lb_addstring_cpp)  
[LB\_DIR](_win32_lb_dir_cpp)  
[LB\_FINDSTRING](_win32_lb_findstring_cpp)  
[LB\_GETTEXT](_win32_lb_gettext_cpp)  
[LB\_INSERTSTRING](_win32_lb_insertstring_cpp)  
[LB\_SELECTSTRING](_win32_lb_selectstring_cpp)  
[WM\_ASKCBFORMATNAME](_win32_wm_askcbformatname_cpp)  
[WM\_CHAR](_win32_wm_char_cpp)  
[WM\_CHARTOITEM](_win32_wm_chartoitem_cpp)  
[WM\_CREATE](_win32_wm_create_cpp)  
[WM\_DEADCHAR](_win32_wm_deadchar_cpp)  
[WM\_DEVMODECHANGE](_win32_wm_devmodechange_cpp)  
[WM\_GETTEXT](_win32_wm_gettext_cpp)  
[WM\_MDICREATE](_win32_wm_mdicreate_cpp)  
[WM\_MENUCHAR](_win32_wm_menuchar_cpp)  
[WM\_NCCREATE](_win32_wm_nccreate_cpp)  
[WM\_SETTEXT](_win32_wm_settext_cpp)  
[WM\_SYSCHAR](_win32_wm_syschar_cpp)  
[WM\_SYSDEADCHAR](_win32_wm_sysdeadchar_cpp)  
[WM\_WININICHANGE](_win32_wm_wininichange_cpp)  
</dl>

## Related topics

<dl> <dt>

[Unicode in the Windows API](unicode-in-the-windows-api.md)
</dt> </dl>

 

 



