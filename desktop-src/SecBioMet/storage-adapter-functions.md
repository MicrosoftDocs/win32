---
title: Storage Adapter Functions
description: A storage adapter manages template databases.
ms.assetid: bfb0c9e5-a95e-4054-bc83-98ff682994a0
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Storage Adapter Functions

A storage adapter manages template databases. The following functions must be implemented by the adapter developer. They are called by the Windows Biometric service.

## In this section



| Topic                                                                                         | Description                                                                                                                             |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| [**StorageAdapterActivate**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_activate_fn?branch=master)<br/>                           | Gives the Storage Adapter the chance to perform any work needed to bring the storage component out of an idle state.<br/>         |
| [**StorageAdapterAddRecord**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_add_record_fn?branch=master)<br/>                         | Adds a template to the database.<br/>                                                                                             |
| [**StorageAdapterAttach**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_attach_fn?branch=master)<br/>                               | Adds a storage adapter to the processing pipeline of the biometric unit.<br/>                                                     |
| [**StorageAdapterClearContext**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_clear_context_fn?branch=master)<br/>                   | Prepares the processing pipeline of the biometric unit for a new operation.<br/>                                                  |
| [**StorageAdapterCloseDatabase**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_close_database_fn?branch=master)<br/>                 | Closes the database associated with the pipeline and frees all related resources.<br/>                                            |
| [**StorageAdapterControlUnit**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_control_unit_fn?branch=master)<br/>                     | Performs a vendor-defined control operation that does not require elevated privilege.<br/>                                        |
| [**StorageAdapterControlUnitPrivileged**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_control_unit_privileged_fn?branch=master)<br/> | Performs a vendor-defined control operation that requires elevated privilege.<br/>                                                |
| [**StorageAdapterCreateDatabase**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_create_database_fn?branch=master)<br/>               | Creates and configures a new database.<br/>                                                                                       |
| [**StorageAdapterDeactivate**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_deactivate_fn?branch=master)<br/>                       | Gives the Storage Adapter the chance to perform any work needed to put the storage component into an idle state.<br/>             |
| [**StorageAdapterDeleteRecord**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_delete_record_fn?branch=master)<br/>                   | Deletes one or more templates from the database.<br/>                                                                             |
| [**StorageAdapterDetach**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_detach_fn?branch=master)<br/>                               | Releases adapter-specific resources attached to the pipeline.<br/>                                                                |
| [**StorageAdapterEraseDatabase**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_erase_database_fn?branch=master)<br/>                 | Erases the database and marks it for deletion.<br/>                                                                               |
| [**StorageAdapterFirstRecord**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_first_record_fn?branch=master)<br/>                     | Positions the result set cursor on the first record in the set.<br/>                                                              |
| [**StorageAdapterGetCurrentRecord**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_get_current_record_fn?branch=master)<br/>           | Retrieves the contents of the current record in the pipeline result set.<br/>                                                     |
| [**StorageAdapterGetDatabaseSize**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_get_database_size_fn?branch=master)<br/>             | Retrieves the database size and available space.<br/>                                                                             |
| [**StorageAdapterGetDataFormat**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_get_data_format_fn?branch=master)<br/>                 | Retrieves format and version information used by the current database associated with the pipeline.<br/>                          |
| [**StorageAdapterGetRecordCount**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_get_record_count_fn?branch=master)<br/>               | Retrieves the number of template records in the pipeline result set.<br/>                                                         |
| [**StorageAdapterNextRecord**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_next_record_fn?branch=master)<br/>                       | Advances the result set cursor by one record.<br/>                                                                                |
| [*StorageAdapterNotifyPowerChange*](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_notify_power_change_fn?branch=master)<br/>           | Receives notification about a change in the computer power state and prepares the storage adapter accordingly.<br/>               |
| [**StorageAdapterOpenDatabase**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_open_database_fn?branch=master)<br/>                   | Opens a database for use by the storage adapter.<br/>                                                                             |
| [**StorageAdapterPipelineCleanup**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_pipeline_cleanup_fn?branch=master)<br/>             | Gives the Storage Adapter the chance to perform any cleanup in preparation for closing the template database.<br/>                |
| [**StorageAdapterPipelineInit**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_pipeline_init_fn?branch=master)<br/>                   | Gives the Storage Adapter the chance to perform any initialization that remains incomplete.<br/>                                  |
| [**StorageAdapterQueryByContent**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_query_by_content_fn?branch=master)<br/>               | Queries the database that is currently open for templates associated with a specified index vector.<br/>                          |
| [**StorageAdapterQueryBySubject**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_query_by_subject_fn?branch=master)<br/>               | Queries the database that is currently open for templates associated with a specified identity and sub-factor.<br/>               |
| [**StorageAdapterQueryExtendedInfo**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_query_extended_info_fn?branch=master)<br/>         | Determines the capabilities and limitations of the biometric storage component.<br/>                                              |
| [**WbioQueryStorageInterface**](/windows/win32/Winbio_adapter/nf-winbio_adapter-wbioquerystorageinterface?branch=master)<br/>                     | Retrieves a pointer to the [**WINBIO\_STORAGE\_INTERFACE**](/windows/win32/Winbio_adapter/ns-winbio_adapter-_winbio_storage_interface?branch=master) structure for the storage adapter.<br/> |



 

## Related topics

<dl> <dt>

[Plug-in Functions](plug-in-functions.md)
</dt> </dl>

 

 





