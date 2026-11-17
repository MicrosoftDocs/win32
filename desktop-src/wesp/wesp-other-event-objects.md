---
title: "WESP registry and other event objects"
description: "Windows endpoint security platform API reference for registry and other event objects, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- EspCreateRegistryKeyReference
- ESP_REGISTRY_KEY_CONFIG_FLAGS
- ESP_REGISTRY_KEY_CONFIG
- ESP_REGISTRY_KEY_INFO
- ESP_REGISTRY_KEY_OBJECT_CONFIG_FLAGS
- ESP_REGISTRY_KEY_OBJECT_CONFIG
- ESP_REGISTRY_KEY_OBJECT_INFO
- EspCreateDesktopReference
- ESP_DESKTOP_CONFIG_FLAGS
- ESP_DESKTOP_CONFIG
- ESP_DESKTOP_INFO
- ESP_KTM_TRANSACTION_CONFIG_FLAGS
- ESP_KTM_TRANSACTION_CONFIG
- ESP_KTM_TRANSACTION_INFO
- EspCreatePipeReference
- ESP_PIPE_CONFIG_FLAGS
- ESP_PIPE_CONFIG
- ESP_PIPE_INFO
- EspCreateMailslotReference
- ESP_MAILSLOT_CONFIG_FLAGS
- ESP_MAILSLOT_CONFIG
- ESP_MAILSLOT_INFO
---

# Registry and other event objects

This page contains reference entries in the [Event objects API family](wesp-api-reference.md#event-objects). Each entry includes its declaration and requirements.

## Registry key

### EspCreateRegistryKeyReference

The API `EspCreateRegistryKeyReference` creates an event object reference to an existing registry key. This is useful in cases where a client needs to reference a registry key outside the context of an event involving the registry key. For example, a client may require a reference to a registry key to query properties or set event object context.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateRegistryKeyReference(
    _In_ ESP_CLIENT Client,
    _In_ const ESP_PATH* KeyPath,
    _Out_ ESP_EVENT_OBJECT_REF* ObjectRef
    );
```

#### Parameters

##### `Client`

Supplies the client.

##### `KeyPath`

Supplies the registry key's path.

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

### ESP_REGISTRY_KEY_CONFIG_FLAGS

The enum `ESP_REGISTRY_KEY_CONFIG_FLAGS` specifies flags for an `ESP_REGISTRY_KEY_CONFIG` structure. There are currently no supported flags.

#### Syntax

```cpp
typedef enum ESP_REGISTRY_KEY_CONFIG_FLAGS
{
    ESP_REGISTRY_KEY_CONFIG_FLAGS_NONE = 0x00000000
} ESP_REGISTRY_KEY_CONFIG_FLAGS;
```

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_REGISTRY_KEY_CONFIG`](wesp-other-event-objects.md#esp_registry_key_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_REGISTRY_KEY_CONFIG

The configuration structure for a registry key event object is `ESP_REGISTRY_KEY_CONFIG`.

#### Syntax

```cpp
typedef struct ESP_REGISTRY_KEY_CONFIG
{
    ESP_REGISTRY_KEY_CONFIG_FLAGS Flags;
    ESP_EVENT_OBJECT_CONFIG EventObjectConfig;

    UINT32 PropertiesCount;
    _Field_size_(PropertiesCount) const ESP_REGISTRY_KEY_PROPERTY_ID* Properties;
} ESP_REGISTRY_KEY_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Flags | Specifies flags for the registry key. |
| EventObjectConfig | Supplies event object configuration for the registry key. |
| PropertiesCount | Supplies the number of elements in the "Properties" array. |
| Properties | Supplies an array of registry key properties that should be captured for the registry key. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EVENT_OBJECT_CONFIG`](wesp-event-object-references.md#esp_event_object_config)
- [`ESP_REGISTRY_KEY_CONFIG_FLAGS`](wesp-other-event-objects.md#esp_registry_key_config_flags)
- [`ESP_REGISTRY_KEY_PROPERTY_ID`](wesp-other-property-ids.md#esp_registry_key_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_REGISTRY_KEY_INFO

The structure `ESP_REGISTRY_KEY_INFO` specifies information for a registry key. This structure is supplied as part of an event notification (one for each registry key associated with an event) and contains various details about the registry key.

#### Syntax

```cpp
typedef struct ESP_REGISTRY_KEY_INFO
{
    ESP_EVENT_OBJECT_INFO ObjectInfo;
} ESP_REGISTRY_KEY_INFO;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ObjectInfo | Specifies information about the registry key's event object. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EVENT_OBJECT_INFO`](wesp-event-object-references.md#esp_event_object_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Registry key object

### ESP_REGISTRY_KEY_OBJECT_CONFIG_FLAGS

The enum `ESP_REGISTRY_KEY_OBJECT_CONFIG_FLAGS` specifies flags for an `ESP_REGISTRY_KEY_OBJECT_CONFIG` structure. There are currently no supported flags.

#### Syntax

```cpp
typedef enum ESP_REGISTRY_KEY_OBJECT_CONFIG_FLAGS
{
    ESP_REGISTRY_KEY_OBJECT_CONFIG_FLAGS_NONE = 0x00000000
} ESP_REGISTRY_KEY_OBJECT_CONFIG_FLAGS;
```

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_REGISTRY_KEY_OBJECT_CONFIG`](wesp-other-event-objects.md#esp_registry_key_object_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_REGISTRY_KEY_OBJECT_CONFIG

The configuration structure for a registry key object event object is `ESP_REGISTRY_KEY_OBJECT_CONFIG`.

#### Syntax

```cpp
typedef struct ESP_REGISTRY_KEY_OBJECT_CONFIG
{
    ESP_REGISTRY_KEY_OBJECT_CONFIG_FLAGS Flags;
    ESP_EVENT_OBJECT_CONFIG EventObjectConfig;

    UINT32 PropertiesCount;
    _Field_size_(PropertiesCount) const ESP_REGISTRY_KEY_OBJECT_PROPERTY_ID* Properties;

    ESP_REGISTRY_KEY_CONFIG RegistryKeyConfig;
    ESP_KTM_TRANSACTION_CONFIG TransactionConfig;
} ESP_REGISTRY_KEY_OBJECT_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Flags | Specifies flags for the registry key object. |
| EventObjectConfig | Supplies event object configuration for the registry key object. |
| PropertiesCount | Supplies the number of elements in the "Properties" array. |
| Properties | Supplies an array of registry key object properties that should be captured for the registry key object. |
| RegistryKeyConfig | Supplies a configuration structure for the registry key object's registry key. |
| TransactionConfig | Supplies a configuration structure for the registry key object's transaction. Note that if the registry key object is not part of a transaction, transaction properties won't be retrieved if the rule matches. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EVENT_OBJECT_CONFIG`](wesp-event-object-references.md#esp_event_object_config)
- [`ESP_KTM_TRANSACTION_CONFIG`](wesp-other-event-objects.md#esp_ktm_transaction_config)
- [`ESP_REGISTRY_KEY_CONFIG`](wesp-other-event-objects.md#esp_registry_key_config)
- [`ESP_REGISTRY_KEY_OBJECT_CONFIG_FLAGS`](wesp-other-event-objects.md#esp_registry_key_object_config_flags)
- [`ESP_REGISTRY_KEY_OBJECT_PROPERTY_ID`](wesp-other-property-ids.md#esp_registry_key_object_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_REGISTRY_KEY_OBJECT_INFO

The structure `ESP_REGISTRY_KEY_OBJECT_INFO` specifies information for a registry key object. This structure is supplied as part of an event notification (one for each registry key object associated with an event) and contains various details about the registry key object.

#### Syntax

```cpp
typedef struct ESP_REGISTRY_KEY_OBJECT_INFO
{
    ESP_EVENT_OBJECT_INFO ObjectInfo;
    _Maybenull_ const ESP_REGISTRY_KEY_INFO* RegistryKeyInfo;
    _Maybenull_ const ESP_KTM_TRANSACTION_INFO* TransactionInfo;
} ESP_REGISTRY_KEY_OBJECT_INFO;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ObjectInfo | Specifies information about the registry key object's event object. |
| RegistryKeyInfo | Specifies information about the registry key object's registry key. This field may be null if the client didn't specify registry key configuration through the "RegistryKeyConfig" field in `ESP_REGISTRY_KEY_OBJECT_CONFIG`. |
| TransactionInfo | Specifies information about the registry key object's KTM transaction. This field may be null if the client didn't specify KTM transaction configuration through the "TransactionConfig" field in `ESP_REGISTRY_KEY_OBJECT_CONFIG`. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EVENT_OBJECT_INFO`](wesp-event-object-references.md#esp_event_object_info)
- [`ESP_KTM_TRANSACTION_INFO`](wesp-other-event-objects.md#esp_ktm_transaction_info)
- [`ESP_REGISTRY_KEY_INFO`](wesp-other-event-objects.md#esp_registry_key_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Desktop

### EspCreateDesktopReference

The API `EspCreateDesktopReference` creates an event object reference to an existing desktop. This is useful in cases where a client needs to reference a desktop outside the context of an event involving the desktop. For example, a client may require a reference to a desktop to query properties or set event object context.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateDesktopReference(
    _In_ ESP_CLIENT Client,
    _In_ PCWSTR DesktopName,
    _Out_ ESP_EVENT_OBJECT_REF* ObjectRef
    );
```

#### Parameters

##### `Client`

Supplies the client.

##### `DesktopName`

Supplies the desktop's name.

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

### ESP_DESKTOP_CONFIG_FLAGS

The enum `ESP_DESKTOP_CONFIG_FLAGS` specifies flags for an `ESP_DESKTOP_CONFIG` structure. There are currently no supported flags.

#### Syntax

```cpp
typedef enum ESP_DESKTOP_CONFIG_FLAGS
{
    ESP_DESKTOP_CONFIG_FLAGS_NONE = 0x00000000
} ESP_DESKTOP_CONFIG_FLAGS;
```

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_DESKTOP_CONFIG`](wesp-other-event-objects.md#esp_desktop_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_DESKTOP_CONFIG

The configuration structure for a desktop event object is `ESP_DESKTOP_CONFIG`.

#### Syntax

```cpp
typedef struct ESP_DESKTOP_CONFIG
{
    ESP_DESKTOP_CONFIG_FLAGS Flags;
    ESP_EVENT_OBJECT_CONFIG EventObjectConfig;

    UINT32 PropertiesCount;
    _Field_size_(PropertiesCount) const ESP_DESKTOP_PROPERTY_ID* Properties;
} ESP_DESKTOP_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Flags | Specifies flags for the desktop. |
| EventObjectConfig | Supplies event object configuration for the desktop. |
| PropertiesCount | Supplies the number of elements in the "Properties" array. |
| Properties | Supplies an array of desktop properties that should be captured for the desktop. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_DESKTOP_CONFIG_FLAGS`](wesp-other-event-objects.md#esp_desktop_config_flags)
- [`ESP_DESKTOP_PROPERTY_ID`](wesp-other-property-ids.md#esp_desktop_property_id)
- [`ESP_EVENT_OBJECT_CONFIG`](wesp-event-object-references.md#esp_event_object_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_DESKTOP_INFO

The structure `ESP_DESKTOP_INFO` specifies information for a desktop. This structure is supplied as part of an event notification (one for each desktop associated with an event) and contains various details about the desktop.

#### Syntax

```cpp
typedef struct ESP_DESKTOP_INFO
{
    ESP_EVENT_OBJECT_INFO ObjectInfo;
} ESP_DESKTOP_INFO;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ObjectInfo | Specifies information about the desktop's event object. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EVENT_OBJECT_INFO`](wesp-event-object-references.md#esp_event_object_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## KTM transaction

### ESP_KTM_TRANSACTION_CONFIG_FLAGS

The enum `ESP_KTM_TRANSACTION_CONFIG_FLAGS` specifies flags for an `ESP_KTM_TRANSACTION_CONFIG` structure.

#### Syntax

```cpp
typedef enum ESP_KTM_TRANSACTION_CONFIG_FLAGS
{
    ESP_KTM_TRANSACTION_CONFIG_FLAGS_NONE                  = 0x00000000,
    ESP_KTM_TRANSACTION_CONFIG_FLAGS_SKIP_IF_OBJECT_ABSENT = 0x00000001
} ESP_KTM_TRANSACTION_CONFIG_FLAGS;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_KTM_TRANSACTION_CONFIG_FLAGS_SKIP_IF_OBJECT_ABSENT` | Specifies to skip applying the configuration if the KTM transaction doesn't exist. For example, if a client sets this flag for a file object's KTM transaction and the file object is not transacted, the KTM transaction configuration won't be applied.<br>If the KTM transaction is absent, this flag implicitly evaluates the KTM transaction's filter to true. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_KTM_TRANSACTION_CONFIG`](wesp-other-event-objects.md#esp_ktm_transaction_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_KTM_TRANSACTION_CONFIG

The configuration structure for a KTM transaction event object is `ESP_KTM_TRANSACTION_CONFIG`.

#### Syntax

```cpp
typedef struct ESP_KTM_TRANSACTION_CONFIG
{
    ESP_KTM_TRANSACTION_CONFIG_FLAGS Flags;
    ESP_EVENT_OBJECT_CONFIG EventObjectConfig;

    UINT32 PropertiesCount;
    _Field_size_(PropertiesCount) const ESP_KTM_TRANSACTION_PROPERTY_ID* Properties;
} ESP_KTM_TRANSACTION_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Flags | Specifies flags for the KTM transaction. |
| EventObjectConfig | Supplies event object configuration for the KTM transaction. |
| PropertiesCount | Supplies the number of elements in the "Properties" array. |
| Properties | Supplies an array of KTM transaction properties that should be captured for the KTM transaction. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EVENT_OBJECT_CONFIG`](wesp-event-object-references.md#esp_event_object_config)
- [`ESP_KTM_TRANSACTION_CONFIG_FLAGS`](wesp-other-event-objects.md#esp_ktm_transaction_config_flags)
- [`ESP_KTM_TRANSACTION_PROPERTY_ID`](wesp-other-property-ids.md#esp_ktm_transaction_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_KTM_TRANSACTION_INFO

The structure `ESP_KTM_TRANSACTION_INFO` specifies information for a KTM transaction. This structure is supplied as part of an event notification (one for each KTM transaction associated with an event) and contains various details about the KTM transaction.

#### Syntax

```cpp
typedef struct ESP_KTM_TRANSACTION_INFO
{
    ESP_EVENT_OBJECT_INFO ObjectInfo;
} ESP_KTM_TRANSACTION_INFO;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ObjectInfo | Specifies information about the KTM transaction's event object. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EVENT_OBJECT_INFO`](wesp-event-object-references.md#esp_event_object_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Pipe

### EspCreatePipeReference

The API `EspCreatePipeReference` creates an event object reference to an existing pipe. This is useful in cases where a client needs to reference a pipe outside the context of an event involving the pipe. For example, a client may require a reference to a pipe to query properties or set event object context.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreatePipeReference(
    _In_ ESP_CLIENT Client,
    _In_ const ESP_PATH* PipePath,
    _Out_ ESP_EVENT_OBJECT_REF* ObjectRef
    );
```

#### Parameters

##### `Client`

Supplies the client.

##### `PipePath`

Supplies the pipe path (e.g. \\.\pipe\Foo).

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

### ESP_PIPE_CONFIG_FLAGS

The enum `ESP_PIPE_CONFIG_FLAGS` specifies flags for an `ESP_PIPE_CONFIG` structure. There are currently no supported flags.

#### Syntax

```cpp
typedef enum ESP_PIPE_CONFIG_FLAGS
{
    ESP_PIPE_CONFIG_FLAGS_NONE = 0x00000000
} ESP_PIPE_CONFIG_FLAGS;
```

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_PIPE_CONFIG`](wesp-other-event-objects.md#esp_pipe_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_PIPE_CONFIG

The configuration structure for a pipe event object is `ESP_PIPE_CONFIG`.

#### Syntax

```cpp
typedef struct ESP_PIPE_CONFIG
{
    ESP_PIPE_CONFIG_FLAGS Flags;
    ESP_EVENT_OBJECT_CONFIG EventObjectConfig;

    UINT32 PropertiesCount;
    _Field_size_(PropertiesCount) const ESP_PIPE_PROPERTY_ID* Properties;
} ESP_PIPE_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Flags | Specifies flags for the pipe. |
| EventObjectConfig | Supplies event object configuration for the pipe. |
| PropertiesCount | Supplies the number of elements in the "Properties" array. |
| Properties | Supplies an array of pipe properties that should be captured for the pipe. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EVENT_OBJECT_CONFIG`](wesp-event-object-references.md#esp_event_object_config)
- [`ESP_PIPE_CONFIG_FLAGS`](wesp-other-event-objects.md#esp_pipe_config_flags)
- [`ESP_PIPE_PROPERTY_ID`](wesp-other-property-ids.md#esp_pipe_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_PIPE_INFO

The structure `ESP_PIPE_INFO` specifies information for a pipe. This structure is supplied as part of an event notification (one for each pipe associated with an event) and contains various details about the pipe.

#### Syntax

```cpp
typedef struct ESP_PIPE_INFO
{
    ESP_EVENT_OBJECT_INFO ObjectInfo;
} ESP_PIPE_INFO;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ObjectInfo | Specifies information about the pipe's event object. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EVENT_OBJECT_INFO`](wesp-event-object-references.md#esp_event_object_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Mailslot

### EspCreateMailslotReference

The API `EspCreateMailslotReference` creates an event object reference to an existing mailslot. This is useful in cases where a client needs to reference a mailslot outside the context of an event involving the mailslot. For example, a client may require a reference to a mailslot to query properties or set event object context.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateMailslotReference(
    _In_ ESP_CLIENT Client,
    _In_ const ESP_PATH* MailslotPath,
    _Out_ ESP_EVENT_OBJECT_REF* ObjectRef
    );
```

#### Parameters

##### `Client`

Supplies the client.

##### `MailslotPath`

Supplies the mailslot path (e.g. \\.\mailslot\Foo).

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

### ESP_MAILSLOT_CONFIG_FLAGS

The enum `ESP_MAILSLOT_CONFIG_FLAGS` specifies flags for an `ESP_MAILSLOT_CONFIG` structure. There are currently no supported flags.

#### Syntax

```cpp
typedef enum ESP_MAILSLOT_CONFIG_FLAGS
{
    ESP_MAILSLOT_CONFIG_FLAGS_NONE = 0x00000000
} ESP_MAILSLOT_CONFIG_FLAGS;
```

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_MAILSLOT_CONFIG`](wesp-other-event-objects.md#esp_mailslot_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_MAILSLOT_CONFIG

The configuration structure for a mailslot event object is `ESP_MAILSLOT_CONFIG`.

#### Syntax

```cpp
typedef struct ESP_MAILSLOT_CONFIG
{
    ESP_MAILSLOT_CONFIG_FLAGS Flags;
    ESP_EVENT_OBJECT_CONFIG EventObjectConfig;

    UINT32 PropertiesCount;
    _Field_size_(PropertiesCount) const ESP_MAILSLOT_PROPERTY_ID* Properties;
} ESP_MAILSLOT_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Flags | Specifies flags for the mailslot. |
| EventObjectConfig | Supplies event object configuration for the mailslot. |
| PropertiesCount | Supplies the number of elements in the "Properties" array. |
| Properties | Supplies an array of mailslot properties that should be captured for the mailslot. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EVENT_OBJECT_CONFIG`](wesp-event-object-references.md#esp_event_object_config)
- [`ESP_MAILSLOT_CONFIG_FLAGS`](wesp-other-event-objects.md#esp_mailslot_config_flags)
- [`ESP_MAILSLOT_PROPERTY_ID`](wesp-other-property-ids.md#esp_mailslot_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_MAILSLOT_INFO

The structure `ESP_MAILSLOT_INFO` specifies information for a mailslot. This structure is supplied as part of an event notification (one for each mailslot associated with an event) and contains various details about the mailslot.

#### Syntax

```cpp
typedef struct ESP_MAILSLOT_INFO
{
    ESP_EVENT_OBJECT_INFO ObjectInfo;
} ESP_MAILSLOT_INFO;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ObjectInfo | Specifies information about the mailslot's event object. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EVENT_OBJECT_INFO`](wesp-event-object-references.md#esp_event_object_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
