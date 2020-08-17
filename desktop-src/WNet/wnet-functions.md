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
| [**MultinetGetConnectionPerformance**](/windows/win32/api/winnetwk/nf-winnetwk-multinetgetconnectionperformancea) | Returns information about the expected performance of a connection to a network resource.                                                                                                                                      |
| [**WNetAddConnection**](/windows/win32/api/winnetwk/nf-winnetwk-wnetaddconnectiona)                               | Connects a local device to a network resource. (Provided for compatibility with 16-bit versions of Windows.)                                                                                                                   |
| [**WNetAddConnection2**](/windows/win32/api/winnetwk/nf-winnetwk-wnetaddconnection2a)                             | Connects a local device to a network resource.                                                                                                                                                                                 |
| [**WNetAddConnection3**](/windows/win32/api/winnetwk/nf-winnetwk-wnetaddconnection3a)                             | Connects a local device to a network resource. This function includes one more parameter than the **WNetAddConnection2** function, a handle to a window that the network provider can use as an owner window for dialog boxes. |
| [**WNetCancelConnection**](/windows/win32/api/winnetwk/nf-winnetwk-wnetcancelconnectiona)                         | Cancels a network connection. (Provided for compatibility with 16-bit versions of Windows.)                                                                                                                                    |
| [**WNetCancelConnection2**](/windows/win32/api/winnetwk/nf-winnetwk-wnetcancelconnection2a)                       | Cancels a network connection, providing the ability to update the user profile with information about persistent connections.                                                                                                  |
| [**WNetConnectionDialog**](/windows/win32/api/winnetwk/nf-winnetwk-wnetconnectiondialog)                         | Starts a general browsing dialog box for connecting to network resources.                                                                                                                                                      |
| [**WNetConnectionDialog1**](/windows/win32/api/winnetwk/nf-winnetwk-wnetconnectiondialog1a)                       | Starts a general browsing dialog box for connecting to network resources, using a [**CONNECTDLGSTRUCT**](/windows/win32/api/winnetwk/ns-winnetwk-connectdlgstructa) structure.                                                                                  |
| [**WNetDisconnectDialog**](/windows/win32/api/winnetwk/nf-winnetwk-wnetdisconnectdialog)                         | Starts a general browsing dialog box for disconnecting from network resources.                                                                                                                                                 |
| [**WNetDisconnectDialog1**](/windows/win32/api/winnetwk/nf-winnetwk-wnetdisconnectdialog1a)                       | Starts a general browsing dialog box for disconnecting from network resources, using a [**DISCDLGSTRUCT**](/windows/win32/api/winnetwk/ns-winnetwk-discdlgstructa) structure.                                                                                   |
| [**WNetGetConnection**](/windows/win32/api/winnetwk/nf-winnetwk-wnetgetconnectiona)                               | Retrieves the name of the network resource associated with a local device.                                                                                                                                                     |
| [**WNetGetUniversalName**](/windows/win32/api/winnetwk/nf-winnetwk-wnetgetuniversalnamea)                         | When given a drive-based path for a network resource, returns a more universal form of the name.                                                                                                                               |
| [**WNetRestoreConnectionW**](/windows/win32/api/winnetwk/nf-winnetwk-wnetrestoreconnectionw)                     | Restores the connection to a network resource, prompting the user, if necessary, for a name and password.                                                                                                                      |
| [**WNetUseConnection**](/windows/win32/api/winnetwk/nf-winnetwk-wnetuseconnectiona)                               | Connects a local device to a network resource; automatically selects an unused local device to redirect to the network resource.                                                                                               |



 

> [!Note]  
> The [**WNetAddConnection**](/windows/win32/api/winnetwk/nf-winnetwk-wnetaddconnectiona) and [**WNetCancelConnection**](/windows/win32/api/winnetwk/nf-winnetwk-wnetcancelconnectiona) functions are supported for compatibility with Windows for Workgroups. However, new applications should use [**WNetAddConnection2**](/windows/win32/api/winnetwk/nf-winnetwk-wnetaddconnection2a) or [**WNetAddConnection3**](/windows/win32/api/winnetwk/nf-winnetwk-wnetaddconnection3a), and [**WNetCancelConnection2**](/windows/win32/api/winnetwk/nf-winnetwk-wnetcancelconnection2a).

 

## Enumeration Functions

Call the following WNet functions to enumerate network resources.



| Function                                     | Description                                                                             |
|----------------------------------------------|-----------------------------------------------------------------------------------------|
| [**WNetCloseEnum**](/windows/win32/api/winnetwk/nf-winnetwk-wnetcloseenum)       | Ends a network resource enumeration.                                                    |
| [**WNetEnumResource**](/windows/win32/api/winnetwk/nf-winnetwk-wnetenumresourcea) | Continues an enumeration of network resources started by the **WNetOpenEnum** function. |
| [**WNetOpenEnum**](/windows/win32/api/winnetwk/nf-winnetwk-wnetopenenuma)         | Starts an enumeration of network resources.                                             |



 

## Information Functions

Call the following WNet informational and utility functions to retrieve network provider and other information.



| Function                                                         | Description                                                                                         |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [**WNetGetLastError**](/windows/win32/api/winnetwk/nf-winnetwk-wnetgetlasterrora)                     | Returns the most recent error code set by a WNet function, the one reported by a network provider.  |
| [**WNetGetNetworkInformation**](/windows/win32/api/winnetwk/nf-winnetwk-wnetgetnetworkinformationa)   | Returns extended information about a specific network provider.                                     |
| [**WNetGetProviderName**](/windows/win32/api/winnetwk/nf-winnetwk-wnetgetprovidernamea)               | Returns the provider name for a specific type of network.                                           |
| [**WNetGetResourceInformation**](/windows/win32/api/winnetwk/nf-winnetwk-wnetgetresourceinformationa) | Returns the network provider that owns a resource, and obtains information about the resource type. |
| [**WNetGetResourceParent**](/windows/win32/api/winnetwk/nf-winnetwk-wnetgetresourceparenta)           | Returns the parent of a network resource.                                                           |



 

## User Functions

Call the following WNet function to retrieve the name of the user associated with a local device.



| Function                           | Description                                                                              |
|------------------------------------|------------------------------------------------------------------------------------------|
| [**WNetGetUser**](/windows/win32/api/winnetwk/nf-winnetwk-wnetgetusera) | Returns the current default user name, or the user name that established the connection. |



 

Many of the WNet functions use a [**NETRESOURCE**](/windows/desktop/api/Winnetwk/ns-winnetwk-netresourcea) structure to store information about a network resource.

 

 