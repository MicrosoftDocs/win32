---
title: Working with per-interface APIs
description: Working with per-interface APIs
ms.assetid: '91b01a8a-ab8b-40bb-a4ef-c0f36a90f170'
keywords: ["Windows Firewall", "using"]
---

# Working with per-interface APIs

The per-interface firewall APIs that are part of the Internet Connection Firewall (ICF) API set, implemented earlier in this product's history, will not be supported in future versions of the operating system. It is therefore recommended that the new Windows Firewall APIs be used.

The following tasks, using the older ICF architecture, can be accomplished using these APIs.



| Task                                                                          | ICF API                                                                                                                |
|-------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Checking whether the firewall is enabled or disabled on a network connection. | [**INetSharingConfiguration::get\_InternetFirewallEnabled**](inetsharingconfiguration-get-internetfirewallenabled.md) |
| Enumerating the open ports on an interface.                                   | [**INetSharingConfiguration::get\_EnumPortMappings**](inetsharingconfiguration-enumportmappings.md)                   |
| Checking if a particular port is open on an interface.                        | [**INetSharingPortMappingProps::get\_Enabled**](inetsharingportmappingprops-get-enabled.md)                           |
| Opening a port on a network connection.                                       | [**INetSharingConfiguration::AddPortMapping**](inetsharingconfiguration-addportmapping.md)                            |



 

**Note**  In a change from Windows XP and Windows XP with Service Pack 1 (SP1), calling an API to open a port or enable or disable the firewall on an interface no longer requires user confirmation, so no dialog is displayed as a result of calling one of these APIs.

 

 




