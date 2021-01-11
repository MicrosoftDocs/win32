---
description: For information on control attributes, see the link to the particular control that you need to create in Controls as well as the links to particular control attributes in the following lists.
ms.assetid: 948ce3d3-e463-40de-8b5f-21ef18b1a0ce
title: Control Attributes
ms.topic: article
ms.date: 05/31/2018
---

# Control Attributes

For information on control attributes, see the link to the particular control that you need to create in [Controls](controls.md) as well as the links to particular control attributes in the following lists.

The following methods are used for specifying the attributes of a control:

-   Use the [ControlCondition table](controlcondition-table.md) to disable, enable, hide, or show a control according to the value of a property or conditional statement. You can also use this table to override the default control specified in the [Dialog table](dialog-table.md).
-   Subscribe the control to a ControlEvent in the [EventMapping table](eventmapping-table.md). Enter the attribute's identifier in the Attribute column and the ControlEvent's identifier in the Event column of this table.
-   Set the control attribute bit flags for the control in the Attribute column of the [Control table](control-table.md). This sets the attributes upon the creation of the control.

Some attributes cannot be set for every control or be specified by all of the above methods. See the particular control and attribute topics for details.

The initial values of some control attributes can be set with bits in the [Control table](control-table.md).



| Attribute                                          | Decimal | Hexadecimal | Constant                               |
|----------------------------------------------------|---------|-------------|----------------------------------------|
| [BiDi](bidi-control-attribute.md)                 | 224     | 0x000000E0  | **msidbControlAttributesBiDi**         |
| [Enabled](enabled-control-attribute.md)           | 2       | 0x00000002  | **msidbControlAttributesEnabled**      |
| [Indirect](indirect-control-attribute.md)         | 8       | 0x00000008  | **msidbControlAttributesIndirect**     |
| [Integer Control](integer-control-attribute.md)   | 16      | 0x00000010  | **msidbControlAttributesInteger**      |
| [LeftScroll](leftscroll-control-attribute.md)     | 128     | 0x00000080  | **msidbControlAttributesLeftScroll**   |
| [RightAligned](rightaligned-control-attribute.md) | 64      | 0x00000040  | **msidbControlAttributesRightAligned** |
| [RTLRO](rtlro-control-attribute.md)               | 32      | 0x00000020  | **msidbControlAttributesRTLRO**        |
| [Sunken](sunken-control-attribute.md)             | 4       | 0x00000004  | **msidbControlAttributesSunken**       |
| [Visible](visible-control-attribute.md)           | 1       | 0x00000001  | **msidbControlAttributesVisible**      |



 

These attributes of Text controls are set with bits.



| Attribute                                            | Decimal | Hexadecimal | Constant                                |
|------------------------------------------------------|---------|-------------|-----------------------------------------|
| [FormatSize](formatsize-control-attribute.md)       | 524288  | 0x00080000  | **msidbControlAttributesFormatSize**    |
| [NoPrefix](noprefix-control-attribute.md)           | 131072  | 0x00020000  | **msidbControlAttributesNoPrefix**      |
| [NoWrap](nowrap-control-attribute.md)               | 262144  | 0x00040000  | **msidbControlAttributesNoWrap**        |
| [Password](password-control-attribute.md)           | 2097152 | 0x00200000  | **msidbControlAttributesPasswordInput** |
| [Transparent](transparent-control-attribute.md)     | 65536   | 0x00010000  | **msidbControlAttributesTransparent**   |
| [UsersLanguage](userslanguage-control-attribute.md) | 1048576 | 0x00100000  | **msidbControlAttributesUsersLanguage** |



 

This attribute of the ProgressBar control is set with a bit.



| Attribute                                      | Decimal | Hexadecimal | Constant                             |
|------------------------------------------------|---------|-------------|--------------------------------------|
| [Progress95](progress95-control-attribute.md) | 65536   | 0x00010000  | **msidbControlAttributesProgress95** |



 

These attributes of Volume and Directory SelectCombo controls are set with bits.



| Attribute                                                | Decimal | Hexadecimal | Constant                                  |
|----------------------------------------------------------|---------|-------------|-------------------------------------------|
| [CDROMVolume](cdromvolume-control-attribute.md)         | 524288  | 0x00080000  | **msidbControlAttributesCDROMVolume**     |
| [FixedVolume](fixedvolume-control-attribute.md)         | 131072  | 0x00020000  | **msidbControlAttributesFixedVolume**     |
| [FloppyVolume](floppyvolume-control-attribute.md)       | 2097152 | 0x00200000  | **msidbControlAttributesFloppyVolume**    |
| [RAMDiskVolume](ramdiskvolume-control-attribute.md)     | 1048576 | 0x00100000  | **msidbControlAttributesRAMDiskVolume**   |
| [RemoteVolume](remotevolume-control-attribute.md)       | 262144  | 0x00040000  | **msidbControlAttributesRemoteVolume**    |
| [RemovableVolume](removablevolume-control-attribute.md) | 65536   | 0x00010000  | **msidbControlAttributesRemovableVolume** |



 

These attributes of ListBox and ComboBox controls are set with bits.



| Attribute                                            | Decimal | Hexadecimal | Constant                            |
|------------------------------------------------------|---------|-------------|-------------------------------------|
| [ComboList Control](combolist-control-attribute.md) | 131072  | 0x00020000  | **msidbControlAttributesComboList** |
| [Sorted Control](sorted-control-attribute.md)       | 65536   | 0x00010000  | **msidbControlAttributesSorted**    |



 

This attribute of the Edit control is set with a bit.



| Attribute                                    | Decimal | Hexadecimal | Constant                            |
|----------------------------------------------|---------|-------------|-------------------------------------|
| [MultiLine](multiline-control-attribute.md) | 65536   | 0x00010000  | **msidbControlAttributesMultiline** |



 

These attributes of PictureButton controls are set with bits.



| Attribute                                          | Decimal | Hexadecimal | Constant                             |
|----------------------------------------------------|---------|-------------|--------------------------------------|
| [Bitmap](bitmap-control-attribute.md)             | 262144  | 0x00040000  | **msidbControlAttributesBitmap**     |
| [FixedSize](fixedsize-control-attribute.md)       | 1048576 | 0x00100000  | **msidbControlAttributesFixedSize**  |
| [Icon](icon-control-attribute.md)                 | 524288  | 0x00080000  | **msidbControlAttributesIcon**       |
| [IconSize16](iconsize-control-attribute.md)       | 2097152 | 0x00200000  | **msidbControlAttributesIconSize16** |
| [IconSize32](iconsize-control-attribute.md)       | 4194304 | 0x00400000  | **msidbControlAttributesIconSize32** |
| [IconSize48](iconsize-control-attribute.md)       | 6291456 | 0x00600000  | **msidbControlAttributesIconSize48** |
| [PushLike Control](pushlike-control-attribute.md) | 131072  | 0x00020000  | **msidbControlAttributesPushLike**   |



 

This attribute of RadioButton control is set with a bit.



| Attribute                                    | Decimal  | Hexadecimal | Constant                            |
|----------------------------------------------|----------|-------------|-------------------------------------|
| [HasBorder](hasborder-control-attribute.md) | 16777216 | 0x01000000  | **msidbControlAttributesHasBorder** |



 

This attribute of PushButton control is set with a bit.



| Attribute                                        | Decimal | Hexadecimal | Constant                                  |
|--------------------------------------------------|---------|-------------|-------------------------------------------|
| [ElevationShield](elevationshield-attribute.md) | 8388608 | 0x00800000  | **msidbControlAttributesElevationShield** |



 

This attribute of VolumeCostList control is set with a bit.



| Attribute                                                                | Decimal | Hexadecimal | Constant                         |
|--------------------------------------------------------------------------|---------|-------------|----------------------------------|
| [ControlShowRollbackCost](controlshowrollbackcost-control-attribute.md) | 4194304 | 0x00400000  | **msidbControlShowRollbackCost** |



 

The following control attributes are not set with bits. These attributes are authored into the user interface tables or are set using [Control Events](control-events.md).

[BillboardName](billboardname-control-attribute.md)

 

[IndirectPropertyName](indirectpropertyname-control-attribute.md)

 

[Position](position-control-attribute.md)

 

[Progress Control](progress-control-attribute.md)

 

[PropertyName](propertyname-control-attribute.md)

 

[PropertyValue](propertyvalue-control-attribute.md)

 

[Text Control](text-control-attribute.md)

 

[TimeRemaining](timeremaining-control-attribute.md)

See [Adding Controls and Text](adding-controls-and-text.md).

 

 



