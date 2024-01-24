---
description: This topic identifies the constants that WinHTTP uses.
ms.assetid: 460f1463-57a8-47eb-9957-17976757bd7f
title: WinHTTP Constants
ms.topic: article
ms.date: 05/31/2018
---

# WinHTTP Constants

WinHTTP uses the following constants:

<dl>

<dt>

[**Error Messages**](error-messages.md)
</dt> <dd>

Error messages specific to the WinHTTP functions. These functions also return Windows error messages where appropriate. The value that corresponds to each constant is the value of the constant for the application programming interface (API) functions and the lower 16 bits of the error number for the [**WinHttpRequest**](winhttprequest.md) object.

</dd> <dt>

[**HTTP Status Codes**](http-status-codes.md)
</dt> <dd>

Constants and corresponding values that indicate HTTP status codes returned by servers on the Internet.

</dd> <dt>

[**Option Flags**](option-flags.md)
</dt> <dd>

Option flags supported by [**WinHttpQueryOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpqueryoption) and [**WinHttpSetOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetoption). All valid option flags have a value greater than or equal to WINHTTP\_FIRST\_OPTION and less than or equal to WINHTTP\_LAST\_OPTION.

</dd> <dt>

[**INTERNET\_PORT**](internet-port.md)
</dt> <dd>

A WORD value indicating the port.

</dd> <dt>

[**INTERNET\_SCHEME**](internet-scheme.md)
</dt> <dd>

Internet schemes supported by WinHTTP.

</dd>

<dt>

[**Query Info Flags**](query-info-flags.md)
</dt>
<dd>

Attributes and modifiers used by [**WinHttpQueryHeaders**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpqueryheaders).
</dd>

<dt>

**WINHTTP_EXTENDED_HEADER_FLAG_UNICODE**
</dt>
<dd>

Has a value of 0x00000001. Indicates to [WinHttpAddRequestHeadersEx](/windows/win32/api/winhttp/nf-winhttp-winhttpaddrequestheadersex) that the strings passed in are Unicode strings.
</dd>

<dt>

**WINHTTP_READ_DATA_EX_FLAG_FILL_BUFFER**
</dt>
<dd>

Has a value of 0x0000000000000001ull. Instructs [WinHttpReadDataEx](/windows/win32/api/winhttp/nf-winhttp-winhttpreaddataex) not to complete the call until the provided data buffer has been filled, or the response is complete. Passing this flag makes the behavior of **WinHttpReadDataEx** equivalent to that of [WinHttpReadData](/windows/win32/api/winhttp/nf-winhttp-winhttpreaddata).
</dd>

</dl>
