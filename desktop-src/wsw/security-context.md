---
title: Security Context
description: Security contexts enable the establishment of a message security context according to WS-SecureConversation.
ms.assetid: bea92650-21bd-41d4-9dba-043d6779d85f
keywords:
- Security Context Native-Web-Services
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# Security Context

Security contexts enable the establishment of a message security context according to WS-SecureConversation. That context can then be used to secure messages as an alternative to one-shot security where the credentials are transmitted for every request. The established security context is a more efficient method of securing messages when multiple messages are exchanged.


Security contexts require the presence of bootstrap security credentials that are used to secure the messages sent in the context. The [**WS\_KERBEROS\_APREQ\_MESSAGE\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_kerberos_apreq_message_security_binding), [**WS\_XML\_TOKEN\_MESSAGE\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_token_message_security_binding), and [**WS\_USERNAME\_MESSAGE\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_username_message_security_binding) structures may be used for this purpose.

Security contexts are a message security feature and are configured by way of message security bindings.

## Client

On the client side, the security context is tied to a particular channel. It is configured using the [**WS\_SECURITY\_CONTEXT\_MESSAGE\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_security_context_message_security_binding). Behavior and lifetime of the context are determined by the channel. When the first message is sent on the channel, the security context is established. After that, the context is proactively renewed at a configurable interval. If the server returns a fault indicating that the context requires renewal, the context is renewed when the next message is sent. If the channel is in the open state, the context is canceled by a cancel message when the channel is closed.

## Server

On the server, a security context is configured the same way as on the client. However, it is not tied to any particular channel. Instead, all channels created for the listener that has the [**WS\_SECURITY\_CONTEXT\_MESSAGE\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_security_context_message_security_binding) set are capable of receiving messages with any of the security contexts that were established on channels of that listener.

When a message arrives on a channel that supports security contexts, the context used by that message can by obtained by calling the [**WsGetMessageProperty**](/windows/desktop/api/WebServices/nf-webservices-wsgetmessageproperty) function with the [**WS\_MESSAGE\_PROPERTY\_SECURITY\_CONTEXT**](/windows/desktop/api/WebServices/ne-webservices-ws_message_property_id). The retrieved value can be used with [**WsRevokeSecurityContext**](/windows/desktop/api/WebServices/nf-webservices-wsrevokesecuritycontext) and [**WsGetSecurityContextProperty**](/windows/desktop/api/WebServices/nf-webservices-wsgetsecuritycontextproperty).

## Metadata

The [**WS\_SECURITY\_CONTEXT\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_security_context_message_security_binding_constraint) structure is used to extract the security context policy from metadata. For more information, see [Metadata Import](metadata-import.md).

The following API elements are used with security contexts.

| Enumeration                                                                    | Description                                         |
|--------------------------------------------------------------------------------|-----------------------------------------------------|
| [**WS\_SECURITY\_CONTEXT\_PROPERTY\_ID**](/windows/desktop/api/WebServices/ne-webservices-ws_security_context_property_id) | Identifies a property of a security context object. |



 



| Function                                                             | Description                                        |
|----------------------------------------------------------------------|----------------------------------------------------|
| [**WsGetSecurityContextProperty**](/windows/desktop/api/WebServices/nf-webservices-wsgetsecuritycontextproperty) | Gets a property of the specified security context. |
| [**WsRevokeSecurityContext**](/windows/desktop/api/WebServices/nf-webservices-wsrevokesecuritycontext)           | Revokes a security context.                        |



 



| Handle                                           | Description                                                 |
|--------------------------------------------------|-------------------------------------------------------------|
| [WS\_SECURITY\_CONTEXT](ws-security-context.md) | An opaque type used to reference a security context object. |



 



| Structure                                                               | Description                                                               |
|-------------------------------------------------------------------------|---------------------------------------------------------------------------|
| [**WS\_SECURITY\_CONTEXT\_PROPERTY**](/windows/desktop/api/WebServices/ns-webservices-ws_security_context_property) | Defines a property of a [WS\_SECURITY\_CONTEXT](ws-security-context.md). |



 

 

 




