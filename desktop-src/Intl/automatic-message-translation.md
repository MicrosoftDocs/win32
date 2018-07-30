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

[CB\_ADDSTRING](https://msdn.microsoft.com/library/Bb775828(v=VS.85).aspx)  
[CB\_DIR](https://msdn.microsoft.com/library/Bb775832(v=VS.85).aspx)  
[CB\_FINDSTRING](https://msdn.microsoft.com/library/Bb775835(v=VS.85).aspx)  
[CB\_GETLBTEXT](https://msdn.microsoft.com/library/Bb775862(v=VS.85).aspx)  
[CB\_INSERTSTRING](https://msdn.microsoft.com/library/Bb775875(v=VS.85).aspx)  
[CB\_SELECTSTRING](https://msdn.microsoft.com/library/Bb775895(v=VS.85).aspx)  
[EM\_GETLINE](https://msdn.microsoft.com/library/Bb761584(v=VS.85).aspx)  
[EM\_REPLACESEL](https://msdn.microsoft.com/library/Bb761633(v=VS.85).aspx)  
[EM\_SETPASSWORDCHAR](https://msdn.microsoft.com/library/Bb761653(v=VS.85).aspx)  
[LB\_ADDFILE](https://msdn.microsoft.com/library/Bb775165(v=VS.85).aspx)  
[LB\_ADDSTRING](https://msdn.microsoft.com/library/Bb775181(v=VS.85).aspx)  
[LB\_DIR](https://msdn.microsoft.com/library/Bb775185(v=VS.85).aspx)  
[LB\_FINDSTRING](https://msdn.microsoft.com/library/Bb775187(v=VS.85).aspx)  
[LB\_GETTEXT](https://msdn.microsoft.com/library/Bb761313(v=VS.85).aspx)  
[LB\_INSERTSTRING](https://msdn.microsoft.com/library/Bb761321(v=VS.85).aspx)  
[LB\_SELECTSTRING](https://msdn.microsoft.com/library/Bb761327(v=VS.85).aspx)  
[WM\_ASKCBFORMATNAME](https://msdn.microsoft.com/library/ms649018(v=VS.85).aspx)  
[WM\_CHAR](https://msdn.microsoft.com/library/ms646276(v=VS.85).aspx)  
[WM\_CHARTOITEM](https://msdn.microsoft.com/library/Bb761358(v=VS.85).aspx)  
[WM\_CREATE](https://msdn.microsoft.com/library/ms632619(v=VS.85).aspx)  
[WM\_DEADCHAR](https://msdn.microsoft.com/library/ms646277(v=VS.85).aspx)  
[WM\_DEVMODECHANGE](https://msdn.microsoft.com/library/Dd145209(v=VS.85).aspx)  
[WM\_GETTEXT](https://msdn.microsoft.com/library/ms632627(v=VS.85).aspx)  
[WM\_MDICREATE](https://msdn.microsoft.com/library/ms644913(v=VS.85).aspx)  
[WM\_MENUCHAR](https://msdn.microsoft.com/library/ms646349(v=VS.85).aspx)  
[WM\_NCCREATE](https://msdn.microsoft.com/library/ms632635(v=VS.85).aspx)  
[WM\_SETTEXT](https://msdn.microsoft.com/library/ms632644(v=VS.85).aspx)  
[WM\_SYSCHAR](https://msdn.microsoft.com/library/ms646357(v=VS.85).aspx)  
[WM\_SYSDEADCHAR](https://msdn.microsoft.com/library/ms646285(v=VS.85).aspx)  
[WM\_WININICHANGE](https://msdn.microsoft.com/library/ms725499(v=VS.85).aspx)  
</dl>

## Related topics

<dl> <dt>

[Unicode in the Windows API](unicode-in-the-windows-api.md)
</dt> </dl>

 

 



