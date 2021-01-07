---
description: Assume for the purposes of an example that the application calls the TAPI lineConfigDialog function, which is designed to open a dialog box to allow configuration of service provider options related to the specified line device.
ms.assetid: a388d192-a327-4e67-968b-344d80c19fb1
title: Functions Designed to Generate UI
ms.topic: article
ms.date: 05/31/2018
---

# Functions Designed to Generate UI

Assume for the purposes of an example that the application calls the TAPI [**lineConfigDialog**](/windows/win32/api/tapi/nf-tapi-lineconfigdialog) function, which is designed to open a dialog box to allow configuration of service provider options related to the specified line device. In response to this call, TAPI requests TAPISRV to call [**TSPI\_providerUIIdentify**](/windows/win32/api/tspi/nf-tspi-tspi_provideruiidentify) in the telephony service provider, obtaining the name of the TSP UI DLL.

In the application's context, TAPI loads the TSP UI DLL and calls the [**TUISPI\_lineConfigDialog**](/windows/win32/api/tspi/nf-tspi-tuispi_lineconfigdialog) function with the parameters supplied by the application, and including a pointer to the TAPI [*DllCallbackProc*](/windows/win32/api/tspi/nc-tspi-tuispidllcallback) function. The TSP UI DLL displays the configuration dialog box, calling the *DllCallbackProc* function as necessary to obtain from the telephony service provider the information to display. Each time the *DllCallbackProc* function is called, TAPI requests TAPISRV to call the telephony service provider's [**TSPI\_providerGenericDialogData**](/windows/win32/api/tspi/nf-tspi-tspi_providergenericdialogdata) function, passing in the parameter block from the UI DLL, and returning the parameter block to the UI DLL. The UI DLL conveys any configuration changes to the telephony service provider by calling *DllCallbackProc*.

When the function is complete, the UI DLL returns from (in this case) [**TUISPI\_lineConfigDialog**](/windows/win32/api/tspi/nf-tspi-tuispi_lineconfigdialog). TAPI calls the [**FreeLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-freelibrary) function to release the UI DLL, and returns to the application.

 

 
