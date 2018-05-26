---
Description: This topic describes how to manage logging categories in the Microsoft Win32 environment.
ms.assetid: 958fecf7-a787-4f86-bc67-53f7564ec43a
title: Managing Logging Categories
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Managing Logging Categories

This functionality is currently available only in the Microsoft Win32 environment. It is not available in the Component Object Model (COM) implementation environment.

A logging category determines the type of errors or other events the fax server logs in the application event log. A logging level describes the severity of events the fax server logs. For a description of predefined logging categories and logging levels, see the [**FAX\_LOG\_CATEGORY**](/windows/previous-versions/Winfax/ns-winfax-_fax_log_categorya?branch=master) topic.

The [**FaxGetLoggingCategories**](/windows/previous-versions/Winfax/nf-winfax-faxgetloggingcategoriesa?branch=master) function permits a fax client application to query the current logging categories for the fax server. The function returns the information in one or more [**FAX\_LOG\_CATEGORY**](/windows/previous-versions/Winfax/ns-winfax-_fax_log_categorya?branch=master) structures. Each structure describes one current logging category. The data includes the descriptive name of the logging category, the category number, and the current logging level. Because the **FaxGetLoggingCategories** function allocates the memory required for the **FAX\_LOG\_CATEGORY** structures, the application must call the [**FaxFreeBuffer**](/windows/previous-versions/Winfax/nc-winfax-pfaxfreebuffer?branch=master) function to deallocate these resources.

To modify a fax server's global configuration settings, an application can call the [**FaxSetLoggingCategories**](/windows/previous-versions/Winfax/nf-winfax-faxsetloggingcategoriesa?branch=master) function.

Note that an application must first call the [**FaxConnectFaxServer**](/windows/previous-versions/Winfax/nf-winfax-faxconnectfaxservera?branch=master) function to obtain a fax server handle before calling the [**FaxGetLoggingCategories**](/windows/previous-versions/Winfax/nf-winfax-faxgetloggingcategoriesa?branch=master) function and the [**FaxSetLoggingCategories**](/windows/previous-versions/Winfax/nf-winfax-faxsetloggingcategoriesa?branch=master) function.

 

 



