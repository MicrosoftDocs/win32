---
title: Storage Adapter Wrappers
description: Functions that you can use to call functions on your storage adapter. These functions are defined in Winbio\_adapter.h.
ms.assetid: 3e7ff098-b8f3-4745-aa75-712a392c6c78
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Storage Adapter Wrappers

The following wrapper functions are defined in Winbio\_adapter.h. You can use them to call functions on your storage adapter.



| Function                                    | Description                                                                                                                                                                     |
|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WbioStorageActivate<br/>              | Calls the [**StorageAdapterActivate**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_activate_fn?branch=master) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                   |
| WbioStorageAddRecord<br/>             | Calls the [**StorageAdapterAddRecord**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_add_record_fn?branch=master) function.<br/>                                                                                       |
| WbioStorageAttach<br/>                | Calls the [**StorageAdapterAttach**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_attach_fn?branch=master) function.<br/>                                                                                             |
| WbioStorageClearContext<br/>          | Calls the [**StorageAdapterClearContext**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_clear_context_fn?branch=master) function.<br/>                                                                                 |
| WbioStorageCloseDatabase<br/>         | Calls the [**StorageAdapterCloseDatabase**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_close_database_fn?branch=master) function.<br/>                                                                               |
| WbioStorageControlUnit<br/>           | Calls the [**StorageAdapterControlUnit**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_control_unit_fn?branch=master) function.<br/>                                                                                   |
| WbioStorageControlUnitPrivileged<br/> | Calls the [**StorageAdapterControlUnitPrivileged**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_control_unit_privileged_fn?branch=master) function.<br/>                                                               |
| WbioStorageCreateDatabase<br/>        | Calls the [**StorageAdapterCreateDatabase**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_create_database_fn?branch=master) function.<br/>                                                                             |
| WbioStorageDeactivate<br/>            | Calls the [**StorageAdapterDeactivate**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_deactivate_fn?branch=master) function.<br/> This wrapper function is supported starting in Windows 10.<br/>               |
| WbioStorageDeleteRecord<br/>          | Calls the [**StorageAdapterDeleteRecord**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_delete_record_fn?branch=master) function.<br/>                                                                                 |
| WbioStorageDetach<br/>                | Calls the [**StorageAdapterDetach**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_detach_fn?branch=master) function.<br/>                                                                                             |
| WbioStorageEraseDatabase<br/>         | Calls the [**StorageAdapterEraseDatabase**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_erase_database_fn?branch=master) function.<br/>                                                                               |
| WbioStorageFirstRecord<br/>           | Calls the [**StorageAdapterFirstRecord**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_first_record_fn?branch=master) function.<br/>                                                                                   |
| WbioStorageGetCurrentRecord<br/>      | Calls the [**StorageAdapterGetCurrentRecord**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_get_current_record_fn?branch=master) function.<br/>                                                                         |
| WbioStorageGetDatabaseSize<br/>       | Calls the [**StorageAdapterGetDatabaseSize**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_get_database_size_fn?branch=master) function.<br/>                                                                           |
| WbioStorageGetDataFormat<br/>         | Calls the [**StorageAdapterGetDataFormat**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_get_data_format_fn?branch=master) function.<br/>                                                                               |
| WbioStorageGetRecordCount<br/>        | Calls the [**StorageAdapterGetRecordCount**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_get_record_count_fn?branch=master) function.<br/>                                                                             |
| WbioStorageNextRecord<br/>            | Calls the [**StorageAdapterNextRecord**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_next_record_fn?branch=master) function.<br/>                                                                                     |
| WbioStorageNotifyPowerChange<br/>     | Calls the [*StorageAdapterNotifyPowerChange*](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_notify_power_change_fn?branch=master) function.<br/> This wrapper function is supported starting in Windows 8.<br/>    |
| WbioStorageOpenDatabase<br/>          | Calls the [**StorageAdapterOpenDatabase**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_open_database_fn?branch=master) function.<br/>                                                                                 |
| WbioStoragePipelineCleanup<br/>       | Calls the [**StorageAdapterPipelineCleanup**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_pipeline_cleanup_fn?branch=master) function.<br/> This wrapper function is supported starting in Windows 10.<br/>     |
| WbioStoragePipelineInit<br/>          | Calls the [**StorageAdapterPipelineInit**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_pipeline_init_fn?branch=master) function.<br/> This wrapper function is supported starting in Windows 10.<br/>           |
| WbioStorageQueryByContent<br/>        | Calls the [**StorageAdapterQueryByContent**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_query_by_content_fn?branch=master) function.<br/>                                                                             |
| WbioStorageQueryBySubject<br/>        | Calls the [**StorageAdapterQueryBySubject**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_query_by_subject_fn?branch=master) function.<br/>                                                                             |
| WbioStorageQueryExtendedInfo<br/>     | Calls the [**StorageAdapterQueryExtendedInfo**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_query_extended_info_fn?branch=master) function.<br/> This wrapper function is supported starting in Windows 10.<br/> |



 

## Related topics

<dl> <dt>

[Storage Adapter Functions](storage-adapter-functions.md)
</dt> <dt>

[Plug-in Functions](plug-in-functions.md)
</dt> </dl>

 

 





