---
title: WNet Functions
description: Windows Networking functions provide information and utilities for managing network resources.
ms.assetid: 8a83186f-a912-4c61-8137-1f6be1f3afd6
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
| [**MultinetGetConnectionPerformance**](multinetgetconnectionperformance.md) | Returns information about the expected performance of a connection to a network resource.                                                                                                                                      |
| [**WNetAddConnection**](wnetaddconnection.md)                               | Connects a local device to a network resource. (Provided for compatibility with 16-bit versions of Windows.)                                                                                                                   |
| [**WNetAddConnection2**](wnetaddconnection2.md)                             | Connects a local device to a network resource.                                                                                                                                                                                 |
| [**WNetAddConnection3**](wnetaddconnection3.md)                             | Connects a local device to a network resource. This function includes one more parameter than the **WNetAddConnection2** function, a handle to a window that the network provider can use as an owner window for dialog boxes. |
| [**WNetCancelConnection**](wnetcancelconnection.md)                         | Cancels a network connection. (Provided for compatibility with 16-bit versions of Windows.)                                                                                                                                    |
| [**WNetCancelConnection2**](wnetcancelconnection2.md)                       | Cancels a network connection, providing the ability to update the user profile with information about persistent connections.                                                                                                  |
| [**WNetConnectionDialog**](wnetconnectiondialog.md)                         | Starts a general browsing dialog box for connecting to network resources.                                                                                                                                                      |
| [**WNetConnectionDialog1**](wnetconnectiondialog1.md)                       | Starts a general browsing dialog box for connecting to network resources, using a [**CONNECTDLGSTRUCT**](connectdlgstruct-str.md) structure.                                                                                  |
| [**WNetDisconnectDialog**](wnetdisconnectdialog.md)                         | Starts a general browsing dialog box for disconnecting from network resources.                                                                                                                                                 |
| [**WNetDisconnectDialog1**](wnetdisconnectdialog1.md)                       | Starts a general browsing dialog box for disconnecting from network resources, using a [**DISCDLGSTRUCT**](discdlgstruct-str.md) structure.                                                                                   |
| [**WNetGetConnection**](wnetgetconnection.md)                               | Retrieves the name of the network resource associated with a local device.                                                                                                                                                     |
| [**WNetGetUniversalName**](wnetgetuniversalname.md)                         | When given a drive-based path for a network resource, returns a more universal form of the name.                                                                                                                               |
| [**WNetRestoreConnectionW**](wnetrestoreconnectionw.md)                     | Restores the connection to a network resource, prompting the user, if necessary, for a name and password.                                                                                                                      |
| [**WNetUseConnection**](wnetuseconnection.md)                               | Connects a local device to a network resource; automatically selects an unused local device to redirect to the network resource.                                                                                               |



 

> [!Note]  
> The [**WNetAddConnection**](wnetaddconnection.md) and [**WNetCancelConnection**](wnetcancelconnection.md) functions are supported for compatibility with Windows for Workgroups. However, new applications should use [**WNetAddConnection2**](wnetaddconnection2.md) or [**WNetAddConnection3**](wnetaddconnection3.md), and [**WNetCancelConnection2**](wnetcancelconnection2.md).

 

## Enumeration Functions

Call the following WNet functions to enumerate network resources.



| Function                                     | Description                                                                             |
|----------------------------------------------|-----------------------------------------------------------------------------------------|
| [**WNetCloseEnum**](wnetcloseenum.md)       | Ends a network resource enumeration.                                                    |
| [**WNetEnumResource**](wnetenumresource.md) | Continues an enumeration of network resources started by the **WNetOpenEnum** function. |
| [**WNetOpenEnum**](wnetopenenum.md)         | Starts an enumeration of network resources.                                             |



 

## Information Functions

Call the following WNet informational and utility functions to retrieve network provider and other information.



| Function                                                         | Description                                                                                         |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [**WNetGetLastError**](wnetgetlasterror.md)                     | Returns the most recent error code set by a WNet function, the one reported by a network provider.  |
| [**WNetGetNetworkInformation**](wnetgetnetworkinformation.md)   | Returns extended information about a specific network provider.                                     |
| [**WNetGetProviderName**](wnetgetprovidername.md)               | Returns the provider name for a specific type of network.                                           |
| [**WNetGetResourceInformation**](wnetgetresourceinformation.md) | Returns the network provider that owns a resource, and obtains information about the resource type. |
| [**WNetGetResourceParent**](wnetgetresourceparent.md)           | Returns the parent of a network resource.                                                           |



 

## User Functions

Call the following WNet function to retrieve the name of the user associated with a local device.



| Function                           | Description                                                                              |
|------------------------------------|------------------------------------------------------------------------------------------|
| [**WNetGetUser**](wnetgetuser.md) | Returns the current default user name, or the user name that established the connection. |



 

Many of the WNet functions use a [**NETRESOURCE**](/windows/win32/Winnetwk/ns-winnetwk-_netresourcea?branch=master) structure to store information about a network resource.

 

 




