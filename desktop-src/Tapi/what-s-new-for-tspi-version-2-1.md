---
Description: 'Starting with TAPI 2.1, the telephony service provider user interface DLLs can be used to manage and display dialog boxes. TAPI loads the DLL into the process of an application that invokes any of the service provider functions that can display a dialog.'
ms.assetid: '0a0320d1-fb75-405e-8074-b37cef956c9f'
title: 'What's New for TSPI Version 2.1'
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# What's New for TSPI Version 2.1

Starting with TAPI 2.1, the telephony service provider user interface DLLs can be used to manage and display dialog boxes. TAPI loads the DLL into the process of an application that invokes any of the service provider functions that can display a dialog.

Starting with TAPI 2.1, proxy request handlers can be implemented. A handler is a full telephony application that normally executes on a telephony server and provides services that are more appropriately implemented in an application than a driver.

Functions and messages that were new or changed for TSPI version 2.1 are as follows:

-   [**TSPI\_lineConditionalMediaDetection**](https://msdn.microsoft.com/en-us/library/ms725536(v=VS.85).aspx)
-   **TSPI\_lineDropNoOwner**—**obsolete**
-   **TSPI\_lineDropOnClose**—**obsolete**
-   [**TSPI\_lineGetID**](https://msdn.microsoft.com/en-us/library/ms725572(v=VS.85).aspx)
-   [**TSPI\_lineSetCallData**](https://msdn.microsoft.com/en-us/library/ms725595(v=VS.85).aspx)
-   [**TSPI\_lineSetCallQualityOfService**](https://msdn.microsoft.com/en-us/library/ms725598(v=VS.85).aspx)
-   [**TSPI\_lineSetCallTreatment**](https://msdn.microsoft.com/en-us/library/ms725599(v=VS.85).aspx)
-   [**TSPI\_lineSetLineDevStatus**](https://msdn.microsoft.com/en-us/library/ms725603(v=VS.85).aspx)
-   [**TSPI\_phoneGetID**](https://msdn.microsoft.com/en-us/library/ms725934(v=VS.85).aspx)
-   [**TSPI\_providerInit**](https://msdn.microsoft.com/en-us/library/ms725960(v=VS.85).aspx)
-   [**TSPI\_providerShutdown**](https://msdn.microsoft.com/en-us/library/ms725963(v=VS.85).aspx)
-   [**LINE\_GATHERDIGITS**](https://msdn.microsoft.com/library/ms725229)
-   [**LINE\_GENERATE**](https://msdn.microsoft.com/library/ms725230)
-   [**LINE\_MONITORDIGITS**](https://msdn.microsoft.com/library/ms725232)
-   [**LINE\_MONITORMEDIA**](https://msdn.microsoft.com/library/ms725233)
-   [**LINE\_MONITORTONE**](https://msdn.microsoft.com/library/ms725234)
-   [**LINE\_REMOVE**](https://msdn.microsoft.com/library/ms725237)
-   [**PHONE\_REMOVE**](https://msdn.microsoft.com/library/ms725260)

The Telephony service provider user interface DLL provides a means of allowing user interaction within the context of the application rather than the service provider itself. TSPI version 2.1 delivered the following new functions, messages, and structures for implementation:

-   [**TSPI\_providerFreeDialogInstance**](https://msdn.microsoft.com/en-us/library/ms725958(v=VS.85).aspx)
-   [**TSPI\_providerGenericDialogData**](https://msdn.microsoft.com/en-us/library/ms725959(v=VS.85).aspx)
-   [**TSPI\_providerUIIdentify**](https://msdn.microsoft.com/en-us/library/ms725964(v=VS.85).aspx)
-   [**TUISPI\_lineConfigDialog**](https://msdn.microsoft.com/en-us/library/ms725976(v=VS.85).aspx)
-   [**TUISPI\_lineConfigDialogEdit**](https://msdn.microsoft.com/en-us/library/ms725977(v=VS.85).aspx)
-   [**TUISPI\_phoneConfigDialog**](https://msdn.microsoft.com/en-us/library/ms725979(v=VS.85).aspx)
-   [**TUISPI\_providerConfig**](https://msdn.microsoft.com/en-us/library/ms725981(v=VS.85).aspx)
-   [**TUISPI\_providerGenericDialog**](https://msdn.microsoft.com/en-us/library/ms725982(v=VS.85).aspx)
-   [**TUISPI\_providerGenericDialogData**](https://msdn.microsoft.com/en-us/library/ms725983(v=VS.85).aspx)
-   [**TUISPI\_providerInstall**](https://msdn.microsoft.com/en-us/library/ms725984(v=VS.85).aspx)
-   [**TUISPI\_providerRemove**](https://msdn.microsoft.com/en-us/library/ms725985(v=VS.85).aspx)
-   [**TUISPICREATEDIALOGINSTANCEPARAMS**](https://msdn.microsoft.com/en-us/library/ms725972(v=VS.85).aspx)
-   [**TUISPIDLLCALLBACK**](https://msdn.microsoft.com/en-us/library/ms725187(v=VS.85).aspx)
-   [**LINE\_CREATEDIALOGINSTANCE**](line-createdialoginstance.md)
-   [**LINE\_SENDDIALOGINSTANCEDATA**](line-senddialoginstancedata.md)

 

 



