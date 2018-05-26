---
Description: This section contains kernel mode network driver reference topics for the Ifdef.h header.
ms.assetid: AF046F11-0D17-4451-8DE1-499443AD0071
title: Ifdef.h
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Ifdef.h

This section contains kernel mode network driver reference topics for the Ifdef.h header. This header is included in the Windows SDK as it is also shared with user mode networking applications.

The Ifdef.h header contains definitions for NDIS Network Interface.

## In this section



| Topic                                                                             | Description                                                                                                                                                                                           |
|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IF\_OPER\_STATUS**](/windows/win32/ifdef/?branch=master)<br/>                             | The IF\_OPER\_STATUS enumeration type defines the current [NDIS network interface](netvista.ndis_network_interfaces2) operational status, as described in RFC 2863.<br/>                        |
| [**NET\_IF\_ACCESS\_TYPE**](/windows/win32/ifdef/ne-ifdef-_net_if_access_type?branch=master)<br/>                    | The NET\_IF\_ACCESS\_TYPE enumeration type specifies the [NDIS network interface](netvista.ndis_network_interfaces2) access type.<br/>                                                          |
| [**NET\_IF\_ADMIN\_STATUS**](/windows/win32/ifdef/ne-ifdef-_net_if_admin_status?branch=master)<br/>                  | The NET\_IF\_ADMIN\_STATUS enumeration type specifies the [NDIS network interface](netvista.ndis_network_interfaces2) administrative status, as described in RFC 2863.<br/>                     |
| [**NET\_IF\_CONNECTION\_TYPE**](/windows/win32/ifdef/ne-ifdef-_net_if_connection_type?branch=master)<br/>            | The NET\_IF\_CONNECTION\_TYPE enumeration type specifies the [NDIS network interface](netvista.ndis_network_interfaces2) connection type.<br/>                                                  |
| [**NET\_IF\_DIRECTION\_TYPE**](/windows/win32/ifdef/ne-ifdef-_net_if_direction_type?branch=master)<br/>              | The NET\_IF\_ACCESS\_TYPE enumeration type specifies the [NDIS network interface](netvista.ndis_network_interfaces2) direction type.<br/>                                                       |
| [**NET\_IF\_MEDIA\_CONNECT\_STATE**](/windows/win32/ifdef/ne-ifdef-_net_if_media_connect_state?branch=master)<br/>   | The NET\_IF\_MEDIA\_CONNECT\_STATE enumeration type specifies the [NDIS network interface](netvista.ndis_network_interfaces2) connection state.<br/>                                            |
| [**NET\_IF\_MEDIA\_DUPLEX\_STATE**](/windows/win32/ifdef/ne-ifdef-_net_if_media_duplex_state?branch=master)<br/>     | The NET\_IF\_MEDIA\_DUPLEX\_STATE enumeration type specifies the [NDIS network interface](netvista.ndis_network_interfaces2) duplex state.<br/>                                                 |
| [**NET\_IF\_OPER\_STATUS**](/windows/win32/ifdef/ne-ifdef-_net_if_oper_status?branch=master)<br/>                    | The NET\_IF\_OPER\_STATUS enumeration type defines the current [NDIS network interface](netvista.ndis_network_interfaces2) operational status.<br/>                                             |
| [**TUNNEL\_TYPE**](/windows/win32/ifdef/ne-ifdef-tunnel_type?branch=master)<br/>                                    | The TUNNEL\_TYPE enumeration type defines the encapsulation method used by a tunnel, as described by the Internet Assigned Names Authority (IANA).<br/>                                         |
| [**NDIS\_INTERFACE\_INFORMATION**](/windows/win32/ifdef/ns-ifdef-_ndis_interface_information?branch=master)<br/> | The NDIS\_INTERFACE\_INFORMATION structure provides information about a network interface for the [OID\_GEN\_INTERFACE\_INFO](netvista.oid_gen_interface_info) OID.<br/>                        |
| [**IF\_COUNTED\_STRING**](/windows/win32/Ifdef/ns-ifdef-_if_counted_string_lh?branch=master)<br/>                       | The [**IF\_COUNTED\_STRING**](/windows/win32/Ifdef/ns-ifdef-_if_counted_string_lh?branch=master) structure specifies a counted string for NDIS interfaces.<br/>                                                                             |
| [**NET\_LUID**](/windows/win32/Ifdef/?branch=master)<br/>                                          | A [**NET\_LUID**](/windows/win32/Ifdef/?branch=master) union can be accessed as a 64-bit value that identifies an NDIS network interface or as a structure that contains the associated interface index and type.<br/> |
| [**NET\_PHYSICAL\_LOCATION**](/windows/win32/Ifdef/ns-ifdef-_net_physical_location_lh?branch=master)<br/>               | The NET\_PHYSICAL\_LOCATION structure provides NDIS with information about the physical location of a registered network interface.<br/>                                                        |



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20Ifdef.h%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




