---
title: WNet Functions
description: Windows Networking functions provide information and utilities for managing network resources.
ms.assetid: 8a83186f-a912-4c61-8137-1f6be1f3afd6
ms.topic: article
ms.date: 05/31/2018
---

# WNet Functions

Windows Networking functions provide information and utilities for managing network resources. The Windows Networking functions can be grouped as follows:

-   [Connection functions](#connection-functions)
-   [Enumeration functions](#enumeration-functions)
-   [Information functions](#information-functions)
-   [User functions](#user-functions)

## Connection Functions

Call the following WNet connection functions to connect a local device to a network resource, and to cancel network connections.



| Function                                                                     | Description                                                                                                                                                                                                                    |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MultinetGetConnectionPerformance**](https://msdn.microsoft.com/library/Aa385342(v=VS.85).aspx) | Returns information about the expected performance of a connection to a network resource.                                                                                                                                      |
| [**WNetAddConnection**](https://msdn.microsoft.com/library/Aa385410(v=VS.85).aspx)                               | Connects a local device to a network resource. (Provided for compatibility with 16-bit versions of Windows.)                                                                                                                   |
| [**WNetAddConnection2**](https://msdn.microsoft.com/library/Aa385413(v=VS.85).aspx)                             | Connects a local device to a network resource.                                                                                                                                                                                 |
| [**WNetAddConnection3**](https://msdn.microsoft.com/library/Aa385418(v=VS.85).aspx)                             | Connects a local device to a network resource. This function includes one more parameter than the **WNetAddConnection2** function, a handle to a window that the network provider can use as an owner window for dialog boxes. |
| [**WNetCancelConnection**](https://msdn.microsoft.com/library/Aa385423(v=VS.85).aspx)                         | Cancels a network connection. (Provided for compatibility with 16-bit versions of Windows.)                                                                                                                                    |
| [**WNetCancelConnection2**](https://msdn.microsoft.com/library/Aa385427(v=VS.85).aspx)                       | Cancels a network connection, providing the ability to update the user profile with information about persistent connections.                                                                                                  |
| [**WNetConnectionDialog**](https://msdn.microsoft.com/library/Aa385433(v=VS.85).aspx)                         | Starts a general browsing dialog box for connecting to network resources.                                                                                                                                                      |
| [**WNetConnectionDialog1**](https://msdn.microsoft.com/library/Aa385436(v=VS.85).aspx)                       | Starts a general browsing dialog box for connecting to network resources, using a [**CONNECTDLGSTRUCT**](https://msdn.microsoft.com/library/Aa385332(v=VS.85).aspx) structure.                                                                                  |
| [**WNetDisconnectDialog**](https://msdn.microsoft.com/library/Aa385440(v=VS.85).aspx)                         | Starts a general browsing dialog box for disconnecting from network resources.                                                                                                                                                 |
| [**WNetDisconnectDialog1**](https://msdn.microsoft.com/library/Aa385443(v=VS.85).aspx)                       | Starts a general browsing dialog box for disconnecting from network resources, using a [**DISCDLGSTRUCT**](https://msdn.microsoft.com/library/Aa385339(v=VS.85).aspx) structure.                                                                                   |
| [**WNetGetConnection**](https://msdn.microsoft.com/library/Aa385453(v=VS.85).aspx)                               | Retrieves the name of the network resource associated with a local device.                                                                                                                                                     |
| [**WNetGetUniversalName**](https://msdn.microsoft.com/library/Aa385474(v=VS.85).aspx)                         | When given a drive-based path for a network resource, returns a more universal form of the name.                                                                                                                               |
| [**WNetRestoreConnectionW**](https://msdn.microsoft.com/library/Aa385480(v=VS.85).aspx)                     | Restores the connection to a network resource, prompting the user, if necessary, for a name and password.                                                                                                                      |
| [**WNetUseConnection**](https://msdn.microsoft.com/library/Aa385482(v=VS.85).aspx)                               | Connects a local device to a network resource; automatically selects an unused local device to redirect to the network resource.                                                                                               |



 

> [!Note]  
> The [**WNetAddConnection**](https://msdn.microsoft.com/library/Aa385410(v=VS.85).aspx) and [**WNetCancelConnection**](https://msdn.microsoft.com/library/Aa385423(v=VS.85).aspx) functions are supported for compatibility with Windows for Workgroups. However, new applications should use [**WNetAddConnection2**](https://msdn.microsoft.com/library/Aa385413(v=VS.85).aspx) or [**WNetAddConnection3**](https://msdn.microsoft.com/library/Aa385418(v=VS.85).aspx), and [**WNetCancelConnection2**](https://msdn.microsoft.com/library/Aa385427(v=VS.85).aspx).

 

## Enumeration Functions

Call the following WNet functions to enumerate network resources.



| Function                                     | Description                                                                             |
|----------------------------------------------|-----------------------------------------------------------------------------------------|
| [**WNetCloseEnum**](https://msdn.microsoft.com/library/Aa385431(v=VS.85).aspx)       | Ends a network resource enumeration.                                                    |
| [**WNetEnumResource**](https://msdn.microsoft.com/library/Aa385449(v=VS.85).aspx) | Continues an enumeration of network resources started by the **WNetOpenEnum** function. |
| [**WNetOpenEnum**](https://msdn.microsoft.com/library/Aa385478(v=VS.85).aspx)         | Starts an enumeration of network resources.                                             |



 

## Information Functions

Call the following WNet informational and utility functions to retrieve network provider and other information.



| Function                                                         | Description                                                                                         |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [**WNetGetLastError**](https://msdn.microsoft.com/library/Aa385459(v=VS.85).aspx)                     | Returns the most recent error code set by a WNet function, the one reported by a network provider.  |
| [**WNetGetNetworkInformation**](https://msdn.microsoft.com/library/Aa385461(v=VS.85).aspx)   | Returns extended information about a specific network provider.                                     |
| [**WNetGetProviderName**](https://msdn.microsoft.com/library/Aa385464(v=VS.85).aspx)               | Returns the provider name for a specific type of network.                                           |
| [**WNetGetResourceInformation**](https://msdn.microsoft.com/library/Aa385469(v=VS.85).aspx) | Returns the network provider that owns a resource, and obtains information about the resource type. |
| [**WNetGetResourceParent**](https://msdn.microsoft.com/library/Aa385470(v=VS.85).aspx)           | Returns the parent of a network resource.                                                           |



 

## User Functions

Call the following WNet function to retrieve the name of the user associated with a local device.



| Function                           | Description                                                                              |
|------------------------------------|------------------------------------------------------------------------------------------|
| [**WNetGetUser**](https://msdn.microsoft.com/library/Aa385476(v=VS.85).aspx) | Returns the current default user name, or the user name that established the connection. |



 

Many of the WNet functions use a [**NETRESOURCE**](/windows/desktop/api/Winnetwk/ns-winnetwk-netresourcea) structure to store information about a network resource.

 

 




