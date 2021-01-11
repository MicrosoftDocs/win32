---
description: The Feature Table defines the logical tree structure of features and contains the columns shown in the following table.
ms.assetid: 1faee1d5-6e39-43ea-bf92-a0b3986a13a1
title: Feature Table
ms.topic: article
ms.date: 05/31/2018
---

# Feature Table

The Feature Table defines the logical tree structure of features and contains the columns shown in the following table.



| Column          | Type                         | Key | Nullable |
|-----------------|------------------------------|-----|----------|
| Feature         | [Identifier](identifier.md) | Y   | N        |
| Feature\_Parent | [Identifier](identifier.md) | N   | Y        |
| Title           | [Text](text.md)             | N   | Y        |
| Description     | [Text](text.md)             | N   | Y        |
| Display         | [Integer](integer.md)       | N   | Y        |
| Level           | [Integer](integer.md)       | N   | N        |
| Directory\_     | [Identifier](identifier.md) | N   | Y        |
| Attributes      | [Integer](integer.md)       | N   | N        |



 

## Columns

<dl> <dt>

<span id="Feature"></span><span id="feature"></span><span id="FEATURE"></span>Feature
</dt> <dd>

The primary key that is used to identify a specific feature record. The value in this field must not exceed a maximum length of 38 characters.

</dd> <dt>

<span id="Feature_Parent"></span><span id="feature_parent"></span><span id="FEATURE_PARENT"></span>Feature\_Parent
</dt> <dd>

An optional key of a parent record in the same table.

The key points to the Feature column. If the parent feature is not selected, then this feature is not installed. A null value in this field indicates that this feature does not have a parent and is a root item. The Feature\_Parent column must not equal the Feature column of the same record.

> [!Note]  
> The maximum depth of any feature is 16. An [error 2701](windows-installer-error-messages.md) results if a feature that exceeds this maximum depth exists.

 

</dd> <dt>

<span id="Title"></span><span id="title"></span><span id="TITLE"></span>Title
</dt> <dd>

A short string of text that identifies a feature.

This string is listed as an item by the [SelectionTree Control](selectiontree-control.md) of the [Selection Dialog](selection-dialog.md).

</dd> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>Description
</dt> <dd>

A longer string of text that describes a feature.

This localizable string is displayed by the [Text Control](text-control.md) of the [Selection Dialog](selection-dialog.md).

</dd> <dt>

<span id="Display"></span><span id="display"></span><span id="DISPLAY"></span>Display
</dt> <dd>

The number in this field specifies the order in which the feature is to be displayed in the user interface.

The value also determines whether or not the feature is initially displayed expanded or collapsed. If the value is null or 0 (zero), the record is not displayed.

-   If the value is odd, the feature node is expanded initially.
-   If the value is even, the feature node is collapsed initially.

</dd> <dt>

<span id="Level"></span><span id="level"></span><span id="LEVEL"></span>Level
</dt> <dd>

The initial installation level of this feature. Processing the [Condition Table](condition-table.md) can modify the level value.

An install level of 0 (zero) disables the item and prevents it from being displayed. A feature with an installation level of 0 (zero) is not installed during any installation, including administrative installations. For more information, see the "Install Level" information in the Remarks section of this topic.

</dd> <dt>

<span id="Directory_"></span><span id="directory_"></span><span id="DIRECTORY_"></span>Directory\_
</dt> <dd>

The Directory\_ column specifies the name of a directory that can be configured by a [Selection Dialog](selection-dialog.md).

Because this field is a key into the [Directory Table](directory-table.md), the specified directory must be listed in the first column of the Directory Table. You must enter a [Public Property](public-properties.md) in this column to make the directory configurable, and to display a **Browse** button on the [Selection Dialog](selection-dialog.md).

</dd> <dt>

<span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes
</dt> <dd>

The remote execution option for features that are not installed and for which no feature state request is made by using any of the following properties.

-   [**ADDLOCAL Property**](addlocal.md)
-   [**ADDSOURCE Property**](addsource.md)
-   [**ADDDEFAULT Property**](adddefault.md)
-   [**COMPADDLOCAL Property**](compaddlocal.md)
-   [**COMPADDSOURCE Property**](compaddsource.md)
-   [**FILEADDLOCAL Property**](fileaddlocal.md)
-   [**FILEADDSOURCE Property**](fileaddsource.md)
-   [**REMOVE Property**](remove.md)
-   [**REINSTALL Property**](reinstall.md)
-   [**ADVERTISE Property**](advertise.md)

Add the indicated bits to the total value of this column to include a remote execution option.

-   If this field is blank, the value defaults to 0 (zero), msidbFeatureAttributesFavorLocal.
-   If the feature install level is 0 (zero), or greater than or equal to the current install level, no change is made in the feature state.



| Name                                         | Decimal | Hexadecimal | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------------------------------------------|---------|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| msidbFeatureAttributesFavorLocal             | 0       | 0x0000      | Components of this feature that are not marked for installation from source are installed locally. A component shared by two or more features, some of which are set to msidbFeatureAttributesFavorLocal and some to msidbFeatureAttributesFavorSource, is installed locally. Components marked msidbComponentAttributesSourceOnly in the [Component Table](component-table.md) are always run from the source CD/server. The bits msidbFeatureAttributesFavorLocal and msidbFeatureAttributesFavorSource work with features not listed by the [**ADVERTISE Property**](advertise.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| msidbFeatureAttributesFavorSource            | 1       | 0x0001      | Components of this feature not marked for local installation are installed to run from the source CD-ROM or server. A component shared by two or more features, some of which are set to msidbFeatureAttributesFavorLocal and some to msidbFeatureAttributesFavorSource, is installed to run locally. Components marked msidbComponentAttributesLocalOnly in the [Component Table](component-table.md) are always installed locally. The bits msidbFeatureAttributesFavorLocal and msidbFeatureAttributesFavorSource work with features not listed by the [**ADVERTISE Property**](advertise.md).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| msidbFeatureAttributesFollowParent           | 2       | 0x0002      | Set this attribute and the state of the feature is the same as the state of the feature's parent. You cannot use this option if the feature is located at the root of a feature tree. Omit this attribute and the feature state is determined according to msidbFeatureAttributesDisallowAdvertise and msidbFeatureAttributesFavorLocal and msidbFeatureAttributesFavorSource.<br/> To guarantee that the child feature's state always follows the state of its parent, even when the child and parent are initially set to absent in the SelectionTree Control, you must include both msidbFeatureAttributesFollowParent and msidbFeatureAttributesUIDisallowAbsent in the attributes of the child feature.<br/> Note that if you set msidbFeatureAttributesFollowParent without setting msidbFeatureAttributesUIDisallowAbsent, the installer cannot force the child feature out of the absent state. In this case, the child feature matches the parent's installation state only if the child is set to something other than absent.<br/> Set msidbFeatureAttributesFollowParent and msidbFeatureAttributesUIDisallowAbsent to ensure a child feature follows the state of the parent feature.<br/> |
| msidbFeatureAttributesFavorAdvertise         | 4       | 0x0004      | Set this attribute and the feature state is Advertise. If the feature is listed by the [**ADDDEFAULT Property**](adddefault.md) this bit is ignored and the feature state is determined according to msidbFeatureAttributesFavorLocal and msidbFeatureAttributesFavorSource. Omit this attribute and the feature state is determined according to msidbFeatureAttributesDisallowAdvertise and msidbFeatureAttributesFavorLocal and msidbFeatureAttributesFavorSource.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| msidbFeatureAttributesDisallowAdvertise      | 8       | 0x0008      | Note that this bit works only with features that are listed by the [**ADVERTISE Property**](advertise.md). Set this attribute to prevent the feature from being advertised.<br/> Set this attribute and if the listed feature is not a parent or child, the feature is installed according to msidbFeatureAttributesFavorLocal and msidbFeatureAttributesFavorSource.<br/> Set this attribute for the parent of a listed feature and the parent is installed.<br/> Set this attribute for the child of a listed feature and the state of the child is Absent.<br/> Omit this attribute and if the listed feature is not a parent or child, the feature state is Advertise.<br/> Omit this attribute and if the listed feature is a parent or child, the state of both features is Advertise.<br/>                                                                                                                                                                                                                                                                                                                                                                                          |
| msidbFeatureAttributesUIDisallowAbsent       | 16      | 0x0010      | Set this attribute and the user interface does not display an option to change the feature state to Absent. Setting this attribute forces the feature to the installation state, whether or not the feature is visible in the UI. Omit this attribute and the user interface displays an option to change the feature state to Absent.<br/> Set msidbFeatureAttributesFollowParent and msidbFeatureAttributesUIDisallowAbsent to ensure a child feature follows the state of the parent feature.<br/> Setting this attribute not only affects the UI, but also forces the feature to the install state whether the feature is visible in the UI or not.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| msidbFeatureAttributesNoUnsupportedAdvertise | 32      | 0x0020      | Set this attribute and advertising is disabled for the feature if the operating system shell does not support Windows Installer descriptors. Omit this attribute and advertising is not disabled.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |



 

Some attributes are exclusive of each other. Attempting to set these attributes together on the same feature causes the installation package to fail [**Package Validation**](package-validation.md).

-   Do not use msidbFeatureAttributesFavorAdvertise with msidbFeatureAttributesDisallowAdvertise.
-   Do not use msidbFeatureAttributesNoUnsupportedAdvertise with msidbFeatureAttributesDisallowAdvertise together.
-   Do not use msidbFeatureAttributesFollowParent with msidbFeatureAttributesFavorSource.
-   Note that the msidbFeatureAttributesFollowParent and msidbFeatureAttributesFavorLocal values are mutually exclusive. If the msidbFeatureAttributesFollowParent value is used, the msidbFeatureAttributesFavorLocal value is assumed to not exist.

</dd> </dl>

Note that if a child feature is installed, its parent feature is also installed. If a parent feature is installed, its child feature is not necessarily installed unless its msidbFeatureAttributesFollowParent and msidbFeatureAttributesUIDisallowAbsent attributes are set. This hierarchical relationship of the installation of parent and child features is also used for the GUI installations and installations that use command-line properties.

## Remarks

Several additional temporary columns are added to this table when it is loaded into memory for computations used by costing and user interface (UI) selection.

A component can be shared between two or more features or applications. If two or more features refer to the same component, then that component is selected for installation if any of the associated features are selected. This can also be the reason child features are not uninstalled when a parent feature is removed. If the child feature consists of components needed by other features or applications, the Windows Installer does not remove the child feature.

For more information, see [Controlling Feature Selection States](controlling-feature-selection-states.md).

Install Level:

-   For any installation, there is a defined install level, which is an integral value from 1 to 32,767. The initial value is determined by the [**INSTALLLEVEL Property**](installlevel.md), which is set in the [Property Table](property-table.md).
-   A feature is installed only if the feature level value is less than or equal to the current install level. The UI can be authored so that when the installation is initialized, the Installer allows the user to modify the install level of any feature in the Feature Table. For example, an author can define install level values that represent specific installation options, such as **Custom**, **Typical**, or **Minimum**, and then create a dialog box that uses [SetInstallLevel ControlEvents](setinstalllevel-controlevent.md) to enable the user to select one of these states.
-   Depending on the state the user selects, the dialog box sets the install level property to the corresponding value. If the author assigns **Typical** a level of 100 and the user selects **Typical**, only those features with a level of 100 or less are installed. In addition, the **Custom** option could lead to another dialog box that contains a [SelectionTree Control](selectiontree-control.md). The SelectionTree Control then allows the user to individually change whether or not each feature is installed.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE10](ice10.md)  
[ICE14](ice14.md)  
[ICE21](ice21.md)  
[ICE32](ice32.md)  
[ICE41](ice41.md)  
[ICE45](ice45.md)  
[ICE47](ice47.md)  
[ICE50](ice50.md)  
[ICE57](ice57.md)  
[ICE59](ice59.md)  
[ICE62](ice62.md)  
[ICE67](ice67.md)  
[ICE79](ice79.md)  
[ICE86](ice86.md)  
[ICE94](ice94.md)  
</dl>

 

 




