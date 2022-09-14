---
description: Lists the diagnostic procedures to use when troubleshooting the Add Printer Wizard.
ms.assetid: 3ffee09b-e980-4a14-97ad-270444457dd7
title: Troubleshooting the Add Printer Wizard
ms.topic: article
ms.date: 05/31/2018
---

# Troubleshooting the Add Printer Wizard

The Add Printer Wizard:

-   Always uses UDP WS-Discovery for device discovery
-   Always initiates a HTTP or HTTPS connection for metadata exchange
-   Sometimes uses directed discovery
-   Sometimes uses a secure channel (HTTPS) for metadata exchange

The following diagnostic procedures should be used (in order) to help identify problems with the Add Printer Wizard.

**To troubleshoot the Add Printer Wizard**

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
</dt> <dt>

[Troubleshooting Applications Using Directed Discovery](troubleshooting-applications-using-directed-discovery.md)
</dt> </dl>

 

 



