---
title: "WESP mailslot events"
description: "Windows endpoint security platform API reference for mailslot events, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- ESP_MAILSLOT_CREATE_CONFIG
- ESP_MAILSLOT_CREATE_PARAMETERS
---

# Mailslot events

This page contains reference entries in the [Events API family](wesp-api-reference.md#events). Each entry includes its declaration and requirements.

## Mailslot creation

### ESP_MAILSLOT_CREATE_CONFIG

The structure `ESP_MAILSLOT_CREATE_CONFIG` is used to configure a mailslot create event.

#### Syntax

```cpp
typedef struct ESP_MAILSLOT_CREATE_CONFIG
{
    ESP_IO_OPERATION_CONFIG OperationConfig;
    ESP_MAILSLOT_CONFIG MailslotConfig;
    ESP_INTEGER_CONFIG DesiredAccessConfig;
    ESP_INTEGER_CONFIG CreateOptionsConfig;
    ESP_INTEGER_CONFIG ShareAccessConfig;
    ESP_ACCESS_STATE_CONFIG AccessStateConfig;
} ESP_MAILSLOT_CREATE_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| OperationConfig | Specifies configuration for the IO operation. |
| MailslotConfig | Specifies configuration for the mailslot. |
| DesiredAccessConfig | Specifies configuration for the desired access. |
| CreateOptionsConfig | Specifies configuration for the create options. |
| ShareAccessConfig | Specifies configuration for the share access. |
| AccessStateConfig | Specifies configuration for the access state. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_ACCESS_STATE_CONFIG`](wesp-rule-value-configuration.md#esp_access_state_config)
- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_IO_OPERATION_CONFIG`](wesp-event-shared-types.md#esp_io_operation_config)
- [`ESP_MAILSLOT_CONFIG`](wesp-other-event-objects.md#esp_mailslot_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_MAILSLOT_CREATE_PARAMETERS

The structure `ESP_MAILSLOT_CREATE_PARAMETERS` contains the parameters associated with a mailslot create event notification.

#### Syntax

```cpp
typedef struct ESP_MAILSLOT_CREATE_PARAMETERS
{
    ESP_IO_OPERATION Operation;
    ESP_MAILSLOT_INFO Mailslot;
    ACCESS_MASK DesiredAccess;
    UINT32 CreateOptions;
    UINT16 ShareAccess;
    ESP_ACCESS_STATE AccessState;
} ESP_MAILSLOT_CREATE_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Operation | The IO operation for the event. |
| Mailslot | The mail slot. |
| DesiredAccess | The ACCESS_MASK requested for the mail slot. |
| CreateOptions | The create options. This corresponds to the "CreateOptions" parameter of FltCreateMailslotFile. |
| ShareAccess | Bitmask of share access rights requested for the mailslot. |
| AccessState | An `ESP_ACCESS_STATE` structure which describes the state of the access in progress. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_ACCESS_STATE`](wesp-event-shared-types.md#esp_access_state)
- [`ESP_IO_OPERATION`](wesp-event-shared-types.md#esp_io_operation)
- [`ESP_MAILSLOT_INFO`](wesp-other-event-objects.md#esp_mailslot_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
