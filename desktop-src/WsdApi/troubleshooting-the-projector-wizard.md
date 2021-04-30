---
description: Lists the diagnostic procedures to use when troubleshooting the Projector Wizard.
ms.assetid: 54efc88c-0b8e-4652-8655-817a288863d1
title: Troubleshooting the Projector Wizard
ms.topic: article
ms.date: 05/31/2018
---

# Troubleshooting the Projector Wizard

The Projector Wizard:

-   Always uses UDP WS-Discovery for device discovery
-   Always uses HTTP for metadata exchange
-   Sometimes uses directed discovery

The following diagnostic procedures should be used (in order) to help identify problems with the Projector Wizard.

**To troubleshoot the Projector Wizard**

1.  If directed discovery is used, [troubleshoot directed discovery](troubleshooting-applications-using-directed-discovery.md).
2.  [Inspect adapter and firewall settings](inspecting-adapter-and-firewall-settings.md).
3.  [Use a generic host and client for UDP WS-Discovery](using-a-generic-host-and-client-for-udp-ws-discovery.md).
4.  [Use WSD Debug Client to verify multicast traffic](using-wsddebug-client-to-verify-multicast-traffic.md).
5.  [Inspect network traces for UDP WS-Discovery](inspecting-network-traces-for-udp-ws-discovery.md).
6.  [Use a generic host and client for HTTP metadata exchange](using-a-generic-host-and-client-for-http-metadata-exchange.md).
7.  [Use WinHTTP logging to verify Get traffic](using-winhttp-logging-to-verify-get-traffic.md).
8.  [Inspect network traces for HTTP metadata exchange](inspecting-network-traces-for-http-metadata-exchange.md).

If the source of the problem cannot be identified using the above diagnostic procedures, follow the directions in [Enabling WSDAPI Tracing](enabling-wsdapi-tracing.md) and contact Microsoft support.

## Related topics

<dl> <dt>

[Getting Started with WSDAPI Troubleshooting](getting-started-with-wsdapi-troubleshooting.md)
</dt> </dl>

 

 



