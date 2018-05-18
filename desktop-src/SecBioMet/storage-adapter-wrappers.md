---
title: Storage Adapter Wrappers
description: Functions that you can use to call functions on your storage adapter. These functions are defined in Winbio\_adapter.h.
ms.assetid: '3e7ff098-b8f3-4745-aa75-712a392c6c78'
---

# Storage Adapter Wrappers

The following wrapper functions are defined in Winbio\_adapter.h. You can use them to call functions on your storage adapter.



| Function                                    | Description                                                                                                                                                                     |
|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WbioStorageActivate<br/>              | Calls the [**StorageAdapterActivate**](storageadapteractivate.md) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                   |
| WbioStorageAddRecord<br/>             | Calls the [**StorageAdapterAddRecord**](storageadapteraddrecord.md) function.<br/>                                                                                       |
| WbioStorageAttach<br/>                | Calls the [**StorageAdapterAttach**](storageadapterattach.md) function.<br/>                                                                                             |
| WbioStorageClearContext<br/>          | Calls the [**StorageAdapterClearContext**](storageadapterclearcontext.md) function.<br/>                                                                                 |
| WbioStorageCloseDatabase<br/>         | Calls the [**StorageAdapterCloseDatabase**](storageadapterclosedatabase.md) function.<br/>                                                                               |
| WbioStorageControlUnit<br/>           | Calls the [**StorageAdapterControlUnit**](storageadaptercontrolunit.md) function.<br/>                                                                                   |
| WbioStorageControlUnitPrivileged<br/> | Calls the [**StorageAdapterControlUnitPrivileged**](storageadaptercontrolunitprivileged.md) function.<br/>                                                               |
| WbioStorageCreateDatabase<br/>        | Calls the [**StorageAdapterCreateDatabase**](storageadaptercreatedatabase.md) function.<br/>                                                                             |
| WbioStorageDeactivate<br/>            | Calls the [**StorageAdapterDeactivate**](storageadapterdeactivate.md) function.<br/> This wrapper function is supported starting in Windows 10.<br/>               |
| WbioStorageDeleteRecord<br/>          | Calls the [**StorageAdapterDeleteRecord**](storageadapterdeleterecord.md) function.<br/>                                                                                 |
| WbioStorageDetach<br/>                | Calls the [**StorageAdapterDetach**](storageadapterdetach.md) function.<br/>                                                                                             |
| WbioStorageEraseDatabase<br/>         | Calls the [**StorageAdapterEraseDatabase**](storageadaptererasedatabase.md) function.<br/>                                                                               |
| WbioStorageFirstRecord<br/>           | Calls the [**StorageAdapterFirstRecord**](storageadapterfirstrecord.md) function.<br/>                                                                                   |
| WbioStorageGetCurrentRecord<br/>      | Calls the [**StorageAdapterGetCurrentRecord**](storageadaptergetcurrentrecord.md) function.<br/>                                                                         |
| WbioStorageGetDatabaseSize<br/>       | Calls the [**StorageAdapterGetDatabaseSize**](storageadaptergetdatabasesize.md) function.<br/>                                                                           |
| WbioStorageGetDataFormat<br/>         | Calls the [**StorageAdapterGetDataFormat**](storageadaptergetdataformat.md) function.<br/>                                                                               |
| WbioStorageGetRecordCount<br/>        | Calls the [**StorageAdapterGetRecordCount**](storageadaptergetrecordcount.md) function.<br/>                                                                             |
| WbioStorageNextRecord<br/>            | Calls the [**StorageAdapterNextRecord**](storageadapternextrecord.md) function.<br/>                                                                                     |
| WbioStorageNotifyPowerChange<br/>     | Calls the [*StorageAdapterNotifyPowerChange*](storageadapternotifypowerchange.md) function.<br/> This wrapper function is supported starting in Windows 8.<br/>    |
| WbioStorageOpenDatabase<br/>          | Calls the [**StorageAdapterOpenDatabase**](storageadapteropendatabase.md) function.<br/>                                                                                 |
| WbioStoragePipelineCleanup<br/>       | Calls the [**StorageAdapterPipelineCleanup**](storageadapterpipelinecleanup.md) function.<br/> This wrapper function is supported starting in Windows 10.<br/>     |
| WbioStoragePipelineInit<br/>          | Calls the [**StorageAdapterPipelineInit**](storageadapterpipelineinit.md) function.<br/> This wrapper function is supported starting in Windows 10.<br/>           |
| WbioStorageQueryByContent<br/>        | Calls the [**StorageAdapterQueryByContent**](storageadapterquerybycontent.md) function.<br/>                                                                             |
| WbioStorageQueryBySubject<br/>        | Calls the [**StorageAdapterQueryBySubject**](storageadapterquerybysubject.md) function.<br/>                                                                             |
| WbioStorageQueryExtendedInfo<br/>     | Calls the [**StorageAdapterQueryExtendedInfo**](storageadapterqueryextendedinfo.md) function.<br/> This wrapper function is supported starting in Windows 10.<br/> |



 

## Related topics

<dl> <dt>

[Storage Adapter Functions](storage-adapter-functions.md)
</dt> <dt>

[Plug-in Functions](plug-in-functions.md)
</dt> </dl>

 

 





