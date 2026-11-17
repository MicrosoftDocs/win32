---
title: "WESP file stream, file, and file object event objects"
description: "Windows endpoint security platform API reference for file stream, file, and file object event objects, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- EspCreateFileStreamReferenceById
- EspCreateFileStreamReferenceByPath
- ESP_FILE_STREAM_CONFIG_FLAGS
- ESP_FILE_STREAM_CONFIG
- ESP_FILE_STREAM_INFO
- EspCreateFileReferenceById
- EspCreateFileReferenceByPath
- ESP_FILE_CONFIG_FLAGS
- ESP_FILE_CONFIG
- ESP_FILE_INFO
- ESP_FILE_OBJECT_CONFIG_FLAGS
- ESP_FILE_OBJECT_CONFIG
- ESP_FILE_OBJECT_INFO
- ESP_FO_TARGET_OBJECT_CONFIG
- ESP_FO_TARGET_OBJECT_INFO
---

# File stream, file, and file object event objects

This page contains reference entries in the [Event objects API family](wesp-api-reference.md#event-objects). Each entry includes its declaration and requirements.

## File stream

### EspCreateFileStreamReferenceById

The API `EspCreateFileStreamReferenceById` creates an event object reference for an existing file stream by its file id. This is useful in cases where a client needs to reference a stream outside the context of an event involving the stream. For example, a client may require a reference to a stream to query properties or set event object context.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateFileStreamReferenceById(
    _In_ ESP_CLIENT Client,
    _In_ const GUID* VolumeGuid,
    _In_ const FILE_ID_DESCRIPTOR* FileId,
    _In_opt_ PCWSTR StreamName,
    _Out_ ESP_EVENT_OBJECT_REF* ObjectRef
    );
```

#### Parameters

##### `Client`

Supplies the client.

##### `VolumeGuid`

Supplies the guid for the volume on which the stream is found.

##### `FileId`

Supplies the file id in which the stream is found.

##### `StreamName`

Supplies the stream name. The caller can supply nullptr to reference the default stream.

##### `ObjectRef`

Receives the reference. The reference must be closed by calling `EspCloseEventObjectReference` once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_EVENT_OBJECT_REF`](wesp-event-object-references.md#esp_event_object_ref)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspCreateFileStreamReferenceByPath

The API `EspCreateFileStreamReferenceByPath` creates an event object reference to an existing file stream by its path. This is useful in cases where a client needs to reference a file stream outside the context of an event involving the stream. For example, a client may require a reference to a file stream to query properties or set event object context.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateFileStreamReferenceByPath(
    _In_ ESP_CLIENT Client,
    _In_ const ESP_PATH* StreamPath,
    _Out_ ESP_EVENT_OBJECT_REF* ObjectRef
    );
```

#### Parameters

##### `Client`

Supplies the client.

##### `StreamPath`

Supplies the stream path.

##### `ObjectRef`

Receives the reference. The reference must be closed by calling `EspCloseEventObjectReference` once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_EVENT_OBJECT_REF`](wesp-event-object-references.md#esp_event_object_ref)
- [`ESP_PATH`](wesp-common-utilities.md#esp_path)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_FILE_STREAM_CONFIG_FLAGS

The enum `ESP_FILE_STREAM_CONFIG_FLAGS` specifies flags for an `ESP_FILE_STREAM_CONFIG` structure.

#### Syntax

```cpp
typedef enum ESP_FILE_STREAM_CONFIG_FLAGS
{
    ESP_FILE_STREAM_CONFIG_FLAGS_NONE                  = 0x00000000,
    ESP_FILE_STREAM_CONFIG_FLAGS_SKIP_IF_OBJECT_ABSENT = 0x00000001
} ESP_FILE_STREAM_CONFIG_FLAGS;
```

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_FILE_STREAM_CONFIG`](wesp-file-objects.md#esp_file_stream_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_FILE_STREAM_CONFIG

The configuration structure for a file stream event object is `ESP_FILE_STREAM_CONFIG`.

#### Syntax

```cpp
typedef struct ESP_FILE_STREAM_CONFIG
{
    ESP_FILE_STREAM_CONFIG_FLAGS Flags;
    ESP_EVENT_OBJECT_CONFIG EventObjectConfig;

    UINT32 PropertiesCount;
    _Field_size_(PropertiesCount) const ESP_FILE_STREAM_PROPERTY_ID* Properties;

    ESP_FILE_CONFIG FileConfig;
} ESP_FILE_STREAM_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Flags | Specifies flags for the file stream. |
| EventObjectConfig | Supplies event object configuration for the file stream. |
| PropertiesCount | Supplies the number of elements in the "Properties" array. |
| Properties | Supplies an array of file stream properties that should be captured for the stream. |
| FileConfig | Supplies the configuration for stream's file. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EVENT_OBJECT_CONFIG`](wesp-event-object-references.md#esp_event_object_config)
- [`ESP_FILE_CONFIG`](wesp-file-objects.md#esp_file_config)
- [`ESP_FILE_STREAM_CONFIG_FLAGS`](wesp-file-objects.md#esp_file_stream_config_flags)
- [`ESP_FILE_STREAM_PROPERTY_ID`](wesp-file-property-ids.md#esp_file_stream_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_FILE_STREAM_INFO

The structure `ESP_FILE_STREAM_INFO` specifies information for a file stream. This structure is supplied as part of an event notification (one for each file stream associated with an event) and contains various details about the file stream.

#### Syntax

```cpp
typedef struct ESP_FILE_STREAM_INFO
{
    ESP_EVENT_OBJECT_INFO ObjectInfo;
    _Maybenull_ const ESP_FILE_INFO* FileInfo;
} ESP_FILE_STREAM_INFO;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ObjectInfo | Specifies information about the file stream's event object. |
| FileInfo | Specifies information about the file stream's file. This field may be null if the client didn't specify file configuration through the "FileConfig" field in `ESP_FILE_STREAM_CONFIG`. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EVENT_OBJECT_INFO`](wesp-event-object-references.md#esp_event_object_info)
- [`ESP_FILE_INFO`](wesp-file-objects.md#esp_file_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## File

### EspCreateFileReferenceById

The API `EspCreateFileReferenceById` creates an event object reference for an existing file by its file id. This is useful in cases where a client needs to reference a file outside the context of an event involving the file. For example, a client may require a reference to a file to query properties or set event object context.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateFileReferenceById(
    _In_ ESP_CLIENT Client,
    _In_ const GUID* VolumeGuid,
    _In_ const FILE_ID_DESCRIPTOR* FileId,
    _Out_ ESP_EVENT_OBJECT_REF* ObjectRef
    );
```

#### Parameters

##### `Client`

Supplies the client.

##### `VolumeGuid`

Supplies the guid for the volume on which the file is found.

##### `FileId`

Supplies the file id for the file.

##### `ObjectRef`

Receives the reference. The reference must be closed by calling `EspCloseEventObjectReference` once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_EVENT_OBJECT_REF`](wesp-event-object-references.md#esp_event_object_ref)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspCreateFileReferenceByPath

The API `EspCreateFileReferenceByPath` creates an event object reference for an existing file by its path. This is useful in cases where a client needs to reference a file outside the context of an event involving the file. For example, a client may require a reference to a file to query properties or set event object context.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateFileReferenceByPath(
    _In_ ESP_CLIENT Client,
    _In_ const ESP_PATH* FilePath,
    _Out_ ESP_EVENT_OBJECT_REF* ObjectRef
    );
```

#### Parameters

##### `Client`

Supplies the client.

##### `FilePath`

Supplies the file path.

##### `ObjectRef`

Receives the reference. The reference must be closed by calling `EspCloseEventObjectReference` once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_EVENT_OBJECT_REF`](wesp-event-object-references.md#esp_event_object_ref)
- [`ESP_PATH`](wesp-common-utilities.md#esp_path)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_FILE_CONFIG_FLAGS

The enum `ESP_FILE_CONFIG_FLAGS` specifies flags for an `ESP_FILE_CONFIG` structure. There are currently no supported flags.

#### Syntax

```cpp
typedef enum ESP_FILE_CONFIG_FLAGS
{
    ESP_FILE_CONFIG_FLAGS_NONE = 0x00000000
} ESP_FILE_CONFIG_FLAGS;
```

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_FILE_CONFIG`](wesp-file-objects.md#esp_file_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_FILE_CONFIG

The configuration structure for a file event object is `ESP_FILE_CONFIG`.

#### Syntax

```cpp
typedef struct ESP_FILE_CONFIG
{
    ESP_FILE_CONFIG_FLAGS Flags;
    ESP_EVENT_OBJECT_CONFIG EventObjectConfig;

    UINT32 PropertiesCount;
    _Field_size_(PropertiesCount) const ESP_FILE_PROPERTY_ID* Properties;

    ESP_VOLUME_CONFIG VolumeConfig;
} ESP_FILE_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Flags | Specifies flags for the file. |
| EventObjectConfig | Supplies event object configuration for the file. |
| PropertiesCount | Supplies the number of elements in the "Properties" array. |
| Properties | Supplies an array of file properties that should be captured for the file. |
| VolumeConfig | Supplies the configuration for the file's volume. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EVENT_OBJECT_CONFIG`](wesp-event-object-references.md#esp_event_object_config)
- [`ESP_FILE_CONFIG_FLAGS`](wesp-file-objects.md#esp_file_config_flags)
- [`ESP_FILE_PROPERTY_ID`](wesp-file-property-ids.md#esp_file_property_id)
- [`ESP_VOLUME_CONFIG`](wesp-storage-objects.md#esp_volume_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_FILE_INFO

The structure `ESP_FILE_INFO` specifies information for a file. This structure is supplied as part of an event notification (one for each file associated with an event) and contains various details about the file.

#### Syntax

```cpp
typedef struct ESP_FILE_INFO
{
    ESP_EVENT_OBJECT_INFO ObjectInfo;
    _Maybenull_ const ESP_VOLUME_INFO* VolumeInfo;
} ESP_FILE_INFO;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ObjectInfo | Specifies information about the file's event object. |
| VolumeInfo | Specifies information about the file's volume. This field may be null if the client didn't specify volume configuration through the "VolumeConfig" field in `ESP_FILE_CONFIG`. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EVENT_OBJECT_INFO`](wesp-event-object-references.md#esp_event_object_info)
- [`ESP_VOLUME_INFO`](wesp-storage-objects.md#esp_volume_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## File object

### ESP_FILE_OBJECT_CONFIG_FLAGS

The enum `ESP_FILE_OBJECT_CONFIG_FLAGS` specifies flags for an `ESP_FILE_OBJECT_CONFIG` structure.

#### Syntax

```cpp
typedef enum ESP_FILE_OBJECT_CONFIG_FLAGS
{
    ESP_FILE_OBJECT_CONFIG_FLAGS_NONE                  = 0x00000000,
    ESP_FILE_OBJECT_CONFIG_FLAGS_SKIP_IF_OBJECT_ABSENT = 0x00000001
} ESP_FILE_OBJECT_CONFIG_FLAGS;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_FILE_OBJECT_CONFIG_FLAGS_SKIP_IF_OBJECT_ABSENT` | Specifies to skip applying the configuration if the file object doesn't exist. For example, if a client specifies "ParentOfTarget" configuration for a set-file-information event, but there's no such file object, the file object configuration won't be applied.<br>If the file object is absent, this flag implicitly evaluates the file object's filter to true. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_FILE_OBJECT_CONFIG`](wesp-file-objects.md#esp_file_object_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_FILE_OBJECT_CONFIG

The configuration structure for a file object event object is `ESP_FILE_OBJECT_CONFIG`.

#### Syntax

```cpp
typedef struct ESP_FILE_OBJECT_CONFIG
{
    ESP_FILE_OBJECT_CONFIG_FLAGS Flags;
    ESP_EVENT_OBJECT_CONFIG EventObjectConfig;

    UINT32 PropertiesCount;
    _Field_size_(PropertiesCount) const ESP_FILE_OBJECT_PROPERTY_ID* Properties;

    ESP_KTM_TRANSACTION_CONFIG TransactionConfig;

    ESP_FO_TARGET_OBJECT_TYPE TargetObjectType;
    ESP_FO_TARGET_OBJECT_CONFIG TargetObjectConfig;
} ESP_FILE_OBJECT_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Flags | Specifies flags for the file object. |
| EventObjectConfig | Supplies event object configuration for the file object. |
| PropertiesCount | Supplies the number of elements in the "Properties" array. |
| Properties | Supplies an array of file object properties that should be captured for the file object. |
| TransactionConfig | Supplies configuration for the file object's transaction. Note that if the file object is not part of a transaction, transaction properties won't be retrieved if the rule matches. |
| TargetObjectType | Supplies the target object's type |
| TargetObjectConfig | Supplies configuration for the file object's target object. This parameter is ignored if the TargetObjectType is `ESP_EVENT_OBJECT_TYPE_NONE`. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EVENT_OBJECT_CONFIG`](wesp-event-object-references.md#esp_event_object_config)
- [`ESP_FILE_OBJECT_CONFIG_FLAGS`](wesp-file-objects.md#esp_file_object_config_flags)
- [`ESP_FILE_OBJECT_PROPERTY_ID`](wesp-file-property-ids.md#esp_file_object_property_id)
- [`ESP_FO_TARGET_OBJECT_CONFIG`](wesp-file-objects.md#esp_fo_target_object_config)
- [`ESP_FO_TARGET_OBJECT_TYPE`](wesp-common-value-types.md#esp_fo_target_object_type)
- [`ESP_KTM_TRANSACTION_CONFIG`](wesp-other-event-objects.md#esp_ktm_transaction_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_FILE_OBJECT_INFO

The structure `ESP_FILE_OBJECT_INFO` specifies information for a file object. This structure is supplied as part of an event notification (one for each file object associated with an event) and contains various details about the file object.

#### Syntax

```cpp
typedef struct ESP_FILE_OBJECT_INFO
{
    ESP_EVENT_OBJECT_INFO ObjectInfo;
    _Maybenull_ const ESP_KTM_TRANSACTION_INFO* TransactionInfo;

    ESP_FO_TARGET_OBJECT_TYPE TargetObjectType;
    _Maybenull_ const ESP_FO_TARGET_OBJECT_INFO* TargetObjectInfo;
} ESP_FILE_OBJECT_INFO;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ObjectInfo | Specifies information about the file object's event object. |
| TransactionInfo | Specifies information about the file object's KTM transaction. This field may be null if the client didn't specify KTM transaction configuration through the "TransactionConfig" field in `ESP_FILE_OBJECT_CONFIG`. |
| TargetObjectType | Specifies the file object's target object type. |
| TargetObjectInfo | Specifies information about the file object's target object. This field may be null if the client didn't specify target object configuration through the "TargetObjectConfig" field in `ESP_FILE_OBJECT_CONFIG`. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EVENT_OBJECT_INFO`](wesp-event-object-references.md#esp_event_object_info)
- [`ESP_FO_TARGET_OBJECT_INFO`](wesp-file-objects.md#esp_fo_target_object_info)
- [`ESP_FO_TARGET_OBJECT_TYPE`](wesp-common-value-types.md#esp_fo_target_object_type)
- [`ESP_KTM_TRANSACTION_INFO`](wesp-other-event-objects.md#esp_ktm_transaction_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_FO_TARGET_OBJECT_CONFIG

The union `ESP_FO_TARGET_OBJECT_CONFIG` specifies configuration for the file object's target object. The active member in the union is determined by the "TargetObjectType" in `ESP_FILE_OBJECT_CONFIG`.

#### Syntax

```cpp
typedef union ESP_FO_TARGET_OBJECT_CONFIG
{
    ESP_FILE_STREAM_CONFIG FileStream;
    ESP_VOLUME_CONFIG Volume;
    ESP_PIPE_CONFIG Pipe;
    ESP_MAILSLOT_CONFIG Mailslot;
} ESP_FO_TARGET_OBJECT_CONFIG;
```

#### Members

| Member | Description |
| --- | --- |
| FileStream | Configuration for the file stream target object. |
| Volume | Configuration for the volume target object. |
| Pipe | Configuration for the pipe target object. |
| Mailslot | Configuration for the mailslot target object. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_FILE_OBJECT_CONFIG`](wesp-file-objects.md#esp_file_object_config)
- [`ESP_FILE_STREAM_CONFIG`](wesp-file-objects.md#esp_file_stream_config)
- [`ESP_MAILSLOT_CONFIG`](wesp-other-event-objects.md#esp_mailslot_config)
- [`ESP_PIPE_CONFIG`](wesp-other-event-objects.md#esp_pipe_config)
- [`ESP_VOLUME_CONFIG`](wesp-storage-objects.md#esp_volume_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_FO_TARGET_OBJECT_INFO

The union `ESP_FO_TARGET_OBJECT_INFO` specifies information for the file object's target object. The active member in the union is determined by the "TargetObjectType" in `ESP_FILE_OBJECT_INFO`.

#### Syntax

```cpp
typedef union ESP_FO_TARGET_OBJECT_INFO
{
    ESP_FILE_STREAM_INFO FileStream;
    ESP_VOLUME_INFO Volume;
    ESP_PIPE_INFO Pipe;
    ESP_MAILSLOT_INFO Mailslot;
} ESP_FO_TARGET_OBJECT_INFO;
```

#### Members

| Member | Description |
| --- | --- |
| FileStream | Information for the file stream target object. |
| Volume | Information for the volume target object. |
| Pipe | Information for the pipe target object. |
| Mailslot | Information for the mailslot target object. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_FILE_OBJECT_INFO`](wesp-file-objects.md#esp_file_object_info)
- [`ESP_FILE_STREAM_INFO`](wesp-file-objects.md#esp_file_stream_info)
- [`ESP_MAILSLOT_INFO`](wesp-other-event-objects.md#esp_mailslot_info)
- [`ESP_PIPE_INFO`](wesp-other-event-objects.md#esp_pipe_info)
- [`ESP_VOLUME_INFO`](wesp-storage-objects.md#esp_volume_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
