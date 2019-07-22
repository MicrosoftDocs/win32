---
Description: Starting with TAPI 2.1, the telephony service provider user interface DLLs can be used to manage and display dialog boxes. TAPI loads the DLL into the process of an application that invokes any of the service provider functions that can display a dialog.
ms.assetid: 0a0320d1-fb75-405e-8074-b37cef956c9f
title: What's New for TSPI Version 2.1
ms.topic: article
ms.date: 05/31/2018
---

# What's New for TSPI Version 2.1

Starting with TAPI 2.1, the telephony service provider user interface DLLs can be used to manage and display dialog boxes. TAPI loads the DLL into the process of an application that invokes any of the service provider functions that can display a dialog.

Starting with TAPI 2.1, proxy request handlers can be implemented. A handler is a full telephony application that normally executes on a telephony server and provides services that are more appropriately implemented in an application than a driver.

Functions and messages that were new or changed for TSPI version 2.1 are as follows:

-   [**TSPI_lineConditionalMediaDetection**](https://msdn.microsoft.com/en-us/library/ms725536(v=VS.85).aspx)
-   **TSPI_lineDropNoOwner**—**obsolete**
-   **TSPI_lineDropOnClose**—**obsolete**
-   [**TSPI_lineGetID**](https://msdn.microsoft.com/en-us/library/ms725572(v=VS.85).aspx)
-   [**TSPI_lineSetCallData**](https://msdn.microsoft.com/en-us/library/ms725595(v=VS.85).aspx)
-   [**TSPI_lineSetCallQualityOfService**](https://msdn.microsoft.com/en-us/library/ms725598(v=VS.85).aspx)
-   [**TSPI_lineSetCallTreatment**](https://msdn.microsoft.com/en-us/library/ms725599(v=VS.85).aspx)
-   [**TSPI_lineSetLineDevStatus**](https://msdn.microsoft.com/en-us/library/ms725603(v=VS.85).aspx)
-   [**TSPI_phoneGetID**](https://msdn.microsoft.com/en-us/library/ms725934(v=VS.85).aspx)
-   [**TSPI_providerInit**](https://msdn.microsoft.com/en-us/library/ms725960(v=VS.85).aspx)
-   [**TSPI_providerShutdown**](https://msdn.microsoft.com/en-us/library/ms725963(v=VS.85).aspx)
-   [**LINE_GATHERDIGITS**](https://docs.microsoft.com/previous-versions/windows/desktop/legacy/ms725229(v=vs.85))
-   [**LINE_GENERATE**](https://docs.microsoft.com/previous-versions/windows/desktop/legacy/ms725230(v=vs.85))
-   [**LINE_MONITORDIGITS**](https://docs.microsoft.com/previous-versions/windows/desktop/legacy/ms725232(v=vs.85))
-   [**LINE_MONITORMEDIA**](https://docs.microsoft.com/previous-versions/windows/desktop/legacy/ms725233(v=vs.85))
-   [**LINE_MONITORTONE**](https://docs.microsoft.com/previous-versions/windows/desktop/legacy/ms725234(v=vs.85))
-   [**LINE_REMOVE**](https://docs.microsoft.com/previous-versions/windows/desktop/legacy/ms725237(v=vs.85))
-   [**PHONE_REMOVE**](https://docs.microsoft.com/previous-versions/windows/desktop/legacy/ms725260(v=vs.85))

The Telephony service provider user interface DLL provides a means of allowing user interaction within the context of the application rather than the service provider itself. TSPI version 2.1 delivered the following new functions, messages, and structures for implementation:

-   [**TSPI_providerFreeDialogInstance**](https://msdn.microsoft.com/en-us/library/ms725958(v=VS.85).aspx)
-   [**TSPI_providerGenericDialogData**](https://msdn.microsoft.com/en-us/library/ms725959(v=VS.85).aspx)
-   [**TSPI_providerUIIdentify**](https://msdn.microsoft.com/en-us/library/ms725964(v=VS.85).aspx)
-   [**TUISPI_lineConfigDialog**](https://msdn.microsoft.com/en-us/library/ms725976(v=VS.85).aspx)
-   [**TUISPI_lineConfigDialogEdit**](https://msdn.microsoft.com/en-us/library/ms725977(v=VS.85).aspx)
-   [**TUISPI_phoneConfigDialog**](https://msdn.microsoft.com/en-us/library/ms725979(v=VS.85).aspx)
-   [**TUISPI_providerConfig**](https://msdn.microsoft.com/en-us/library/ms725981(v=VS.85).aspx)
-   [**TUISPI_providerGenericDialog**](https://msdn.microsoft.com/en-us/library/ms725982(v=VS.85).aspx)
-   [**TUISPI_providerGenericDialogData**](https://msdn.microsoft.com/en-us/library/ms725983(v=VS.85).aspx)
-   [**TUISPI_providerInstall**](https://msdn.microsoft.com/en-us/library/ms725984(v=VS.85).aspx)
-   [**TUISPI_providerRemove**](https://msdn.microsoft.com/en-us/library/ms725985(v=VS.85).aspx)
-   [**TUISPICREATEDIALOGINSTANCEPARAMS**](https://msdn.microsoft.com/en-us/library/ms725972(v=VS.85).aspx)
-   [**TUISPIDLLCALLBACK**](https://msdn.microsoft.com/en-us/library/ms725187(v=VS.85).aspx)
-   [**LINE_CREATEDIALOGINSTANCE**](line-createdialoginstance.md)
-   [**LINE_SENDDIALOGINSTANCEDATA**](line-senddialoginstancedata.md)

 

 



