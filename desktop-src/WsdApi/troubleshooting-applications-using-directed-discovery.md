---
description: Applications that use directed discovery send Probe messages over HTTP or HTTPS to discover devices.
ms.assetid: 599f5962-da91-4688-b333-a784f06581ed
title: Troubleshooting WSDAPI Applications Using Directed Discovery
ms.topic: article
ms.date: 05/31/2018
---

# Troubleshooting WSDAPI Applications Using Directed Discovery

Applications that use directed discovery send [Probe](probe-message.md) messages over HTTP or HTTPS to discover devices. The corresponding [ProbeMatches](probematches-message.md) messages sent in response are also sent over HTTP or HTTPS. Directed discovery can be initiated by the Add Printer Wizard, a Function Discovery client, or a WSDAPI application. The Probe and ProbeMatches messages are structurally identical to those sent over UDP. The messages are prefixed with the appropriate HTTP or HTTPS headers.

The following diagnostic procedures should be used (in order) to help identify problems with an application using directed discovery.

**To troubleshoot a WSDAPI application using directed discovery**

1.  [Inspect adapter and firewall settings](inspecting-adapter-and-firewall-settings.md).
2.  [Use a generic host and client for HTTP metadata exchange](using-a-generic-host-and-client-for-http-metadata-exchange.md).
3.  [Use WinHTTP logging to verify Get traffic](using-winhttp-logging-to-verify-get-traffic.md).
4.  [Inspect network traces for an application using directed discovery](inspecting-network-traces-for-applications-using-directed-discovery.md).

If the source of the problem cannot be identified using the above diagnostic procedures, follow the directions in [Enabling WSDAPI Tracing](enabling-wsdapi-tracing.md) and contact Microsoft support.

## Related topics

<dl> <dt>

[Getting Started with WSDAPI Troubleshooting](getting-started-with-wsdapi-troubleshooting.md)
</dt> <dt>

[Troubleshooting the Add Printer Wizard](troubleshooting-the-add-printer-wizard.md)
</dt> <dt>

[Troubleshooting WSDAPI Applications](troubleshooting-wsdapi-applications.md)
</dt> </dl>

 

 



