---
Description: Represents a server component on a managed node.
audience: developer
ms.assetid: 31e4b549-ea2f-4d02-8cee-ba0b7f660715
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: MSFT\_ServerManagerServerComponent class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_ServerManagerServerComponent class

Represents a server component on a managed node.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("deploymentprovider")]
class MSFT_ServerManagerServerComponent
{
  String                 UniqueName;
  String                 DisplayName;
  String                 Description;
  sint32                 NumericId;
  sint32                 MajorVersion;
  sint32                 MinorVersion;
  uint8                  Installed;
  uint8                  FeatureType;
  String                 ParentName;
  String                 SubFeatures[];
  String                 NonAncestorDependencies[];
  String                 MutualExclusions[];
  Boolean                InstallWithParentByDefault;
  String                 Deploys[];
  object                 Descriptor;
  uint8                  ConfigurationStatus;
  String                 EventQuery;
  String                 BestPracticeModels[];
  MSFT_ServiceToMonitor  SystemServices[];
  String                 PostInstallDescription;
  String                 PostUninstallDescription;
  MSFT_OptionalCompanion OptionalCompanions[];
};
```

## Members

The **MSFT\_ServerManagerServerComponent** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_ServerManagerServerComponent** class has these properties.

<dl> <dt>

**BestPracticeModels**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**ConfigurationStatus**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the status of the server component configuration.

<dt>

<span id="ConfigurationFailed"></span><span id="configurationfailed"></span><span id="CONFIGURATIONFAILED"></span>

**ConfigurationFailed** (0)


</dt> <dd></dd> <dt>

<span id="NotConfigured"></span><span id="notconfigured"></span><span id="NOTCONFIGURED"></span>

**NotConfigured** (1)


</dt> <dd></dd> <dt>

<span id="Configured"></span><span id="configured"></span><span id="CONFIGURED"></span>

**Configured** (2)


</dt> <dd></dd> <dt>

<span id="NotApplicable"></span><span id="notapplicable"></span><span id="NOTAPPLICABLE"></span>

**NotApplicable** (3)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (4)


</dt> <dd></dd> </dl>

</dd> <dt>

**Deploys**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the description of the server component.

</dd> <dt>

**Descriptor**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **EmbeddedObject**
</dt> </dl>

Gets the name of the [**MSFT\_ServerManagerServerComponentDescriptor**](msft-servermanagerservercomponentdescriptor.md) object that contains the identity of the server component.

</dd> <dt>

**DisplayName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the display name of the server component.

</dd> <dt>

**EventQuery**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**FeatureType**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the feature type of the server component.

<dt>

<span id="Role"></span><span id="role"></span><span id="ROLE"></span>

**Role** (0)


</dt> <dd></dd> <dt>

<span id="RoleService"></span><span id="roleservice"></span><span id="ROLESERVICE"></span>

**RoleService** (1)


</dt> <dd></dd> <dt>

<span id="Feature"></span><span id="feature"></span><span id="FEATURE"></span>

**Feature** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**Installed**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the status of the server component installation.

<dt>

<span id="Available"></span><span id="available"></span><span id="AVAILABLE"></span>

**Available** (0)


</dt> <dd></dd> <dt>

<span id="Installed"></span><span id="installed"></span><span id="INSTALLED"></span>

**Installed** (1)


</dt> <dd></dd> <dt>

<span id="UninstallPending"></span><span id="uninstallpending"></span><span id="UNINSTALLPENDING"></span>

**UninstallPending** (2)


</dt> <dd></dd> <dt>

<span id="InstallPending"></span><span id="installpending"></span><span id="INSTALLPENDING"></span>

**InstallPending** (3)


</dt> <dd></dd> <dt>

<span id="NotPresent"></span><span id="notpresent"></span><span id="NOTPRESENT"></span>

**NotPresent** (4)


</dt> <dd></dd> <dt>

<span id="Removed"></span><span id="removed"></span><span id="REMOVED"></span>

**Removed** (5)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (6)


</dt> <dd></dd> </dl>

</dd> <dt>

**InstallWithParentByDefault**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether this server component is installed by default when a parent server component is installed. True to install this server component with a parent server component by default; otherwise false.

</dd> <dt>

**MajorVersion**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the major version number of the server component.

</dd> <dt>

**MinorVersion**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the minor version number of the server component.

</dd> <dt>

**MutualExclusions**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**NonAncestorDependencies**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains the names of the dependencies of the server component that aren't ancestors of the server component.

</dd> <dt>

**NumericId**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the ID of the server component.

</dd> <dt>

**OptionalCompanions**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_OptionalCompanion** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**MSFT\_OptionalCompanion**](msft-optionalcompanion.md)")
</dt> </dl>

Gets an array that contains the names of the child [**MSFT\_OptionalCompanion**](msft-optionalcompanion.md) objects that are managed by the server component.

</dd> <dt>

**ParentName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the name of the parent server component.

</dd> <dt>

**PostInstallDescription**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**PostUninstallDescription**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**SubFeatures**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains the names of features managed by the server component.

</dd> <dt>

**SystemServices**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_ServiceToMonitor** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**MSFT\_ServiceToMonitor**](msft-servicetomonitor.md)")
</dt> </dl>

Gets an array that contains the names of the [**MSFT\_ServiceToMonitor**](msft-servicetomonitor.md) objects that represent the system services that are managed by the server component.

</dd> <dt>

**UniqueName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the unique name of the server component.

</dd> </dl>

## Requirements



|                                     |                                                                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                                  |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                                                  |
| MOF<br/>                      | <dl> <dt>ServerManager.DeploymentProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ServerManager.DeploymentProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[ServerManager Deploymentprovider Provider Classes](server-manager-deployment.md)
</dt> </dl>

 

 




