---
title: "WESP event capabilities"
description: "Windows endpoint security platform API reference for event capabilities, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- EspGetEventCapabilities
- ESP_EVENT_CAPABILITIES
- EspIsThreadPropertySupported
- EspIsProcessPropertySupported
- EspIsFileStreamPropertySupported
- EspIsFilePropertySupported
- EspIsFileObjectPropertySupported
- EspIsVolumePropertySupported
- EspIsDiskPropertySupported
- EspIsRegistryKeyPropertySupported
- EspIsRegistryKeyObjectPropertySupported
- EspIsDesktopPropertySupported
- EspIsKtmTransactionPropertySupported
- EspIsPipePropertySupported
- EspIsMailslotPropertySupported
- EspIsTokenPropertySupported
- EspIsEventPropertySupported
- EspIsClientPropertySupported
---

# Event capabilities

This page contains reference entries in the [Event capabilities API family](wesp-api-reference.md#event-capabilities). Each entry includes its declaration and requirements.

## Event capabilities

### EspGetEventCapabilities

The API `EspGetEventCapabilities` can be used to obtain the supported capabilities for a specific event for a specific client. Some event types may not be supported on down-level OS releases, or may not support all capabilities. The capabilities supported by a given WESP client are determined based on their certificate. Some clients may have full capabilities (e.g. block/monitor) for all events, whereas other clients may only have monitor capabilities for a subset of events. This API can also be used by clients to determine whether blocking an event is supported.

#### Syntax

```cpp
HRESULT
WINAPI
EspGetEventCapabilities(
    _In_ ESP_CLIENT Client,
    _In_ ESP_EVENT_TYPE EventType,
    _Out_ ESP_EVENT_CAPABILITIES* Capabilities
    );
```

#### Parameters

##### `Client`

Specifies the client.

##### `EventType`

Specifies the event type.

##### `Capabilities`

Receives the supported capabilities for the event.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_EVENT_CAPABILITIES`](wesp-event-capabilities.md#esp_event_capabilities)
- [`ESP_EVENT_TYPE`](wesp-event-shared-types.md#esp_event_type)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_EVENT_CAPABILITIES

The enum `ESP_EVENT_CAPABILITIES` defines the set of capabilities that are supported for a given event type.

#### Syntax

```cpp
typedef enum ESP_EVENT_CAPABILITIES
{
    ESP_EVENT_CAPABILITIES_NONE                 = 0x00000000,
    ESP_EVENT_CAPABILITIES_MONITOR              = 0x00000001,
    ESP_EVENT_CAPABILITIES_BLOCK                = 0x00000002,
    ESP_EVENT_CAPABILITIES_ALLOW                = 0x00000004,
    ESP_EVENT_CAPABILITIES_NOTIFY_ON_COMPLETION = 0x00000008,
    ESP_EVENT_CAPABILITIES_MODIFY               = 0x00000010
} ESP_EVENT_CAPABILITIES;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_EVENT_CAPABILITIES_MONITOR` | The event can be monitored. This is the standard capability allowing the client to use the following rule actions:<br>`ESP_RULE_ACTION_NOTIFY`<br>`ESP_RULE_ACTION_NO_NOTIFY`<br>`ESP_RULE_ACTION_IGNORE`<br>`ESP_RULE_ACTION_MATCH_SUBRULES`<br>`ESP_RULE_ACTION_CONTINUE_MATCHING_NEXT_RULE`<br>`ESP_RULE_ACTION_CONTINUE_MATCHING_NEXT_SUBRULE` |
| `ESP_EVENT_CAPABILITIES_BLOCK` | The event can be blocked using the rule action `ESP_RULE_ACTION_BLOCK`. |
| `ESP_EVENT_CAPABILITIES_ALLOW` | The event can be allowed using the rule action `ESP_RULE_ACTION_ALLOW`. |
| `ESP_EVENT_CAPABILITIES_NOTIFY_ON_COMPLETION` | The event supports the rule action `ESP_RULE_ACTION_NOTIFY_ON_COMPLETION`. |
| `ESP_EVENT_CAPABILITIES_MODIFY` | The event can be modified through the "EventModify" field in the rule descriptor. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Property support

### EspIsThreadPropertySupported

The API `EspIsThreadPropertySupported` can be used to dynamically check if a thread property ID is supported by the WESP framework. Some thread property IDs may not be supported on down-level OS releases.

#### Syntax

```cpp
HRESULT
WINAPI
EspIsThreadPropertySupported(
    _In_ ESP_CLIENT Client,
    _In_ ESP_THREAD_PROPERTY_ID PropertyId,
    _Out_ BOOL* IsSupported
    );
```

#### Parameters

##### `Client`

Specifies the client.

##### `PropertyId`

The thread property ID.

##### `IsSupported`

Receives a boolean that is true if the property is supported; false otherwise.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_THREAD_PROPERTY_ID`](wesp-execution-property-ids.md#esp_thread_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspIsProcessPropertySupported

The API `EspIsProcessPropertySupported` can be used to dynamically check if a process property ID is supported by the WESP framework. Some process property IDs may not be supported on down-level OS releases.

#### Syntax

```cpp
HRESULT
WINAPI
EspIsProcessPropertySupported(
    _In_ ESP_CLIENT Client,
    _In_ ESP_PROCESS_PROPERTY_ID PropertyId,
    _Out_ BOOL* IsSupported
    );
```

#### Parameters

##### `Client`

Specifies the client.

##### `PropertyId`

The process property ID.

##### `IsSupported`

Receives a boolean that is true if the property is supported; false otherwise.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_PROCESS_PROPERTY_ID`](wesp-execution-property-ids.md#esp_process_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspIsFileStreamPropertySupported

The API `EspIsFileStreamPropertySupported` can be used to dynamically check if a file stream property ID is supported by the WESP framework. Some file stream property IDs may not be supported on down-level OS releases.

#### Syntax

```cpp
HRESULT
WINAPI
EspIsFileStreamPropertySupported(
    _In_ ESP_CLIENT Client,
    _In_ ESP_FILE_STREAM_PROPERTY_ID PropertyId,
    _Out_ BOOL* IsSupported
    );
```

#### Parameters

##### `Client`

Specifies the client.

##### `PropertyId`

The stream property ID.

##### `IsSupported`

Receives a boolean that is true if the property is supported; false otherwise.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_FILE_STREAM_PROPERTY_ID`](wesp-file-property-ids.md#esp_file_stream_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspIsFilePropertySupported

The API `EspIsFilePropertySupported` can be used to dynamically check if a file property ID is supported by the WESP framework. Some file property IDs may not be supported on down-level OS releases.

#### Syntax

```cpp
HRESULT
WINAPI
EspIsFilePropertySupported(
    _In_ ESP_CLIENT Client,
    _In_ ESP_FILE_PROPERTY_ID PropertyId,
    _Out_ BOOL* IsSupported
    );
```

#### Parameters

##### `Client`

Specifies the client.

##### `PropertyId`

The file property ID.

##### `IsSupported`

Receives a boolean that is true if the property is supported; false otherwise.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_FILE_PROPERTY_ID`](wesp-file-property-ids.md#esp_file_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspIsFileObjectPropertySupported

The API `EspIsFileObjectPropertySupported` can be used to dynamically check if a file object property ID is supported by the WESP framework. Some file object property IDs may not be supported on down-level OS releases.

#### Syntax

```cpp
HRESULT
WINAPI
EspIsFileObjectPropertySupported(
    _In_ ESP_CLIENT Client,
    _In_ ESP_FILE_OBJECT_PROPERTY_ID PropertyId,
    _Out_ BOOL* IsSupported
    );
```

#### Parameters

##### `Client`

Specifies the client.

##### `PropertyId`

The file object property ID.

##### `IsSupported`

Receives a boolean that is true if the property is supported; false otherwise.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_FILE_OBJECT_PROPERTY_ID`](wesp-file-property-ids.md#esp_file_object_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspIsVolumePropertySupported

The API `EspIsVolumePropertySupported` can be used to dynamically check if a volume property ID is supported by the WESP framework. Some volume property IDs may not be supported on down-level OS releases.

#### Syntax

```cpp
HRESULT
WINAPI
EspIsVolumePropertySupported(
    _In_ ESP_CLIENT Client,
    _In_ ESP_VOLUME_PROPERTY_ID PropertyId,
    _Out_ BOOL* IsSupported
    );
```

#### Parameters

##### `Client`

Specifies the client.

##### `PropertyId`

The volume property ID.

##### `IsSupported`

Receives a boolean that is true if the property is supported; false otherwise.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_VOLUME_PROPERTY_ID`](wesp-file-property-ids.md#esp_volume_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspIsDiskPropertySupported

The API `EspIsDiskPropertySupported` can be used to dynamically check if a disk property ID is supported by the WESP framework. Some disk property IDs may not be supported on down-level OS releases.

#### Syntax

```cpp
HRESULT
WINAPI
EspIsDiskPropertySupported(
    _In_ ESP_CLIENT Client,
    _In_ ESP_DISK_PROPERTY_ID PropertyId,
    _Out_ BOOL* IsSupported
    );
```

#### Parameters

##### `Client`

Specifies the client.

##### `PropertyId`

The disk property ID.

##### `IsSupported`

Receives a boolean that is true if the property is supported; false otherwise.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_DISK_PROPERTY_ID`](wesp-file-property-ids.md#esp_disk_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspIsRegistryKeyPropertySupported

The API `EspIsRegistryKeyPropertySupported` can be used to dynamically check if a registry key property ID is supported by the WESP framework. Some registry key property IDs may not be supported on down-level OS releases.

#### Syntax

```cpp
HRESULT
WINAPI
EspIsRegistryKeyPropertySupported(
    _In_ ESP_CLIENT Client,
    _In_ ESP_REGISTRY_KEY_PROPERTY_ID PropertyId,
    _Out_ BOOL* IsSupported
    );
```

#### Parameters

##### `Client`

Specifies the client.

##### `PropertyId`

The registry key property ID.

##### `IsSupported`

Receives a boolean that is true if the property is supported; false otherwise.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_REGISTRY_KEY_PROPERTY_ID`](wesp-other-property-ids.md#esp_registry_key_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspIsRegistryKeyObjectPropertySupported

The API `EspIsRegistryKeyObjectPropertySupported` can be used to dynamically check if a registry key object property ID is supported by the WESP framework. Some registry key object property IDs may not be supported on down-level OS releases.

#### Syntax

```cpp
HRESULT
WINAPI
EspIsRegistryKeyObjectPropertySupported(
    _In_ ESP_CLIENT Client,
    _In_ ESP_REGISTRY_KEY_OBJECT_PROPERTY_ID PropertyId,
    _Out_ BOOL* IsSupported
    );
```

#### Parameters

##### `Client`

Specifies the client.

##### `PropertyId`

The registry key object property ID.

##### `IsSupported`

Receives a boolean that is true if the property is supported; false otherwise.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_REGISTRY_KEY_OBJECT_PROPERTY_ID`](wesp-other-property-ids.md#esp_registry_key_object_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspIsDesktopPropertySupported

The API `EspIsDesktopPropertySupported` can be used to dynamically check if a desktop property ID is supported by the WESP framework. Some desktop property IDs may not be supported on down-level OS releases.

#### Syntax

```cpp
HRESULT
WINAPI
EspIsDesktopPropertySupported(
    _In_ ESP_CLIENT Client,
    _In_ ESP_DESKTOP_PROPERTY_ID PropertyId,
    _Out_ BOOL* IsSupported
    );
```

#### Parameters

##### `Client`

Specifies the client.

##### `PropertyId`

The desktop property ID.

##### `IsSupported`

Receives a boolean that is true if the property is supported; false otherwise.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_DESKTOP_PROPERTY_ID`](wesp-other-property-ids.md#esp_desktop_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspIsKtmTransactionPropertySupported

The API `EspIsKtmTransactionPropertySupported` can be used to dynamically check if a KTM transaction property ID is supported by the WESP framework. Some KTM transaction property IDs may not be supported on down-level OS releases.

#### Syntax

```cpp
HRESULT
WINAPI
EspIsKtmTransactionPropertySupported(
    _In_ ESP_CLIENT Client,
    _In_ ESP_KTM_TRANSACTION_PROPERTY_ID PropertyId,
    _Out_ BOOL* IsSupported
    );
```

#### Parameters

##### `Client`

Specifies the client.

##### `PropertyId`

The KTM transaction property ID.

##### `IsSupported`

Receives a boolean that is true if the property is supported; false otherwise.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_KTM_TRANSACTION_PROPERTY_ID`](wesp-other-property-ids.md#esp_ktm_transaction_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspIsPipePropertySupported

The API `EspIsPipePropertySupported` can be used to dynamically check if a pipe property ID is supported by the WESP framework. Some pipe property IDs may not be supported on down-level OS releases.

#### Syntax

```cpp
HRESULT
WINAPI
EspIsPipePropertySupported(
    _In_ ESP_CLIENT Client,
    _In_ ESP_PIPE_PROPERTY_ID PropertyId,
    _Out_ BOOL* IsSupported
    );
```

#### Parameters

##### `Client`

Specifies the client.

##### `PropertyId`

The pipe property ID.

##### `IsSupported`

Receives a boolean that is true if the property is supported; false otherwise.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_PIPE_PROPERTY_ID`](wesp-other-property-ids.md#esp_pipe_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspIsMailslotPropertySupported

The API `EspIsMailslotPropertySupported` can be used to dynamically check if a mailslot property ID is supported by the WESP framework. Some mailslot property IDs may not be supported on down-level OS releases.

#### Syntax

```cpp
HRESULT
WINAPI
EspIsMailslotPropertySupported(
    _In_ ESP_CLIENT Client,
    _In_ ESP_MAILSLOT_PROPERTY_ID PropertyId,
    _Out_ BOOL* IsSupported
    );
```

#### Parameters

##### `Client`

Specifies the client.

##### `PropertyId`

The mailslot property ID.

##### `IsSupported`

Receives a boolean that is true if the property is supported; false otherwise.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_MAILSLOT_PROPERTY_ID`](wesp-other-property-ids.md#esp_mailslot_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspIsTokenPropertySupported

The API `EspIsTokenPropertySupported` can be used to dynamically check if a token property ID is supported by the WESP framework. Some token property IDs may not be supported on down-level OS releases.

#### Syntax

```cpp
HRESULT
WINAPI
EspIsTokenPropertySupported(
    _In_ ESP_CLIENT Client,
    _In_ ESP_TOKEN_PROPERTY_ID PropertyId,
    _Out_ BOOL* IsSupported
    );
```

#### Parameters

##### `Client`

Specifies the client.

##### `PropertyId`

The token property ID.

##### `IsSupported`

Receives a boolean that is true if the property is supported; false otherwise.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_TOKEN_PROPERTY_ID`](wesp-execution-property-ids.md#esp_token_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspIsEventPropertySupported

The API `EspIsEventPropertySupported` can be used to dynamically check if an event property ID is supported by the WESP framework. Some event property IDs may not be supported on down-level OS releases.

#### Syntax

```cpp
HRESULT
WINAPI
EspIsEventPropertySupported(
    _In_ ESP_CLIENT Client,
    _In_ ESP_EVENT_PROPERTY_ID PropertyId,
    _Out_ BOOL* IsSupported
    );
```

#### Parameters

##### `Client`

Specifies the client.

##### `PropertyId`

The event property ID.

##### `IsSupported`

Receives a boolean that is true if the property is supported; false otherwise.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_EVENT_PROPERTY_ID`](wesp-execution-property-ids.md#esp_event_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspIsClientPropertySupported

The API `EspIsClientPropertySupported` can be used to dynamically check if a client property ID is supported by the WESP framework. Some thread property IDs may not be supported on down-level OS releases.

#### Syntax

```cpp
HRESULT
WINAPI
EspIsClientPropertySupported(
    _In_ ESP_CLIENT Client,
    _In_ ESP_CLIENT_PROPERTY_ID PropertyId,
    _Out_ BOOL* IsSupported
    );
```

#### Parameters

##### `Client`

Specifies the client.

##### `PropertyId`

The client property ID.

##### `IsSupported`

Receives a boolean that is true if the property is supported; false otherwise.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_CLIENT_PROPERTY_ID`](wesp-execution-property-ids.md#esp_client_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
