---
description: In certain cases, a user that is not a system administrator can only override an approved list of restricted Windows Installer public properties.
ms.assetid: e16e8187-75b6-4104-a53c-928a56fcee6b
title: Restricted Public Properties
ms.topic: article
ms.date: 05/31/2018
---

# Restricted Public Properties

In the case of a managed installation, the package author may need to limit which [public properties](public-properties.md) are passed to the server side and can be changed by a user that is not a system administrator. Some restrictions are commonly necessary to maintain a secure environment when the installation requires the installer to use elevated privileges. If all of the following conditions are met, a user that is not a system administrator can only override an approved list of restricted public properties:

-   The system is Windows 2000.
-   The user is not a system administrator.
-   The application or product is being installed with elevated privileges.

If all of the above conditions are true, the installer defaults to the following list of restricted public properties that can be changed by any user:

-   [**ACTION**](action.md)
-   [**AFTERREBOOT**](afterreboot.md)
-   [**ALLUSERS**](allusers.md)
-   [**EXECUTEACTION**](executeaction.md)
-   [**EXECUTEMODE**](executemode.md)
-   [**FILEADDDEFAULT**](fileadddefault.md)
-   [**FILEADDLOCAL**](fileaddlocal.md)
-   [**FILEADDSOURCE**](fileaddsource.md)
-   [**INSTALLLEVEL**](installlevel.md)
-   [**LIMITUI**](limitui.md)
-   [**LOGACTION**](logaction.md)
-   [**NOCOMPANYNAME**](nocompanyname.md)
-   [**NOUSERNAME**](nousername.md)
-   [**MSIENFORCEUPGRADECOMPONENTRULES**](msienforceupgradecomponentrules.md)
-   [**MSIINSTANCEGUID**](msiinstanceguid.md)
-   [**MSINEWINSTANCE**](msinewinstance.md)
-   [**MSIPATCHREMOVE**](msipatchremove.md)
-   [**PATCH**](patch.md)
-   [**PRIMARYFOLDER**](primaryfolder.md)
-   [**PROMPTROLLBACKCOST**](promptrollbackcost.md)
-   [**REBOOT**](reboot.md)
-   [**REINSTALL**](reinstall.md)
-   [**REINSTALLMODE**](reinstallmode.md)
-   [**RESUME**](resume.md)
-   [**SEQUENCE**](sequence.md)
-   [**SHORTFILENAMES**](shortfilenames.md)
-   [**TRANSFORMS**](transforms.md)
-   [**TRANSFORMSATSOURCE**](transformsatsource.md)

The author of an installation package can extend this default list to include additional public properties by using the [**SecureCustomProperties**](securecustomproperties.md) property.

Setting the [**EnableUserControl**](-enableusercontrol.md) property or the [EnableUserControl](enableusercontrol.md)[system policy](system-policy.md) extends the list to all public properties. All users can then change any public property.

The installer sets the [**RestrictedUserControl**](restrictedusercontrol.md) property whenever the list of public properties passed to the server by non-administrator users is restricted.

## Related topics

<dl> <dt>

[About Properties](about-properties.md)
</dt> </dl>

 

 



