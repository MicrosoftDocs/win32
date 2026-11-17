---
title: "WESP thread, process, and token event objects"
description: "Windows endpoint security platform API reference for thread, process, and token event objects, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- EspCreateThreadReference
- ESP_THREAD_CONFIG_FLAGS
- ESP_THREAD_CONFIG
- ESP_THREAD_INFO
- EspCreateProcessReference
- ESP_PROCESS_CONFIG_FLAGS
- ESP_PROCESS_CONFIG
- ESP_PROCESS_INFO
- EspCreateThreadTokenReference
- EspCreateProcessTokenReference
- ESP_TOKEN_CONFIG_FLAGS
- ESP_TOKEN_CONFIG
- ESP_TOKEN_INFO
---

# Thread, process, and token event objects

This page contains reference entries in the [Event objects API family](wesp-api-reference.md#event-objects). Each entry includes its declaration and requirements.

## Thread

### EspCreateThreadReference

The API `EspCreateThreadReference` creates an event object reference to an existing thread. This is useful in cases where a client needs to reference a thread outside the context of an event involving the thread. For example, a client may require a reference to a thread to query properties or set event object context keys.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateThreadReference(
    _In_ ESP_CLIENT Client,
    _In_ UINT32 ThreadId,
    _Out_ ESP_EVENT_OBJECT_REF* ObjectRef
    );
```

#### Parameters

##### `Client`

Supplies the client.

##### `ThreadId`

Supplies the thread id.

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

### ESP_THREAD_CONFIG_FLAGS

The enum `ESP_THREAD_CONFIG_FLAGS` specifies flags for an `ESP_THREAD_CONFIG` structure.

#### Syntax

```cpp
typedef enum ESP_THREAD_CONFIG_FLAGS
{
    ESP_THREAD_CONFIG_FLAGS_NONE                  = 0x00000000,
    ESP_THREAD_CONFIG_FLAGS_SKIP_IF_OBJECT_ABSENT = 0x00000001
} ESP_THREAD_CONFIG_FLAGS;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_THREAD_CONFIG_FLAGS_SKIP_IF_OBJECT_ABSENT` | Specifies to skip applying the configuration if the thread doesn't exist. For example, if a client sets this flag for an IO operation's requestor thread and there's no requestor thread, the thread configuration won't be applied.<br>If the thread is absent, this flag implicitly evaluates the thread's filter to true. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_THREAD_CONFIG`](wesp-execution-objects.md#esp_thread_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_THREAD_CONFIG

The configuration structure for a thread event object is `ESP_THREAD_CONFIG`.

#### Syntax

```cpp
typedef struct ESP_THREAD_CONFIG
{
    ESP_THREAD_CONFIG_FLAGS Flags;
    ESP_EVENT_OBJECT_CONFIG EventObjectConfig;

    UINT32 PropertiesCount;
    _Field_size_(PropertiesCount) const ESP_THREAD_PROPERTY_ID* Properties;

    ESP_TOKEN_CONFIG TokenConfig;
    ESP_PROCESS_CONFIG OwningProcessConfig;
} ESP_THREAD_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Flags | Specifies flags for the thread. |
| EventObjectConfig | Supplies event object configuration for the thread. |
| PropertiesCount | Supplies the number of elements in the "Properties" array. |
| Properties | Supplies an array of thread properties that should be captured for the thread. |
| TokenConfig | Supplies the configuration for the thread's token. |
| OwningProcessConfig | Supplies the configuration for the thread's owning process. This is the equivalent of IoThreadToProcess(). |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EVENT_OBJECT_CONFIG`](wesp-event-object-references.md#esp_event_object_config)
- [`ESP_PROCESS_CONFIG`](wesp-execution-objects.md#esp_process_config)
- [`ESP_THREAD_CONFIG_FLAGS`](wesp-execution-objects.md#esp_thread_config_flags)
- [`ESP_THREAD_PROPERTY_ID`](wesp-execution-property-ids.md#esp_thread_property_id)
- [`ESP_TOKEN_CONFIG`](wesp-execution-objects.md#esp_token_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_THREAD_INFO

The structure `ESP_THREAD_INFO` specifies information for a thread. This structure is supplied as part of an event notification (one for each thread associated with an event) and contains various details about the thread.

#### Syntax

```cpp
typedef struct ESP_THREAD_INFO
{
    ESP_EVENT_OBJECT_INFO ObjectInfo;
    _Maybenull_ const ESP_TOKEN_INFO* TokenInfo;
    _Maybenull_ const ESP_PROCESS_INFO* OwningProcessInfo;
} ESP_THREAD_INFO;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ObjectInfo | Specifies information about the thread's event object. |
| TokenInfo | Specifies information about the thread's token. This field may be null if the client didn't specify token configuration through the "TokenConfig" field in `ESP_THREAD_CONFIG`. |
| OwningProcessInfo | Specifies information about the thread's owning process. This field may be null if the client didn't specify owning process configuration through the "OwningProcessConfig" field in `ESP_THREAD_CONFIG`. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EVENT_OBJECT_INFO`](wesp-event-object-references.md#esp_event_object_info)
- [`ESP_PROCESS_INFO`](wesp-execution-objects.md#esp_process_info)
- [`ESP_TOKEN_INFO`](wesp-execution-objects.md#esp_token_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Process

### EspCreateProcessReference

The API `EspCreateProcessReference` creates an event object reference for an existing process. This is useful in cases where a client needs to reference a process outside the context of an event involving the process. For example, a client may require a reference to a process to query properties or set event object context keys.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateProcessReference(
    _In_ ESP_CLIENT Client,
    _In_ UINT32 ProcessId,
    _Out_ ESP_EVENT_OBJECT_REF* ObjectRef
    );
```

#### Parameters

##### `Client`

Supplies the client.

##### `ProcessId`

Supplies the process id.

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

### ESP_PROCESS_CONFIG_FLAGS

The enum `ESP_PROCESS_CONFIG_FLAGS` specifies flags for an `ESP_PROCESS_CONFIG` structure.

#### Syntax

```cpp
typedef enum ESP_PROCESS_CONFIG_FLAGS
{
    ESP_PROCESS_CONFIG_FLAGS_NONE                              = 0x00000000,
    ESP_PROCESS_CONFIG_FLAGS_SKIP_IF_OBJECT_ABSENT             = 0x00000001,
    ESP_PROCESS_CONFIG_FLAGS_INCLUDE_EVENT_OBJECT_PARENT_CHAIN = 0x00000002,
    ESP_PROCESS_CONFIG_FLAGS_QUERY_PROPERTIES_PARENT_CHAIN     = 0x00000004,
    ESP_PROCESS_CONFIG_FLAGS_FILTER_MATCH_ANY_PARENT           = 0x00000008,
    ESP_PROCESS_CONFIG_FLAGS_FILTER_MATCH_ALL_PARENTS          = 0x00000010
} ESP_PROCESS_CONFIG_FLAGS;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_PROCESS_CONFIG_FLAGS_SKIP_IF_OBJECT_ABSENT` | Specifies to skip applying the configuration if the process doesn't exist. For example, if a client sets this flag for an IO operation's requestor process and there's no requestor process, the process configuration won't be applied.<br>If the process is absent, this flag implicitly evaluates the process's filter to true. |
| `ESP_PROCESS_CONFIG_FLAGS_INCLUDE_EVENT_OBJECT_PARENT_CHAIN` | Includes the event object for each process in the parent chain in the notification. |
| `ESP_PROCESS_CONFIG_FLAGS_QUERY_PROPERTIES_PARENT_CHAIN` | Includes the process properties query for each process in the parent chain in the notification. |
| `ESP_PROCESS_CONFIG_FLAGS_FILTER_MATCH_ANY_PARENT` | The specified process filter will match if it matches this process or any process in the parent chain. This flag cannot be set if the match-all-parents flag is set. |
| `ESP_PROCESS_CONFIG_FLAGS_FILTER_MATCH_ALL_PARENTS` | The specified process filter will match if it matches this process and every process in the parent chain. This flag cannot be set if the match-any-parent flag is set. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_PROCESS_CONFIG`](wesp-execution-objects.md#esp_process_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_PROCESS_CONFIG

The configuration structure for a process event object is `ESP_PROCESS_CONFIG`.

#### Syntax

```cpp
typedef struct ESP_PROCESS_CONFIG
{
    ESP_PROCESS_CONFIG_FLAGS Flags;
    ESP_EVENT_OBJECT_CONFIG EventObjectConfig;

    UINT32 PropertiesCount;
    _Field_size_(PropertiesCount) const ESP_PROCESS_PROPERTY_ID* Properties;

    ESP_TOKEN_CONFIG TokenConfig;
    ESP_FILE_STREAM_CONFIG ImageFileConfig;
    const struct ESP_PROCESS_CONFIG* ParentProcessConfig;
} ESP_PROCESS_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Flags | Specifies flags for the process. |
| EventObjectConfig | Supplies event object configuration for the process. |
| PropertiesCount | Supplies the number of elements in the "Properties" array. |
| Properties | Supplies an array of process properties that should be captured for the process. |
| TokenConfig | Supplies the configuration for the process's token. |
| ImageFileConfig | Supplies the configuration for the process's image file. |
| ParentProcessConfig | Supplies the configuration for the parent process. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EVENT_OBJECT_CONFIG`](wesp-event-object-references.md#esp_event_object_config)
- [`ESP_FILE_STREAM_CONFIG`](wesp-file-objects.md#esp_file_stream_config)
- [`ESP_PROCESS_CONFIG_FLAGS`](wesp-execution-objects.md#esp_process_config_flags)
- [`ESP_PROCESS_PROPERTY_ID`](wesp-execution-property-ids.md#esp_process_property_id)
- [`ESP_TOKEN_CONFIG`](wesp-execution-objects.md#esp_token_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_PROCESS_INFO

The structure `ESP_PROCESS_INFO` specifies information for a process. This structure is supplied as part of an event notification (one for each process associated with an event) and contains various details about the process.

#### Syntax

```cpp
typedef struct ESP_PROCESS_INFO
{
    ESP_EVENT_OBJECT_INFO ObjectInfo;
    _Maybenull_ const ESP_TOKEN_INFO* TokenInfo;
    _Maybenull_ const ESP_FILE_STREAM_INFO* ImageFileInfo;
    _Maybenull_ const struct ESP_PROCESS_INFO* ParentProcessInfo;
} ESP_PROCESS_INFO;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ObjectInfo | Specifies information about the process's event object. |
| TokenInfo | Specifies information about the thread's token. This field may be null if the client didn't specify token configuration through the "TokenConfig" field in `ESP_PROCESS_CONFIG`. |
| ImageFileInfo | Specifies information about the process's image file. This field may be null if the client didn't specify image file configuration through the "ImageFileConfig" field in `ESP_PROCESS_CONFIG`. |
| ParentProcessInfo | Specifies information about the process's parent process. This field may be null if the client didn't specify parent process configuration through the "ParentProcessConfig" field in `ESP_PROCESS_CONFIG`. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EVENT_OBJECT_INFO`](wesp-event-object-references.md#esp_event_object_info)
- [`ESP_FILE_STREAM_INFO`](wesp-file-objects.md#esp_file_stream_info)
- [`ESP_TOKEN_INFO`](wesp-execution-objects.md#esp_token_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Token

### EspCreateThreadTokenReference

The API `EspCreateThreadTokenReference` creates an event object reference to an existing thread's token. This is useful in cases where a client needs to reference a thread's token outside the context of an event involving the thread's token. For example, a client may require a reference to a thread's token to query properties or set event object context.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateThreadTokenReference(
    _In_ ESP_CLIENT Client,
    _In_ UINT32 ThreadId,
    _Out_ ESP_EVENT_OBJECT_REF* ObjectRef
    );
```

#### Parameters

##### `Client`

Supplies the client.

##### `ThreadId`

Supplies the thread id.

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

### EspCreateProcessTokenReference

The API `EspCreateProcessTokenReference` creates an event object reference to an existing process's token. This is useful in cases where a client needs to reference a process's token outside the context of an event involving the process's token. For example, a client may require a reference to a process's token to query properties or set event object context.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateProcessTokenReference(
    _In_ ESP_CLIENT Client,
    _In_ UINT32 ProcessId,
    _Out_ ESP_EVENT_OBJECT_REF* ObjectRef
    );
```

#### Parameters

##### `Client`

Supplies the client.

##### `ProcessId`

Supplies the process id.

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

### ESP_TOKEN_CONFIG_FLAGS

The enum `ESP_TOKEN_CONFIG_FLAGS` specifies flags for an `ESP_TOKEN_CONFIG` structure.

#### Syntax

```cpp
typedef enum ESP_TOKEN_CONFIG_FLAGS
{
    ESP_TOKEN_CONFIG_FLAGS_NONE                  = 0x00000000,
    ESP_TOKEN_CONFIG_FLAGS_SKIP_IF_OBJECT_ABSENT = 0x00000001
} ESP_TOKEN_CONFIG_FLAGS;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_TOKEN_CONFIG_FLAGS_SKIP_IF_OBJECT_ABSENT` | Specifies to skip applying the configuration if the token doesn't exist. For example, if a client sets this flag for a thread's token and the thread is not impersonating, the token configuration won't be applied.<br>If the token is absent, this flag implicitly evaluates the token's filter to true. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_TOKEN_CONFIG`](wesp-execution-objects.md#esp_token_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_TOKEN_CONFIG

The configuration structure for a token event object is `ESP_TOKEN_CONFIG`.

#### Syntax

```cpp
typedef struct ESP_TOKEN_CONFIG
{
    ESP_TOKEN_CONFIG_FLAGS Flags;
    ESP_EVENT_OBJECT_CONFIG EventObjectConfig;

    UINT32 PropertiesCount;
    _Field_size_(PropertiesCount) const ESP_TOKEN_PROPERTY_ID* Properties;
} ESP_TOKEN_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Flags | Specifies flags for the token. |
| EventObjectConfig | Supplies event object configuration for the token. |
| PropertiesCount | Supplies the number of elements in the "Properties" array. |
| Properties | Supplies an array of token properties that should be captured for the token. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EVENT_OBJECT_CONFIG`](wesp-event-object-references.md#esp_event_object_config)
- [`ESP_TOKEN_CONFIG_FLAGS`](wesp-execution-objects.md#esp_token_config_flags)
- [`ESP_TOKEN_PROPERTY_ID`](wesp-execution-property-ids.md#esp_token_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_TOKEN_INFO

The structure `ESP_TOKEN_INFO` specifies information for a token. This structure is supplied as part of an event notification (one for each token associated with an event) and contains various details about the token.

#### Syntax

```cpp
typedef struct ESP_TOKEN_INFO
{
    ESP_EVENT_OBJECT_INFO ObjectInfo;
} ESP_TOKEN_INFO;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ObjectInfo | Specifies information about the token's event object. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EVENT_OBJECT_INFO`](wesp-event-object-references.md#esp_event_object_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
