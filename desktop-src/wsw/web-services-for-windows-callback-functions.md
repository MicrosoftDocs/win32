---
title: Windows Web Services Callback Functions
description: Callbacks enable an application to call a function defined at another layer or level.
ms.assetid: 7398ec42-388a-494c-9fe4-5bd62aa009cb
keywords:
- WWSAPI
- WWS
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Windows Web Services Callback Functions

Callbacks enable an application to call a function defined at another layer or level. The application registers the function argument as a handler that is to be called asynchronously at a later time as required. The callback is invoked if the function completes asynchronously indicating function success or error. The callback is not called if the operation completes synchronously.

The Windows Web Services API includes the following callback functions:

-   [**WS\_ABANDON\_MESSAGE\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_abandon_message_callback?branch=master)
-   [**WS\_ABORT\_CHANNEL\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_abort_channel_callback?branch=master)
-   [**WS\_ABORT\_LISTENER\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_abort_listener_callback?branch=master)
-   [**WS\_ACCEPT\_CHANNEL\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_accept_channel_callback?branch=master)
-   [**WS\_ASYNC\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_async_callback?branch=master)
-   [**WS\_ASYNC\_FUNCTION**](/windows/win32/WebServices/nc-webservices-ws_async_function?branch=master)
-   [**WS\_CERT\_ISSUER\_LIST\_NOTIFICATION\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_cert_issuer_list_notification_callback?branch=master)
-   [**WS\_CERTIFICATE\_VALIDATION\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_certificate_validation_callback?branch=master)
-   [**WS\_CLOSE\_CHANNEL\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_close_channel_callback?branch=master)
-   [**WS\_CLOSE\_LISTENER\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_close_listener_callback?branch=master)
-   [**WS\_CREATE\_CHANNEL\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_create_channel_callback?branch=master)
-   [**WS\_CREATE\_CHANNEL\_FOR\_LISTENER\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_create_channel_for_listener_callback?branch=master)
-   [**WS\_CREATE\_DECODER\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_create_decoder_callback?branch=master)
-   [**WS\_CREATE\_ENCODER\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_create_encoder_callback?branch=master)
-   [**WS\_CREATE\_LISTENER\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_create_listener_callback?branch=master)
-   [**WS\_DECODER\_DECODE\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_decoder_decode_callback?branch=master)
-   [**WS\_DECODER\_END\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_decoder_end_callback?branch=master)
-   [**WS\_DECODER\_GET\_CONTENT\_TYPE\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_decoder_get_content_type_callback?branch=master)
-   [**WS\_DECODER\_START\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_decoder_start_callback?branch=master)
-   [**WS\_DURATION\_COMPARISON\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_duration_comparison_callback?branch=master)
-   [**WS\_DYNAMIC\_STRING\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_dynamic_string_callback?branch=master)
-   [**WS\_ENCODER\_ENCODE\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_encoder_encode_callback?branch=master)
-   [**WS\_ENCODER\_END\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_encoder_end_callback?branch=master)
-   [**WS\_ENCODER\_GET\_CONTENT\_TYPE\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_encoder_get_content_type_callback?branch=master)
-   [**WS\_ENCODER\_START\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_encoder_start_callback?branch=master)
-   [**WS\_FREE\_CHANNEL\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_free_channel_callback?branch=master)
-   [**WS\_FREE\_DECODER\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_free_decoder_callback?branch=master)
-   [**WS\_FREE\_ENCODER\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_free_encoder_callback?branch=master)
-   [**WS\_FREE\_LISTENER\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_free_listener_callback?branch=master)
-   [**WS\_GET\_CERT\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_get_cert_callback?branch=master)
-   [**WS\_GET\_CHANNEL\_PROPERTY\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_get_channel_property_callback?branch=master)
-   [**WS\_GET\_LISTENER\_PROPERTY\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_get_listener_property_callback?branch=master)
-   [**WS\_HTTP\_REDIRECT\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_http_redirect_callback?branch=master)
-   [**WS\_IS\_DEFAULT\_VALUE\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_is_default_value_callback?branch=master)
-   [**WS\_MESSAGE\_DONE\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_message_done_callback?branch=master)
-   [**WS\_OPEN\_CHANNEL\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_open_channel_callback?branch=master)
-   [**WS\_OPEN\_LISTENER\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_open_listener_callback?branch=master)
-   [**WS\_OPERATION\_CANCEL\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_operation_cancel_callback?branch=master)
-   [**WS\_OPERATION\_FREE\_STATE\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_operation_free_state_callback?branch=master)
-   [**WS\_PROXY\_MESSAGE\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_proxy_message_callback?branch=master)
-   [**WS\_PULL\_BYTES\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_pull_bytes_callback?branch=master)
-   [**WS\_PUSH\_BYTES\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_push_bytes_callback?branch=master)
-   [**WS\_READ\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_read_callback?branch=master)
-   [**WS\_READ\_MESSAGE\_END\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_read_message_end_callback?branch=master)
-   [**WS\_READ\_MESSAGE\_START\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_read_message_start_callback?branch=master)
-   [**WS\_READ\_TYPE\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_read_type_callback?branch=master)
-   [**WS\_RESET\_CHANNEL\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_reset_channel_callback?branch=master)
-   [**WS\_RESET\_LISTENER\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_reset_listener_callback?branch=master)
-   [**WS\_SERVICE\_ACCEPT\_CHANNEL\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_service_accept_channel_callback?branch=master)
-   [**WS\_SERVICE\_CLOSE\_CHANNEL\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_service_close_channel_callback?branch=master)
-   [**WS\_SERVICE\_MESSAGE\_RECEIVE\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_service_message_receive_callback?branch=master)
-   [**WS\_SERVICE\_SECURITY\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_service_security_callback?branch=master)
-   [**WS\_SERVICE\_STUB\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_service_stub_callback?branch=master)
-   [**WS\_SET\_CHANNEL\_PROPERTY\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_set_channel_property_callback?branch=master)
-   [**WS\_SET\_LISTENER\_PROPERTY\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_set_listener_property_callback?branch=master)
-   [**WS\_SHUTDOWN\_SESSION\_CHANNEL\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_shutdown_session_channel_callback?branch=master)
-   [**WS\_VALIDATE\_PASSWORD\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_validate_password_callback?branch=master)
-   [**WS\_VALIDATE\_SAML\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_validate_saml_callback?branch=master)
-   [**WS\_WRITE\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_write_callback?branch=master)
-   [**WS\_WRITE\_MESSAGE\_END\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_write_message_end_callback?branch=master)
-   [**WS\_WRITE\_MESSAGE\_START\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_write_message_start_callback?branch=master)
-   [**WS\_WRITE\_TYPE\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_write_type_callback?branch=master)

 

 




