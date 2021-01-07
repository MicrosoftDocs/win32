---
description: Applications using the Unicode and character set API functions generally use the same window class. The operating system transparently translates messages between windows of different classes.
ms.assetid: 68e9839b-39f8-411a-8ae4-4a627c667cae
title: Automatic Message Translation
ms.topic: article
ms.date: 05/31/2018
---

# Automatic Message Translation

Applications using the Unicode and character set API functions generally use the same window class. The operating system transparently translates messages between windows of different classes.

A window function is implemented to receive messages in Unicode or Windows code page format. The window function can send messages or call functions of either type.

The following messages have text arguments and are subject to automatic text translation. For information about automatic translation, see [Subclassing and Automatic Message Translation](subclassing-and-automatic-message-translation.md).

<dl>

[CB\_ADDSTRING](../controls/cb-addstring.md)  
[CB\_DIR](../controls/cb-dir.md)  
[CB\_FINDSTRING](../controls/cb-findstring.md)  
[CB\_GETLBTEXT](../controls/cb-getlbtext.md)  
[CB\_INSERTSTRING](../controls/cb-insertstring.md)  
[CB\_SELECTSTRING](../controls/cb-selectstring.md)  
[EM\_GETLINE](../controls/em-getline.md)  
[EM\_REPLACESEL](../controls/em-replacesel.md)  
[EM\_SETPASSWORDCHAR](../controls/em-setpasswordchar.md)  
[LB\_ADDFILE](../controls/lb-addfile.md)  
[LB\_ADDSTRING](../controls/lb-addstring.md)  
[LB\_DIR](../controls/lb-dir.md)  
[LB\_FINDSTRING](../controls/lb-findstring.md)  
[LB\_GETTEXT](../controls/lb-gettext.md)  
[LB\_INSERTSTRING](../controls/lb-insertstring.md)  
[LB\_SELECTSTRING](../controls/lb-selectstring.md)  
[WM\_ASKCBFORMATNAME](../dataxchg/wm-askcbformatname.md)  
[WM\_CHAR](../inputdev/wm-char.md)  
[WM\_CHARTOITEM](../controls/wm-chartoitem.md)  
[WM\_CREATE](../winmsg/wm-create.md)  
[WM\_DEADCHAR](../inputdev/wm-deadchar.md)  
[WM\_DEVMODECHANGE](../gdi/wm-devmodechange.md)  
[WM\_GETTEXT](../winmsg/wm-gettext.md)  
[WM\_MDICREATE](../winmsg/wm-mdicreate.md)  
[WM\_MENUCHAR](../menurc/wm-menuchar.md)  
[WM\_NCCREATE](../winmsg/wm-nccreate.md)  
[WM\_SETTEXT](../winmsg/wm-settext.md)  
[WM\_SYSCHAR](../menurc/wm-syschar.md)  
[WM\_SYSDEADCHAR](../inputdev/wm-sysdeadchar.md)  
[WM\_WININICHANGE](../winmsg/wm-wininichange.md)  
</dl>

## Related topics

<dl> <dt>

[Unicode in the Windows API](unicode-in-the-windows-api.md)
</dt> </dl>

 

 
