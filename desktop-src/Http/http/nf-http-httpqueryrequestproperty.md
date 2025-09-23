---
title: HttpQueryRequestProperty
description: Gives an application access to find-grained information about a request.
ms.topic: reference
ms.date: 04/25/2025
req.lib: 
req.dll: httpapi.dll
topic_type:
- APIRef
- kbSyntax
api_type:
- DllExport
api_location:
- Kernelbase.dll
api_name:
- HttpQueryRequestProperty
targetos: Windows
ms.localizationpriority: low
---

# HttpQueryRequestProperty function

Gives an application access to find-grained information about a request. Mostly connection flow statistics, but also the Server Name Indication (SNI&mdash;presents the server domain name requested by the client to the server so that it can select the correct certificate, among other reasons), and other traits of the underlying TLS connection (when applicable).

The [HTTP_REQUEST](/previous-versions/windows/desktop/legacy/aa364545(v=vs.85)) structure gets filled in with the information that pretty much every server application will need in order to respond to a request, and **HttpQueryRequestProperty** is for getting useful diagnostic data about a request, or more detailed information where it's going to be really necessary. Most applications aren't concerned with the precise breakdown of timings for API calls, but very large or very performance-driven applications or teams might want those details for better debugging. But be aware that there's a cost associated with gathering or retrieving most of the data covered by **HttpQueryRequestProperty**.

Whereas [HttpSetRequestProperty](/windows/win32/api/http/nf-http-httpsetrequestproperty) works on just two values in [HTTP_REQUEST_PROPERTY](/windows/win32/api/http/ne-http-http_request_property), the HttpQueryRequestProperty function works on all of them.

See **Remarks** for info about how to call the function.

## Syntax

```cpp
HTTPAPI_LINKAGE ULONG WINAPI
HttpQueryRequestProperty(
  _In_ HANDLE RequestQueueHandle,
  _In_ HTTP_OPAQUE_ID Id,
  _In_ HTTP_REQUEST_PROPERTY PropertyId,
  _In_reads_bytes_opt_(QualifierSize) VOID *Qualifier,
  _In_ ULONG QualifierSize,
  _Out_writes_bytes_to_opt_(OutputBufferSize, *BytesReturned) PVOID Output,
  _In_ ULONG OutputBufferSize,
  _Out_opt_ PULONG BytesReturned,
  _In_opt_ LPOVERLAPPED Overlapped
);
```

## Parameters

`RequestQueueHandle`

Type: \_In\_ **HANDLE**

The handle to the request queue where the request being queried was received.

`Id`

Type: \_In\_ **HTTP_OPAQUE_ID**

The opaque ID of the request.

`PropertyId`

Type: \_In\_ **[HTTP_REQUEST_PROPERTY](/windows/win32/api/http/ne-http-http_request_property)**

A member of the **HTTP_REQUEST_PROPERTY** enumeration describing the property type that's set. The enumeration includes notes about supported properties and how to enable them.

`Qualifier`

Type: \_In\_reads\_bytes\_opt\_(QualifierSize) **VOID \***

An optional parameter required for some values of *PropertyId* to identify bounds on what data you're requesting. For the Stats options, it can be used to define the window of time to look back for connection statistics.

`QualifierSize`

Type: \_In\_ **ULONG**

The size of the structure passed in *Qualifier*. If *Qualifier* is `NULL`, then set this to 0.

`Output`

Type: \_Out\_writes\_bytes\_to\_opt\_(OutputBufferSize, *BytesReturned) **PVOID**

Receives the contents of the property requested. You're responsible for allocating and freeing this buffer. For many properties, this is a fixed-size buffer depending on the property requested. See [HTTP_REQUEST_PROPERTY](/windows/win32/api/http/ne-http-http_request_property) for the specifics of a given property.

When a property returns a variable-length buffer, you can probe for the size of buffer needed by leaving this parameter `NULL`, and passing in a pointer for *BytesReturned*. For more details, see [HTTP_REQUEST_PROPERTY](/windows/win32/api/http/ne-http-http_request_property).

`OutputBufferSize`

Type: \_In\_ **ULONG**

The size of the buffer passed in *Output*, or 0 if it's NULL.

`BytesReturned`

Type: \_Out\_opt\_ **PULONG**

Returns the number of bytes written to *Output*. Or, for variable-length properties, can return the size of buffer needed if *Output* wasn't large enough. For variable-length properties, you should call first with *Output* set to `NULL` so that you can retrieve through *BytesReturned* the buffer size you need, then allocate that amount of memory, then retry the query.

`Overlapped`

Type: \_In\_opt\_ **LPOVERLAPPED**

While you can provide an **OVERLAPPED** structure for asynchronous operation, setting this parameter is not a guarantee that the API will run asynchronously; most operations on this API are always synchronous. The event in this structure is used only if the API returns **ERROR_IO_PENDING**.

## Return value

Type: **ULONG**

If the function succeeds, then the return value is **ERROR_SUCCESS**. If an **OVERLAPPED** structure is provided, and the function runs asynchronously, then **ERROR_IO_PENDING** will be returned, and is not an error.

If the function fails, then the return value is one of the following error codes:

|Return code|Description|
|-|-|
|**ERROR_INVALID_PARAMETER**|One or more of the arguments is invalid.|
|**ERROR_INVALID_FUNCTION**|The request doesn't support the property you've queried.|
|**ERROR_MORE_DATA**|The size of the output buffer is insufficient, allocate a larger buffer for the next request.|
|Other|Check the [system error codes](/windows/win32/debug/system-error-codes) defined in `WinError.h`|

## Remarks

This function does not have an associated header file or library file. Your application can call [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) with the DLL name (`httpapi.dll`) to obtain a module handle. It can then call [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) with the module handle and the name of this function to get the function address.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 10, version 1709 [desktop apps only] |
| **Minimum supported server** | Windows Server, version 1709 [desktop apps only] |
| **Target Platform** | Windows |
| **Header** | None |
| **Library** | None |
| **DLL** | httpapi.dll |


## See also

* [HttpSetRequestProperty](/windows/win32/api/http/nf-http-httpsetrequestproperty)
* [HttpSetRequestQueueProperty](/windows/win32/api/http/nf-http-httpsetrequestqueueproperty)
* [HttpSetServerSessionProperty](/windows/win32/api/http/nf-http-httpsetserversessionproperty)
* [HttpSetServiceConfiguration](/windows/win32/api/http/nf-http-httpsetserviceconfiguration)
* [HttpSetUrlGroupProperty](/windows/win32/api/http/nf-http-httpseturlgroupproperty)
* [HttpQueryRequestQueueProperty](/windows/win32/api/http/nf-http-httpqueryrequestqueueproperty)
* [HttpQueryServerSessionProperty](/windows/win32/api/http/nf-http-httpqueryserversessionproperty)
* [HttpQueryServiceConfiguration](/windows/win32/api/http/nf-http-httpqueryserviceconfiguration)
* [HttpQueryUrlGroupProperty](/windows/win32/api/http/nf-http-httpqueryurlgroupproperty)
