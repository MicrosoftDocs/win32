---
title: RAS Custom Scripting
description: Developers can create a custom-scripting DLL that resides on a RAS client computer. This DLL can communicate with the server during the process of establishing a connection.
ms.assetid: c27b8b02-6018-4441-a355-1fb890b9001c
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RAS Custom Scripting

Developers can create a custom-scripting DLL that resides on a RAS client computer. This DLL can communicate with the server during the process of establishing a connection.

**Windows NT:** Custom scripting is not available.

## Setting up the DLL

To set up the DLL, create a value with the name **CustomScriptDllPath** under the following registry key:

```
HKEY_LOCAL_MACHINE
   System
      CurrentControlSet
         Services
            Rasman
               Parameters
```

This value should be of type **REG\_EXPAND\_SZ**. The value should contain the path to the custom-scripting DLL. Only one custom-scripting DLL is supported for each RAS client computer.

## Interaction Between the Server, RAS, and the Custom-Scripting DLL

The custom scripting DLL should export a single entry point: [**RasCustomScriptExecute**](/windows/win32/Ras/nc-ras-rascustomscriptexecutefn?branch=master). RAS calls this function during the RASCS\_Interactive state of the connection process. The RASCS\_Interactive state is a paused state, which allows the user to interact with a user interface presented by the custom-scripting DLL. See [**RASCONNSTATE**](/windows/win32/Ras/?branch=master) for more information about connection states.

RAS will pass as parameters to the [**RasCustomScriptExecute**](/windows/win32/Ras/nc-ras-rascustomscriptexecutefn?branch=master) function:

-   A handle to the port on the client computer that is being used for the connection.
-   Strings that identify the phone book and entry for the connection.
-   RAS also passes in a handle to a window to enable the DLL to present a user interface.
-   A set of function pointers that the DLL can use to communicate with the server.

See [**RasCustomScriptExecute**](/windows/win32/Ras/nc-ras-rascustomscriptexecutefn?branch=master) for more information about these parameters.

RAS passes a pointer to a [**RASCUSTOMSCRIPTEXTENSIONS**](/windows/win32/Ras/?branch=master) structure as the last parameter to [**RasCustomScriptExecute**](/windows/win32/Ras/nc-ras-rascustomscriptexecutefn?branch=master). This structure contains a pointer to a function of type [**PFNRASSETCOMMSETTINGS**](/windows/win32/Ras/nc-ras-pfnrassetcommsettings?branch=master). The custom-scripting DLL calls this function to modify the communication settings on the port being used by the connection.

RAS mediates the interaction between the server and the custom-scripting DLL. Typically, the server initiates the dialog. For example, the server may request the user name and password of the user.

When using custom-scripting to establish a connection, the server need not be running Windows NT 4.0 or Windows 2000.

## Custom Scripting User Interface Must Support IDCANCEL

If the custom dialer displays a user interface, the user interface must support WM\_COMMAND messages where LOWORD(*wParam*) equals IDCANCEL.

## Configuring the Connection

The [**RasCustomScriptExecute**](/windows/win32/Ras/nc-ras-rascustomscriptexecutefn?branch=master) entry point can be invoked from [**RasDialDlg**](/windows/win32/Rasdlg/nf-rasdlg-rasdialdlga?branch=master) or, on Windows XP, from [**RasDial**](/windows/win32/Ras/nf-ras-rasdiala?branch=master).

To invoke [**RasCustomScriptExecute**](/windows/win32/Ras/nc-ras-rascustomscriptexecutefn?branch=master) from [**RasDialDlg**](/windows/win32/Rasdlg/nf-rasdlg-rasdialdlga?branch=master), set the RASEO\_CustomScript option in the phone-book entry for the connection. See the **dwfOptions** member of [**RASENTRY**](/windows/win32/Ras/?branch=master) for a description of phone-book entry options. Use the [**RasGetEntryProperties**](/windows/win32/Ras/nf-ras-rasgetentrypropertiesa?branch=master) and [**RasSetEntryProperties**](/windows/win32/Ras/nf-ras-rassetentrypropertiesa?branch=master) functions to set this option programmatically.

**Windows XP:** To invoke [**RasCustomScriptExecute**](/windows/win32/Ras/nc-ras-rascustomscriptexecutefn?branch=master) from [**RasDial**](/windows/win32/Ras/nf-ras-rasdiala?branch=master), the call to **RasDial** must specify a [**RASDIALEXTENSIONS**](/windows/win32/Ras/?branch=master) structure, and this structure must specify the RDEOPT\_UseCustomScripting flag. In addition, the phone-book entry for the connection must specify the RASEO\_CustomScript option as described in the preceding paragraph.

## Invoking the Custom Scripting DLL

If the user activates a connection for a phone-book entry that has RASEO\_CustomScript set, RAS invokes the custom-scripting DLL. In this scenario, RAS invokes the custom-scripting DLL from [**RasDialDlg**](/windows/win32/Rasdlg/nf-rasdlg-rasdialdlga?branch=master).

To invoke the custom-scripting DLL programmatically, establish the connection using the [**RasDialDlg**](/windows/win32/Rasdlg/nf-rasdlg-rasdialdlga?branch=master) function. On Windows XP, the [**RasDial**](/windows/win32/Ras/nf-ras-rasdiala?branch=master) function also invokes the custom-scripting DLL.

 

 




