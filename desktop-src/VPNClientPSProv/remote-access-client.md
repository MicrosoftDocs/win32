---
title: VPNClientPSProvider Provider
description: This section provides reference information for VPNClientPSProvider provider classes defined in VPNClientPSProvider.mof and implemented in VPNClientPSProvider.dll.
audience: developer
ms.assetid: 35188939-BBBE-4C25-ABBA-C159E011C6AC
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# VPNClientPSProvider Provider

This section provides reference information for **VPNClientPSProvider** provider classes defined in VPNClientPSProvider.mof and implemented in VPNClientPSProvider.dll.

## In this section

<dl> <dt>

[**CIM\_ManagedElement**](cim-managedelement.md)
</dt> <dd>

ManagedElement is an abstract class that provides a common superclass (or top of the inheritance tree) for the non-association classes in the CIM Schema.

</dd> <dt>

[**CIM\_NextHopRoute**](cim-nexthoproute.md)
</dt> <dd>

NextHopRoute represents one of a series of \\'hops\\' to reach a network destination. A route is administratively defined, or calculated/learned by a particular routing process. A ConcreteDependency associaton may be instantiated between a route and its routing service to indicate this. (In this scenario, the route is dependent on the service.)

</dd> <dt>

[**MSFT\_NetRoute**](msft-netroute.md)
</dt> <dd>

Represents the Route class in TCPIP WMIv2 provider.

</dd> <dt>

[**EapConfiguration**](eapconfiguration.md)
</dt> <dd>

The [**EapConfiguration**](eapconfiguration.md) class represents an Extensible Authentication Protocol (EAP) configuration object.

</dd> <dt>

[**MSFT\_NetRoute**](msft-netroute-vpnclientpsprovider.md)
</dt> <dd>

Represents a TCP/IP route.

</dd> <dt>

[**MSFT\_VpnConnection**](msft-vpnconnection.md)
</dt> <dd>

The [**MSFT\_VpnConnection**](msft-vpnconnection.md) class provides a method to configure a virtual private network (VPN) connection profile.

</dd> <dt>

[**PS\_EapConfiguration**](ps-eapconfiguration.md)
</dt> <dd>

The [**PS\_EapConfiguration**](ps-eapconfiguration.md) class provides methods to create new Extensible Authentication Protocol (EAP) configuration objects that use certain authentication protocols.

</dd> <dt>

[**PS\_VpnConnection**](ps-vpnconnection.md)
</dt> <dd>

The [**PS\_VpnConnection**](ps-vpnconnection.md) class contains the profile management functionality of the Get Connected wizard (GCW).

</dd> <dt>

[**PS\_VpnConnectionIPsecConfiguration**](ps-vpnconnectionipsecconfiguration.md)
</dt> <dd>

The [**PS\_VpnConnectionIPsecConfiguration**](ps-vpnconnectionipsecconfiguration.md) class can set or remove the IPsec custom policy configuration of a VPN connection profile.

</dd> <dt>

[**PS\_VpnConnectionProxy**](ps-vpnconnectionproxy.md)
</dt> <dd>

The [**PS\_VpnConnectionProxy**](ps-vpnconnectionproxy.md) class provides a method to modify the proxy configuration of a VPN profile.

</dd> <dt>

[**PS\_VpnConnectionRoute**](ps-vpnconnectionroute.md)
</dt> <dd>

The [**PS\_VpnConnectionRoute**](ps-vpnconnectionroute.md) class provides methods to add or remove routes to be plumbed for a VPN profile.

</dd> <dt>

[**PS\_VpnConnectionTrigger**](ps-vpnconnectiontrigger.md)
</dt> <dd>

The [**PS\_VpnConnectionTrigger**](ps-vpnconnectiontrigger.md) class has a method to retrieve the trigger properties of the VPN profile.

</dd> <dt>

[**PS\_VpnConnectionTriggerApplication**](ps-vpnconnectiontriggerapplication.md)
</dt> <dd>

The [**PS\_VpnConnectionTriggerApplication**](ps-vpnconnectiontriggerapplication.md) class provides methods to configure an application, which when launched will trigger a VPN connection.

</dd> <dt>

[**PS\_VpnConnectionTriggerDnsConfiguration**](ps-vpnconnectiontriggerdnsconfiguration.md)
</dt> <dd>

The [**PS\_VpnConnectionTriggerDnsConfiguration**](ps-vpnconnectiontriggerdnsconfiguration.md) class provides methods to manage the DNS trigger configuration of the VPN profile.

</dd> <dt>

[**PS\_VpnConnectionTriggerTrustedNetwork**](ps-vpnconnectiontriggertrustednetwork.md)
</dt> <dd>

The [**PS\_VpnConnectionTriggerTrustedNetwork**](ps-vpnconnectiontriggertrustednetwork.md) class provides methods to configure the trusted network configuration for VPN triggering.

</dd> <dt>

[**PS\_VpnServerAddress**](ps-vpnserveraddress.md)
</dt> <dd>

The [**PS\_VpnServerAddress**](ps-vpnserveraddress.md) class provides a method to create a new VPN Server address object.

</dd> <dt>

[**ThirdPartyVpnConnection**](thirdpartyvpnconnection.md)
</dt> <dd>

The [**ThirdPartyVpnConnection**](thirdpartyvpnconnection.md) class represents third party VPN profiles.

</dd> <dt>

[**VpnCommonConfig**](vpncommonconfig.md)
</dt> <dd>

The [**VpnCommonConfig**](vpncommonconfig.md) class represents the common attributes of the [**VpnConnection**](vpnconnection.md) and [**ThirdPartyVpnConnection**](thirdpartyvpnconnection.md) objects.

</dd> <dt>

[**VpnConnection**](vpnconnection.md)
</dt> <dd>

The [**VpnConnection**](vpnconnection.md) class represents the profile of a virtual private network (VPN) connection.

</dd> <dt>

[**VpnConnectionIPsecConfiguration**](vpnconnectionipsecconfiguration.md)
</dt> <dd>

The [**VpnConnectionIPsecConfiguration**](vpnconnectionipsecconfiguration.md) class represents the IPsec configuration for a VPN connection.

</dd> <dt>

[**VpnConnectionProxy**](vpnconnectionproxy.md)
</dt> <dd>

The [**VpnConnectionProxy**](vpnconnectionproxy.md) class represents the proxy settings for a VPN connection.

</dd> <dt>

[**VpnConnectionTrigger**](vpnconnectiontrigger.md)
</dt> <dd>

The [**VpnConnectionTrigger**](vpnconnectiontrigger.md) class represents the auto-trigger properties of a VPN connection.

</dd> <dt>

[**VpnConnectionTriggerApplication**](vpnconnectiontriggerapplication.md)
</dt> <dd>

The [**VpnConnectionTriggerApplication**](vpnconnectiontriggerapplication.md) class represents an application that auto-triggers a VPN connection.

</dd> <dt>

[**VpnConnectionTriggerDnsConfiguration**](vpnconnectiontriggerdnsconfiguration.md)
</dt> <dd>

The [**VpnConnectionTriggerDnsConfiguration**](vpnconnectiontriggerdnsconfiguration.md) class represents the DNS configuration for an auto-triggered VPN connection.

</dd> <dt>

[**VpnConnectionTriggerTrustedNetwork**](vpnconnectiontriggertrustednetwork.md)
</dt> <dd>

The [**VpnConnectionTriggerTrustedNetwork**](vpnconnectiontriggertrustednetwork.md) class represents the trusted network configuration for VPN triggering.

</dd> <dt>

[**VpnServerAddress**](vpnserveraddress.md)
</dt> <dd>

The [**VpnServerAddress**](vpnserveraddress.md) class represents a VPN server.

</dd> </dl>

 

 




