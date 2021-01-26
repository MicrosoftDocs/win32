---
title: ENUMTYPE structure
description: The ENUMTYPE structure contains information that defines the profile enumeration constraints.
ms.assetid: 9c1065ad-00ac-4f5c-b738-090e38e1516f
keywords:
- ENUMTYPE structure Windows Color System
- PENUMTYPE structure pointer Windows Color System
- LPENUMTYPE structure pointer Windows Color System
topic_type:
- apiref
api_name:
- ENUMTYPE
api_location:
- Icm.h
api_type:
- HeaderDef
ms.localizationpriority: high


ms.topic: structure
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# ENUMTYPE structure

The **ENUMTYPE** structure contains information that defines the profile enumeration constraints.

## Syntax


```C++
typedef struct tagENUMTYPE {
  DWORD  dwSize;
  DWORD  dwVersion;
  DWORD  dwFields;
  PCTSTR pDeviceName;
  DWORD  dwMediaType;
  DWORD  dwDitheringMode;
  DWORD  dwResolution[2];
  DWORD  dwCMMType;
  DWORD  dwClass;
  DWORD  dwDataColorSpace;
  DWORD  dwConnectionSpace;
  DWORD  dwSignature;
  DWORD  dwPlatform;
  DWORD  dwProfileFlags;
  DWORD  dwManufacturer;
  DWORD  dwModel;
  DWORD  dwAttributes[2];
  DWORD  dwRenderingIntent;
  DWORD  dwCreator;
  DWORD  dwDeviceClass;
} ENUMTYPE, *PENUMTYPE, *LPENUMTYPE;
```



## Members

<dl> <dt>

**dwSize**
</dt> <dd>

The size of this structure in bytes.

</dd> <dt>

**dwVersion**
</dt> <dd>

The version number of the **ENUMTYPE** structure. Should be set to ENUM\_TYPE\_VERSION.

</dd> <dt>

**dwFields**
</dt> <dd>

Indicates which fields in this structure are being used. Can be set to any combination of the following constant values.

ET\_DEVICENAME

 

ET\_MEDIATYPE

 

ET\_DITHERMODE

 

ET\_RESOLUTION

 

ET\_CMMTYPE

 

ET\_CLASS

 

ET\_DATACOLORSPACE

 

ET\_CONNECTIONSPACE

 

ET\_SIGNATURE

 

ET\_PLATFORM

 

ET\_PROFILEFLAGS

 

ET\_MANUFACTURER

 

ET\_MODEL

 

ET\_ATTRIBUTES

 

ET\_RENDERINGINTENT

 

ET\_CREATOR

 

ET\_DEVICECLASS

</dd> <dt>

**pDeviceName**
</dt> <dd>

User friendly name of the device.

</dd> <dt>

**dwMediaType**
</dt> <dd>

Indicates which type of media is associated with the profile, such as a printer or screen.

</dd> <dt>

**dwDitheringMode**
</dt> <dd>

Indicates the style of dithering that will be used when an image is displayed.

</dd> <dt>

**dwResolution**
</dt> <dd>

The horizontal (x) and vertical (y) resolution in pixels of the device on which the image will be displayed. The x resolution is stored in **dwResolution\[0\]**, and the y resolution is kept in **dwResolution\[1\]**.

</dd> <dt>

**dwCMMType**
</dt> <dd>

The identification number of the CMM that is used in the profile. Identification numbers are registered with the ICC.

</dd> <dt>

**dwClass**
</dt> <dd>

Indicates the profile class. For a description of profile classes, see [Using Device Profiles with WCS](using-device-profiles-with-wcs.md). A profile class may have any of the following values.



| Profile Class                  | Signature         |
|--------------------------------|-------------------|
| Input Device Profile           | CLASS\_SCANNER    |
| Display Device Profile         | CLASS\_MONITOR    |
| Output Device Profile          | CLASS\_PRINTER    |
| Device Link Profile            | CLASS\_LINK       |
| Color Space Conversion Profile | CLASS\_COLORSPACE |
| Abstract Profile               | CLASS\_ABSTRACT   |
| Named Color Profile            | CLASS\_NAMED      |
| Color Appearance Model Profile | CLASS\_CAMP       |
| Color Gamut Map Model Profile  | CLASS\_GMMP       |



 

</dd> <dt>

**dwDataColorSpace**
</dt> <dd>

A signature value that indicates the color space in which the profile data is defined. Can be any value from the [Color Space Constants](color-space-constants.md).

</dd> <dt>

**dwConnectionSpace**
</dt> <dd>

A signature value that indicates the color space in which the profile connection space (PCS) is defined. Can be any of the following values.



| Profile Class | Signature  |
|---------------|------------|
| XYZ           | SPACE\_XYZ |
| Lab           | SPACE\_Lab |



 

When the **dwClass** member is set to CLASS\_LINK, the PCS is taken from the **dwDataColorSpace** member.

</dd> <dt>

**dwSignature**
</dt> <dd>

Reserved for internal use.

</dd> <dt>

**dwPlatform**
</dt> <dd>

The primary platform for which the profile was created. The member can be set to any of the following values.



| Platform               | Value  |
|------------------------|--------|
| Apple Computer, Inc.   | 'APPL' |
| Microsoft Corp.        | 'MSFT' |
| Silicon Graphics, Inc. | 'SGI'  |
| Sun Microsystems, Inc. | 'SUNW' |
| Taligent               | 'TGNT' |



 

</dd> <dt>

**dwProfileFlags**
</dt> <dd>

Bit flags containing hints that the CMM uses to interpret the profile data and can be set to one of the following values.



| Constant              | Meaning                                                                                                                  |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------|
| FLAG\_EMBEDDEDPROFILE | The profile is embedded in a bitmap file.                                                                                |
| FLAG\_DEPENDENTONDATA | The profile can't be used independently of the embedded color data. Used for profiles that are embedded in bitmap files. |



 

</dd> <dt>

**dwManufacturer**
</dt> <dd>

The identification number of the device profile manufacturer. All manufacturer identification numbers are registered with the ICC.

</dd> <dt>

**dwModel**
</dt> <dd>

The device manufacturer's device model number. All model identification numbers are registered with the ICC.

</dd> <dt>

**dwAttributes**
</dt> <dd>

Attributes of profile that can be any of the following values.



| Constant             | Meaning                                                                                  |
|----------------------|------------------------------------------------------------------------------------------|
| ATTRIB\_TRANSPARENCY | Turns transparency on. If this flag is not used, the attribute is reflective by default. |
| ATTRIB\_MATTE        | Turns matte display on. If this flag is not used, the attribute is glossy by default.    |



 

</dd> <dt>

**dwRenderingIntent**
</dt> <dd>

The profile rendering intent that can be set to one of the following values:

INTENT\_PERCEPTUAL

 

INTENT\_SATURATION

 

INTENT\_RELATIVE\_COLORIMETRIC

 

INTENT\_ABSOLUTE\_COLORIMETRIC

For more information, see [Rendering Intents](rendering-intents.md).

</dd> <dt>

**dwCreator**
</dt> <dd>

Signature of the software that created the profile. Signatures are registered with the ICC.

</dd> <dt>

**dwDeviceClass**
</dt> <dd>

Indicates the device class. A device class may have one of the following values.



| Profile Class          | Signature      |
|------------------------|----------------|
| Input Device Profile   | CLASS\_SCANNER |
| Display Device Profile | CLASS\_MONITOR |
| Output Device Profile  | CLASS\_PRINTER |



 

</dd> </dl>

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl> |



## See also

<dl> <dt>

[Further Information](further-information.md)
</dt> <dt>

[Using Device Profiles with WCS](using-device-profiles-with-wcs.md)
</dt> <dt>

[Rendering Intents](rendering-intents.md)
</dt> </dl>

 

 





