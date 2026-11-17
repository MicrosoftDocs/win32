---
title: "WESP collection creation and management"
description: "Windows endpoint security platform API reference for collection creation and management, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- EspCreateCollection
- EspOpenCollection
- EspCloseCollection
- EspGetCollectionId
- EspGetCollectionType
- EspEnumerateCollectionIds
- EspEnumerateCollectionEntries
- ESP_COLLECTION
- ESP_COLLECTION_TYPE
- ESP_COLLECTION_LIFETIME
- ESP_COLLECTION_DESCRIPTOR
---

# Collection creation and management

This page contains reference entries in the [Collections API family](wesp-api-reference.md#collections). Each entry includes its declaration and requirements.

## Collection functions

### EspCreateCollection

The API `EspCreateCollection` is used to create a new collection for a client.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateCollection(
    _In_ ESP_CLIENT Client,
    _In_ const ESP_COLLECTION_DESCRIPTOR* Descriptor,
    _Out_ ESP_COLLECTION* Collection
    );
```

#### Parameters

##### `Client`

Supplies the client for which to create the collection.

##### `Descriptor`

Supplies an `ESP_COLLECTION_DESCRIPTOR` structure that describes the collection.

##### `Collection`

Receives a reference to the collection. This reference must be closed by calling `EspCloseCollection` once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_COLLECTION`](wesp-collection-management.md#esp_collection)
- [`ESP_COLLECTION_DESCRIPTOR`](wesp-collection-management.md#esp_collection_descriptor)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspOpenCollection

The API `EspOpenCollection` is used to open a reference to a collection using its id.

#### Syntax

```cpp
HRESULT
WINAPI
EspOpenCollection(
    _In_ ESP_CLIENT Client,
    _In_ const GUID* CollectionId,
    _Out_ ESP_COLLECTION* Collection
    );
```

#### Parameters

##### `Client`

Supplies the client.

##### `CollectionId`

Supplies the collection id.

##### `Collection`

Receives a reference to the collection. This reference must be closed by calling `EspCloseCollection` once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_COLLECTION`](wesp-collection-management.md#esp_collection)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspCloseCollection

The API `EspCloseCollection` is used to close a reference to an `ESP_COLLECTION` object. Closing a collection does not delete the collection; it simply closes the client's local reference.

#### Syntax

```cpp
HRESULT
WINAPI
EspCloseCollection(
    _In_ _Post_invalid_ ESP_COLLECTION Collection
    );
```

#### Parameters

##### `Collection`

Supplies the collection to close. The supplied "Collection" cannot be used after this API returns.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_COLLECTION`](wesp-collection-management.md#esp_collection)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspGetCollectionId

The API `EspGetCollectionId` retrieves the collection identifier. Each collection has a unique identifier that is generated when the collection is created.

#### Syntax

```cpp
HRESULT
WINAPI
EspGetCollectionId(
    _In_ ESP_COLLECTION Collection,
    _Out_ GUID* CollectionId
    );
```

#### Parameters

##### `Collection`

Supplies the collection.

##### `CollectionId`

Receives the collection id.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_COLLECTION`](wesp-collection-management.md#esp_collection)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspGetCollectionType

The API `EspGetCollectionType` retrieves the collection type.

#### Syntax

```cpp
HRESULT
WINAPI
EspGetCollectionType(
    _In_ ESP_COLLECTION Collection,
    _Out_ ESP_COLLECTION_TYPE* Type
    );
```

#### Parameters

##### `Collection`

Supplies the collection.

##### `Type`

Receives the collection type.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_COLLECTION`](wesp-collection-management.md#esp_collection)
- [`ESP_COLLECTION_TYPE`](wesp-collection-management.md#esp_collection_type)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspEnumerateCollectionIds

The API `EspEnumerateCollectionIds` enumerates the client's collection IDs with the specified lifetime.

#### Syntax

```cpp
HRESULT
WINAPI
EspEnumerateCollectionIds(
    _In_ ESP_CLIENT Client,
    _In_ ESP_COLLECTION_LIFETIME Lifetime,
    _Out_ UINT32* CollectionIdsCount,
    _Outptr_result_buffer_all_(*CollectionIdsCount) GUID** CollectionIds
    );
```

#### Parameters

##### `Client`

Specifies the client.

##### `Lifetime`

Specifies the lifetime to enumerate.

##### `CollectionIdsCount`

Receives the number of elements in the CollectionIds array.

##### `CollectionIds`

Receives an array of collection IDs. This array must be freed by calling `EspFreeMemory`.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_COLLECTION_LIFETIME`](wesp-collection-management.md#esp_collection_lifetime)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspEnumerateCollectionEntries

The API `EspEnumerateCollectionEntries` is used to retrieve all the entries in a collection. Clients can use this API to look at the current set of entries in a collection.

#### Syntax

```cpp
HRESULT
WINAPI
EspEnumerateCollectionEntries(
    _In_ ESP_COLLECTION Collection,
    _Out_ UINT32* EntriesCount,
    _Outptr_result_buffer_all_(*EntriesCount) ESP_COLLECTION_ENTRY** Entries
    );
```

#### Parameters

##### `Collection`

Supplies the collection.

##### `EntriesCount`

Receives the number of elements in the entries array.

##### `Entries`

Receives an array of collection entries. This array must be freed by calling `EspFreeMemory`.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_COLLECTION`](wesp-collection-management.md#esp_collection)
- [`ESP_COLLECTION_ENTRY`](wesp-collection-updates.md#esp_collection_entry)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Collection handle and types

### ESP_COLLECTION

Identifies a WESP collection.

#### Syntax

```cpp
DECLARE_HANDLE(ESP_COLLECTION);
```

#### Remarks

Obtain this handle with `EspCreateCollection`. Release it with `EspCloseCollection`.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_COLLECTION_TYPE

The enum `ESP_COLLECTION_TYPE` specifies a kind of collection.

#### Syntax

```cpp
typedef enum ESP_COLLECTION_TYPE
{
    ESP_COLLECTION_TYPE_NONE = 0,
    ESP_COLLECTION_TYPE_INTEGER,
    ESP_COLLECTION_TYPE_STRING,
    ESP_COLLECTION_TYPE_BINARY
} ESP_COLLECTION_TYPE;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_COLLECTION_TYPE_INTEGER` | The collection contains string entries. Each entry in the collection is a UINT64. |
| `ESP_COLLECTION_TYPE_STRING` | The collection contains string entries. Each entry in the collection is a `ESP_UNICODE_STRING`. |
| `ESP_COLLECTION_TYPE_BINARY` | The collection contains binary entries. Each entry in the collection is a `ESP_BUFFER`. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_COLLECTION_LIFETIME

The enum `ESP_COLLECTION_LIFETIME` specifies the lifetime of a collection.

#### Syntax

```cpp
typedef enum ESP_COLLECTION_LIFETIME
{
    ESP_COLLECTION_LIFETIME_NONE = 0,
    ESP_COLLECTION_LIFETIME_CLIENT_SESSION,
    ESP_COLLECTION_LIFETIME_BOOT_SESSION,
    ESP_COLLECTION_LIFETIME_PERSISTED
} ESP_COLLECTION_LIFETIME;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_COLLECTION_LIFETIME_CLIENT_SESSION` | The collection's lifetime is tied to the client's session. If the client disconnects, the collection is destroyed. |
| `ESP_COLLECTION_LIFETIME_BOOT_SESSION` | The collection's lifetime is tied to the current boot session. The collection is deleted when the machine reboots. |
| `ESP_COLLECTION_LIFETIME_PERSISTED` | The collection's lifetime is persisted across boot sessions. If a rule is persisted, its filter can only be associated with persisted collections. A persisted collection is automatically deleted when there are no longer any rules that reference it. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_COLLECTION_DESCRIPTOR

The structure `ESP_COLLECTION_DESCRIPTOR` describes a collection. It is supplied when a collection is created (i.e. `EspCreateCollection`).

typedef struct `ESP_COLLECTION_DESCRIPTOR`

{

GUID CollectionId;

`ESP_COLLECTION_TYPE` CollectionType;

`ESP_COLLECTION_LIFETIME` Lifetime;

`ESP_STRING_COLLECTION_FLAGS` StringFlags;

} `ESP_COLLECTION_DESCRIPTOR`;

#### Syntax

```cpp
typedef struct ESP_COLLECTION_DESCRIPTOR
{
    GUID CollectionId;
    ESP_COLLECTION_TYPE CollectionType;
    ESP_COLLECTION_LIFETIME Lifetime;
    ESP_STRING_COLLECTION_FLAGS StringFlags;
} ESP_COLLECTION_DESCRIPTOR;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| CollectionId | Specifies the collection's unique identifier. If a zeroed-guid is supplied, the collection ID is randomly generated. |
| CollectionType | Specifies the collection's type. The supported types are:<br>Integer<br>String<br>Binary |
| Lifetime | Specifies the collection's lifetime. |
| StringFlags | Specifies flags for the collection when the collection type is string. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_COLLECTION_LIFETIME`](wesp-collection-management.md#esp_collection_lifetime)
- [`ESP_COLLECTION_TYPE`](wesp-collection-management.md#esp_collection_type)
- [`ESP_STRING_COLLECTION_FLAGS`](wesp-collection-updates.md#esp_string_collection_flags)
- [`EspCreateCollection`](wesp-collection-management.md#espcreatecollection)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
