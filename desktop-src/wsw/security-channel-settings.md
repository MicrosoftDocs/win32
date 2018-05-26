---
title: Security Channel Settings
description: Security channel settings control the way security is applied and verified on a channel.
ms.assetid: ad964874-0bc7-4f03-8ceb-33627ff99f08
keywords:
- Security Channel Settings Web Services for Windows
- WWSAPI
- WWS
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Security Channel Settings

Security channel settings control the way security is applied and verified on a channel. Each security channel setting is represented by a collection of property-value pairs, with the property keys defined by the enumeration [**WS\_SECURITY\_PROPERTY\_ID**](/windows/win32/WebServices/ne-webservices-ws_security_property_id?branch=master). Each property in the collection has a reasonable default value. Because of these default values, it is possible to define and use a security description without specifying any of the security channel settings.

## 

[Security binding settings](security-binding-settings.md) contain similar collections of property-value pairs whose keys are defined by the [**WS\_SECURITY\_BINDING\_PROPERTY**](/windows/win32/WebServices/ns-webservices-_ws_security_binding_property?branch=master) structure. The difference between these two sorts of settings is that the security channel settings are scoped to a security description (that is, they contain channel-wide security properties), whereas security binding settings are scoped to one of the security bindings, and there may be many security bindings. Consequently, for example, a custom security description that contains three security bindings will have one security channel settings bag for the entire channel and three security binding settings bags, one for each security binding.

The following enumerations are used with security channel settings:

-   [**WS\_PROTECTION\_LEVEL**](/windows/win32/WebServices/ne-webservices-ws_protection_level?branch=master)
-   [**WS\_REQUEST\_SECURITY\_TOKEN\_PROPERTY\_ID**](/windows/win32/WebServices/ne-webservices-ws_request_security_token_property_id?branch=master)
-   [**WS\_SECURITY\_ALGORITHM\_ID**](/windows/win32/WebServices/ne-webservices-ws_security_algorithm_id?branch=master)
-   [**WS\_SECURITY\_ALGORITHM\_PROPERTY\_ID**](/windows/win32/WebServices/ne-webservices-__unnamed_enum_7?branch=master)
-   [**WS\_SECURITY\_HEADER\_LAYOUT**](/windows/win32/WebServices/ne-webservices-ws_security_header_layout?branch=master)
-   [**WS\_SECURITY\_HEADER\_VERSION**](/windows/win32/WebServices/ne-webservices-ws_security_header_version?branch=master)
-   [**WS\_SECURITY\_PROPERTY\_ID**](/windows/win32/WebServices/ne-webservices-ws_security_property_id?branch=master)
-   [**WS\_SECURITY\_TIMESTAMP\_USAGE**](/windows/win32/WebServices/ne-webservices-ws_security_timestamp_usage?branch=master)
-   [**WS\_XML\_SECURITY\_TOKEN\_PROPERTY\_ID**](/windows/win32/WebServices/ne-webservices-ws_xml_security_token_property_id?branch=master)

The following structures are used with security channel settings:

-   [**WS\_REQUEST\_SECURITY\_TOKEN\_PROPERTY**](/windows/win32/WebServices/ns-webservices-_ws_request_security_token_property?branch=master)
-   [**WS\_SECURITY\_ALGORITHM\_PROPERTY**](/windows/win32/WebServices/ns-webservices-_ws_security_algorithm_property?branch=master)
-   [**WS\_SECURITY\_ALGORITHM\_SUITE**](/windows/win32/WebServices/ns-webservices-_ws_security_algorithm_suite?branch=master)
-   [**WS\_SECURITY\_PROPERTY**](/windows/win32/WebServices/ns-webservices-_ws_security_property?branch=master)
-   [**WS\_XML\_SECURITY\_TOKEN\_PROPERTY**](/windows/win32/WebServices/ns-webservices-_ws_xml_security_token_property?branch=master)

 

 




