---
title: "WESP thread events"
description: "Windows endpoint security platform API reference for thread events, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- ESP_THREAD_CREATE_FLAGS
- ESP_THREAD_CREATE_CONFIG
- ESP_THREAD_CREATE_PARAMETERS
- ESP_THREAD_START_CONFIG
- ESP_THREAD_START_PARAMETERS
- ESP_THREAD_TERMINATE_CONFIG
- ESP_THREAD_TERMINATE_PARAMETERS
---

# Thread events

This page contains reference entries in the [Events API family](wesp-api-reference.md#events). Each entry includes its declaration and requirements.

## Thread creation

### ESP_THREAD_CREATE_FLAGS

The enum `ESP_THREAD_CREATE_FLAGS` defines flags for the thread create event.

#### Syntax

```cpp
typedef enum ESP_THREAD_CREATE_FLAGS
{
    ESP_THREAD_CREATE_FLAGS_NONE   = 0x00000000,
    ESP_THREAD_CREATE_FLAGS_REMOTE = 0x00000001
} ESP_THREAD_CREATE_FLAGS;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_THREAD_CREATE_FLAGS_REMOTE` | The thread was created as a remote thread (e.g. using the API CreateRemoteThread). |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_THREAD_CREATE_CONFIG

The structure `ESP_THREAD_CREATE_CONFIG` is used to configure a thread create event.

#### Syntax

```cpp
typedef struct ESP_THREAD_CREATE_CONFIG
{
    ESP_THREAD_CONFIG ThreadConfig;
    ESP_INTEGER_CONFIG FlagsConfig;
} ESP_THREAD_CREATE_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ThreadConfig | Specifies configuration for the thread being created. |
| FlagsConfig | Specifies configuration for the flags. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_THREAD_CONFIG`](wesp-execution-objects.md#esp_thread_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_THREAD_CREATE_PARAMETERS

The structure `ESP_THREAD_CREATE_PARAMETERS` contains the parameters associated with a thread create event notification.

#### Syntax

```cpp
typedef struct ESP_THREAD_CREATE_PARAMETERS
{
    ESP_THREAD_INFO Thread;
    ESP_THREAD_CREATE_FLAGS Flags;
} ESP_THREAD_CREATE_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Thread | The thread that is being created. |
| Flags | Flags for the thread create event. The supported flags are:<br>RemoteThread: Indicates the thread is a remote thread. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_THREAD_CREATE_FLAGS`](wesp-thread-events.md#esp_thread_create_flags)
- [`ESP_THREAD_INFO`](wesp-execution-objects.md#esp_thread_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Thread start

### ESP_THREAD_START_CONFIG

The structure `ESP_THREAD_START_CONFIG` is used to configure a thread start event.

#### Syntax

```cpp
typedef struct ESP_THREAD_START_CONFIG
{
    ESP_THREAD_CONFIG ThreadConfig;
} ESP_THREAD_START_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ThreadConfig | Specifies configuration for the thread being started. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_THREAD_CONFIG`](wesp-execution-objects.md#esp_thread_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_THREAD_START_PARAMETERS

The structure `ESP_THREAD_START_PARAMETERS` contains the parameters associated with a thread start event notification.

#### Syntax

```cpp
typedef struct ESP_THREAD_START_PARAMETERS
{
    ESP_THREAD_INFO Thread;
} ESP_THREAD_START_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Thread | The thread that is being started. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_THREAD_INFO`](wesp-execution-objects.md#esp_thread_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Thread termination

### ESP_THREAD_TERMINATE_CONFIG

The structure `ESP_THREAD_TERMINATE_CONFIG` is used to configure a thread terminate event.

#### Syntax

```cpp
typedef struct ESP_THREAD_TERMINATE_CONFIG
{
    ESP_THREAD_CONFIG ThreadConfig;
} ESP_THREAD_TERMINATE_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ThreadConfig | Specifies configuration for the thread being terminated. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_THREAD_CONFIG`](wesp-execution-objects.md#esp_thread_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_THREAD_TERMINATE_PARAMETERS

The structure `ESP_THREAD_TERMINATE_PARAMETERS` contains the parameters associated with a thread terminate event notification.

#### Syntax

```cpp
typedef struct ESP_THREAD_TERMINATE_PARAMETERS
{
    ESP_THREAD_INFO Thread;
} ESP_THREAD_TERMINATE_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Thread | The thread that is being terminated. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_THREAD_INFO`](wesp-execution-objects.md#esp_thread_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
