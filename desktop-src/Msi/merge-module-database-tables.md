---
description: The following tables are required in a standard merge module.
ms.assetid: 2af6cea0-6d93-4aa5-a708-d305f11986ef
title: Merge Module Database Tables
ms.topic: article
ms.date: 05/31/2018
---

# Merge Module Database Tables

The following tables are required in a standard merge module.



| Table name                                       | Comment                                                                                          |
|--------------------------------------------------|--------------------------------------------------------------------------------------------------|
| [Component](component-table.md)                 | (REQUIRED)                                                                                       |
| [Directory](directory-table.md)                 | (REQUIRED)                                                                                       |
| [FeatureComponents](featurecomponents-table.md) | (REQUIRED)                                                                                       |
| [File](file-table.md)                           | (REQUIRED)                                                                                       |
| [ModuleSignature](modulesignature-table.md)     | (REQUIRED) Merged into the installer database. Lists the information identifying a merge module. |
| [ModuleComponents](modulecomponents-table.md)   | (REQUIRED) Merged into the installer database. Lists all the components in the merge module.     |



 

The following tables only occur in merge modules or other installer databases that have already been combined with a merge module.



| Table name                                     | Comment                                                                                                     |
|------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| [ModuleDependency](moduledependency-table.md) | Merged into the installer database. Lists other merge modules required by this merge module.                |
| [ModuleExclusion](moduleexclusion-table.md)   | Merged into the installer database. Lists other merge modules that are incompatible with this merge module. |



 

The following ModuleSequence tables only occur in merge modules.



| Table name                                                             | Comment                                                                                   |
|------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [ModuleAdminUISequence](moduleadminuisequence-table.md)               | Merges actions into the [AdminUISequence table](adminuisequence-table.md).               |
| [ModuleAdminExecuteSequence](moduleadminexecutesequence-table.md)     | Merges actions into the [AdminExecuteSequence table](adminexecutesequence-table.md).     |
| [ModuleAdvtUISequence](moduleadvtuisequence-table.md)                 | Do not use this table. For details, see [AdvtUISequence table](advtuisequence-table.md). |
| [ModuleAdvtExecuteSequence](moduleadvtexecutesequence-table.md)       | Merges actions into the [AdvtExecuteSequence table](advtexecutesequence-table.md).       |
| [ModuleIgnoreTable](moduleignoretable-table.md)                       | Lists tables in the module that are not merged into the .msi file.                        |
| [ModuleInstallUISequence](moduleinstalluisequence-table.md)           | Merges actions into the [InstallUISequence table](installuisequence-table.md).           |
| [ModuleInstallExecuteSequence](moduleinstallexecutesequence-table.md) | Merges actions into the [InstallExecuteSequence table](installexecutesequence-table.md). |



 

The following tables are required in every configurable merge module. Mergemod.dll 2.0 or later is required to create configurable merge module. For details, see [Configurable Merge Modules](configurable-merge-modules.md).



| Table name                                                 | Comment                                                                                                                                                                                          |
|------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ModuleSubstitution Table](modulesubstitution-table.md)   | (REQUIRED) This table is not merged into the target installation database. Specifies the configurable fields in the target database and provides a template for the configuration of each field. |
| [ModuleConfiguration Table](moduleconfiguration-table.md) | (REQUIRED) This table is not merged into the target installation database. Identifies the configurable attributes of the module.                                                                 |



 

The following installer tables cannot occur in a standard merge module.

-   [BBControl](bbcontrol-table.md)
-   [Billboard](billboard-table.md)
-   [CCPSearch](ccpsearch-table.md)
-   [Error](error-table.md)
-   [Feature](feature-table.md)
-   [LaunchCondition table](launchcondition-table.md)
-   [Media](media-table.md)
-   [Patch](patch-table.md)
-   [Upgrade](upgrade-table.md)

The following installer tables are optional in merge modules.

-   [ActionText](actiontext-table.md)
-   [AdminExecuteSequence](adminexecutesequence-table.md)
-   [AdminUISequence](adminuisequence-table.md)
-   [AdvtExecuteSequence](advtexecutesequence-table.md)
-   [AdvtUISequence](advtuisequence-table.md)
-   [AppId](appid-table.md)
-   [AppSearch](appsearch-table.md)
-   [BindImage](bindimage-table.md)
-   [CheckBox](checkbox-table.md)
-   [Class](class-table.md)
-   [ComboBox](combobox-table.md)
-   [CompLocator](complocator-table.md)
-   [Control](control-table.md)
-   [ControlCondition](controlcondition-table.md)
-   [CreateFolder](createfolder-table.md)
-   [CustomAction](customaction-table.md)
-   [Dialog](dialog-table.md)
-   [DrLocator](drlocator-table.md)
-   [DuplicateFile](duplicatefile-table.md)
-   [Environment](environment-table.md)
-   [EventMapping](eventmapping-table.md)
-   [Extension](extension-table.md)
-   [Font](font-table.md)
-   [Icon](icon-table.md)
-   [IniFile](inifile-table.md)
-   [IniLocator](inilocator-table.md)
-   [InstallExecuteSequence](installexecutesequence-table.md)
-   [InstallUISequence](installuisequence-table.md)
-   [ListBox](listbox-table.md)
-   [ListView](listview-table.md)
-   [MIME](mime-table.md)
-   [MoveFile](movefile-table.md)
-   [ODBCAttribute](odbcattribute-table.md)
-   [ODBCDataSource](odbcdatasource-table.md)
-   [ODBCDriver](odbcdriver-table.md)
-   [ODBCSourceAttribute](odbcsourceattribute-table.md)
-   [ODBCTranslator](odbctranslator-table.md)
-   [ProgID Table](progid-table.md)
-   [Property](property-table.md)
-   [PublishComponent](publishcomponent-table.md)
-   [RadioButton](radiobutton-table.md)
-   [Registry Table](registry-table.md)
-   [RegLocator](reglocator-table.md)
-   [RemoveFile](removefile-table.md)
-   [RemoveIniFile](removeinifile-table.md)
-   [RemoveRegistry](removeregistry-table.md)
-   [ReserveCost](reservecost-table.md)
-   [SelfReg](selfreg-table.md)
-   [ServiceControl](servicecontrol-table.md)
-   [ServiceInstall](serviceinstall-table.md)
-   [Shortcut](shortcut-table.md)
-   [Signature](signature-table.md)
-   [TextStyle](textstyle-table.md)
-   [TypeLib](typelib-table.md)
-   [UIText](uitext-table.md)
-   [Verb](verb-table.md)

 

 



