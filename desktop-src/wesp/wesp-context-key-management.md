---
title: "WESP context key management"
description: "Windows endpoint security platform API reference for context key management, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- EspSetClientContextKey
- EspSetEventObjectContextKey
- EspEnumerateAllClientContextKeys
- EspEnumerateAllEventObjectContextKeys
- ESP_CONTEXT_KEY_VALUE_TYPE
- ESP_CONTEXT_KEY_UPDATE_TYPE
- ESP_CONTEXT_KEY_LIFETIME
- ESP_CONTEXT_KEY_UPDATE_FLAGS
- ESP_CONTEXT_KEY_UPDATE
- ESP_CONTEXT_KEY_INFO
- ESP_CONTEXT_KEY_CONFIG
---

# Context key management

This page contains reference entries in the [Context keys API family](wesp-api-reference.md#context-keys). Each entry includes its declaration and requirements.

## Context key functions

### EspSetClientContextKey

The API `EspSetClientContextKey` adds, removes, or updates a client context key. This is useful for maintaining global state for a client. For example, let's say a client has a series of flags that represent whether a policy is enabled or not.  These flags can be stored in a client context key by calling `EspSetClientContextKey`. Clients can then create filters that compare against this context key. This provides a mechanism for a client to toggle flags on/off in their client context to enable or disable global behavior without needing to update rules.

#### Syntax

```cpp
HRESULT
WINAPI
EspSetClientContextKey(
    _In_ ESP_CLIENT Client,
    _In_ const ESP_CONTEXT_KEY_UPDATE* Update
    );
```

#### Parameters

##### `Client`

Supplies the client for which to set context.

##### `Update`

Supplies an `ESP_CONTEXT_KEY_UPDATE` structure that describes the context key update.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_CONTEXT_KEY_UPDATE`](wesp-context-key-management.md#esp_context_key_update)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspSetEventObjectContextKey

The API `EspSetEventObjectContextKey` is used to add, remove, or update an event object context key.

#### Syntax

```cpp
HRESULT
WINAPI
EspSetEventObjectContextKey(
    _In_ ESP_EVENT_OBJECT Object,
    _In_ const ESP_CONTEXT_KEY_UPDATE* Update
    );
```

#### Parameters

##### `Object`

Supplies the event object.

##### `Update`

Supplies an `ESP_CONTEXT_KEY_UPDATE` structure that describes the context key update.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CONTEXT_KEY_UPDATE`](wesp-context-key-management.md#esp_context_key_update)
- [`ESP_EVENT_OBJECT`](wesp-event-object-references.md#esp_event_object)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspEnumerateAllClientContextKeys

The API `EspEnumerateAllClientContextKeys` enumerates all the context keys currently associated with a client.

#### Syntax

```cpp
HRESULT
WINAPI
EspEnumerateAllClientContextKeys(
    _In_ ESP_CLIENT Client,
    _Out_ UINT32* EntriesCount,
    _Outptr_result_buffer_all_(*EntriesCount) ESP_CONTEXT_KEY_INFO** Entries
    );
```

#### Parameters

##### `Client`

Supplies the client to enumerate all context keys for.

##### `EntriesCount`

Receives the number of elements in the entries array.

##### `Entries`

Receives an array of `ESP_CONTEXT_KEY_INFO` structures that contain information for each context key. This array must be freed by calling `EspFreeMemory`.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_CONTEXT_KEY_INFO`](wesp-context-key-management.md#esp_context_key_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspEnumerateAllEventObjectContextKeys

The API `EspEnumerateAllEventObjectContextKeys` enumerates all the context keys currently associated with an event object.

#### Syntax

```cpp
HRESULT
WINAPI
EspEnumerateAllEventObjectContextKeys(
    _In_ ESP_EVENT_OBJECT Object,
    _Out_ UINT32* EntriesCount,
    _Outptr_result_buffer_all_(*EntriesCount) ESP_CONTEXT_KEY_INFO** Entries
    );
```

#### Parameters

##### `Object`

Supplies the event object to enumerate all context keys for.

##### `EntriesCount`

Receives the number of elements in the entries array.

##### `Entries`

Receives an array of `ESP_CONTEXT_KEY_INFO` structures that contains information for each context key. The array must be freed by calling `EspFreeMemory`.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CONTEXT_KEY_INFO`](wesp-context-key-management.md#esp_context_key_info)
- [`ESP_EVENT_OBJECT`](wesp-event-object-references.md#esp_event_object)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Context key types

### ESP_CONTEXT_KEY_VALUE_TYPE

The enum `ESP_CONTEXT_KEY_VALUE_TYPE` defines a context key value type.

#### Syntax

```cpp
typedef enum ESP_CONTEXT_KEY_VALUE_TYPE
{
    ESP_CONTEXT_KEY_VALUE_TYPE_NONE = 0,
    ESP_CONTEXT_KEY_VALUE_TYPE_INTEGER,
    ESP_CONTEXT_KEY_VALUE_TYPE_STRING,
    ESP_CONTEXT_KEY_VALUE_TYPE_BINARY,
    ESP_CONTEXT_KEY_VALUE_TYPE_BINDING_KEY
} ESP_CONTEXT_KEY_VALUE_TYPE;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_CONTEXT_KEY_VALUE_TYPE_INTEGER` | Specifies an integer context key value type. |
| `ESP_CONTEXT_KEY_VALUE_TYPE_STRING` | Specifies a string context key value type. String context keys store a `ESP_UNICODE_STRING` structure. |
| `ESP_CONTEXT_KEY_VALUE_TYPE_BINARY` | Specifies a binary context key value type. Binary context keys store a byte blob. |
| `ESP_CONTEXT_KEY_VALUE_TYPE_BINDING_KEY` | Specifies a binding key value type. This is used with context updates to specify that the context key's value should be resolved to the binding key at rule evaluation time. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_CONTEXT_KEY_UPDATE_TYPE

The enum `ESP_CONTEXT_KEY_UPDATE_TYPE` defines a context key update type.

#### Syntax

```cpp
typedef enum ESP_CONTEXT_KEY_UPDATE_TYPE
{
    ESP_CONTEXT_KEY_UPDATE_TYPE_NONE = 0,
    ESP_CONTEXT_KEY_UPDATE_TYPE_CREATE,
    ESP_CONTEXT_KEY_UPDATE_TYPE_CREATE_OR_REPLACE,
    ESP_CONTEXT_KEY_UPDATE_TYPE_CREATE_IF_NOT_FOUND,
    ESP_CONTEXT_KEY_UPDATE_TYPE_REMOVE,
    ESP_CONTEXT_KEY_UPDATE_TYPE_MODIFY
} ESP_CONTEXT_KEY_UPDATE_TYPE;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_CONTEXT_KEY_UPDATE_TYPE_CREATE` | Creates a new context key. If the key already exists, the update fails. |
| `ESP_CONTEXT_KEY_UPDATE_TYPE_CREATE_OR_REPLACE` | Creates a new context key. If the key already exists, the existing key is replaced. |
| `ESP_CONTEXT_KEY_UPDATE_TYPE_CREATE_IF_NOT_FOUND` | Creates a new context key only if the key doesn't exist. |
| `ESP_CONTEXT_KEY_UPDATE_TYPE_REMOVE` | Removes an existing context key. If the context key doesn't exist, this is a no-op. |
| `ESP_CONTEXT_KEY_UPDATE_TYPE_MODIFY` | Modifies an existing context key. This is only supported for integer context key value types. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_CONTEXT_KEY_LIFETIME

The enum `ESP_CONTEXT_KEY_LIFETIME` defines a context key lifetime.

#### Syntax

```cpp
typedef enum ESP_CONTEXT_KEY_LIFETIME
{
    ESP_CONTEXT_KEY_LIFETIME_NONE = 0,
    ESP_CONTEXT_KEY_LIFETIME_CLIENT_SESSION,
    ESP_CONTEXT_KEY_LIFETIME_BOOT_SESSION
} ESP_CONTEXT_KEY_LIFETIME;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_CONTEXT_KEY_LIFETIME_CLIENT_SESSION` | The context key's lifetime is tied to the client's session. If the client disconnects, the context key is removed. |
| `ESP_CONTEXT_KEY_LIFETIME_BOOT_SESSION` | The context key's lifetime is tied to the boot session. If the client disconnects, the context key is preserved. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_CONTEXT_KEY_UPDATE_FLAGS

The enum `ESP_CONTEXT_KEY_UPDATE_FLAGS` specifies flags for a context update. No flags are currently supported.

#### Syntax

```cpp
typedef enum ESP_CONTEXT_KEY_UPDATE_FLAGS
{
    ESP_CONTEXT_KEY_UPDATE_FLAGS_NONE = 0x00000000
} ESP_CONTEXT_KEY_UPDATE_FLAGS;
```

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_CONTEXT_KEY_UPDATE

The structure `ESP_CONTEXT_KEY_UPDATE` describes a context key update.

#### Syntax

```cpp
typedef struct ESP_CONTEXT_KEY_UPDATE
{
    UINT32 ContextKey;
    ESP_CONTEXT_KEY_LIFETIME Lifetime;
    ESP_CONTEXT_KEY_UPDATE_TYPE UpdateType;
    ESP_CONTEXT_KEY_UPDATE_FLAGS Flags;
    ESP_NUMERICAL_TRANSFORM_TYPE TransformType;
    ESP_CONTEXT_KEY_VALUE_TYPE ValueType;

    union
    {
        UINT64 Integer;
        ESP_UNICODE_STRING String;
        ESP_BUFFER Binary;
        UINT64 BindingKey;
    } Value;
} ESP_CONTEXT_KEY_UPDATE;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ContextKey | Supplies the context key to update. |
| Lifetime | Specifies the lifetime of the context key. The supported values are:<br>Client Session: The context key's lifetime is tied to the client's lifetime. This means the context key is deleted once the client disconnects.<br>Boot Session: The context key's lifetime is tied to the boot session. So, if the client disconnects, the context key is preserved until the machine reboots.<br>Persisted: The context key will persist across boot sessions. This lifetime can currently only be used with stream event objects.<br>This parameter is ignored if the update type is "Remove" or "Modify". |
| UpdateType | The type of update to do. The supported types are:<br>Create: Creates a new context key. If the key already exists, the update fails.<br>Create or Replace: Creates a new context key. If the key already exists, the existing key is replaced.<br>Create If Not Found: Creates a new context key only if the key doesn't exist.<br>Remove: Removes an existing context key.<br>Modify: Modifies an existing context key. This is only supported for integer value types. |
| Flags | Specifies flags for the context key update. |
| TransformType | Supplies a numerical transform type to apply to an existing integer context key. This field must only be set if the update type is modify. |
| ValueType | Supplies the type for the value. The supported types are:<br>Integer<br>String<br>Binary<br>Binding Key<br>If the update type is "Remove", this parameter is ignored.<br>The "Binding Key" value type can be specified only as part of rule configuration through an `ESP_CONTEXT_KEY_CONFIG` structure. When the value type is binding key, the caller supplies a binding key through the "Value" field. During context updates, this value is substituted with the value resolved from the binding key.<br>For example, if the specified "Value" represents a binding key for the process command line, it is substituted with the process command line. For IDs that represent context keys, such as `ESP_THREAD_PROPERTY_ID_CONTEXT_KEY`, the binding key is substituted with the corresponding context key's value. |
| Value.Integer | Specifies the UINT64 value if the value type is `ESP_CONTEXT_KEY_VALUE_TYPE_INTEGER`. |
| Value.String | Specifies the `ESP_UNICODE_STRING` value if the value type is `ESP_CONTEXT_KEY_VALUE_TYPE_STRING`. |
| Value.Binary | Specifies the `ESP_BUFFER` value if the value type is `ESP_CONTEXT_KEY_VALUE_TYPE_BINARY`. |
| Value.BindingKey | Specifies the binding key value if the value type is `ESP_CONTEXT_KEY_VALUE_TYPE_BINDING_KEY`. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BUFFER`](wesp-common-utilities.md#esp_buffer)
- [`ESP_CONTEXT_KEY_LIFETIME`](wesp-context-key-management.md#esp_context_key_lifetime)
- [`ESP_CONTEXT_KEY_UPDATE_FLAGS`](wesp-context-key-management.md#esp_context_key_update_flags)
- [`ESP_CONTEXT_KEY_UPDATE_TYPE`](wesp-context-key-management.md#esp_context_key_update_type)
- [`ESP_CONTEXT_KEY_VALUE_TYPE`](wesp-context-key-management.md#esp_context_key_value_type)
- [`ESP_NUMERICAL_TRANSFORM_TYPE`](wesp-filter-comparison-types.md#esp_numerical_transform_type)
- [`ESP_UNICODE_STRING`](wesp-common-utilities.md#esp_unicode_string)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_CONTEXT_KEY_INFO

The structure `ESP_CONTEXT_KEY_INFO` stores context key information.

#### Syntax

```cpp
typedef struct ESP_CONTEXT_KEY_INFO
{
    UINT32 ContextKey;
    ESP_CONTEXT_KEY_LIFETIME Lifetime;
    ESP_CONTEXT_KEY_VALUE_TYPE ValueType;

    union
    {
        UINT64 Integer;
        ESP_UNICODE_STRING String;
        ESP_BUFFER Binary;
    } Value;
} ESP_CONTEXT_KEY_INFO;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ContextKey | Specifies the context key. |
| Lifetime | Specifies the lifetime of the context key. The supported values are:<br>Client Session: The context key's lifetime is tied to the client's lifetime.<br>Boot Session: The context key's lifetime is tied to the boot session. |
| ValueType | Specifies the value type. |
| Value.Integer | Specifies the value when the value type is `ESP_CONTEXT_KEY_VALUE_TYPE_INTEGER`. |
| Value.String | Specifies the value when the value type is `ESP_CONTEXT_KEY_VALUE_TYPE_STRING`. |
| Value.Binary | Specifies the value when the value type is `ESP_CONTEXT_KEY_VALUE_TYPE_BINARY`. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BUFFER`](wesp-common-utilities.md#esp_buffer)
- [`ESP_CONTEXT_KEY_LIFETIME`](wesp-context-key-management.md#esp_context_key_lifetime)
- [`ESP_CONTEXT_KEY_VALUE_TYPE`](wesp-context-key-management.md#esp_context_key_value_type)
- [`ESP_UNICODE_STRING`](wesp-common-utilities.md#esp_unicode_string)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_CONTEXT_KEY_CONFIG

The structure `ESP_CONTEXT_KEY_CONFIG` is used to set context key configuration.

#### Syntax

```cpp
typedef struct ESP_CONTEXT_KEY_CONFIG
{
    UINT32 UpdatesCount;
    _Field_size_(UpdatesCount) const ESP_CONTEXT_KEY_UPDATE* Updates;
} ESP_CONTEXT_KEY_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| UpdatesCount | Supplies the number of elements in the context updates array. |
| Updates | Supplies an array of context key updates. Note that the updates are guaranteed to be applied atomically. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_CONTEXT_KEY_UPDATE`](wesp-context-key-management.md#esp_context_key_update)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
