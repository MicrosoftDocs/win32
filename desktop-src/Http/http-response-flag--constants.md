---
title: HTTP_RESPONSE_FLAG_ Constants (Http.h)
description: Define options to configure responses in the HTTP Server API.
ms.assetid: bcb59457-fd22-4166-8a72-ba85209ec8c7
topic_type:
- apiref
api_name:
- HTTP_RESPONSE_FLAG_MULTIPLE_ENCODINGS_AVAILABLE
api_location:
- http.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# HTTP\_RESPONSE\_FLAG\_ Constants

The **HTTP\_RESPONSE\_FLAG\_** constants define options to configure responses in the HTTP Server API.

These constants are used in the **Flags** member of the [**HTTP\_RESPONSE\_V1**](/windows/desktop/api/Http/ns-http-http_response_v1) structure.

<dl> <dt>

<span id="HTTP_RESPONSE_FLAG_MULTIPLE_ENCODINGS_AVAILABLE"></span><span id="http_response_flag_multiple_encodings_available"></span>**HTTP\_RESPONSE\_FLAG\_MULTIPLE\_ENCODINGS\_AVAILABLE**
</dt> <dd> <dl> <dt>



Encodings other than identity form are available for this resource. This flag is ignored if the application has not asked for the response to be cached. It's used as a hint to the HTTP Server API for content negotiation when serving from the kernel response cache.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                           |
| Header<br/>                   | <dl> <dt>Http.h</dt> </dl> |



## See also

<dl> <dt>

[HTTP Server API Version 2.0 Constants](http-server-api-version-2-0-constants.md)
</dt> <dt>

[**HTTP\_RESPONSE\_V1**](/windows/desktop/api/Http/ns-http-http_response_v1)
</dt> </dl>

 

 





