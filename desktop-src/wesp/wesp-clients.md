---
title: "WESP clients"
description: "Windows endpoint security platform API reference for clients, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- EspRegisterClient
- EspUnregisterClient
- EspConnectClient
- EspDisconnectClient
- EspEnumerateRegisteredClients
- EspEnumerateConnectedClients
- EspQueryClientDescriptor
- ESP_CLIENT
- ESP_CLIENT_DESCRIPTOR
- ESP_CLIENT_CONFIG
---

# Clients

This page contains reference entries in the [Clients API family](wesp-api-reference.md#clients). Each entry includes its declaration and requirements.

## Client functions

### EspRegisterClient

The API `EspRegisterClient` is used to register a client with the WESP framework. The WESP framework persists a client's registration. Clients should call this API when their product is first installed.

#### Syntax

```cpp
HRESULT
WINAPI
EspRegisterClient(
    _In_ const ESP_CLIENT_DESCRIPTOR* Descriptor
    );
```

#### Parameters

##### `Descriptor`

Specifies the descriptor for the client being registered.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Remarks

When registering a client, the caller specifies a client ID (GUID) and altitude (PCWSTR) through the `ESP_CLIENT_DESCRIPTOR` structure that is supplied to `EspRegisterClient`. Client IDs and altitudes must both be unique. If an existing client is registered with the same client ID or altitude, the API `EspRegisterClient` fails with `ERROR_ALREADY_EXISTS`.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT_DESCRIPTOR`](wesp-clients.md#esp_client_descriptor)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspUnregisterClient

The API `EspUnregisterClient` is used to unregister a client with the WESP framework. This API will delete all persisted state associated with the client, and should be called once when the product is uninstalled. A client cannot be unregistered if it is still connected.

#### Syntax

```cpp
HRESULT
WINAPI
EspUnregisterClient(
    _In_ const GUID* ClientId
    );
```

#### Parameters

##### `ClientId`

Specifies the client id to unregister. The client must be disconnected before it can be unregistered.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

Documented error conditions include:

| RETURN VALUE | DESCRIPTION |
| --- | --- |
| `ERROR_INVALID_STATE` | The client is currently connected. |
| `ERROR_NOT_FOUND` | The client is not currently registered. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspConnectClient

The API `EspConnectClient` is used to establish a connection with the WESP framework. The API returns an opaque object `ESP_CLIENT` which is the basis for invoking other WESP APIs. The WESP framework supports only one active connection per-client ID. In other words, once `EspConnectClient` has successfully been called, any subsequent call to the API with the same client ID will fail until the existing connection is disconnected.

#### Syntax

```cpp
HRESULT
WINAPI
EspConnectClient(
    _In_ const GUID* ClientId,
    _Out_ ESP_CLIENT* Client
    );
```

#### Parameters

##### `ClientId`

Specifies the client id to connect. The client id must have been previously registered by calling `EspRegisterClient`.

##### `Client`

Receives an opaque object that represents the client. This object must be closed by calling `EspDisconnectClient` once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

Documented error conditions include:

| RETURN VALUE | DESCRIPTION |
| --- | --- |
| `ERROR_NOT_FOUND` | The client ID is not registered. |
| `ERROR_INVALID_STATE` | The client is already connected. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspDisconnectClient

The API `EspDisconnectClient` is used to disconnect a WESP client. If a WESP process terminates, its client is automatically disconnected. This API should be called once a WESP application no longer requires an active client connection. It will free all memory associated with the client.

#### Syntax

```cpp
HRESULT
WINAPI
EspDisconnectClient(
    _In_ _Post_invalid_ ESP_CLIENT Client
    );
```

#### Parameters

##### `Client`

Specifies the client to disconnect. The supplied "Client" cannot be used after this API returns.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspEnumerateRegisteredClients

The API `EspEnumerateRegisteredClients` is used to enumerate all the registered WESP clients. This can be used to discover which other WESP clients are installed on the system.

#### Syntax

```cpp
HRESULT
WINAPI
EspEnumerateRegisteredClients(
    _Out_ UINT32* ClientIdsCount,
    _Outptr_result_buffer_all_(*ClientIdsCount) GUID** ClientIds
    );
```

#### Parameters

##### `ClientIdsCount`

Receives the number of elements in the ClientIds array.

##### `ClientIds`

Receives an array of client IDs that are currently registered. The caller must free this array by calling `EspFreeMemory`.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspEnumerateConnectedClients

The API `EspEnumerateConnectedClients` is used to enumerate all the connected WESP clients. This can be used to discover which other WESP clients are currently connected on the system.

#### Syntax

```cpp
HRESULT
WINAPI
EspEnumerateConnectedClients(
    _Out_ UINT32* ClientIdsCount,
    _Outptr_result_buffer_all_(*ClientIdsCount) GUID** ClientIds
    );
```

#### Parameters

##### `ClientIdsCount`

Receives the number of elements in the ClientIds array.

##### `ClientIds`

Receives an array of client IDs that are currently connected. The caller must free this array by calling `EspFreeMemory`.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspQueryClientDescriptor

The API `EspQueryClientDescriptor` can be used to query the descriptor for a given client. This API can be used to retrieve more information about a client that is currently connected or registered with the WESP framework.

#### Syntax

```cpp
HRESULT
WINAPI
EspQueryClientDescriptor(
    _In_ const GUID* ClientId,
    _Outptr_ ESP_CLIENT_DESCRIPTOR** Descriptor
    );
```

#### Parameters

##### `ClientId`

Specifies the client id for which to query the descriptor.

##### `Descriptor`

Receives the client descriptor. The caller must free this descriptor by calling `EspFreeMemory`.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT_DESCRIPTOR`](wesp-clients.md#esp_client_descriptor)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Client handle and structures

### ESP_CLIENT

Identifies a connection to a registered WESP client.

#### Syntax

```cpp
DECLARE_HANDLE(ESP_CLIENT);
```

#### Remarks

Obtain this handle with `EspConnectClient`. Release it with `EspDisconnectClient`.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_CLIENT_DESCRIPTOR

The structure `ESP_CLIENT_DESCRIPTOR` describes a client. It is used to register a client through the API `EspRegisterClient`.

#### Syntax

```cpp
typedef struct ESP_CLIENT_DESCRIPTOR
{
    GUID ClientId;
    PCWSTR ClientName;
    PCWSTR Altitude;
} ESP_CLIENT_DESCRIPTOR;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ClientId | Specifies the client's id. The client id uniquely identifies the client. |
| ClientName | This field is a friendly name for the client. The maximum string size is 256 characters. This field cannot be null. |
| Altitude | This field specifies the altitude for the client. Each WESP client has a unique altitude. The altitude defines the ordering between clients for processing events. Clients at a higher altitude will process events before clients at a lower altitude. The altitude is an infinite-precision string interpreted as a decimal number. The maximum string size is 256 characters. This field cannot be null.<br>For example, if there is client A with altitude "100" and client B with altitude "50", client A will process events before client B, because "100" is larger than "50". Similarly, if there is client A with altitude "100.1" and client B with altitude "100", client A will process events before client B. Note that the WESP altitude is different than the altitude used by FltMgr drivers. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`EspRegisterClient`](wesp-clients.md#espregisterclient)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_CLIENT_CONFIG

The structure `ESP_CLIENT_CONFIG` is used to set client configuration for a rule.

#### Syntax

```cpp
typedef struct ESP_CLIENT_CONFIG
{
    ESP_FILTER Filter;
    ESP_CONTEXT_KEY_CONFIG ContextConfig;

    UINT32 PropertiesCount;
    _Field_size_(PropertiesCount) const ESP_CLIENT_PROPERTY_ID* Properties;

    UINT32 BindingsCount;
    _Field_size_(BindingsCount) const ESP_PROPERTY_BINDING* Bindings;
} ESP_CLIENT_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Filter | Specifies a filter for the client. The filter must have been created using `EspCreateClientFilter`, or must be composed of filters created through `EspCreateClientFilter`. |
| ContextConfig | Supplies an `ESP_CONTEXT_KEY_CONFIG` structure. This structure can be used to configure context key updates and capture binding keys for the client. |
| PropertiesCount | Supplies the number of elements in the "Properties" array. |
| Properties | Supplies an array of client properties that should be captured for the client. |
| BindingsCount | Supplies the number of elements in the bindings array. |
| Bindings | Supplies an array of client property bindings. This allows the client to configure binding keys for various properties. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_CLIENT_PROPERTY_ID`](wesp-execution-property-ids.md#esp_client_property_id)
- [`ESP_CONTEXT_KEY_CONFIG`](wesp-context-key-management.md#esp_context_key_config)
- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [`ESP_PROPERTY_BINDING`](wesp-rule-configuration.md#esp_property_binding)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
