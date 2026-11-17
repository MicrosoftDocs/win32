---
title: "WESP scalar, string, and buffer property accessors"
description: "Windows endpoint security platform API reference for scalar, string, and buffer property accessors, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- EspGetPropertyError
- EspGetPropertyBool
- EspGetPropertyUint8
- EspGetPropertyUint16
- EspGetPropertyUint32
- EspGetPropertyUint64
- EspGetPropertyInt32
- EspGetPropertyNtStatus
- EspGetPropertyFileTime
- EspGetPropertyGuid
- EspGetPropertyUnicodeString
- EspGetPropertyBuffer
- EspGetPropertyStringList
---

# Scalar, string, and buffer property accessors

This page contains reference entries in the [Property queries API family](wesp-api-reference.md#property-queries). Each entry includes its declaration and requirements.

## Errors and scalar values

### EspGetPropertyError

Retrieves the property-level error stored in an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertyError(const ESP_PROPERTY* Property, HRESULT* Value);
```

#### Parameters

##### `Property`

The property to inspect.

##### `Value`

Receives the requested value when the function succeeds.

#### Return value

Returns `S_OK` if the value is retrieved successfully, `E_POINTER` if an argument or required property-value pointer is null, or `E_INVALIDARG` if the property's variant type does not match the requested value type.

#### Remarks

This is an inline helper declared in espclient.h.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |

#### See also

- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspGetPropertyBool

Retrieves the Bool value from an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertyBool(const ESP_PROPERTY* Property, BOOL* Value);
```

#### Parameters

##### `Property`

The property to inspect.

##### `Value`

Receives the requested value when the function succeeds.

#### Return value

Returns `S_OK` if the value is retrieved successfully, `E_POINTER` if an argument or required property-value pointer is null, or `E_INVALIDARG` if the property's variant type does not match the requested value type. If the property contains an error variant, returns the stored error.

#### Remarks

This is an inline helper declared in espclient.h.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |

#### See also

- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspGetPropertyUint8

Retrieves the Uint8 value from an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertyUint8(const ESP_PROPERTY* Property, UINT8* Value);
```

#### Parameters

##### `Property`

The property to inspect.

##### `Value`

Receives the requested value when the function succeeds.

#### Return value

Returns `S_OK` if the value is retrieved successfully, `E_POINTER` if an argument or required property-value pointer is null, or `E_INVALIDARG` if the property's variant type does not match the requested value type. If the property contains an error variant, returns the stored error.

#### Remarks

This is an inline helper declared in espclient.h.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |

#### See also

- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspGetPropertyUint16

Retrieves the Uint16 value from an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertyUint16(const ESP_PROPERTY* Property, UINT16* Value);
```

#### Parameters

##### `Property`

The property to inspect.

##### `Value`

Receives the requested value when the function succeeds.

#### Return value

Returns `S_OK` if the value is retrieved successfully, `E_POINTER` if an argument or required property-value pointer is null, or `E_INVALIDARG` if the property's variant type does not match the requested value type. If the property contains an error variant, returns the stored error.

#### Remarks

This is an inline helper declared in espclient.h.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |

#### See also

- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspGetPropertyUint32

Retrieves the Uint32 value from an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertyUint32(const ESP_PROPERTY* Property, UINT32* Value);
```

#### Parameters

##### `Property`

The property to inspect.

##### `Value`

Receives the requested value when the function succeeds.

#### Return value

Returns `S_OK` if the value is retrieved successfully, `E_POINTER` if an argument or required property-value pointer is null, or `E_INVALIDARG` if the property's variant type does not match the requested value type. If the property contains an error variant, returns the stored error.

#### Remarks

This is an inline helper declared in espclient.h.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |

#### See also

- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspGetPropertyUint64

Retrieves the Uint64 value from an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertyUint64(const ESP_PROPERTY* Property, UINT64* Value);
```

#### Parameters

##### `Property`

The property to inspect.

##### `Value`

Receives the requested value when the function succeeds.

#### Return value

Returns `S_OK` if the value is retrieved successfully, `E_POINTER` if an argument or required property-value pointer is null, or `E_INVALIDARG` if the property's variant type does not match the requested value type. If the property contains an error variant, returns the stored error.

#### Remarks

This is an inline helper declared in espclient.h.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |

#### See also

- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspGetPropertyInt32

Retrieves the Int32 value from an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertyInt32(const ESP_PROPERTY* Property, INT32* Value);
```

#### Parameters

##### `Property`

The property to inspect.

##### `Value`

Receives the requested value when the function succeeds.

#### Return value

Returns `S_OK` if the value is retrieved successfully, `E_POINTER` if an argument or required property-value pointer is null, or `E_INVALIDARG` if the property's variant type does not match the requested value type. If the property contains an error variant, returns the stored error.

#### Remarks

This is an inline helper declared in espclient.h.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |

#### See also

- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspGetPropertyNtStatus

Retrieves the NtStatus value from an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertyNtStatus(const ESP_PROPERTY* Property, NTSTATUS* Value);
```

#### Parameters

##### `Property`

The property to inspect.

##### `Value`

Receives the requested value when the function succeeds.

#### Return value

Returns `S_OK` if the value is retrieved successfully, `E_POINTER` if an argument or required property-value pointer is null, or `E_INVALIDARG` if the property's variant type does not match the requested value type. If the property contains an error variant, returns the stored error.

#### Remarks

This is an inline helper declared in espclient.h.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |

#### See also

- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspGetPropertyFileTime

Retrieves the FileTime value from an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertyFileTime(const ESP_PROPERTY* Property, FILETIME* Value);
```

#### Parameters

##### `Property`

The property to inspect.

##### `Value`

Receives the requested value when the function succeeds.

#### Return value

Returns `S_OK` if the value is retrieved successfully, `E_POINTER` if an argument or required property-value pointer is null, or `E_INVALIDARG` if the property's variant type does not match the requested value type. If the property contains an error variant, returns the stored error.

#### Remarks

This is an inline helper declared in espclient.h.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |

#### See also

- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspGetPropertyGuid

Retrieves the Guid value from an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertyGuid(const ESP_PROPERTY* Property, GUID* Value);
```

#### Parameters

##### `Property`

The property to inspect.

##### `Value`

Receives the requested value when the function succeeds.

#### Return value

Returns `S_OK` if the value is retrieved successfully, `E_POINTER` if an argument or required property-value pointer is null, or `E_INVALIDARG` if the property's variant type does not match the requested value type. If the property contains an error variant, returns the stored error.

#### Remarks

This is an inline helper declared in espclient.h.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |

#### See also

- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Strings and buffers

### EspGetPropertyUnicodeString

Retrieves the UnicodeString value from an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertyUnicodeString(const ESP_PROPERTY* Property, ESP_UNICODE_STRING* Value);
```

#### Parameters

##### `Property`

The property to inspect.

##### `Value`

Receives the requested value when the function succeeds.

#### Return value

Returns `S_OK` if the value is retrieved successfully, `E_POINTER` if an argument or required property-value pointer is null, or `E_INVALIDARG` if the property's variant type does not match the requested value type. If the property contains an error variant, returns the stored error.

#### Remarks

This is an inline helper declared in espclient.h.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |

#### See also

- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [`ESP_UNICODE_STRING`](wesp-common-utilities.md#esp_unicode_string)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspGetPropertyBuffer

Retrieves the Buffer value from an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertyBuffer(const ESP_PROPERTY* Property, ESP_BUFFER* Value);
```

#### Parameters

##### `Property`

The property to inspect.

##### `Value`

Receives the requested value when the function succeeds.

#### Return value

Returns `S_OK` if the value is retrieved successfully, `E_POINTER` if an argument or required property-value pointer is null, or `E_INVALIDARG` if the property's variant type does not match the requested value type. If the property contains an error variant, returns the stored error.

#### Remarks

This is an inline helper declared in espclient.h.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |

#### See also

- [`ESP_BUFFER`](wesp-common-utilities.md#esp_buffer)
- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspGetPropertyStringList

Retrieves the StringList value from an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertyStringList(const ESP_PROPERTY* Property, ESP_STRING_LIST* Value);
```

#### Parameters

##### `Property`

The property to inspect.

##### `Value`

Receives the requested value when the function succeeds.

#### Return value

Returns `S_OK` if the value is retrieved successfully, `E_POINTER` if an argument or required property-value pointer is null, or `E_INVALIDARG` if the property's variant type does not match the requested value type. If the property contains an error variant, returns the stored error.

#### Remarks

This is an inline helper declared in espclient.h.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |

#### See also

- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [`ESP_STRING_LIST`](wesp-common-utilities.md#esp_string_list)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
