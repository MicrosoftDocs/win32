---
title: "WESP filter creation and composition"
description: "Windows endpoint security platform API reference for filter creation and composition, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- EspCreateFilter
- EspCloseFilter
- EspCreateAndFilter
- EspCreateOrFilter
- EspCreateXorFilter
- EspCreateNotFilter
- EspCreateThreadFilter
- EspCreateProcessFilter
- EspCreateFileStreamFilter
- EspCreateFileFilter
- EspCreateFileObjectFilter
- EspCreateVolumeFilter
- EspCreateDiskFilter
- EspCreateRegistryKeyFilter
- EspCreateRegistryKeyObjectFilter
- EspCreateDesktopFilter
- EspCreateKtmTransactionFilter
- EspCreatePipeFilter
- EspCreateMailslotFilter
- EspCreateTokenFilter
- EspCreateClientFilter
- EspCreateEventFilter
- ESP_FILTER
---

# Filter creation and composition

This page contains reference entries in the [Filters API family](wesp-api-reference.md#filters). Each entry includes its declaration and requirements.

## Creation and composition functions

### EspCreateFilter

The API `EspCreateFilter` is used to create a non-typed filter -- a filter that isn't associated with any property ID. This is used to filter standalone fields of an event such as the desired access of a file-object-create event or the value name of a registry set-value-key event.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateFilter(
    _In_ ESP_COMPARISON_TYPE ComparisonType,
    _In_ const void* Comparison,
    _Out_ ESP_FILTER* Filter
    );
```

#### Parameters

##### `ComparisonType`

The comparison type. This determines the expected structure that the "Comparison" parameter points to.

##### `Comparison`

The comparison structure.

##### `Filter`

Receives a reference to the filter. This reference must be closed by calling `EspCloseFilter` once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_COMPARISON_TYPE`](wesp-filter-comparison-types.md#esp_comparison_type)
- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspCloseFilter

The API `EspCloseFilter` is used to close a reference to a `ESP_FILTER` object. It should be called by clients once they no longer need their `ESP_FILTER` object.

#### Syntax

```cpp
HRESULT
WINAPI
EspCloseFilter(
    _In_ _Post_invalid_ ESP_FILTER Filter
    );
```

#### Parameters

##### `Filter`

Supplies the filter to close. The supplied "Filter" cannot be used after this API returns.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspCreateAndFilter

The API `EspCreateAndFilter` is used to create a composite filter that represents the logical conjunction (AND) of two existing filters. This is useful when defining rules that must match multiple filters.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateAndFilter(
    _In_ ESP_FILTER Left,
    _In_ ESP_FILTER Right,
    _Out_ ESP_FILTER* NewFilter
    );
```

#### Parameters

##### `Left`

Supplies a filter for the left side of the AND expression.

##### `Right`

Supplies a filter for the right side of the AND expression.

##### `NewFilter`

Receives a new filter reference that is the logical expression "Left AND Right". This reference must be closed by calling `EspCloseFilter` once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspCreateOrFilter

The API `EspCreateOrFilter` is used to create a composite filter that represents the logical disjunction (OR) of two existing filters. This is useful when defining rules that must match one or more filters.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateOrFilter(
    _In_ ESP_FILTER Left,
    _In_ ESP_FILTER Right,
    _Out_ ESP_FILTER* NewFilter
    );
```

#### Parameters

##### `Left`

Supplies a filter for the left side of the OR expression.

##### `Right`

Supplies a filter for the right side of the OR expression.

##### `NewFilter`

Receives a new filter reference that is the logical expression "Left OR Right". This reference must be closed by calling `EspCloseFilter` once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspCreateXorFilter

The API `EspCreateXorFilter` is used to create a composite filter that represents the logical exclusive disjunction (XOR) of two existing filters. This is useful when defining rules that must match exactly one filter, but not both.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateXorFilter(
    _In_ ESP_FILTER Left,
    _In_ ESP_FILTER Right,
    _Out_ ESP_FILTER* NewFilter
    );
```

#### Parameters

##### `Left`

Supplies a filter for the left side of the XOR expression.

##### `Right`

Supplies a filter for the right side of the XOR expression.

##### `NewFilter`

Receives a new filter reference that is the logical expression "Left XOR Right". This reference must be closed by calling `EspCloseFilter` once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspCreateNotFilter

The API `EspCreateNotFilter` is used to create a composite filter that represents the logical negation (NOT) of a filter. This is useful when defining rules that must match if a filter matches to FALSE.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateNotFilter(
    _In_ ESP_FILTER Filter,
    _Out_ ESP_FILTER* NewFilter
    );
```

#### Parameters

##### `Filter`

Supplies the filter to be used for creating its logical negation.

##### `NewFilter`

Receives a new filter reference that is the logical negation of the supplied filter. This reference must be closed by calling `EspCloseFilter` once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspCreateThreadFilter

The API `EspCreateThreadFilter` is used to create a filter for a thread event object. This allows clients to filter on thread properties.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateThreadFilter(
    _In_ ESP_THREAD_PROPERTY_ID PropertyId,
    _In_ ESP_COMPARISON_TYPE ComparisonType,
    _In_ const void* Comparison,
    _Out_ ESP_FILTER* Filter
    );
```

#### Parameters

##### `PropertyId`

The property ID to compare.

##### `ComparisonType`

The comparison type. This determines the expected structure that the "Comparison" parameter points to.

##### `Comparison`

The comparison structure.

##### `Filter`

Receives a reference to the filter. This reference must be closed by calling `EspCloseFilter` once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_COMPARISON_TYPE`](wesp-filter-comparison-types.md#esp_comparison_type)
- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [`ESP_THREAD_PROPERTY_ID`](wesp-execution-property-ids.md#esp_thread_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspCreateProcessFilter

The API `EspCreateProcessFilter` is used to create a filter for a process event object. This allows clients to filter on process properties.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateProcessFilter(
    _In_ ESP_PROCESS_PROPERTY_ID PropertyId,
    _In_ ESP_COMPARISON_TYPE ComparisonType,
    _In_ const void* Comparison,
    _Out_ ESP_FILTER* Filter
    );
```

#### Parameters

##### `PropertyId`

The property ID to compare.

##### `ComparisonType`

The comparison type. This determines the expected structure that the "Comparison" parameter points to.

##### `Comparison`

The comparison structure.

##### `Filter`

Receives a reference to the filter. This reference must be closed by calling `EspCloseFilter` once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_COMPARISON_TYPE`](wesp-filter-comparison-types.md#esp_comparison_type)
- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [`ESP_PROCESS_PROPERTY_ID`](wesp-execution-property-ids.md#esp_process_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspCreateFileStreamFilter

The API `EspCreateFileStreamFilter` is used to create a filter for a file stream event object. This allows clients to filter on file stream properties.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateFileStreamFilter(
    _In_ ESP_FILE_STREAM_PROPERTY_ID PropertyId,
    _In_ ESP_COMPARISON_TYPE ComparisonType,
    _In_ const void* Comparison,
    _Out_ ESP_FILTER* Filter
    );
```

#### Parameters

##### `PropertyId`

The property ID to compare.

##### `ComparisonType`

The comparison type. This determines the expected structure that the "Comparison" parameter points to.

##### `Comparison`

The comparison structure.

##### `Filter`

Receives a reference to the filter. This reference must be closed by calling `EspCloseFilter` once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_COMPARISON_TYPE`](wesp-filter-comparison-types.md#esp_comparison_type)
- [`ESP_FILE_STREAM_PROPERTY_ID`](wesp-file-property-ids.md#esp_file_stream_property_id)
- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspCreateFileFilter

The API `EspCreateFileFilter` is used to create a filter for a file event object. This allows clients to filter on file properties.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateFileFilter(
    _In_ ESP_FILE_PROPERTY_ID PropertyId,
    _In_ ESP_COMPARISON_TYPE ComparisonType,
    _In_ const void* Comparison,
    _Out_ ESP_FILTER* Filter
    );
```

#### Parameters

##### `PropertyId`

The property ID to compare.

##### `ComparisonType`

The comparison type. This determines the expected structure that the "Comparison" parameter points to.

##### `Comparison`

The comparison structure.

##### `Filter`

Receives a reference to the filter. This reference must be closed by calling `EspCloseFilter` once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_COMPARISON_TYPE`](wesp-filter-comparison-types.md#esp_comparison_type)
- [`ESP_FILE_PROPERTY_ID`](wesp-file-property-ids.md#esp_file_property_id)
- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspCreateFileObjectFilter

The API `EspCreateFileObjectFilter` is used to create a filter for a file object event object. This allows clients to filter on file object properties.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateFileObjectFilter(
    _In_ ESP_FILE_OBJECT_PROPERTY_ID PropertyId,
    _In_ ESP_COMPARISON_TYPE ComparisonType,
    _In_ const void* Comparison,
    _Out_ ESP_FILTER* Filter
    );
```

#### Parameters

##### `PropertyId`

The property ID to compare.

##### `ComparisonType`

The comparison type. This determines the expected structure that the "Comparison" parameter points to.

##### `Comparison`

The comparison structure.

##### `Filter`

Receives a reference to the filter. This reference must be closed by calling `EspCloseFilter` once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_COMPARISON_TYPE`](wesp-filter-comparison-types.md#esp_comparison_type)
- [`ESP_FILE_OBJECT_PROPERTY_ID`](wesp-file-property-ids.md#esp_file_object_property_id)
- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspCreateVolumeFilter

The API `EspCreateVolumeFilter` is used to create a filter for a volume event object. This allows clients to filter on volume properties.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateVolumeFilter(
    _In_ ESP_VOLUME_PROPERTY_ID PropertyId,
    _In_ ESP_COMPARISON_TYPE ComparisonType,
    _In_ const void* Comparison,
    _Out_ ESP_FILTER* Filter
    );
```

#### Parameters

##### `PropertyId`

The property ID to compare.

##### `ComparisonType`

The comparison type. This determines the expected structure that the "Comparison" parameter points to.

##### `Comparison`

The comparison structure.

##### `Filter`

Receives a reference to the filter. This reference must be closed by calling `EspCloseFilter` once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_COMPARISON_TYPE`](wesp-filter-comparison-types.md#esp_comparison_type)
- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [`ESP_VOLUME_PROPERTY_ID`](wesp-file-property-ids.md#esp_volume_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspCreateDiskFilter

The API `EspCreateDiskFilter` is used to create a filter for a disk event object. This allows clients to filter on disk properties.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateDiskFilter(
    _In_ ESP_DISK_PROPERTY_ID PropertyId,
    _In_ ESP_COMPARISON_TYPE ComparisonType,
    _In_ const void* Comparison,
    _Out_ ESP_FILTER* Filter
    );
```

#### Parameters

##### `PropertyId`

The property ID to compare.

##### `ComparisonType`

The comparison type. This determines the expected structure that the "Comparison" parameter points to.

##### `Comparison`

The comparison structure.

##### `Filter`

Receives a reference to the filter. This reference must be closed by calling `EspCloseFilter` once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_COMPARISON_TYPE`](wesp-filter-comparison-types.md#esp_comparison_type)
- [`ESP_DISK_PROPERTY_ID`](wesp-file-property-ids.md#esp_disk_property_id)
- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspCreateRegistryKeyFilter

The API `EspCreateRegistryKeyFilter` is used to create a filter for a registry key event object. This allows clients to filter on registry key properties.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateRegistryKeyFilter(
    _In_ ESP_REGISTRY_KEY_PROPERTY_ID PropertyId,
    _In_ ESP_COMPARISON_TYPE ComparisonType,
    _In_ const void* Comparison,
    _Out_ ESP_FILTER* Filter
    );
```

#### Parameters

##### `PropertyId`

The property ID to compare.

##### `ComparisonType`

The comparison type. This determines the expected structure that the "Comparison" parameter points to.

##### `Comparison`

The comparison structure.

##### `Filter`

Receives a reference to the filter. This reference must be closed by calling `EspCloseFilter` once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_COMPARISON_TYPE`](wesp-filter-comparison-types.md#esp_comparison_type)
- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [`ESP_REGISTRY_KEY_PROPERTY_ID`](wesp-other-property-ids.md#esp_registry_key_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspCreateRegistryKeyObjectFilter

The API `EspCreateRegistryKeyObjectFilter` is used to create a filter for a registry key object event object. This allows clients to filter on registry key object properties.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateRegistryKeyObjectFilter(
    _In_ ESP_REGISTRY_KEY_OBJECT_PROPERTY_ID PropertyId,
    _In_ ESP_COMPARISON_TYPE ComparisonType,
    _In_ const void* Comparison,
    _Out_ ESP_FILTER* Filter
    );
```

#### Parameters

##### `PropertyId`

The property ID to compare.

##### `ComparisonType`

The comparison type. This determines the expected structure that the "Comparison" parameter points to.

##### `Comparison`

The comparison structure.

##### `Filter`

Receives a reference to the filter. This reference must be closed by calling `EspCloseFilter` once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_COMPARISON_TYPE`](wesp-filter-comparison-types.md#esp_comparison_type)
- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [`ESP_REGISTRY_KEY_OBJECT_PROPERTY_ID`](wesp-other-property-ids.md#esp_registry_key_object_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspCreateDesktopFilter

The API `EspCreateDesktopFilter` is used to create a filter for a desktop event object. This allows clients to filter on desktop properties.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateDesktopFilter(
    _In_ ESP_DESKTOP_PROPERTY_ID PropertyId,
    _In_ ESP_COMPARISON_TYPE ComparisonType,
    _In_ const void* Comparison,
    _Out_ ESP_FILTER* Filter
    );
```

#### Parameters

##### `PropertyId`

The property ID to compare.

##### `ComparisonType`

The comparison type. This determines the expected structure that the "Comparison" parameter points to.

##### `Comparison`

The comparison structure.

##### `Filter`

Receives a reference to the filter. This reference must be closed by calling `EspCloseFilter` once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_COMPARISON_TYPE`](wesp-filter-comparison-types.md#esp_comparison_type)
- [`ESP_DESKTOP_PROPERTY_ID`](wesp-other-property-ids.md#esp_desktop_property_id)
- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspCreateKtmTransactionFilter

The API `EspCreateKtmTransactionFilter` is used to create a filter for a KTM transaction event object. This allows clients to filter on KTM transaction properties.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateKtmTransactionFilter(
    _In_ ESP_KTM_TRANSACTION_PROPERTY_ID PropertyId,
    _In_ ESP_COMPARISON_TYPE ComparisonType,
    _In_ const void* Comparison,
    _Out_ ESP_FILTER* Filter
    );
```

#### Parameters

##### `PropertyId`

The property ID to compare.

##### `ComparisonType`

The comparison type. This determines the expected structure that the "Comparison" parameter points to.

##### `Comparison`

The comparison structure.

##### `Filter`

Receives a reference to the filter. This reference must be closed by calling `EspCloseFilter` once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_COMPARISON_TYPE`](wesp-filter-comparison-types.md#esp_comparison_type)
- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [`ESP_KTM_TRANSACTION_PROPERTY_ID`](wesp-other-property-ids.md#esp_ktm_transaction_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspCreatePipeFilter

The API `EspCreatePipeFilter` is used to create a filter for a pipe event object. This allows clients to filter on pipe properties.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreatePipeFilter(
    _In_ ESP_PIPE_PROPERTY_ID PropertyId,
    _In_ ESP_COMPARISON_TYPE ComparisonType,
    _In_ const void* Comparison,
    _Out_ ESP_FILTER* Filter
    );
```

#### Parameters

##### `PropertyId`

The property ID to compare.

##### `ComparisonType`

The comparison type. This determines the expected structure that the "Comparison" parameter points to.

##### `Comparison`

The comparison structure.

##### `Filter`

Receives a reference to the filter. This reference must be closed by calling `EspCloseFilter` once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_COMPARISON_TYPE`](wesp-filter-comparison-types.md#esp_comparison_type)
- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [`ESP_PIPE_PROPERTY_ID`](wesp-other-property-ids.md#esp_pipe_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspCreateMailslotFilter

The API `EspCreateMailslotFilter` is used to create a filter for a mailslot event object. This allows clients to filter on mailslot properties.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateMailslotFilter(
    _In_ ESP_MAILSLOT_PROPERTY_ID PropertyId,
    _In_ ESP_COMPARISON_TYPE ComparisonType,
    _In_ const void* Comparison,
    _Out_ ESP_FILTER* Filter
    );
```

#### Parameters

##### `PropertyId`

The property ID to compare.

##### `ComparisonType`

The comparison type. This determines the expected structure that the "Comparison" parameter points to.

##### `Comparison`

The comparison structure.

##### `Filter`

Receives a reference to the filter. This reference must be closed by calling `EspCloseFilter` once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_COMPARISON_TYPE`](wesp-filter-comparison-types.md#esp_comparison_type)
- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [`ESP_MAILSLOT_PROPERTY_ID`](wesp-other-property-ids.md#esp_mailslot_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspCreateTokenFilter

The API `EspCreateTokenFilter` is used to create a filter for a token event object. This allows clients to filter on token properties.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateTokenFilter(
    _In_ ESP_TOKEN_PROPERTY_ID PropertyId,
    _In_ ESP_COMPARISON_TYPE ComparisonType,
    _In_ const void* Comparison,
    _Out_ ESP_FILTER* Filter
    );
```

#### Parameters

##### `PropertyId`

The property ID to compare.

##### `ComparisonType`

The comparison type. This determines the expected structure that the "Comparison" parameter points to.

##### `Comparison`

The comparison structure.

##### `Filter`

Receives a reference to the filter. This reference must be closed by calling `EspCloseFilter` once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_COMPARISON_TYPE`](wesp-filter-comparison-types.md#esp_comparison_type)
- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [`ESP_TOKEN_PROPERTY_ID`](wesp-execution-property-ids.md#esp_token_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspCreateClientFilter

The API `EspCreateClientFilter` is used to create a client filter. Client filters allow filtering on global context keys associated with the client. Client filters are useful in cases where a client wants to filter based on global policy. For example, let's say a client has a series of flags that represent whether a policy is enabled or disabled.  These flags can be stored in a client context key by calling `EspSetClientContextKey`, and then a context key comparison filter can be created that checks whether a flag is set. This client filter can then be associated with multiple rules. This provides a mechanism for toggling flags on/off in a client context key to enable or disable behavior without needing to update rules. Client properties are defined in the enum `ESP_CLIENT_PROPERTY_ID`.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateClientFilter(
    _In_ ESP_CLIENT_PROPERTY_ID PropertyId,
    _In_ ESP_COMPARISON_TYPE ComparisonType,
    _In_ const void* Comparison,
    _Out_ ESP_FILTER* Filter
    );
```

#### Parameters

##### `PropertyId`

The property ID to compare.

##### `ComparisonType`

The comparison type. This determines the expected structure that the "Comparison" parameter points to.

##### `Comparison`

The comparison structure.

##### `Filter`

Receives a reference to the filter. This reference must be closed by calling `EspCloseFilter` once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT_PROPERTY_ID`](wesp-execution-property-ids.md#esp_client_property_id)
- [`ESP_COMPARISON_TYPE`](wesp-filter-comparison-types.md#esp_comparison_type)
- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [`EspSetClientContextKey`](wesp-context-key-management.md#espsetclientcontextkey)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspCreateEventFilter

The API `EspCreateEventFilter` is used to create a filter for an event property. Event filters allow filtering on properties that are common to all events. For example, this allows a client to filter on the NTSTATUS of an event, the event time, whether the event originated from a WESP client, etc. Event properties are defined in the enum `ESP_EVENT_PROPERTY_ID`.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateEventFilter(
    _In_ ESP_EVENT_PROPERTY_ID PropertyId,
    _In_ ESP_COMPARISON_TYPE ComparisonType,
    _In_ const void* Comparison,
    _Out_ ESP_FILTER* Filter
    );
```

#### Parameters

##### `PropertyId`

The property ID to compare.

##### `ComparisonType`

The comparison type. This determines the expected structure that the "Comparison" parameter points to.

##### `Comparison`

The comparison structure.

##### `Filter`

Receives a reference to the filter. This reference must be closed by calling `EspCloseFilter` once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_COMPARISON_TYPE`](wesp-filter-comparison-types.md#esp_comparison_type)
- [`ESP_EVENT_PROPERTY_ID`](wesp-execution-property-ids.md#esp_event_property_id)
- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Filter handle

### ESP_FILTER

Identifies a WESP filter.

#### Syntax

```cpp
DECLARE_HANDLE(ESP_FILTER);
```

#### Remarks

Obtain this handle with `EspCreateFilter`. Release it with `EspCloseFilter`.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)
