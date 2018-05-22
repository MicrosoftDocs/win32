---
title: COLORPROFILESUBTYPE enumeration
description: Specifies the subtype of the color profile.
ms.assetid: 'b5cc965e-47b2-4309-8558-5208c7a2b587'
keywords: ["COLORPROFILESUBTYPE enumeration Windows Color System", "COLORPROFILSUBTYPE enumeration Windows Color System", "COLORPROFILESUBTYPE PCOLORPROFILESUBTYPE enumeration pointer Windows Color System", "LPCOLORPROFILESUBTYPE enumeration pointer Windows Color System"]
topic_type:
- apiref
api_name:
- COLORPROFILSUBTYPE
api_location:
- Icm.h
api_type:
- HeaderDef
---

# COLORPROFILESUBTYPE enumeration

Specifies the subtype of the color profile.

## Syntax


```C++
typedef enum tagCOLORPROFILSUBTYPE { 
  CPST_NONE                   = 0x0000,
  CPST_RGB_WORKING_SPACE      = 0x0001,
  CPST_PERCEPTUAL             = 0x0002,
  CPST_ABSOLUTE_COLORIMETRIC  = 0x0004,
  CPST_RELATIVE_COLORIMETRIC  = 0x0008,
  CPST_SATURATION             = 0x0010,
  CPST_CUSTOM_WORKING_SPACE   = 0x0020
} COLORPROFILSUBTYPE, *COLORPROFILESUBTYPE PCOLORPROFILESUBTYPE, *LPCOLORPROFILESUBTYPE;
```



## Constants

<dl> <dt>

<span id="CPST_NONE"></span><span id="cpst_none"></span>**CPST\_NONE**
</dt> <dd>

The color profile subtype is not applicable to the selected color profile type.

</dd> <dt>

<span id="CPST_RGB_WORKING_SPACE"></span><span id="cpst_rgb_working_space"></span>**CPST\_RGB\_WORKING\_SPACE**
</dt> <dd>

The RGB color working space for International Color Consortium (ICC) profiles or device model profiles (DMPs) defined in WCS.

</dd> <dt>

<span id="CPST_PERCEPTUAL"></span><span id="cpst_perceptual"></span>**CPST\_PERCEPTUAL**
</dt> <dd>

A perceptual rendering intent for gamut map model profiles (GMMPs) defined in WCS.

</dd> <dt>

<span id="CPST_ABSOLUTE_COLORIMETRIC"></span><span id="cpst_absolute_colorimetric"></span>**CPST\_ABSOLUTE\_COLORIMETRIC**
</dt> <dd>

An absolute colorimetric rendering intent for GMMPs defined in WCS.

</dd> <dt>

<span id="CPST_RELATIVE_COLORIMETRIC"></span><span id="cpst_relative_colorimetric"></span>**CPST\_RELATIVE\_COLORIMETRIC**
</dt> <dd>

A relative colorimetric rendering intent for GMMPs defined in WCS.

</dd> <dt>

<span id="CPST_SATURATION"></span><span id="cpst_saturation"></span>**CPST\_SATURATION**
</dt> <dd>

A saturation rendering intent for GMMPs defined in WCS.

</dd> <dt>

<span id="CPST_CUSTOM_WORKING_SPACE"></span><span id="cpst_custom_working_space"></span>**CPST\_CUSTOM\_WORKING\_SPACE**
</dt> <dd>

A custom color working space.

</dd> </dl>

## Remarks

For a description of rendering intents, see [Rendering Intents](rendering-intents.md).

The PCOLORPROFILESUBTYPE and LPCOLORPROFILESUBTYPE data types are defined as pointers to the **COLORPROFILESUBTYPE** enumeration:

`typedef COLORPROFILESUBTYPE *PCOLORPROFILESUBTYPE, *LPCOLORPROFILESUBTYPE;`

The valid profile type/subtype combinations are



${ROWSPAN3}$ COLORPROFILETYPE<br/> ${REMOVE}$  

Valid COLORPROFILESUBTYPE<br/>

${ROWSPAN3}$ Notes<br/> ${REMOVE}$  

default for a device<br/>

global default<br/>

Intended Usage<br/>

Intended Usage<br/>

CPT\_ICC<br/>

CPST\_NONE<br/>

Get/Set default ICC profile associated with a device<br/>

CPST\_RGBWorkingSpace or CPST\_CustomWorkingSpace<br/>

Get/Set ICC profile as global RGB or custom working space<br/>

CPT\_DMP<br/>

CPST\_NONE<br/>

Get/Set default DMP profile associated with a device<br/>

CPST\_RGBWorkingSpace or CPST\_CustomWorkingSpace<br/>

Get/Set DMP as global RGB or custom working space<br/>

CPT\_CAMP<br/>

CPST\_NONE<br/>

Get/Set default CAMP profile associated with a device<br/>

CPST\_NONE<br/>

Get/Set CAMP profile as global color appearance profile<br/>

CPT\_GMMP<br/>

CPST\_NONE<br/>

Get/Set default GMMP profile associated with a device<br/>

CPST\_Perceptual or<br/> CPST\_Absolute\_colorimetric or<br/> CPST\_Relative\_colorimetric or<br/> CPTS\_Saturation<br/>

Get/Set GMMP as global gamut map model profile for a specific rendering intent as described by that subtype to be used in CreateMultiProfileTransform API when resolving the rendering intent array in WCS transform.<br/>

COLORPROFILESUBTYPE Global default can be or?d with WCS\_DEFAULT to set this GMMP as the global default for use in OpenColorProfile or WcsOpenColorProfile where GMMP is **NULL**.<br/>



 

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                   |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl> |



## See also

<dl> <dt>

[**COLORPROFILETYPE**](colorprofiletype.md)
</dt> <dt>

[**WcsSetDefaultColorProfile**](wcssetdefaultcolorprofile.md)
</dt> </dl>

 

 





