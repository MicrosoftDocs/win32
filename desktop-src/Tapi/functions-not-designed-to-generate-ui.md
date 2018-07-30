---
Description: Assume that the service provider must display a dialog box (like the Unimodem or ATSP Talk/Hangup dialog box) during the processing of lineMakeCall or lineDial.
ms.assetid: 46f87947-bfcd-48ad-8c33-7ea4d9caa34c
title: Functions Not Designed to Generate UI
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Functions Not Designed to Generate UI

Assume that the service provider must display a dialog box (like the Unimodem or ATSP **Talk/Hangup** dialog box) during the processing of [**lineMakeCall**](https://msdn.microsoft.com/en-us/library/ms735988(v=VS.85).aspx) or [**lineDial**](https://msdn.microsoft.com/en-us/library/ms735612(v=VS.85).aspx). In this case, it is the service provider, not the application, that decides that UI must be displayed.

To invoke the UI DLL in the application process, the service provider calls the TSPI [*Line\_Event*](https://msdn.microsoft.com/en-us/library/ms725228(v=VS.85).aspx) callback, generating a [**LINE\_CREATEDIALOGINSTANCE**](line-createdialoginstance.md) message, passing in a pointer to a structure of type [**TUISPICREATEDIALOGINSTANCEPARAMS**](https://msdn.microsoft.com/en-us/library/ms725972(v=VS.85).aspx). This structure contains the **dwRequestID** of the function with which the UI is associated, allowing TAPISRV to identify the client application in which the UI is to be generated.

TAPISRV requests the correct application's instance of TAPI to load the UI DLL and create a thread for the UI within the application's process. From this new UI thread, TAPI calls the UI DLL's [**TUISPI\_providerGenericDialog**](https://msdn.microsoft.com/en-us/library/ms725982(v=VS.85).aspx) function, passing in data that was specified by the telephony service provider in the structure passed in with the [**LINE\_CREATEDIALOGINSTANCE**](line-createdialoginstance.md) message; the UI DLL displays the appropriate dialog box (which is a matter for private design between the UI DLL and the telephony service provider). The UI DLL does not return from **TUISPI\_providerGenericDialog** until the dialog box is closed.

The telephony service provider can generate updated data to display in the dialog box (or, for example, instruct the dialog box to be closed, if the call is abandoned or other events occur) by sending a [**LINE\_SENDDIALOGINSTANCEDATA**](line-senddialoginstancedata.md) message. TAPISRV conveys the data to TAPI, which calls the UI DLL's [**TUISPI\_providerGenericDialogData**](https://msdn.microsoft.com/en-us/library/ms725983(v=VS.85).aspx) function. This mechanism provides a unidirectional "send" to the UI DLL. If the UI DLL wants to inform the telephony service provider of the results of the dialog box or obtain other data, it can call the [*DllCallbackProc*](https://msdn.microsoft.com/en-us/library/ms725187(v=VS.85).aspx) function (a pointer to which it received when [**TUISPI\_providerGenericDialog**](https://msdn.microsoft.com/en-us/library/ms725982(v=VS.85).aspx) was called).

When the dialog box is dismissed, [**TUISPI\_providerGenericDialog**](https://msdn.microsoft.com/en-us/library/ms725982(v=VS.85).aspx) returns to TAPI. TAPI calls [**FreeLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms683152) to release the UI DLL, and exits the UI thread it had created in the application context. It then requests TAPISRV to call the telephony service provider's [**TSPI\_providerFreeDialogInstance**](https://msdn.microsoft.com/en-us/library/ms725958(v=VS.85).aspx) function to unbind the association created when the telephony service provider originally sent the [**LINE\_CREATEDIALOGINSTANCE**](line-createdialoginstance.md) message. This function is also called if the application process terminates unexpectedly before **TUISPI\_providerGenericDialog** returns.

 

 



