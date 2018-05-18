---
Description: 'The Offline Files application programming interface enables applications to control and monitor the local client side caching of files, servers, shares, and directories.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '4ceaa0bc-ee25-49c5-a759-2d020a315256'
ms.prod: 'windows-server-dev'
ms.technology: 'offline-files'
ms.tgt_platform: multiple
title: About Offline Files API
---

# About Offline Files API

The Offline Files application programming interface enables applications to control and monitor the local client side caching of files, servers, shares, and directories. Applications can use the functions and interfaces described in the [Offline Files API Reference](offline-files-api-reference.md) section to enumerate, find, add, remove, or synchronize the items saved in the local Offline Files cache. The computer must be running Windows Vista or Windows Server 2008 to use the Offline Files API.

> [!Note]  
> On Windows Server operating systems beginning with Windows Server 2008 R2, the Offline Files COM API and WMI provider are available only if the [Desktop Experience](http://go.microsoft.com/fwlink/p/?linkid=140788) feature is installed.

 

## Offline Files Service

Offline Files needs to be both enabled and running before an application can use the [Offline Files API interfaces](offline-files-api-interfaces.md). The [Offline Files API](offline-files-api-functions.md) provides two functions used to query the current state and to enable or disable Offline Files: [**OfflineFilesEnable**](offlinefilesenable.md) and [**OfflineFilesQueryStatus**](offlinefilesquerystatus.md). Applications are required to use these functions to query or change the state of the Offline Files feature. The COM-based Offline Files API interfaces can be used to perform all other Offline Files operations.

Applications can use the [**OfflineFilesQueryStatus**](offlinefilesquerystatus.md) function to determine the current state of Offline Files. Parameter values returned by this function indicate whether the two parts of Offline Files—the Offline Files service and the Client Side Caching (CSC) driver—are enabled and running.

Applications can use the [**OfflineFilesEnable**](offlinefilesenable.md) function to enable or disable Offline Files. A restart of the computer is required after calling this function unless the Offline Files service and the CSC driver are both already running and enabled.

## Offline Files Cache

The Offline Files object model uses multiple item objects to represent the servers, shares, directories, and files being saved offline, and a single cache object to represent the local store containing the offline copies of these items. After starting Offline Files, the application can use the [**CoCreateInstance**](_com_cocreateinstance) function to create an instance of the [**IOfflineFilesCache**](iofflinefilescache.md) interface.

Applications can add and delete items from the Offline Files cache, query items in the cache, synchronize items in the cache, and encrypt the contents of the cache for enhanced data security by using the methods available on the [**IOfflineFilesCache**](iofflinefilescache.md) interface.

The [**IOfflineFilesItem**](iofflinefilesitem.md) interface provides the functionality that is common to all items and can be used to obtain name, type, and capability information for any item in the Offline Files cache. Offline Files exposes item information on interfaces supported by an instance of the **IOfflineFilesItem** interface. For example, an item in the offline cache can be recognized as a directory because it has an instance of **IOfflineFilesItem** interface that supports the [**IOfflineFilesDirectoryItem**](iofflinefilesdirectoryitem.md) interface. After an application obtains an instance of **IOfflineFilesItem** interface, it can use the [**QueryInterface**](_com_iunknown_queryinterface) method to determine whether an interface of interest is supported. The application can alternatively use the [**GetItemType Method of the IOfflineFilesItem Interface**](iofflinefilesitem-getitemtype.md) to obtain type information for an item.

The Offline Files object model represents items in the cache as types: server, share, directory, and file. For each type of item, Offline Files exposes an interface: the [**IOfflineFilesServerItem**](iofflinefilesserveritem.md), [**IOfflineFilesShareItem**](iofflinefilesshareitem.md), [**IOfflineFilesDirectoryItem**](iofflinefilesdirectoryitem.md), and [**IEnumOfflineFilesItems**](ienumofflinefilesitems.md) interfaces. The Offline Files object model organizes items into a hierarchy of containers and contained items. If an item supports the [**IOfflineFilesItemContainer**](iofflinefilesitemcontainer.md) interface, it can contain other items. Not all items contain child items. For example, if [**QueryInterface**](_com_iunknown_queryinterface) is called for the **IOfflineFilesItemContainer** interface on an instance of the [**IOfflineFilesFileItem**](iofflinefilesfileitem.md) interface, it returns with **E\_NOINTERFACE**, because a file item cannot contain other items.

## Offline Files Enumeration

Applications can use the enumerator methods on the [**IOfflineFilesItemContainer**](iofflinefilesitemcontainer.md) interface to perform a hierarchical traversal of the items in the Offline Files cache. For an example of hierarchical enumeration, see the [**EnumItems Method of the IOfflineFilesItemContainer Interface**](iofflinefilesitemcontainer-enumitems.md). First the application enumerates server items in the cache, then share items from each server, then directory and file items from each share, and finally directory and file items from each directory. This form of enumeration creates an enumerator object for each container item. Hierarchical enumeration enables the greatest control over whether or not a particular scope in the cache gets enumerated.

Applications can use the [**EnumItemsEx Method of the IOfflineFilesItemContainer Interface**](iofflinefilesitemcontainer-enumitemsex.md) to perform a flat enumeration of items in the Offline Files cache. Flat enumeration performs a traversal of the cache in which any child items are enumerated immediately after each container item. For example, a directory item is returned followed by any of its immediate children directories or files. Only one enumerator object is created when using flat enumeration.

## Enumeration Filters

Applications using the [**EnumItemsEx Method of the IOfflineFilesItemContainer Interface**](iofflinefilesitemcontainer-enumitemsex.md) can include or exclude files or directories from flat enumeration based upon a comparison of item flags, file name, or times. A specification of a filter can by implemented with the [**IOfflineFilesItemFilter**](iofflinefilesitemfilter.md) interface.

The [**GetPatternFilter Method of the IOfflineFilesItemFilter Interface**](iofflinefilesitemfilter-getpatternfilter.md) specifies a file or directory name to control filename-based filtering of files or directories. This works similar to the [**FindFirstFile**](https://msdn.microsoft.com/library/windows/desktop/aa364418) function, and searches for a file or subdirectory with a name that matches a specific name. The name can include wildcard characters. The enumeration then returns only items that match that wildcard specification. Only names to be included in the enumeration can be specified. There is no way to exclude items matching the name. This type of filtering is applied before any other types of filtering.

The [**GetFilterFlags Method of the IOfflineFilesItemFilter Interface**](iofflinefilesitemfilter-getfilterflags.md) provides flags used to control flag-based filtering of files or directories. This method uses the [**Offline Files filter flags**](offline-files-filter-flags.md) to specify files or directories. Items can be included or excluded based upon the comparison.

The [**GetTimeFilter Method of the IOfflineFilesItemFilter Interface**](iofflinefilesitemfilter-gettimefilter.md) provides time specifications used to control time-based filtering of files or directories. Time-based filtering can compare the item’s Creation, Last Write, or Last Access time to a specified UTC time. The comparison can be Equal to ( == ), Not equal to ( != ), Less than ( &lt; ), Greater than ( &gt; ), Less than or equal to ( &lt;= ), and Greater than or equal to ( &gt;= ) operators. Items can be included or excluded based upon the comparison.

## Offline Files Events

Offline Files enables applications to receive progress events for lengthy operations. Applications can implement the [**IOfflineFilesProgress**](iofflinefilesprogress.md), [**IOfflineFilesSyncProgress**](iofflinefilessyncprogress.md), and [**IOfflineFilesSimpleProgress**](iofflinefilessimpleprogress.md) interfaces to receive begin and end notifications with methods that support reporting progress events. Applications can register to receive progress events simply by passing an interface pointer to a method that supports progress events. It is not necessary to register progress events.

Offline Files enables applications to register to receive events associated with Offline Files. A cache object exposes a connection point container implementing the [**IConnectionPointContainer**](_com_iconnectionpointcontainer) interface. Applications can call methods on this interface to obtain the IConnectionPoint Interface associated with a particular type of event. Having a pointer to an IConnectionPoint interface, the client then calls the Advise method to connect its event sink interface to the event source. To receive Offline Files events, an application can implement an event sink object using the [**IOfflineFilesEvents**](iofflinefilesevents.md) or [**IOfflineFilesEvents2**](iofflinefilesevents2.md) interface. To receive all events, register the interface implementation using [**IConnectionPoint::Advise**](_com_iconnectionpoint_advise). A cache object is a connection point container implementing **IConnectionPointContainer**.

## Event Filters

Event filtering enables an application to receive only a specified subset of events. The application can specify the events to filter using the methods of the [**IOfflineFilesEventsFilter**](iofflinefileseventsfilter.md) interface. The events specified by the [**Ping Method of the IOfflineFilesEvents Interface**](iofflinefilesevents-ping.md) and the [**DataLost Method of the IOfflineFilesEvents Interface**](iofflinefilesevents-datalost.md) cannot be filtered and are always delivered to the application.

Path filtering enables an application to receive only events that involve files or directories within the scope of a specified file path. The path filter may be a single file or directory, a single directory and its immediate contents or a single directory and its entire contents recursively. As with event filtering, applications implement the [**IOfflineFilesEventsFilter**](iofflinefileseventsfilter.md) interface. In this case we implement the [**GetPathFilter method**](iofflinefileseventsfilter-getpathfilter.md). Only one path filter per event sink is supported. If multiple path filters are necessary, multiple event sinks must be created and registered, each with its own path filter.

## Offline Files Settings

Applications can access the value of setting preferences used to control Offline Files. Offline Files determines the value of a setting based upon the priority of setting values and uses the highest priority value available. From the greatest to least priority, the setting values are per-machine policy, per-user policy, per-machine preference, per-user preference, and internal default. Methods of the [**IOfflineFilesSetting**](iofflinefilessetting.md) interface enable applications to query or update settings. There is no way to set policy using the Offline Files API. Applications can create an enumerator of instances of the **IOfflineFilesSetting** interface with the [**EnumSettingObjects Method of the IOfflineFilesCache Interface**](iofflinefilescache-enumsettingobjects.md). Applications can create an instance of the **IOfflineFilesSetting** interface with the [**GetSettingObject Method of the IOfflineFilesCache Interface**](iofflinefilescache-getsettingobject.md).

## Scriptable Interface

A scriptable interface is offered by the Offline Files WMI provider and provides a subset of the functionality available using the COM-based API. For more information see [About Offline Files WMI Provider](about-offline-files-wmi-provider.md).

 

 



