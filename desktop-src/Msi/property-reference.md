---
description: 'This section lists the properties defined by Windows Installer:'
ms.assetid: c91119b9-59d5-4a33-91cd-d3ba63659d12
title: Property Reference
ms.topic: article
ms.date: 05/31/2018
---

# Property Reference

This section lists the properties defined by Windows Installer:

-   [Component Location Properties](#component-location-properties)
-   [Configuration Properties](#configuration-properties)
-   [Date, Time Properties](#date-time-properties)
-   [Feature Installation Options Properties](#feature-installation-options-properties)
-   [Hardware Properties](#hardware-properties)
-   [Installation Status Properties](#installation-status-properties)
-   [Operating System Properties](#operating-system-properties)
-   [Product Information Properties](#product-information-properties)
-   [Summary Information Update Properties](#summary-information-update-properties)
-   [System Folder Properties](#system-folder-properties)
-   [User Information Properties](#user-information-properties)

Additional properties can be specified by authored data or custom actions. Properties with names containing no lowercase letters are public properties and can be specified on the command line.

For information about values of the **Uninstall** registry key that are provided by installer properties, see [Uninstall Registry Key](uninstall-registry-key.md).

## Component Location Properties

The following list provides links to more information about the component location properties.



| Property                                                            | Description                                                                                                                                                                                                        |
|---------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**OriginalDatabase**](originaldatabase.md)<br/>             | The installer sets this property to the launched-from database, the database on the source, or the cached database.<br/>                                                                                     |
| [**ParentOriginalDatabase**](parentoriginaldatabase.md)<br/> | The installer sets this property for installations run by a [Concurrent Installation](concurrent-installations.md) action.<br/>                                                                             |
| [**SourceDir**](sourcedir.md)<br/>                           | Root directory that contains the source files.<br/>                                                                                                                                                          |
| [**TARGETDIR**](targetdir.md)<br/>                           | Specifies the root destination directory for the installation. During an [administrative installation](administrative-installation.md) this property is the location to copy the installation package.<br/> |



 

## Configuration Properties

The following list provides links to more information about other configurable properties.



| Property                                                                                | Description                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ACTION**](action.md)<br/>                                                     | Initial action called after the installer is initialized.<br/>                                                                                                                                                                                                                                                                                                                          |
| [**ALLUSERS**](allusers.md)<br/>                                                 | Determines where configuration information is stored.<br/>                                                                                                                                                                                                                                                                                                                              |
| [**ARPAUTHORIZEDCDFPREFIX**](arpauthorizedcdfprefix.md)<br/>                     | URL of the update channel for an application.<br/>                                                                                                                                                                                                                                                                                                                                      |
| [**ARPCOMMENTS**](arpcomments.md)<br/>                                           | Provides Comments for the **Add or Remove Programs** in **Control Panel**.<br/>                                                                                                                                                                                                                                                                                                         |
| [**ARPCONTACT**](arpcontact.md)<br/>                                             | Provides Contact for the **Add or Remove Programs** in **Control Panel**.<br/>                                                                                                                                                                                                                                                                                                          |
| [**ARPINSTALLLOCATION**](arpinstalllocation.md)<br/>                             | Fully qualified path to the primary folder of an application.<br/>                                                                                                                                                                                                                                                                                                                      |
| [**ARPNOMODIFY**](arpnomodify.md)<br/>                                           | Disables functionality that modifies a product.<br/>                                                                                                                                                                                                                                                                                                                                    |
| [**ARPNOREMOVE**](arpnoremove.md)<br/>                                           | Disables functionality that removes a product.<br/>                                                                                                                                                                                                                                                                                                                                     |
| [**ARPNOREPAIR**](arpnorepair.md)<br/>                                           | Disables the **Repair** button in the Programs wizard.<br/>                                                                                                                                                                                                                                                                                                                             |
| [**ARPPRODUCTICON**](arpproducticon.md)<br/>                                     | Specifies the primary icon for the installation package.<br/>                                                                                                                                                                                                                                                                                                                           |
| [**ARPREADME**](arpreadme.md)<br/>                                               | Provides a **ReadMe** for the **Add or Remove Programs** in **Control Panel**.<br/>                                                                                                                                                                                                                                                                                                     |
| [**ARPSIZE**](arpsize.md)<br/>                                                   | Estimated size of an application in kilobytes.<br/>                                                                                                                                                                                                                                                                                                                                     |
| [**ARPSYSTEMCOMPONENT**](arpsystemcomponent.md)<br/>                             | Prevents display of an application in the **Add or Remove Programs** list.<br/>                                                                                                                                                                                                                                                                                                         |
| [**ARPURLINFOABOUT**](arpurlinfoabout.md)<br/>                                   | URL for the home page of an application.<br/>                                                                                                                                                                                                                                                                                                                                           |
| [**ARPURLUPDATEINFO**](arpurlupdateinfo.md)<br/>                                 | URL for application update information.<br/>                                                                                                                                                                                                                                                                                                                                            |
| [**AVAILABLEFREEREG**](availablefreereg.md)<br/>                                 | Registry space (in kilobytes) that an application requires. Used by [AllocateRegistrySpace action](allocateregistryspace-action.md).<br/>                                                                                                                                                                                                                                              |
| [**CCP\_DRIVE**](ccp-drive.md)<br/>                                              | The root path for qualifying products for CCP.<br/>                                                                                                                                                                                                                                                                                                                                     |
| [**DefaultUIFont**](defaultuifont.md)<br/>                                       | Default font style used for controls.<br/>                                                                                                                                                                                                                                                                                                                                              |
| [**DISABLEADVTSHORTCUTS**](disableadvtshortcuts.md)<br/>                         | Set to disable the generation the specific shortcuts that support [installation-on-demand](installation-on-demand.md).<br/>                                                                                                                                                                                                                                                            |
| [**DISABLEMEDIA**](-disablemedia.md)<br/>                                        | Prevents the installer from registering media sources, such as a CD-ROMs, as valid sources for the product.<br/>                                                                                                                                                                                                                                                                        |
| [**DISABLEROLLBACK**](-disablerollback.md)<br/>                                  | Disables rollback for the current configuration.<br/>                                                                                                                                                                                                                                                                                                                                   |
| [**EXECUTEACTION**](executeaction.md)<br/>                                       | Top-level action that ExecuteAction initiates.<br/>                                                                                                                                                                                                                                                                                                                                     |
| [**EXECUTEMODE**](executemode.md)<br/>                                           | Mode of execution that the installer performs.<br/>                                                                                                                                                                                                                                                                                                                                     |
| [**FASTOEM**](fastoem.md)<br/>                                                   | Improves installation performance under specific OEM scenarios.<br/>                                                                                                                                                                                                                                                                                                                    |
| [**INSTALLLEVEL**](installlevel.md)<br/>                                         | Initial level where features are installed.<br/>                                                                                                                                                                                                                                                                                                                                        |
| [**LIMITUI**](limitui.md)<br/>                                                   | UI level capped as Basic.<br/>                                                                                                                                                                                                                                                                                                                                                          |
| [**LOGACTION**](logaction.md)<br/>                                               | List of action names to be logged.<br/>                                                                                                                                                                                                                                                                                                                                                 |
| [**MEDIAPACKAGEPATH**](mediapackagepath.md)<br/>                                 | This property must be set to the relative path if the installation package is not located at the root of the CD-ROM.<br/>                                                                                                                                                                                                                                                               |
| [**MSIARPSETTINGSIDENTIFIER**](msiarpsettingsidentifier.md)<br/>                 | This optional property contains a semi-colon delimited list of the registry locations where the application stores a user's settings and preferences. Available with Windows Installer 4.0.<br/>                                                                                                                                                                                        |
| [**MSIDISABLEEEUI**](msidisableeeui.md)<br/>                                     | Disable the embedded user interface for the installation.<br/> **[Windows Installer 4.0 and earlier](not-supported-in-windows-installer-4-0.md):** Not supported.<br/>                                                                                                                                                                                                           |
| [**MSIFASTINSTALL**](msifastinstall.md)<br/>                                     | Reduce the time required to install a large Windows Installer package.<br/> **[Windows Installer 4.5 and earlier](not-supported-in-windows-installer-4-5.md):** Not supported.<br/>                                                                                                                                                                                              |
| [**MSIINSTALLPERUSER**](msiinstallperuser.md)<br/>                               | Requests that the Windows Installer install the package only for the current user.<br/> **[Windows Installer 4.5 and earlier](not-supported-in-windows-installer-4-5.md):** Not supported.<br/>                                                                                                                                                                                  |
| [**MSINODISABLEMEDIA**](msinodisablemedia.md)<br/>                               | Set this property to prevent the installer from setting the [**DISABLEMEDIA**](-disablemedia.md) property.<br/>                                                                                                                                                                                                                                                                        |
| [**MSIENFORCEUPGRADECOMPONENTRULES**](msienforceupgradecomponentrules.md)<br/>   | Set this property to 1 (one) on the command line or in the [Property Table](property-table.md) to apply the upgrade component rules during [small updates](small-updates.md) and [minor upgrades](minor-upgrades.md) of a specific product. Available beginning with Windows Installer 3.0.<br/>                                                                                     |
| [**MSIUNINSTALLSUPERSEDEDCOMPONENTS**](msiuninstallsupersededcomponents.md)<br/> | When this property has been set to 1, the installer can unregister and uninstall redundant components to prevent leaving behind orphan components on the computer.<br/> **[Windows Installer 4.0 and earlier](not-supported-in-windows-installer-4-0.md):** Not supported.<br/>                                                                                                  |
| [**PRIMARYFOLDER**](primaryfolder.md)<br/>                                       | Allows the author to designate a primary folder for an installation. Used to determine the values for the [**PrimaryVolumePath**](primaryvolumepath.md), [**PrimaryVolumeSpaceAvailable**](primaryvolumespaceavailable.md), [**PrimaryVolumeSpaceRequired**](primaryvolumespacerequired.md), and [**PrimaryVolumeSpaceRemaining**](primaryvolumespaceremaining.md) properties.<br/> |
| [**Privileged**](privileged.md)<br/>                                             | Runs an installation with elevated privileges.<br/>                                                                                                                                                                                                                                                                                                                                     |
| [**PROMPTROLLBACKCOST**](promptrollbackcost.md)<br/>                             | Action if there is insufficient disk space for the installation.<br/>                                                                                                                                                                                                                                                                                                                   |
| [**REBOOT**](reboot.md)<br/>                                                     | Forces or suppresses a restart.<br/>                                                                                                                                                                                                                                                                                                                                                    |
| [**REBOOTPROMPT**](rebootprompt.md)<br/>                                         | Suppresses the display of prompts for restarts to the user. Any restarts that are needed happen automatically.<br/>                                                                                                                                                                                                                                                                     |
| [**ROOTDRIVE**](rootdrive.md)<br/>                                               | Default drive for an installation.<br/>                                                                                                                                                                                                                                                                                                                                                 |
| [**SEQUENCE**](sequence.md)<br/>                                                 | A table that has the sequence table schema.<br/>                                                                                                                                                                                                                                                                                                                                        |
| [**SHORTFILENAMES**](shortfilenames.md)<br/>                                     | Causes short file names to be used.<br/>                                                                                                                                                                                                                                                                                                                                                |
| [**TRANSFORMS**](transforms.md)<br/>                                             | List of transforms to be applied to a database.<br/>                                                                                                                                                                                                                                                                                                                                    |
| [**TRANSFORMSATSOURCE**](transformsatsource.md)<br/>                             | Informs the installer that the transforms for a product reside at the source.<br/>                                                                                                                                                                                                                                                                                                      |
| [**TRANSFORMSSECURE**](transformssecure.md)<br/>                                 | Setting the [**TRANSFORMSECURE**](transformssecure.md) property to 1 (one) informs the installer that transforms are to be cached locally on the user computer in a location where the user does not have write access.<br/>                                                                                                                                                           |
| [**MsiLogFileLocation**](msilogfilelocation.md)<br/>                             | The installer sets the value of this property to the full path of the log file, when logging has been enabled. This property is available starting with Windows Installer 4.0.<br/>                                                                                                                                                                                                     |
| [**MsiLogging**](msilogging.md)<br/>                                             | Sets the default logging mode for the Windows Installer package. This property is available starting with Windows Installer 4.0.<br/>                                                                                                                                                                                                                                                   |
| [**MSIUSEREALADMINDETECTION**](msiuserealadmindetection.md)<br/>                 | Set this property to 1 to request that the installer use actual user information when setting the [**AdminUser**](adminuser.md) property. This property is available starting with Windows Installer 4.0.<br/>                                                                                                                                                                         |



 

## Date, Time Properties

The [**Date**](date.md) and [**Time**](time.md) properties are live properties that the installer sets when data is extracted.



| Property                        | Description                  |
|---------------------------------|------------------------------|
| [**Date**](date.md)<br/> | The current date.<br/> |
| [**Time**](time.md)<br/> | The current time.<br/> |



 

## Feature Installation Options Properties

The following list provides links to more information about the feature installation options properties.



| Property                                                                | Description                                                                                                                                                                       |
|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ADDDEFAULT**](adddefault.md)<br/>                             | List of features to be installed in the default configuration.<br/>                                                                                                         |
| [**ADDLOCAL**](addlocal.md)<br/>                                 | List of features to be installed locally.<br/>                                                                                                                              |
| [**ADDSOURCE**](addsource.md)<br/>                               | List of features to be run from source.<br/>                                                                                                                                |
| [**ADVERTISE**](advertise.md)<br/>                               | List of features to be advertised.<br/>                                                                                                                                     |
| [**COMPADDDEFAULT**](compadddefault.md)<br/>                     | List of components to be installed in the default configuration.<br/>                                                                                                       |
| [**COMPADDLOCAL**](compaddlocal.md)<br/>                         | List of component IDs to be installed locally.<br/>                                                                                                                         |
| [**COMPADDSOURCE**](compaddsource.md)<br/>                       | List of component IDs to run from source media.<br/>                                                                                                                        |
| [**FILEADDDEFAULT**](fileadddefault.md)<br/>                     | List of file keys for files to be installed in the default configuration.<br/>                                                                                              |
| [**FILEADDLOCAL**](fileaddlocal.md)<br/>                         | List of file keys for files to be run locally.<br/>                                                                                                                         |
| [**FILEADDSOURCE**](fileaddsource.md)<br/>                       | List of file keys to be run from the source media.<br/>                                                                                                                     |
| [**MSIDISABLELUAPATCHING**](msidisableluapatching.md)<br/>       | Setting this property prevents Least Privileged User (LUA) patching of an application.<br/>                                                                                 |
| [**MsiPatchRemovalList**](msipatchremovallist.md)<br/>           | List of patches to be removed during the installation.<br/>                                                                                                                 |
| [**MSIRESTARTMANAGERCONTROL**](msirestartmanagercontrol.md)<br/> | Specifies whether the package uses the [Restart Manager](../rstmgr/restart-manager-portal.md) or [FilesInUse](filesinuse-dialog.md) functionality.<br/>                                          |
| [**MSIDISABLERMRESTART**](msidisablermrestart.md)<br/>           | Specifies how applications or services that are currently using files affected by an update should be shutdown and restarted to enable the installation of the update.<br/> |
| [**MSIRMSHUTDOWN**](msirmshutdown.md)<br/>                       | Specifies how applications or services that are currently using files affected by an update should be shutdown to enable the installation of the update.<br/>               |
| [**MSIPATCHREMOVE**](msipatchremove.md)<br/>                     | Setting this property removes patches.<br/>                                                                                                                                 |
| [**PATCH**](patch.md)<br/>                                       | Setting this property applies a patch.<br/>                                                                                                                                 |
| [**REINSTALL**](reinstall.md)<br/>                               | List of features to be reinstalled.<br/>                                                                                                                                    |
| [**REINSTALLMODE**](reinstallmode.md)<br/>                       | A string that contains letters that specify the type of reinstall to perform.<br/>                                                                                          |
| [**REMOVE**](remove.md)<br/>                                     | List of features to be removed.<br/>                                                                                                                                        |



 

## Hardware Properties

The following list identifies the hardware properties that the Windows Installer sets at startup.




| Property | Description | 
|----------|-------------|
| <a href="alpha.md"><strong>Alpha</strong></a><br /> | The numeric processor level when running on an Alpha processor.<br /><blockquote>[!Note]<br />This property is obsolete, the Alpha platform is not supported by Windows Installer.</blockquote><br /> | 
| <a href="borderside.md"><strong>BorderSide</strong></a><br /> | The width of the window borders, in pixels.<br /> | 
| <a href="bordertop.md"><strong>BorderTop</strong></a><br /> | The height of the window borders, in pixels.<br /> | 
| <a href="captionheight.md"><strong>CaptionHeight</strong></a><br /> | The height of normal caption area, in pixels.<br /> | 
| <a href="colorbits.md"><strong>ColorBits</strong></a><br /> | The number of adjacent color bits for each pixel.<br /> | 
| <a href="intel.md"><strong>Intel</strong></a><br /> | The numeric processor level when running on an Intel processor.<br /> | 
| <a href="intel64.md"><strong>Intel64</strong></a><br /> | The numeric processor level when running on an Itanium processor.<br /> | 
| <a href="msix64.md"><strong>Msix64</strong></a><br /> | The numeric processor level when running on an x64 processor.<br /> | 
| <a href="physicalmemory.md"><strong>PhysicalMemory</strong></a><br /> | The size of the installed RAM, in megabytes.<br /> | 
| <a href="screenx.md"><strong>ScreenX</strong></a><br /> | The width of the screen, in pixels.<br /> | 
| <a href="screeny.md"><strong>ScreenY</strong></a><br /> | The height of the screen, in pixels.<br /> | 
| <a href="textheight.md"><strong>TextHeight</strong></a><br /> | The height of characters, in logical units.<br /> | 
| <a href="virtualmemory.md"><strong>VirtualMemory</strong></a><br /> | The amount of available page file space, in megabytes.<br /> | 




 

## Installation Status Properties

The following list provides links to more information about status properties that are updated by the installer during installation.



| Property                                                                      | Description                                                                                                                                                                                                                                                              |
|-------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AFTERREBOOT**](afterreboot.md)<br/>                                 | Indicates current installation follows a reboot that the [ForceReboot action](forcereboot-action.md) invokes.<br/>                                                                                                                                                |
| [**CostingComplete**](costingcomplete.md)<br/>                         | Indicates whether disk space costing is complete.<br/>                                                                                                                                                                                                             |
| [**Installed**](installed.md)<br/>                                     | Indicates that a product is already installed.<br/>                                                                                                                                                                                                                |
| [**MSICHECKCRCS**](msicheckcrcs.md)<br/>                               | The Installer does a CRC on files only if the [**MSICHECKCRCS**](msicheckcrcs.md) property is set.<br/>                                                                                                                                                           |
| [**MsiRestartManagerSessionKey**](msirestartmanagersessionkey.md)<br/> | The Installer sets this property to the session key for the [Restart Manager](../rstmgr/restart-manager-portal.md) session.<br/>                                                                                                                                                         |
| [**MsiRunningElevated**](msirunningelevated-.md)<br/>                  | The Installer sets the value of this property to 1 when the installer is running with [*elevated*](e-gly.md) privileges.<br/>                                                                                                                   |
| [**MsiSystemRebootPending**](msisystemrebootpending.md)<br/>           | The Installer sets this property to 1 if a restart of the operating system is currently pending.<br/>                                                                                                                                                              |
| [**MsiUIHideCancel**](msiuihidecancel.md)<br/>                         | The Installer sets [**MsiUIHideCancel**](msiuihidecancel.md) to 1 when the internal install level includes **INSTALLUILEVEL\_HIDECANCEL**.<br/>                                                                                                                   |
| [**MsiUIProgressOnly**](msiuiprogressonly.md)<br/>                     | The Installer sets [**MsiUIProgressOnly**](msiuiprogressonly.md) to 1 when the internal install level includes **INSTALLUILEVEL\_PROGRESSONLY**.<br/>                                                                                                             |
| [**MsiUISourceResOnly**](msiuisourceresonly.md)<br/>                   | [**MsiUISourceResOnly**](msiuisourceresonly.md) to 1 (one) when the internal install level includes **INSTALLUILEVEL\_SOURCERESONLY**.<br/>                                                                                                                       |
| [**NOCOMPANYNAME**](nocompanyname.md)<br/>                             | Suppresses the automatic setting of the [**COMPANYNAME**](companyname.md) property.<br/>                                                                                                                                                                          |
| [**NOUSERNAME**](nousername.md)<br/>                                   | Suppresses the automatic setting of the [**USERNAME**](username.md) property.<br/>                                                                                                                                                                                |
| [**OutOfDiskSpace**](outofdiskspace.md)<br/>                           | Insufficient disk space to accommodate the installation.<br/>                                                                                                                                                                                                      |
| [**OutOfNoRbDiskSpace**](outofnorbdiskspace.md)<br/>                   | Insufficient disk space with rollback turned off.<br/>                                                                                                                                                                                                             |
| [**Preselected**](preselected.md)<br/>                                 | Features are already selected.<br/>                                                                                                                                                                                                                                |
| [**PrimaryVolumePath**](primaryvolumepath.md)<br/>                     | The Installer sets the value of this property to the path of the volume that the [**PRIMARYFOLDER**](primaryfolder.md) property designates.<br/>                                                                                                                  |
| [**PrimaryVolumeSpaceAvailable**](primaryvolumespaceavailable.md)<br/> | The Installer sets the value of this property to a string that represents the total number of bytes available on the volume that the [**PrimaryVolumePath**](primaryvolumepath.md) property references.<br/>                                                      |
| [**PrimaryVolumeSpaceRemaining**](primaryvolumespaceremaining.md)<br/> | The Installer sets the value of this property to a string that represents the total number of bytes remaining on the volume that the [**PrimaryVolumePath**](primaryvolumepath.md) property references if all the currently selected features are installed.<br/> |
| [**PrimaryVolumeSpaceRequired**](primaryvolumespacerequired.md)<br/>   | The Installer sets the value of this property to a string that represents the total number of bytes required by all currently selected features on the volume that the [**PrimaryVolumePath**](primaryvolumepath.md) property references.<br/>                    |
| [**ProductLanguage**](productlanguage.md)<br/>                         | Numeric language identifier (LANGID) for the database. (REQUIRED)<br/>                                                                                                                                                                                             |
| [**ReplacedInUseFiles**](replacedinusefiles.md)<br/>                   | Set if the installer installs over a file that is being held in use.<br/>                                                                                                                                                                                          |
| [**RESUME**](resume.md)<br/>                                           | Resumed installation.<br/>                                                                                                                                                                                                                                         |
| [**RollbackDisabled**](rollbackdisabled.md)<br/>                       | The installer sets this property when rollback is disabled.<br/>                                                                                                                                                                                                   |
| [**UILevel**](uilevel.md)<br/>                                         | Indicates the user interface level.<br/>                                                                                                                                                                                                                           |
| [**UpdateStarted**](updatestarted.md)<br/>                             | Set when changes to the system have begun for this installation.<br/>                                                                                                                                                                                              |
| [**UPGRADINGPRODUCTCODE**](upgradingproductcode.md)<br/>               | Set by the installer when an upgrade removes an application.<br/>                                                                                                                                                                                                  |
| [**VersionMsi**](versionmsi.md)<br/>                                   | The installer sets this property to the version of Windows Installer that is run during the installation.<br/>                                                                                                                                                     |



 

## Operating System Properties

The following list provides links to more information about operating system properties that the Installer sets at startup.



| Property Name                                                                             | Brief Description                                                                                                                                                                                                                                                                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AdminUser**](adminuser.md)<br/>                                                 | Set on Windows 2000 if the user has administrator privileges.<br/>                                                                                                                                                                                                                        |
| [**ComputerName**](computername.md)<br/>                                           | Computer name of the current system.<br/>                                                                                                                                                                                                                                                 |
| [**MsiNetAssemblySupport**](msinetassemblysupport.md)<br/>                         | On systems that support common language runtime assemblies, the Installer sets the value of this property to the file version of fusion.dll. The Installer does not set this property if the operating system does not support common language runtime assemblies.<br/>                   |
| [**MsiNTProductType**](msintproducttype.md)<br/>                                   | Indicates the Windows product type.<br/>                                                                                                                                                                                                                                                  |
| [**MsiNTSuiteBackOffice**](msintsuitebackoffice.md)<br/>                           | On Windows 2000 and later operating systems, the Installer sets this property to 1 (one) only if Microsoft BackOffice components are installed.<br/>                                                                                                                                      |
| [**MsiNTSuiteDataCenter**](msintsuitedatacenter.md)<br/>                           | On Windows 2000 and later operating systems, the Installer sets this property to 1 (one) only if Windows 2000 Datacenter Server is installed.<br/>                                                                                                                                        |
| [**MsiNTSuiteEnterprise**](msintsuiteenterprise.md)<br/>                           | On Windows 2000 and later operating systems, the Installer sets this property to 1 (one) only if Windows 2000 Advanced Server is installed.<br/>                                                                                                                                          |
| [**MsiNTSuitePersonal**](msintsuitepersonal.md)<br/>                               | On Windows XP and later operating systems, the Installer sets this property to 1 (one) only if the operating system is Home (not Professional).<br/>                                                                                                                                      |
| [**MsiNTSuiteSmallBusiness**](msintsuitesmallbusiness.md)<br/>                     | On Windows 2000 and later operating systems, the Installer sets this property to 1 (one) only if Microsoft Small Business Server is installed.<br/>                                                                                                                                       |
| [**MsiNTSuiteSmallBusinessRestricted**](msintsuitesmallbusinessrestricted.md)<br/> | On Windows 2000 and later operating systems, the Installer sets this property to 1 (one) only if Microsoft Small Business Server is installed with the restrictive client license.<br/>                                                                                                   |
| [**MsiNTSuiteWebServer**](msintsuitewebserver.md)<br/>                             | On Windows 2000 and later operating systems, the Installer sets the [**MsiNTSuiteWebServer**](msintsuitewebserver.md) property to 1 (one) if the web edition of the Windows Server 2003 is installed. Only available with the Windows Server 2003 release of the Windows Installer.<br/> |
| [**MsiTabletPC**](msitabletpc.md)<br/>                                             | The installer sets this property to a nonzero value if the current operating system is Windows XP Tablet PC Edition.<br/>                                                                                                                                                                 |
| [**MsiWin32AssemblySupport**](msiwin32assemblysupport.md)<br/>                     | On systems that support Win32 assemblies, the Installer sets the value of this property to the file version of sxs.dll. The Installer does not set this property if the operating system does not support Win32 assemblies.<br/>                                                          |
| [**OLEAdvtSupport**](oleadvtsupport.md)<br/>                                       | Set if OLE supports the Windows Installer.<br/>                                                                                                                                                                                                                                           |
| [**RedirectedDllSupport**](redirecteddllsupport.md)<br/>                           | The Installer sets the [**RedirectedDllSupport**](redirecteddllsupport.md) property if the system performing the installation supports [Isolated Components](isolated-components.md).<br/>                                                                                              |
| [**RemoteAdminTS**](remoteadmints.md)<br/>                                         | The Installer sets the [**RemoteAdminTS**](remoteadmints.md) property when the system is a remote administration server running the Terminal Server role service.<br/>                                                                                                                   |
| [**ServicePackLevel**](servicepacklevel.md)<br/>                                   | The version number of the operating system service pack.<br/>                                                                                                                                                                                                                             |
| [**ServicePackLevelMinor**](servicepacklevelminor.md)<br/>                         | The minor version number of the operating system service pack.<br/>                                                                                                                                                                                                                       |
| [**SharedWindows**](sharedwindows.md)<br/>                                         | Set when the system is operating as Shared Windows.<br/>                                                                                                                                                                                                                                  |
| [**ShellAdvtSupport**](shelladvtsupport.md)<br/>                                   | Set if the shell supports feature advertising.<br/>                                                                                                                                                                                                                                       |
| [**SystemLanguageID**](systemlanguageid.md)<br/>                                   | Default language identifier for the system.<br/>                                                                                                                                                                                                                                          |
| [**TerminalServer**](terminalserver.md)<br/>                                       | Set when the system is a server running the Terminal Server role service.<br/>                                                                                                                                                                                                            |
| [**TTCSupport**](ttcsupport.md)<br/>                                               | Indicates if the operating system supports using .ttc (true type font collections) files.<br/>                                                                                                                                                                                            |
| [**Version9X**](version9x.md)<br/>                                                 | Version number for the Windows operating system.<br/>                                                                                                                                                                                                                                     |
| [**VersionDatabase**](versiondatabase.md)<br/>                                     | Numeric database version of the current installation.<br/>                                                                                                                                                                                                                                |
| [**VersionNT**](versionnt.md)<br/>                                                 | Version number for the operating system.<br/>                                                                                                                                                                                                                                             |
| [**VersionNT64**](versionnt64.md)<br/>                                             | Version number for the operating system if the system is running on a 64-bit computer.<br/>                                                                                                                                                                                               |
| [**Windows build**](windowsbuild.md)<br/>                                          | Build number of the operating system.<br/>                                                                                                                                                                                                                                                |



 

## Product Information Properties

The following list provides links to more information about product-specific properties specified in the [Property Table](property-table.md).



| Property Name                                                  | Brief Description                                                                                                                         |
|----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [**ARPHELPLINK**](arphelplink.md)<br/>                  | Internet address or URL for technical support.<br/>                                                                                 |
| [**ARPHELPTELEPHONE**](arphelptelephone.md)<br/>        | Technical support phone numbers.<br/>                                                                                               |
| [**DiskPrompt**](diskprompt.md)<br/>                    | String displayed by a message box that prompts for a disk.<br/>                                                                     |
| [**IsAdminPackage**](isadminpackage.md)<br/>            | Set to 1 (one) if the current installation is running from a package created through an administrative installation.<br/>           |
| [**LeftUnit**](leftunit.md)<br/>                        | Places units to the left of the number.<br/>                                                                                        |
| [**Manufacturer**](manufacturer.md)<br/>                | Name of the application manufacturer. (Required)<br/>                                                                               |
| [**MediaSourceDir**](mediasourcedir.md)<br/>            | The installer sets this property to 1 (one) when the installation uses a media source, such as a CD-ROM.<br/>                       |
| [**MSIINSTANCEGUID**](msiinstanceguid.md)<br/>          | The presence of this property indicates that a product code changing transform is registered to the product.<br/>                   |
| [**MSINEWINSTANCE**](msinewinstance.md)<br/>            | This property indicates the installation of a new instance of a product with instance transforms.<br/>                              |
| [**ParentProductCode**](parentoriginaldatabase.md)<br/> | The installer sets this property for installations that a [Concurrent Installation](concurrent-installations.md) action runs.<br/> |
| [**PIDTemplate**](pidtemplate.md)<br/>                  | String used as a template for the [**PIDKEY**](pidkey.md) property.<br/>                                                           |
| [**ProductCode**](productcode.md)<br/>                  | A unique identifier for a specific product release. (Required)<br/>                                                                 |
| [**ProductName**](productname.md)<br/>                  | Human readable name of an application. (Required)<br/>                                                                              |
| [**ProductState**](productstate.md)<br/>                | Set to the installed state of a product.<br/>                                                                                       |
| [**ProductVersion**](productversion.md)<br/>            | String format of the product version as a numeric value. (Required)<br/>                                                            |
| [**UpgradeCode**](upgradecode.md)<br/>                  | A GUID that represents a related set of products.<br/>                                                                              |



 

## Summary Information Update Properties

The following properties are only set by transforms in .msp files that are used to update the summary information stream of an administrative image.



| Property                                                              | Description                                                                                                                  |
|-----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| [**PATCHNEWPACKAGECODE**](patchnewpackagecode.md)<br/>         | The value of this property is written to the [**Revision Number Summary**](revision-number-summary.md) Property.<br/> |
| [**PATCHNEWSUMMARYCOMMENTS**](patchnewsummarycomments.md)<br/> | The value of this property is written to the [**Comments Summary**](comments-summary.md) Property.<br/>               |
| [**PATCHNEWSUMMARYSUBJECT**](patchnewsummarysubject.md)<br/>   | The value of this property is written to the [**Subject Summary**](subject-summary.md) Property.<br/>                 |



 

## System Folder Properties

The following list provides links to more information about system folders that the installer sets at setup.



| Property                                                        | Description                                                                           |
|-----------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [**AdminToolsFolder**](admintoolsfolder.md)<br/>         | The full path to the directory that contains administrative tools.<br/>         |
| [**AppDataFolder**](appdatafolder.md)<br/>               | The full path to the **Roaming** folder for the current user.<br/>              |
| [**CommonAppDataFolder**](commonappdatafolder.md)<br/>   | The full path to application data for all users.<br/>                           |
| [**CommonFiles64Folder**](commonfiles64folder.md)<br/>   | The full path to the predefined **64-bit Common Files** folder.<br/>            |
| [**CommonFilesFolder**](commonfilesfolder.md)<br/>       | The full path to the **Common Files** folder for the current user.<br/>         |
| [**DesktopFolder**](desktopfolder.md)<br/>               | The full path to the **Desktop** folder.<br/>                                   |
| [**FavoritesFolder**](favoritesfolder.md)<br/>           | The full path to the **Favorites** folder for the current user.<br/>            |
| [**FontsFolder**](fontsfolder.md)<br/>                   | The full path to the **Fonts** folder.<br/>                                     |
| [**LocalAppDataFolder**](localappdatafolder.md)<br/>     | The full path to the folder that contains local (nonroaming) applications.<br/> |
| [**MyPicturesFolder**](mypicturesfolder.md)<br/>         | The full path to the **Pictures** folder.<br/>                                  |
| [**NetHoodFolder**](nethoodfolder.md)<br/>               | The full path to the **NetHood** folder.<br/>                                   |
| [**PersonalFolder**](personalfolder.md)<br/>             | The full path to the **Documents** folder for the current user.<br/>            |
| [**PrintHoodFolder**](printhoodfolder.md)<br/>           | The full path to the **PrintHood** folder.<br/>                                 |
| [**ProgramFiles64Folder**](programfiles64folder.md)<br/> | The full path to the predefined **64-bit Program Files** folder.<br/>           |
| [**ProgramFilesFolder**](programfilesfolder.md)<br/>     | The full path to the predefined **32-bit Program Files** folder.<br/>           |
| [**ProgramMenuFolder**](programmenufolder.md)<br/>       | The full path to the **Program Menu** folder.<br/>                              |
| [**RecentFolder**](recentfolder.md)<br/>                 | The full path to the **Recent** folder.<br/>                                    |
| [**SendToFolder**](sendtofolder.md)<br/>                 | The full path to the **SendTo** folder for the current user.<br/>               |
| [**StartMenuFolder**](startmenufolder.md)<br/>           | The full path to the **Start menu** folder.<br/>                                |
| [**StartupFolder**](startupfolder.md)<br/>               | The full path to the **Startup** folder.<br/>                                   |
| [**System16Folder**](system16folder.md)<br/>             | The full path to folder for 16-bit system DLLs.<br/>                            |
| [**System64Folder**](system64folder.md)<br/>             | The full path to the predefined **System64** folder.<br/>                       |
| [**SystemFolder**](systemfolder.md)<br/>                 | The full path to the **System** folder for the current user.<br/>               |
| [**TempFolder**](tempfolder.md)<br/>                     | The full path to the **Temp** folder.<br/>                                      |
| [**TemplateFolder**](templatefolder.md)<br/>             | The full path to the **Template** folder for the current user.<br/>             |
| [**WindowsFolder**](windowsfolder.md)<br/>               | The full path to the **Windows** folder.<br/>                                   |
| [**WindowsVolume**](windowsvolume.md)<br/>               | The volume of the **Windows** folder.<br/>                                      |



 

## User Information Properties

The following list provides links to more information about user-supplied information.



| Property                                                      | Description                                                                             |
|---------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [**AdminProperties**](adminproperties.md)<br/>         | List of properties that are set during an administration installation.<br/>       |
| [**COMPANYNAME**](companyname.md)<br/>                 | Organization name of the user who is performing the installation.<br/>            |
| [**LogonUser**](logonuser.md)<br/>                     | User name for the user who is currently logged on.<br/>                           |
| [**MsiHiddenProperties**](msihiddenproperties.md)<br/> | List of properties that are prevented from being written into the log.<br/>       |
| [**PIDKEY**](pidkey.md)<br/>                           | Part of the Product ID that the user enters.<br/>                                 |
| [**ProductID**](productid.md)<br/>                     | Full Product ID after a successful validation.<br/>                               |
| [**UserLanguageID**](userlanguageid.md)<br/>           | Default language identifier of the current user.<br/>                             |
| [**USERNAME**](username.md)<br/>                       | User who is performing the installation.<br/>                                     |
| [**UserSID property**](usersid.md)<br/>                | Set by the installer according to the security identifier (SID) of the user.<br/> |



 

 

 
