---
description: An administrator can use the following methods to enable a non-administrator user to install an application with elevated system privileges.
ms.assetid: 61b9297e-f45e-4f50-9001-9bae580e1bf4
title: Installing a Package with Elevated Privileges for a Non-Admin
ms.topic: article
ms.date: 05/31/2018
---

# Installing a Package with Elevated Privileges for a Non-Admin

An administrator can use the following methods to enable a non-administrator user to install an application with elevated system privileges.

-   In Windows Vista with Windows Installer, a member of the Administrators group can provide authorization for a non-administrator to elevate the installation through [*User Account Control*](u-gly.md) (UAC) as described in [Using Windows Installer with UAC](using-windows-installer-with-uac.md).

    **Windows Vista:** Required.

The following methods can also be used to install an application with elevated system privileges.

-   An administrator can advertise an application on a user's computer by assigning or publishing the Windows Installer package using application deployment and [Group Policy](/previous-versions/windows/desktop/Policy/group-policy-start-page). The administrator advertises the package for per-machine installation. If a non-administrator user then installs the application, the installation can run with elevated privileges. Non-administrator users cannot install unadvertised packages that require elevated system privileges.
-   An administrator can go to the user's computer and [advertise](advertisement.md) the application for per-machine installation. Because the Windows Installer always has elevated privileges while doing installs in the per-machine [installation context](installation-context.md), if a non-administrator user then installs the advertised application, the installation can run with elevated privileges. Non-administrator users still cannot install unadvertised packages that require elevated privileges.
-   A non-privileged user can install an advertised application that requires elevated privileges if a local system agent advertises the application. The application can be advertised for a per-user or per-machine installation. An application installed using this method is considered managed. For more information, see [Advertising a Per-User Application To Be Installed with Elevated Privileges](advertising-a-per-user-application-to-be-installed-with-elevated-privileges.md).
-   An administrator can set the [AlwaysInstallElevated](alwaysinstallelevated.md) policy for both per-user and per-machine installations. This method can open a computer to a security risk, because when this policy is set, a non-administrator user can run installations with elevated privileges and access secure locations on the computer, such as the SystemFolder or the **HKLM** registry key.

    If the application is installed per-machine while the [AlwaysInstallElevated](alwaysinstallelevated.md) policy is set, the product is treated as managed. In this case, the application can still perform a repair with elevated privileges if the policy is removed. Also, if the application is installed per-user while the AlwaysInstallElevated policy is set, the application is unable to perform a repair if the policy is removed.

-   An administrator can go to a user's computer and do a per-machine installation of the application. Because privileges are required to perform this type of installation, per-machine installations are always managed.

## Related topics

<dl> <dt>

[Installation Context](installation-context.md)
</dt> </dl>

 

 
