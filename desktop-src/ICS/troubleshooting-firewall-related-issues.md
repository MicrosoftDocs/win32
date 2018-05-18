---
title: Troubleshooting Firewall-Related Issues
description: Pfirewall.log contains a log of all the dropped and allowed firewall connections.
ms.assetid: 'd7373e5c-bcbd-423a-9e9f-cdbf481b9a78'
---

# Troubleshooting Firewall-Related Issues

Pfirewall.log contains a log of all the dropped and allowed firewall connections.

The default log path is C:\\Windows\\system32\\LogFiles\\Firewall\\pfirewall.log

## Generating a Firewall Packet Log

You can enable packet logging on all profiles by using the following netshell commands:

"netsh advfirewall&gt;set allprofiles logging allowedconnections enable"

"netsh advfirewall&gt;set allprofiles logging droppedconnections enable"

## Diagnosing the Windows Filtering Platform Behavior

The Windows Firewall is layered on top of WFP which provides the actual enforcement of the firewall rules through traffic filters derived from the firewall policy. The following steps will let you trace in the event viewer what happened in WFP while you reproduce the problem that you want to debug.

To enable WFP auditing:

auditpol /set /subcategory:"Filtering Platform Packet Drop" /success:enable /failure:enable

auditpol /set /subcategory:"Filtering Platform Connection" /success:enable /failure:enable

auditpol /set /subcategory:"IPsec Driver" /success:enable /failure:enable

auditpol /set /subcategory:"IPsec Main Mode" /success:enable /failure:enable

auditpol /set /subcategory:"IPsec Quick Mode" /success:enable /failure:enable

auditpol /set /subcategory:"IPsec Extended Mode" /success:enable /failure:enable

Repro the failure

To disable WFP auditing:

auditpol /set /subcategory:"Filtering Platform Packet Drop" /success:disable /failure:disable

auditpol /set /subcategory:"Filtering Platform Connection" /success: disable /failure:disable

auditpol /set /subcategory:"IPsec Driver" /success:disable /failure:disable

auditpol /set /subcategory:"IPsec Main Mode" /success:disable /failure:disable

auditpol /set /subcategory:"IPsec Quick Mode" /success:disable /failure:disable

auditpol /set /subcategory:"IPsec Extended Mode" /success:disable /failure:disable

 

 




