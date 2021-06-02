---
description: Administrator Overrides
ms.assetid: 25b6ce86-52c8-4f7f-97af-86b2eaf3e9af
title: Administrator Overrides
ms.topic: article
ms.date: 05/31/2018
---

# Administrator Overrides

Windows has a single default access control list (ACL) on all power policy objects. The ACL grants read, write, and change permissions to members of the Authenticated Users group. All other users are granted read-only permission. Applications that call power policy functions can determine whether a user has permissions for a specified power setting by using the [**PowerSettingAccessCheck**](/windows/desktop/api/PowrProf/nf-powrprof-powersettingaccesscheck) function.

Power settings may be overridden via Group Policy. Overrides can be set through domain group policy or local group policy. [**PowerSettingAccessCheck**](/windows/desktop/api/PowrProf/nf-powrprof-powersettingaccesscheck) will report if a specified power setting has a group policy override.

The command line tool **PowerCfg.exe** displays an error message when a command cannot be completed either because the user did not have permissions to change the power setting or because the power setting has a group policy override.

The Power Options application in Control Panel does not provide support for configuring power policy access permissions. Changing permissions must be done via **PowerCfg.exe**.

 

 



