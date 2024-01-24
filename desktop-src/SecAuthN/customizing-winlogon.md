---
description: Customize Winlogon behavior by implementing a Credential Provider.
ms.assetid: 70b47e29-c755-4c59-a493-d7fcbbc94b83
title: Customizing Winlogon
ms.topic: article
ms.date: 05/31/2018
---

# Customizing Winlogon

Customize [*Winlogon*](/windows/desktop/SecGloss/w-gly) behavior by implementing a Credential Provider. For information about Credential Providers, see [**ICredentialProvider Interface**](/windows/win32/api/credentialprovider/nn-credentialprovider-icredentialprovider).

**Windows Server 2003 and Windows XP:** Credential Providers are not supported.

The following sections describe ways to customize Winlogon in Windows versions prior to Windows Vista.

> [!Note]  
> GINA DLLs and Winlogon notification packages are ignored in Windows Vista.

 

-   [Winlogon Notification Packages](#winlogon-notification-packages)
-   [GINA Stubs](#gina-stubs)
-   [GINA Hooks](#gina-hooks)

## Winlogon Notification Packages

A Winlogon notification package is a DLL that exports functions that handle Winlogon events. For example, when a user logs onto the system, Winlogon calls each notification package to provide information about the event. For more information, see [Winlogon Notification Packages](winlogon-notification-packages.md).

## GINA Stubs

A [*GINA*](/windows/desktop/SecGloss/g-gly) stub is a custom GINA DLL that uses the export function implementations of a previously installed GINA DLL (typically MsGina.dll). A GINA stub gets pointers to each function exported by the previously installed GINA DLL. Each GINA stub function then uses the appropriate function pointer to call the corresponding function in the previously installed GINA DLL.

> [!IMPORTANT]
> Each GINA stub function must call the corresponding function in the previously installed GINA.

 

A GINA stub function can implement additional functionality in one or more of its export functions. For example, the [**WlxLoggedOutSAS**](/windows/desktop/api/Winwlx/nf-winwlx-wlxloggedoutsas) function of a GINA stub might check the current time before calling the **WlxLoggedOutSAS** function of the MsGina.dll. If the current time was within a specific range, the stub function could display a message that indicates logon is disallowed during that time period and return **WLX\_SAS\_ACTION\_NONE** to Winlogon. The **WlxLoggedOutSAS** function of the MsGina.dll would then be called only during the allowed time period.

The GINA stub application gets a dispatch table to Winlogon support functions through the *pWinlogonFunctions* parameter of the [**WlxInitialize**](/windows/desktop/api/Winwlx/nf-winwlx-wlxinitialize) function. The GINA stub application can use this dispatch table to call Winlogon support functions. For example, A GINA stub application can call the [**WlxSasNotify**](/windows/win32/api/winwlx/nc-winwlx-pwlx_sas_notify) function to cause a [*secure attention sequence*](/windows/desktop/SecGloss/s-gly) (SAS) event when a [*smart card*](/windows/desktop/SecGloss/s-gly) is inserted into a [*reader*](/windows/desktop/SecGloss/r-gly).

For more information about creating a GINA stub, see the Gina Stubs sample in the \\Samples\\Security\\Gina\\GinaStub directory of a Platform Software Development Kit (SDK) installation.

> [!Note]  
> All calls between a GINA and Winlogon must be within a single thread.

 

## GINA Hooks

A GINA hook is a GINA stub that, in its implementation of the [**WlxInitialize**](/windows/desktop/api/Winwlx/nf-winwlx-wlxinitialize) function, replaces the pointer to the [**WlxDialogBoxParam**](/windows/win32/api/winwlx/nc-winwlx-pwlx_dialog_box_param) support function in the dispatch table with a pointer to its own implementation of the **WlxDialogBoxParam** function. As a result, each time the previously installed GINA (typically MsGina.dll) calls the **WlxDialogBoxParam** function, the function implemented by the GINA hook is called.

The [**WlxDialogBoxParam**](/windows/win32/api/winwlx/nc-winwlx-pwlx_dialog_box_param) function implemented by the GINA hook can replace the [**DialogProc**](/windows/win32/api/winuser/nc-winuser-dlgproc) callback procedure that responds to a specific dialog box event.

This gives the GINA hook full control over the appearance and behavior of all of the dialog boxes that MsGina.dll creates.

For more information about creating a GINA hook, see the Gina Hooks sample in the \\Samples\\Security\\Gina\\GinaHook directory of a Platform SDK installation.

> [!Note]  
> All calls between a GINA and Winlogon must be within a single thread.

 

 

 
