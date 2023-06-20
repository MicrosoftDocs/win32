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
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Functions Called by the System

\[The feature associated with this page, [﻿Audio Compression Manager](/windows/win32/multimedia/audio-compression-manager), is a legacy feature. Microsoft strongly recommends that new code does not use this feature.\]

The system calls three different kinds of application-defined functions. Callback functions are functions in your application that the system calls in response to a request made by an application. Hook procedures help an application handle the customization of dialog boxes. A driver procedure is an application's implementation of its own codec, converter, or filter.

The callback functions have the following names:

-   [**acmDriverEnumCallback**](/windows/win32/api/msacm/nc-msacm-acmdriverenumcb)
-   [**acmFilterEnumCallback**](/windows/desktop/api/Msacm/nc-msacm-acmfilterenumcb)
-   [**acmFilterTagEnumCallback**](/windows/desktop/api/Msacm/nc-msacm-acmfiltertagenumcb)
-   [**acmFormatEnumCallback**](/windows/desktop/api/Msacm/nc-msacm-acmformatenumcb)
-   [**acmFormatTagEnumCallback**](/windows/desktop/api/Msacm/nc-msacm-acmformattagenumcb)
-   [**acmStreamConvertCallback**](/previous-versions//dd742925(v=vs.85))

Most of the enumeration functions in the ACM use callback functions. For example, when you call an enumeration function, the ACM enumerates the items by repeatedly calling the application through the callback function.

Some functions cannot be called from within these callback functions. Functions that cannot be called manipulate internal ACM structures that are used by the enumeration functions. The following functions should not be called from within a callback function:

-   [**acmDriverAdd**](/windows/desktop/api/Msacm/nf-msacm-acmdriveradd)
-   [**acmDriverPriority**](/windows/desktop/api/Msacm/nf-msacm-acmdriverpriority)
-   [**acmDriverRemove**](/windows/desktop/api/Msacm/nf-msacm-acmdriverremove)

The system calls the following functions to help an application handle the customization of dialog boxes:

-   [**acmFilterChooseHookProc**](/windows/desktop/api/Msacm/nc-msacm-acmfilterchoosehookproc)
-   [**acmFormatChooseHookProc**](/windows/desktop/api/Msacm/nc-msacm-acmformatchoosehookproc)

The following function is specified as a prototype that allows an application to use a customized codec, converter, or filter. A function conforming to this prototype may be passed as an argument to the [**acmDriverAdd**](/windows/desktop/api/Msacm/nf-msacm-acmdriveradd) function.

-   [**acmDriverProc**](/windows/desktop/api/Msacm/nc-msacm-acmdriverproc)

 

 