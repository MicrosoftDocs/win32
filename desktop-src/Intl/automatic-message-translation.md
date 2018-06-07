---
Description: Applications using the Unicode and character set API functions generally use the same window class. The operating system transparently translates messages between windows of different classes.
ms.assetid: 68e9839b-39f8-411a-8ae4-4a627c667cae
title: Automatic Message Translation
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Automatic Message Translation

Applications using the Unicode and character set API functions generally use the same window class. The operating system transparently translates messages between windows of different classes.

A window function is implemented to receive messages in Unicode or Windows code page format. The window function can send messages or call functions of either type.

The following messages have text arguments and are subject to automatic text translation. For information about automatic translation, see [Subclassing and Automatic Message Translation](subclassing-and-automatic-message-translation.md).

<dl>

[CB\_ADDSTRING](https://www.bing.com/search?q=CB\_ADDSTRING)  
[CB\_DIR](https://www.bing.com/search?q=CB\_DIR)  
[CB\_FINDSTRING](https://www.bing.com/search?q=CB\_FINDSTRING)  
[CB\_GETLBTEXT](https://www.bing.com/search?q=CB\_GETLBTEXT)  
[CB\_INSERTSTRING](https://www.bing.com/search?q=CB\_INSERTSTRING)  
[CB\_SELECTSTRING](https://www.bing.com/search?q=CB\_SELECTSTRING)  
[EM\_GETLINE](https://www.bing.com/search?q=EM\_GETLINE)  
[EM\_REPLACESEL](https://www.bing.com/search?q=EM\_REPLACESEL)  
[EM\_SETPASSWORDCHAR](https://www.bing.com/search?q=EM\_SETPASSWORDCHAR)  
[LB\_ADDFILE](https://www.bing.com/search?q=LB\_ADDFILE)  
[LB\_ADDSTRING](https://www.bing.com/search?q=LB\_ADDSTRING)  
[LB\_DIR](https://www.bing.com/search?q=LB\_DIR)  
[LB\_FINDSTRING](https://www.bing.com/search?q=LB\_FINDSTRING)  
[LB\_GETTEXT](https://www.bing.com/search?q=LB\_GETTEXT)  
[LB\_INSERTSTRING](https://www.bing.com/search?q=LB\_INSERTSTRING)  
[LB\_SELECTSTRING](https://www.bing.com/search?q=LB\_SELECTSTRING)  
[WM\_ASKCBFORMATNAME](https://www.bing.com/search?q=WM\_ASKCBFORMATNAME)  
[WM\_CHAR](https://www.bing.com/search?q=WM\_CHAR)  
[WM\_CHARTOITEM](https://www.bing.com/search?q=WM\_CHARTOITEM)  
[WM\_CREATE](https://www.bing.com/search?q=WM\_CREATE)  
[WM\_DEADCHAR](https://www.bing.com/search?q=WM\_DEADCHAR)  
[WM\_DEVMODECHANGE](https://www.bing.com/search?q=WM\_DEVMODECHANGE)  
[WM\_GETTEXT](https://www.bing.com/search?q=WM\_GETTEXT)  
[WM\_MDICREATE](https://www.bing.com/search?q=WM\_MDICREATE)  
[WM\_MENUCHAR](https://www.bing.com/search?q=WM\_MENUCHAR)  
[WM\_NCCREATE](https://www.bing.com/search?q=WM\_NCCREATE)  
[WM\_SETTEXT](https://www.bing.com/search?q=WM\_SETTEXT)  
[WM\_SYSCHAR](https://www.bing.com/search?q=WM\_SYSCHAR)  
[WM\_SYSDEADCHAR](https://www.bing.com/search?q=WM\_SYSDEADCHAR)  
[WM\_WININICHANGE](https://www.bing.com/search?q=WM\_WININICHANGE)  
</dl>

## Related topics

<dl> <dt>

[Unicode in the Windows API](unicode-in-the-windows-api.md)
</dt> </dl>

 

 



