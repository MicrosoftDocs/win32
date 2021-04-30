---
description: These constants and corresponding values indicate HTTP status codes returned by servers on the Internet.
ms.assetid: 3de6a35d-41e9-4fce-ab92-e970c7c07e55
title: HTTP Status Codes (Winhttp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# HTTP Status Codes (Winhttp.h)

These constants and corresponding values indicate HTTP status codes returned by servers on the Internet.

<dl> <dt>

<span id="HTTP_STATUS_CONTINUE"></span><span id="http_status_continue"></span>**HTTP\_STATUS\_CONTINUE**
</dt> <dd> <dl> <dt>

100
</dt> <dt>



The request can be continued.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_SWITCH_PROTOCOLS"></span><span id="http_status_switch_protocols"></span>**HTTP\_STATUS\_SWITCH\_PROTOCOLS**
</dt> <dd> <dl> <dt>

101
</dt> <dt>



The server has switched protocols in an upgrade header.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_OK"></span><span id="http_status_ok"></span>**HTTP\_STATUS\_OK**
</dt> <dd> <dl> <dt>

200
</dt> <dt>



The request completed successfully.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_CREATED"></span><span id="http_status_created"></span>**HTTP\_STATUS\_CREATED**
</dt> <dd> <dl> <dt>

201
</dt> <dt>



The request has been fulfilled and resulted in the creation of a new resource.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_ACCEPTED"></span><span id="http_status_accepted"></span>**HTTP\_STATUS\_ACCEPTED**
</dt> <dd> <dl> <dt>

202
</dt> <dt>



The request has been accepted for processing, but the processing has not been completed.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_PARTIAL"></span><span id="http_status_partial"></span>**HTTP\_STATUS\_PARTIAL**
</dt> <dd> <dl> <dt>

203
</dt> <dt>



The returned meta information in the entity-header is not the definitive set available from the originating server.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_NO_CONTENT"></span><span id="http_status_no_content"></span>**HTTP\_STATUS\_NO\_CONTENT**
</dt> <dd> <dl> <dt>

204
</dt> <dt>



The server has fulfilled the request, but there is no new information to send back.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_RESET_CONTENT"></span><span id="http_status_reset_content"></span>**HTTP\_STATUS\_RESET\_CONTENT**
</dt> <dd> <dl> <dt>

205
</dt> <dt>



The request has been completed, and the client program should reset the document view that caused the request to be sent to allow the user to easily initiate another input action.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_PARTIAL_CONTENT"></span><span id="http_status_partial_content"></span>**HTTP\_STATUS\_PARTIAL\_CONTENT**
</dt> <dd> <dl> <dt>

206
</dt> <dt>



The server has fulfilled the partial GET request for the resource.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_WEBDAV_MULTI_STATUS"></span><span id="http_status_webdav_multi_status"></span>**HTTP\_STATUS\_WEBDAV\_MULTI\_STATUS**
</dt> <dd> <dl> <dt>

207
</dt> <dt>



During a World Wide Web Distributed Authoring and Versioning (WebDAV) operation, this indicates multiple status codes for a single response. The response body contains Extensible Markup Language (XML) that describes the status codes. For more information, see [HTTP Extensions for Distributed Authoring](../webdav/webdav-portal.md).


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_AMBIGUOUS"></span><span id="http_status_ambiguous"></span>**HTTP\_STATUS\_AMBIGUOUS**
</dt> <dd> <dl> <dt>

300
</dt> <dt>



The requested resource is available at one or more locations.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_MOVED"></span><span id="http_status_moved"></span>**HTTP\_STATUS\_MOVED**
</dt> <dd> <dl> <dt>

301
</dt> <dt>



The requested resource has been assigned to a new permanent Uniform Resource Identifier (URI), and any future references to this resource should be done using one of the returned URIs.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_REDIRECT"></span><span id="http_status_redirect"></span>**HTTP\_STATUS\_REDIRECT**
</dt> <dd> <dl> <dt>

302
</dt> <dt>



The requested resource resides temporarily under a different URI.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_REDIRECT_METHOD"></span><span id="http_status_redirect_method"></span>**HTTP\_STATUS\_REDIRECT\_METHOD**
</dt> <dd> <dl> <dt>

303
</dt> <dt>



The response to the request can be found under a different URI and should be retrieved using a GET [*HTTP verb*](glossary.md) on that resource.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_NOT_MODIFIED"></span><span id="http_status_not_modified"></span>**HTTP\_STATUS\_NOT\_MODIFIED**
</dt> <dd> <dl> <dt>

304
</dt> <dt>



The requested resource has not been modified.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_USE_PROXY"></span><span id="http_status_use_proxy"></span>**HTTP\_STATUS\_USE\_PROXY**
</dt> <dd> <dl> <dt>

305
</dt> <dt>



The requested resource must be accessed through the proxy given by the location field.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_REDIRECT_KEEP_VERB"></span><span id="http_status_redirect_keep_verb"></span>**HTTP\_STATUS\_REDIRECT\_KEEP\_VERB**
</dt> <dd> <dl> <dt>

307
</dt> <dt>



The redirected request keeps the same [*HTTP verb*](glossary.md). HTTP/1.1 behavior.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_BAD_REQUEST"></span><span id="http_status_bad_request"></span>**HTTP\_STATUS\_BAD\_REQUEST**
</dt> <dd> <dl> <dt>

400
</dt> <dt>



The request could not be processed by the server due to invalid syntax.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_DENIED"></span><span id="http_status_denied"></span>**HTTP\_STATUS\_DENIED**
</dt> <dd> <dl> <dt>

401
</dt> <dt>



The requested resource requires user authentication.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_PAYMENT_REQ"></span><span id="http_status_payment_req"></span>**HTTP\_STATUS\_PAYMENT\_REQ**
</dt> <dd> <dl> <dt>

402
</dt> <dt>



Not implemented in the HTTP protocol.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_FORBIDDEN"></span><span id="http_status_forbidden"></span>**HTTP\_STATUS\_FORBIDDEN**
</dt> <dd> <dl> <dt>

403
</dt> <dt>



The server understood the request, but cannot fulfill it.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_NOT_FOUND"></span><span id="http_status_not_found"></span>**HTTP\_STATUS\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

404
</dt> <dt>



The server has not found anything that matches the requested URI.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_BAD_METHOD"></span><span id="http_status_bad_method"></span>**HTTP\_STATUS\_BAD\_METHOD**
</dt> <dd> <dl> <dt>

405
</dt> <dt>



The [*HTTP verb*](glossary.md) used is not allowed.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_NONE_ACCEPTABLE"></span><span id="http_status_none_acceptable"></span>**HTTP\_STATUS\_NONE\_ACCEPTABLE**
</dt> <dd> <dl> <dt>

406
</dt> <dt>



No responses acceptable to the client were found.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_PROXY_AUTH_REQ"></span><span id="http_status_proxy_auth_req"></span>**HTTP\_STATUS\_PROXY\_AUTH\_REQ**
</dt> <dd> <dl> <dt>

407
</dt> <dt>



Proxy authentication required.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_REQUEST_TIMEOUT"></span><span id="http_status_request_timeout"></span>**HTTP\_STATUS\_REQUEST\_TIMEOUT**
</dt> <dd> <dl> <dt>

408
</dt> <dt>



The server timed out waiting for the request.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_CONFLICT"></span><span id="http_status_conflict"></span>**HTTP\_STATUS\_CONFLICT**
</dt> <dd> <dl> <dt>

409
</dt> <dt>



The request could not be completed due to a conflict with the current state of the resource. The user should resubmit with more information.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_GONE"></span><span id="http_status_gone"></span>**HTTP\_STATUS\_GONE**
</dt> <dd> <dl> <dt>

410
</dt> <dt>



The requested resource is no longer available at the server, and no forwarding address is known.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_LENGTH_REQUIRED"></span><span id="http_status_length_required"></span>**HTTP\_STATUS\_LENGTH\_REQUIRED**
</dt> <dd> <dl> <dt>

411
</dt> <dt>



The server cannot accept the request without a defined content length.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_PRECOND_FAILED"></span><span id="http_status_precond_failed"></span>**HTTP\_STATUS\_PRECOND\_FAILED**
</dt> <dd> <dl> <dt>

412
</dt> <dt>



The precondition given in one or more of the request header fields evaluated to false when it was tested on the server.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_REQUEST_TOO_LARGE"></span><span id="http_status_request_too_large"></span>**HTTP\_STATUS\_REQUEST\_TOO\_LARGE**
</dt> <dd> <dl> <dt>

413
</dt> <dt>



The server cannot process the request because the request entity is larger than the server is able to process.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_URI_TOO_LONG"></span><span id="http_status_uri_too_long"></span>**HTTP\_STATUS\_URI\_TOO\_LONG**
</dt> <dd> <dl> <dt>

414
</dt> <dt>



The server cannot service the request because the request URI is longer than the server can interpret.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_UNSUPPORTED_MEDIA"></span><span id="http_status_unsupported_media"></span>**HTTP\_STATUS\_UNSUPPORTED\_MEDIA**
</dt> <dd> <dl> <dt>

415
</dt> <dt>



The server cannot service the request because the entity of the request is in a format not supported by the requested resource for the requested method.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_RETRY_WITH"></span><span id="http_status_retry_with"></span>**HTTP\_STATUS\_RETRY\_WITH**
</dt> <dd> <dl> <dt>

449
</dt> <dt>



The request should be retried after doing the appropriate action.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_SERVER_ERROR"></span><span id="http_status_server_error"></span>**HTTP\_STATUS\_SERVER\_ERROR**
</dt> <dd> <dl> <dt>

500
</dt> <dt>



The server encountered an unexpected condition that prevented it from fulfilling the request.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_NOT_SUPPORTED"></span><span id="http_status_not_supported"></span>**HTTP\_STATUS\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

501
</dt> <dt>



The server does not support the functionality required to fulfill the request.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_BAD_GATEWAY"></span><span id="http_status_bad_gateway"></span>**HTTP\_STATUS\_BAD\_GATEWAY**
</dt> <dd> <dl> <dt>

502
</dt> <dt>



The server, while acting as a gateway or proxy, received an invalid response from the upstream server it accessed in attempting to fulfill the request.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_SERVICE_UNAVAIL"></span><span id="http_status_service_unavail"></span>**HTTP\_STATUS\_SERVICE\_UNAVAIL**
</dt> <dd> <dl> <dt>

503
</dt> <dt>



The service is temporarily overloaded.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_GATEWAY_TIMEOUT"></span><span id="http_status_gateway_timeout"></span>**HTTP\_STATUS\_GATEWAY\_TIMEOUT**
</dt> <dd> <dl> <dt>

504
</dt> <dt>



The request was timed out waiting for a gateway.


</dt> </dl> </dd> <dt>

<span id="HTTP_STATUS_VERSION_NOT_SUP"></span><span id="http_status_version_not_sup"></span>**HTTP\_STATUS\_VERSION\_NOT\_SUP**
</dt> <dd> <dl> <dt>

505
</dt> <dt>



The server does not support the HTTP protocol version that was used in the request message.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP, Windows 2000 Professional with SP3 \[desktop apps only\]<br/>      |
| Minimum supported server<br/> | Windows Server 2003, Windows 2000 Server with SP3 \[desktop apps only\]<br/>   |
| Header<br/>                   | <dl> <dt>Winhttp.h</dt> </dl> |



## See also

<dl> <dt>

[WinHTTP Versions](winhttp-versions.md)
</dt> </dl>

 

