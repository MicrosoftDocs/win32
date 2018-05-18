---
title: Configuring and Enabling Server Side Logging
description: Configuring and Enabling Server Side Logging
ms.assetid: 'd67d8f9a-6d8a-43f2-a1ef-75f69c04b1ac'
---

# Configuring and Enabling Server Side Logging

The application enables logging on the server session or the URL group before sending the response with [**HttpSendHttpResponse**](httpsendhttpresponse.md). The following example shows how to configure and enable W3C type server side logging:

1.  The application initializes the [**HTTP\_LOGGING\_INFO**](http-logging-info.md) structure with **HttpLoggingTypeW3C** specified in the **Format** member, and a bitmask of the [**HTTP\_LOG\_FIELD**](http-log-field--constants.md) constants in the **Fields** member.
2.  The application calls [**HttpSetServerSessionProperty**](httpsetserversessionproperty.md) or [**HttpSetUrlGroupProperty**](httpseturlgroupproperty.md) with **HttpServerLoggingProperty** specified in the *Property* parameter and a pointer to the [**HTTP\_LOGGING\_INFO**](http-logging-info.md) structure in the *pPropertyInformation* parameter.

The bitmask of the [**HTTP\_LOG\_FIELD**](http-log-field--constants.md) constants contain the fields that may be logged in the W3C log file. Note that setting the **HttpServerLoggingProperty** property on a server session or a URL group does not mean that HTTP responses will be logged. Logging is performed on a per request basis when W3C is enabled in the call to [**HttpSendHttpResponse**](httpsendhttpresponse.md) or [**HttpSendResponseEntityBody**](httpsendresponseentitybody.md).

To enable W3C response logging on a per request basis, the application performs the following steps:

1.  The application initializes the members of the [**HTTP\_LOG\_FIELDS\_DATA**](http-log-fields-data.md) with the field information that will be logged for that response.
2.  The **Base.Type** member of the [**HTTP\_LOG\_FIELDS\_DATA**](http-log-fields-data.md) structure should be initialized to **HttpLogDataTypeFields**. The **Base.Type** field ensures the future extensibility of the structure and API.
3.  The application calls [**HttpSendHttpResponse**](httpsendhttpresponse.md) or [**HttpSendResponseEntityBody**](httpsendresponseentitybody.md) with a pointer to the [**HTTP\_LOG\_FIELDS\_DATA**](http-log-fields-data.md) structure in the *pLogData* parameter. The application should type cast the pointer to [**PHTTP\_LOG\_DATA**](http-log-data.md).

 

 




