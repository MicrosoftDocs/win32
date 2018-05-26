---
Description: The following enumerations are defined in the Volume Shadow Copy API.
ms.assetid: f2f09791-b17e-4f54-9d29-83a4189bffc1
title: Volume Shadow Copy API Enumerations
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Volume Shadow Copy API Enumerations

The following enumerations are defined in the Volume Shadow Copy API.



| Name                                                                           | Description                                                                                                                                                        |
|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**VSS\_ALTERNATE\_WRITER\_STATE**](/windows/win32/VsWriter/ne-vswriter-vss_alternate_writer_state?branch=master)            | Defines the set of valid states used to indicate whether a writer has an associated alternate writer.                                                              |
| [**VSS\_APPLICATION\_LEVEL**](/windows/win32/Vss/ne-vss-_vss_application_level?branch=master)                       | Defines the set of valid application levels.                                                                                                                       |
| [**VSS\_BACKUP\_SCHEMA**](/windows/win32/Vss/ne-vss-_vss_backup_schema?branch=master)                               | Defines the set of backup schemas—operations a writer can participate in.                                                                                          |
| [**VSS\_BACKUP\_TYPE**](/windows/win32/Vss/ne-vss-_vss_backup_type?branch=master)                                   | Defines the set of backup types.                                                                                                                                   |
| [**VSS\_COMPONENT\_FLAGS**](/windows/win32/VsWriter/ne-vswriter-vss_component_flags?branch=master)                           | Indicates support for auto-recovery.                                                                                                                               |
| [**VSS\_COMPONENT\_TYPE**](/windows/win32/VsWriter/ne-vswriter-vss_component_type?branch=master)                             | Defines the set of component types.                                                                                                                                |
| [**VSS\_FILE\_RESTORE\_STATUS**](/windows/win32/VsWriter/ne-vswriter-vss_file_restore_status?branch=master)                  | Defines the set of statuses of a file restore operation.                                                                                                           |
| [**VSS\_FILE\_SPEC\_BACKUP\_TYPE**](/windows/win32/Vss/ne-vss-_vss_file_spec_backup_type?branch=master)             | Defines the set of backup operations supported by writers.                                                                                                         |
| [**\_VSS\_HARDWARE\_OPTIONS**](/windows/win32/Vss/ne-vss-_vss_hardware_options?branch=master)                      | Defines shadow copy LUN flags.                                                                                                                                     |
| [**VSS\_MGMT\_OBJECT\_TYPE**](/windows/win32/VsMgmt/ne-vsmgmt-_vss_mgmt_object_type?branch=master)                        | Discriminant for the [**VSS\_MGMT\_OBJECT\_UNION**](/windows/win32/VsMgmt/ns-vsmgmt-__midl___midl_itf_vsmgmt_0000_0000_0001?branch=master) union within the [**VSS\_MGMT\_OBJECT\_PROP**](/windows/win32/VsMgmt/ns-vsmgmt-_vss_mgmt_object_prop?branch=master) structure. |
| [**VSS\_OBJECT\_TYPE**](/windows/win32/Vss/ne-vss-_vss_object_type?branch=master)                                   | Used to identify an object as a shadow copy set, shadow copy, or provider.                                                                                         |
| [**VSS\_PROTECTION\_FAULT**](/windows/win32/VsMgmt/ne-vsmgmt-_vss_protection_fault?branch=master)                         | Defines the set of shadow copy protection faults.                                                                                                                  |
| [**VSS\_PROTECTION\_LEVEL**](/windows/win32/VsMgmt/ne-vsmgmt-_vss_protection_level?branch=master)                         | Defines the set of volume shadow copy protection levels.                                                                                                           |
| [**VSS\_PROVIDER\_CAPABILITIES**](/windows/win32/vss/ne-vss-_vss_provider_capabilities?branch=master)              | Reserved for future use.                                                                                                                                           |
| [**VSS\_PROVIDER\_TYPE**](/windows/win32/Vss/ne-vss-_vss_provider_type?branch=master)                               | Defines the set of provider types.                                                                                                                                 |
| [**VSS\_RECOVERY\_OPTIONS**](/windows/win32/Vss/ne-vss-_vss_recovery_options?branch=master)                         | Used by a requester to specify how a resynchronization operation is to be performed.                                                                               |
| [**VSS\_RESTORE\_TARGET**](/windows/win32/VsWriter/ne-vswriter-vss_restore_target?branch=master)                             | Defines the set of restore targets.                                                                                                                                |
| [**VSS\_RESTORE\_TYPE**](/windows/win32/Vss/ne-vss-_vss_restore_type?branch=master)                                 | Defines the set of restore operation to be performed.                                                                                                              |
| [**VSS\_RESTOREMETHOD\_ENUM**](/windows/win32/VsWriter/ne-vswriter-vss_restoremethod_enum?branch=master)                     | Defines the set of default file restore methods for a writer.                                                                                                      |
| [**VSS\_ROLLFORWARD\_TYPE**](/windows/win32/Vss/ne-vss-_vss_rollforward_type?branch=master)                         | Used by a requester to indicate the type of roll-forward operation it is about to perform.                                                                         |
| [**VSS\_SNAPSHOT\_COMPATIBILITY**](/windows/win32/Vss/ne-vss-_vss_snapshot_compatibility?branch=master)             | Defines the set of volume control or file I/O operations that can be disabled for a volume that has been shadow copied.                                            |
| [**\_VSS\_SNAPSHOT\_CONTEXT**](/windows/win32/Vss/ne-vss-_vss_snapshot_context?branch=master)                      | Specifies how a shadow copy is to be created, queried, or deleted and the degree of writer involvement.                                                            |
| [**VSS\_SNAPSHOT\_STATE**](/windows/win32/Vss/ne-vss-_vss_snapshot_state?branch=master)                             | Defines the set of states of a shadow copy operation.                                                                                                              |
| [**VSS\_SOURCE\_TYPE**](/windows/win32/VsWriter/ne-vswriter-vss_source_type?branch=master)                                   | Defines the set of types of data that a writer can manage.                                                                                                         |
| [**VSS\_SUBSCRIBE\_MASK**](/windows/win32/VsWriter/ne-vswriter-vss_subscribe_mask?branch=master)                             | Defines the set of events that a writer can receive.                                                                                                               |
| [**VSS\_USAGE\_TYPE**](/windows/win32/VsWriter/ne-vswriter-vss_usage_type?branch=master)                                     | Specifies how the host system uses the data managed by a writer.                                                                                                   |
| [**\_VSS\_VOLUME\_SNAPSHOT\_ATTRIBUTES**](/windows/win32/Vss/ne-vss-_vss_volume_snapshot_attributes?branch=master) | Defines the set of attributes of a shadow copy.                                                                                                                    |
| [**VSS\_WRITER\_STATE**](/windows/win32/Vss/ne-vss-_vss_writer_state?branch=master)                                 | Defines the set of states of the writer.                                                                                                                           |
| [**VSS\_WRITERRESTORE\_ENUM**](/windows/win32/VsWriter/ne-vswriter-vss_writerrestore_enum?branch=master)                     | Defines the set of conditions under which a writer will handle events generated during a restore operation.                                                        |



 

 

 



