---
title: "WESP volume events"
description: "Windows endpoint security platform API reference for volume events, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- ESP_VOLUME_MOUNT_CONFIG
- ESP_VOLUME_MOUNT_PARAMETERS
- ESP_VOLUME_DISMOUNT_CONFIG
- ESP_VOLUME_DISMOUNT_PARAMETERS
- ESP_VOLUME_FSCTL_CONFIG
- ESP_VOLUME_FSCTL_PARAMETERS
---

# Volume events

This page contains reference entries in the [Events API family](wesp-api-reference.md#events). Each entry includes its declaration and requirements.

## Volume mount

### ESP_VOLUME_MOUNT_CONFIG

The structure `ESP_VOLUME_MOUNT_CONFIG` is used to configure a volume mount event.

#### Syntax

```cpp
typedef struct ESP_VOLUME_MOUNT_CONFIG
{
    ESP_IO_OPERATION_CONFIG OperationConfig;
    ESP_VOLUME_CONFIG VolumeConfig;
    ESP_INTEGER_CONFIG DeviceTypeConfig;
} ESP_VOLUME_MOUNT_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| OperationConfig | Specifies configuration for the IO operation. |
| VolumeConfig | Specifies configuration for the volume being mounted. |
| DeviceTypeConfig | Specifies configuration for the device type. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_IO_OPERATION_CONFIG`](wesp-event-shared-types.md#esp_io_operation_config)
- [`ESP_VOLUME_CONFIG`](wesp-storage-objects.md#esp_volume_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_VOLUME_MOUNT_PARAMETERS

The structure `ESP_VOLUME_MOUNT_PARAMETERS` contains the parameters associated with a volume mount event notification.

#### Syntax

```cpp
typedef struct ESP_VOLUME_MOUNT_PARAMETERS
{
    ESP_IO_OPERATION Operation;
    ESP_VOLUME_INFO Volume;
    UINT32 DeviceType;
} ESP_VOLUME_MOUNT_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Operation | The IO operation for the event. |
| Volume | The volume being mounted. |
| DeviceType | Device type of the file system's volume device object for the newly mounted volume. For example:<br>FILE_DEVICE_CD_ROM_FILE_SYSTEM<br>FILE_DEVICE_DISK_FILE_SYSTEM<br>FILE_DEVICE_NETWORK_FILE_SYSTEM |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_IO_OPERATION`](wesp-event-shared-types.md#esp_io_operation)
- [`ESP_VOLUME_INFO`](wesp-storage-objects.md#esp_volume_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Volume dismount

### ESP_VOLUME_DISMOUNT_CONFIG

The structure `ESP_VOLUME_DISMOUNT_CONFIG` is used to configure a volume dismount event.

#### Syntax

```cpp
typedef struct ESP_VOLUME_DISMOUNT_CONFIG
{
    ESP_VOLUME_CONFIG VolumeConfig;
} ESP_VOLUME_DISMOUNT_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| VolumeConfig | Specifies configuration for the volume being dismounted. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_VOLUME_CONFIG`](wesp-storage-objects.md#esp_volume_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_VOLUME_DISMOUNT_PARAMETERS

The structure `ESP_VOLUME_DISMOUNT_PARAMETERS` contains the parameters associated with a volume dismount event notification.

#### Syntax

```cpp
typedef struct ESP_VOLUME_DISMOUNT_PARAMETERS
{
    ESP_VOLUME_INFO Volume;
} ESP_VOLUME_DISMOUNT_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Volume | The volume being dismounted. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_VOLUME_INFO`](wesp-storage-objects.md#esp_volume_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Volume control

### ESP_VOLUME_FSCTL_CONFIG

The structure `ESP_VOLUME_FSCTL_CONFIG` is used to configure a volume FSCTL event.

#### Syntax

```cpp
typedef struct ESP_VOLUME_FSCTL_CONFIG
{
    ESP_IO_OPERATION_CONFIG OperationConfig;
    ESP_VOLUME_CONFIG VolumeConfig;
    ESP_INTEGER_CONFIG ControlCodeConfig;
    ESP_INTEGER_CONFIG InputBufferSizeConfig;
    ESP_BINARY_CONFIG InputBufferConfig;
} ESP_VOLUME_FSCTL_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| OperationConfig | Specifies configuration for the IO operation. |
| VolumeConfig | Specifies configuration for the volume. |
| ControlCodeConfig | Specifies configuration for the control code. |
| InputBufferSizeConfig | Specifies configuration for the input buffer size. |
| InputBufferConfig | Specifies configuration for the input buffer. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BINARY_CONFIG`](wesp-rule-value-configuration.md#esp_binary_config)
- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_IO_OPERATION_CONFIG`](wesp-event-shared-types.md#esp_io_operation_config)
- [`ESP_VOLUME_CONFIG`](wesp-storage-objects.md#esp_volume_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_VOLUME_FSCTL_PARAMETERS

The structure `ESP_VOLUME_FSCTL_PARAMETERS` contains the parameters associated with a volume FSCTL event notification.

#### Syntax

```cpp
typedef struct ESP_VOLUME_FSCTL_PARAMETERS
{
    ESP_IO_OPERATION Operation;
    ESP_VOLUME_INFO Volume;
    UINT32 ControlCode;
    UINT32 InputBufferSize;
    _Field_size_bytes_(InputBufferSize) const void* InputBuffer;
} ESP_VOLUME_FSCTL_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Operation | The IO operation for the event. |
| Volume | The volume for the FSCTL operation. |
| ControlCode | The control code. |
| InputBufferSize | The size in bytes of the input buffer. |
| InputBuffer | The input buffer. By default, the input buffer is not supplied. The client must specify to include the input buffer through the "InputBufferConfig" field in the structure `ESP_VOLUME_FSCTL_CONFIG`. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_IO_OPERATION`](wesp-event-shared-types.md#esp_io_operation)
- [`ESP_VOLUME_INFO`](wesp-storage-objects.md#esp_volume_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
