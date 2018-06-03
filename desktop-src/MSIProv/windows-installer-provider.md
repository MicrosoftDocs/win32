---
title: Windows Installer Provider
description: The Windows \ 160;Installer provider \ 8212; also known as the MSI provider \ 8212; allows WMI-enabled applications to access information collected from Windows Installer compliant applications.
ms.assetid: d635cc67-242e-4e8a-9b31-2cdb6b0937d6
keywords:
- providers Windows Management Instrumentation , Windows Installer, MSI provider, Install
- Windows Installer provider Windows Management Instrumentation
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Windows Installer Provider

The Windows Installer provider— also known as the MSI provider— allows WMI-enabled applications to access information collected from Windows Installer compliant applications. The MSI provider is installed by default on all Windows 32-bit desktop and server operating systems. The provider is an optional component on Windows 64-bit desktop and server operating systems, but can be installed through the **Control** panel.

The Windows Installer provider makes the functions of the Windows Installer available through WMI classes. The Windows Installer technology organizes software into a hierarchy of parts that have subparts. Each part contains properties of the installed software product. Arranging the parts in a hierarchy clarifies the nature of the software product installation.

The Windows Installer provider reads the properties of a software product installation for remote users and local computers to use the installation procedures that the Windows Installer provides. By using WMI, you can perform many powerful software installation tasks.

The Windows Installer provider is an instance and method provider that implements the standard [**IWbemProviderInit**](https://msdn.microsoft.com/library/aa391853) interface, and the following [**IWbemServices**](https://msdn.microsoft.com/library/aa392093) methods:

-   [**CreateInstanceEnumAsync**](https://msdn.microsoft.com/library/aa392098)
-   [**DeleteInstanceAsync**](https://msdn.microsoft.com/library/aa392102)
-   [**ExecMethodAsync**](https://msdn.microsoft.com/library/aa392104)
-   [**ExecQueryAsync**](https://msdn.microsoft.com/library/aa392108)
-   [**GetObjectAsync**](https://msdn.microsoft.com/library/aa392110)
-   [**PutInstanceAsync**](https://msdn.microsoft.com/library/aa392116)

The following table identifies the classes and descriptions that the Windows Installer provider supports.



| Class category                                  | Description                                                                                                                                                     |
|-------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Actions](#actions)                             | Classes derived from [**CIM\_Action**](https://msdn.microsoft.com/library/aa386541) represent actions performed during an installation, upgrade, uninstall, or application maintenance. |
| [Associations](#associations)                   | Instances of this association class represent references to other Installer provider classes.                                                                   |
| [Checks](#checks)                               | Classes derived from [**CIM\_Check**](https://msdn.microsoft.com/library/aa387206) represent conditions that should be true when a software feature or element is installed.             |
| [Core Classes](#core-classes)                   | Classes that you can use to access 90 percent of software installation information. These are the most important classes.                                       |
| [External Associations](#external-associations) | Instances of this association class represent references to Microsoft Win32 classes that the Installer provider classes do not support.                         |
| [Settings](#settings)                           | Instances of settings capture a set of properties that are meaningful within the context of a specific environment (setup).                                     |



 

## Actions

Actions are derived from the Distributed Management Task Force (DMTF) [**CIM\_Action**](https://msdn.microsoft.com/library/aa386541) class. An action is an operation that is part of a process to either create a software element in its next state, or to eliminate the software element in the current state. Functions derived from **CIM\_Action** are those performed during an installation, upgrade, uninstall, or application maintenance.

The [**CIM\_Action**](https://msdn.microsoft.com/library/aa386541) class can also supply details about actions that the Windows Installer takes if a product or feature is installed, upgraded, or uninstalled.

For example, if a shared element such as a Spell Checker is uninstalled, Microsoft Installer (MSI) might have to update other applications such as word processors and email programs to ensure that they do not offer the Spell Checker feature.

> [!Note]  
> The classes identified in the following list are always associated with software features or their associated elements.

 

The following list identifies the action classes for the Windows Installer provider:

-   [**Win32\_BindImageAction**](win32-bindimageaction.md)
-   [**Win32\_ClassInfoAction**](win32-classinfoaction.md)
-   [**Win32\_CreateFolderAction**](win32-createfolderaction.md)
-   [**Win32\_DuplicateFileAction**](win32-duplicatefileaction.md)
-   [**Win32\_ExtensionInfoAction**](win32-extensioninfoaction.md)
-   [**Win32\_FontInfoAction**](win32-fontinfoaction.md)
-   [**Win32\_MIMEInfoAction**](win32-mimeinfoaction.md)
-   [**Win32\_MoveFileAction**](win32-movefileaction.md)
-   [**Win32\_PublishComponentAction**](win32-publishcomponentaction.md)
-   [**Win32\_RegistryAction**](win32-registryaction.md)
-   [**Win32\_RemoveFileAction**](win32-removefileaction.md)
-   [**Win32\_RemoveIniAction**](win32-removeiniaction.md)
-   [**Win32\_SelfRegModuleAction**](win32-selfregmoduleaction.md)
-   [**Win32\_ShortcutAction**](win32-shortcutaction.md)
-   [**Win32\_TypeLibraryAction**](win32-typelibraryaction.md)

## Associations

Association classes exist so that associations between software application installation objects (products and software features, software elements, checks, and actions) can be represented. These associations are internal to the schema. They do not associate classes outside of the Windows Installer provider schema.

The following list identifies the association classes for the Windows Installer provider:

-   [**Win32\_ActionCheck**](win32-actioncheck.md)
-   [**Win32\_ApplicationCommandLine**](win32-applicationcommandline.md)
-   [**Win32\_CheckCheck**](win32-checkcheck.md)
-   [**Win32\_ODBCDriverSoftwareElement**](win32-odbcdriversoftwareelement.md)
-   [**Win32\_ProductCheck**](win32-productcheck.md)
-   [**Win32\_ProductResource**](win32-productresource.md)
-   [**Win32\_ProductSoftwareFeatures**](win32-productsoftwarefeatures.md)
-   [**Win32\_SettingCheck**](win32-settingcheck.md)
-   [**Win32\_ShortcutSAP**](win32-shortcutsap.md)
-   [**Win32\_SoftwareElementAction**](win32-softwareelementaction.md)
-   [**Win32\_SoftwareElementCheck**](win32-softwareelementcheck.md)
-   [**Win32\_SoftwareElementResource**](win32-softwareelementresource.md)
-   [**Win32\_SoftwareFeatureAction**](win32-softwarefeatureaction.md)
-   [**Win32\_SoftwareFeatureCheck**](win32-softwarefeaturecheck.md)
-   [**Win32\_SoftwareFeatureParent**](win32-softwarefeatureparent.md)
-   [**Win32\_SoftwareFeatureSoftwareElements**](win32-softwarefeaturesoftwareelements.md)

## Core Classes

The core classes are the base classes of the Windows Installer provider schema. They make up the basic application installation instance hierarchy. You can use the following classes to access the bulk of the information on software application-installations.

The following list identifies the core classes for the Windows Installer provider:

-   [**Win32\_Product**](win32-product.md)
-   [**Win32\_SoftwareElement**](win32-softwareelement.md)
-   [**Win32\_SoftwareFeature**](win32-softwarefeature.md)

## Checks

Checks are derived from the DMTF [**CIM\_Check**](https://msdn.microsoft.com/library/aa387206) class. A check is a condition or characteristic that is expected to be true within the scope of a [**CIM\_ComputerSystem**](https://msdn.microsoft.com/library/aa387219) instance. The **CIM\_Check** class represents details to be checked when a software feature or element is installed. This information might specify that other software features should be installed, or that specific hardware requirements must be met. An example is a check to see if enough disk space is available.

> [!Note]  
> These classes are always associated with software features or their associated elements.

 

The following list identifies the check classes for the Windows Installer provider:

-   [**Win32\_Condition**](win32-condition.md)
-   [**Win32\_DirectorySpecification**](win32-directoryspecification.md)
-   [**Win32\_EnvironmentSpecification**](win32-environmentspecification.md)
-   [**Win32\_FileSpecification**](win32-filespecification.md)
-   [**Win32\_IniFileSpecification**](win32-inifilespecification.md)
-   [**Win32\_LaunchCondition**](win32-launchcondition.md)
-   [**Win32\_ODBCDataSourceSpecification**](win32-odbcdatasourcespecification.md)
-   [**Win32\_ODBCDriverSpecification**](win32-odbcdriverspecification.md)
-   [**Win32\_ODBCTranslatorSpecification**](win32-odbctranslatorspecification.md)
-   [**Win32\_ProgIDSpecification**](win32-progidspecification.md)
-   [**Win32\_ReserveCost**](win32-reservecost.md)
-   [**Win32\_ServiceSpecification**](win32-servicespecification.md)
-   [**Win32\_SoftwareElementCondition**](win32-softwareelementcondition.md)

## External Associations

External association classes are like association classes except that they represent relationships between objects of Windows Installer classes and objects of standard Win32 classes. Examples of external associations are those that bind software elements to a computer or service access point (SAP).

> [!Note]  
> A [**CIM\_ComputerSystem**](https://msdn.microsoft.com/library/aa387219) object represents the environment in which [**CIM\_SoftwareElement**](https://msdn.microsoft.com/library/aa388467) instances will be or are installed. If a software element is already installed, the [**CIM\_InstalledSoftwareElement**](https://msdn.microsoft.com/library/aa387870) association is used to identify the **CIM\_ComputerSystem** object that represents the environment.

 

The following list identifies the external association classes for the Windows Installer provider:

-   [**Win32\_InstalledSoftwareElement**](win32-installedsoftwareelement.md)
-   [**Win32\_ServiceSpecificationService**](win32-servicespecificationservice.md)

## Settings

Settings contain more information about installations or their components.

The following list identifies the setting classes for the Windows Installer provider:

-   [**Win32\_Binary**](win32-binary.md)
-   [**Win32\_MSIResource**](win32-msiresource.md)
-   [**Win32\_ODBCAttribute**](win32-odbcattribute.md)
-   [**Win32\_ODBCSourceAttribute**](win32-odbcsourceattribute.md)
-   [**Win32\_Patch**](win32-patch.md)
-   [**Win32\_PatchPackage**](win32-patchpackage.md)
-   [**Win32\_Property**](win32-property.md)
-   [**Win32\_ServiceControl**](win32-servicecontrol.md)

## Related topics

<dl> <dt>

[WMI Providers](https://msdn.microsoft.com/library/aa394570)
</dt> </dl>

 

 




