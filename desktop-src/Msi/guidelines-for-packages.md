---
description: Because User Account Control (UAC) in Windows Vista restricts privileges during an installation, developers of Windows Installer packages should not assume that their installation always has access to all parts of the system.
ms.assetid: 8e3b4ad8-b978-4e27-b060-1d023846718f
title: Guidelines for Packages
ms.topic: article
ms.date: 05/31/2018
---

# Guidelines for Packages

Because [*User Account Control*](u-gly.md) (UAC) in Windows Vista restricts privileges during an installation, developers of Windows Installer packages should not assume that their installation always has access to all parts of the system.

An installer package that can be successfully deployed to standard users via [Group Policy](/previous-versions/windows/desktop/Policy/group-policy-start-page) should in most cases also work with UAC in Windows Vista. Exceptions to this can occur if the [InstallUISequence table](installuisequence-table.md) contains the [LaunchConditions action](launchconditions-action.md) or the [LaunchCondition table](launchcondition-table.md) contains a condition based on the [Privileged property](privileged.md). Windows Installer package developers should therefore adhere to the following guidelines to ensure their package works with UAC and Windows Vista.

-   When including an [*installation context*](i-gly.md) condition with an action in the [InstallUISequence table](installuisequence-table.md), use a conditional statement based on the [Privileged property](privileged.md). Do not use a condition based on the [**AdminUser**](adminuser.md) property.
-   When including the installation context with the installation launch conditions, use a [Custom Action Type 19](custom-action-type-19.md) in the [InstallExecuteSequence table](installexecutesequence-table.md) and make the custom action conditional upon the [Privileged property](privileged.md). Do not use an action in the [LaunchCondition table](launchcondition-table.md) with a condition based on the [AdminUser property](adminuser.md) or Privileged property.
-   To read or modify the system configuration, use a [deferred execution custom action](deferred-execution-custom-actions.md) in the [InstallExecuteSequence table](installexecutesequence-table.md). Do not use immediate execution custom actions in the [InstallUISequence table](installuisequence-table.md) to modify the system configuration.
-   To modify parts of the system that are not user specific, use a deferred custom action in the [InstallExecuteSequence table](installexecutesequence-table.md). You should include the msidbCustomActionTypeNoImpersonate bit in the custom action type.
-   Omit Bit 3 from the value of the [**Word Count**](word-count-summary.md) Summary Property to indicate that the package can be required to be elevated. Do not include this bit unless elevated privileges are not required to install this package.
-   Include a manifest with the application's Requested Execution Level.
-   Include a certificate in the [MsiPatchCertificate](msipatchcertificate-table.md) table of original package and sign all patches with the same certificate.
-   If elevated privileges are required to install a Windows Installer package, the author of the package should include the [ElevationShield](elevationshield-attribute.md) attribute for the [PushButton control](pushbutton-control.md) used to start the installation. This will alert the user that clicking on the button will display the UAC dialog box requesting administrator authorization to continue the installation.
-   Set the [**MSIDEPLOYMENTCOMPLIANT**](msideploymentcompliant.md) property to 1 to indicate to the Windows Installer that the package has been authored and tested to comply with UAC in Windows Vista. If this property is not set, the installer determines whether the package complies with UAC.

Outside of [Group Policy](/previous-versions/windows/desktop/Policy/group-policy-start-page), the following check for UAC compliance can be used on Windows XP.

**To check for UAC compliance outside of Group Policy**

1.  Log on to the computer as an administrator.
2.  Advertise the package for a per-machine installation:

    **msiexec /jm** *package.msi*

3.  Log off the computer.
4.  Log on to the computer as a standard user.
5.  Attempt to install the advertised package:

    **msiexec /i** *package.msi*

6.  In most cases, if the installation is successful, the package is UAC compliant.
7.  Set the [**MSIDEPLOYMENTCOMPLIANT**](msideploymentcompliant.md) property in the package to 1.
8.  Test for correct installation of the package using Windows Vista.

 

 
