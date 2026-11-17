---
title: "WESP pipe events"
description: "Windows endpoint security platform API reference for pipe events, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- ESP_PIPE_CREATE_CONFIG
- ESP_PIPE_CREATE_PARAMETERS
---

# Pipe events

This page contains reference entries in the [Events API family](wesp-api-reference.md#events). Each entry includes its declaration and requirements.

## Pipe creation

### ESP_PIPE_CREATE_CONFIG

The structure `ESP_PIPE_CREATE_CONFIG` is used to configure a pipe create event.

#### Syntax

```cpp
typedef struct ESP_PIPE_CREATE_CONFIG
{
    ESP_IO_OPERATION_CONFIG OperationConfig;
    ESP_PIPE_CONFIG PipeConfig;
    ESP_INTEGER_CONFIG DesiredAccessConfig;
    ESP_INTEGER_CONFIG CreateOptionsConfig;
    ESP_INTEGER_CONFIG ShareAccessConfig;
    ESP_INTEGER_CONFIG NamedPipeTypeConfig;
    ESP_INTEGER_CONFIG ReadModeConfig;
    ESP_ACCESS_STATE_CONFIG AccessStateConfig;
} ESP_PIPE_CREATE_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| OperationConfig | Specifies configuration for the IO operation. |
| PipeConfig | Specifies configuration for the pipe. |
| DesiredAccessConfig | Specifies configuration for the desired access. |
| CreateOptionsConfig | Specifies configuration for the create options. |
| ShareAccessConfig | Specifies configuration for the share access. |
| NamedPipeTypeConfig | Specifies configuration for the named pipe type. |
| ReadModeConfig | Specifies configuration for the read mode. |
| AccessStateConfig | Specifies configuration for the access state. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_ACCESS_STATE_CONFIG`](wesp-rule-value-configuration.md#esp_access_state_config)
- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_IO_OPERATION_CONFIG`](wesp-event-shared-types.md#esp_io_operation_config)
- [`ESP_PIPE_CONFIG`](wesp-other-event-objects.md#esp_pipe_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_PIPE_CREATE_PARAMETERS

The structure `ESP_PIPE_CREATE_PARAMETERS` contains the parameters associated with a pipe create event notification.

#### Syntax

```cpp
typedef struct ESP_PIPE_CREATE_PARAMETERS
{
    ESP_IO_OPERATION Operation;
    ESP_PIPE_INFO Pipe;
    ACCESS_MASK DesiredAccess;
    UINT32 CreateOptions;
    UINT16 ShareAccess;
    UINT32 NamedPipeType;
    UINT32 ReadMode;
    ESP_ACCESS_STATE AccessState;
} ESP_PIPE_CREATE_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Operation | The IO operation for the event. |
| Pipe | The pipe being created. |
| DesiredAccess | The ACCESS_MASK requested for the named pipe. |
| CreateOptions | The create options. This corresponds to the "CreateOptions" parameter of FltCreateNamedPipeFile. |
| ShareAccess | Bitmask of share access rights requested for the named pipe. |
| NamedPipeType | Type of named pipe to create. |
| ReadMode | Mode in which to read the pipe. |
| AccessState | An `ESP_ACCESS_STATE` structure which describes the state of the access in progress. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_ACCESS_STATE`](wesp-event-shared-types.md#esp_access_state)
- [`ESP_IO_OPERATION`](wesp-event-shared-types.md#esp_io_operation)
- [`ESP_PIPE_INFO`](wesp-other-event-objects.md#esp_pipe_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
