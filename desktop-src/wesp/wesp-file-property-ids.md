---
title: "WESP file and storage property IDs"
description: "Windows endpoint security platform API reference for file and storage property IDs, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- ESP_FILE_STREAM_PROPERTY_ID
- ESP_FILE_PROPERTY_ID
- ESP_FILE_OBJECT_PROPERTY_ID
- ESP_VOLUME_PROPERTY_ID
- ESP_DISK_PROPERTY_ID
---

# File and storage property IDs

This page contains reference entries in the [Property queries API family](wesp-api-reference.md#property-queries). Each entry includes its declaration and requirements.

## File stream properties

### ESP_FILE_STREAM_PROPERTY_ID

File stream properties are defined in the enum `ESP_FILE_STREAM_PROPERTY_ID`. The expected comparison structure for each property ID and its property data is commented next to each enum value below.

#### Syntax

```cpp
typedef enum ESP_FILE_STREAM_PROPERTY_ID
{
    ESP_FILE_STREAM_PROPERTY_ID_NONE = 0,
    ESP_FILE_STREAM_PROPERTY_ID_NAME, // ESP_STRING_COMPARISON - ESP_UNICODE_STRING
    ESP_FILE_STREAM_PROPERTY_ID_SIZE, // ESP_INTEGER_COMPARISON - UINT64
    ESP_FILE_STREAM_PROPERTY_ID_ALLOCATION_SIZE, // ESP_INTEGER_COMPARISON - UINT64
    ESP_FILE_STREAM_PROPERTY_ID_IS_ADS // ESP_BOOL_COMPARISON - BOOL
} ESP_FILE_STREAM_PROPERTY_ID;
```

#### Values

| Property ID | Description | Property Variant Type |
| --- | --- | --- |
| `ESP_FILE_STREAM_PROPERTY_ID_NAME` | The file stream name. | `ESP_VARIANT_TYPE_UNICODE_STRING` |
| `ESP_FILE_STREAM_PROPERTY_ID_SIZE` | The file stream size. | `ESP_VARIANT_TYPE_UINT64` |
| `ESP_FILE_STREAM_PROPERTY_ID_ALLOCATION_SIZE` | The file stream allocation size. | `ESP_VARIANT_TYPE_UINT64` |
| `ESP_FILE_STREAM_PROPERTY_ID_IS_ADS` | Whether the file stream is an alternate data stream. If false, the file stream is the default stream. | `ESP_VARIANT_TYPE_BOOL` |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BOOL_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_bool_comparison)
- [`ESP_INTEGER_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_integer_comparison)
- [`ESP_STRING_COMPARISON`](wesp-filter-string-comparisons.md#esp_string_comparison)
- [`ESP_UNICODE_STRING`](wesp-common-utilities.md#esp_unicode_string)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## File properties

### ESP_FILE_PROPERTY_ID

File properties are defined in the enum `ESP_FILE_PROPERTY_ID`. The expected comparison structure for each property ID and its property data is commented next to each enum value below.

#### Syntax

```cpp
typedef enum ESP_FILE_PROPERTY_ID
{
    ESP_FILE_PROPERTY_ID_NONE = 0,
    ESP_FILE_PROPERTY_ID_FILE_ID_128, // ESP_BINARY_COMPARISON - FILE_ID_128
    ESP_FILE_PROPERTY_ID_ATTRIBUTES, // ESP_INTEGER_COMPARISON - UINT32
    ESP_FILE_PROPERTY_ID_CREATION_TIME, // ESP_INTEGER_COMPARISON - FILETIME
    ESP_FILE_PROPERTY_ID_LAST_ACCESS_TIME, // ESP_INTEGER_COMPARISON - FILETIME
    ESP_FILE_PROPERTY_ID_LAST_WRITE_TIME, // ESP_INTEGER_COMPARISON - FILETIME
    ESP_FILE_PROPERTY_ID_CHANGE_TIME, // ESP_INTEGER_COMPARISON - FILETIME
    ESP_FILE_PROPERTY_ID_EA_LIST, // ESP_EA_LIST_COMPARISON - ESP_EA_LIST
    ESP_FILE_PROPERTY_ID_IS_REPARSE_POINT, // ESP_BOOL_COMPARISON - BOOL
    ESP_FILE_PROPERTY_ID_IS_SYMLINK, // ESP_BOOL_COMPARISON - BOOL
    ESP_FILE_PROPERTY_ID_IS_DIRECTORY, // ESP_BOOL_COMPARISON - BOOL
    ESP_FILE_PROPERTY_ID_IS_DIRECTORY_CASE_SENSITIVE, // ESP_BOOL_COMPARISON - BOOL
    ESP_FILE_PROPERTY_ID_SECURITY_DESCRIPTOR, // ESP_SECURITY_DESCRIPTOR_COMPARISON - SECURITY_DESCRIPTOR
    ESP_FILE_PROPERTY_ID_NUMBER_OF_LINKS, // ESP_INTEGER_COMPARISON - UINT32
    ESP_FILE_PROPERTY_ID_REPARSE_TAG, // ESP_INTEGER_COMPARISON - UINT32
    ESP_FILE_PROPERTY_ID_REPARSE_BUFFER, // ESP_BINARY_COMPARISON - ESP_BUFFER
    ESP_FILE_PROPERTY_ID_CACHED_SIGNING_LEVEL, // ESP_INTEGER_COMPARISON - SE_SIGNING_LEVEL (SeGetCachedSigningLevel)
    ESP_FILE_PROPERTY_ID_ADS_NAMES, // ESP_STRING_LIST_COMPARISON - ESP_STRING_LIST
    ESP_FILE_PROPERTY_ID_USN // ESP_INTEGER_COMPARISON - USN
} ESP_FILE_PROPERTY_ID;
```

#### Values

| Property ID | Description | Property Variant Type |
| --- | --- | --- |
| `ESP_FILE_PROPERTY_ID_FILE_ID_128` | The 128 bit file id. | `ESP_VARIANT_TYPE_FILE_ID_128` |
| `ESP_FILE_PROPERTY_ID_ATTRIBUTES` | The file's attributes. | `ESP_VARIANT_TYPE_UINT32` |
| `ESP_FILE_PROPERTY_ID_CREATION_TIME` | The file creation time. | `ESP_VARIANT_TYPE_FILETIME` |
| `ESP_FILE_PROPERTY_ID_LAST_ACCESS_TIME` | The file last access time. | `ESP_VARIANT_TYPE_FILETIME` |
| `ESP_FILE_PROPERTY_ID_LAST_WRITE_TIME` | The file last write time. | `ESP_VARIANT_TYPE_FILETIME` |
| `ESP_FILE_PROPERTY_ID_CHANGE_TIME` | The file change time. | `ESP_VARIANT_TYPE_FILETIME` |
| `ESP_FILE_PROPERTY_ID_EA_LIST` | The file's extended attributes list. | `ESP_VARIANT_TYPE_EA_LIST` |
| `ESP_FILE_PROPERTY_ID_IS_REPARSE_POINT` | Whether the file is a reparse point. | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_FILE_PROPERTY_ID_IS_SYMLINK` | Whether the file is a symbolic link (i.e. IO_REPARSE_TAG_SYMLINK). | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_FILE_PROPERTY_ID_IS_DIRECTORY` | Whether the file is a directory. | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_FILE_PROPERTY_ID_IS_DIRECTORY_CASE_SENSITIVE` | Whether the directory is case sensitive. | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_FILE_PROPERTY_ID_SECURITY_DESCRIPTOR` | The file's security descriptor. | `ESP_VARIANT_TYPE_SECURITY_DESCRIPTOR` |
| `ESP_FILE_PROPERTY_ID_NUMBER_OF_LINKS` | The number of hardlinks for the file. | `ESP_VARIANT_TYPE_UINT32` |
| `ESP_FILE_PROPERTY_ID_REPARSE_TAG` | The file's reparse tag if it is a reparse point. | `ESP_VARIANT_TYPE_UINT32` |
| `ESP_FILE_PROPERTY_ID_REPARSE_BUFFER` | The file's reparse buffer if it is a reparse point. | `ESP_VARIANT_TYPE_BUFFER` |
| `ESP_FILE_PROPERTY_ID_CACHED_SIGNING_LEVEL` | The file's cached signing level (i.e. SeGetCachedSigningLevel). | `ESP_VARIANT_TYPE_SIGNING_LEVEL` |
| `ESP_FILE_PROPERTY_ID_ADS_NAMES` | The file's alternate data stream names. | `ESP_VARIANT_TYPE_STRING_LIST` |
| `ESP_FILE_PROPERTY_ID_USN` | The file's USN. | `ESP_VARIANT_TYPE_USN` |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BINARY_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_binary_comparison)
- [`ESP_BOOL_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_bool_comparison)
- [`ESP_BUFFER`](wesp-common-utilities.md#esp_buffer)
- [`ESP_EA_LIST`](wesp-common-value-types.md#esp_ea_list)
- [`ESP_EA_LIST_COMPARISON`](wesp-filter-domain-comparisons.md#esp_ea_list_comparison)
- [`ESP_INTEGER_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_integer_comparison)
- [`ESP_SECURITY_DESCRIPTOR_COMPARISON`](wesp-filter-security-comparisons.md#esp_security_descriptor_comparison)
- [`ESP_STRING_LIST`](wesp-common-utilities.md#esp_string_list)
- [`ESP_STRING_LIST_COMPARISON`](wesp-filter-string-comparisons.md#esp_string_list_comparison)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## File object properties

### ESP_FILE_OBJECT_PROPERTY_ID

File object properties are defined in the enum `ESP_FILE_OBJECT_PROPERTY_ID`. The expected comparison structure for each property ID and its property data is commented next to each enum value below.

#### Syntax

```cpp
typedef enum ESP_FILE_OBJECT_PROPERTY_ID
{
    ESP_FILE_OBJECT_PROPERTY_ID_NONE = 0,
    ESP_FILE_OBJECT_PROPERTY_ID_NORMALIZED_NT_PATH, // ESP_STRING_COMPARISON - ESP_UNICODE_STRING (FLT_FILE_NAME_NORMALIZED)
    ESP_FILE_OBJECT_PROPERTY_ID_NORMALIZED_DOS_PATH, // ESP_STRING_COMPARISON - ESP_UNICODE_STRING (FLT_FILE_NAME_NORMALIZED)
    ESP_FILE_OBJECT_PROPERTY_ID_LOCAL_LOOPBACK_NT_PATH, // ESP_STRING_COMPARISON - ESP_UNICODE_STRING
    ESP_FILE_OBJECT_PROPERTY_ID_LOCAL_LOOPBACK_DOS_PATH, // ESP_STRING_COMPARISON - ESP_UNICODE_STRING
    ESP_FILE_OBJECT_PROPERTY_ID_EXTENSION, // ESP_STRING_COMPARISON - ESP_UNICODE_STRING (FLT_FILE_NAME_INFORMATION.Extension)
    ESP_FILE_OBJECT_PROPERTY_ID_FINAL_COMPONENT, // ESP_STRING_COMPARISON - ESP_UNICODE_STRING (FLT_FILE_NAME_INFORMATION.FinalComponent)
    ESP_FILE_OBJECT_PROPERTY_ID_RELATIVE_PATH, // ESP_STRING_COMPARISON - ESP_UNICODE_STRING
    ESP_FILE_OBJECT_PROPERTY_ID_FILE_NAME, // ESP_STRING_COMPARISON - ESP_UNICODE_STRING (FILE_OBJECT.FileName)
    ESP_FILE_OBJECT_PROPERTY_ID_OPENED_NT_NAME, // ESP_STRING_COMPARISON - ESP_UNICODE_STRING (FLT_FILE_NAME_OPENED)
    ESP_FILE_OBJECT_PROPERTY_ID_OPENED_DOS_NAME, // ESP_STRING_COMPARISON - ESP_UNICODE_STRING (FLT_FILE_NAME_OPENED)
    ESP_FILE_OBJECT_PROPERTY_ID_IS_TRANSACTED, // ESP_BOOL_COMPARISON - BOOL
    ESP_FILE_OBJECT_PROPERTY_ID_READ_ACCESS, // ESP_BOOL_COMPARISON - BOOL
    ESP_FILE_OBJECT_PROPERTY_ID_WRITE_ACCESS, // ESP_BOOL_COMPARISON - BOOL
    ESP_FILE_OBJECT_PROPERTY_ID_DELETE_ACCESS, // ESP_BOOL_COMPARISON - BOOL
    ESP_FILE_OBJECT_PROPERTY_ID_SHARED_READ_ACCESS, // ESP_BOOL_COMPARISON - BOOL
    ESP_FILE_OBJECT_PROPERTY_ID_SHARED_WRITE_ACCESS, // ESP_BOOL_COMPARISON - BOOL
    ESP_FILE_OBJECT_PROPERTY_ID_SHARED_DELETE_ACCESS, // ESP_BOOL_COMPARISON - BOOL
    ESP_FILE_OBJECT_PROPERTY_ID_FLAGS, // ESP_INTEGER_COMPARISON - UINT32 (FILE_OBJECT.Flags)
    ESP_FILE_OBJECT_PROPERTY_ID_LOCK_OPERATION, // ESP_BOOL_COMPARISON - BOOL (FILE_OBJECT.LockOperation)
    ESP_FILE_OBJECT_PROPERTY_ID_DELETE_PENDING, // ESP_BOOL_COMPARISON - BOOL (FILE_OBJECT.DeletePending)
    ESP_FILE_OBJECT_PROPERTY_ID_IS_ATTACHED_TO_HOST_SILO, // ESP_BOOL_COMPARISON - BOOL
    ESP_FILE_OBJECT_PROPERTY_ID_IS_PAGING_FILE, // ESP_BOOL_COMPARISON - BOOL (FsRtlIsPagingFile)
    ESP_FILE_OBJECT_PROPERTY_ID_IS_SYSTEM_PAGING_FILE, // ESP_BOOL_COMPARISON - BOOL (FsRtlIsSystemPagingFile)
    ESP_FILE_OBJECT_PROPERTY_ID_IS_IGNORING_SHARING, // ESP_BOOL_COMPARISON - BOOL (IoIsFileObjectIgnoringSharing)
    ESP_FILE_OBJECT_PROPERTY_ID_HAS_USER_WRITABLE_REFERENCES, // ESP_BOOL_COMPARISON - BOOL (MmDoesFileHaveUserWritableReferences)
    ESP_FILE_OBJECT_PROPERTY_ID_WAS_OPENED_AS_COPY_SOURCE, // ESP_BOOL_COMPARISON - BOOL (IoIsFileObjectOpenedAsCopySource)
    ESP_FILE_OBJECT_PROPERTY_ID_WAS_OPENED_AS_COPY_DESTINATION, // ESP_BOOL_COMPARISON - BOOL (IoIsFileObjectOpenedAsCopyDestination)
    ESP_FILE_OBJECT_PROPERTY_ID_TARGET_OBJECT_TYPE, // ESP_INTEGER_COMPARISON - ESP_FO_TARGET_OBJECT_TYPE
} ESP_FILE_OBJECT_PROPERTY_ID;
```

#### Values

| Property ID | Description | Property Variant Type |
| --- | --- | --- |
| `ESP_FILE_OBJECT_PROPERTY_ID_NORMALIZED_NT_PATH` | The file object's normalized NT path. | `ESP_VARIANT_TYPE_UNICODE_STRING` |
| `ESP_FILE_OBJECT_PROPERTY_ID_NORMALIZED_DOS_PATH` | The file object's normalized DOS path. | `ESP_VARIANT_TYPE_UNICODE_STRING` |
| `ESP_FILE_OBJECT_PROPERTY_ID_LOCAL_LOOPBACK_NT_PATH` | The local loopback NT path (if any). For example, if a file is opened with the path "\\localhost\C$\Windows" or "\\?\UNC\localhost\C$\Windows", the local loopback path would be something  like "\Device\HarddiskVolume1\Windows". | `ESP_VARIANT_TYPE_UNICODE_STRING` |
| `ESP_FILE_OBJECT_PROPERTY_ID_LOCAL_LOOPBACK_DOS_PATH` | The local loopback DOS path (if any). For example, if a file is opened with the path "\\localhost\C$\Windows" or "\\?\UNC\localhost\C$\Windows", the local loopback path would be something  like "C:\Windows". | `ESP_VARIANT_TYPE_UNICODE_STRING` |
| `ESP_FILE_OBJECT_PROPERTY_ID_EXTENSION` | The file object's file name extension (excluding "."). | `ESP_VARIANT_TYPE_UNICODE_STRING` |
| `ESP_FILE_OBJECT_PROPERTY_ID_FINAL_COMPONENT` | The final name component parsed from the name string. This is the equivalent of "FLT_FILE_NAME_INFORMATION.FinalComponent". | `ESP_VARIANT_TYPE_UNICODE_STRING` |
| `ESP_FILE_OBJECT_PROPERTY_ID_RELATIVE_PATH` | The file object's normalized relative path. The is the normalized path relative to the volume root. | `ESP_VARIANT_TYPE_UNICODE_STRING` |
| `ESP_FILE_OBJECT_PROPERTY_ID_FILE_NAME` | The file object's file name. This is the equivalent of "FILE_OBJECT.FileName". | `ESP_VARIANT_TYPE_UNICODE_STRING` |
| `ESP_FILE_OBJECT_PROPERTY_ID_OPENED_NT_NAME` | The file object's opened NT name. This is the equivalent of querying the file object name with FLT_FILE_NAME_OPENED. | `ESP_VARIANT_TYPE_UNICODE_STRING` |
| `ESP_FILE_OBJECT_PROPERTY_ID_OPENED_DOS_NAME` | The file object's opened DOS name. This is the equivalent of querying the file object name with FLT_FILE_NAME_OPENED. | `ESP_VARIANT_TYPE_UNICODE_STRING` |
| `ESP_FILE_OBJECT_PROPERTY_ID_IS_TRANSACTED` | Whether the FILE_OBJECT is part of a KTM transaction. | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_FILE_OBJECT_PROPERTY_ID_READ_ACCESS` | Whether the FILE_OBJECT was opened for read access. This is the equivalent to "FILE_OBJECT.ReadAccess". | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_FILE_OBJECT_PROPERTY_ID_WRITE_ACCESS` | Whether the FILE_OBJECT was opened for write access. This is the equivalent to "FILE_OBJECT.WriteAccess". | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_FILE_OBJECT_PROPERTY_ID_DELETE_ACCESS` | Whether the FILE_OBJECT was opened for delete access. This is the equivalent to "FILE_OBJECT.DeleteAccess". | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_FILE_OBJECT_PROPERTY_ID_SHARED_READ_ACCESS` | Whether the FILE_OBJECT was opened for shared read access. This is the equivalent to "FILE_OBJECT.SharedRead". | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_FILE_OBJECT_PROPERTY_ID_SHARED_WRITE_ACCESS` | Whether the FILE_OBJECT was opened for shared write access. This is the equivalent to "FILE_OBJECT.SharedWrite". | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_FILE_OBJECT_PROPERTY_ID_SHARED_DELETE_ACCESS` | Whether the FILE_OBJECT was opened for shared delete access. This is the equivalent to "FILE_OBJECT.SharedDelete". | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_FILE_OBJECT_PROPERTY_ID_FLAGS` | The file object's flags. This is the equivalent to "FILE_OBJECT.Flags". | `ESP_VARIANT_TYPE_UINT32` |
| `ESP_FILE_OBJECT_PROPERTY_ID_LOCK_OPERATION` | Whether a lock operation has been performed on the FILE_OBJECT. This is the equivalent to "FILE_OBJECT.LockOperation". | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_FILE_OBJECT_PROPERTY_ID_DELETE_PENDING` | Whether a delete operation for the file associated with the file object exists. This is the equivalent to "FILE_OBJECT.DeletePending". | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_FILE_OBJECT_PROPERTY_ID_IS_ATTACHED_TO_HOST_SILO` | Whether the FILE_OBJECT is attached to the host silo. | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_FILE_OBJECT_PROPERTY_ID_IS_PAGING_FILE` | Whether the FILE_OBJECT is a paging file. This is the equivalent to FsRtlIsPagingFile. | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_FILE_OBJECT_PROPERTY_ID_IS_SYSTEM_PAGING_FILE` | Whether the FILE_OBJECT is the system paging file. This is the equivalent to FsRtlIsSystemPagingFile. | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_FILE_OBJECT_PROPERTY_ID_IS_IGNORING_SHARING` | Whether the FILE_OBJECT is ignoring sharing. This is the equivalent to IoIsFileObjectIgnoringSharing. | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_FILE_OBJECT_PROPERTY_ID_HAS_USER_WRITABLE_REFERENCES` | Whether the FILE_OBJECT has user writable references. This is the equivalent to MmDoesFileHaveUserWritableReferences. | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_FILE_OBJECT_PROPERTY_ID_WAS_OPENED_AS_COPY_SOURCE` | Whether the FILE_OBJECT was previously opened with copy intent as a source file. This is the equivalent to IoCheckFileObjectOpenedAsCopySource. | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_FILE_OBJECT_PROPERTY_ID_WAS_OPENED_AS_COPY_DESTINATION` | Whether the FILE_OBJECT was previously opened with copy intent as a destination file. This is the equivalent to IoCheckFileObjectOpenedAsDestinationSource. | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_FILE_OBJECT_PROPERTY_ID_TARGET_OBJECT_TYPE` | The file object's target object type (e.g. file stream, volume, pipe, mailslot) | `ESP_VARIANT_TYPE_FO_TARGET_OBJECT_TYPE` |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BOOL_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_bool_comparison)
- [`ESP_FO_TARGET_OBJECT_TYPE`](wesp-common-value-types.md#esp_fo_target_object_type)
- [`ESP_INTEGER_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_integer_comparison)
- [`ESP_STRING_COMPARISON`](wesp-filter-string-comparisons.md#esp_string_comparison)
- [`ESP_UNICODE_STRING`](wesp-common-utilities.md#esp_unicode_string)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Volume properties

### ESP_VOLUME_PROPERTY_ID

Volume properties are defined in the enum `ESP_VOLUME_PROPERTY_ID`. The expected comparison structure for each property ID and its property data is commented next to each enum value below.

#### Syntax

```cpp
typedef enum ESP_VOLUME_PROPERTY_ID
{
    ESP_VOLUME_PROPERTY_ID_NONE = 0,
    ESP_VOLUME_PROPERTY_ID_NT_PATH, // ESP_STRING_COMPARISON - ESP_UNICODE_STRING
    ESP_VOLUME_PROPERTY_ID_DOS_PATH, // ESP_STRING_COMPARISON - ESP_UNICODE_STRING
    ESP_VOLUME_PROPERTY_ID_FILESYSTEM_TYPE, // ESP_INTEGER_COMPARISON - UINT32 (FLT_FILESYSTEM_TYPE)
    ESP_VOLUME_PROPERTY_ID_DEVICE_TYPE, // ESP_INTEGER_COMPARISON - DEVICE_TYPE
    ESP_VOLUME_PROPERTY_ID_SERIAL_NUMBER, // ESP_INTEGER_COMPARISON - UINT32
    ESP_VOLUME_PROPERTY_ID_GUID, // ESP_BINARY_COMPARISON - GUID
    ESP_VOLUME_PROPERTY_ID_LABEL, // ESP_STRING_COMPARISON - ESP_UNICODE_STRING
    ESP_VOLUME_PROPERTY_ID_IS_SNAPSHOT_VOLUME, // ESP_BOOL_COMPARISON - BOOL
    ESP_VOLUME_PROPERTY_ID_IS_READ_ONLY_VOLUME, // ESP_BOOL_COMPARISON - BOOL
    ESP_VOLUME_PROPERTY_ID_IS_SYSTEM_VOLUME, // ESP_BOOL_COMPARISON - BOOL
    ESP_VOLUME_PROPERTY_ID_IS_DEV_VOLUME, // ESP_BOOL_COMPARISON - BOOL
    ESP_VOLUME_PROPERTY_ID_IS_TRUSTED_VOLUME, // ESP_BOOL_COMPARISON - BOOL (FLTFL_INSTANCE_SETUP_TRUSTED_VOLUME)
    ESP_VOLUME_PROPERTY_ID_DEVICE_CHARACTERISTICS, // ESP_INTEGER_COMPARISON - UINT32 (DEVICE_OBJECT.Characteristics)
    ESP_VOLUME_PROPERTY_ID_DEVICE_FLAGS, // ESP_INTEGER_COMPARISON - UINT32 (DEVICE_OBJECT.Flags)
    ESP_VOLUME_PROPERTY_ID_FILESYSTEM_ATTRIBUTES, // ESP_INTEGER_COMPARISON - UINT32 (FILE_FS_ATTRIBUTE_INFORMATION.FileSystemAttributes)
    ESP_VOLUME_PROPERTY_ID_FILESYSTEM_NAME // ESP_STRING_COMPARISON - ESP_UNICODE_STRING (FILE_FS_ATTRIBUTE_INFORMATION.FileSystemName)
} ESP_VOLUME_PROPERTY_ID;
```

#### Values

| Property ID | Description | Property Variant Type |
| --- | --- | --- |
| `ESP_VOLUME_PROPERTY_ID_NT_PATH` | The volume's NT path (e.g. "\Device\HarddiskVolume1"). | `ESP_VARIANT_TYPE_UNICODE_STRING` |
| `ESP_VOLUME_PROPERTY_ID_DOS_PATH` | The volume's DOS path (e.g. "C:\"). | `ESP_VARIANT_TYPE_UNICODE_STRING` |
| `ESP_VOLUME_PROPERTY_ID_FILESYSTEM_TYPE` | The volume's filesystem type (i.e. "FLT_FILESYSTEM_TYPE_*"). | `ESP_VARIANT_TYPE_UINT32` |
| `ESP_VOLUME_PROPERTY_ID_DEVICE_TYPE` | The volume's device type. | `ESP_VARIANT_TYPE_DEVICE_TYPE` |
| `ESP_VOLUME_PROPERTY_ID_SERIAL_NUMBER` | The volume's serial number. | `ESP_VARIANT_TYPE_UINT32` |
| `ESP_VOLUME_PROPERTY_ID_GUID` | The volume's GUID. | `ESP_VARIANT_TYPE_GUID` |
| `ESP_VOLUME_PROPERTY_ID_LABEL` | The volume's label. | `ESP_VARIANT_TYPE_UNICODE_STRING` |
| `ESP_VOLUME_PROPERTY_ID_IS_SNAPSHOT_VOLUME` | Whether the volume is a snapshot volume. | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_VOLUME_PROPERTY_ID_IS_READ_ONLY_VOLUME` | Whether the volume is a read only volume. | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_VOLUME_PROPERTY_ID_IS_SYSTEM_VOLUME` | Whether the volume is the system volume (e.g. C:\). | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_VOLUME_PROPERTY_ID_IS_DEV_VOLUME` | Whether the volume is a developer volume (i.e. dev drive). | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_VOLUME_PROPERTY_ID_IS_TRUSTED_VOLUME` | Whether the volume is a trusted volume (i.e. FLTFL_INSTANCE_SETUP_TRUSTED_VOLUME). | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_VOLUME_PROPERTY_ID_DEVICE_CHARACTERISTICS` | The volume's device characteristics. This is the equivalent of "DEVICE_OBJECT.Characteristics". | `ESP_VARIANT_TYPE_UINT32` |
| `ESP_VOLUME_PROPERTY_ID_DEVICE_FLAGS` | The volume's device flags. This is the equivalent of "DEVICE_OBJECT.Flags". | `ESP_VARIANT_TYPE_UINT32` |
| `ESP_VOLUME_PROPERTY_ID_FILESYSTEM_ATTRIBUTES` | The volume's filesystem attributes. This is the equivalent of "FILE_FS_ATTRIBUTE_INFORMATION.FileSystemAttributes". | `ESP_VARIANT_TYPE_UINT32` |
| `ESP_VOLUME_PROPERTY_ID_FILESYSTEM_NAME` | The volume's filesystem name. This is the equivalent of "FILE_FS_ATTRIBUTE_INFORMATION.FileSystemName". | `ESP_VARIANT_TYPE_UNICODE_STRING` |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BINARY_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_binary_comparison)
- [`ESP_BOOL_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_bool_comparison)
- [`ESP_INTEGER_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_integer_comparison)
- [`ESP_STRING_COMPARISON`](wesp-filter-string-comparisons.md#esp_string_comparison)
- [`ESP_UNICODE_STRING`](wesp-common-utilities.md#esp_unicode_string)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Disk properties

### ESP_DISK_PROPERTY_ID

Disk properties are defined in the enum `ESP_DISK_PROPERTY_ID`. The expected comparison structure for each property ID and its property data is commented next to each enum value below.

#### Syntax

```cpp
typedef enum ESP_DISK_PROPERTY_ID
{
    ESP_DISK_PROPERTY_ID_NONE = 0,
    ESP_DISK_PROPERTY_ID_NT_PATH, // ESP_STRING_COMPARISON - ESP_UNICODE_STRING
    ESP_DISK_PROPERTY_ID_DOS_PATH, // ESP_STRING_COMPARISON - ESP_UNICODE_STRING
    ESP_DISK_PROPERTY_ID_SERIAL_NUMBER, // ESP_STRING_COMPARISON - ESP_UNICODE_STRING
    ESP_DISK_PROPERTY_ID_BUS_TYPE, // ESP_INTEGER_COMPARISON - STORAGE_BUS_TYPE
    ESP_DISK_PROPERTY_ID_VENDOR_ID, // ESP_STRING_COMPARISON - ESP_UNICODE_STRING
    ESP_DISK_PROPERTY_ID_PRODUCT_ID, // ESP_STRING_COMPARISON - ESP_UNICODE_STRING
    ESP_DISK_PROPERTY_ID_DISK_NUMBER, // ESP_INTEGER_COMPARISON - UINT32
    ESP_DISK_PROPERTY_ID_INSTANCE_ID, // ESP_STRING_COMPARISON - ESP_UNICODE_STRING (IoGetDevicePropertyData + DEVPKEY_Device_InstanceId)
    ESP_DISK_PROPERTY_ID_IS_DEVICE_HOTPLUG, // ESP_BOOL_COMPARISON - BOOL (STORAGE_HOTPLUG_INFO.DeviceHotplug)
    ESP_DISK_PROPERTY_ID_IS_MEDIA_HOTPLUG, // ESP_BOOL_COMPARISON - BOOL (STORAGE_HOTPLUG_INFO.MediaHotplug)
    ESP_DISK_PROPERTY_ID_IS_MEDIA_REMOVABLE, // ESP_BOOL_COMPARISON - BOOL (STORAGE_HOTPLUG_INFO.MediaRemovable)
    ESP_DISK_PROPERTY_ID_DEVICE_CHARACTERISTICS, // ESP_INTEGER_COMPARISON - UINT32 (DEVICE_OBJECT.Characteristics)
    ESP_DISK_PROPERTY_ID_DEVICE_FLAGS // ESP_INTEGER_COMPARISON - UINT32 (DEVICE_OBJECT.Flags)
} ESP_DISK_PROPERTY_ID;
```

#### Values

| Property ID | Description | Property Variant Type |
| --- | --- | --- |
| `ESP_DISK_PROPERTY_ID_NT_PATH` | The disk's NT path. | `ESP_VARIANT_TYPE_UNICODE_STRING` |
| `ESP_DISK_PROPERTY_ID_DOS_PATH` | The disk's DOS path. | `ESP_VARIANT_TYPE_UNICODE_STRING` |
| `ESP_DISK_PROPERTY_ID_SERIAL_NUMBER` | The disk's serial number. | `ESP_VARIANT_TYPE_UNICODE_STRING` |
| `ESP_DISK_PROPERTY_ID_BUS_TYPE` | The disk's bus type. | `ESP_VARIANT_TYPE_STORAGE_BUS_TYPE` |
| `ESP_DISK_PROPERTY_ID_VENDOR_ID` | The disk's vendor id. | `ESP_VARIANT_TYPE_UNICODE_STRING` |
| `ESP_DISK_PROPERTY_ID_PRODUCT_ID` | The disk's product id. | `ESP_VARIANT_TYPE_UNICODE_STRING` |
| `ESP_DISK_PROPERTY_ID_DISK_NUMBER` | The disk number. | `ESP_VARIANT_TYPE_UINT32` |
| `ESP_DISK_PROPERTY_ID_INSTANCE_ID` | The disk's instance id. This is the equivalent of IoGetDevicePropertyData with property key "DEVPKEY_Device_InstanceId". | `ESP_VARIANT_TYPE_UNICODE_STRING` |
| `ESP_DISK_PROPERTY_ID_IS_DEVICE_HOTPLUG` | Whether the disk is a hot plug device. This is the equivalent of "STORAGE_HOTPLUG_INFO.DeviceHotplug". | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_DISK_PROPERTY_ID_IS_MEDIA_HOTPLUG` | Whether the media is not lockable. This is the equivalent of "STORAGE_HOTPLUG_INFO.MediaHotplug". | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_DISK_PROPERTY_ID_IS_MEDIA_REMOVABLE` | Whether the device media is removable. This is the equivalent of "STORAGE_HOTPLUG_INFO.MediaRemovable". | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_DISK_PROPERTY_ID_DEVICE_CHARACTERISTICS` | The disk's device characteristics. This is the equivalent of "DEVICE_OBJECT.Characteristics". | `ESP_VARIANT_TYPE_UINT32` |
| `ESP_DISK_PROPERTY_ID_DEVICE_FLAGS` | The disk's device flags. This is the equivalent of "DEVICE_OBJECT.Flags". | `ESP_VARIANT_TYPE_UINT32` |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BOOL_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_bool_comparison)
- [`ESP_INTEGER_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_integer_comparison)
- [`ESP_STRING_COMPARISON`](wesp-filter-string-comparisons.md#esp_string_comparison)
- [`ESP_UNICODE_STRING`](wesp-common-utilities.md#esp_unicode_string)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
