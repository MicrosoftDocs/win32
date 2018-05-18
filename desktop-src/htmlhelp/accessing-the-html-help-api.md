---
title: Accessing the HTML Help API
description: The functionality provided by the HTML Help API resides in the HTML Help ActiveX control (Hhctrl.ocx), which is installed when you set up HTML Help Workshop.
ms.assetid: 'CEC91F48-11CE-4187-B6DB-21C3FB100784'
---

# Accessing the HTML Help API

The functionality provided by the HTML Help API resides in the HTML Help ActiveX control (Hhctrl.ocx), which is installed when you set up HTML Help Workshop.

To gain access to the HTML Help API, you link to the Htmlhelp.lib file and include the Htmlhelp.h file in your Windows program. Both of these files are installed on your system when you set up HTML Help Workshop.

## About Htmlhelp.lib

Htmlhelp.lib is an export library that exposes the HTML Help API and loads Hhctrl.ocx only when **HtmlHelp()** is called. In addition, Htmlhelp.lib locates the registered Hhctrl.ocx.

By default, Htmlhelp.lib is located in the following directory:

C:\\Program Files\\HTML Help Workshop\\Lib

> [!Note]  
> In later versions of Windows, Htmlhelp.lib is located in the following directory: C:\\Program Files (x86)\\HTML Help Workshop\\Lib

 

## About Htmlhelp.h

Htmlhelp.h is a header file that contains the declarations for **HtmlHelp()**. It must be included in your Windows program.

By default, Htmlhelp.h is located in the following directory:

C:\\Program Files\\HTML Help Workshop\\Include

> [!Note]  
> In later versions of Windows, Htmlhelp.h is located in the following directory: C:\\Program Files (x86)\\HTML Help Workshop\\Include

 

## Notes

-   Copy Htmlhelp.lib to your Lib folder and Htmlhelp.h to your Include folder, so the compiler can find these files.
-   If you are using the HTML Help API with Windows 95 and Internet Explorer 3.x, you must either set up [DCOM for Microsoft Windows 95, version 1.2](http://microsoft.com/com/tech/dcom.asp), or set up [Internet Explorer](http://www.microsoft.com/windows/ie/default.md), version 4 or later. Otherwise, the calls that you make to **HtmlHelp()** may not be processed correctly.

## Related topics

<dl> <dt>

[About the HTML Help API](html-help-api-overview.md)
</dt> </dl>

 

 




