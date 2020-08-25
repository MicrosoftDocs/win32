---
title: Using a Multiple Document Interface
description: Using a Multiple Document Interface
ms.assetid: bc59f19c-1064-4df8-8864-38e6d188f92f
keywords:
- MCIWndRegisterClass function
ms.topic: article
ms.date: 05/31/2018
---

# Using a Multiple Document Interface

Applications that use a multiple document interface (MDI) might need to specify window styles that are not available through the [**MCIWndCreate**](/windows/desktop/api/Vfw/nf-vfw-mciwndcreatea) function. For these applications, you can register and create an MCIWnd window by using the [**MCIWndRegisterClass**](/windows/desktop/api/Vfw/nf-vfw-mciwndregisterclass) function with the [CreateWindowEx](/windows/win32/api/winuser/nf-winuser-createwindowexa) function. The **MCIWndRegisterClass** function registers the MCIWND\_WINDOW\_CLASS window class and then **CreateWindowEx** creates an instance of an MCIWnd window.

 

 