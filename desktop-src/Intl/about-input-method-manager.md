---
Description: Use of the IMM functionality in your IME-aware application relieves users of the need to remember all possible character values.
ms.assetid: 43b3e561-b844-4688-ab3d-d99f92ed140e
title: About Input Method Manager
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# About Input Method Manager

Use of the IMM functionality in your IME-aware application relieves users of the need to remember all possible character values. Instead, it allows the IME to monitor a user's keystrokes, anticipates the characters the user might want, and presents a list of candidate characters from which to choose.

> [!Note]  
> The IMM performs similar operations to those of the [Text Services Framework](https://msdn.microsoft.com/ecc34b2e-89e8-48a8-8a8e-442d2145fe24), used by applications that communicate with text services.

 

By default, the IMM provides an IME window through which the user enters keystrokes and views and selects candidates. Applications can use the IMM functions and messages to create and manage their own IME windows, providing a custom interface while using the conversion capabilities of the IME.

The IMM is only enabled on East Asian (Chinese, Japanese, Korean) localized Windows operating systems. On these systems, the application calls [GetSystemMetrics](https://www.bing.com/search?q=GetSystemMetrics) with SM\_DBCSENABLED to determine if the IMM is enabled.

**Windows 2000:** Full-featured IMM support is provided in all localized language versions. However, the IMM is enabled only when an Asian language pack is installed. An IME-aware application can call [GetSystemMetrics](https://www.bing.com/search?q=GetSystemMetrics) with SM\_IMMENABLED to determine if the IMM is enabled.

This topic contains the following sections.

-   [Candidate Lists](candidate-lists.md)
-   [Composition String](composition-string.md)
-   [HexToUnicode IME](hextounicode-ime.md)
-   [Hot Keys](hot-keys.md)
-   [IME Messages](ime-messages.md)
-   [IME Window Class](ime-window-class.md)
-   [Input Context](input-context.md)
-   [Status, Composition, and Candidates Windows](status--composition--and-candidates-windows.md)

 

 



