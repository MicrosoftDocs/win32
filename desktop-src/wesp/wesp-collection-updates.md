---
title: "WESP collection updates"
description: "Windows endpoint security platform API reference for collection updates, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- EspUpdateCollection
- ESP_COLLECTION_UPDATE_TYPE
- ESP_COLLECTION_UPDATE_FLAGS
- ESP_STRING_COLLECTION_FLAGS
- ESP_COLLECTION_ENTRY
- ESP_COLLECTION_UPDATE_ENTRY
---

# Collection updates

This page contains reference entries in the [Collections API family](wesp-api-reference.md#collections). Each entry includes its declaration and requirements.

## Collection update function

### EspUpdateCollection

The API `EspUpdateCollection` is used to update a collection. Clients can use this API to add or remove entries in the collection. When updating a collection, the API guarantees that either all updates succeed, or no updates succeed. After a collection is updated, the updates will immediately be reflected for any filter that references the collection.

#### Syntax

```cpp
HRESULT
WINAPI
EspUpdateCollection(
    _In_ ESP_COLLECTION Collection,
    _In_ ESP_COLLECTION_UPDATE_FLAGS Flags,
    _In_ UINT32 EntriesCount,
    _In_reads_(EntriesCount) const ESP_COLLECTION_UPDATE_ENTRY* Entries
    );
```

#### Parameters

##### `Collection`

Supplies the collection to update.

##### `Flags`

Supplies flags for the collection.

##### `EntriesCount`

Supplies the number of elements in the entries array.

##### `Entries`

Supplies an array of update entries.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_COLLECTION`](wesp-collection-management.md#esp_collection)
- [`ESP_COLLECTION_UPDATE_ENTRY`](wesp-collection-updates.md#esp_collection_update_entry)
- [`ESP_COLLECTION_UPDATE_FLAGS`](wesp-collection-updates.md#esp_collection_update_flags)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Collection entries and update types

### ESP_COLLECTION_UPDATE_TYPE

The enum `ESP_COLLECTION_UPDATE_TYPE` defines a collection update type.

#### Syntax

```cpp
typedef enum ESP_COLLECTION_UPDATE_TYPE
{
    ESP_COLLECTION_UPDATE_TYPE_NONE = 0,
    ESP_COLLECTION_UPDATE_TYPE_ADD,
    ESP_COLLECTION_UPDATE_TYPE_REMOVE
} ESP_COLLECTION_UPDATE_TYPE;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_COLLECTION_UPDATE_TYPE_ADD` | Adds an entry to the collection. If the entry already exists, this is a no-op. |
| `ESP_COLLECTION_UPDATE_TYPE_REMOVE` | Removes an entry from the collection. If the entry doesn't exist, this is a no-op. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_COLLECTION_UPDATE_FLAGS

The enum `ESP_COLLECTION_UPDATE_FLAGS` specifies flags for updating a collection.

#### Syntax

```cpp
typedef enum ESP_COLLECTION_UPDATE_FLAGS
{
    ESP_COLLECTION_UPDATE_FLAGS_NONE                = 0x00000000,
    ESP_COLLECTION_UPDATE_FLAGS_REMOVE_ALL_EXISTING = 0x00000001
} ESP_COLLECTION_UPDATE_FLAGS;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_COLLECTION_UPDATE_FLAGS_REMOVE_ALL_EXISTING` | All existing collection entries should be removed as part of the update. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_STRING_COLLECTION_FLAGS

The enum `ESP_STRING_COLLECTION_FLAGS` defines string collection flags.

#### Syntax

```cpp
typedef enum ESP_STRING_COLLECTION_FLAGS
{
    ESP_STRING_COLLECTION_FLAGS_NONE                  = 0x00000000,
    ESP_STRING_COLLECTION_FLAGS_CASE_SENSITIVE        = 0x00000001,
    ESP_STRING_COLLECTION_FLAGS_SUPPORT_PATTERN_MATCH = 0x00000002
} ESP_STRING_COLLECTION_FLAGS;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_STRING_COLLECTION_FLAGS_CASE_SENSITIVE` | The string collection is case sensitive. If not set, the string collection is case insensitive. |
| `ESP_STRING_COLLECTION_FLAGS_SUPPORT_PATTERN_MATCH` | If set, the string collection supports pattern matching. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_COLLECTION_ENTRY

The union `ESP_COLLECTION_ENTRY` represents a collection entry. The active member in the union is determined by the collection type.

#### Syntax

```cpp
typedef union ESP_COLLECTION_ENTRY
{
    UINT64 Integer;
    ESP_UNICODE_STRING String;
    ESP_BUFFER Binary;
} ESP_COLLECTION_ENTRY;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Integer | An entry in an integer collection. |
| String | An entry in a string collection. |
| Binary | An entry in a binary collection. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BUFFER`](wesp-common-utilities.md#esp_buffer)
- [`ESP_UNICODE_STRING`](wesp-common-utilities.md#esp_unicode_string)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_COLLECTION_UPDATE_ENTRY

The structure `ESP_COLLECTION_UPDATE_ENTRY` is used with the API `EspUpdateCollection` to update a collection.

#### Syntax

```cpp
typedef struct ESP_COLLECTION_UPDATE_ENTRY
{
    ESP_COLLECTION_UPDATE_TYPE UpdateType;
    ESP_COLLECTION_ENTRY Entry;
} ESP_COLLECTION_UPDATE_ENTRY;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| UpdateType | Supplies the type of update to make. The following types are supported:<br>Add<br>Remove |
| Entry | Supplies the collection entry to update. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_COLLECTION_ENTRY`](wesp-collection-updates.md#esp_collection_entry)
- [`ESP_COLLECTION_UPDATE_TYPE`](wesp-collection-updates.md#esp_collection_update_type)
- [`EspUpdateCollection`](wesp-collection-updates.md#espupdatecollection)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
