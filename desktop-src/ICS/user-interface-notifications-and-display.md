---
title: User Interface Notifications and Display
description: If the user interface for the feature shows the state of the firewall rules, it should use the INetFwPolicy2 get\_IsRuleGroupCurrentlyEnabled method, which provides a Boolean response regardless of whether the firewall rule group is enabled locally or by a domain administrator through Group Policy.
ms.assetid: 62893cde-8605-4efa-a2e8-c9c0a6e5ce57
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# User Interface Notifications and Display

If the user interface for the feature shows the state of the firewall rules, it should use the [**INetFwPolicy2::get\_IsRuleGroupCurrentlyEnabled**](/windows/previous-versions/Netfw/nf-netfw-inetfwpolicy2-get_isrulegroupcurrentlyenabled?branch=master) method, which provides a Boolean response regardless of whether the firewall rule group is enabled locally or by a domain administrator through Group Policy.

It may be prudent to check whether modifying the local policy will have any impact on the resultant policy. The firewall "shields-up" feature or the domain administrator may be disallowing local policy exceptions, in which case any API calls would be fruitless. The [**INetFwPolicy2::get\_LocalPolicyModifyState**](/windows/previous-versions/Netfw/?branch=master) method indicates whether local policy changes will take effect. If they do not, the API provides a return code to indicate why the changes will not take effect. This provides application developers with sufficient information to assist the user with correcting the problem.

 

 




