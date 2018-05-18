---
title: Storage Adapter Functions
description: A storage adapter manages template databases.
ms.assetid: 'bfb0c9e5-a95e-4054-bc83-98ff682994a0'
---

# Storage Adapter Functions

A storage adapter manages template databases. The following functions must be implemented by the adapter developer. They are called by the Windows Biometric service.

## In this section



| Topic                                                                                         | Description                                                                                                                             |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| [**StorageAdapterActivate**](storageadapteractivate.md)<br/>                           | Gives the Storage Adapter the chance to perform any work needed to bring the storage component out of an idle state.<br/>         |
| [**StorageAdapterAddRecord**](storageadapteraddrecord.md)<br/>                         | Adds a template to the database.<br/>                                                                                             |
| [**StorageAdapterAttach**](storageadapterattach.md)<br/>                               | Adds a storage adapter to the processing pipeline of the biometric unit.<br/>                                                     |
| [**StorageAdapterClearContext**](storageadapterclearcontext.md)<br/>                   | Prepares the processing pipeline of the biometric unit for a new operation.<br/>                                                  |
| [**StorageAdapterCloseDatabase**](storageadapterclosedatabase.md)<br/>                 | Closes the database associated with the pipeline and frees all related resources.<br/>                                            |
| [**StorageAdapterControlUnit**](storageadaptercontrolunit.md)<br/>                     | Performs a vendor-defined control operation that does not require elevated privilege.<br/>                                        |
| [**StorageAdapterControlUnitPrivileged**](storageadaptercontrolunitprivileged.md)<br/> | Performs a vendor-defined control operation that requires elevated privilege.<br/>                                                |
| [**StorageAdapterCreateDatabase**](storageadaptercreatedatabase.md)<br/>               | Creates and configures a new database.<br/>                                                                                       |
| [**StorageAdapterDeactivate**](storageadapterdeactivate.md)<br/>                       | Gives the Storage Adapter the chance to perform any work needed to put the storage component into an idle state.<br/>             |
| [**StorageAdapterDeleteRecord**](storageadapterdeleterecord.md)<br/>                   | Deletes one or more templates from the database.<br/>                                                                             |
| [**StorageAdapterDetach**](storageadapterdetach.md)<br/>                               | Releases adapter-specific resources attached to the pipeline.<br/>                                                                |
| [**StorageAdapterEraseDatabase**](storageadaptererasedatabase.md)<br/>                 | Erases the database and marks it for deletion.<br/>                                                                               |
| [**StorageAdapterFirstRecord**](storageadapterfirstrecord.md)<br/>                     | Positions the result set cursor on the first record in the set.<br/>                                                              |
| [**StorageAdapterGetCurrentRecord**](storageadaptergetcurrentrecord.md)<br/>           | Retrieves the contents of the current record in the pipeline result set.<br/>                                                     |
| [**StorageAdapterGetDatabaseSize**](storageadaptergetdatabasesize.md)<br/>             | Retrieves the database size and available space.<br/>                                                                             |
| [**StorageAdapterGetDataFormat**](storageadaptergetdataformat.md)<br/>                 | Retrieves format and version information used by the current database associated with the pipeline.<br/>                          |
| [**StorageAdapterGetRecordCount**](storageadaptergetrecordcount.md)<br/>               | Retrieves the number of template records in the pipeline result set.<br/>                                                         |
| [**StorageAdapterNextRecord**](storageadapternextrecord.md)<br/>                       | Advances the result set cursor by one record.<br/>                                                                                |
| [*StorageAdapterNotifyPowerChange*](storageadapternotifypowerchange.md)<br/>           | Receives notification about a change in the computer power state and prepares the storage adapter accordingly.<br/>               |
| [**StorageAdapterOpenDatabase**](storageadapteropendatabase.md)<br/>                   | Opens a database for use by the storage adapter.<br/>                                                                             |
| [**StorageAdapterPipelineCleanup**](storageadapterpipelinecleanup.md)<br/>             | Gives the Storage Adapter the chance to perform any cleanup in preparation for closing the template database.<br/>                |
| [**StorageAdapterPipelineInit**](storageadapterpipelineinit.md)<br/>                   | Gives the Storage Adapter the chance to perform any initialization that remains incomplete.<br/>                                  |
| [**StorageAdapterQueryByContent**](storageadapterquerybycontent.md)<br/>               | Queries the database that is currently open for templates associated with a specified index vector.<br/>                          |
| [**StorageAdapterQueryBySubject**](storageadapterquerybysubject.md)<br/>               | Queries the database that is currently open for templates associated with a specified identity and sub-factor.<br/>               |
| [**StorageAdapterQueryExtendedInfo**](storageadapterqueryextendedinfo.md)<br/>         | Determines the capabilities and limitations of the biometric storage component.<br/>                                              |
| [**WbioQueryStorageInterface**](wbioquerystorageinterface.md)<br/>                     | Retrieves a pointer to the [**WINBIO\_STORAGE\_INTERFACE**](winbio-storage-interface.md) structure for the storage adapter.<br/> |



 

## Related topics

<dl> <dt>

[Plug-in Functions](plug-in-functions.md)
</dt> </dl>

 

 





