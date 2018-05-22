---
title: COLORPROFILETYPE enumeration
description: Specifies the type of color profile.
ms.assetid: 'aaf6fd19-0693-4a76-812f-ff958eb5c944'
keywords: ["COLORPROFILETYPE enumeration Windows Color System", "PCOLORPROFILETYPE enumeration pointer Windows Color System", "LPCOLORPROFILETYPE enumeration pointer Windows Color System"]
topic_type:
- apiref
api_name:
- COLORPROFILETYPE
api_location:
- Icm.h
api_type:
- HeaderDef
---

# COLORPROFILETYPE enumeration

Specifies the type of color profile.

## Syntax


```C++
typedef enum tagCOLORPROFILETYPE { 
  CPT_ICC   = 0x0001,
  CPT_DMP,
  CPT_CAMP,
  CPT_GMMP
} COLORPROFILETYPE, *PCOLORPROFILETYPE, *LPCOLORPROFILETYPE;
```



## Constants

<dl> <dt>

<span id="CPT_ICC"></span><span id="cpt_icc"></span>**CPT\_ICC**
</dt> <dd>

An International Color Consortium (ICC) profile. If you specify this value, only the CPST\_RGB\_WORKING\_SPACE and CPST\_CUSTOM\_WORKING\_SPACE values of [**COLORPROFILESUBTYPE**](colorprofilesubtype.md) are valid.

</dd> <dt>

<span id="CPT_DMP"></span><span id="cpt_dmp"></span>**CPT\_DMP**
</dt> <dd>

A device model profile (DMP) defined in WCS. If you specify this value, only the CPST\_RGB\_WORKING\_SPACE and CPST\_CUSTOM\_WORKING\_SPACE values of [**COLORPROFILESUBTYPE**](colorprofilesubtype.md) are valid.

</dd> <dt>

<span id="CPT_CAMP"></span><span id="cpt_camp"></span>**CPT\_CAMP**
</dt> <dd>

A color appearance model profile (CAMP) defined in WCS. If you specify this value, only the CPST\_NONE value of [**COLORPROFILESUBTYPE**](colorprofilesubtype.md) is valid.

</dd> <dt>

<span id="CPT_GMMP"></span><span id="cpt_gmmp"></span>**CPT\_GMMP**
</dt> <dd>

Specifies a WCS gamut map model profile (GMMP). If this value is specified, only the CPST\_PERCEPTUAL, CPST\_SATURATION, CPST\_RELATIVE\_COLORIMETRIC, and CPST\_ABSOLUTE\_COLORIMETRIC values of [**COLORPROFILESUBTYPE**](colorprofilesubtype.md) are valid. Any of these values may optionally be combined (in a bitwise **OR** operation) with CPST\_DEFAULT.

</dd> </dl>

## Remarks

The PCOLORPROFILETYPE and LPCOLORPROFILETYPE data types are defined as pointers to this enumeration:

`typedef COLORPROFILETYPE *PCOLORPROFILETYPE, *LPCOLORPROFILETYPE;`

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                   |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl> |



## See also

<dl> <dt>

[**COLORPROFILESUBTYPE**](colorprofilesubtype.md)
</dt> </dl>

 

 





