---
title: "WESP file object events"
description: "Windows endpoint security platform API reference for file object events, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- ESP_FO_CREATE_CONFIG
- ESP_FO_CREATE_PARAMETERS
- ESP_FO_CREATE_MODIFY
- ESP_FO_OPEN_CONFIG
- ESP_FO_OPEN_PARAMETERS
- ESP_FO_READ_CONFIG
- ESP_FO_READ_PARAMETERS
- ESP_FO_WRITE_CONFIG
- ESP_FO_WRITE_PARAMETERS
- ESP_FO_CLEANUP_CONFIG
- ESP_FO_CLEANUP_PARAMETERS
---

# File object events

This page contains reference entries in the [Events API family](wesp-api-reference.md#events). Each entry includes its declaration and requirements.

## File object creation

### ESP_FO_CREATE_CONFIG

The structure `ESP_FO_CREATE_CONFIG` is used to configure a file object create event.

#### Syntax

```cpp
typedef struct ESP_FO_CREATE_CONFIG
{
    ESP_IO_OPERATION_CONFIG OperationConfig;
    ESP_INTEGER_CONFIG DesiredAccessConfig;
    ESP_INTEGER_CONFIG CreateOptionsConfig;
    ESP_INTEGER_CONFIG CreateDispositionConfig;
    ESP_INTEGER_CONFIG FileAttributesConfig;
    ESP_INTEGER_CONFIG ShareAccessConfig;
    ESP_INTEGER_CONFIG AllocationSizeConfig;
    ESP_ECP_LIST_CONFIG EcpListConfig;
    ESP_REMOTE_CLIENT_CONFIG RemoteClientConfig;
    ESP_ACCESS_STATE_CONFIG AccessStateConfig;
    ESP_INTEGER_CONFIG CreateOutcomeConfig;
} ESP_FO_CREATE_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| OperationConfig | Specifies configuration for the IO operation. |
| DesiredAccessConfig | Specifies configuration for the desired access. |
| CreateOptionsConfig | Specifies configuration for the create options. |
| CreateDispositionConfig | Specifies configuration for the create disposition. |
| FileAttributesConfig | Specifies configuration for the file attributes. |
| ShareAccessConfig | Specifies configuration for the share access. |
| AllocationSizeConfig | Specifies configuration for the allocation size. |
| EcpListConfig | Specifies configuration for the ECP list. |
| RemoteClientConfig | Specifies configuration for the remote client. |
| AccessStateConfig | Specifies configuration for the access state. |
| CreateOutcomeConfig | Specifies configuration for the create outcome. This field can only be set for the NotifyOnCompletion action. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_ACCESS_STATE_CONFIG`](wesp-rule-value-configuration.md#esp_access_state_config)
- [`ESP_ECP_LIST_CONFIG`](wesp-rule-value-configuration.md#esp_ecp_list_config)
- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_IO_OPERATION_CONFIG`](wesp-event-shared-types.md#esp_io_operation_config)
- [`ESP_REMOTE_CLIENT_CONFIG`](wesp-rule-value-configuration.md#esp_remote_client_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_FO_CREATE_PARAMETERS

The structure `ESP_FO_CREATE_PARAMETERS` contains the parameters associated with a file object create event notification.

#### Syntax

```cpp
typedef struct ESP_FO_CREATE_PARAMETERS
{
    ESP_IO_OPERATION Operation;
    ACCESS_MASK DesiredAccess;
    UINT32 CreateOptions;
    UINT32 CreateDisposition;
    UINT16 FileAttributes;
    UINT16 ShareAccess;
    UINT64 AllocationSize;
    ESP_ECP_LIST EcpList;
    ESP_REMOTE_CLIENT RemoteClient;
    ESP_ACCESS_STATE AccessState;
    BOOL CreateOutcomeIsPresent;
    UINT32 CreateOutcome;
} ESP_FO_CREATE_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Operation | The IO operation for the event. |
| DesiredAccess | The ACCESS_MASK requested for the file object. |
| CreateOptions | The create options. This corresponds to the "CreateOptions" parameter of FltCreateFile. |
| CreateDisposition | The create disposition. This corresponds to the "CreateDisposition" parameter of FltCreateFile. |
| FileAttributes | Bitmask of attributes to be applied when creating the file object. |
| ShareAccess | Bitmask of share access rights requested for the file object. |
| AllocationSize | Specifies the initial allocation size in bytes for the file. |
| EcpList | The list of ECPs. By default, ECPs are not included in the structure. The client must specify which ECP's to include in the notification through the "EcpListConfig" field in the structure `ESP_FO_CREATE_CONFIG`. |
| RemoteClient | A remote client. This structure is only set if the file is being opened on behalf of a remote client. |
| AccessState | An `ESP_ACCESS_STATE` structure which describes the state of the access in progress. |
| CreateOutcomeIsPresent | Whether the create outcome field is present. The create outcome parameter is only present for the NotifyOnCompletion action. |
| CreateOutcome | The outcome of the create. This parameter is only supplied for the NotifyOnCompletion action. One of the following values is supplied:<br>FILE_SUPERSEDED<br>FILE_OPENED<br>FILE_CREATED<br>FILE_OVERWRITTEN<br>FILE_EXISTS<br>FILE_DOES_NOT_EXIST |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_ACCESS_STATE`](wesp-event-shared-types.md#esp_access_state)
- [`ESP_ECP_LIST`](wesp-event-shared-types.md#esp_ecp_list)
- [`ESP_IO_OPERATION`](wesp-event-shared-types.md#esp_io_operation)
- [`ESP_REMOTE_CLIENT`](wesp-event-shared-types.md#esp_remote_client)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_FO_CREATE_MODIFY

The structure `ESP_FO_CREATE_MODIFY` is used to modify event data for the file object create event.

#### Syntax

```cpp
typedef struct ESP_FO_CREATE_MODIFY
{
    ESP_ACCESS_MASK_MODIFICATION_LIST DesiredAccess;
} ESP_FO_CREATE_MODIFY;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| DesiredAccess | The modifications to make to the DesiredAccess field of a file object create event. This can be used to set or clear the access mask. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_ACCESS_MASK_MODIFICATION_LIST`](wesp-rule-event-modification.md#esp_access_mask_modification_list)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## File object open

### ESP_FO_OPEN_CONFIG

The structure `ESP_FO_OPEN_CONFIG` is used to configure a file object open event.

#### Syntax

```cpp
typedef struct ESP_FO_OPEN_CONFIG
{
    ESP_IO_OPERATION_CONFIG OperationConfig;
    ESP_INTEGER_CONFIG DesiredAccessConfig;
    ESP_INTEGER_CONFIG CreateOptionsConfig;
    ESP_INTEGER_CONFIG CreateDispositionConfig;
    ESP_INTEGER_CONFIG FileAttributesConfig;
    ESP_INTEGER_CONFIG ShareAccessConfig;
    ESP_ECP_LIST_CONFIG EcpListConfig;
    ESP_REMOTE_CLIENT_CONFIG RemoteClientConfig;
    ESP_ACCESS_STATE_CONFIG AccessStateConfig;
} ESP_FO_OPEN_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| OperationConfig | Specifies configuration for the IO operation. |
| DesiredAccessConfig | Specifies configuration for the desired access. |
| CreateOptionsConfig | Specifies configuration for the create options. |
| CreateDispositionConfig | Specifies configuration for the create disposition. |
| FileAttributesConfig | Specifies configuration for the file attributes. |
| ShareAccessConfig | Specifies configuration for the share access. |
| EcpListConfig | Specifies configuration for the ECP list. |
| RemoteClientConfig | Specifies configuration for the remote client. |
| AccessStateConfig | Specifies configuration for the access state. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_ACCESS_STATE_CONFIG`](wesp-rule-value-configuration.md#esp_access_state_config)
- [`ESP_ECP_LIST_CONFIG`](wesp-rule-value-configuration.md#esp_ecp_list_config)
- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_IO_OPERATION_CONFIG`](wesp-event-shared-types.md#esp_io_operation_config)
- [`ESP_REMOTE_CLIENT_CONFIG`](wesp-rule-value-configuration.md#esp_remote_client_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_FO_OPEN_PARAMETERS

The structure `ESP_FO_OPEN_PARAMETERS` contains the parameters associated with a file object open event notification.

#### Syntax

```cpp
typedef struct ESP_FO_OPEN_PARAMETERS
{
    ESP_IO_OPERATION Operation;
    ACCESS_MASK DesiredAccess;
    UINT32 CreateOptions;
    UINT32 CreateDisposition;
    UINT16 FileAttributes;
    UINT16 ShareAccess;
    ESP_ECP_LIST EcpList;
    ESP_REMOTE_CLIENT RemoteClient;
    ESP_ACCESS_STATE AccessState;
} ESP_FO_OPEN_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Operation | The IO operation for the event. |
| DesiredAccess | The ACCESS_MASK requested for the file object. |
| CreateOptions | The create options. This corresponds to the "CreateOptions" parameter of FltCreateFile. |
| CreateDisposition | The create disposition. This corresponds to the "CreateDisposition" parameter of FltCreateFile. |
| FileAttributes | Bitmask of attributes to be applied when opening the file object. |
| ShareAccess | Bitmask of share access rights requested for the file object. |
| EcpList | The list of ECPs. By default, ECPs are not included in the structure. The client must specify which ECP's to include in the notification through the "EcpListConfig" field in the structure `ESP_FO_OPEN_CONFIG`. |
| RemoteClient | A remote client. This structure is only set if the file is being opened on behalf of a remote client. |
| AccessState | An `ESP_ACCESS_STATE` structure which describes the state of the access in progress. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_ACCESS_STATE`](wesp-event-shared-types.md#esp_access_state)
- [`ESP_ECP_LIST`](wesp-event-shared-types.md#esp_ecp_list)
- [`ESP_IO_OPERATION`](wesp-event-shared-types.md#esp_io_operation)
- [`ESP_REMOTE_CLIENT`](wesp-event-shared-types.md#esp_remote_client)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## File object read

### ESP_FO_READ_CONFIG

The structure `ESP_FO_READ_CONFIG` is used to configure a file object read event.

#### Syntax

```cpp
typedef struct ESP_FO_READ_CONFIG
{
    ESP_IO_OPERATION_CONFIG OperationConfig;
    ESP_BYTE_RANGE_CONFIG ReadRangeConfig;
} ESP_FO_READ_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| OperationConfig | Specifies configuration for the IO operation. |
| ReadRangeConfig | Specifies configuration for the read range. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BYTE_RANGE_CONFIG`](wesp-rule-value-configuration.md#esp_byte_range_config)
- [`ESP_IO_OPERATION_CONFIG`](wesp-event-shared-types.md#esp_io_operation_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_FO_READ_PARAMETERS

The structure `ESP_FO_READ_PARAMETERS` contains the parameters associated with a file object read event notification.

#### Syntax

```cpp
typedef struct ESP_FO_READ_PARAMETERS
{
    ESP_IO_OPERATION Operation;
    ESP_BYTE_RANGE ReadRange;
} ESP_FO_READ_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Operation | The IO operation for the event. |
| ReadRange | The byte range that is being read. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BYTE_RANGE`](wesp-common-value-types.md#esp_byte_range)
- [`ESP_IO_OPERATION`](wesp-event-shared-types.md#esp_io_operation)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## File object write

### ESP_FO_WRITE_CONFIG

The structure `ESP_FO_WRITE_CONFIG` is used to configure a file object write event.

#### Syntax

```cpp
typedef struct ESP_FO_WRITE_CONFIG
{
    ESP_IO_OPERATION_CONFIG OperationConfig;
    ESP_BYTE_RANGE_CONFIG WriteRangeConfig;
    ESP_INTEGER_CONFIG WriteBufferSizeConfig;
    ESP_BINARY_CONFIG WriteBufferConfig;
} ESP_FO_WRITE_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| OperationConfig | Specifies configuration for the IO operation. |
| WriteRangeConfig | Specifies configuration for the write range. |
| WriteBufferSizeConfig | Specifies configuration for the write buffer size. |
| WriteBufferConfig | Specifies configuration for the write buffer. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BINARY_CONFIG`](wesp-rule-value-configuration.md#esp_binary_config)
- [`ESP_BYTE_RANGE_CONFIG`](wesp-rule-value-configuration.md#esp_byte_range_config)
- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_IO_OPERATION_CONFIG`](wesp-event-shared-types.md#esp_io_operation_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_FO_WRITE_PARAMETERS

The structure `ESP_FO_WRITE_PARAMETERS` contains the parameters associated with a file object write event notification.

#### Syntax

```cpp
typedef struct ESP_FO_WRITE_PARAMETERS
{
    ESP_IO_OPERATION Operation;
    ESP_BYTE_RANGE WriteRange;
    UINT32 WriteBufferSize;
    _Field_size_bytes_(WriteBufferSize) const void* WriteBuffer;
} ESP_FO_WRITE_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Operation | The IO operation for the event. |
| WriteRange | The byte range that is being written to. |
| WriteBufferSize | Size in bytes of the write buffer. |
| WriteBuffer | Buffer that contains the data to be written. By default, the write buffer is set to null. The client must specify to include the write buffer through the "WriteBufferConfig" field in the structure `ESP_FO_WRITE_CONFIG`. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BYTE_RANGE`](wesp-common-value-types.md#esp_byte_range)
- [`ESP_IO_OPERATION`](wesp-event-shared-types.md#esp_io_operation)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## File object cleanup

### ESP_FO_CLEANUP_CONFIG

The structure `ESP_FO_CLEANUP_CONFIG` is used to configure a file cleanup event.

#### Syntax

```cpp
typedef struct ESP_FO_CLEANUP_CONFIG
{
    ESP_IO_OPERATION_CONFIG OperationConfig;
} ESP_FO_CLEANUP_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| OperationConfig | Specifies configuration for the IO operation. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_IO_OPERATION_CONFIG`](wesp-event-shared-types.md#esp_io_operation_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_FO_CLEANUP_PARAMETERS

The structure `ESP_FO_CLEANUP_PARAMETERS` contains the parameters associated with a file object cleanup event notification.

#### Syntax

```cpp
typedef struct ESP_FO_CLEANUP_PARAMETERS
{
    ESP_IO_OPERATION Operation;
} ESP_FO_CLEANUP_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Operation | The IO operation for the event. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_IO_OPERATION`](wesp-event-shared-types.md#esp_io_operation)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
