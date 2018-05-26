---
title: Functions Called by the System
description: Functions Called by the System
ms.assetid: 006ac524-d456-44e9-957b-42a85dc92519
keywords:
- multimedia audio,ACM functions
- audio,ACM functions
- audio compression manager (ACM),functions
- ACM (audio compression manager),functions
- ACM functions
- callback functions
- audio compression manager (ACM),callback functions
- ACM (audio compression manager),callback functions
- hook procedures
- driver procedures
- audio compression manager (ACM),hook procedures
- ACM (audio compression manager),hook procedures
- audio compression manager (ACM),driver procedures
- ACM (audio compression manager),driver procedures
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Functions Called by the System

The system calls three different kinds of application-defined functions. Callback functions are functions in your application that the system calls in response to a request made by an application. Hook procedures help an application handle the customization of dialog boxes. A driver procedure is an application's implementation of its own codec, converter, or filter.

The callback functions have the following names:

-   [**acmDriverEnumCallback**](/windows/win32/Msacm/nc-msacm-acmdriverenumcb?branch=master)
-   [**acmFilterEnumCallback**](/windows/win32/Msacm/nc-msacm-acmfilterenumcb?branch=master)
-   [**acmFilterTagEnumCallback**](/windows/win32/Msacm/nc-msacm-acmfiltertagenumcb?branch=master)
-   [**acmFormatEnumCallback**](/windows/win32/Msacm/nc-msacm-acmformatenumcb?branch=master)
-   [**acmFormatTagEnumCallback**](/windows/win32/Msacm/nc-msacm-acmformattagenumcb?branch=master)
-   [**acmStreamConvertCallback**](https://msdn.microsoft.com/library/windows/desktop/dd742925)

Most of the enumeration functions in the ACM use callback functions. For example, when you call an enumeration function, the ACM enumerates the items by repeatedly calling the application through the callback function.

Some functions cannot be called from within these callback functions. Functions that cannot be called manipulate internal ACM structures that are used by the enumeration functions. The following functions should not be called from within a callback function:

-   [**acmDriverAdd**](/windows/win32/Msacm/nf-msacm-acmdriveradd?branch=master)
-   [**acmDriverPriority**](/windows/win32/Msacm/nf-msacm-acmdriverpriority?branch=master)
-   [**acmDriverRemove**](/windows/win32/Msacm/nf-msacm-acmdriverremove?branch=master)

The system calls the following functions to help an application handle the customization of dialog boxes:

-   [**acmFilterChooseHookProc**](/windows/win32/Msacm/nc-msacm-acmfilterchoosehookproc?branch=master)
-   [**acmFormatChooseHookProc**](/windows/win32/Msacm/nc-msacm-acmformatchoosehookproc?branch=master)

The following function is specified as a prototype that allows an application to use a customized codec, converter, or filter. A function conforming to this prototype may be passed as an argument to the [**acmDriverAdd**](/windows/win32/Msacm/nf-msacm-acmdriveradd?branch=master) function.

-   [**acmDriverProc**](/windows/win32/Msacm/nc-msacm-acmdriverproc?branch=master)

 

 




