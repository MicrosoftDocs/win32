---
Description: 'The following enumerations are defined in the Volume Shadow Copy API.'
ms.assetid: 'f2f09791-b17e-4f54-9d29-83a4189bffc1'
title: Volume Shadow Copy API Enumerations
---

# Volume Shadow Copy API Enumerations

The following enumerations are defined in the Volume Shadow Copy API.



| Name                                                                           | Description                                                                                                                                                        |
|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**VSS\_ALTERNATE\_WRITER\_STATE**](vss-alternate-writer-state.md)            | Defines the set of valid states used to indicate whether a writer has an associated alternate writer.                                                              |
| [**VSS\_APPLICATION\_LEVEL**](vss-application-level.md)                       | Defines the set of valid application levels.                                                                                                                       |
| [**VSS\_BACKUP\_SCHEMA**](vss-backup-schema.md)                               | Defines the set of backup schemas—operations a writer can participate in.                                                                                          |
| [**VSS\_BACKUP\_TYPE**](vss-backup-type.md)                                   | Defines the set of backup types.                                                                                                                                   |
| [**VSS\_COMPONENT\_FLAGS**](vss-component-flags.md)                           | Indicates support for auto-recovery.                                                                                                                               |
| [**VSS\_COMPONENT\_TYPE**](vss-component-type.md)                             | Defines the set of component types.                                                                                                                                |
| [**VSS\_FILE\_RESTORE\_STATUS**](vss-file-restore-status.md)                  | Defines the set of statuses of a file restore operation.                                                                                                           |
| [**VSS\_FILE\_SPEC\_BACKUP\_TYPE**](vss-file-spec-backup-type.md)             | Defines the set of backup operations supported by writers.                                                                                                         |
| [**\_VSS\_HARDWARE\_OPTIONS**](-vss-hardware-options.md)                      | Defines shadow copy LUN flags.                                                                                                                                     |
| [**VSS\_MGMT\_OBJECT\_TYPE**](vss-mgmt-object-type.md)                        | Discriminant for the [**VSS\_MGMT\_OBJECT\_UNION**](vss-mgmt-object-union.md) union within the [**VSS\_MGMT\_OBJECT\_PROP**](vss-mgmt-object-prop.md) structure. |
| [**VSS\_OBJECT\_TYPE**](vss-object-type.md)                                   | Used to identify an object as a shadow copy set, shadow copy, or provider.                                                                                         |
| [**VSS\_PROTECTION\_FAULT**](vss-protection-fault.md)                         | Defines the set of shadow copy protection faults.                                                                                                                  |
| [**VSS\_PROTECTION\_LEVEL**](vss-protection-level.md)                         | Defines the set of volume shadow copy protection levels.                                                                                                           |
| [**VSS\_PROVIDER\_CAPABILITIES**](-vss-provider-capabilities.md)              | Reserved for future use.                                                                                                                                           |
| [**VSS\_PROVIDER\_TYPE**](vss-provider-type.md)                               | Defines the set of provider types.                                                                                                                                 |
| [**VSS\_RECOVERY\_OPTIONS**](vss-recovery-options.md)                         | Used by a requester to specify how a resynchronization operation is to be performed.                                                                               |
| [**VSS\_RESTORE\_TARGET**](vss-restore-target.md)                             | Defines the set of restore targets.                                                                                                                                |
| [**VSS\_RESTORE\_TYPE**](vss-restore-type.md)                                 | Defines the set of restore operation to be performed.                                                                                                              |
| [**VSS\_RESTOREMETHOD\_ENUM**](vss-restoremethod-enum.md)                     | Defines the set of default file restore methods for a writer.                                                                                                      |
| [**VSS\_ROLLFORWARD\_TYPE**](vss-rollforward-type.md)                         | Used by a requester to indicate the type of roll-forward operation it is about to perform.                                                                         |
| [**VSS\_SNAPSHOT\_COMPATIBILITY**](vss-snapshot-compatibility.md)             | Defines the set of volume control or file I/O operations that can be disabled for a volume that has been shadow copied.                                            |
| [**\_VSS\_SNAPSHOT\_CONTEXT**](-vss-snapshot-context.md)                      | Specifies how a shadow copy is to be created, queried, or deleted and the degree of writer involvement.                                                            |
| [**VSS\_SNAPSHOT\_STATE**](vss-snapshot-state.md)                             | Defines the set of states of a shadow copy operation.                                                                                                              |
| [**VSS\_SOURCE\_TYPE**](vss-source-type.md)                                   | Defines the set of types of data that a writer can manage.                                                                                                         |
| [**VSS\_SUBSCRIBE\_MASK**](vss-subscribe-mask.md)                             | Defines the set of events that a writer can receive.                                                                                                               |
| [**VSS\_USAGE\_TYPE**](vss-usage-type.md)                                     | Specifies how the host system uses the data managed by a writer.                                                                                                   |
| [**\_VSS\_VOLUME\_SNAPSHOT\_ATTRIBUTES**](-vss-volume-snapshot-attributes.md) | Defines the set of attributes of a shadow copy.                                                                                                                    |
| [**VSS\_WRITER\_STATE**](vss-writer-state.md)                                 | Defines the set of states of the writer.                                                                                                                           |
| [**VSS\_WRITERRESTORE\_ENUM**](vss-writerrestore-enum.md)                     | Defines the set of conditions under which a writer will handle events generated during a restore operation.                                                        |



 

 

 



