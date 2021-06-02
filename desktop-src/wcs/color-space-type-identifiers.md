---
title: Color Space Type Identifiers
description: These constants specify the type of a Postscript 2 color space array. The following values are valid color space array types.
ms.assetid: dc312db2-3bc5-461f-819c-37ff14cff896
topic_type:
- apiref
api_name:
- CSA_A
- CSA_GRAY
- CSA_ABC
- CSA_DEF
- CSA_RGB
- CSA_Lab
- CSA_DEFG
- CSA_CMYK
api_type:
- NA
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# Color Space Type Identifiers

These constants specify the type of a Postscript 2 color space array. The following values are valid color space array types.

<dl> <dt>

<span id="CSA_A"></span><span id="csa_a"></span>**CSA\_A**
</dt> <dd> <dl> <dt>



Get a CIEBasedA color space array from the monochrome profile.


</dt> </dl> </dd> <dt>

<span id="CSA_GRAY"></span><span id="csa_gray"></span>**CSA\_GRAY**
</dt> <dd> <dl> <dt>



Get a CIEBasedA color space array from the monochrome profile.


</dt> </dl> </dd> <dt>

<span id="CSA_ABC"></span><span id="csa_abc"></span>**CSA\_ABC**
</dt> <dd> <dl> <dt>



Get a CIEBasedABC color space array from the RGB or L<sup>\*</sup>a<sup>\*</sup>b profile.


</dt> </dl> </dd> <dt>

<span id="CSA_DEF"></span><span id="csa_def"></span>**CSA\_DEF**
</dt> <dd> <dl> <dt>



Get a CIEBasedDEF color space array from the RGB or L<sup>\*</sup>a<sup>\*</sup>b profile.


</dt> </dl> </dd> <dt>

<span id="CSA_RGB"></span><span id="csa_rgb"></span>**CSA\_RGB**
</dt> <dd> <dl> <dt>



Get a CIEBasedDEF color space array followed by a CIEBasedABC color space array from the RGB profile. On execution, if the printer doesn't support CIEBasedDEF color spaces, the function uses the CIEBasedABC definition.


</dt> </dl> </dd> <dt>

<span id="CSA_Lab"></span><span id="csa_lab"></span><span id="CSA_LAB"></span>**CSA\_Lab**
</dt> <dd> <dl> <dt>



Gets a CIEBasedABC color space array from the L<sup>\*</sup>a<sup>\*</sup>b profile.


</dt> </dl> </dd> <dt>

<span id="CSA_DEFG"></span><span id="csa_defg"></span>**CSA\_DEFG**
</dt> <dd> <dl> <dt>



Get a CIEBasedDEFG color space array from the CMYK profile.


</dt> </dl> </dd> <dt>

<span id="CSA_CMYK"></span><span id="csa_cmyk"></span>**CSA\_CMYK**
</dt> <dd> <dl> <dt>



Get a CIEBasedCMYK color space array from the CMYK profile.


</dt> </dl> </dd> </dl>

## See also

<dl> <dt>

[Basic color management concepts](basic-color-management-concepts.md)
</dt> <dt>

[ICM Constants](wcs-constants.md)
</dt> </dl>

 

 




