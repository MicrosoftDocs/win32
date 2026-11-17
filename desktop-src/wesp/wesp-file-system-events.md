---
title: "WESP file system events"
description: "Windows endpoint security platform API reference for file system events, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- ESP_FS_CREATE_FILE_SECTION_CONFIG
- ESP_FS_CREATE_FILE_SECTION_PARAMETERS
- ESP_FS_QUERY_FILE_INFORMATION_CONFIG
- ESP_FS_QUERY_FILE_INFORMATION_PARAMETERS
- ESP_FS_SET_FILE_INFORMATION_CONFIG
- ESP_FS_SET_FILE_INFORMATION_PARAMETERS
- ESP_FS_SET_FILE_SECURITY_CONFIG
- ESP_FS_SET_FILE_SECURITY_PARAMETERS
- ESP_FS_QUERY_DIRECTORY_INFORMATION_CONFIG
- ESP_FS_QUERY_DIRECTORY_INFORMATION_PARAMETERS
- ESP_FS_FSCTL_FILE_CONFIG
- ESP_FS_FSCTL_FILE_PARAMETERS
- ESP_FS_SET_EA_CONFIG
- ESP_FS_SET_EA_PARAMETERS
- ESP_FS_QUERY_OPEN_FILE_CONFIG
- ESP_FS_QUERY_OPEN_FILE_PARAMETERS
- ESP_FS_QUERY_OPEN_FILE_MODIFY
- ESP_FS_LOCK_FILE_CONFIG
- ESP_FS_LOCK_FILE_PARAMETERS
- ESP_FILE_UNLOCK_TYPE
- ESP_FS_UNLOCK_FILE_CONFIG
- ESP_FS_UNLOCK_FILE_PARAMETERS
---

# File system events

This page contains reference entries in the [Events API family](wesp-api-reference.md#events). Each entry includes its declaration and requirements.

## File sections

### ESP_FS_CREATE_FILE_SECTION_CONFIG

The structure `ESP_FS_CREATE_FILE_SECTION_CONFIG` is used to configure a create file section event.

#### Syntax

```cpp
typedef struct ESP_FS_CREATE_FILE_SECTION_CONFIG
{
    ESP_IO_OPERATION_CONFIG OperationConfig;
    ESP_INTEGER_CONFIG PageProtectionConfig;
    ESP_INTEGER_CONFIG FlagsConfig;
    ESP_INTEGER_CONFIG DesiredReadAlignmentConfig;
} ESP_FS_CREATE_FILE_SECTION_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| OperationConfig | Specifies configuration for the IO operation. |
| PageProtectionConfig | Specifies configuration for the page protection. |
| FlagsConfig | Specifies configuration for the flags. |
| DesiredReadAlignmentConfig | Specifies configuration for the desired read alignment. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_IO_OPERATION_CONFIG`](wesp-event-shared-types.md#esp_io_operation_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_FS_CREATE_FILE_SECTION_PARAMETERS

The structure `ESP_FS_CREATE_FILE_SECTION_PARAMETERS` contains the parameters associated with a create file section event notification.

#### Syntax

```cpp
typedef struct ESP_FS_CREATE_FILE_SECTION_PARAMETERS
{
    ESP_IO_OPERATION Operation;
    UINT32 PageProtection;
    UINT32 Flags;
    UINT32 DesiredReadAlignment;
} ESP_FS_CREATE_FILE_SECTION_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Operation | The IO operation for the event. |
| PageProtection | The page protection type for the section. |
| Flags | The flags for the section. This is the equivalent of the kernel structure "FS_FILTER_SECTION_SYNC_OUTPUT.Flags". |
| DesiredReadAlignment | The optimal size for efficient reads. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_IO_OPERATION`](wesp-event-shared-types.md#esp_io_operation)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## File information queries

### ESP_FS_QUERY_FILE_INFORMATION_CONFIG

The structure `ESP_FS_QUERY_FILE_INFORMATION_CONFIG` is used to configure a query file information event.

#### Syntax

```cpp
typedef struct ESP_FS_QUERY_FILE_INFORMATION_CONFIG
{
    ESP_IO_OPERATION_CONFIG OperationConfig;
    ESP_INTEGER_CONFIG InformationClassConfig;
} ESP_FS_QUERY_FILE_INFORMATION_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| OperationConfig | Specifies configuration for the IO operation. |
| InformationClassConfig | Specifies configuration for the information class being queried. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_IO_OPERATION_CONFIG`](wesp-event-shared-types.md#esp_io_operation_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_FS_QUERY_FILE_INFORMATION_PARAMETERS

The structure `ESP_FS_QUERY_FILE_INFORMATION_PARAMETERS` contains the parameters associated with a query file information event notification.

#### Syntax

```cpp
typedef struct ESP_FS_QUERY_FILE_INFORMATION_PARAMETERS
{
    ESP_IO_OPERATION Operation;
    UINT32 InformationClass;
} ESP_FS_QUERY_FILE_INFORMATION_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Operation | The IO operation for the event. |
| InformationClass | The information class being queried (FILE_INFORMATION_CLASS). |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_IO_OPERATION`](wesp-event-shared-types.md#esp_io_operation)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## File information updates

### ESP_FS_SET_FILE_INFORMATION_CONFIG

The structure `ESP_FS_SET_FILE_INFORMATION_CONFIG` is used to configure a set file information event.

#### Syntax

```cpp
typedef struct ESP_FS_SET_FILE_INFORMATION_CONFIG
{
    ESP_IO_OPERATION_CONFIG OperationConfig;
    ESP_INTEGER_CONFIG InformationClassConfig;
    ESP_FILE_OBJECT_CONFIG ParentOfTargetConfig;
    ESP_BOOL_CONFIG ReplaceIfExistsConfig;
    ESP_BOOL_CONFIG AdvanceOnlyConfig;
    ESP_INTEGER_CONFIG InformationBufferSizeConfig;
    ESP_BINARY_CONFIG InformationBufferConfig;
} ESP_FS_SET_FILE_INFORMATION_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| OperationConfig | Specifies configuration for the IO operation. |
| InformationClassConfig | Specifies configuration for the information class being set. |
| ParentOfTargetConfig | Specifies configuration for the parent of target file object. |
| ReplaceIfExistsConfig | Specifies configuration for the replace if exists field. |
| AdvanceOnlyConfig | Specifies configuration for the advance only field. |
| InformationBufferSizeConfig | Specifies configuration for the information buffer size. |
| InformationBufferConfig | Specifies configuration for the information buffer. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BINARY_CONFIG`](wesp-rule-value-configuration.md#esp_binary_config)
- [`ESP_BOOL_CONFIG`](wesp-rule-value-configuration.md#esp_bool_config)
- [`ESP_FILE_OBJECT_CONFIG`](wesp-file-objects.md#esp_file_object_config)
- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_IO_OPERATION_CONFIG`](wesp-event-shared-types.md#esp_io_operation_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_FS_SET_FILE_INFORMATION_PARAMETERS

The structure `ESP_FS_SET_FILE_INFORMATION_PARAMETERS` contains the parameters associated with a set file information event notification.

#### Syntax

```cpp
typedef struct ESP_FS_SET_FILE_INFORMATION_PARAMETERS
{
    ESP_IO_OPERATION Operation;
    UINT32 InformationClass;
    ESP_FILE_OBJECT_INFO ParentOfTarget;
    BOOL ReplaceIfExists;
    BOOL AdvanceOnly;
    UINT32 InformationBufferSize;
    _Field_size_bytes_(InformationBufferSize) const void* InformationBuffer;
} ESP_FS_SET_FILE_INFORMATION_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Operation | The IO operation for the event. |
| InformationClass | The information class being set (FILE_INFORMATION_CLASS). |
| ParentOfTarget | For rename or link operations. If InfoBuffer->FileName contains a fully qualified file name, or if InfoBuffer->RootDirectory is non-NULL, this member is a file object event object for the parent directory of the file that is the target of the operation. |
| ReplaceIfExists | For rename or link operations. Set to TRUE to specify that a file that already exists with the same name is to be replaced with the given file. Set to FALSE if the rename or link operation should fail if a file with the given name already exists. |
| AdvanceOnly | A flag for end-of-file operations. This determines the use of the "EndOfFile" field in FILE_END_OF_FILE_INFORMATION structure when the information class is FileEndOfFileInformation. If true, a new valid data length for the file will be set from "EndOfFile" only if it increases the current valid data length. If false, a new file size is set for "EndOfFile". |
| InformationBufferSize | Size in bytes of InformationBuffer. |
| InformationBuffer | Buffer for the information being set. By default, the buffer is not supplied. The client must specify to include the information buffer through the "InformationBufferConfig" field in the structure `ESP_FS_SET_FILE_INFORMATION_CONFIG`. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_FILE_OBJECT_INFO`](wesp-file-objects.md#esp_file_object_info)
- [`ESP_IO_OPERATION`](wesp-event-shared-types.md#esp_io_operation)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## File security

### ESP_FS_SET_FILE_SECURITY_CONFIG

The structure `ESP_FS_SET_FILE_SECURITY_CONFIG` is used to configure a set file security event.

#### Syntax

```cpp
typedef struct ESP_FS_SET_FILE_SECURITY_CONFIG
{
    ESP_IO_OPERATION_CONFIG OperationConfig;
    ESP_INTEGER_CONFIG SecurityInformationConfig;
    ESP_SECURITY_DESCRIPTOR_CONFIG SecurityDescriptorConfig;
} ESP_FS_SET_FILE_SECURITY_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| OperationConfig | Specifies configuration for the IO operation. |
| SecurityInformationConfig | Specifies configuration for the security information being set. |
| SecurityDescriptorConfig | Specifies configuration for the security descriptor. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_IO_OPERATION_CONFIG`](wesp-event-shared-types.md#esp_io_operation_config)
- [`ESP_SECURITY_DESCRIPTOR_CONFIG`](wesp-rule-value-configuration.md#esp_security_descriptor_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_FS_SET_FILE_SECURITY_PARAMETERS

The structure `ESP_FS_SET_FILE_SECURITY_PARAMETERS` contains the parameters associated with a set file security event notification.

#### Syntax

```cpp
typedef struct ESP_FS_SET_FILE_SECURITY_PARAMETERS
{
    ESP_IO_OPERATION Operation;
    SECURITY_INFORMATION SecurityInformation;
    _Maybenull_ const SECURITY_DESCRIPTOR* SecurityDescriptor;
} ESP_FS_SET_FILE_SECURITY_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Operation | The IO operation for the event. |
| SecurityInformation | The security information to be set on the file. |
| SecurityDescriptor | Pointer to a security descriptor that contains the values of the security information to be assigned to the file. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_IO_OPERATION`](wesp-event-shared-types.md#esp_io_operation)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Directory information

### ESP_FS_QUERY_DIRECTORY_INFORMATION_CONFIG

The structure `ESP_FS_QUERY_DIRECTORY_INFORMATION_CONFIG` is used to configure a query directory information event.

#### Syntax

```cpp
typedef struct ESP_FS_QUERY_DIRECTORY_INFORMATION_CONFIG
{
    ESP_IO_OPERATION_CONFIG OperationConfig;
    ESP_STRING_CONFIG FileNameMatchConfig;
    ESP_INTEGER_CONFIG InformationClassConfig;
} ESP_FS_QUERY_DIRECTORY_INFORMATION_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| OperationConfig | Specifies configuration for the IO operation. |
| FileNameMatchConfig | Specifies configuration for the file name match. |
| InformationClassConfig | Specifies configuration for the information class being queried. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_IO_OPERATION_CONFIG`](wesp-event-shared-types.md#esp_io_operation_config)
- [`ESP_STRING_CONFIG`](wesp-rule-value-configuration.md#esp_string_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_FS_QUERY_DIRECTORY_INFORMATION_PARAMETERS

The structure `ESP_FS_QUERY_DIRECTORY_INFORMATION_PARAMETERS` contains the parameters associated with a query directory information event notification.

#### Syntax

```cpp
typedef struct ESP_FS_QUERY_DIRECTORY_INFORMATION_PARAMETERS
{
    ESP_IO_OPERATION Operation;
    ESP_UNICODE_STRING FileNameMatch;
    UINT32 InformationClass;
} ESP_FS_QUERY_DIRECTORY_INFORMATION_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Operation | The IO operation for the event. |
| FileNameMatch | The file name pattern to match in the directory (e.g. *.txt). |
| InformationClass | The information class for the directory query (FILE_INFORMATION_CLASS). |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_IO_OPERATION`](wesp-event-shared-types.md#esp_io_operation)
- [`ESP_UNICODE_STRING`](wesp-common-utilities.md#esp_unicode_string)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## File system control

### ESP_FS_FSCTL_FILE_CONFIG

The structure `ESP_FS_FSCTL_FILE_CONFIG` is used to configure a file FSCTL event.

#### Syntax

```cpp
typedef struct ESP_FS_FSCTL_FILE_CONFIG
{
    ESP_IO_OPERATION_CONFIG OperationConfig;
    ESP_INTEGER_CONFIG ControlCodeConfig;
    ESP_INTEGER_CONFIG InputBufferSizeConfig;
    ESP_BINARY_CONFIG InputBufferConfig;
} ESP_FS_FSCTL_FILE_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| OperationConfig | Specifies configuration for the IO operation. |
| ControlCodeConfig | Specifies configuration for the control code. |
| InputBufferSizeConfig | Specifies configuration for the input buffer size. |
| InputBufferConfig | Specifies configuration for the input buffer. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BINARY_CONFIG`](wesp-rule-value-configuration.md#esp_binary_config)
- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_IO_OPERATION_CONFIG`](wesp-event-shared-types.md#esp_io_operation_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_FS_FSCTL_FILE_PARAMETERS

The structure `ESP_FS_FSCTL_FILE_PARAMETERS` contains the parameters associated with a file FSCTL event notification.

#### Syntax

```cpp
typedef struct ESP_FS_FSCTL_FILE_PARAMETERS
{
    ESP_IO_OPERATION Operation;
    UINT32 ControlCode;
    UINT32 InputBufferSize;
    _Field_size_bytes_(InputBufferSize) const void* InputBuffer;
} ESP_FS_FSCTL_FILE_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Operation | The IO operation for the event. |
| ControlCode | The control code. |
| InputBufferSize | The size in bytes of the input buffer. |
| InputBuffer | The input buffer. By default, the input buffer is not supplied. The client must specify to include the input buffer through the "InputBufferConfig" field in the structure `ESP_FS_FSCTL_FILE_CONFIG`. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_IO_OPERATION`](wesp-event-shared-types.md#esp_io_operation)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Extended attributes

### ESP_FS_SET_EA_CONFIG

The structure `ESP_FS_SET_EA_CONFIG` is used to configure a set EA event.

#### Syntax

```cpp
typedef struct ESP_FS_SET_EA_CONFIG
{
    ESP_IO_OPERATION_CONFIG OperationConfig;
    ESP_EA_LIST_CONFIG ExtendedAttributesConfig;
} ESP_FS_SET_EA_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| OperationConfig | Specifies configuration for the IO operation. |
| ExtendedAttributesConfig | Specifies configuration for the extended attributes being set. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EA_LIST_CONFIG`](wesp-rule-value-configuration.md#esp_ea_list_config)
- [`ESP_IO_OPERATION_CONFIG`](wesp-event-shared-types.md#esp_io_operation_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_FS_SET_EA_PARAMETERS

The structure `ESP_FS_SET_EA_PARAMETERS` contains the parameters associated with a set EA event notification.

#### Syntax

```cpp
typedef struct ESP_FS_SET_EA_PARAMETERS
{
    ESP_IO_OPERATION Operation;
    ESP_EA_LIST ExtendedAttributes;
} ESP_FS_SET_EA_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Operation | The IO operation for the event. |
| ExtendedAttributes | The list of extended attributes being set. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EA_LIST`](wesp-common-value-types.md#esp_ea_list)
- [`ESP_IO_OPERATION`](wesp-event-shared-types.md#esp_io_operation)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Query open

### ESP_FS_QUERY_OPEN_FILE_CONFIG

The structure `ESP_FS_QUERY_OPEN_FILE_CONFIG` is used to configure a query open file event.

#### Syntax

```cpp
typedef struct ESP_FS_QUERY_OPEN_FILE_CONFIG
{
    ESP_IO_OPERATION_CONFIG OperationConfig;
    ESP_INTEGER_CONFIG InformationClassConfig;
    ESP_BOOL_CONFIG IsBindLinkConfig;
} ESP_FS_QUERY_OPEN_FILE_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| OperationConfig | Specifies configuration for the IO operation. |
| InformationClassConfig | Specifies configuration for the information class. |
| IsBindLinkConfig | Specifies configuration for the IsBindLink field. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BOOL_CONFIG`](wesp-rule-value-configuration.md#esp_bool_config)
- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_IO_OPERATION_CONFIG`](wesp-event-shared-types.md#esp_io_operation_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_FS_QUERY_OPEN_FILE_PARAMETERS

The structure `ESP_FS_QUERY_OPEN_FILE_PARAMETERS` contains the parameters associated with a query open file event notification.

#### Syntax

```cpp
typedef struct ESP_FS_QUERY_OPEN_FILE_PARAMETERS
{
    ESP_IO_OPERATION Operation;
    UINT32 InformationClass;
    BOOL IsBindLink;
} ESP_FS_QUERY_OPEN_FILE_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Operation | The IO operation for the event. |
| InformationClass | The file information class (FILE_INFORMATION_CLASS). |
| IsBindLink | Whether the query open event is due to a bind link creation. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_IO_OPERATION`](wesp-event-shared-types.md#esp_io_operation)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_FS_QUERY_OPEN_FILE_MODIFY

The structure `ESP_FS_QUERY_OPEN_FILE_MODIFY` is used to modify event data for the query file open event.

#### Syntax

```cpp
typedef struct ESP_FS_QUERY_OPEN_FILE_MODIFY
{
    BOOL ShouldVetoBinding;
} ESP_FS_QUERY_OPEN_FILE_MODIFY;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ShouldVetoBinding | Specifies a boolean indicating whether to veto the bind link creation. The client can set this to true to block the creation of a bind link. If the query open is not for a bind link creation, this field is ignored. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

## File locking

### ESP_FS_LOCK_FILE_CONFIG

The structure `ESP_FS_LOCK_FILE_CONFIG` is used to configure a lock file event.

#### Syntax

```cpp
typedef struct ESP_FS_LOCK_FILE_CONFIG
{
    ESP_IO_OPERATION_CONFIG OperationConfig;
    ESP_BYTE_RANGE_CONFIG LockRangeConfig;
    ESP_INTEGER_CONFIG KeyConfig;
    ESP_PROCESS_CONFIG ProcessConfig;
    ESP_BOOL_CONFIG FailImmediatelyConfig;
    ESP_BOOL_CONFIG ExclusiveLockConfig;
} ESP_FS_LOCK_FILE_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| OperationConfig | Specifies configuration for the IO operation. |
| LockRangeConfig | Specifies configuration for the lock range. |
| KeyConfig | Specifies configuration for the key. |
| ProcessConfig | Specifies configuration for the process. |
| FailImmediatelyConfig | Specifies configuration for the "FailImmediately" field. |
| ExclusiveLockConfig | Specifies configuration for the "ExclusiveLock" field. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BOOL_CONFIG`](wesp-rule-value-configuration.md#esp_bool_config)
- [`ESP_BYTE_RANGE_CONFIG`](wesp-rule-value-configuration.md#esp_byte_range_config)
- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_IO_OPERATION_CONFIG`](wesp-event-shared-types.md#esp_io_operation_config)
- [`ESP_PROCESS_CONFIG`](wesp-execution-objects.md#esp_process_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_FS_LOCK_FILE_PARAMETERS

The structure `ESP_FS_LOCK_FILE_PARAMETERS` contains the parameters associated with a lock file event notification.

#### Syntax

```cpp
typedef struct ESP_FS_LOCK_FILE_PARAMETERS
{
    ESP_IO_OPERATION Operation;
    ESP_BYTE_RANGE LockRange;
    UINT32 Key;
    ESP_PROCESS_INFO Process;
    BOOL FailImmediately;
    BOOL ExclusiveLock;
} ESP_FS_LOCK_FILE_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Operation | The IO operation for the event. |
| LockRange | The byte range within the file to lock. |
| Key | Key value to be assigned to the byte range lock. |
| Process | The process that requested the byte range lock. |
| FailImmediately | Specifies whether the lock request should fail if the lock cannot be granted immediately. |
| ExclusiveLock | Specifies whether an exclusive lock is requested. If false, a shared lock is requested. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BYTE_RANGE`](wesp-common-value-types.md#esp_byte_range)
- [`ESP_IO_OPERATION`](wesp-event-shared-types.md#esp_io_operation)
- [`ESP_PROCESS_INFO`](wesp-execution-objects.md#esp_process_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## File unlocking

### ESP_FILE_UNLOCK_TYPE

The enum `ESP_FILE_UNLOCK_TYPE` defines a file unlock type.

#### Syntax

```cpp
typedef enum ESP_FILE_UNLOCK_TYPE
{
    ESP_FILE_UNLOCK_TYPE_NONE = 0,
    ESP_FILE_UNLOCK_TYPE_BY_RANGE,
    ESP_FILE_UNLOCK_TYPE_BY_KEY,
    ESP_FILE_UNLOCK_TYPE_ALL
} ESP_FILE_UNLOCK_TYPE;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_FILE_UNLOCK_TYPE_BY_RANGE` | Unlock a specific byte range on the file. |
| `ESP_FILE_UNLOCK_TYPE_BY_KEY` | Unlock all byte ranges associated with the specified key. |
| `ESP_FILE_UNLOCK_TYPE_ALL` | Unlock all byte ranges on the file. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_FS_UNLOCK_FILE_CONFIG

The structure `ESP_FS_UNLOCK_FILE_CONFIG` is used to configure an unlock file event.

#### Syntax

```cpp
typedef struct ESP_FS_UNLOCK_FILE_CONFIG
{
    ESP_IO_OPERATION_CONFIG OperationConfig;
    ESP_INTEGER_CONFIG UnlockTypeConfig;
    ESP_BYTE_RANGE_CONFIG LockRangeConfig;
    ESP_INTEGER_CONFIG KeyConfig;
    ESP_PROCESS_CONFIG ProcessConfig;
} ESP_FS_UNLOCK_FILE_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| OperationConfig | Specifies configuration for the IO operation. |
| UnlockTypeConfig | Specifies configuration for the unlock type. |
| LockRangeConfig | Specifies configuration for the lock range. |
| KeyConfig | Specifies configuration for the key. |
| ProcessConfig | Specifies configuration for the process. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BYTE_RANGE_CONFIG`](wesp-rule-value-configuration.md#esp_byte_range_config)
- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_IO_OPERATION_CONFIG`](wesp-event-shared-types.md#esp_io_operation_config)
- [`ESP_PROCESS_CONFIG`](wesp-execution-objects.md#esp_process_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_FS_UNLOCK_FILE_PARAMETERS

The structure `ESP_FS_UNLOCK_FILE_PARAMETERS` contains the parameters associated with an unlock file event notification.

#### Syntax

```cpp
typedef struct ESP_FS_UNLOCK_FILE_PARAMETERS
{
    ESP_IO_OPERATION Operation;
    ESP_FILE_UNLOCK_TYPE UnlockType;
    ESP_BYTE_RANGE LockRange;
    UINT32 Key;
    ESP_PROCESS_INFO Process;
} ESP_FS_UNLOCK_FILE_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Operation | The IO operation for the event. |
| UnlockType | The unlock type. The supported values are:<br>By Range<br>By Key<br>All |
| LockRange | The byte range within the file to unlock. |
| Key | The byte range lock key. |
| Process | The process that owns the lock. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BYTE_RANGE`](wesp-common-value-types.md#esp_byte_range)
- [`ESP_FILE_UNLOCK_TYPE`](wesp-file-system-events.md#esp_file_unlock_type)
- [`ESP_IO_OPERATION`](wesp-event-shared-types.md#esp_io_operation)
- [`ESP_PROCESS_INFO`](wesp-execution-objects.md#esp_process_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
