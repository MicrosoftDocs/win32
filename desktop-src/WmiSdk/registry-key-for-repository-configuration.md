---
description: Windows Management Instrumentation (WMI) has a new registry key to enable or disable the AutoRestore repository feature.
ms.assetid: 6c93fc40-b5d8-42da-9d02-7fa04fce3f65
ms.tgt_platform: multiple
title: Registry Key for Repository Configuration
ms.topic: article
ms.date: 05/31/2018
---

# Registry Key for Repository Configuration

Windows Management Instrumentation (WMI) has a new registry key to enable or disable the AutoRestore repository feature.. For more information on restoring the WMI repository, see [Backup or Restore WMI Repository](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc731460(v=ws.11)).

In Windows 7, the default behavior is to auto-restore a repository from a backed-up version if a repository corruption is detected. WMI provides the **AutoRestoreEnabled** registry value to disable this feature.

The registry keys for WMI are located in the registry at **HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**WBEM**\\**CIMOM**\\.

<dl> <dt>

<span id="AutoRestoreEnabled"></span><span id="autorestoreenabled"></span><span id="AUTORESTOREENABLED"></span>**AutoRestoreEnabled**
</dt> <dd>

Enables the user to determine whether or not to use the AutoRestore repository feature. By default this key is set to 1 and the AutoRestore Repository feature is enabled.

The following settings are possible:

<dl> <dt>

<span id="0"></span>0
</dt> <dd>

Disabled

</dd> <dt>

<span id="1"></span>1
</dt> <dd>

Enabled

</dd> </dl> </dd> </dl>

The **AutoRestoreEnabled** registry value can be modified by using the Group Policy Management Console (GPMC). For more information, see [Group Policy Management Console](/previous-versions/windows/desktop/gpmc/group-policy-management-console-portal).

This procedure provides details about how to enable or disable the AutoRestore repository feature:

**To change the default value of the **AutoRestoreEnabled** key by using Group Policy**

1.  Open the GPMC.
2.  Create a Group Policy object (GPO).
3.  Edit the GPO.
4.  Browse to Preferences/Windows Settings/Registry.
5.  Right-click and select **New... Registry**. This action presents a user interface where you can enter registry information.
6.  Select the **Update** command.
7.  Select the following registry key path: **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\WBEM\\CIMOM**.
8.  In the **name** field, enter **AutoRestoreEnabled**.
9.  In the **data** field, enter 0 to disable or 1 to enable the AutoRestore repository feature.
10. Click OK.

 

 
