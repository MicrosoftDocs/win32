---
title: Errors
description: This section outlines error that may be issues by Windows Web Services functions in result of a failure to execute the command.
ms.assetid: 2e5b853f-589c-4f89-9d7e-cd02263a2247
keywords:
- Errors Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# Errors

This section outlines error that may be issues by Windows Web Services functions in result of a failure to execute the command.

-   [Out Parameters](#out-parameters)
-   [Error Codes](#error-codes)
-   [Rich Errors](#rich-errors)
-   [Faults and Errors](#faults-and-errors)
-   [Language Sensitive Error Information](#language-sensitive-error-information)
-   [Canonical Error Codes](#canonical-error-codes)
-   [Invalid API Usage](#invalid-api-usage)
-   [Security](#security)

## Out Parameters

As a general rule, the value of out parameters are not modified if a function fails.

There are a few instances where out parameters are modified if the function fails. These cases are explicitly called out in the documentation for each parameter. If the documentation does not mention anything about modifying out parameters in the case of failure, then you can safely assume that the function will not modify them.

## Error Codes

All error return codes are HRESULTs. This API defines a set of HRESULTs in the FACILITY\_WEBSERVICES range, but also returns errors defined elsewhere in the Windows API.

Refer to the documentation for specific API's to learn about which error codes are returned. The list is not intended to be exhaustive for each API, but rather a list of error codes for which there are common scenarios for explicit handling. A caller should always assume other error codes are possible from any API.

This API defines a relatively small number of error codes, which correspond to scenarios where a program will want to take action based on the error. Error codes alone may not be sufficient in order to determine what went wrong, or in order to provide a good description of the problem to the user. The best understanding of the problem comes from using Rich Errors, as described below.

## Rich Errors

In additional to returning an error code, a caller may optionally request rich error information for any API call by passing a non-**NULL**[WS\_ERROR](ws-error.md) object. To create an error object, use [**WsCreateError**](/windows/desktop/api/WebServices/nf-webservices-wscreateerror). If there is an error, then the API that caused the error will fill the error object with additional context about the error situation. If there is no error, then the error object is unmodified. Passing a **NULL** error object indicates that the caller is not interested in rich error information. Callees (including callbacks) must be prepared to handle **NULL** error objects.

Note that the same error object can be used for multiple API calls, but may only be used for one API call at a time (as it is single threaded). Each time an error occurs, error information is appended to the error object. As a call chain unwinds, multiple functions may add information to the error object to provide additional context about the error. To clear the contents of the error object before reusing it (after an error occurs), use [**WsResetError**](/windows/desktop/api/WebServices/nf-webservices-wsreseterror). If no error occurs, it is not necessary to reset the error object before reusing it.

Rich error information consists of the following:

-   A set of property values, which provide additional information about the error if present. See [**WS\_ERROR\_PROPERTY**](/windows/desktop/api/WebServices/ns-webservices-ws_error_property).
-   Zero or more error strings. The strings are added using [**WsAddErrorString**](/windows/desktop/api/WebServices/nf-webservices-wsadderrorstring), and can be queried using using [**WsGetErrorString**](/windows/desktop/api/WebServices/nf-webservices-wsgeterrorstring). The number of strings can be queried using [**WS\_ERROR\_PROPERTY\_STRING\_COUNT**](/windows/desktop/api/WebServices/ne-webservices-ws_error_property_id).

## Faults and Errors

See [Faults](faults.md) for information about how errors and faults relate.

## Language Sensitive Error Information

When creating an error object, the LANGID of the desired language translation for error information is specified. This is used when adding error information to the error object.

This language value can be retrieved or set using [**WS\_ERROR\_PROPERTY\_LANGID**](/windows/desktop/api/WebServices/ne-webservices-ws_error_property_id).

## Canonical Error Codes

This API provides a canonical set of error codes (WS\_E\_\*) that allow for different communication technologies to be used without having to depend on the specific error codes of the specific underlying implementation. For a complete list of these error codes, see [Windows Web Services Return Values](windows-web-services-return-values.md).

This allows, for example, a program to check for the error code **WS\_E\_ENDPOINT\_NOT\_FOUND** whether using TCP, UDP, or HTTP, and take some action (like attempting to use a different endpoint).

When an implementation specific error code is mapped to a canonical error, the original error code is saved in the error object, and may still be accessed for diagnostic purposes. See [**WS\_ERROR\_PROPERTY\_ORIGINAL\_ERROR\_CODE**](/windows/desktop/api/WebServices/ne-webservices-ws_error_property_id) for more information.

## Invalid API Usage

The following error codes are reserved for invalid API usage, and will not be returned in other circumstances. If any of these errors are returned it may be an indication of an application bug.

-   **WS\_E\_INVALID\_OPERATION**
-   **E\_INVALIDARG**

The following enumerations are part of tracing:

-   [**WS\_ERROR\_PROPERTY\_ID**](/windows/desktop/api/WebServices/ne-webservices-ws_error_property_id)
-   [**WS\_EXCEPTION\_CODE**](/windows/desktop/api/WebServices/ne-webservices-ws_exception_code)

The following error codes are part of tracing:

-   **CERT\_E\_CN\_NO\_MATCH**
-   **CERT\_E\_EXPIRED**
-   **CERT\_E\_UNTRUSTEDROOT**
-   **CERT\_E\_WRONG\_USAGE**
-   **CRYPT\_E\_REVOCATION\_OFFLINE**
-   **E\_INVALIDARG**
-   **E\_OUTOFMEMORY**
-   **WS\_E\_ADDRESS\_IN\_USE**
-   **WS\_E\_ADDRESS\_NOT\_AVAILABLE**
-   **WS\_E\_ENDPOINT\_ACCESS\_DENIED**
-   **WS\_E\_ENDPOINT\_ACTION\_NOT\_SUPPORTED**
-   **WS\_E\_ENDPOINT\_DISCONNECTED**
-   **WS\_E\_ENDPOINT\_FAILURE**
-   **WS\_E\_ENDPOINT\_FAULT\_RECEIVED**
-   **WS\_E\_ENDPOINT\_NOT\_AVAILABLE**
-   **WS\_E\_ENDPOINT\_NOT\_FOUND**
-   **WS\_E\_ENDPOINT\_TOO\_BUSY**
-   **WS\_E\_ENDPOINT\_UNREACHABLE**
-   **WS\_E\_INVALID\_ENDPOINT\_URL**
-   **WS\_E\_INVALID\_FORMAT**
-   **WS\_E\_INVALID\_OPERATION**
-   **WS\_E\_NOT\_SUPPORTED**
-   **WS\_E\_NO\_TRANSLATION\_AVAILABLE**
-   **WS\_E\_NUMERIC\_OVERFLOW**
-   **WS\_E\_OBJECT\_FAULTED**
-   **WS\_E\_OPERATION\_ABANDONED**
-   **WS\_E\_OPERATION\_ABORTED**
-   **WS\_E\_OPERATION\_TIMED\_OUT**
-   **WS\_E\_OTHER**
-   **WS\_E\_PROXY\_ACCESS\_DENIED**
-   **WS\_E\_PROXY\_FAILURE**
-   **WS\_E\_PROXY\_REQUIRES\_BASIC\_AUTH**
-   **WS\_E\_PROXY\_REQUIRES\_DIGEST\_AUTH**
-   **WS\_E\_PROXY\_REQUIRES\_NEGOTIATE\_AUTH**
-   **WS\_E\_PROXY\_REQUIRES\_NTLM\_AUTH**
-   **WS\_E\_QUOTA\_EXCEEDED**
-   **WS\_E\_SECURITY\_SYSTEM\_FAILURE**
-   **WS\_E\_SECURITY\_TOKEN\_EXPIRED**
-   **WS\_E\_SECURITY\_VERIFICATION\_FAILURE**
-   **WS\_E\_SERVER\_REQUIRES\_BASIC\_AUTH**
-   **WS\_E\_SERVER\_REQUIRES\_DIGEST\_AUTH**
-   **WS\_E\_SERVER\_REQUIRES\_NEGOTIATE\_AUTH**
-   **WS\_E\_SERVER\_REQUIRES\_NTLM\_AUTH**
-   **WS\_S\_ASYNC**
-   **WS\_S\_END**

The following functions are part of tracing:

-   [**WS\_ERROR\_PROPERTY\_ID**](/windows/desktop/api/WebServices/ne-webservices-ws_error_property_id)
-   [**WS\_EXCEPTION\_CODE**](/windows/desktop/api/WebServices/ne-webservices-ws_exception_code)

The following handle is part of tracing:

-   [WS\_ERROR](ws-error.md)

The following structure is part of tracing:

-   [**WS\_ERROR\_PROPERTY**](/windows/desktop/api/WebServices/ns-webservices-ws_error_property)

## Security

There are a number of security considerations that the user of the error object should be aware of:

-   The error object may contain untrusted data. Examples of this are: the WS\_FAULT, and the error strings, both of which can be stored in the error object based on information received over an untrusted channel. The user of the error object should be careful when inspecting the information in the error object and making decisions based on its values.
-   A user of the error object should call [**WsResetError**](/windows/desktop/api/WebServices/nf-webservices-wsreseterror) after inspecting the information about the error. Failing to do so can lead to memory accumulation.
-   A user of the error object should be very careful when using the WS\_FULL\_FAULT\_DISCLOSURE value of the [**WS\_FAULT\_DISCLOSURE**](/windows/desktop/api/WebServices/ne-webservices-ws_fault_disclosure) enumeration, because the generated fault could contain private information that was accumulated as part of the error recording process.

 

 




