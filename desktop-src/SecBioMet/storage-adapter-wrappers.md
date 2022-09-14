---
title: Storage Adapter Wrappers
description: Functions that you can use to call functions on your storage adapter. These functions are defined in Winbio\_adapter.h.
ms.assetid: 3e7ff098-b8f3-4745-aa75-712a392c6c78
ms.topic: article
ms.date: 05/31/2018
---

# Storage Adapter Wrappers

The following wrapper functions are defined in Winbio\_adapter.h. You can use them to call functions on your storage adapter.



| Function                                    | Description                                                                                                                                                                     |
|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WbioStorageActivate<br/>              | Calls the [**StorageAdapterActivate**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_storage_activate_fn) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                   |
| WbioStorageAddRecord<br/>             | Calls the [**StorageAdapterAddRecord**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_storage_add_record_fn) function.<br/>                                                                                       |
| WbioStorageAttach<br/>                | Calls the [**StorageAdapterAttach**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_storage_attach_fn) function.<br/>                                                                                             |
| WbioStorageClearContext<br/>          | Calls the [**StorageAdapterClearContext**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_storage_clear_context_fn) function.<br/>                                                                                 |
| WbioStorageCloseDatabase<br/>         | Calls the [**StorageAdapterCloseDatabase**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_storage_close_database_fn) function.<br/>                                                                               |
| WbioStorageControlUnit<br/>           | Calls the [**StorageAdapterControlUnit**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_storage_control_unit_fn) function.<br/>                                                                                   |
| WbioStorageControlUnitPrivileged<br/> | Calls the [**StorageAdapterControlUnitPrivileged**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_storage_control_unit_privileged_fn) function.<br/>                                                               |
| WbioStorageCreateDatabase<br/>        | Calls the [**StorageAdapterCreateDatabase**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_storage_create_database_fn) function.<br/>                                                                             |
| WbioStorageDeactivate<br/>            | Calls the [**StorageAdapterDeactivate**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_storage_deactivate_fn) function.<br/> This wrapper function is supported starting in Windows 10.<br/>               |
| WbioStorageDeleteRecord<br/>          | Calls the [**StorageAdapterDeleteRecord**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_storage_delete_record_fn) function.<br/>                                                                                 |
| WbioStorageDetach<br/>                | Calls the [**StorageAdapterDetach**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_storage_detach_fn) function.<br/>                                                                                             |
| WbioStorageEraseDatabase<br/>         | Calls the [**StorageAdapterEraseDatabase**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_storage_erase_database_fn) function.<br/>                                                                               |
| WbioStorageFirstRecord<br/>           | Calls the [**StorageAdapterFirstRecord**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_storage_first_record_fn) function.<br/>                                                                                   |
| WbioStorageGetCurrentRecord<br/>      | Calls the [**StorageAdapterGetCurrentRecord**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_storage_get_current_record_fn) function.<br/>                                                                         |
| WbioStorageGetDatabaseSize<br/>       | Calls the [**StorageAdapterGetDatabaseSize**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_storage_get_database_size_fn) function.<br/>                                                                           |
| WbioStorageGetDataFormat<br/>         | Calls the [**StorageAdapterGetDataFormat**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_storage_get_data_format_fn) function.<br/>                                                                               |
| WbioStorageGetRecordCount<br/>        | Calls the [**StorageAdapterGetRecordCount**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_storage_get_record_count_fn) function.<br/>                                                                             |
| WbioStorageNextRecord<br/>            | Calls the [**StorageAdapterNextRecord**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_storage_next_record_fn) function.<br/>                                                                                     |
| WbioStorageNotifyPowerChange<br/>     | Calls the [*StorageAdapterNotifyPowerChange*](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_storage_notify_power_change_fn) function.<br/> This wrapper function is supported starting in Windows 8.<br/>    |
| WbioStorageOpenDatabase<br/>          | Calls the [**StorageAdapterOpenDatabase**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_storage_open_database_fn) function.<br/>                                                                                 |
| WbioStoragePipelineCleanup<br/>       | Calls the [**StorageAdapterPipelineCleanup**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_storage_pipeline_cleanup_fn) function.<br/> This wrapper function is supported starting in Windows 10.<br/>     |
| WbioStoragePipelineInit<br/>          | Calls the [**StorageAdapterPipelineInit**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_storage_pipeline_init_fn) function.<br/> This wrapper function is supported starting in Windows 10.<br/>           |
| WbioStorageQueryByContent<br/>        | Calls the [**StorageAdapterQueryByContent**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_storage_query_by_content_fn) function.<br/>                                                                             |
| WbioStorageQueryBySubject<br/>        | Calls the [**StorageAdapterQueryBySubject**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_storage_query_by_subject_fn) function.<br/>                                                                             |
| WbioStorageQueryExtendedInfo<br/>     | Calls the [**StorageAdapterQueryExtendedInfo**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_storage_query_extended_info_fn) function.<br/> This wrapper function is supported starting in Windows 10.<br/> |



 

## Related topics

<dl> <dt>

[Storage Adapter Functions](storage-adapter-functions.md)
</dt> <dt>

[Plug-in Functions](plug-in-functions.md)
</dt> </dl>

 

 





