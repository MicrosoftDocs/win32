---
description: A misconfigured firewall can cause WSD applications to fail.
ms.assetid: eba61235-29b4-463a-b7c5-d34d3b39b095
title: Inspecting Adapter and Firewall Settings
ms.topic: article
ms.date: 05/31/2018
---

# Inspecting Adapter and Firewall Settings

A misconfigured firewall can cause WSD applications to fail. This topic provides some troubleshooting procedures to use when WSD clients and hosts cannot see each other on the network. The firewall settings should be inspected before using any other application troubleshooting procedure.

**To inspect the adapter and firewall settings**

1.  Verify that the **Network Discovery** exception is enabled.
2.  Check that there are no application-specific firewall rules blocking the application.
3.  Explicitly enable the ports used for discovery and metadata exchange.
4.  Disable the firewall and retest the application.
    > [!Note]  
    > The firewall should be re-enabled after completing this step.

     

## Verifying that the Network Discovery exception is enabled

If any WS-Discovery applications are running, the **Network Discovery** firewall exception must be allowed.

**To enable the Network Discovery firewall exception**

1.  Click **Start**, click **Run**, and then type **firewall.cpl**. This opens the **Windows Firewall Control Panel** applet.
2.  Choose **Allow a program through Windows Firewall**.
3.  On the **Exceptions** tab, select the **Network Discovery** check box.
4.  Click **OK** to close the firewall applet.

Retest the program after making this firewall change. If the program now works successfully, the cause of the problem has been identified and no further troubleshooting steps are necessary. Otherwise, move on to the next step.

## Checking for application-specific firewall rules

Advanced configuration of the Windows Firewall can take place in a Microsoft Management Control (MMC) snap-in named **Windows Firewall with Advanced Security**. This snap-in can be used to troubleshoot suspected firewall problems.

Developers can use the [Windows Firewall with Advanced Security](/previous-versions/windows/desktop/ics/windows-firewall-with-advanced-security-reference) APIs to create firewall rules that apply to their WSD applications. Specifically, the [**Add**](/previous-versions/windows/desktop/api/netfw/nf-netfw-inetfwrules-add) method of the [**INetFwRules**](/previous-versions/windows/desktop/api/netfw/nn-netfw-inetfwrules) interface can be used to add a new firewall rule. If firewall rules are created incorrectly, clients and hosts may not be able to see each other on the network.

**To check for application-specific firewall rules**

1.  Click **Start**, click **Run**, and then type **wf.msc**.
2.  Look for application-specific rules that may be blocking traffic. For more information, see [Windows Firewall with Advanced Security - Diagnostics and Troubleshooting Tools](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc722062(v=ws.10)?ocid=fwlink).
3.  Remove application-specific rules.

If no application-specific rules were found, move on to the next step. If an application-specific rule was found and removed, retest the program after making the firewall change. If the program now works successfully, the cause of the problem has been identified and no further troubleshooting steps are necessary. Otherwise, move on to the next step.

## Enabling the ports used for discovery and metadata exchange

WS-Discovery uses the UDP port 3702 for message exchange. In addition, TCP ports 5357 and 5358 are sometimes used for metadata exchange. These ports can be explicitly opened on the firewall using the procedures described in "Open a port in Windows Firewall".

Retest the program after making this firewall change. If the program now works successfully, the cause of the problem has been identified and no further troubleshooting steps are necessary. Otherwise, move on to the next step.

## Disabling the firewall

The Windows Firewall can be disabled to help troubleshoot suspected problems. Other applicable firewalls (such as the firewall on a router) can also be disabled for troubleshooting purposes. For information about enabling and disabling the Windows Firewall, see [Turn Windows Firewall on or off](https://support.microsoft.com/en-us/windows/turn-microsoft-defender-firewall-on-or-off-ec0844f7-aebd-0583-67fe-601ecf5d774f).

Retest the application after disabling any applicable firewalls. If the program now works successfully, then the firewall was blocking the traffic. There are a few possible causes of blocked traffic.

-   Application-specific exceptions blocked the traffic. Check for application-specific firewall rules as described above.
-   The device took too long to respond to UDP requests. The Windows Firewall may block UDP responses that return more than 4 seconds after the initial request was sent. Continue troubleshooting by following the procedures given in [Using a Generic Host and Client for UDP WS-Discovery](using-a-generic-host-and-client-for-udp-ws-discovery.md) to see if the problem reproduces with a host that responds in less than 4 seconds.

If the application still fails after the firewall is disabled, then the firewall is not causing the application failure. Re-enable the firewalls and continue troubleshooting by following the procedures given in [Using a Generic Host and Client for UDP WS-Discovery](using-a-generic-host-and-client-for-udp-ws-discovery.md).

Firewalls should always be re-enabled after troubleshooting has finished.

## Related topics

<dl> <dt>

[WSDAPI Diagnostic Procedures](wsdapi-diagnostic-procedures.md)
</dt> <dt>

[Getting Started with WSDAPI Troubleshooting](getting-started-with-wsdapi-troubleshooting.md)
</dt> </dl>

 

 
