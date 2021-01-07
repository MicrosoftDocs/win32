---
description: ICE30 validates that the installation of components containing the same file never installs the file more than once in the same directory.
ms.assetid: 74cb455b-a53e-4c6b-98ff-08cf0858f11f
title: ICE30
ms.topic: article
ms.date: 05/31/2018
---

# ICE30

ICE30 validates that the installation of components containing the same file never installs the file more than once in the same directory.

ICE30 goes to every component in the [Component table](component-table.md) and then determines the component's target directory from the [Directory table](directory-table.md). It then checks to see which of these components install to the same target directory. Finally, it uses the [File table](file-table.md) to verify that none of the files in these components have the same name.

ICE30 checks both long file names (LFN) and short file names (SFN).

ICE30 does not evaluate properties in the resolution of directories because these properties can change at runtime and alter the directory resolution scheme. This means ICE30 can detect file collisions due to directories with the same property in their paths, but does not detect collisions resulting from two properties having the same value.

## Result

ICE30 posts an error message for each pair of components that installs the same file to the same directory.

## Example

The example shown returns each of the following errors twice.



| ICE30 error or warning                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ERROR: The target file 'README.1st' is installed in 'TARGETDIR\\PRODUCT' by two different components on an SFN system: 'Component1' and 'Component2'. This breaks component reference counting.                                                                                           | Component1 and Component2 both have a file named 'READEME.1st'. When using short file names, the installer installs both Dir1 and Dir2 to the same directory, TARGETDIR\\PRODUCT.<br/> ICE30 generate two errors, one for each file. In an authoring environment that displays error locations, the first error is at one file's entry in the [File Table](file-table.md), and the second at the location of the other file.<br/> |
| ERROR: Installation of a conditionalized component would cause the target file 'README.1st' to be installed in 'TARGETDIR\\COMMON TOOLS' by two different components on an LFN system: 'Component3' and 'Component4'. This would break component reference counting.                      | Component4 has an entry in the Condition column of the [Component table](component-table.md) and Component3 does not. If [**VersionNT**](versionnt.md) is True, Component4 is installed, and there a collision with the Readme.1st always installed by Component3.<br/> ICE30 generates 4 errors, one pair for SFN, one for LFN.<br/>                                                                                            |
| WARNING: The target file 'README.1st' might be installed in 'TARGETDIR\\COMMON TOOLS' by two different conditionalized components on an SFN system: 'Component4' and 'Component5'. If the conditions are not mutually exclusive, this will break the component reference counting system. | Because Component4 and Component5 both have entries in the Condition column of the [Component table](component-table.md) this file collision may not occur. ICE30 only posts a warning because the conditions must be determined at the time of the installation.<br/> ICE30 generates 4 warnings, one pair for SFN, one for LFN.<br/>                                                                                            |



 

[Component Table](component-table.md) (partial)



| Component  | Directory | Condition |
|------------|-----------|-----------|
| Component1 | Dir1      |           |
| Component2 | Dir2      |           |
| Component3 | Dir3      |           |
| Component4 | Dir3      | VersionNT |
| Component5 | Dir3      | Version9X |



 

[Directory Table](directory-table.md)



| Directory | Parent\_Directory | DefaultDir                    |
|-----------|-------------------|-------------------------------|
| SOURCEDIR |                   | TARGETDIR                     |
| Dir1      | SOURCEDIR         | Product\|Component1 Product:. |
| Dir2      | SOURCEDIR         | Product:.                     |
| Dir3      | SOURCEDIR         | Common\|Common Tools:         |



 

[File Table](file-table.md) (partial)



| File  | Component\_ | FileName   |
|-------|-------------|------------|
| File1 | Component1  | README.1st |
| File2 | Component2  | README.1st |
| File3 | Component3  | README.1st |
| File4 | Component4  | README.1st |
| File5 | Component5  | README.1st |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 




