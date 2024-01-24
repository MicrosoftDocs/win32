---
description: Represent network address types. Use one or more (as a bitwise combination) of the following constants to create a network address mask to use with the macro NetAddr\_SetAllowType.
title: NET_STRING (Iphlpapi.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 4144dac9-772c-49cb-b924-e852fb4c81c7
api_name: 
 - NET_STRING_IPV4_ADDRESS
 - NET_STRING_IPV4_SERVICE
 - NET_STRING_IPV4_NETWORK
 - NET_STRING_IPV6_ADDRESS
 - NET_STRING_IPV6_ADDRESS_NO_SCOPE
 - NET_STRING_IPV6_SERVICE
 - NET_STRING_IPV6_SERVICE_NO_SCOPE
 - NET_STRING_IPV6_NETWORK
 - NET_STRING_NAMED_ADDRESS
 - NET_STRING_NAMED_SERVICE
 - NET_STRING_IP_ADDRESS
 - NET_STRING_IP_ADDRESS_NO_SCOPE
 - NET_STRING_IP_SERVICE
 - NET_STRING_IP_SERVICE_NO_SCOPE
 - NET_STRING_IP_NETWORK
 - NET_STRING_ANY_ADDRESS
 - NET_STRING_ANY_ADDRESS_NO_SCOPE
 - NET_STRING_ANY_SERVICE
 - NET_STRING_ANY_SERVICE_NO_SCOPE
api_type: 
 - HeaderDef
api_location: 
 - Iphlpapi.h
topic_type: 
 - APIRef
 - kbSyntax

---

# NET\_STRING

Represent network address types. Use one or more (as a bitwise combination) of the following constants to create a network address mask to use with the macro [**NetAddr\_SetAllowType**](/windows/desktop/api/Shellapi/nf-shellapi-netaddr_setallowtype).



| Constant                                                                                                                                                                                                                   | Description                                                                                                                                                                    |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="NET_STRING_IPV4_ADDRESS"></span><span id="net_string_ipv4_address"></span><dl> <dt>**NET\_STRING\_IPV4\_ADDRESS**</dt> </dl>                              | The string identifies an IPv4 host/router using literal address (port or prefix not allowed).<br/>                                                                       |
| <span id="NET_STRING_IPV4_SERVICE"></span><span id="net_string_ipv4_service"></span><dl> <dt>**NET\_STRING\_IPV4\_SERVICE**</dt> </dl>                              | The string identifies an IPv4 service using literal address (port required; prefix not allowed).<br/>                                                                    |
| <span id="NET_STRING_IPV4_NETWORK"></span><span id="net_string_ipv4_network"></span><dl> <dt>**NET\_STRING\_IPV4\_NETWORK**</dt> </dl>                              | The string identifies an IPv4 network (prefix required; port not allowed).<br/>                                                                                          |
| <span id="NET_STRING_IPV6_ADDRESS"></span><span id="net_string_ipv6_address"></span><dl> <dt>**NET\_STRING\_IPV6\_ADDRESS**</dt> </dl>                              | The string identifies an IPv6 Host/router using literal address (port or prefix not allowed; scope-id allowed.)<br/>                                                     |
| <span id="NET_STRING_IPV6_ADDRESS_NO_SCOPE"></span><span id="net_string_ipv6_address_no_scope"></span><dl> <dt>**NET\_STRING\_IPV6\_ADDRESS\_NO\_SCOPE**</dt> </dl> | The string identifies an IPv6 Host/router using literal address where the interface context is already known (port or prefix not allowed; scope-id not allowed).<br/>    |
| <span id="NET_STRING_IPV6_SERVICE"></span><span id="net_string_ipv6_service"></span><dl> <dt>**NET\_STRING\_IPV6\_SERVICE**</dt> </dl>                              | The string identifies an IPv6 service using literal address (port required; prefix not allowed; scope-id allowed).<br/>                                                  |
| <span id="NET_STRING_IPV6_SERVICE_NO_SCOPE"></span><span id="net_string_ipv6_service_no_scope"></span><dl> <dt>**NET\_STRING\_IPV6\_SERVICE\_NO\_SCOPE**</dt> </dl> | The string identifies an IPv6 service using literal address where the interface context is already known (port required; prefix not allowed; scope-id not allowed).<br/> |
| <span id="NET_STRING_IPV6_NETWORK"></span><span id="net_string_ipv6_network"></span><dl> <dt>**NET\_STRING\_IPV6\_NETWORK**</dt> </dl>                              | The string identifies an IPv6 network (prefix required; port or scope-id not allowed).<br/>                                                                              |
| <span id="NET_STRING_NAMED_ADDRESS"></span><span id="net_string_named_address"></span><dl> <dt>**NET\_STRING\_NAMED\_ADDRESS**</dt> </dl>                           | The string identifies an Internet Host using the DNS(port or prefix or scope-id not allowed).<br/>                                                                       |
| <span id="NET_STRING_NAMED_SERVICE"></span><span id="net_string_named_service"></span><dl> <dt>**NET\_STRING\_NAMED\_SERVICE**</dt> </dl>                           | The string identifies an Internet service using DNS (port required; prefix or scope-id not allowed).<br/>                                                                |
| <span id="NET_STRING_IP_ADDRESS"></span><span id="net_string_ip_address"></span><dl> <dt>**NET\_STRING\_IP\_ADDRESS**</dt> </dl>                                    | NET\_STRING\_IPV4\_ADDRESS \| NET\_STRING\_IPV6\_ADDRESS.<br/>                                                                                                           |
| <span id="NET_STRING_IP_ADDRESS_NO_SCOPE"></span><span id="net_string_ip_address_no_scope"></span><dl> <dt>**NET\_STRING\_IP\_ADDRESS\_NO\_SCOPE**</dt> </dl>       | NET\_STRING\_IPV4\_ADDRESS \| NET\_STRING\_IPV6\_ADDRESS\_NO\_SCOPE. <br/>                                                                                               |
| <span id="NET_STRING_IP_SERVICE"></span><span id="net_string_ip_service"></span><dl> <dt>**NET\_STRING\_IP\_SERVICE**</dt> </dl>                                    | NET\_STRING\_IPV4\_SERVICE \| NET\_STRING\_IPV6\_SERVICE.<br/>                                                                                                           |
| <span id="NET_STRING_IP_SERVICE_NO_SCOPE"></span><span id="net_string_ip_service_no_scope"></span><dl> <dt>**NET\_STRING\_IP\_SERVICE\_NO\_SCOPE**</dt> </dl>       | NET\_STRING\_NAMED\_ADDRESS \| NET\_STRING\_IP\_ADDRESS\_NO\_SCOPE.<br/>                                                                                                 |
| <span id="NET_STRING_IP_NETWORK"></span><span id="net_string_ip_network"></span><dl> <dt>**NET\_STRING\_IP\_NETWORK**</dt> </dl>                                    | NET\_STRING\_IPV4\_NETWORK \| NET\_STRING\_IPV6\_NETWORK.<br/>                                                                                                           |
| <span id="NET_STRING_ANY_ADDRESS"></span><span id="net_string_any_address"></span><dl> <dt>**NET\_STRING\_ANY\_ADDRESS**</dt> </dl>                                 | NET\_STRING\_NAMED\_ADDRESS \| NET\_STRING\_IP\_ADDRESS.<br/>                                                                                                            |
| <span id="NET_STRING_ANY_ADDRESS_NO_SCOPE"></span><span id="net_string_any_address_no_scope"></span><dl> <dt>**NET\_STRING\_ANY\_ADDRESS\_NO\_SCOPE**</dt> </dl>    | NET\_STRING\_NAMED\_ADDRESS \| NET\_STRING\_IP\_ADDRESS\_NO\_SCOPE.<br/>                                                                                                 |
| <span id="NET_STRING_ANY_SERVICE"></span><span id="net_string_any_service"></span><dl> <dt>**NET\_STRING\_ANY\_SERVICE**</dt> </dl>                                 | NET\_STRING\_NAMED\_SERVICE \| NET\_STRING\_IP\_SERVICE.<br/>                                                                                                            |
| <span id="NET_STRING_ANY_SERVICE_NO_SCOPE"></span><span id="net_string_any_service_no_scope"></span><dl> <dt>**NET\_STRING\_ANY\_SERVICE\_NO\_SCOPE**</dt> </dl>    | NET\_STRING\_NAMED\_ADDRESS \| NET\_STRING\_IP\_ADDRESS\_NO\_SCOPE.<br/>                                                                                                 |



## Remarks

These values are defined in Iphlpapi.h.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Iphlpapi.h</dt> </dl> |



 

 




