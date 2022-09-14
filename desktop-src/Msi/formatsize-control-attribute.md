---
description: If this bit is set for a static text control, the control automatically attempts to format the displayed text as a number that represents a count of bytes.
ms.assetid: acf76fff-b7a4-456b-91b9-eb3087879d7b
title: FormatSize Control Attribute
ms.topic: article
ms.date: 05/31/2018
---

# FormatSize Control Attribute

If this bit is set for a static text control, the control automatically attempts to format the displayed text as a number that represents a count of bytes. For proper formatting, the control's text must be set to a string that represents a number expressed in units of 512 bytes. The displayed value is then formatted in kilobytes (KB), megabytes (MB), or gigabytes (GB), and displayed with the appropriate string that represents the units. For more information, see [Text Control](text-control.md).



| Numerical value of original text | Unit string used |
|----------------------------------|------------------|
| Less than 20480                  | KB               |
| Less than 20971520               | MB               |
| Less than 10737418240            | GB               |



 

## Valid Controls



| Decimal | Hexadecimal | Control                          |
|---------|-------------|----------------------------------|
| 524288  | 0x00080000  | msidbControlAttributesFormatSize |



 

## Remarks

To set this attribute on a control, include the FormatSize bits in the Attributes column of the control's record in the [Control Table](control-table.md). The control's text must be set to a string representing a number expressed in units of 512 bytes. The text of the unit strings are defined in the [UIText Table](uitext-table.md). The positioning of the unit string is controlled by the [**LeftUnit**](leftunit.md) Property. If the **LeftUnit** Property is defined to be any value, the unit string appears before the numerical value. If anything other than numerical characters appears in the text associated with the control, the displayed value is undefined.

At run time, the installer resolves the [**PrimaryVolumeSpaceRequired**](primaryvolumespacerequired.md) Property to the total number of bytes required for the installation in units of 512. A static text control with FormatSize bit can be used to automatically format and label the total number of bytes required for the installation in KB, MB, or GB as appropriate. For the purposes of this example, assume the total number of bytes is 18,336,768. The installer sets the value of the PrimaryVolumeSpaceRequired property to 18,336,768 divided by 512, or 35,814. The number displayed by the text control with FormatSize would be 17MB.

The numerical values of the original text are given in units of 512. In the table above, the string 20,480 corresponds to the KB string because 20,480 times 512 yields a result of 10,485,760 bytes or 10,240 KB.

The unit strings listed in the previous table refer to keys in the [UIText Table](uitext-table.md), where the text of the unit string is defined.

The positioning of the unit string is controlled by the [**LeftUnit**](leftunit.md) Property. If the **LeftUnit** Property is defined to be any value, the unit string appears before the numerical value.

If anything other than numerical characters appears in the text associated with the control, the displayed value is undefined.

For more information, see [Control Attributes](control-attributes.md) and [Controls](controls.md).

 

 



