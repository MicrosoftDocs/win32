---
title: Date and Time Conversion Functions
description: The following functions convert between dates and times stored in MS-DOS format and the Variant representation.
ms.assetid: 46ecf46e-dedf-4443-9fe9-f3c2c34d925d
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Date and Time Conversion Functions

The following functions convert between dates and times stored in MS-DOS format and the Variant representation.

## In this section



| Topic                                                                   | Description                                                                                                    |
|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [**DosDateTimeToVariantTime**](/windows/previous-versions/OleAuto/nf-oleauto-dosdatetimetovarianttime?branch=master)<br/> | Converts the MS-DOS representation of time to the date and time representation stored in a variant.<br/> |
| [**GetAltMonthNames**](/windows/previous-versions/OleAuto/nf-oleauto-getaltmonthnames?branch=master)<br/>                 | Retrieves the secondary (alternate) month names.<br/>                                                    |
| [**SystemTimeToVariantTime**](/windows/previous-versions/OleAuto/nf-oleauto-systemtimetovarianttime?branch=master)<br/>   | Converts a system time to a variant representation.<br/>                                                 |
| [**VarDateFromUdate**](/windows/previous-versions/OleAuto/nf-oleauto-vardatefromudate?branch=master)<br/>                 | Converts a time and date converted from MS-DOS format to variant format.<br/>                            |
| [**VarDateFromUdateEx**](/windows/previous-versions/OleAuto/nf-oleauto-vardatefromudateex?branch=master)<br/>             | Converts a time and date converted from MS-DOS format to variant format.<br/>                            |
| [**VariantTimeToDosDateTime**](/windows/previous-versions/OleAuto/nf-oleauto-varianttimetodosdatetime?branch=master)<br/> | Converts the variant representation of a date and time to MS-DOS date and time values.<br/>              |
| [**VariantTimeToSystemTime**](/windows/previous-versions/OleAuto/nf-oleauto-varianttimetosystemtime?branch=master)<br/>   | Converts the variant representation of time to system time values. <br/>                                 |
| [**VarUdateFromDate**](/windows/previous-versions/OleAuto/nf-oleauto-varudatefromdate?branch=master)<br/>                 | Converts a time and date converted from variant format to MS-DOS format. <br/>                           |



 

> [!Note]  
> If these functions are passed NULL pointers, there will be an access violation and the program will crash. It is your responsibility to protect these functions against NULL pointers.

 

## Related topics

<dl> <dt>

[Conversion and Manipulation Functions](conversion-and-manipulation-functions.md)
</dt> </dl>

 

 





