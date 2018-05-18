---
Description: 'This topic describes how to manage logging categories in the Microsoft Win32 environment.'
ms.assetid: '958fecf7-a787-4f86-bc67-53f7564ec43a'
title: Managing Logging Categories
---

# Managing Logging Categories

This functionality is currently available only in the Microsoft Win32 environment. It is not available in the Component Object Model (COM) implementation environment.

A logging category determines the type of errors or other events the fax server logs in the application event log. A logging level describes the severity of events the fax server logs. For a description of predefined logging categories and logging levels, see the [**FAX\_LOG\_CATEGORY**](-mfax-fax-log-category-str.md) topic.

The [**FaxGetLoggingCategories**](-mfax-faxgetloggingcategories.md) function permits a fax client application to query the current logging categories for the fax server. The function returns the information in one or more [**FAX\_LOG\_CATEGORY**](-mfax-fax-log-category-str.md) structures. Each structure describes one current logging category. The data includes the descriptive name of the logging category, the category number, and the current logging level. Because the **FaxGetLoggingCategories** function allocates the memory required for the **FAX\_LOG\_CATEGORY** structures, the application must call the [**FaxFreeBuffer**](-mfax-faxfreebuffer.md) function to deallocate these resources.

To modify a fax server's global configuration settings, an application can call the [**FaxSetLoggingCategories**](-mfax-faxsetloggingcategories.md) function.

Note that an application must first call the [**FaxConnectFaxServer**](-mfax-faxconnectfaxserver.md) function to obtain a fax server handle before calling the [**FaxGetLoggingCategories**](-mfax-faxgetloggingcategories.md) function and the [**FaxSetLoggingCategories**](-mfax-faxsetloggingcategories.md) function.

 

 



