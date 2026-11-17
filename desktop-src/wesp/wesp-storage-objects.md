---
title: "WESP volume and disk event objects"
description: "Windows endpoint security platform API reference for volume and disk event objects, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- EspCreateVolumeReference
- ESP_VOLUME_CONFIG_FLAGS
- ESP_VOLUME_CONFIG
- ESP_VOLUME_INFO
- EspCreateDiskReference
- ESP_DISK_CONFIG_FLAGS
- ESP_DISK_CONFIG
- ESP_DISK_INFO
---

# Volume and disk event objects

This page contains reference entries in the [Event objects API family](wesp-api-reference.md#event-objects). Each entry includes its declaration and requirements.

## Volume

### EspCreateVolumeReference

The API `EspCreateVolumeReference` creates an event object reference to an existing volume. This is useful in cases where a client needs to reference a volume outside the context of an event involving the volume. For example, a client may require a reference to a volume to query properties or set event object context.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateVolumeReference(
    _In_ ESP_CLIENT Client,
    _In_ const GUID* VolumeGuid,
    _Out_ ESP_EVENT_OBJECT_REF* ObjectRef
    );
```

#### Parameters

##### `Client`

Supplies the client.

##### `VolumeGuid`

Supplies the volume guid.

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

### ESP_VOLUME_CONFIG_FLAGS

The enum `ESP_VOLUME_CONFIG_FLAGS` specifies flags for an `ESP_VOLUME_CONFIG` structure. There are currently no supported flags.

#### Syntax

```cpp
typedef enum ESP_VOLUME_CONFIG_FLAGS
{
    ESP_VOLUME_CONFIG_FLAGS_NONE = 0x00000000
} ESP_VOLUME_CONFIG_FLAGS;
```

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_VOLUME_CONFIG`](wesp-storage-objects.md#esp_volume_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_VOLUME_CONFIG

The configuration structure for a volume event object is `ESP_VOLUME_CONFIG`.

#### Syntax

```cpp
typedef struct ESP_VOLUME_CONFIG
{
    ESP_VOLUME_CONFIG_FLAGS Flags;
    ESP_EVENT_OBJECT_CONFIG EventObjectConfig;

    UINT32 PropertiesCount;
    _Field_size_(PropertiesCount) const ESP_VOLUME_PROPERTY_ID* Properties;

    ESP_DISK_CONFIG DiskConfig;
} ESP_VOLUME_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Flags | Specifies flags for the volume. |
| EventObjectConfig | Supplies event object configuration for the volume. |
| PropertiesCount | Supplies the number of elements in the "Properties" array. |
| Properties | Supplies an array of volume properties that should be captured for the volume. |
| DiskConfig | Supplies the configuration for the volume's disk. Note that not all volumes have an associated disk (e.g. SMB volumes). |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_DISK_CONFIG`](wesp-storage-objects.md#esp_disk_config)
- [`ESP_EVENT_OBJECT_CONFIG`](wesp-event-object-references.md#esp_event_object_config)
- [`ESP_VOLUME_CONFIG_FLAGS`](wesp-storage-objects.md#esp_volume_config_flags)
- [`ESP_VOLUME_PROPERTY_ID`](wesp-file-property-ids.md#esp_volume_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_VOLUME_INFO

The structure `ESP_VOLUME_INFO` specifies information for a volume. This structure is supplied as part of an event notification (one for each volume associated with an event) and contains various details about the volume.

#### Syntax

```cpp
typedef struct ESP_VOLUME_INFO
{
    ESP_EVENT_OBJECT_INFO ObjectInfo;
    _Maybenull_ const ESP_DISK_INFO* DiskInfo;
} ESP_VOLUME_INFO;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ObjectInfo | Specifies information about the volume's event object. |
| DiskInfo | Specifies information about the volume's disk. This field may be null if the client didn't specify disk configuration through the "DiskConfig" field in `ESP_VOLUME_CONFIG`. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_DISK_INFO`](wesp-storage-objects.md#esp_disk_info)
- [`ESP_EVENT_OBJECT_INFO`](wesp-event-object-references.md#esp_event_object_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Disk

### EspCreateDiskReference

The API `EspCreateDiskReference` creates an event object reference to an existing disk. This is useful in cases where a client needs to reference a disk outside the context of an event involving the disk. For example, a client may require a reference to a disk to query properties or set event object context.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateDiskReference(
    _In_ ESP_CLIENT Client,
    _In_ const ESP_PATH* DiskPath,
    _Out_ ESP_EVENT_OBJECT_REF* ObjectRef
    );
```

#### Parameters

##### `Client`

Supplies the client.

##### `DiskPath`

Supplies the disk's path.

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

### ESP_DISK_CONFIG_FLAGS

The enum `ESP_DISK_CONFIG_FLAGS` specifies flags for an `ESP_DISK_CONFIG` structure.

#### Syntax

```cpp
typedef enum ESP_DISK_CONFIG_FLAGS
{
    ESP_DISK_CONFIG_FLAGS_NONE                  = 0x00000000,
    ESP_DISK_CONFIG_FLAGS_SKIP_IF_OBJECT_ABSENT = 0x00000001
} ESP_DISK_CONFIG_FLAGS;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_DISK_CONFIG_FLAGS_SKIP_IF_OBJECT_ABSENT` | Specifies to skip applying the configuration if the disk doesn't exist. For example, if a client sets this flag for a volume's disk and the volume doesn't have a disk (e.g. SMB), the disk configuration won't be applied.<br>If the disk is absent, this flag implicitly evaluates the disk's filter to true. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_DISK_CONFIG`](wesp-storage-objects.md#esp_disk_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_DISK_CONFIG

The configuration structure for a disk event object is `ESP_DISK_CONFIG`.

#### Syntax

```cpp
typedef struct ESP_DISK_CONFIG
{
    ESP_DISK_CONFIG_FLAGS Flags;
    ESP_EVENT_OBJECT_CONFIG EventObjectConfig;

    UINT32 PropertiesCount;
    _Field_size_(PropertiesCount) const ESP_DISK_PROPERTY_ID* Properties;
} ESP_DISK_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Flags | Specifies flags for the disk. |
| EventObjectConfig | Supplies event object configuration for the disk. |
| PropertiesCount | Supplies the number of elements in the "Properties" array. |
| Properties | Supplies an array of disk properties that should be captured for the disk. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_DISK_CONFIG_FLAGS`](wesp-storage-objects.md#esp_disk_config_flags)
- [`ESP_DISK_PROPERTY_ID`](wesp-file-property-ids.md#esp_disk_property_id)
- [`ESP_EVENT_OBJECT_CONFIG`](wesp-event-object-references.md#esp_event_object_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_DISK_INFO

The structure `ESP_DISK_INFO` specifies information for a disk. This structure is supplied as part of an event notification (one for each disk associated with an event) and contains various details about the disk.

#### Syntax

```cpp
typedef struct ESP_DISK_INFO
{
    ESP_EVENT_OBJECT_INFO ObjectInfo;
} ESP_DISK_INFO;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ObjectInfo | Specifies information about the disk's event object. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EVENT_OBJECT_INFO`](wesp-event-object-references.md#esp_event_object_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
