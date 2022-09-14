---
description: The lists and tables in this section show the output of the generic formatter. Be aware that the generic formatter uses the DataType and DataQualifier members of the PROPERTYINFO structure to determine how to format the displayed data.
ms.assetid: cf3dc6cd-7b24-464a-9d2b-5e35c4e8825e
title: Generic Formatter Output
ms.topic: article
ms.date: 05/31/2018
---

# Generic Formatter Output

The lists and tables in this section show the output of the [*generic formatter*](g.md). Be aware that the generic formatter uses the **DataType** and **DataQualifier** members of the [**PROPERTYINFO**](propertyinfo.md) structure to determine how to format the displayed data.

For more information and an example of the output for a specific property data type, see:

-   [PROP\_TYPE\_VOID](/windows)
-   [PROP\_TYPE\_SUMMARY](/windows)
-   [PROP\_TYPE\_BYTE](/windows)
-   [PROP\_TYPE\_WORD](/windows)
-   [PROP\_TYPE\_DWORD](/windows)
-   PROP\_TYPE\_LARGEINT (generic formatter does not support)
-   PROP\_TYPE\_ADDR (generic formatter does not support)
-   [PROP\_TYPE\_TIME](/windows)
-   [PROP\_TYPE\_STRING](/windows)
-   [PROP\_TYPE\_IP\_ADDRESS](/windows)
-   PROP\_TYPE\_BYTESWAPPED\_WORD (Obsolete. For more information, see [PROP\_TYPE\_WORD](/windows))
-   PROP\_TYPE\_BYTESWAPPED\_DWORD (Obsolete. For more information, see [PROP\_TYPE\_DWORD](/windows))
-   PROP\_TYPE\_TYPED\_STRING (Obsolete)
-   [PROP\_TYPE\_RAW\_DATA](/windows)
-   [PROP\_TYPE\_COMMENT](/windows)
-   PROP\_TYPE\_SRCFRIENDLYNAME (generic formatter does not support)
-   PROP\_TYPE\_DSTFRIENDLYNAME (generic formatter does not support)
-   PROP\_TYPE\_TOKENRING\_ADDRESS (generic formatter does not support)
-   PROP\_TYPE\_FDDI\_ADDRESS (generic formatter does not support)
-   PROP\_TYPE\_ETHERNET\_ADDRESS (generic formatter does not support)
-   PROP\_TYPE\_OBJECT\_IDENTIFIER (generic formatter does not support)
-   PROP\_TYPE\_VINES\_IP\_ADDRESS (generic formatter does not support)
-   PROP\_TYPE\_VAR\_LEN\_SMALL\_INT (generic formatter does not support)

## PROP\_TYPE\_VOID and PROP\_TYPE\_COMMENT

The following table lists the generic format output for **PROP\_TYPE\_VOID** and **PROP\_TYPE\_COMMENT** data type properties.

In the formatter output column, the value of the data in the capture is XYZ.



| Property qualifier            | Formatter output                                      |
|-------------------------------|-------------------------------------------------------|
| PROP\_QUAL\_NONE              | XYZ                                                   |
| PROP\_QUAL\_RANGE             | XYZ                                                   |
| PROP\_QUAL\_BITFIELD          | Obsolete                                              |
| PROP\_QUAL\_LABELED\_SET      | XYZ                                                   |
| PROP\_QUAL\_LABELED\_BITFIELD | Obsolete. For more information, see PROP\_QUAL\_FLAGS |
| PROP\_QUAL\_CONST             | XYZ                                                   |
| PROP\_QUAL\_FLAGS             | XYZ                                                   |
| PROP\_QUAL\_ARRAY             | XYZ                                                   |



 

## PROP\_TYPE\_SUMMARY

The following table lists the generic format output for **PROP\_TYPE\_SUMMARY** data type properties.

In the example output column, the value of the data in the capture is XYZ.



| Property qualifier            | Example output                                        |
|-------------------------------|-------------------------------------------------------|
| PROP\_QUAL\_NONE              | XYZ                                                   |
| PROP\_QUAL\_RANGE             | XYZ                                                   |
| PROP\_QUAL\_BITFIELD          | Obsolete                                              |
| PROP\_QUAL\_LABELED\_SET      | XYZ                                                   |
| PROP\_QUAL\_LABELED\_BITFIELD | Obsolete. For more information, see PROP\_QUAL\_FLAGS |
| PROP\_QUAL\_CONST             | XYZ                                                   |
| PROP\_QUAL\_FLAGS             | XYZ                                                   |
| PROP\_QUAL\_ARRAY             | XYZ                                                   |



 

## PROP\_TYPE\_BYTE

The following table lists the generic format output for **PROP\_TYPE\_BYTE** data type properties.

In the example output column, the value of the data in the capture is 10.



| Property qualifier            | Example output                                                                                                |
|-------------------------------|---------------------------------------------------------------------------------------------------------------|
| PROP\_QUAL\_NONE              | 10 (0xa)"                                                                                                     |
| PROP\_QUAL\_RANGE             | 10 (0xa) Range:(1 (0x1) - 20 (0x14))                                                                          |
| PROP\_QUAL\_SET               | 10 (0xa) Matches Set Value or<br/> 10 (0xa) Unknown Set Value<br/>                                |
| PROP\_QUAL\_BITFIELD          | Obsolete.                                                                                                     |
| PROP\_QUAL\_LABELED\_SET      | Corresponding label in a label set or number.                                                                 |
| PROP\_QUAL\_LABELED\_BITFIELD | Obsolete. For more information, see PROP\_QUAL\_FLAGS.                                                        |
| PROP\_QUAL\_CONST             | No output. No data is displayed in the detail pane.                                                           |
| PROP\_QUAL\_FLAGS             | .......0 = Label Off String ......1. = Label On String .....0.. = Label Off String ....1... = Label On String |
| PROP\_QUAL\_ARRAY             | 0a ff ...                                                                                                     |



 

## PROP\_TYPE\_WORD

The following table lists the generic format output for a **PROP\_TYPE\_WORD** data type property.

> [!Note]  
> For non-Intel, byte-swapped DWORD properties, you must change the data to an Intel format. To change the format, set the *IFlags* parameter of the **Attach** property instance function IFLAG\_SWAPPED when you map the property instance to a location.

 

In the example output column, the value of the data in the capture is 10.



| Property qualifier            | Example output                                                                                                                                                                                                                |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PROP\_QUAL\_NONE              | 10 (0xa)                                                                                                                                                                                                                      |
| PROP\_QUAL\_RANGE             | 10 (0xa) Range:(1 (0x1) - 20 (0x14))                                                                                                                                                                                          |
| PROP\_QUAL\_SET               | 10 (0xa) Matches Set Value or<br/> 10 (0xa) Unknown Set Value<br/>                                                                                                                                                |
| PROP\_QUAL\_BITFIELD          | Obsolete.                                                                                                                                                                                                                     |
| PROP\_QUAL\_LABELED\_SET      | Corresponding label in the label set or number.                                                                                                                                                                               |
| PROP\_QUAL\_LABELED\_BITFIELD | Obsolete. For more information, see PROP\_QUAL\_FLAGS.                                                                                                                                                                        |
| PROP\_QUAL\_CONST             | No output. No data is displayed in the detail pane.                                                                                                                                                                           |
| PROP\_QUAL\_FLAGS             | .......0 = Label Off String ......0. = Label Off String .....0.. = Label Off String ....0... = Label Off String ...0.... = Label Off String ..1..... = Label On String .0...... = Label Off String 1....... = Label On String |
| PROP\_QUAL\_ARRAY             | 000a ffff ...                                                                                                                                                                                                                 |



 

## PROP\_TYPE\_DWORD

The following table lists the generic format output for **PROP\_TYPE\_DWORD** data type properties.

> [!Note]  
> For non-Intel, byte-swapped DWORD properties, you must change the data to an Intel format. To change the format, set the *IFlags* parameter of the **Attach** property instance function IFLAG\_SWAPPED when you map the property instance to a location.

 

In the example output column, the value of the data in the capture is 10.



| Property qualifier            | Example output                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PROP\_QUAL\_NONE              | 10 (0xa)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| PROP\_QUAL\_RANGE             | 10 (0xa) Range:(1 (0x1) - 20 (0x14))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| PROP\_QUAL\_SET               | 10 (0xa) Matches Set Value or<br/> 10 (0xa) Unknown Set Value<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| PROP\_QUAL\_BITFIELD          | Obsolete.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| PROP\_QUAL\_LABELED\_SET      | Corresponding label in label set or number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| PROP\_QUAL\_LABELED\_BITFIELD | Obsolete. For more information, see PROP\_QUAL\_FLAGS.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| PROP\_QUAL\_CONST             | No output. No data is displayed in the detail pane.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| PROP\_QUAL\_FLAGS             | ...............0 = Label Off String ..............0. = Label Off String .............0.. = Label Off String ............0... = Label Off String ...........0.... = Label Off String ..........0..... = Label Off String .........0...... = Label Off String ........0....... = Label Off String .......0........ = Label Off String ......0......... = Label Off String .....0.......... = Label Off String ....0........... = Label Off String ...0............ = Label Off String ..1............. = Label On String .0.............. = Label Off String 1............... = Label On String |
| PROP\_QUAL\_ARRAY             | 0000000a ffffffff ...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |



 

## PROP\_TYPE\_RAW\_DATA

The following table lists the generic format output for a **PROP\_TYPE\_RAW\_DATA** data type property. Be aware that the formatter output does not display the raw data, but does display the property label.



| Property qualifier            | Formatter output |
|-------------------------------|------------------|
| PROP\_QUAL\_NONE              | Property label.  |
| PROP\_QUAL\_RANGE             | Property label.  |
| PROP\_QUAL\_BITFIELD          | Property label.  |
| PROP\_QUAL\_LABELED\_SET      | Property label.  |
| PROP\_QUAL\_LABELED\_BITFIELD | Property label.  |
| PROP\_QUAL\_CONST             | Property label.  |
| PROP\_QUAL\_FLAGS             | Property label.  |
| PROP\_QUAL\_ARRAY             | Property label.  |



 

## PROP\_TYPE\_TIME

The following table lists the generic format output for a **PROP\_TYPE\_TIME** data type property. Be aware that the formatted output may vary depending on the data qualifier of the property.

The generic formatter calls [**GetDateFormat**](/windows/desktop/api/datetimeapi/nf-datetimeapi-getdateformata) to get a time that is based on the system clock of the local computer.



| Property qualifier            | Formatter output                                            |
|-------------------------------|-------------------------------------------------------------|
| PROP\_QUAL\_NONE              | Displays the system time based on the local computer clock. |
| PROP\_QUAL\_RANGE             | Displays the system time based on the local computer clock. |
| PROP\_QUAL\_BITFIELD          | Obsolete.                                                   |
| PROP\_QUAL\_LABELED\_SET      | Displays the system time based on the local computer clock. |
| PROP\_QUAL\_LABELED\_BITFIELD | Obsolete. For more information, see PROP\_QUAL\_FLAGS.      |
| PROP\_QUAL\_CONST             | Displays the system time based on the local computer clock. |
| PROP\_QUAL\_FLAGS             | Displays the system time based on the local computer clock. |
| PROP\_QUAL\_ARRAY             | Displays the system time based on the local computer clock. |



 

## PROP\_TYPE\_STRING

The following table lists the generic format output for **PROP\_TYPE\_STRING** data type properties. Be aware that the formatter output may vary depending on the data qualifier of the property.



| Property qualifier            | Formatter output                                       |
|-------------------------------|--------------------------------------------------------|
| PROP\_QUAL\_NONE              | Attached string.                                       |
| PROP\_QUAL\_RANGE             | Attached string.                                       |
| PROP\_QUAL\_BITFIELD          | Obsolete.                                              |
| PROP\_QUAL\_LABELED\_SET      | Attached string.                                       |
| PROP\_QUAL\_LABELED\_BITFIELD | Obsolete. For more information, see PROP\_QUAL\_FLAGS. |
| PROP\_QUAL\_CONST             | Attached string.                                       |
| PROP\_QUAL\_FLAGS             | Attached string.                                       |
| PROP\_QUAL\_ARRAY             | Attached string.                                       |



 

## PROP\_TYPE\_IP\_ADDRESS

The following table lists the generic format output for **PROP\_TYPE\_IP\_ADDRESS** data type properties. Be aware that the formatted output may vary depending on the property data qualifier of the property.

In the example output column, the value of the data in the capture is "129.65.100.2".



| Property qualifier            | Example output                                         |
|-------------------------------|--------------------------------------------------------|
| PROP\_QUAL\_NONE              | 129.65.100.2                                           |
| PROP\_QUAL\_RANGE             | 129.65.100.2                                           |
| PROP\_QUAL\_BITFIELD          | Obsolete.                                              |
| PROP\_QUAL\_LABELED\_SET      | 129.65.100.2                                           |
| PROP\_QUAL\_LABELED\_BITFIELD | Obsolete. For more information, see PROP\_QUAL\_FLAGS. |
| PROP\_QUAL\_CONST             | 129.65.100.2                                           |
| PROP\_QUAL\_FLAGS             | 129.65.100.2                                           |
| PROP\_QUAL\_ARRAY             | 129.65.100.2                                           |



 

 

