---
title: "WESP common utilities, strings, and buffers"
description: "Windows endpoint security platform API reference for common utilities, strings, and buffers, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- EspInitUnicodeString
- EspStringMatchesPattern
- EspFreeMemory
- ESP_CONSTANT_UNICODE_STRING
- ESP_PATH_FORMAT
- ESP_UNICODE_STRING
- ESP_PATH
- ESP_BUFFER
- ESP_STRING_LIST
---

# Common utilities, strings, and buffers

This page contains reference entries in the [Common API family](wesp-api-reference.md#common). Each entry includes its declaration and requirements.

## Utility functions

### EspInitUnicodeString

The API `EspInitUnicodeString` initializes an `ESP_UNICODE_STRING` struct from a null-terminated string.

#### Syntax

```cpp
HRESULT
WINAPI
EspInitUnicodeString(
    _In_opt_ PCWSTR String,
    _Out_ ESP_UNICODE_STRING* UnicodeString
    );
```

#### Parameters

##### `String`

Supplies a null-terminated string.

##### `UnicodeString`

Receives the initialized unicode string.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_UNICODE_STRING`](wesp-common-utilities.md#esp_unicode_string)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspStringMatchesPattern

The API `EspStringMatchesPattern` checks if a string matches a given pattern.

#### Syntax

```cpp
HRESULT
WINAPI
EspStringMatchesPattern(
    _In_ const ESP_UNICODE_STRING* String,
    _In_ const ESP_UNICODE_STRING* Pattern,
    _Out_ BOOL* Matches
    );
```

#### Parameters

##### `String`

Supplies the string to match with the pattern.

##### `Pattern`

Supplies the string pattern.

##### `Matches`

Receives a boolean that indicates whether the string matches the pattern.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_UNICODE_STRING`](wesp-common-utilities.md#esp_unicode_string)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspFreeMemory

The API `EspFreeMemory` is used to free memory that was allocated by various WESP APIs. For example, it is used to free the memory that was allocated by the API `EspEnumerateConnectedClients`.

#### Syntax

```cpp
void
WINAPI
EspFreeMemory(
    _In_ _Post_invalid_ void* Buffer
    );
```

#### Parameters

##### `Buffer`

Supplies a pointer to the buffer to free.

#### Return value

None.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`EspEnumerateConnectedClients`](wesp-clients.md#espenumerateconnectedclients)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## String macro

### ESP_CONSTANT_UNICODE_STRING

The macro `ESP_CONSTANT_UNICODE_STRING` declares an `ESP_UNICODE_STRING` from a constant string. For example, it can be used to declare an `ESP_UNICODE_STRING` as follows:

#### Syntax

```cpp
#ifdef __cplusplus
#define ESP_CONSTANT_UNICODE_STRING(s) \
    (ESP_UNICODE_STRING{ (UINT16)(sizeof(s) - sizeof((s)[0])), s })
#else
#define ESP_CONSTANT_UNICODE_STRING(s) \
    ((ESP_UNICODE_STRING){ (UINT16)(sizeof(s) - sizeof((s)[0])), s })
#endif
```

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_UNICODE_STRING`](wesp-common-utilities.md#esp_unicode_string)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Strings, paths, and buffers

### ESP_PATH_FORMAT

The enum `ESP_PATH_FORMAT` defines a path format.

#### Syntax

```cpp
typedef enum ESP_PATH_FORMAT
{
    ESP_PATH_FORMAT_NONE = 0,
    ESP_PATH_FORMAT_DOS,
    ESP_PATH_FORMAT_NT
} ESP_PATH_FORMAT;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_PATH_FORMAT_DOS` | The path format is DOS (e.g. "C:\Windows\notepad.exe"). |
| `ESP_PATH_FORMAT_NT` | The path format is NT (e.g. \Device\HarddiskVolume1\Windows\notepad.exe). |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_UNICODE_STRING

The structure `ESP_UNICODE_STRING` represents a counted unicode string.

#### Syntax

```cpp
typedef struct ESP_UNICODE_STRING
{
    UINT16 Length;
    _Field_size_bytes_(Length) PCWCH Buffer;
} ESP_UNICODE_STRING;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Length | Specifies the length in bytes of the string. |
| Buffer | Specifies the string buffer. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_PATH

The structure `ESP_PATH` represents a path.

#### Syntax

```cpp
typedef struct ESP_PATH
{
    ESP_PATH_FORMAT Format;
    ESP_UNICODE_STRING Path;
} ESP_PATH;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Format | Specifies the path format. The supported values are NT or DOS. |
| Path | Specifies a unicode string that holds the path. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_PATH_FORMAT`](wesp-common-utilities.md#esp_path_format)
- [`ESP_UNICODE_STRING`](wesp-common-utilities.md#esp_unicode_string)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_BUFFER

The structure `ESP_BUFFER` represents a buffer.

#### Syntax

```cpp
typedef struct ESP_BUFFER
{
    UINT32 DataSize;
    _Field_size_bytes_(DataSize) const void* Data;
} ESP_BUFFER;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| DataSize | Specifies the size in bytes of the buffer. |
| Data | Specifies the buffer data. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_STRING_LIST

The structure `ESP_STRING_LIST` represents a list of strings.

#### Syntax

```cpp
typedef struct ESP_STRING_LIST
{
    UINT32 StringsCount;
    _Field_size_(StringsCount) const ESP_UNICODE_STRING* Strings;
} ESP_STRING_LIST;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| StringsCount | Specifies the number of elements in the strings array. |
| Strings | Specifies an array of strings. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_UNICODE_STRING`](wesp-common-utilities.md#esp_unicode_string)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
