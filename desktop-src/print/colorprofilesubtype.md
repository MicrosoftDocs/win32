---
Description: 'The COLORPROFILESUBTYPE enumeration is used to specify the subtype of color profile.'
ms.assetid: '7ec0dd2d-7be5-4c85-8096-64a45aee01a5'
title: COLORPROFILESUBTYPE enumeration
---

# COLORPROFILESUBTYPE enumeration

The COLORPROFILESUBTYPE enumeration is used to specify the subtype of color profile.

## Syntax


```C++
typedef enum  { 
  CPST_PERCEPTUAL             = INTENT_PERCEPTUAL,
  CPST_RELATIVE_COLORIMETRIC  = INTENT_RELATIVE_COLORIMETRIC,
  CPST_SATURATION             = INTENT_SATURATION,
  CPST_ABSOLUTE_COLORIMETRIC  = INTENT_ABSOLUTE_COLORIMETRIC,
  CPST_NONE                   = 1,
  CPST_RGB_WORKING_SPACE      = 2,
  CPST_CUSTOM_WORKING_SPACE   = 3
} COLORPROFILESUBTYPE;
```



## Constants

<dl> <dt>

<span id="CPST_PERCEPTUAL"></span><span id="cpst_perceptual"></span>**CPST\_PERCEPTUAL**
</dt> <dd>

Specifies a perceptual rendering intent for WCS gamut map model profiles (GMMPs).

</dd> <dt>

<span id="CPST_RELATIVE_COLORIMETRIC"></span><span id="cpst_relative_colorimetric"></span>**CPST\_RELATIVE\_COLORIMETRIC**
</dt> <dd>

Specifies a relative colorimetric rendering intent for WCS GMMPs.

</dd> <dt>

<span id="CPST_SATURATION"></span><span id="cpst_saturation"></span>**CPST\_SATURATION**
</dt> <dd>

Specifies a saturation rendering intent for WCS GMMPs.

</dd> <dt>

<span id="CPST_ABSOLUTE_COLORIMETRIC"></span><span id="cpst_absolute_colorimetric"></span>**CPST\_ABSOLUTE\_COLORIMETRIC**
</dt> <dd>

Specifies an absolute colorimetric rendering intent for WCS GMMPs.

</dd> <dt>

<span id="CPST_NONE"></span><span id="cpst_none"></span>**CPST\_NONE**
</dt> <dd>

Specifies that the color profile subtype is not applicable to the selected color profile type.

</dd> <dt>

<span id="CPST_RGB_WORKING_SPACE"></span><span id="cpst_rgb_working_space"></span>**CPST\_RGB\_WORKING\_SPACE**
</dt> <dd>

Specifies the RGB color working space for ICC profiles or WCS device model profiles (DMPs).

</dd> <dt>

<span id="CPST_CUSTOM_WORKING_SPACE"></span><span id="cpst_custom_working_space"></span>**CPST\_CUSTOM\_WORKING\_SPACE**
</dt> <dd>

Specifies a custom color working space.

</dd> </dl>

## Remarks

For a description of rendering intents, see [Rendering Intents](http://go.microsoft.com/fwlink/p/?linkid=52269) in the Windows SDK documentation.

The PCOLORPROFILESUBTYPE and LPCOLORPROFILESUBTYPE data types are defined as pointers to this enumeration:


```
typedef COLORPROFILESUBTYPE *PCOLORPROFILESUBTYPE, *LPCOLORPROFILESUBTYPE;
```



## Requirements



|                    |                                                                                  |
|--------------------|----------------------------------------------------------------------------------|
| Version<br/> | Included in Windows Vista and later.<br/>                                  |
| Header<br/>  | <dl> <dt>Icm.h</dt> </dl> |



## See also

<dl> <dt>

[**COLORPROFILETYPE**](colorprofiletype.md)
</dt> <dt>

[**WcsSetDefaultColorProfile**](wcssetdefaultcolorprofile.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20COLORPROFILESUBTYPE%20enumeration%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





