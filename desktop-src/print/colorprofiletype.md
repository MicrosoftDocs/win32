---
Description: The COLORPROFILETYPE enumeration is used to specify the type of color profile.
ms.assetid: 756ba822-ace2-4893-a989-9d355434e57c
title: COLORPROFILETYPE enumeration
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# COLORPROFILETYPE enumeration

The COLORPROFILETYPE enumeration is used to specify the type of color profile.

## Syntax


```C++
typedef enum  { 
  CPT_ICC   = 0,
  CPT_DMP   = 1,
  CPT_CAMP  = 2,
  CPT_GMMP  = 3
} COLORPROFILETYPE;
```



## Constants

<dl> <dt>

<span id="CPT_ICC"></span><span id="cpt_icc"></span>**CPT\_ICC**
</dt> <dd>

Specifies an ICC profile. If this value is specified, only the CPST\_RGB\_WORKING\_SPACE and CPST\_CUSTOM\_WORKING\_SPACE values of [**COLORPROFILESUBTYPE**](colorprofilesubtype.md) are valid.

</dd> <dt>

<span id="CPT_DMP"></span><span id="cpt_dmp"></span>**CPT\_DMP**
</dt> <dd>

Specifies a WCS device model profile (DMP). If this value is specified, only the CPST\_RGB\_WORKING\_SPACE and CPST\_CUSTOM\_WORKING\_SPACE values of [**COLORPROFILESUBTYPE**](colorprofilesubtype.md) are valid.

</dd> <dt>

<span id="CPT_CAMP"></span><span id="cpt_camp"></span>**CPT\_CAMP**
</dt> <dd>

Specifies a WCS color appearance model profile (CAMP). If this value is specified, only the CPST\_NONE value of [**COLORPROFILESUBTYPE**](colorprofilesubtype.md) is valid.

</dd> <dt>

<span id="CPT_GMMP"></span><span id="cpt_gmmp"></span>**CPT\_GMMP**
</dt> <dd>

Specifies a WCS gamut map model profile (GMMP). If this value is specified, only the CPST\_PERCEPTUAL, CPST\_SATURATION, CPST\_RELATIVE\_COLORIMETRIC, and CPST\_ABSOLUTE\_COLORIMETRIC values of [**COLORPROFILESUBTYPE**](colorprofilesubtype.md) are valid. Any one of these values may optionally be combined (in a bitwise OR operation) with CPST\_DEFAULT.

</dd> </dl>

## Remarks

The PCOLORPROFILETYPE and LPCOLORPROFILETYPE data types are defined as pointers to this enumeration:


```
typedef COLORPROFILETYPE *PCOLORPROFILETYPE, *LPCOLORPROFILETYPE;
```



## Requirements



|                    |                                                                                  |
|--------------------|----------------------------------------------------------------------------------|
| Version<br/> | Included in Windows Vista and later.<br/>                                  |
| Header<br/>  | <dl> <dt>Icm.h</dt> </dl> |



## See also

<dl> <dt>

[**COLORPROFILESUBTYPE**](colorprofilesubtype.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20COLORPROFILETYPE%20enumeration%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





