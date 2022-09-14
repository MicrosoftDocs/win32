---
description: ICEM09 verifies the merge module safely handles predefined directories.
ms.assetid: 747ae5ee-adc1-4aa7-8239-2379f76bfd0f
title: ICEM09
ms.topic: article
ms.date: 05/31/2018
---

# ICEM09

ICEM09 verifies the merge module safely handles predefined directories. It does this by verifying that no component in the module installs a directory to a predefined system directory such as "ProgramFilesFolder" or "StartMenuFolder". Instead, modules should use directories with unique names (created with the merge module naming convention) and use custom actions to target the appropriate target directory. This approach prevents modules from conflicting with an existing directory structure in the final database. ICEM09 checks that the custom actions needed for this technique to work either do not exist (so that the merge tool can generate them) or exist in the correct form (so that they work as expected).

Failure to fix a warning or error reported by ICEM09 could cause problems for the clients of your merge module. Directory table rows with primary keys such as ProgramFilesFolder often exist in a database; therefore, if components in your module install directly to predefined directories such as ProgramFilesFolder, the directory entries in the module may collide with already existing rows. This condition would require the user of your module to split the source files from your module in order to match the existing source directory.

## Result

ICEM09 reports an error or warning when a module component installs a directory to a pre-defined system directory, causing a possible name conflict with the existing directory structure.

## Example

ICEM09 posts the following warnings for a module containing the database entries shown.

``` syntax
Warning: The component 'Component1.<GUID>' installs directly into the pre-defined 
directory 'ProgramFilesFolder'. It is recommended that merge modules alias 
all such directories to unique names.
```

Rename the merge module directory so it does not match a Windows Installer property and therefore is unique. Then set a property of the same name to the value of the Windows Installer directory. When directory resolution takes place, the directory has a property of the same name, so the install location of the directory is the value of the property. Files move from the distinct source location to the same target location. This process should completely remove the merge conflicts.

``` syntax
Warning: The 'ModuleInstallExecuteSequence' table contains a type 51 action 
(StartMenuFolder.<GUID>) for a pre-defined directory, but this action 
does not have sequence number '1'
```

If the action does not have sequence number 1, it may not merge in to the target database early enough in the sequence to work effectively.

To fix this warning, set the sequence number to 1. Note that most current merge tools (but not some older versions) will generate these custom actions at merge time, so it is not always necessary to explicitly author the actions into the merge module.

``` syntax
Warning: The 'CustomAction' table contains a type 51 action (MyAppDataFolderAction) 
for a pre-defined directory, but the name is not the same as the target directory. 
Many merge tools will generate duplicate actions."
```

Because the CustomAction column is the primary key of CustomAction table, some merge tools may generate duplicate actions because the pre-authored action name is different.

To fix this warning, name the action the same as the target directory. Note that most current merge tools (but not some older versions) generate these custom actions at merge time, so it is not always necessary to explicitly author the actions into the merge module.

[Directory Table](directory-table.md)



| Directory          | Directory\_Parent | DefaultDir |
|--------------------|-------------------|------------|
| ProgramFilesFolder | Directory1        | A          |
| StartMenuFolder    | Directory2        | B:C        |
| AppDataFolder      | Directory3        | D          |
| MyPicturesFolder   | Directory4        | E          |



 

[Component Table](component-table.md)



| Component               | Directory          |
|-------------------------|--------------------|
| Component1.&lt;GUID&gt; | ProgramFilesFolder |
| Component2.&lt;GUID&gt; | StartMenuFolder    |
| Component3.&lt;GUID&gt; | AppDataFolder      |
| Component4.&lt;GUID&gt; | MyPicturesFolder   |



 

[CustomAction Table](customaction-table.md)



| CustomAction                 | Type | Source                       | Target              |
|------------------------------|------|------------------------------|---------------------|
| StartMenuFolder.&lt;GUID&gt; | 51   | StartMenuFolder.&lt;GUID&gt; | \[StartMenuFolder\] |
| MyAppDataFolderAction        | 51   | AppDataFolder.&lt;GUID&gt;   | \[AppDataFolder\]   |



 

[ModuleInstallExecuteSequence Table](moduleinstallexecutesequence-table.md)



| Action                       | Sequence | BaseAction | After | Condition |
|------------------------------|----------|------------|-------|-----------|
| StartMenuFolder.&lt;GUID&gt; | 100      |            |       |           |



 

## Related topics

<dl> <dt>

[Merge Module ICE Reference](merge-module-ice-reference.md)
</dt> </dl>

 

 



