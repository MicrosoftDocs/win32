---
title: ICatAdm interface
description: Manages a catalog definition for Indexing Service.
ms.assetid: 72ed5a66-85aa-4e76-a826-1f952a547a39
keywords:
- ICatAdm interface Indexing Service
- ICatAdm interface Indexing Service , described
topic_type:
- apiref
api_name:
- ICatAdm
api_location:
- Ciodm.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# ICatAdm interface

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Manages a catalog definition for Indexing Service. The catalog defines the set of documents to index by specifying the list of directories that are used by Indexing Service to determine the files to index. Catalog objects can be created only by means of the [**AddCatalog**](iadminindexserver-addcatalog.md) method on the AdminIndexServer object and can be retrieved by either of the following:

-   The enumeration methods [**FindFirstCatalog**](iadminindexserver-findfirstcatalog.md) and [**FindNextCatalog**](iadminindexserver-findnextcatalog.md) on AdminIndexServer
-   The [**GetCatalogByName**](iadminindexserver-getcatalogbyname.md) on AdminIndexServer

The properties supported on this object include counters that show the current state of the indexing process.

Use methods defined on the CatAdm object to monitor performance, adjust local parameters, force merges, and add and remove scopes from the catalog.

## Members

The **ICatAdm** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **ICatAdm** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ICatAdm** interface has these methods.



| Method                                               | Description                                                      |
|:-----------------------------------------------------|:-----------------------------------------------------------------|
| [**AddScope**](icatadm-addscope.md)                 | Creates a new scope.<br/>                                  |
| [**ContinueCatalog**](icatadm-continuecatalog.md)   | Starts the catalog and retrieves its previous state.<br/>  |
| [**FindFirstScope**](icatadm-findfirstscope.md)     | Finds the first scope in an enumeration.<br/>              |
| [**FindNextScope**](icatadm-findnextscope.md)       | Finds the next scope in an enumeration.<br/>               |
| [**ForceMasterMerge**](icatadm-forcemastermerge.md) | Begins a master index merge for the catalog.<br/>          |
| [**GetScope**](icatadm-getscope.md)                 | Retrieves current scope object.<br/>                       |
| [**GetScopeByAlias**](icatadm-getscopebyalias.md)   | Retrieves a scope object by alias name.<br/>               |
| [**GetScopeByPath**](icatadm-getscopebypath.md)     | Retrieves a scope object by path name.<br/>                |
| [**IsCatalogPaused**](icatadm-iscatalogpaused.md)   | Determines whether the catalog is in read-only mode.<br/>  |
| [**IsCatalogRunning**](icatadm-iscatalogrunning.md) | Determines whether the catalog is in read/write mode.<br/> |
| [**IsCatalogStopped**](icatadm-iscatalogstopped.md) | Determines whether the catalog is stopped.<br/>            |
| [**PauseCatalog**](icatadm-pausecatalog.md)         | Pauses the catalog and retrieves its previous state.<br/>  |
| [**RemoveScope**](icatadm-removescope.md)           | Removes an existing scope object from a collection.<br/>   |
| [**StartCatalog**](icatadm-startcatalog.md)         | Starts the catalog and retrieves its previous state.<br/>  |
| [**StopCatalog**](icatadm-stopcatalog.md)           | Stops the catalog and retrieves its previous state.<br/>   |



 

### Properties

The **ICatAdm** interface has these properties.



| Property                                                                  | Access type          | Description                                                                                                                            |
|:--------------------------------------------------------------------------|:---------------------|:---------------------------------------------------------------------------------------------------------------------------------------|
| [**CatalogLocation**](icatadm-cataloglocation.md)<br/>             | Read-only<br/> | The case-insentitive path.<br/>                                                                                                  |
| [**CatalogName**](icatadm-catalogname.md)<br/>                     | Read-only<br/> | The case-insensitive catalog name.<br/>                                                                                          |
| [**DelayedFilterCount**](icatadm-delayedfiltercount.md)<br/>       | Read-only<br/> | The number of documents delayed for indexing during a previous pass. Possible reasons for delay include sharing violations.<br/> |
| [**DocumentsToFilter**](icatadm-documentstofilter.md)<br/>         | Read-only<br/> | The number of documents to be indexed.<br/>                                                                                      |
| [**FilteredDocumentCount**](icatadm-filtereddocumentcount.md)<br/> | Read-only<br/> | The number of documents indexed since the last time Indexing Service started.<br/>                                               |
| [**FreshTestCount**](icatadm-freshtestcount.md)<br/>               | Read-only<br/> | The number of entries in the fresh test list. For internal use only.<br/>                                                        |
| [**IndexSize**](icatadm-indexsize.md)<br/>                         | Read-only<br/> | The total size of the index, in megabytes. Includes master and shadow indexes, and the property store.<br/>                      |
| [**IsUpToDate**](icatadm-isuptodate.md)<br/>                       | Read-only<br/> | Indicates whether the index is up to date.<br/>                                                                                  |
| [**PctMergeComplete**](icatadm-pctmergecomplete.md)<br/>           | Read-only<br/> | The percentage of the merge process completed.<br/>                                                                              |
| [**PendingScanCount**](icatadm-pendingscancount.md)<br/>           | Read-only<br/> | The number of directories to be scanned.<br/>                                                                                    |
| [**PersistentIndexCount**](icatadm-persistentindexcount.md)<br/>   | Read-only<br/> | The number of persistent indexes that currently exist.<br/>                                                                      |
| [**QueryCount**](icatadm-querycount.md)<br/>                       | Read-only<br/> | The number of active queries since Indexing Service started.<br/>                                                                |
| [**StateInfo**](icatadm-stateinfo.md)<br/>                         | Read-only<br/> | The state of the service.<br/>                                                                                                   |
| [**TotalDocumentCount**](icatadm-totaldocumentcount.md)<br/>       | Read-only<br/> | The total document count in the set of documents to be indexed.<br/>                                                             |
| [**UniqueKeyCount**](icatadm-uniquekeycount.md)<br/>               | Read-only<br/> | The number of unique keys. Includes existing persistent indexes and nonpersistent wordlists.<br/>                                |
| [**WordListCount**](icatadm-wordlistcount.md)<br/>                 | Read-only<br/> | The number of existing word lists.<br/>                                                                                          |



 

## Remarks

Access CatAdm objects only through methods defined on the AdminIndexServer object.

This object supports IErrorInfo to report errors.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows 7<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                    |
| DLL<br/>                      | <dl> <dt>Ciodm.dll</dt> </dl> |



 

 





