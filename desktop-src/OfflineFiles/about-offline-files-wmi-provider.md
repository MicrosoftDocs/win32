---
Description: 'The Offline Files WMI provider enables administrators and developers to access with scripts a subset of the functionality offered by the Offline Files API Reference.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '5646e766-715c-4920-ab3c-04423a3f6f10'
ms.prod: 'windows-server-dev'
ms.technology: 'offline-files'
ms.tgt_platform: multiple
title: About Offline Files WMI Provider
---

# About Offline Files WMI Provider

The Offline Files WMI provider enables administrators and developers to access with scripts a subset of the functionality offered by the [Offline Files API Reference](offline-files-api-reference.md).

> [!Note]  
> On Windows Server operating systems beginning with Windows Server 2008 R2, the Offline Files COM API and WMI provider are available only if the [Desktop Experience](http://go.microsoft.com/fwlink/p/?linkid=140788) feature is installed.

 

The OfflineFilesWmiProvider.mof file defines the Offline Files WMI provider described in the [Offline Files WMI Provider Reference](offline-files-wmi-provider-reference.md) section. You can access the Offline Files provider classes in the ROOT\\CIMV2 namespace. For more information about WMI, see [Windows Management Instrumentation](https://msdn.microsoft.com/library/aa394582). The computer must be running Windows Vista or Windows Server 2008 to use Offline Files.

An object of the [**Win32\_OfflineFilesCache**](win32-offlinefilescache.md) class represents the single Offline Files cache available on the computer. Each computer can have only one instance of the **Win32\_OfflineFilesCache** class. The items in the cache represent remote servers, shares, directories, and files being cached on the local computer. The Location property of an object of this class provides the location of the directory containing the Offline Files cache. Use this object to enable, disable, and manipulate Offline Files on the local computer.

An object of the [**Win32\_OfflineFilesItem**](win32-offlinefilesitem.md) class represents a single file, directory, share, or server in the Offline Files cache. Properties of this class expose change information, connection information, encryption information, file system information, file system name, UNC path of parent item, and pin information for the item.

An object of the [**Win32\_OfflineFilesFileSysInfo**](win32-offlinefilesfilesysinfo.md) class represents the common file system information about a file or directory in the Offline Files cache, such as file attributes, size, and time values. An instance of this class is obtained through the FileSysInfo property of the [**Win32\_OfflineFilesItem**](win32-offlinefilesitem.md) object.

An object of [**Win32\_OfflineFilesPinInfo**](win32-offlinefilespininfo.md) class represents the pinned status of an item in the Offline Files cache. When an item is pinned in the Offline Files cache, it is guaranteed to be available offline. An instance of this class is obtained through the PinInfo property of the [**Win32\_OfflineFilesItem**](win32-offlinefilesitem.md) object.

An object of the [**Win32\_OfflineFilesChangeInfo**](win32-offlinefileschangeinfo.md) class represents the information associated with local changes made to an item in the Offline Files cache while working offline. Use to determine whether the item was created, deleted, or modified offline. These are changes to the copy of the item on the local computer that have not been synchronized with the remote copy. An instance of this class is obtained through the ChangeInfo property of the [**Win32\_OfflineFilesItem**](win32-offlinefilesitem.md) object.

An object of the [**Win32\_OfflineFilesConnectionInfo**](win32-offlinefilesconnectioninfo.md) class represents the current connection state of the item: unknown, online, or offline. An instance of this class is obtained through the ConnectionInfo property of the [**Win32\_OfflineFilesItem**](win32-offlinefilesitem.md) object.

An object of the [**Win32\_OfflineFilesSuspendInfo**](win32-offlinefilessuspendinfo.md) class represents whether an item is suspended or not and, if so, if it is a suspended root or not. An instance of this class is obtained through the SuspendInfo property of the [**Win32\_OfflineFilesItem**](win32-offlinefilesitem.md) object.

The [**Win32\_OfflineFilesAssociatedItems**](win32-offlinefilesassociateditems.md) class is reserved for future use.

Note that the scripting interface implicitly uses flat enumeration of items in the Offline Files cache. It is not possible to traverse the items in the Offline Files cache using the hierarchical enumeration possible with the COM-based API and implemented by the Offline Files API Interfaces. For more information, see [About Offline Files API](about-offline-files-api.md).

 

 



