---
title: Security Binding Settings
description: Security binding settings control the way a security token is obtained or used.
ms.assetid: 4bc03cb4-1ac2-4ad1-a45d-eae8f50f5355
keywords:
- Security Binding Settings Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# Security Binding Settings

Security binding settings control the way a security token is obtained or used. They are represented as a collection of property-value pairs, with the property keys defined by the enumeration [**WS\_SECURITY\_BINDING\_PROPERTY**](/windows/desktop/api/WebServices/ns-webservices-ws_security_binding_property). Each property in the collection has a reasonable default value. As a result, it is possible to define and use a security description without specifying any of the security binding settings.


For information on channel-wide security settings, with properties whose keys are defined by the [**WS\_SECURITY\_PROPERTY\_ID**](/windows/desktop/api/WebServices/ne-webservices-ws_security_property_id) enumeration, see[Security Channel Settings](security-channel-settings.md).

The following API elements are used with security binding settings.

| Enumeration                                                                          | Description                                                                                                                                                       |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WS\_CERT\_FAILURE**](/windows/win32/api/webservices/ne-webservices-ws_value_type)                                         | Defines failures related to certificate validation.                                                                                                               |
| **WS\_HTTP\_HEADER\_AUTH\_SCHEME**                 | Defines the options for performing client authentication using HTTP authentication headers.                                                                       |
| [**WS\_HTTP\_HEADER\_AUTH\_TARGET**](/windows/desktop/api/WebServices/ne-webservices-ws_http_header_auth_target)                 | Defines the target for the HTTP header authentication security binding.                                                                                           |
| [**WS\_REQUEST\_SECURITY\_TOKEN\_ACTION**](/windows/desktop/api/WebServices/ne-webservices-ws_request_security_token_action)     | Defines which set of actions to use when negotiating security tokens using WS-Trust.                                                                              |
| [**WS\_SECURITY\_ALGORITHM\_SUITE\_NAME**](/windows/desktop/api/WebServices/ne-webservices-ws_security_algorithm_suite_name)     | A suite of security algorithms used for tasks such as signing and encryting.                                                                                      |
| [**WS\_SECURITY\_BINDING\_PROPERTY\_ID**](/windows/desktop/api/WebServices/ne-webservices-ws_security_binding_property_id)       | Identifies the properties used to specify security binding settings.                                                                                              |
| [**WS\_SECURITY\_KEY\_ENTROPY\_MODE**](/windows/desktop/api/WebServices/ne-webservices-ws_security_key_entropy_mode)             | Defines how randomness should be contributed to the issued key during a security token negotiation done with message and mixed-mode security.                     |
| [**WS\_SECURITY\_KEY\_TYPE**](/windows/desktop/api/WebServices/ne-webservices-ws_security_key_type)                              | The key type of a security token.                                                                                                                                 |
| [**WS\_SECURITY\_TOKEN\_REFERENCE\_MODE**](/windows/desktop/api/WebServices/ne-webservices-ws_security_token_reference_mode)     | the mechanism to use to refer to a security token from signatures, encrypted items and derived tokens in the context of message and mixed-mode security bindings. |
| [**WS\_TRUST\_VERSION**](/windows/desktop/api/WebServices/ne-webservices-ws_trust_version)                                       | Defines the WS-Trust specification version to be used with message security and mixed-mode security.                                                              |
| [**WS\_WINDOWS\_INTEGRATED\_AUTH\_PACKAGE**](/windows/desktop/api/WebServices/ne-webservices-ws_windows_integrated_auth_package) | Defines the specific SSP package to be used for Windows Integrated Authentication.                                                                                |



 



| Structure                                                               | Description                                    |
|-------------------------------------------------------------------------|------------------------------------------------|
| [**WS\_SECURITY\_BINDING\_PROPERTY**](/windows/desktop/api/WebServices/ns-webservices-ws_security_binding_property) | Specifies a security binding specific setting. |



 

 

 




