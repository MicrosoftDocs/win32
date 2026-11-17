---
title: "WESP structured and domain-specific property accessors"
description: "Windows endpoint security platform API reference for structured and domain-specific property accessors, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- EspGetPropertyContextKeyInfo
- EspGetPropertyMemoryAddressBasic
- EspGetPropertyFileId128
- EspGetPropertyUsn
- EspGetPropertyEaList
- EspGetPropertyStorageBusType
- EspGetPropertyDeviceType
- EspGetPropertySubsystemInformationType
- EspGetPropertyFoTargetObjectType
- EspGetPropertySigningLevel
- EspGetPropertySecurityDescriptor
- EspGetPropertyAcl
- EspGetPropertySid
- EspGetPropertyImpersonationLevel
- EspGetPropertyTokenPrivileges
- EspGetPropertyTokenGroups
- EspGetPropertyTokenType
- EspGetPropertyTokenElevationType
- EspGetPropertyTransactionOutcome
- EspGetPropertyTransactionState
---

# Structured and domain-specific property accessors

This page contains reference entries in the [Property queries API family](wesp-api-reference.md#property-queries). Each entry includes its declaration and requirements.

## Context key information

### EspGetPropertyContextKeyInfo

Retrieves context-key information from an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertyContextKeyInfo(const ESP_PROPERTY* Property, ESP_CONTEXT_KEY_INFO* Value);
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

- [`ESP_CONTEXT_KEY_INFO`](wesp-context-key-management.md#esp_context_key_info)
- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Memory, file, and storage values

### EspGetPropertyMemoryAddressBasic

Retrieves the MemoryAddressBasic value from an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertyMemoryAddressBasic(const ESP_PROPERTY* Property, ESP_MEMORY_ADDRESS_BASIC* Value);
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

- [`ESP_MEMORY_ADDRESS_BASIC`](wesp-common-value-types.md#esp_memory_address_basic)
- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspGetPropertyFileId128

Retrieves the FileId128 value from an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertyFileId128(const ESP_PROPERTY* Property, FILE_ID_128* Value);
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

### EspGetPropertyUsn

Retrieves the Usn value from an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertyUsn(const ESP_PROPERTY* Property, USN* Value);
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

### EspGetPropertyEaList

Retrieves the EaList value from an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertyEaList(const ESP_PROPERTY* Property, ESP_EA_LIST* Value);
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

- [`ESP_EA_LIST`](wesp-common-value-types.md#esp_ea_list)
- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspGetPropertyStorageBusType

Retrieves the StorageBusType value from an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertyStorageBusType(const ESP_PROPERTY* Property, STORAGE_BUS_TYPE* Value);
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

### EspGetPropertyDeviceType

Retrieves the DeviceType value from an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertyDeviceType(const ESP_PROPERTY* Property, DEVICE_TYPE* Value);
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

### EspGetPropertySubsystemInformationType

Retrieves the SubsystemInformationType value from an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertySubsystemInformationType(const ESP_PROPERTY* Property, ESP_SUBSYSTEM_INFORMATION_TYPE* Value);
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
- [`ESP_SUBSYSTEM_INFORMATION_TYPE`](wesp-common-value-types.md#esp_subsystem_information_type)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspGetPropertyFoTargetObjectType

Retrieves the FoTargetObjectType value from an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertyFoTargetObjectType(const ESP_PROPERTY* Property, ESP_FO_TARGET_OBJECT_TYPE* Value);
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

- [`ESP_FO_TARGET_OBJECT_TYPE`](wesp-common-value-types.md#esp_fo_target_object_type)
- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Security and token values

### EspGetPropertySigningLevel

Retrieves the SigningLevel value from an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertySigningLevel(const ESP_PROPERTY* Property, SE_SIGNING_LEVEL* Value);
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

### EspGetPropertySecurityDescriptor

Retrieves the SecurityDescriptor value from an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertySecurityDescriptor(const ESP_PROPERTY* Property, SECURITY_DESCRIPTOR** Value);
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

### EspGetPropertyAcl

Retrieves the Acl value from an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertyAcl(const ESP_PROPERTY* Property, ACL** Value);
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

### EspGetPropertySid

Retrieves the Sid value from an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertySid(const ESP_PROPERTY* Property, SID** Value);
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

### EspGetPropertyImpersonationLevel

Retrieves the ImpersonationLevel value from an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertyImpersonationLevel(const ESP_PROPERTY* Property, SECURITY_IMPERSONATION_LEVEL* Value);
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

### EspGetPropertyTokenPrivileges

Retrieves the TokenPrivileges value from an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertyTokenPrivileges(const ESP_PROPERTY* Property, TOKEN_PRIVILEGES** Value);
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

### EspGetPropertyTokenGroups

Retrieves the TokenGroups value from an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertyTokenGroups(const ESP_PROPERTY* Property, TOKEN_GROUPS** Value);
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

### EspGetPropertyTokenType

Retrieves the TokenType value from an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertyTokenType(const ESP_PROPERTY* Property, TOKEN_TYPE* Value);
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

### EspGetPropertyTokenElevationType

Retrieves the TokenElevationType value from an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertyTokenElevationType(const ESP_PROPERTY* Property, TOKEN_ELEVATION_TYPE* Value);
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

## Transaction values

### EspGetPropertyTransactionOutcome

Retrieves the TransactionOutcome value from an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertyTransactionOutcome(const ESP_PROPERTY* Property, TRANSACTION_OUTCOME* Value);
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

### EspGetPropertyTransactionState

Retrieves the TransactionState value from an `ESP_PROPERTY` structure.

#### Syntax

```cpp
inline HRESULT EspGetPropertyTransactionState(const ESP_PROPERTY* Property, TRANSACTION_STATE* Value);
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
