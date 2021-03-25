---
description: "Learn more about: WUA Networking Error Codes"
ms.assetid: 07ff2ed7-09bc-4af7-84f9-66a921c0f53f
title: WUA Networking Error Codes (Wuerror.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WUA Networking Error Codes

The Windows Update Agent (WUA) API can return the following error codes when performing network operations such as searching for updates:



| Constant/value                                                                                                                                                                                                                                                                                        | Description                                                                                                                                                                                  |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="WU_E_WINHTTP_INVALID_FILE"></span><span id="wu_e_winhttp_invalid_file"></span><dl> <dt>**WU\_E\_WINHTTP\_INVALID\_FILE**</dt> <dt>0x80240038</dt> </dl>                                  | The downloaded file has an unexpected content type.<br/>                                                                                                                               |
| <span id="WU_E_PT_HTTP_STATUS_BAD_REQUEST"></span><span id="wu_e_pt_http_status_bad_request"></span><dl> <dt>**WU\_E\_PT\_HTTP\_STATUS\_BAD\_REQUEST**</dt> <dt>0x80244016</dt> </dl>              | Same as HTTP status 400 – The server could not process the request due to invalid syntax.<br/>                                                                                         |
| <span id="WU_E_PT_HTTP_STATUS_DENIED"></span><span id="wu_e_pt_http_status_denied"></span><dl> <dt>**WU\_E\_PT\_HTTP\_STATUS\_DENIED**</dt> <dt>0x80244017</dt> </dl>                              | Same as HTTP status 401 – The requested resource requires user authentication.<br/>                                                                                                    |
| <span id="WU_E_PT_HTTP_STATUS_FORBIDDEN"></span><span id="wu_e_pt_http_status_forbidden"></span><dl> <dt>**WU\_E\_PT\_HTTP\_STATUS\_FORBIDDEN**</dt> <dt>0x80244018</dt> </dl>                     | Same as HTTP status 403 – Server understood the request, but declines to fulfill it.<br/>                                                                                              |
| <span id="WU_E_PT_HTTP_STATUS_NOT_FOUND"></span><span id="wu_e_pt_http_status_not_found"></span><dl> <dt>**WU\_E\_PT\_HTTP\_STATUS\_NOT\_FOUND**</dt> <dt>0x80244019</dt> </dl>                    | Same as HTTP status 404 – The server cannot find the requested URI (Uniform Resource Identifier).<br/>                                                                                 |
| <span id="WU_E_PT_HTTP_STATUS_BAD_METHOD"></span><span id="wu_e_pt_http_status_bad_method"></span><dl> <dt>**WU\_E\_PT\_HTTP\_STATUS\_BAD\_METHOD**</dt> <dt>0x8024401A</dt> </dl>                 | Same as HTTP status 405 – The HTTP method is not allowed.<br/>                                                                                                                         |
| <span id="WU_E_PT_HTTP_STATUS_PROXY_AUTH_REQ"></span><span id="wu_e_pt_http_status_proxy_auth_req"></span><dl> <dt>**WU\_E\_PT\_HTTP\_STATUS\_PROXY\_AUTH\_REQ**</dt> <dt>0x8024401B</dt> </dl>    | Same as HTTP status 407 – Proxy authentication is required.<br/>                                                                                                                       |
| <span id="WU_E_PT_HTTP_STATUS_REQUEST_TIMEOUT"></span><span id="wu_e_pt_http_status_request_timeout"></span><dl> <dt>**WU\_E\_PT\_HTTP\_STATUS\_REQUEST\_TIMEOUT**</dt> <dt>0x8024401C</dt> </dl>  | Same as HTTP status 408 – The server timed out waiting for the request.<br/>                                                                                                           |
| <span id="WU_E_PT_HTTP_STATUS_CONFLICT"></span><span id="wu_e_pt_http_status_conflict"></span><dl> <dt>**WU\_E\_PT\_HTTP\_STATUS\_CONFLICT**</dt> <dt>0x8024401D</dt> </dl>                        | Same as HTTP status 409 – The request was not completed due to a conflict with the current state of the resource.<br/>                                                                 |
| <span id="WU_E_PT_HTTP_STATUS_GONE"></span><span id="wu_e_pt_http_status_gone"></span><dl> <dt>**WU\_E\_PT\_HTTP\_STATUS\_GONE**</dt> <dt>0x8024401E</dt> </dl>                                    | Same as HTTP status 410 – Requested resource is no longer available at the server.<br/>                                                                                                |
| <span id="WU_E_PT_HTTP_STATUS_SERVER_ERROR"></span><span id="wu_e_pt_http_status_server_error"></span><dl> <dt>**WU\_E\_PT\_HTTP\_STATUS\_SERVER\_ERROR**</dt> <dt>0x8024401F</dt> </dl>           | Same as HTTP status 500 – An error internal to the server prevented fulfilling the request.<br/>                                                                                       |
| <span id="WU_E_PT_HTTP_STATUS_NOT_SUPPORTED"></span><span id="wu_e_pt_http_status_not_supported"></span><dl> <dt>**WU\_E\_PT\_HTTP\_STATUS\_NOT\_SUPPORTED**</dt> <dt>0x80244020</dt> </dl>        | Same as HTTP status 501 – Server does not support the functionality required to fulfill the request. <br/>                                                                             |
| <span id="WU_E_PT_HTTP_STATUS_BAD_GATEWAY"></span><span id="wu_e_pt_http_status_bad_gateway"></span><dl> <dt>**WU\_E\_PT\_HTTP\_STATUS\_BAD\_GATEWAY**</dt> <dt>0x80244021</dt> </dl>              | Same as HTTP status 502 – The server, while acting as a gateway or proxy, received an invalid response from the upstream server it accessed in attempting to fulfill the request.<br/> |
| <span id="WU_E_PT_HTTP_STATUS_SERVICE_UNAVAIL"></span><span id="wu_e_pt_http_status_service_unavail"></span><dl> <dt>**WU\_E\_PT\_HTTP\_STATUS\_SERVICE\_UNAVAIL**</dt> <dt>0x80244022</dt> </dl>  | Same as HTTP status 503 – The service is temporarily overloaded.<br/>                                                                                                                  |
| <span id="WU_E_PT_HTTP_STATUS_GATEWAY_TIMEOUT"></span><span id="wu_e_pt_http_status_gateway_timeout"></span><dl> <dt>**WU\_E\_PT\_HTTP\_STATUS\_GATEWAY\_TIMEOUT**</dt> <dt>0x80244023</dt> </dl>  | Same as HTTP status 504 – The request was timed out waiting for a gateway.<br/>                                                                                                        |
| <span id="WU_E_PT_HTTP_STATUS_VERSION_NOT_SUP"></span><span id="wu_e_pt_http_status_version_not_sup"></span><dl> <dt>**WU\_E\_PT\_HTTP\_STATUS\_VERSION\_NOT\_SUP**</dt> <dt>0x80244024</dt> </dl> | Same as HTTP status 505 – The server does not support the HTTP protocol version used for the request.<br/>                                                                             |
| <span id="WU_E_PT_HTTP_STATUS_NOT_MAPPED"></span><span id="wu_e_pt_http_status_not_mapped"></span><dl> <dt>**WU\_E\_PT\_HTTP\_STATUS\_NOT\_MAPPED**</dt> <dt>0x8024402B</dt> </dl>                 | The request could not be completed and the reason did not correspond to any of the WU\_E\_PT\_HTTP\_\* error codes.<br/>                                                               |
| <span id="WU_E_PT_WINHTTP_NAME_NOT_RESOLVED"></span><span id="wu_e_pt_winhttp_name_not_resolved"></span><dl> <dt>**WU\_E\_PT\_WINHTTP\_NAME\_NOT\_RESOLVED**</dt> <dt>0x8024402C</dt> </dl>        | Same as ERROR\_WINHTTP\_NAME\_NOT\_RESOLVED - The proxy server or target server name cannot be resolved.<br/>                                                                          |



## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wuerror.h</dt> </dl> |



 

 




