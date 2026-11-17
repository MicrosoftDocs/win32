---
title: "WESP shared event types"
description: "Windows endpoint security platform API reference for shared event types, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- ESP_EVENT_TYPE
- ESP_IO_OPERATION_FLAGS
- ESP_IO_OPERATION
- ESP_IO_OPERATION_CONFIG
- ESP_ECP_DESCRIPTOR
- ESP_ECP_LIST
- ESP_REMOTE_CLIENT
- ESP_ACCESS_STATE
---

# Shared event types

This page contains reference entries in the [Events API family](wesp-api-reference.md#events). Each entry includes its declaration and requirements.

## Shared enumerations

### ESP_EVENT_TYPE

Identifies the system event associated with a WESP rule or notification.

#### Syntax

```cpp
typedef enum ESP_EVENT_TYPE
{
    ESP_EVENT_TYPE_NONE = 0,

    // Thread events: 1-999.
    ESP_EVENT_TYPE_THREAD_CREATE,
    ESP_EVENT_TYPE_THREAD_START,
    ESP_EVENT_TYPE_THREAD_TERMINATE,

    // Process events: 1000-1999.
    ESP_EVENT_TYPE_PROCESS_CREATE = 1000,
    ESP_EVENT_TYPE_PROCESS_TERMINATE,
    ESP_EVENT_TYPE_PROCESS_LOAD_IMAGE,

    // File object events: 2000-2999.
    ESP_EVENT_TYPE_FO_CREATE = 2000,
    ESP_EVENT_TYPE_FO_OPEN,
    ESP_EVENT_TYPE_FO_READ,
    ESP_EVENT_TYPE_FO_WRITE,
    ESP_EVENT_TYPE_FO_CLEANUP,

    // Filesystem events: 3000-3999.
    ESP_EVENT_TYPE_FS_CREATE_FILE_SECTION = 3000,
    ESP_EVENT_TYPE_FS_QUERY_FILE_INFORMATION,
    ESP_EVENT_TYPE_FS_SET_FILE_INFORMATION,
    ESP_EVENT_TYPE_FS_SET_FILE_SECURITY,
    ESP_EVENT_TYPE_FS_QUERY_DIRECTORY_INFORMATION,
    ESP_EVENT_TYPE_FS_FSCTL_FILE,
    ESP_EVENT_TYPE_FS_SET_EA,
    ESP_EVENT_TYPE_FS_QUERY_OPEN_FILE,
    ESP_EVENT_TYPE_FS_LOCK_FILE,
    ESP_EVENT_TYPE_FS_UNLOCK_FILE,
    ESP_EVENT_TYPE_KTM_TRANSACTION_COMMIT,
    ESP_EVENT_TYPE_KTM_TRANSACTION_ROLLBACK,

    // Volume events: 4000-4999.
    ESP_EVENT_TYPE_VOLUME_MOUNT = 4000,
    ESP_EVENT_TYPE_VOLUME_DISMOUNT,
    ESP_EVENT_TYPE_VOLUME_FSCTL,

    // Named pipe events: 5000-5999.
    ESP_EVENT_TYPE_PIPE_CREATE = 5000,

    // Mailslot events: 6000-6999.
    ESP_EVENT_TYPE_MAILSLOT_CREATE = 6000,

    // Registry events: 7000-7999.
    ESP_EVENT_TYPE_REG_CREATE_KEY = 7000,
    ESP_EVENT_TYPE_REG_OPEN_KEY,
    ESP_EVENT_TYPE_REG_DELETE_KEY,
    ESP_EVENT_TYPE_REG_SET_VALUE_KEY,
    ESP_EVENT_TYPE_REG_DELETE_VALUE_KEY,
    ESP_EVENT_TYPE_REG_RENAME_KEY,
    ESP_EVENT_TYPE_REG_REPLACE_KEY,
    ESP_EVENT_TYPE_REG_RESTORE_KEY,
    ESP_EVENT_TYPE_REG_SET_KEY_SECURITY,
    ESP_EVENT_TYPE_REG_QUERY_KEY,
    ESP_EVENT_TYPE_REG_QUERY_VALUE_KEY,
    ESP_EVENT_TYPE_REG_SAVE_KEY,
    ESP_EVENT_TYPE_REG_LOAD_KEY,
    ESP_EVENT_TYPE_REG_ENUM_KEY,
    ESP_EVENT_TYPE_REG_ENUM_VALUE_KEY,

    // OB events: 8000-8999.
    ESP_EVENT_TYPE_OB_CREATE_HANDLE = 8000,
    ESP_EVENT_TYPE_OB_DUPLICATE_HANDLE,

    // Boot events: 9000-9999.
    ESP_EVENT_TYPE_BOOT_LOAD_DRIVER = 9000
} ESP_EVENT_TYPE;
```

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_IO_OPERATION_FLAGS

The enum `ESP_IO_OPERATION_FLAGS` specifies flags for an IO operation.

#### Syntax

```cpp
typedef enum ESP_IO_OPERATION_FLAGS
{
    ESP_IO_OPERATION_FLAGS_NONE    = 0x00000000,
    ESP_IO_OPERATION_FLAGS_IRP     = 0x00000001,
    ESP_IO_OPERATION_FLAGS_FAST_IO = 0x00000002
} ESP_IO_OPERATION_FLAGS;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_IO_OPERATION_FLAGS_IRP` | The IO operation is for an IRP operation. |
| `ESP_IO_OPERATION_FLAGS_FAST_IO` | The IO operation is for a fast IO operation. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Shared structures

### ESP_IO_OPERATION

The structure `ESP_IO_OPERATION` represents an IO operation.

#### Syntax

```cpp
typedef struct ESP_IO_OPERATION
{
    ESP_IO_OPERATION_FLAGS IoFlags;
    _Maybenull_ const ESP_THREAD_INFO* RequestorThread;
    _Maybenull_ const ESP_PROCESS_INFO* RequestorProcess;
    _Maybenull_ const ESP_FILE_OBJECT_INFO* TargetFileObject;
    UINT32 IrpFlags;
    UINT8 OperationFlags;
    BOOL RequestorModeIsKernelMode;
    UINT32 IoPriorityHint;
} ESP_IO_OPERATION;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| IoFlags | Specifies flags for the IO operation. |
| RequestorThread | Specifies information about the IRP's requestor thread. This field may be null if no requestor thread configuration is set for the IRP |
| RequestorProcess | Specifies information about the IRP's requestor thread. This field may be null if no requestor process configuration is set for the IRP |
| TargetFileObject | Specifies information about the file object that is the target of the IO operation. This is the equivalent of "FLT_IO_PARAMETER_BLOCK::TargetFileObject". This field may be null if no target file object configuration is set for the IRP. |
| IrpFlags | Specifies the IRP's flags. This is the equivalent of FLT_IO_PARAMETER_BLOCK::IrpFlags. |
| OperationFlags | Specifies the operation flags. This is the equivalent of FLT_IO_PARAMETER_BLOCK::OperationFlags. |
| RequestorModeIsKernelMode | Indicates whether the IRP originated from kernel mode. |
| IoPriorityHint | Specifies the IO priority of the IRP (i.e. IO_PRIORITY_HINT enum). |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_FILE_OBJECT_INFO`](wesp-file-objects.md#esp_file_object_info)
- [`ESP_IO_OPERATION_FLAGS`](wesp-event-shared-types.md#esp_io_operation_flags)
- [`ESP_PROCESS_INFO`](wesp-execution-objects.md#esp_process_info)
- [`ESP_THREAD_INFO`](wesp-execution-objects.md#esp_thread_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_IO_OPERATION_CONFIG

The structure `ESP_IO_OPERATION_CONFIG` is used to configure an IO operation value.

#### Syntax

```cpp
typedef struct ESP_IO_OPERATION_CONFIG
{
    ESP_INTEGER_CONFIG IoFlagsConfig;
    ESP_THREAD_CONFIG RequestorThreadConfig;
    ESP_PROCESS_CONFIG RequestorProcessConfig;
    ESP_FILE_OBJECT_CONFIG TargetFileObjectConfig;
    ESP_INTEGER_CONFIG IrpFlagsConfig;
    ESP_INTEGER_CONFIG OperationFlagsConfig;
    ESP_BOOL_CONFIG RequestorModeIsKernelModeConfig;
    ESP_INTEGER_CONFIG IoPriorityHintConfig;
} ESP_IO_OPERATION_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| IoFlagsConfig | Specifies configuration for the IO flags. |
| RequestorThreadConfig | Specifies configuration for the requestor thread. |
| RequestorProcessConfig | Specifies configuration for the requestor process. |
| TargetFileObjectConfig | Specifies configuration for the target file object. |
| IrpFlagsConfig | Specifies configuration for the IRP flags. |
| OperationFlagsConfig | Specifies configuration for the operation flags. |
| RequestorModeIsKernelModeConfig | Specifies configuration for the IRP field RequestorModeIsKernelMode . |
| IoPriorityHintConfig | Specifies configuration for the IO priority hint. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BOOL_CONFIG`](wesp-rule-value-configuration.md#esp_bool_config)
- [`ESP_FILE_OBJECT_CONFIG`](wesp-file-objects.md#esp_file_object_config)
- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_PROCESS_CONFIG`](wesp-execution-objects.md#esp_process_config)
- [`ESP_THREAD_CONFIG`](wesp-execution-objects.md#esp_thread_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_ECP_DESCRIPTOR

The structure `ESP_ECP_DESCRIPTOR` describes an extra create parameter.

#### Syntax

```cpp
typedef struct ESP_ECP_DESCRIPTOR
{
    GUID Ecp;
    BOOL IsFromUserMode;
    UINT32 EcpContextSize;
    _Field_size_bytes_(EcpContextSize) const void* EcpContext;
} ESP_ECP_DESCRIPTOR;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Ecp | Specifies the ECP guid. |
| IsFromUserMode | Specifies a boolean indicating whether the ECP originated from user mode. |
| EcpContextSize | Specifies the size in bytes of the ECP context. |
| EcpContext | Specifies the ECP's context. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_ECP_LIST

The structure `ESP_ECP_LIST` is used to describe a list of extra create parameters.

#### Syntax

```cpp
typedef struct ESP_ECP_LIST
{
    UINT32 DescriptorsCount;
    _Field_size_(DescriptorsCount) const ESP_ECP_DESCRIPTOR* Descriptors;
} ESP_ECP_LIST;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| DescriptorsCount | Specifies the number of elements in the descriptors array. |
| Descriptors | Specifies an array of `ESP_ECP_DESCRIPTOR` structures. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_ECP_DESCRIPTOR`](wesp-event-shared-types.md#esp_ecp_descriptor)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_REMOTE_CLIENT

The structure `ESP_REMOTE_CLIENT` is used to represent a remote client. This is used for the create file event to represent when a file is being opened by a remote client.

#### Syntax

```cpp
typedef struct ESP_REMOTE_CLIENT
{
    BOOL IsPresent;
    ESP_UNICODE_STRING ShareName;
    _Maybenull_ const SID* UserSid;
    ESP_NETWORK_IP_ADDRESS IpAddress;
    UINT16 Port;
} ESP_REMOTE_CLIENT;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| IsPresent | Specifies whether a remote client is present. |
| ShareName | Specifies the share name for the server that contains the file to be opened. |
| UserSid | Specifies the user sid of the remote client. |
| IpAddress | Specifies the IP address of the remote client. |
| Port | Specifies the port of the remote client. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_NETWORK_IP_ADDRESS`](wesp-common-value-types.md#esp_network_ip_address)
- [`ESP_UNICODE_STRING`](wesp-common-utilities.md#esp_unicode_string)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_ACCESS_STATE

The structure `ESP_ACCESS_STATE` is used to represent the state of an access in progress.

#### Syntax

```cpp
typedef struct ESP_ACCESS_STATE
{
    UINT32 Flags;
    ACCESS_MASK RemainingDesiredAccess;
    ACCESS_MASK PreviouslyGrantedAccess;
    ACCESS_MASK OriginalGrantedAccess;
    _Maybenull_ const SECURITY_DESCRIPTOR* SecurityDescriptor;
    _Maybenull_ const ESP_TOKEN_INFO* SubjectTokenInfo;
} ESP_ACCESS_STATE;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Flags | Specifies flags for the access. This is the equivalent of the "Flags" field in the kernel structure ACCESS_STATE. |
| RemainingDesiredAccess | Specifies an access mask that describes the access rights that have not yet been granted. |
| PreviouslyGrantedAccess | Specifies an access mask that describes the access rights that have already been granted. |
| OriginalGrantedAccess | Specifies an access mask that describes the original access right that were requested. |
| SecurityDescriptor | Specifies the security descriptor for the object this access relates to. This is the equivalent of the "SecurityDescriptor" field in the kernel structure ACCESS_STATE. |
| SubjectTokenInfo | Specifies the subject token for this access. This is the equivalent of the "SubjectSecurityContext" field in the kernel structure ACCESS_STATE. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_TOKEN_INFO`](wesp-execution-objects.md#esp_token_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
