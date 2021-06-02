---
description: The following enumerations are defined in the Volume Shadow Copy API.
ms.assetid: f2f09791-b17e-4f54-9d29-83a4189bffc1
title: Volume Shadow Copy API Enumerations
ms.topic: article
ms.date: 05/31/2018
---

# Volume Shadow Copy API Enumerations

The following enumerations are defined in the Volume Shadow Copy API.



| Name                                                                           | Description                                                                                                                                                        |
|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**VSS\_ALTERNATE\_WRITER\_STATE**](/windows/desktop/api/VsWriter/ne-vswriter-vss_alternate_writer_state)            | Defines the set of valid states used to indicate whether a writer has an associated alternate writer.                                                              |
| [**VSS\_APPLICATION\_LEVEL**](/windows/desktop/api/Vss/ne-vss-vss_application_level)                       | Defines the set of valid application levels.                                                                                                                       |
| [**VSS\_BACKUP\_SCHEMA**](/windows/desktop/api/Vss/ne-vss-vss_backup_schema)                               | Defines the set of backup schemas—operations a writer can participate in.                                                                                          |
| [**VSS\_BACKUP\_TYPE**](/windows/desktop/api/Vss/ne-vss-vss_backup_type)                                   | Defines the set of backup types.                                                                                                                                   |
| [**VSS\_COMPONENT\_FLAGS**](/windows/desktop/api/VsWriter/ne-vswriter-vss_component_flags)                           | Indicates support for auto-recovery.                                                                                                                               |
| [**VSS\_COMPONENT\_TYPE**](/windows/desktop/api/VsWriter/ne-vswriter-vss_component_type)                             | Defines the set of component types.                                                                                                                                |
| [**VSS\_FILE\_RESTORE\_STATUS**](/windows/desktop/api/VsWriter/ne-vswriter-vss_file_restore_status)                  | Defines the set of statuses of a file restore operation.                                                                                                           |
| [**VSS\_FILE\_SPEC\_BACKUP\_TYPE**](/windows/desktop/api/Vss/ne-vss-vss_file_spec_backup_type)             | Defines the set of backup operations supported by writers.                                                                                                         |
| [**\_VSS\_HARDWARE\_OPTIONS**](/windows/desktop/api/Vss/ne-vss-vss_hardware_options)                      | Defines shadow copy LUN flags.                                                                                                                                     |
| [**VSS\_MGMT\_OBJECT\_TYPE**](/windows/desktop/api/VsMgmt/ne-vsmgmt-vss_mgmt_object_type)                        | Discriminant for the [**VSS\_MGMT\_OBJECT\_UNION**](/windows/desktop/api/VsMgmt/ns-vsmgmt-__midl___midl_itf_vsmgmt_0000_0000_0001) union within the [**VSS\_MGMT\_OBJECT\_PROP**](/windows/desktop/api/VsMgmt/ns-vsmgmt-vss_mgmt_object_prop) structure. |
| [**VSS\_OBJECT\_TYPE**](/windows/desktop/api/Vss/ne-vss-vss_object_type)                                   | Used to identify an object as a shadow copy set, shadow copy, or provider.                                                                                         |
| [**VSS\_PROTECTION\_FAULT**](/windows/desktop/api/VsMgmt/ne-vsmgmt-vss_protection_fault)                         | Defines the set of shadow copy protection faults.                                                                                                                  |
| [**VSS\_PROTECTION\_LEVEL**](/windows/desktop/api/VsMgmt/ne-vsmgmt-vss_protection_level)                         | Defines the set of volume shadow copy protection levels.                                                                                                           |
| [**VSS\_PROVIDER\_CAPABILITIES**](/windows/desktop/api/vss/ne-vss-vss_provider_capabilities)              | Reserved for future use.                                                                                                                                           |
| [**VSS\_PROVIDER\_TYPE**](/windows/desktop/api/Vss/ne-vss-vss_provider_type)                               | Defines the set of provider types.                                                                                                                                 |
| [**VSS\_RECOVERY\_OPTIONS**](/windows/desktop/api/Vss/ne-vss-vss_recovery_options)                         | Used by a requester to specify how a resynchronization operation is to be performed.                                                                               |
| [**VSS\_RESTORE\_TARGET**](/windows/desktop/api/VsWriter/ne-vswriter-vss_restore_target)                             | Defines the set of restore targets.                                                                                                                                |
| [**VSS\_RESTORE\_TYPE**](/windows/desktop/api/Vss/ne-vss-vss_restore_type)                                 | Defines the set of restore operation to be performed.                                                                                                              |
| [**VSS\_RESTOREMETHOD\_ENUM**](/windows/desktop/api/VsWriter/ne-vswriter-vss_restoremethod_enum)                     | Defines the set of default file restore methods for a writer.                                                                                                      |
| [**VSS\_ROLLFORWARD\_TYPE**](/windows/desktop/api/Vss/ne-vss-vss_rollforward_type)                         | Used by a requester to indicate the type of roll-forward operation it is about to perform.                                                                         |
| [**VSS\_SNAPSHOT\_COMPATIBILITY**](/windows/desktop/api/Vss/ne-vss-vss_snapshot_compatibility)             | Defines the set of volume control or file I/O operations that can be disabled for a volume that has been shadow copied.                                            |
| [**\_VSS\_SNAPSHOT\_CONTEXT**](/windows/desktop/api/Vss/ne-vss-vss_snapshot_context)                      | Specifies how a shadow copy is to be created, queried, or deleted and the degree of writer involvement.                                                            |
| [**VSS\_SNAPSHOT\_STATE**](/windows/desktop/api/Vss/ne-vss-vss_snapshot_state)                             | Defines the set of states of a shadow copy operation.                                                                                                              |
| [**VSS\_SOURCE\_TYPE**](/windows/desktop/api/VsWriter/ne-vswriter-vss_source_type)                                   | Defines the set of types of data that a writer can manage.                                                                                                         |
| [**VSS\_SUBSCRIBE\_MASK**](/windows/desktop/api/VsWriter/ne-vswriter-vss_subscribe_mask)                             | Defines the set of events that a writer can receive.                                                                                                               |
| [**VSS\_USAGE\_TYPE**](/windows/desktop/api/VsWriter/ne-vswriter-vss_usage_type)                                     | Specifies how the host system uses the data managed by a writer.                                                                                                   |
| [**\_VSS\_VOLUME\_SNAPSHOT\_ATTRIBUTES**](/windows/desktop/api/Vss/ne-vss-vss_volume_snapshot_attributes) | Defines the set of attributes of a shadow copy.                                                                                                                    |
| [**VSS\_WRITER\_STATE**](/windows/desktop/api/Vss/ne-vss-vss_writer_state)                                 | Defines the set of states of the writer.                                                                                                                           |
| [**VSS\_WRITERRESTORE\_ENUM**](/windows/desktop/api/VsWriter/ne-vswriter-vss_writerrestore_enum)                     | Defines the set of conditions under which a writer will handle events generated during a restore operation.                                                        |



 

 

 



