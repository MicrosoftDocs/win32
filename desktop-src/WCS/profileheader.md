---
title: PROFILEHEADER structure
description: The PROFILEHEADER structure contains information that describes the contents of a device profile file. This header occurs at the beginning of a device profile file.
ms.assetid: '7006cae0-0166-4fd9-8bf9-f0f0ed249956'
keywords: ["PROFILEHEADER structure Windows Color System"]
topic_type:
- apiref
api_name:
- PROFILEHEADER
api_location:
- Icm.h
api_type:
- HeaderDef
---

# PROFILEHEADER structure

The **PROFILEHEADER** structure contains information that describes the contents of a device profile file. This header occurs at the beginning of a device profile file.

## Syntax


```C++
typedef struct tagPROFILEHEADER {
  DWORD  phSize;
  DWORD  phCMMType;
  DWORD  phVersion;
  DWORD  phClass;
  DWORD  phDataColorSpace;
  DWORD  phConnectionSpace;
  DWORD  phDateTime[3];
  DWORD  phSignature;
  DWORD  phPlatform;
  DWORD  phProfileFlags;
  DWORD  phManufacturer;
  DWORD  phModel;
  DWORD  phAttributes[2];
  DWORD  phRenderingIntent;
  CIEXYZ phIlluminant;
  DWORD  phCreator;
  BYTE   phReserved[44];
} PROFILEHEADER;
```



## Members

<dl> <dt>

**phSize**
</dt> <dd>

The size of the profile in bytes.

</dd> <dt>

**phCMMType**
</dt> <dd>

The identification number of the CMM that is used in the profile. Identification numbers are registered with the ICC.

</dd> <dt>

**phVersion**
</dt> <dd>

The version number of the profile. The version number is determined by the ICC. The current major version number is 02h. The current minor version number is 10h. The major and minor version numbers are in binary coded decimal (BCD). They must be stored in the following format.



| Byte Number | Contents                                                                                                                  |
|-------------|---------------------------------------------------------------------------------------------------------------------------|
| 0           | Major version number in BCD.                                                                                              |
| 1           | Minor version number in the most significant nibble of this byte. Bug fix version number in the least significant nibble. |
| 2           | Reserved. Must be set to 0.                                                                                               |
| 3           | Reserved. Must be set to 0.                                                                                               |



 

</dd> <dt>

**phClass**
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

**phDataColorSpace**
</dt> <dd>

A signature value that indicates the color space in which the profile data is defined. The member can be any of value from the [Color Space Constants](color-space-constants.md).

</dd> <dt>

**phConnectionSpace**
</dt> <dd>

A signature value that indicates the color space in which the profile connection space (PCS) is defined. The member can be any of the following values.



| Profile Class | Signature  |
|---------------|------------|
| XYZ           | SPACE\_XYZ |
| Lab           | SPACE\_Lab |



 

When the **phClass** member is set to CLASS\_LINK, the PCS is taken from the **phDataColorSpace** member.

</dd> <dt>

**phDateTime**
</dt> <dd>

The data and time that the profile was created.

</dd> <dt>

**phSignature**
</dt> <dd>

Reserved for internal use.

</dd> <dt>

**phPlatform**
</dt> <dd>

The primary platform for which the profile was created. The primary platform can be set to any of the following values.



| Platform               | Value  |
|------------------------|--------|
| Apple Computer, Inc.   | 'APPL' |
| Microsoft Corp.        | 'MSFT' |
| Silicon Graphics, Inc. | 'SGI'  |
| Sun Microsystems, Inc. | 'SUNW' |
| Taligent               | 'TGNT' |



 

</dd> <dt>

**phProfileFlags**
</dt> <dd>

Bit flags containing hints that the CMM uses to interpret the profile data. The member can be set to the following values.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Constant</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>
<table>
<tbody>
<tr class="odd">
<td>FLAG_EMBEDDEDPROFILE</td>

</tr>
</tbody>
</table>

<p> </p></td>
<td>
<table>
<tbody>
<tr class="odd">
<td>The profile is embedded in a bitmap file.</td>

</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td>
<table>
<tbody>
<tr class="odd">
<td>FLAG_DEPENDENTONDATA</td>

</tr>
</tbody>
</table>

<p> </p></td>
<td>
<table>
<tbody>
<tr class="odd">
<td>The profile can't be used independently of the embedded color data. Used for profiles that are embedded in bitmap files.</td>

</tr>
</tbody>
</table>

<p> </p></td>
</tr>
</tbody>
</table>



 

</dd> <dt>

**phManufacturer**
</dt> <dd>

The identification number of the device profile manufacturer. All manufacturer identification numbers are registered with the ICC.

</dd> <dt>

**phModel**
</dt> <dd>

The device manufacturer's device model number. All model identification numbers are registered with the ICC.

</dd> <dt>

**phAttributes**
</dt> <dd>

Attributes of profile. The profile attributes can be any of the following values.



| Constant             | Meaning                                                                                  |
|----------------------|------------------------------------------------------------------------------------------|
| ATTRIB\_TRANSPARENCY | Turns transparency on. If this flag is not used, the attribute is reflective by default. |
| ATTRIB\_MATTE        | Turns matte display on. If this flag is not used, the attribute is glossy by default.    |



 

</dd> <dt>

**phRenderingIntent**
</dt> <dd>

The profile rendering intent. The member can be set to one of the following values:

INTENT\_PERCEPTUAL

 

INTENT\_SATURATION

 

INTENT\_RELATIVE\_COLORIMETRIC

 

INTENT\_ABSOLUTE\_COLORIMETRIC

For more information, see [Rendering Intents](rendering-intents.md).

</dd> <dt>

**phIlluminant**
</dt> <dd>

Profile illuminant.

</dd> <dt>

**phCreator**
</dt> <dd>

Signature of the software that created the profile. Signatures are registered with the ICC.

</dd> <dt>

**phReserved**
</dt> <dd>

Reservedfuture.

</dd> </dl>

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl> |



## See also

<dl> <dt>

[Further Information](further-information.md)
</dt> <dt>

[Using Device Profiles with WCS](using-device-profiles-with-wcs.md)
</dt> <dt>

[Rendering Intents](rendering-intents.md)
</dt> </dl>

 

 





