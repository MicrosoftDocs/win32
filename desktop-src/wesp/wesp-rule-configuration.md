---
title: "WESP rule configuration and property bindings"
description: "Windows endpoint security platform API reference for rule configuration and property bindings, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- ESP_RULE_CONFIG_EXTENSION_TYPE
- ESP_BINDING_KEY_DATA_TYPE
- ESP_RULE_CONFIG
- ESP_RULE_CONFIG_EXTENSION
- ESP_EVENT_CONFIG
- ESP_PROPERTY_BINDING
---

# Rule configuration and property bindings

This page contains reference entries in the [Rules API family](wesp-api-reference.md#rules). Each entry includes its declaration and requirements.

## Rule configuration

### ESP_RULE_CONFIG_EXTENSION_TYPE

Identifies the type of a rule configuration extension.

#### Syntax

```cpp
typedef enum ESP_RULE_CONFIG_EXTENSION_TYPE
{
    ESP_RULE_CONFIG_EXTENSION_TYPE_NONE = 0
} ESP_RULE_CONFIG_EXTENSION_TYPE;
```

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_BINDING_KEY_DATA_TYPE

The enum `ESP_BINDING_KEY_DATA_TYPE` defines the different data types a binding key can resolve as.

#### Syntax

```cpp
typedef enum ESP_BINDING_KEY_DATA_TYPE
{
    ESP_BINDING_KEY_DATA_TYPE_NONE = 0,
    ESP_BINDING_KEY_DATA_TYPE_INTEGER,
    ESP_BINDING_KEY_DATA_TYPE_STRING,
    ESP_BINDING_KEY_DATA_TYPE_BINARY
} ESP_BINDING_KEY_DATA_TYPE;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_BINDING_KEY_DATA_TYPE_INTEGER` | The binding key's data type is an integer (i.e. UINT64). |
| `ESP_BINDING_KEY_DATA_TYPE_STRING` | The binding key's data type is string (i.e. `ESP_UNICODE_STRING`). |
| `ESP_BINDING_KEY_DATA_TYPE_BINARY` | The binding key's data type is binary. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_RULE_CONFIG

The structure `ESP_RULE_CONFIG` describes configuration for a rule.

#### Syntax

```cpp
typedef struct ESP_RULE_CONFIG
{
    ESP_EVENT_CONFIG EventConfig;
    ESP_CLIENT_CONFIG ClientConfig;
    ESP_THREAD_CONFIG CurrentThreadConfig;
    ESP_PROCESS_CONFIG CurrentProcessConfig;
    UINT32 ExtensionsCount;
    _Field_size_(ExtensionsCount) const ESP_RULE_CONFIG_EXTENSION* Extensions;
} ESP_RULE_CONFIG;
```

#### Members

| PARAMETER | DESCRIPTION |
| --- | --- |
| EventConfig | Supplies a configuration structure for the event. |
| ClientConfig | Supplies a configuration structure for the client. |
| CurrentThreadConfig | Specifies a configuration structure for the current thread. This structure can be used to configure the thread equivalent to PsGetCurrentThread. |
| CurrentProcessConfig | Specifies a configuration structure for the current process. This structure can be used to configure the process equivalent to PsGetCurrentProcess. |
| ExtensionsCount | The number of elements in the Extensions array. |
| Extensions | The array of `ESP_RULE_CONFIG_EXTENSION` structures. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_CLIENT_CONFIG`](wesp-clients.md#esp_client_config)
- [`ESP_EVENT_CONFIG`](wesp-rule-configuration.md#esp_event_config)
- [`ESP_PROCESS_CONFIG`](wesp-execution-objects.md#esp_process_config)
- [`ESP_RULE_CONFIG_EXTENSION`](wesp-rule-configuration.md#esp_rule_config_extension)
- [`ESP_THREAD_CONFIG`](wesp-execution-objects.md#esp_thread_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_RULE_CONFIG_EXTENSION

Describes an extension to a WESP rule configuration.

#### Syntax

```cpp
typedef struct ESP_RULE_CONFIG_EXTENSION
{
    ESP_RULE_CONFIG_EXTENSION_TYPE Type;
    const void* Extension;
} ESP_RULE_CONFIG_EXTENSION;
```

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_RULE_CONFIG_EXTENSION_TYPE`](wesp-rule-configuration.md#esp_rule_config_extension_type)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_EVENT_CONFIG

The structure `ESP_EVENT_CONFIG` is used to set event configuration for a rule.

#### Syntax

```cpp
typedef struct ESP_EVENT_CONFIG
{
    ESP_FILTER Filter;
    ESP_CONTEXT_KEY_CONFIG ContextConfig;

    UINT32 PropertiesCount;
    _Field_size_(PropertiesCount) const ESP_EVENT_PROPERTY_ID* Properties;

    UINT32 BindingsCount;
    _Field_size_(BindingsCount) const ESP_PROPERTY_BINDING* Bindings;

    const void* EventTypeConfig;
} ESP_EVENT_CONFIG;
```

#### Members

| PARAMETER | DESCRIPTION |
| --- | --- |
| Filter | Supplies an event filter. An event filter is created by calling `EspCreateEventFilter`. |
| ContextConfig | Supplies an `ESP_CONTEXT_KEY_CONFIG` structure. This structure can be used to configure context key updates and capture binding keys for the event. |
| PropertiesCount | Supplies the number of elements in the "Properties" array. |
| Properties | Supplies an array of event properties that should be captured for the event. |
| BindingsCount | Supplies the number of elements in the bindings array. |
| Bindings | Supplies an array of event property bindings. This allows the client to configure binding keys for various properties. |
| EventTypeConfig | Specifies a pointer to the event type's configuration structure. Each event type uses its own distinct configuration structure. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_CONTEXT_KEY_CONFIG`](wesp-context-key-management.md#esp_context_key_config)
- [`ESP_EVENT_PROPERTY_ID`](wesp-execution-property-ids.md#esp_event_property_id)
- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [`ESP_PROPERTY_BINDING`](wesp-rule-configuration.md#esp_property_binding)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_PROPERTY_BINDING

The structure `ESP_PROPERTY_BINDING` stores a binding key configuration for a property.

#### Syntax

```cpp
typedef struct ESP_PROPERTY_BINDING
{
    UINT32 PropertyId;
    UINT64 BindingKey;
} ESP_PROPERTY_BINDING;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| PropertyId | Specifies the property ID. |
| BindingKey | Specifies the binding key for the property. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)
