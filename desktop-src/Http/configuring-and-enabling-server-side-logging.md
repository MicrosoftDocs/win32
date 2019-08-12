---
title: Configuring and Enabling Server Side Logging
description: Configuring and Enabling Server Side Logging
ms.assetid: d67d8f9a-6d8a-43f2-a1ef-75f69c04b1ac
ms.topic: article
ms.date: 05/31/2018
---

# Configuring and Enabling Server Side Logging

The application enables logging on the server session or the URL group before sending the response with [**HttpSendHttpResponse**](/windows/desktop/api/Http/nf-http-httpsendhttpresponse). The following example shows how to configure and enable W3C type server side logging:

1.  The application initializes the [**HTTP\_LOGGING\_INFO**](/windows/desktop/api/Http/ns-http-http_logging_info) structure with **HttpLoggingTypeW3C** specified in the **Format** member, and a bitmask of the [**HTTP\_LOG\_FIELD**](http-log-field--constants.md) constants in the **Fields** member.
2.  The application calls [**HttpSetServerSessionProperty**](/windows/desktop/api/Http/nf-http-httpsetserversessionproperty) or [**HttpSetUrlGroupProperty**](/windows/desktop/api/Http/nf-http-httpseturlgroupproperty) with **HttpServerLoggingProperty** specified in the *Property* parameter and a pointer to the [**HTTP\_LOGGING\_INFO**](/windows/desktop/api/Http/ns-http-http_logging_info) structure in the *pPropertyInformation* parameter.

The bitmask of the [**HTTP\_LOG\_FIELD**](http-log-field--constants.md) constants contain the fields that may be logged in the W3C log file. Note that setting the **HttpServerLoggingProperty** property on a server session or a URL group does not mean that HTTP responses will be logged. Logging is performed on a per request basis when W3C is enabled in the call to [**HttpSendHttpResponse**](/windows/desktop/api/Http/nf-http-httpsendhttpresponse) or [**HttpSendResponseEntityBody**](/windows/desktop/api/Http/nf-http-httpsendresponseentitybody).

To enable W3C response logging on a per request basis, the application performs the following steps:

1.  The application initializes the members of the [**HTTP\_LOG\_FIELDS\_DATA**](/windows/desktop/api/Http/ns-http-http_log_fields_data) with the field information that will be logged for that response.
2.  The **Base.Type** member of the [**HTTP\_LOG\_FIELDS\_DATA**](/windows/desktop/api/Http/ns-http-http_log_fields_data) structure should be initialized to **HttpLogDataTypeFields**. The **Base.Type** field ensures the future extensibility of the structure and API.
3.  The application calls [**HttpSendHttpResponse**](/windows/desktop/api/Http/nf-http-httpsendhttpresponse) or [**HttpSendResponseEntityBody**](/windows/desktop/api/Http/nf-http-httpsendresponseentitybody) with a pointer to the [**HTTP\_LOG\_FIELDS\_DATA**](/windows/desktop/api/Http/ns-http-http_log_fields_data) structure in the *pLogData* parameter. The application should type cast the pointer to [**PHTTP\_LOG\_DATA**](/windows/desktop/api/Http/ns-http-http_log_data).

 

 




