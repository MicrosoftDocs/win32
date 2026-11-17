---
title: "WESP shared event object APIs and types"
description: "Windows endpoint security platform API reference for shared event object APIs and types, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- EspGetEventObjectId
- EspGetEventObjectType
- EspCreateEventObjectReference
- EspCreateEventObjectReferenceById
- EspDuplicateEventObjectReference
- EspGetEventObjectFromReference
- EspCloseEventObjectReference
- ESP_EVENT_OBJECT
- ESP_EVENT_OBJECT_REF
- ESP_EVENT_OBJECT_TYPE
- ESP_EVENT_OBJECT_INFO
- ESP_EVENT_OBJECT_CONFIG
---

# Shared event object APIs and types

This page contains reference entries in the [Event objects API family](wesp-api-reference.md#event-objects). Each entry includes its declaration and requirements.

## Shared functions

### EspGetEventObjectId

The API `EspGetEventObjectId` can be used to retrieve an event object's id.

#### Syntax

```cpp
HRESULT
WINAPI
EspGetEventObjectId(
    _In_ ESP_EVENT_OBJECT Object,
    _Out_ UINT64* ObjectId
    );
```

#### Parameters

##### `Object`

Supplies the event object.

##### `ObjectId`

Receives the event object id.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_EVENT_OBJECT`](wesp-event-object-references.md#esp_event_object)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspGetEventObjectType

The API `EspGetEventObjectType` can be used to retrieve an event object's type.

#### Syntax

```cpp
HRESULT
WINAPI
EspGetEventObjectType(
    _In_ ESP_EVENT_OBJECT Object,
    _Out_ ESP_EVENT_OBJECT_TYPE* Type
    );
```

#### Parameters

##### `Object`

Supplies the event object.

##### `Type`

Receives the event object type.  The following event object types are supported.<br>Thread: represents a thread instance (i.e. ETHREAD).<br>Process: represents a process instance (i.e. EPROCESS).<br>File Stream: represents a physical file stream on a volume.<br>File: represents a physical file on a volume. Its properties describe persistent, on-disk state such as attributes, timestamps, security descriptor, and file ID. A file exists independently of any open handles.<br>File Object: represents a single open instance of a file, equivalent to a kernel FILE_OBJECT. Multiple file objects can refer to the same underlying file simultaneously, each with its own access mode, share access, flags, etc. A file object's target can be a file stream, volume, pipe, or mailslot (see `ESP_FO_TARGET_OBJECT_TYPE`).<br>Volume: represents a physical volume.<br>Disk: represents a physical disk.<br>Registry Key: represents a persistent registry key in a registry hive. Its properties describe the key's durable state such as its path, whether it is a symbolic link, and its security descriptor.<br>Registry Key Object: represents an open handle to a registry key, equivalent to the kernel PVOID Object supplied to registry callback routines (e.g. REG_POST_OPERATION_INFORMATION). Multiple registry key objects can refer to the same underlying registry key simultaneously. A registry key object tracks per-open state such as whether it was opened transactionally and its object ID.<br>Desktop: represents a Desktop OB object instance (i.e. ExDesktopObjectType).<br>KTM Transaction: represents a KTM transaction instance.<br>Pipe: represents a pipe instance.<br>Mailslot: represents a mailslot instance.<br>Token: represents a token instance (i.e. ACCESS_TOKEN).

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_EVENT_OBJECT`](wesp-event-object-references.md#esp_event_object)
- [`ESP_EVENT_OBJECT_TYPE`](wesp-event-object-references.md#esp_event_object_type)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspCreateEventObjectReference

The API `EspCreateEventObjectReference` is used to create a reference to an event object. This API is useful when processing an event notification to acquire a reference to an event object associated with the event. A client can use this reference to query properties for the event object, or set context keys, after they've completed the event notification. These references keep the event object alive and allow the client to query or set context keys, but they do not keep the associated kernel object alive. Event object references are automatically closed when the client disconnects, or their process terminates.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateEventObjectReference(
    _In_ ESP_EVENT_OBJECT Object,
    _Out_ ESP_EVENT_OBJECT_REF* ObjectRef
    );
```

#### Parameters

##### `Object`

Supplies the event object.

##### `ObjectRef`

Receives the event object reference. The caller must call `EspCloseEventObjectReference` once they no longer need it.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_EVENT_OBJECT`](wesp-event-object-references.md#esp_event_object)
- [`ESP_EVENT_OBJECT_REF`](wesp-event-object-references.md#esp_event_object_ref)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspCreateEventObjectReferenceById

The API `EspCreateEventObjectReference` is used to create a reference to an event object using its event object ID.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateEventObjectReferenceById(
    _In_ ESP_CLIENT Client,
    _In_ UINT64 ObjectId,
    _Out_ ESP_EVENT_OBJECT_REF* ObjectRef
    );
```

#### Parameters

##### `Client`

Supplies the client.

##### `ObjectId`

Supplies the event object id.

##### `ObjectRef`

Receives the event object reference. The caller must call `EspCloseEventObjectReference` once they no longer need it.

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
- [`EspCreateEventObjectReference`](wesp-event-object-references.md#espcreateeventobjectreference)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspDuplicateEventObjectReference

The API `EspDuplicateEventObjectReference` duplicates an existing event object reference.

#### Syntax

```cpp
HRESULT
WINAPI
EspDuplicateEventObjectReference(
    _In_ ESP_EVENT_OBJECT_REF ObjectRef,
    _Out_ ESP_EVENT_OBJECT_REF* DuplicateRef
    );
```

#### Parameters

##### `ObjectRef`

Supplies the event object reference to duplicate.

##### `DuplicateRef`

Receives the duplicate event object reference. The reference must be closed by calling `EspCloseEventObjectReference` once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_EVENT_OBJECT_REF`](wesp-event-object-references.md#esp_event_object_ref)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspGetEventObjectFromReference

The API `EspGetEventObjectFromReference` retrieves the event object (`ESP_EVENT_OBJECT`) from a strong reference (`ESP_EVENT_OBJECT_REF`). The returned `ESP_EVENT_OBJECT` is valid for as long as the reference is held.

#### Syntax

```cpp
HRESULT
WINAPI
EspGetEventObjectFromReference(
    _In_ ESP_EVENT_OBJECT_REF ObjectRef,
    _Out_ ESP_EVENT_OBJECT* Object
    );
```

#### Parameters

##### `ObjectRef`

Supplies the event object reference.

##### `Object`

Receives the event object.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_EVENT_OBJECT`](wesp-event-object-references.md#esp_event_object)
- [`ESP_EVENT_OBJECT_REF`](wesp-event-object-references.md#esp_event_object_ref)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspCloseEventObjectReference

The API `EspCloseEventObjectReference` is used to close an event object reference that was previously acquired by calling `EspCreateEventObjectReference`. This API can only fail if an invalid reference is supplied (e.g. NULL).

#### Syntax

```cpp
HRESULT
WINAPI
EspCloseEventObjectReference(
    _In_ _Post_invalid_ ESP_EVENT_OBJECT_REF ObjectRef
    );
```

#### Parameters

##### `ObjectRef`

Supplies the event object reference to close. The supplied "ObjectRef" cannot be used after this API returns.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_EVENT_OBJECT_REF`](wesp-event-object-references.md#esp_event_object_ref)
- [`EspCreateEventObjectReference`](wesp-event-object-references.md#espcreateeventobjectreference)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Shared handles and types

### ESP_EVENT_OBJECT

Identifies a WESP event object.

#### Syntax

```cpp
DECLARE_HANDLE(ESP_EVENT_OBJECT);
```

#### Remarks

Use `EspCreateEventObjectReference` to create a reference to an event object. Release that reference with `EspCloseEventObjectReference`.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_EVENT_OBJECT_REF

Identifies a reference to a WESP event object.

#### Syntax

```cpp
DECLARE_HANDLE(ESP_EVENT_OBJECT_REF);
```

#### Remarks

Obtain this handle with `EspCreateEventObjectReference`. Release it with `EspCloseEventObjectReference`.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_EVENT_OBJECT_TYPE

The enum `ESP_EVENT_OBJECT_TYPE` defines an event object type.

#### Syntax

```cpp
typedef enum ESP_EVENT_OBJECT_TYPE
{
    ESP_EVENT_OBJECT_TYPE_NONE = 0,
    ESP_EVENT_OBJECT_TYPE_THREAD,
    ESP_EVENT_OBJECT_TYPE_PROCESS,
    ESP_EVENT_OBJECT_TYPE_FILE,
    ESP_EVENT_OBJECT_TYPE_FILE_OBJECT,
    ESP_EVENT_OBJECT_TYPE_FILE_STREAM,
    ESP_EVENT_OBJECT_TYPE_VOLUME,
    ESP_EVENT_OBJECT_TYPE_DISK,
    ESP_EVENT_OBJECT_TYPE_REGISTRY_KEY,
    ESP_EVENT_OBJECT_TYPE_REGISTRY_KEY_OBJECT,
    ESP_EVENT_OBJECT_TYPE_DESKTOP,
    ESP_EVENT_OBJECT_TYPE_KTM_TRANSACTION,
    ESP_EVENT_OBJECT_TYPE_PIPE,
    ESP_EVENT_OBJECT_TYPE_MAILSLOT,
    ESP_EVENT_OBJECT_TYPE_TOKEN
} ESP_EVENT_OBJECT_TYPE;
```

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_EVENT_OBJECT_INFO

The structure `ESP_EVENT_OBJECT_INFO` specifies information for an event object. This structure is supplied as part of an event notification (one for each event object associated with an event) and contains various details about the event object.

#### Syntax

```cpp
typedef struct ESP_EVENT_OBJECT_INFO
{
    _Maybenull_ ESP_EVENT_OBJECT Object;
    ESP_PROPERTY_QUERY PropertyQuery;
} ESP_EVENT_OBJECT_INFO;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Object | Specifies the raw event object. This field is null unless `IncludeInNotification` in the corresponding `ESP_EVENT_OBJECT_CONFIG` structure was set to true. |
| PropertyQuery | Specifies the queried properties for the event object. These properties are requested through the corresponding per-type configuration, such as `ESP_THREAD_CONFIG.Properties`. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EVENT_OBJECT`](wesp-event-object-references.md#esp_event_object)
- [`ESP_PROPERTY_QUERY`](wesp-property-queries.md#esp_property_query)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_EVENT_OBJECT_CONFIG

The structure `ESP_EVENT_OBJECT_CONFIG` is used to set configuration for an event object associated with a rule. This allows the client to configure various things for an event object such as its filter, context key updates, and binding keys. Each event object type's configuration structure (e.g. `ESP_THREAD_CONFIG`) embeds an `ESP_EVENT_OBJECT_CONFIG` structure.

#### Syntax

```cpp
typedef struct ESP_EVENT_OBJECT_CONFIG
{
    ESP_FILTER Filter;
    ESP_CONTEXT_KEY_CONFIG ContextConfig;
    BOOL IncludeInNotification;
    UINT32 BindingsCount;
    _Field_size_(BindingsCount) const ESP_PROPERTY_BINDING* Bindings;
} ESP_EVENT_OBJECT_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Filter | Specifies a filter for the event object. The filter must be of the same type as the event object. For example, the `ESP_EVENT_OBJECT_CONFIG` structure within an `ESP_THREAD_CONFIG` structure must specify a filter created through `EspCreateThreadFilter`, or be composed of filters created through `EspCreateThreadFilter`. |
| ContextConfig | Specifies an `ESP_CONTEXT_KEY_CONFIG` structure. This structure can be used to configure context key updates and capture binding keys for the event object. |
| IncludeInNotification | Specifies a boolean indicating whether the event object should be supplied as part of the notification. If true, the `ESP_EVENT_OBJECT` will be supplied. If false, the `ESP_EVENT_OBJECT` will not be supplied. |
| BindingsCount | Specifies the number of elements in the "Bindings" array. |
| Bindings | Specifies an array of property bindings. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_CONTEXT_KEY_CONFIG`](wesp-context-key-management.md#esp_context_key_config)
- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [`ESP_PROPERTY_BINDING`](wesp-rule-configuration.md#esp_property_binding)
- [`ESP_THREAD_CONFIG`](wesp-execution-objects.md#esp_thread_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
