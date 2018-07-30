---
Description: The following illustration shows the general architecture of telephony service providers and their associated user interface dynamic-link libraries (UI DLLs).
ms.assetid: f47662f9-2fca-4044-ab26-617e5b1f9eae
title: Architecture
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Architecture

The following illustration shows the general architecture of telephony service providers and their associated user interface dynamic-link libraries (UI DLLs).

![tsps and associated ui dlls](images/spuidl01.png)

The service provider consists of a minimum of two components. The service provider DLL (designated in the illustration as MAIN.TSP) executes in the context of the TAPISRV process, and performs all of the tasks of the service provider that are not related to user interface elements associated with a particular application's use of the device (most likely, in conjunction with lower-level components not shown in the illustration). But unlike previous versions of TAPI in which the user interface code was integrated into the service provider (and executed, because of the previous architecture, within the context of the application), the service provider must now include a separate component that implements the user interface elements.

The service provider UI DLL must export functions that are called by TAPI when the application calls TAPI functions that generate UI: [**TUISPI\_lineConfigDialog**](https://msdn.microsoft.com/en-us/library/ms725976(v=VS.85).aspx), [**TUISPI\_lineConfigDialogEdit**](https://msdn.microsoft.com/en-us/library/ms725977(v=VS.85).aspx), [**TUISPI\_phoneConfigDialog**](https://msdn.microsoft.com/en-us/library/ms725979(v=VS.85).aspx), [**TUISPI\_providerConfig**](https://msdn.microsoft.com/en-us/library/ms725981(v=VS.85).aspx), [**TUISPI\_providerInstall**](https://msdn.microsoft.com/en-us/library/ms725984(v=VS.85).aspx), and [**TUISPI\_providerRemove**](https://msdn.microsoft.com/en-us/library/ms725985(v=VS.85).aspx). Each of these functions includes as a parameter a pointer to a callback function in TAPI, of type [**TUISPIDLLCALLBACK**](https://msdn.microsoft.com/en-us/library/ms725187(v=VS.85).aspx), which the UI DLL can use to communicate bidirectionally (both send and receive data) with the service provider DLL executing in the TAPISRV process. If the service provider ever generates spontaneous UI, such as the Unimodem **Talk/Hangup** dialog box, in conjunction with any TSPI function for which UI is not expected (for example, any function that does not have an *hwnd* parameter), then the UI DLL must export [**TUISPI\_providerGenericDialog**](https://msdn.microsoft.com/en-us/library/ms725982(v=VS.85).aspx) and [**TUISPI\_providerGenericDialogData**](https://msdn.microsoft.com/en-us/library/ms725983(v=VS.85).aspx).

> [!Note]  
> The original TSPI UI-generating functions ( [**TSPI\_lineConfigDialog**](https://msdn.microsoft.com/en-us/library/ms725537(v=VS.85).aspx), [**TSPI\_lineConfigDialogEdit**](https://msdn.microsoft.com/en-us/library/ms725538(v=VS.85).aspx), [**TSPI\_phoneConfigDialog**](https://msdn.microsoft.com/en-us/library/ms725924(v=VS.85).aspx), [**TSPI\_providerConfig**](https://msdn.microsoft.com/en-us/library/ms725954(v=VS.85).aspx), [**TSPI\_providerInstall**](https://msdn.microsoft.com/en-us/library/ms725961(v=VS.85).aspx), and [**TSPI\_providerRemove**](https://msdn.microsoft.com/en-us/library/ms725962(v=VS.85).aspx)) are obsolete and never called by TAPI. Therefore, these are not required to be exported by the service provider DLL. However, if the service provider wants to be listed as one that can be added by the Telephony Control Panel, a utility supplied with Windows Telephony in versions 1.4 and earlier, it must export **TSPI\_providerInstall**; if it wants to have the [**Remove**](https://msdn.microsoft.com/en-us/library/ms729476(v=VS.85).aspx) button enabled in the Telephony Control Panel when it is selected, it must export **TSPI\_providerRemove**; and if it wants the **Setup** button to be enabled in the Telephony Control Panel when it is selected, it must export **TSPI\_providerConfig**. The Telephony Control Panel checks for the presence of these functions in the service provider TSP file to adjust its user interface to reflect which operations can be performed.

 

The service provider DLL must export the [**TSPI\_providerUIIdentify**](https://msdn.microsoft.com/en-us/library/ms725964(v=VS.85).aspx) function that TAPISRV process uses to obtain the name of the UI DLL to load in the application process. It must export the [**TSPI\_providerGenericDialogData**](https://msdn.microsoft.com/en-us/library/ms725959(v=VS.85).aspx) function to receive and respond to requests from the UI DLL for data to display, and it must export [**TSPI\_providerFreeDialogInstance**](https://msdn.microsoft.com/en-us/library/ms725958(v=VS.85).aspx) for TAPISRV process to tell the service provider when to release an association established for the purpose of generating spontaneous UI in conjunction with a function that is not defined as presenting UI to the user. The service provider DLL can unidirectionally send data to the UI DLL by using the new TSPI message [**LINE\_SENDDIALOGINSTANCEDATA**](line-senddialoginstancedata.md).

Because the names of the TSPI and TUISPI functions are intentionally defined to be different, the service provider DLL and the UI DLL can be the same DLL file, if desired. With proper segmentation, this does not necessarily result in any unnecessary usage of memory in the application context, and can simplify the installation process for service providers that can currently be implemented in a single DLL. TAPI calls only the functions that are appropriate for the context in which the DLL is being used.

The telephony service provider and the UI DLL must both be designed with the requirement in mind that the UI functions can be invoked from multiple application processes simultaneously. They must also consider that the application and the TAPI service under which the telephony service provider is executing can be on separate computers on a LAN.

 

 



