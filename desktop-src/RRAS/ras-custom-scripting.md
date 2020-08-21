---
title: RAS Custom Scripting
description: Developers can create a custom-scripting DLL that resides on a RAS client computer. This DLL can communicate with the server during the process of establishing a connection.
ms.assetid: c27b8b02-6018-4441-a355-1fb890b9001c
ms.topic: article
ms.date: 05/31/2018
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

The custom scripting DLL should export a single entry point: [**RasCustomScriptExecute**](/windows/desktop/api/Ras/nc-ras-rascustomscriptexecutefn). RAS calls this function during the RASCS\_Interactive state of the connection process. The RASCS\_Interactive state is a paused state, which allows the user to interact with a user interface presented by the custom-scripting DLL. See [**RASCONNSTATE**](/previous-versions/windows/desktop/legacy/aa376727(v=vs.85)) for more information about connection states.

RAS will pass as parameters to the [**RasCustomScriptExecute**](/windows/desktop/api/Ras/nc-ras-rascustomscriptexecutefn) function:

-   A handle to the port on the client computer that is being used for the connection.
-   Strings that identify the phone book and entry for the connection.
-   RAS also passes in a handle to a window to enable the DLL to present a user interface.
-   A set of function pointers that the DLL can use to communicate with the server.

See [**RasCustomScriptExecute**](/windows/desktop/api/Ras/nc-ras-rascustomscriptexecutefn) for more information about these parameters.

RAS passes a pointer to a [**RASCUSTOMSCRIPTEXTENSIONS**](/previous-versions/windows/desktop/legacy/aa376738(v=vs.85)) structure as the last parameter to [**RasCustomScriptExecute**](/windows/desktop/api/Ras/nc-ras-rascustomscriptexecutefn). This structure contains a pointer to a function of type [**PFNRASSETCOMMSETTINGS**](/windows/desktop/api/Ras/nc-ras-pfnrassetcommsettings). The custom-scripting DLL calls this function to modify the communication settings on the port being used by the connection.

RAS mediates the interaction between the server and the custom-scripting DLL. Typically, the server initiates the dialog. For example, the server may request the user name and password of the user.

When using custom-scripting to establish a connection, the server need not be running Windows NT 4.0 or Windows 2000.

## Custom Scripting User Interface Must Support IDCANCEL

If the custom dialer displays a user interface, the user interface must support WM\_COMMAND messages where LOWORD(*wParam*) equals IDCANCEL.

## Configuring the Connection

The [**RasCustomScriptExecute**](/windows/desktop/api/Ras/nc-ras-rascustomscriptexecutefn) entry point can be invoked from [**RasDialDlg**](/windows/desktop/api/Rasdlg/nf-rasdlg-rasdialdlga) or, on Windows XP, from [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala).

To invoke [**RasCustomScriptExecute**](/windows/desktop/api/Ras/nc-ras-rascustomscriptexecutefn) from [**RasDialDlg**](/windows/desktop/api/Rasdlg/nf-rasdlg-rasdialdlga), set the RASEO\_CustomScript option in the phone-book entry for the connection. See the **dwfOptions** member of [**RASENTRY**](/previous-versions/windows/desktop/legacy/aa377274(v=vs.85)) for a description of phone-book entry options. Use the [**RasGetEntryProperties**](/windows/desktop/api/Ras/nf-ras-rasgetentrypropertiesa) and [**RasSetEntryProperties**](/windows/desktop/api/Ras/nf-ras-rassetentrypropertiesa) functions to set this option programmatically.

**Windows XP:** To invoke [**RasCustomScriptExecute**](/windows/desktop/api/Ras/nc-ras-rascustomscriptexecutefn) from [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala), the call to **RasDial** must specify a [**RASDIALEXTENSIONS**](/previous-versions/windows/desktop/legacy/aa377029(v=vs.85)) structure, and this structure must specify the RDEOPT\_UseCustomScripting flag. In addition, the phone-book entry for the connection must specify the RASEO\_CustomScript option as described in the preceding paragraph.

## Invoking the Custom Scripting DLL

If the user activates a connection for a phone-book entry that has RASEO\_CustomScript set, RAS invokes the custom-scripting DLL. In this scenario, RAS invokes the custom-scripting DLL from [**RasDialDlg**](/windows/desktop/api/Rasdlg/nf-rasdlg-rasdialdlga).

To invoke the custom-scripting DLL programmatically, establish the connection using the [**RasDialDlg**](/windows/desktop/api/Rasdlg/nf-rasdlg-rasdialdlga) function. On Windows XP, the [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) function also invokes the custom-scripting DLL.

 

 