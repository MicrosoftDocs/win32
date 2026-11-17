---
title: "WESP context key property ID macros"
description: "Windows endpoint security platform API reference for context key property ID macros, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- ESP_EVENT_PROPERTY_ID_CONTEXT_KEY
- ESP_CLIENT_PROPERTY_ID_CONTEXT_KEY
- ESP_THREAD_PROPERTY_ID_CONTEXT_KEY
- ESP_PROCESS_PROPERTY_ID_CONTEXT_KEY
- ESP_FILE_STREAM_PROPERTY_ID_CONTEXT_KEY
- ESP_FILE_PROPERTY_ID_CONTEXT_KEY
- ESP_FILE_OBJECT_PROPERTY_ID_CONTEXT_KEY
- ESP_VOLUME_PROPERTY_ID_CONTEXT_KEY
- ESP_DISK_PROPERTY_ID_CONTEXT_KEY
- ESP_REGISTRY_KEY_PROPERTY_ID_CONTEXT_KEY
- ESP_REGISTRY_KEY_OBJECT_PROPERTY_ID_CONTEXT_KEY
- ESP_DESKTOP_PROPERTY_ID_CONTEXT_KEY
- ESP_KTM_TRANSACTION_PROPERTY_ID_CONTEXT_KEY
- ESP_PIPE_PROPERTY_ID_CONTEXT_KEY
- ESP_MAILSLOT_PROPERTY_ID_CONTEXT_KEY
- ESP_TOKEN_PROPERTY_ID_CONTEXT_KEY
---

# Context key property ID macros

This page contains reference entries in the [Context keys API family](wesp-api-reference.md#context-keys). Each entry includes its declaration and requirements.

## Property ID macros

### ESP_EVENT_PROPERTY_ID_CONTEXT_KEY

Builds a context-key property ID for the event property namespace.

#### Syntax

```cpp
#define ESP_EVENT_PROPERTY_ID_CONTEXT_KEY(key) ((ESP_EVENT_PROPERTY_ID)_esp_impl_PROPERTY_ID_CONTEXT_KEY(key))
```

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EVENT_PROPERTY_ID`](wesp-execution-property-ids.md#esp_event_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_CLIENT_PROPERTY_ID_CONTEXT_KEY

Builds a context-key property ID for the client property namespace.

#### Syntax

```cpp
#define ESP_CLIENT_PROPERTY_ID_CONTEXT_KEY(key) ((ESP_CLIENT_PROPERTY_ID)_esp_impl_PROPERTY_ID_CONTEXT_KEY(key))
```

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_CLIENT_PROPERTY_ID`](wesp-execution-property-ids.md#esp_client_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_THREAD_PROPERTY_ID_CONTEXT_KEY

Builds a context-key property ID for the thread property namespace.

#### Syntax

```cpp
#define ESP_THREAD_PROPERTY_ID_CONTEXT_KEY(key) ((ESP_THREAD_PROPERTY_ID)_esp_impl_PROPERTY_ID_CONTEXT_KEY(key))
```

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_THREAD_PROPERTY_ID`](wesp-execution-property-ids.md#esp_thread_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_PROCESS_PROPERTY_ID_CONTEXT_KEY

Builds a context-key property ID for the process property namespace.

#### Syntax

```cpp
#define ESP_PROCESS_PROPERTY_ID_CONTEXT_KEY(key) ((ESP_PROCESS_PROPERTY_ID)_esp_impl_PROPERTY_ID_CONTEXT_KEY(key))
```

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_PROCESS_PROPERTY_ID`](wesp-execution-property-ids.md#esp_process_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_FILE_STREAM_PROPERTY_ID_CONTEXT_KEY

Builds a context-key property ID for the file stream property namespace.

#### Syntax

```cpp
#define ESP_FILE_STREAM_PROPERTY_ID_CONTEXT_KEY(key) ((ESP_FILE_STREAM_PROPERTY_ID)_esp_impl_PROPERTY_ID_CONTEXT_KEY(key))
```

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_FILE_STREAM_PROPERTY_ID`](wesp-file-property-ids.md#esp_file_stream_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_FILE_PROPERTY_ID_CONTEXT_KEY

Builds a context-key property ID for the file property namespace.

#### Syntax

```cpp
#define ESP_FILE_PROPERTY_ID_CONTEXT_KEY(key) ((ESP_FILE_PROPERTY_ID)_esp_impl_PROPERTY_ID_CONTEXT_KEY(key))
```

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_FILE_PROPERTY_ID`](wesp-file-property-ids.md#esp_file_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_FILE_OBJECT_PROPERTY_ID_CONTEXT_KEY

Builds a context-key property ID for the file object property namespace.

#### Syntax

```cpp
#define ESP_FILE_OBJECT_PROPERTY_ID_CONTEXT_KEY(key) ((ESP_FILE_OBJECT_PROPERTY_ID)_esp_impl_PROPERTY_ID_CONTEXT_KEY(key))
```

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_FILE_OBJECT_PROPERTY_ID`](wesp-file-property-ids.md#esp_file_object_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_VOLUME_PROPERTY_ID_CONTEXT_KEY

Builds a context-key property ID for the volume property namespace.

#### Syntax

```cpp
#define ESP_VOLUME_PROPERTY_ID_CONTEXT_KEY(key) ((ESP_VOLUME_PROPERTY_ID)_esp_impl_PROPERTY_ID_CONTEXT_KEY(key))
```

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_VOLUME_PROPERTY_ID`](wesp-file-property-ids.md#esp_volume_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_DISK_PROPERTY_ID_CONTEXT_KEY

Builds a context-key property ID for the disk property namespace.

#### Syntax

```cpp
#define ESP_DISK_PROPERTY_ID_CONTEXT_KEY(key) ((ESP_DISK_PROPERTY_ID)_esp_impl_PROPERTY_ID_CONTEXT_KEY(key))
```

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_DISK_PROPERTY_ID`](wesp-file-property-ids.md#esp_disk_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_REGISTRY_KEY_PROPERTY_ID_CONTEXT_KEY

Builds a context-key property ID for the registry key property namespace.

#### Syntax

```cpp
#define ESP_REGISTRY_KEY_PROPERTY_ID_CONTEXT_KEY(key) ((ESP_REGISTRY_KEY_PROPERTY_ID)_esp_impl_PROPERTY_ID_CONTEXT_KEY(key))
```

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_REGISTRY_KEY_PROPERTY_ID`](wesp-other-property-ids.md#esp_registry_key_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_REGISTRY_KEY_OBJECT_PROPERTY_ID_CONTEXT_KEY

Builds a context-key property ID for the registry key object property namespace.

#### Syntax

```cpp
#define ESP_REGISTRY_KEY_OBJECT_PROPERTY_ID_CONTEXT_KEY(key) ((ESP_REGISTRY_KEY_OBJECT_PROPERTY_ID)_esp_impl_PROPERTY_ID_CONTEXT_KEY(key))
```

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_REGISTRY_KEY_OBJECT_PROPERTY_ID`](wesp-other-property-ids.md#esp_registry_key_object_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_DESKTOP_PROPERTY_ID_CONTEXT_KEY

Builds a context-key property ID for the desktop property namespace.

#### Syntax

```cpp
#define ESP_DESKTOP_PROPERTY_ID_CONTEXT_KEY(key) ((ESP_DESKTOP_PROPERTY_ID)_esp_impl_PROPERTY_ID_CONTEXT_KEY(key))
```

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_DESKTOP_PROPERTY_ID`](wesp-other-property-ids.md#esp_desktop_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_KTM_TRANSACTION_PROPERTY_ID_CONTEXT_KEY

Builds a context-key property ID for the ktm transaction property namespace.

#### Syntax

```cpp
#define ESP_KTM_TRANSACTION_PROPERTY_ID_CONTEXT_KEY(key) ((ESP_KTM_TRANSACTION_PROPERTY_ID)_esp_impl_PROPERTY_ID_CONTEXT_KEY(key))
```

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_KTM_TRANSACTION_PROPERTY_ID`](wesp-other-property-ids.md#esp_ktm_transaction_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_PIPE_PROPERTY_ID_CONTEXT_KEY

Builds a context-key property ID for the pipe property namespace.

#### Syntax

```cpp
#define ESP_PIPE_PROPERTY_ID_CONTEXT_KEY(key) ((ESP_PIPE_PROPERTY_ID)_esp_impl_PROPERTY_ID_CONTEXT_KEY(key))
```

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_PIPE_PROPERTY_ID`](wesp-other-property-ids.md#esp_pipe_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_MAILSLOT_PROPERTY_ID_CONTEXT_KEY

Builds a context-key property ID for the mailslot property namespace.

#### Syntax

```cpp
#define ESP_MAILSLOT_PROPERTY_ID_CONTEXT_KEY(key) ((ESP_MAILSLOT_PROPERTY_ID)_esp_impl_PROPERTY_ID_CONTEXT_KEY(key))
```

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_MAILSLOT_PROPERTY_ID`](wesp-other-property-ids.md#esp_mailslot_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_TOKEN_PROPERTY_ID_CONTEXT_KEY

Builds a context-key property ID for the token property namespace.

#### Syntax

```cpp
#define ESP_TOKEN_PROPERTY_ID_CONTEXT_KEY(key) ((ESP_TOKEN_PROPERTY_ID)_esp_impl_PROPERTY_ID_CONTEXT_KEY(key))
```

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_TOKEN_PROPERTY_ID`](wesp-execution-property-ids.md#esp_token_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
