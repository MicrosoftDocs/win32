---
title: Adding User-Controlled Playback
description: Adding User-Controlled Playback
ms.assetid: 'c865bbc1-f78a-4d88-ab60-fba76818d175'
keywords: ["MCIWndCreate function"]
---

# Adding User-Controlled Playback

You can add user-controlled playback to an existing application by calling the [**MCIWndCreate**](mciwndcreate.md) function as follows:


```C++
MCIWndCreate(hwndParent, hInstModule, NULL, "filename.typ"); 
```



The [**MCIWndCreate**](mciwndcreate.md) parameters identify handles to the parent window and to the module instance associated with the MCIWnd window. They also specify window styles and the filename (or device name) to associate with the MCIWnd window.

**MCIWndCreate** automatically performs the following steps that, for other window classes, you would implement in your code yourself:

1.  Register the MCIWnd window class.
2.  Create the MCIWnd window.
3.  Load the specified content.
4.  Establish the current playback position at the beginning of the content.
5.  Display the device control.
6.  Display the playback area of the window, if needed.

 

 




