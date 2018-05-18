---
title: Using the Connections Dialog Box
description: The WNetConnectionDialog function creates a dialog box that allows the user to browse and connect to network resources.
ms.assetid: 'ef375004-e426-4dee-b318-b470721116fa'
---

# Using the Connections Dialog Box

The [**WNetConnectionDialog**](wnetconnectiondialog.md) function creates a dialog box that allows the user to browse and connect to network resources. You can also call the [**WNetConnectionDialog1**](wnetconnectiondialog1.md) function to create a connections dialog box. **WNetConnectionDialog1** requires a [**CONNECTDLGSTRUCT**](connectdlgstruct-str.md) structure.

The [**WNetDisconnectDialog**](wnetdisconnectdialog.md) function creates a dialog box that allows the user to disconnect from network resources.

The following code sample demonstrates how to call the **WNetConnectionDialog** function to create a dialog box that displays disk resources. If the call fails, the sample calls an application-defined error handler.


```C++
DWORD dwResult; 
//
// Call the WNetConnectionDialog function.
//
dwResult = WNetConnectionDialog(hwnd, RESOURCETYPE_DISK);
//
// Call an application-defined error handler 
//  to process errors.
//
if(dwResult != NO_ERROR) 
{
    NetErrorHandler(hwnd, dwResult, (LPSTR)"WNetConnectionDialog"); 
    return FALSE; 
}
```



For more information about using an application-defined error handler, see [Retrieving Network Errors](retrieving-network-errors.md).

 

 




