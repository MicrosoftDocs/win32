---
title: Active Accessibility Text Services
description: The following Active Accessibility Text Services interfaces are available in msaatext.dll. For more information about these interfaces, see Active Accessibility Text Services.
ms.assetid: 2e007f26-9d4a-440f-a564-f785c914f236
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Active Accessibility Text Services

The following Active Accessibility Text Services interfaces are available in msaatext.dll. For more information about these interfaces, see [Active Accessibility Text Services](active-accessibility-text-services-collision227.md).

> [!Note]  
> Active Accessibility Text Services is deprecated. Please see [Microsoft Windows Text Services Framework](http://go.microsoft.com/fwlink/p/?linkid=131573) for more information on advanced text input and natural language technologies.

 



|                                              |                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IAccServerDocMgr**](/windows/win32/msaatext/nn-msaatext-iaccserverdocmgr?branch=master) | Servers use this interface to present the [ITextStoreAnchor](http://go.microsoft.com/fwlink/p/?linkid=178215) interface to the system, and to make it available for clients. Servers use this interface if they do not support Text Services Framework, but want their documents to be accessible. |
| [**IAccClientDocMgr**](/windows/win32/msaatext/nn-msaatext-iaccclientdocmgr?branch=master) | Clients use this interface to obtain interface pointers to currently available documents.                                                                                                                                                                                                          |
| [**IAccDictionary**](/windows/win32/msaatext/nn-msaatext-iaccdictionary?branch=master)     | This interface provides the default dictionary for Active Accessibility Text Services. The default dictionary provides localized strings for all system properties. Servers implement this interface when they want to expose custom property GUIDs for their documents.                           |



 

 

 




