---
title: Property item descriptions
description: The following list gives descriptions of the property items supported by Windows GDI+.
ms.assetid: fc95aa3f-8381-430d-8cbf-6d23816a738d
ms.topic: article
ms.date: 02/22/2022
---

# Property item descriptions

The following list gives descriptions of the property items supported by Windows GDI+. The descriptions are brief and general so that they apply to a variety of image file formats. For a detailed description of how a property item is used by a particular file format, see the specification for that file format. For links to several file specifications and other documents that describe metadata in detail, see [Image File Format Specifications](-gdiplus-constant-image-file-format-specifications.md).

The Exchangeable Image File (EXIF) format is a Japan Electronic Industry Development Association (JEIDA) standard, revised June 1998 as version 2.1. Portions of the EXIF specification are used with permission of JEIDA.

The types in the `Type` column are described in [Image property tag type constants](/windows/win32/gdiplus/-gdiplus-constant-image-property-tag-type-constants).

## PropertyTagGpsVer

Version of the Global Positioning Systems (GPS) IFD, given as 2.0.0.0. This tag is mandatory when the PropertyTagGpsIFD tag is present. When the version is 2.0.0.0, the tag value is 0x02000000.

| Property info | Value |
|-------|---------------------|
| Tag   | 0x0000              |
| Type  | PropertyTagTypeByte |
| Count | 4                   |

## PropertyTagGpsLatitudeRef

Null-terminated character string that specifies whether the latitude is north or south. `N` specifies north latitude, and `S` specifies south latitude.

| Property info | Value |
|-------|--------------------------------------------|
| Tag   | 0x0001                                     |
| Type  | PropertyTagTypeASCII                       |
| Count | 2 (one character plus the NULL terminator) |

## PropertyTagGpsLatitude

Latitude. Latitude is expressed as three rational values giving the degrees, minutes, and seconds respectively. When degrees, minutes, and seconds are expressed, the format is dd/1, mm/1, ss/1. When degrees and minutes are used and, for example, fractions of minutes are given up to two decimal places, the format is dd/1, mmmm/100, 0/1.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x0002                  |
| Type  | PropertyTagTypeRational |
| Count | 3                       |

## PropertyTagGpsLongitudeRef

Null-terminated character string that specifies whether the longitude is east or west longitude. `E` specifies east longitude, and `W` specifies west longitude.

| Property info | Value |
|-------|--------------------------------------------|
| Tag   | 0x0003                                     |
| Type  | PropertyTagTypeASCII                       |
| Count | 2 (one character plus the NULL terminator) |

## PropertyTagGpsLongitude

Longitude. Longitude is expressed as three rational values giving the degrees, minutes, and seconds respectively. When degrees, minutes and seconds are expressed, the format is ddd/1, mm/1, ss/1. When degrees and minutes are used and, for example, fractions of minutes are given up to two decimal places, the format is ddd/1, mmmm/100, 0/1.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x0004                  |
| Type  | PropertyTagTypeRational |
| Count | 3                       |

## PropertyTagGpsAltitudeRef

Reference altitude, in meters.

| Property info | Value |
|-------|---------------------|
| Tag   | 0x0005              |
| Type  | PropertyTagTypeByte |
| Count | 1                   |

## PropertyTagGpsAltitude

Altitude, in meters, based on the reference altitude specified by PropertyTagGpsAltitudeRef.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x0006                  |
| Type  | PropertyTagTypeRational |
| Count | 1                       |

## PropertyTagGpsGpsTime

Time as Coordinated Universal Time (UTC). The value is expressed as three rational numbers that give the hour, minute, and second.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x0007                  |
| Type  | PropertyTagTypeRational |
| Count | 3                       |

## PropertyTagGpsGpsSatellites

Null-terminated character string that specifies the GPS satellites used for measurements. This tag can be used to specify the ID number, angle of elevation, azimuth, SNR, and other information about each satellite. The format is not specified. If the GPS receiver is incapable of taking measurements, the value of the tag must be set to **NULL**.

| Property info | Value |
|-------|----------------------------------------------------|
| Tag   | 0x0008                                             |
| Type  | PropertyTagTypeASCII                               |
| Count | Length of the string including the NULL terminator |

## PropertyTagGpsGpsStatus

Null-terminated character string that specifies the status of the GPS receiver when the image is recorded. `A` means measurement is in progress, and `V` means the measurement is Interoperability.

| Property info | Value |
|-------|--------------------------------------------|
| Tag   | 0x0009                                     |
| Type  | PropertyTagTypeASCII                       |
| Count | 2 (one character plus the NULL terminator) |

## PropertyTagGpsGpsMeasureMode

Null-terminated character string that specifies the GPS measurement mode. `2` specifies 2-D measurement, and `3` specifies 3-D measurement.

| Property info | Value |
|-------|--------------------------------------------|
| Tag   | 0x000A                                     |
| Type  | PropertyTagTypeASCII                       |
| Count | 2 (one character plus the NULL terminator) |

## PropertyTagGpsGpsDop

GPS DOP (data degree of precision). An HDOP value is written during 2-D measurement, and a PDOP value is written during 3-D measurement.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x000B                  |
| Type  | PropertyTagTypeRational |
| Count | 1                       |

## PropertyTagGpsSpeedRef

Null-terminated character string that specifies the unit used to express the GPS receiver speed of movement. `K`, `M`, and `N` represent kilometers per hour, miles per hour, and knots respectively.

| Property info | Value |
|-------|--------------------------------------------|
| Tag   | 0x000C                                     |
| Type  | PropertyTagTypeASCII                       |
| Count | 2 (one character plus the NULL terminator) |

## PropertyTagGpsSpeed

Speed of the GPS receiver movement.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x000D                  |
| Type  | PropertyTagTypeRational |
| Count | 1                       |

## PropertyTagGpsTrackRef

Null-terminated character string that specifies the reference for giving the direction of GPS receiver movement. `T` specifies true direction, and `M` specifies magnetic direction.

| Property info | Value |
|-------|--------------------------------------------|
| Tag   | 0x000E                                     |
| Type  | PropertyTagTypeASCII                       |
| Count | 2 (one character plus the NULL terminator) |

## PropertyTagGpsTrack

Direction of GPS receiver movement. The range of values is from 0.00 to 359.99.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x000F                  |
| Type  | PropertyTagTypeRational |
| Count | 1                       |

## PropertyTagGpsImgDirRef

Null-terminated character string that specifies the reference for the direction of the image when it is captured. `T` specifies true direction, and `M` specifies magnetic direction.

| Property info | Value |
|-------|--------------------------------------------|
| Tag   | 0x0010                                     |
| Type  | PropertyTagTypeASCII                       |
| Count | 2 (one character plus the NULL terminator) |

## PropertyTagGpsImgDir

Direction of the image when it was captured. The range of values is from 0.00 to 359.99.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x0011                  |
| Type  | PropertyTagTypeRational |
| Count | 1                       |

## PropertyTagGpsMapDatum

Null-terminated character string that specifies geodetic survey data used by the GPS receiver. If the survey data is restricted to Japan, the value of this tag is `TOKYO` or `WGS-84`.

| Property info | Value |
|-------|----------------------------------------------------|
| Tag   | 0x0012                                             |
| Type  | PropertyTagTypeASCII                               |
| Count | Length of the string including the NULL terminator |

## PropertyTagGpsDestLatRef

Null-terminated character string that specifies whether the latitude of the destination point is north or south latitude. `N` specifies north latitude, and `S` specifies south latitude.

| Property info | Value |
|-------|--------------------------------------------|
| Tag   | 0x0013                                     |
| Type  | PropertyTagTypeASCII                       |
| Count | 2 (one character plus the NULL terminator) |

## PropertyTagGpsDestLat

Latitude of the destination point. The latitude is expressed as three rational values giving the degrees, minutes, and seconds respectively. When degrees, minutes, and seconds are expressed, the format is dd/1, mm/1, ss/1. When degrees and minutes are used and, for example, fractions of minutes are given up to two decimal places, the format is dd/1, mmmm/100, 0/1.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x0014                  |
| Type  | PropertyTagTypeRational |
| Count | 3                       |

## PropertyTagGpsDestLongRef

Null-terminated character string that specifies whether the longitude of the destination point is east or west longitude. `E` specifies east longitude, and `W` specifies west longitude.

| Property info | Value |
|-------|--------------------------------------------|
| Tag   | 0x0015                                     |
| Type  | PropertyTagTypeASCII                       |
| Count | 2 (one character plus the NULL terminator) |

## PropertyTagGpsDestLong

Longitude of the destination point. The longitude is expressed as three rational values giving the degrees, minutes, and seconds respectively. When degrees, minutes, and seconds are expressed, the format is ddd/1, mm/1, ss/1. When degrees and minutes are used and, for example, fractions of minutes are given up to two decimal places, the format is ddd/1, mmmm/100, 0/1.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x0016                  |
| Type  | PropertyTagTypeRational |
| Count | 3                       |

## PropertyTagGpsDestBearRef

Null-terminated character string that specifies the reference used for giving the bearing to the destination point. `T` specifies true direction, and `M` specifies magnetic direction.

| Property info | Value |
|-------|--------------------------------------------|
| Tag   | 0x0017                                     |
| Type  | PropertyTagTypeASCII                       |
| Count | 2 (one character plus the NULL terminator) |

## PropertyTagGpsDestBear

Bearing to the destination point. The range of values is from 0.00 to 359.99.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x0018                  |
| Type  | PropertyTagTypeRational |
| Count | 1                       |

## PropertyTagGpsDestDistRef

Null-terminated character string that specifies the unit used to express the distance to the destination point. K, M, and N represent kilometers, miles, and knots respectively.

| Property info | Value |
|-------|--------------------------------------------|
| Tag   | 0x0019                                     |
| Type  | PropertyTagTypeASCII                       |
| Count | 2 (one character plus the NULL terminator) |

## PropertyTagGpsDestDist

Distance to the destination point.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x001A                  |
| Type  | PropertyTagTypeRational |
| Count | 1                       |

## PropertyTagNewSubfileType

Type of data in a subfile.

| Property info | Value |
|-------|---------------------|
| Tag   | 0x00FE              |
| Type  | PropertyTagTypeLong |
| Count | 1                   |

## PropertyTagSubfileType

Type of data in a subfile.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x00FF               |
| Type  | PropertyTagTypeShort |
| Count | 1                    |

## PropertyTagImageWidth

Number of pixels per row.

| Property info | Value |
|-------|---------------------------------------------|
| Tag   | 0x0100                                      |
| Type  | PropertyTagTypeShort or PropertyTagTypeLong |
| Count | 1                                           |

## PropertyTagImageHeight

Number of pixel rows.

| Property info | Value |
|-------|---------------------------------------------|
| Tag   | 0x0101                                      |
| Type  | PropertyTagTypeShort or PropertyTagTypeLong |
| Count | 1                                           |

## PropertyTagBitsPerSample

Number of bits per color component. See also [PropertyTagSamplesPerPixel](#propertytagsamplesperpixel).

| Property info | Value |
|-------|------------------------------------------|
| Tag   | 0x0102                                   |
| Type  | PropertyTagTypeShort                     |
| Count | Number of samples (components) per pixel |

## PropertyTagCompression

Compression scheme used for the image data.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x0103               |
| Type  | PropertyTagTypeShort |
| Count | 1                    |

## PropertyTagPhotometricInterp

How pixel data will be interpreted.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x0106               |
| Type  | PropertyTagTypeShort |
| Count | 1                    |

## PropertyTagThreshHolding

Technique used to convert from gray pixels to black and white pixels.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x0107               |
| Type  | PropertyTagTypeShort |
| Count | 1                    |

## PropertyTagCellWidth

Width of the dithering or halftoning matrix.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x0108               |
| Type  | PropertyTagTypeShort |
| Count | 1                    |

## PropertyTagCellHeight

Height of the dithering or halftoning matrix.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x0109               |
| Type  | PropertyTagTypeShort |
| Count | 1                    |

## PropertyTagFillOrder

Logical order of bits in a byte.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x010A               |
| Type  | PropertyTagTypeShort |
| Count | 1                    |

## PropertyTagDocumentName

Null-terminated character string that specifies the name of the document from which the image was scanned.

| Property info | Value |
|-------|----------------------------------------------------|
| Tag   | 0x010D                                             |
| Type  | PropertyTagTypeASCII                               |
| Count | Length of the string including the NULL terminator |

## PropertyTagImageDescription

Null-terminated character string that specifies the title of the image.

| Property info | Value |
|-------|----------------------------------------------------|
| Tag   | 0x010E                                             |
| Type  | PropertyTagTypeASCII                               |
| Count | Length of the string including the NULL terminator |

## PropertyTagEquipMake

Null-terminated character string that specifies the manufacturer of the equipment used to record the image.

| Property info | Value |
|-------|----------------------------------------------------|
| Tag   | 0x010F                                             |
| Type  | PropertyTagTypeASCII                               |
| Count | Length of the string including the NULL terminator |

## PropertyTagEquipModel

Null-terminated character string that specifies the model name or model number of the equipment used to record the image.

| Property info | Value |
|-------|----------------------------------------------------|
| Tag   | 0x0110                                             |
| Type  | PropertyTagTypeASCII                               |
| Count | Length of the string including the NULL terminator |

## PropertyTagStripOffsets

For each strip, the byte offset of that strip. See also [PropertyTagRowsPerStrip](#propertytagrowsperstrip) and [PropertyTagStripBytesCount](#propertytagstripbytescount).

| Property info | Value |
|-------|---------------------------------------------|
| Tag   | 0x0111                                      |
| Type  | PropertyTagTypeShort or PropertyTagTypeLong |
| Count | Number of strips                            |

## PropertyTagOrientation

Image orientation viewed in terms of rows and columns.

| Property info | Value |
|-------|---------------------------------------------|
| Tag   | 0x0112                                      |
| Type  | PropertyTagTypeShort |
| Count | 1                            |

1 - The 0th row is at the top of the visual image, and the 0th column is the visual left side. <br/>2 - The 0th row is at the visual top of the image, and the 0th column is the visual right side. <br/>3 - The 0th row is at the visual bottom of the image, and the 0th column is the visual right side. <br/>4 - The 0th row is at the visual bottom of the image, and the 0th column is the visual left side. <br/>5 - The 0th row is the visual left side of the image, and the 0th column is the visual top. <br/>6 - The 0th row is the visual right side of the image, and the 0th column is the visual top. <br/>7 - The 0th row is the visual right side of the image, and the 0th column is the visual bottom. <br/>8 - The 0th row is the visual left side of the image, and the 0th column is the visual bottom.

## PropertyTagSamplesPerPixel

Number of color components per pixel.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x0115               |
| Type  | PropertyTagTypeShort |
| Count | 1                    |

## PropertyTagRowsPerStrip

Number of rows per strip. See also [PropertyTagStripBytesCount](#propertytagstripbytescount) and [PropertyTagStripOffsets](#propertytagstripoffsets).

| Property info | Value |
|-------|---------------------------------------------|
| Tag   | 0x0116                                      |
| Type  | PropertyTagTypeShort or PropertyTagTypeLong |
| Count | 1                                           |

## PropertyTagStripBytesCount

For each strip, the total number of bytes in that strip.

| Property info | Value |
|-------|---------------------------------------------|
| Tag   | 0x0117                                      |
| Type  | PropertyTagTypeShort or PropertyTagTypeLong |
| Count | Number of strips                            |

## PropertyTagMinSampleValue

For each color component, the minimum value assigned to that component. See also [PropertyTagSamplesPerPixel](#propertytagsamplesperpixel).

| Property info | Value |
|-------|------------------------------------------|
| Tag   | 0x0118                                   |
| Type  | PropertyTagTypeShort                     |
| Count | Number of samples (components) per pixel |

## PropertyTagMaxSampleValue

For each color component, the maximum value assigned to that component. See also [PropertyTagSamplesPerPixel](#propertytagsamplesperpixel).

| Property info | Value |
|-------|------------------------------------------|
| Tag   | 0x0119                                   |
| Type  | PropertyTagTypeShort                     |
| Count | Number of samples (components) per pixel |

## PropertyTagXResolution

Number of pixels per unit in the image width (x) direction. The unit is specified by [PropertyTagResolutionUnit](#propertytagresolutionunit).

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x011A                  |
| Type  | PropertyTagTypeRational |
| Count | 1                       |

## PropertyTagYResolution

Number of pixels per unit in the image height (y) direction. The unit is specified by [PropertyTagResolutionUnit](#propertytagresolutionunit).

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x011B                  |
| Type  | PropertyTagTypeRational |
| Count | 1                       |

## PropertyTagPlanarConfig

Whether pixel components are recorded in chunky or planar format.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x011C               |
| Type  | PropertyTagTypeShort |
| Count | 1                    |

## PropertyTagPageName

Null-terminated character string that specifies the name of the page from which the image was scanned.

| Property info | Value |
|-------|----------------------------------------------------|
| Tag   | 0x011D                                             |
| Type  | PropertyTagTypeASCII                               |
| Count | Length of the string including the NULL terminator |

## PropertyTagXPosition

Offset from the left side of the page to the left side of the image. The unit of measure is specified by [PropertyTagResolutionUnit](#propertytagresolutionunit).

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x011E                  |
| Type  | PropertyTagTypeRational |
| Count | 1                       |

## PropertyTagYPosition

Offset from the top of the page to the top of the image. The unit of measure is specified by [PropertyTagResolutionUnit](#propertytagresolutionunit).

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x011F                  |
| Type  | PropertyTagTypeRational |
| Count | 1                       |

## PropertyTagFreeOffset

For each string of contiguous unused bytes, the byte offset of that string.

| Property info | Value |
|------|---------------------|
| Tag  | 0x0120              |
| Type | PropertyTagTypeLong |

## PropertyTagFreeByteCounts

For each string of contiguous unused bytes, the number of bytes in that string.

| Property info | Value |
|-------|-----------------------------------------------|
| Tag   | 0x0121                                        |
| Type  | PropertyTagTypeLong                           |
| Count | Number of strings of contiguous unused bytes. |

## PropertyTagGrayResponseUnit

Precision of the number specified by PropertyTagGrayResponseCurve. 1 specifies tenths, 2 specifies hundredths, 3 specifies thousandths, and so on.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x0122               |
| Type  | PropertyTagTypeShort |
| Count | 1                    |

## PropertyTagGrayResponseCurve

For each possible pixel value in a grayscale image, the optical density of that pixel value.

| Property info | Value |
|-------|---------------------------------|
| Tag   | 0x0123                          |
| Type  | PropertyTagTypeShort            |
| Count | Number of possible pixel values |

## PropertyTagT4Option

Set of flags that relate to T4 encoding.

| Property info | Value |
|-------|---------------------|
| Tag   | 0x0124              |
| Type  | PropertyTagTypeLong |
| Count | 1                   |

## PropertyTagT6Option

Set of flags that relate to T6 encoding.

| Property info | Value |
|-------|---------------------|
| Tag   | 0x0125              |
| Type  | PropertyTagTypeLong |
| Count | 1                   |

## PropertyTagResolutionUnit

Unit of measure for the horizontal resolution and the vertical resolution.

| Property info | Value |
|-------|---------------------|
| Tag   | 0x0128              |
| Type  | PropertyTagTypeShort |
| Count | 1|

2 - inch<br/>3 - centimeter

## PropertyTagPageNumber

Page number of the page from which the image was scanned.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x0129               |
| Type  | PropertyTagTypeShort |
| Count | 1                    |

## PropertyTagTransferFunction

Tables that specify transfer functions for the image.

| Property info | Value |
|-------|------------------------------------------------------|
| Tag   | 0x012D                                               |
| Type  | PropertyTagTypeShort                                 |
| Count | Total number of 16-bit words required for the tables |

## PropertyTagSoftwareUsed

Null-terminated character string that specifies the name and version of the software or firmware of the device used to generate the image.

| Property info | Value |
|-------|----------------------------------------------------|
| Tag   | 0x0131                                             |
| Type  | PropertyTagTypeASCII                               |
| Count | Length of the string including the NULL terminator |

## PropertyTagDateTime

Date and time the image was created.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x0132               |
| Type  | PropertyTagTypeASCII |
| Count | 20                   |

## PropertyTagArtist

Null-terminated character string that specifies the name of the person who created the image.

| Property info | Value |
|-------|----------------------------------------------------|
| Tag   | 0x013B                                             |
| Type  | PropertyTagTypeASCII                               |
| Count | Length of the string including the NULL terminator |

## PropertyTagHostComputer

Null-terminated character string that specifies the computer and/or operating system used to create the image.

| Property info | Value |
|-------|----------------------------------------------------|
| Tag   | 0x013C                                             |
| Type  | PropertyTagTypeASCII                               |
| Count | Length of the string including the NULL terminator |

## PropertyTagPredictor

Type of prediction scheme that was applied to the image data before the encoding scheme was applied.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x013D               |
| Type  | PropertyTagTypeShort |
| Count | 1                    |

## PropertyTagWhitePoint

Chromaticity of the white point of the image.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x013E                  |
| Type  | PropertyTagTypeRational |
| Count | 2                       |

## PropertyTagPrimaryChromaticities

For each of the three primary colors in the image, the chromaticity of that color.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x013F                  |
| Type  | PropertyTagTypeRational |
| Count | 6                       |

## PropertyTagColorMap

Color palette (lookup table) for a palette-indexed image.

| Property info | Value |
|-------|-------------------------------------------------|
| Tag   | 0x0140                                          |
| Type  | PropertyTagTypeShort                            |
| Count | Number of 16-bit words required for the palette |

## PropertyTagHalftoneHints

Information used by the halftone function

| Property info | Value |
|-------|----------------------|
| Tag   | 0x0141               |
| Type  | PropertyTagTypeShort |
| Count | 2                    |

## PropertyTagTileWidth

Number of pixel columns in each tile.

| Property info | Value |
|-------|---------------------------------------------|
| Tag   | 0x0142                                      |
| Type  | PropertyTagTypeShort or PropertyTagTypeLong |
| Count | 1                                           |

## PropertyTagTileLength

Number of pixel rows in each tile.

| Property info | Value |
|-------|---------------------------------------------|
| Tag   | 0x0143                                      |
| Type  | PropertyTagTypeShort or PropertyTagTypeLong |
| Count | 1                                           |

## PropertyTagTileOffset

For each tile, the byte offset of that tile.

| Property info | Value |
|-------|---------------------|
| Tag   | 0x0144              |
| Type  | PropertyTagTypeLong |
| Count | Number of tiles     |

## PropertyTagTileByteCounts

For each tile, the number of bytes in that tile.

| Property info | Value |
|-------|---------------------------------------------|
| Tag   | 0x0145                                      |
| Type  | PropertyTagTypeShort or PropertyTagTypeLong |
| Count | Number of tiles                             |

## PropertyTagInkSet

Set of inks used in a separated image.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x014C               |
| Type  | PropertyTagTypeShort |
| Count | 1                    |

## PropertyTagInkNames

Sequence of concatenated, null-terminated, character strings that specify the names of the inks used in a separated image.

| Property info | Value |
|-------|------------------------------------------------------------------------|
| Tag   | 0x014D                                                                 |
| Type  | PropertyTagTypeASCII                                                   |
| Count | Total length of the sequence of strings including the NULL terminators |

## PropertyTagNumberOfInks

Number of inks.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x014E               |
| Type  | PropertyTagTypeShort |
| Count | 1                    |

## PropertyTagDotRange

Color component values that correspond to a 0 percent dot and a 100 percent dot.

| Property info | Value |
|-------|---------------------------------------------|
| Tag   | 0x0150                                      |
| Type  | PropertyTagTypeByte or PropertyTagTypeShort |
| Count | 2 or 2×PropertyTagSamplesPerPixel           |

## PropertyTagTargetPrinter

Null-terminated character string that describes the intended printing environment.

| Property info | Value |
|-------|----------------------------------------------------|
| Tag   | 0x0151                                             |
| Type  | PropertyTagTypeASCII                               |
| Count | Length of the string including the NULL terminator |

## PropertyTagExtraSamples

Number of extra color components. For example, one extra component might hold an alpha value.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x0152               |
| Type  | PropertyTagTypeShort |
| Count | 1                    |

## PropertyTagSampleFormat

For each color component, the numerical format (unsigned, signed, floating point) of that component. See also [PropertyTagSamplesPerPixel](#propertytagsamplesperpixel).

| Property info | Value |
|-------|------------------------------------------|
| Tag   | 0x0153                                   |
| Type  | PropertyTagTypeShort                     |
| Count | Number of samples (components) per pixel |

## PropertyTagSMinSampleValue

For each color component, the minimum value of that component. See also [PropertyTagSamplesPerPixel](#propertytagsamplesperpixel).

| Property info | Value |
|-------|-----------------------------------------------------|
| Tag   | 0x0154                                              |
| Type  | The type that best matches the pixel component data |
| Count | Number of samples (components) per pixel            |

## PropertyTagSMaxSampleValue

For each color component, the maximum value of that component. See also [PropertyTagSamplesPerPixel](#propertytagsamplesperpixel).

| Property info | Value |
|-------|-----------------------------------------------------|
| Tag   | 0x0155                                              |
| Type  | The type that best matches the pixel component data |
| Count | Number of samples (components) per pixel            |

## PropertyTagTransferRange

Table of values that extends the range of the transfer function.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x0156               |
| Type  | PropertyTagTypeShort |
| Count | 6                    |

## PropertyTagJPEGProc

JPEG compression process.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x0200               |
| Type  | PropertyTagTypeShort |
| Count | 1                    |

## PropertyTagJPEGInterFormat

Offset to the start of a JPEG bitstream.

| Property info | Value |
|-------|---------------------|
| Tag   | 0x0201              |
| Type  | PropertyTagTypeLong |
| Count | 1                   |

## PropertyTagJPEGInterLength

Length, in bytes, of the JPEG bitstream.

| Property info | Value |
|-------|---------------------|
| Tag   | 0x0202              |
| Type  | PropertyTagTypeLong |
| Count | 1                   |

## PropertyTagJPEGRestartInterval

Length of the restart interval.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x0203               |
| Type  | PropertyTagTypeShort |
| Count | 1                    |

## PropertyTagJPEGLosslessPredictors

For each color component, a lossless predictor-selection value for that component. See also [PropertyTagSamplesPerPixel](#propertytagsamplesperpixel).

| Property info | Value |
|-------|------------------------------------------|
| Tag   | 0x0205                                   |
| Type  | PropertyTagTypeShort                     |
| Count | Number of samples (components) per pixel |

## PropertyTagJPEGPointTransforms

For each color component, a point transformation value for that component. See also [PropertyTagSamplesPerPixel](#propertytagsamplesperpixel).

| Property info | Value |
|-------|------------------------------------------|
| Tag   | 0x0206                                   |
| Type  | PropertyTagTypeShort                     |
| Count | Number of samples (components) per pixel |

## PropertyTagJPEGQTables

For each color component, the offset to the quantization table for that component. See also [PropertyTagSamplesPerPixel](#propertytagsamplesperpixel).

| Property info | Value |
|-------|------------------------------------------|
| Tag   | 0x0207                                   |
| Type  | PropertyTagTypeLong                      |
| Count | Number of samples (components) per pixel |

## PropertyTagJPEGDCTables

For each color component, the offset to the DC Huffman table (or lossless Huffman table) for that component. See also [PropertyTagSamplesPerPixel](#propertytagsamplesperpixel).

| Property info | Value |
|-------|------------------------------------------|
| Tag   | 0x0208                                   |
| Type  | PropertyTagTypeLong                      |
| Count | Number of samples (components) per pixel |

## PropertyTagJPEGACTables

For each color component, the offset to the AC Huffman table for that component. See also [PropertyTagSamplesPerPixel](#propertytagsamplesperpixel).

| Property info | Value |
|-------|------------------------------------------|
| Tag   | 0x0209                                   |
| Type  | PropertyTagTypeLong                      |
| Count | Number of samples (components) per pixel |

## PropertyTagYCbCrCoefficients

Coefficients for transformation from RGB to YCbCr image data.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x0211                  |
| Type  | PropertyTagTypeRational |
| Count | 3                       |

## PropertyTagYCbCrSubsampling

Sampling ratio of chrominance components in relation to the luminance component.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x0212               |
| Type  | PropertyTagTypeShort |
| Count | 2                    |

## PropertyTagYCbCrPositioning

Position of chrominance components in relation to the luminance component.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x0213               |
| Type  | PropertyTagTypeShort |
| Count | 1                    |

## PropertyTagREFBlackWhite

Reference black point value and reference white point value.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x0214                  |
| Type  | PropertyTagTypeRational |
| Count | 6                       |

## PropertyTagGamma

Gamma value attached to the image. The gamma value is stored as a rational number (pair of **long**) with a numerator of 100000. For example, a gamma value of 2.2 is stored as the pair (100000, 45455).

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x0301                  |
| Type  | PropertyTagTypeRational |
| Count | 1                       |

## PropertyTagICCProfileDescriptor

Null-terminated character string that identifies an ICC profile.

| Property info | Value |
|-------|----------------------------------------------------|
| Tag   | 0x0302                                             |
| Type  | PropertyTagTypeASCII                               |
| Count | Length of the string including the NULL terminator |

## PropertyTagSRGBRenderingIntent

How the image should be displayed as defined by the International Color Consortium (ICC). If a GDI+  [**Image**](/windows/desktop/api/gdiplusheaders/nl-gdiplusheaders-image) object is constructed with the *useEmbeddedColorManagement* parameter set to **TRUE**, then GDI+ renders the image according to the specified rendering intent. The intent can be set to perceptual, relative colorimetric, saturation, or absolute colorimetric.

-   Perceptual intent, which is suitable for photographs, gives good adaptation to the display device gamut at the expense of colorimetric accuracy.
-   Relative colorimetric intent is suitable for images (for example, logos) that require color appearance matching that is relative to the display device white point.
-   Saturation intent, which is suitable for charts and graphs, preserves saturation at the expense of hue and lightness.
-   Absolute colorimetric intent is suitable for proofs (previews of images destined for a different display device) that require preservation of absolute colorimetry.

| Property info | Value |
|-------|----------------------------------------------------|
| Tag   | 0x0303                                             |
| Type  | PropertyTagTypeByte                               |
| Count | 1 |

0 - perceptual <br/>1 - relative colorimetric <br/>2 - saturation <br/>3 - absolute colorimetric

## PropertyTagImageTitle

Null-terminated character string that specifies the title of the image.

| Property info | Value |
|-------|----------------------------------------------------|
| Tag   | 0x0320                                             |
| Type  | PropertyTagTypeASCII                               |
| Count | Length of the string including the NULL terminator |

## PropertyTagResolutionXUnit

Units in which to display horizontal resolution.

| Property info | Value |
|-------|----------------------------------------------------|
| Tag   | 0x5001                                             |
| Type  | PropertyTagTypeShort                               |
| Count | 1 |

1 - pixels per inch <br/>2 - pixels per centimeter

## PropertyTagResolutionYUnit

Units in which to display vertical resolution.

| Property info | Value |
|-------|----------------------------------------------------|
| Tag   | 0x5002                                             |
| Type  | PropertyTagTypeShort                               |
| Count | 1 |

1 - pixels per inch <br/>2 - pixels per centimeter

## PropertyTagResolutionXLengthUnit

Units in which to display the image width.

| Property info | Value |
|-------|----------------------------------------------------|
| Tag   | 0x5003                                             |
| Type  | PropertyTagTypeShort                               |
| Count | 1 |

1 - inches <br/>2 - centimeters <br/>3 - points <br/>4 - picas <br/>5 - columns

## PropertyTagResolutionYLengthUnit

Units in which to display the image height.

| Property info | Value |
|-------|----------------------------------------------------|
| Tag   | 0x5004                                             |
| Type  | PropertyTagTypeShort                               |
| Count | 1 |

1 - inches <br/>2 - centimeters <br/>3 - points <br/>4 - picas <br/>5 - columns

## PropertyTagPrintFlags

Sequence of one-byte Boolean values that specify printing options.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x5005               |
| Type  | PropertyTagTypeASCII |
| Count | Number of flags      |

## PropertyTagPrintFlagsVersion

Print flags version.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x5006               |
| Type  | PropertyTagTypeShort |
| Count | 1                    |

## PropertyTagPrintFlagsCrop

Print flags center crop marks.

| Property info | Value |
|-------|---------------------|
| Tag   | 0x5007              |
| Type  | PropertyTagTypeByte |
| Count | 1                   |

## PropertyTagPrintFlagsBleedWidth

Print flags bleed width.

| Property info | Value |
|-------|---------------------|
| Tag   | 0x5008              |
| Type  | PropertyTagTypeLong |
| Count | 1                   |

## PropertyTagPrintFlagsBleedWidthScale

Print flags bleed width scale.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x5009               |
| Type  | PropertyTagTypeShort |
| Count | 1                    |

## PropertyTagHalftoneLPI

Ink's screen frequency, in lines per inch.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x500A                  |
| Type  | PropertyTagTypeRational |
| Count | 1                       |

## PropertyTagHalftoneLPIUnit

Units for the screen frequency.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x500B                  |
| Type  | PropertyTagTypeShort |
| Count | 1                       |

1 - lines per inch <br/>2 - lines per centimeter

## PropertyTagHalftoneDegree

Angle for screen.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x500C                  |
| Type  | PropertyTagTypeRational |
| Count | 1                       |

## PropertyTagHalftoneShape

Shape of the halftone dots.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x500D                  |
| Type  | PropertyTagTypeShort |
| Count | 1                       |

0 - round <br/>1 - ellipse <br/>2 - line <br/>3 - square <br/>4 - cross <br/>6 - diamond

## PropertyTagHalftoneMisc

Miscellaneous halftone information.

| Property info | Value |
|-------|---------------------|
| Tag   | 0x500E              |
| Type  | PropertyTagTypeLong |
| Count | 1                   |

## PropertyTagHalftoneScreen

Boolean value that specifies whether to use the printer's default screens.

| Property info | Value |
|-------|---------------------|
| Tag   | 0x500F              |
| Type  | PropertyTagTypeByte |
| Count | 1                   |

1 - use printer's default screens <br/>2 - other

## PropertyTagJPEGQuality

Private tag used by the Adobe Photoshop format. Not for public use.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x5010               |
| Type  | PropertyTagTypeShort |
| Count | Any                  |

## PropertyTagGridSize

Block of information about grids and guides.

| Property info | Value |
|-------|--------------------------|
| Tag   | 0x5011                   |
| Type  | PropertyTagTypeUndefined |
| Count | Any                      |

## PropertyTagThumbnailFormat

Format of the thumbnail image.

| Property info | Value |
|-------|--------------------------|
| Tag   | 0x0x50125011                   |
| Type  | PropertyTagTypeLong |
| Count | 1                      |

0 - raw RGB <br/>1 - JPEG

## PropertyTagThumbnailWidth

Width, in pixels, of the thumbnail image.

| Property info | Value |
|-------|---------------------|
| Tag   | 0x5013              |
| Type  | PropertyTagTypeLong |
| Count | 1                   |

## PropertyTagThumbnailHeight

Height, in pixels, of the thumbnail image.

| Property info | Value |
|-------|---------------------|
| Tag   | 0x5014              |
| Type  | PropertyTagTypeLong |
| Count | 1                   |

## PropertyTagThumbnailColorDepth

bits per pixel (BPP) for the thumbnail image.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x5015               |
| Type  | PropertyTagTypeShort |
| Count | 1                    |

## PropertyTagThumbnailPlanes

Number of color planes for the thumbnail image.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x5016               |
| Type  | PropertyTagTypeShort |
| Count | 1                    |

## PropertyTagThumbnailRawBytes

Byte offset between rows of pixel data.

| Property info | Value |
|-------|---------------------|
| Tag   | 0x5017              |
| Type  | PropertyTagTypeLong |
| Count | 1                   |

## PropertyTagThumbnailSize

Total size, in bytes, of the thumbnail image.

| Property info | Value |
|-------|---------------------|
| Tag   | 0x5018              |
| Type  | PropertyTagTypeLong |
| Count | 1                   |

## PropertyTagThumbnailCompressedSize

Compressed size, in bytes, of the thumbnail image.

| Property info | Value |
|-------|---------------------|
| Tag   | 0x5019              |
| Type  | PropertyTagTypeLong |
| Count | 1                   |

## PropertyTagColorTransferFunction

Table of values that specify color transfer functions.

| Property info | Value |
|-------|--------------------------|
| Tag   | 0x501A                   |
| Type  | PropertyTagTypeUndefined |
| Count | Any                      |

## PropertyTagThumbnailData

Raw thumbnail bits in JPEG or RGB format. Depends on PropertyTagThumbnailFormat.

| Property info | Value |
|-------|---------------------|
| Tag   | 0x501B              |
| Type  | PropertyTagTypeByte |
| Count | Variable            |

## PropertyTagThumbnailImageWidth

Number of pixels per row in the thumbnail image.

| Property info | Value |
|-------|---------------------------------------------|
| Tag   | 0x5020                                      |
| Type  | PropertyTagTypeShort or PropertyTagTypeLong |
| Count | 1                                           |

## PropertyTagThumbnailImageHeight

Number of pixel rows in the thumbnail image.

| Property info | Value |
|-------|---------------------------------------------|
| Tag   | 0x5021                                      |
| Type  | PropertyTagTypeShort or PropertyTagTypeLong |
| Count | 1                                           |

## PropertyTagThumbnailBitsPerSample

Number of bits per color component in the thumbnail image. See also [PropertyTagThumbnailSamplesPerPixel](#propertytagthumbnailsamplesperpixel).

| Property info | Value |
|-------|-----------------------------------------------------------------|
| Tag   | 0x5022                                                          |
| Type  | PropertyTagTypeShort                                            |
| Count | Number of samples (components) per pixel in the thumbnail image |

## PropertyTagThumbnailCompression

Compression scheme used for thumbnail image data.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x5023               |
| Type  | PropertyTagTypeShort |
| Count | 1                    |

## PropertyTagThumbnailPhotometricInterp

How thumbnail pixel data will be interpreted.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x5024               |
| Type  | PropertyTagTypeShort |
| Count | 1                    |

## PropertyTagThumbnailImageDescription

Null-terminated character string that specifies the title of the image.

| Property info | Value |
|-------|----------------------------------------------------|
| Tag   | 0x5025                                             |
| Type  | PropertyTagTypeASCII                               |
| Count | Length of the string including the NULL terminator |

## PropertyTagThumbnailEquipMake

Null-terminated character string that specifies the manufacturer of the equipment used to record the thumbnail image.

| Property info | Value |
|-------|----------------------------------------------------|
| Tag   | 0x5026                                             |
| Type  | PropertyTagTypeASCII                               |
| Count | Length of the string including the NULL terminator |

## PropertyTagThumbnailEquipModel

Null-terminated character string that specifies the model name or model number of the equipment used to record the thumbnail image.

| Property info | Value |
|-------|----------------------------------------------------|
| Tag   | 0x5027                                             |
| Type  | PropertyTagTypeASCII                               |
| Count | Length of the string including the NULL terminator |

## PropertyTagThumbnailStripOffsets

For each strip in the thumbnail image, the byte offset of that strip. See also [PropertyTagThumbnailRowsPerStrip](#propertytagthumbnailrowsperstrip) and [PropertyTagThumbnailStripBytesCount](#propertytagthumbnailstripbytescount).

| Property info | Value |
|-------|---------------------------------------------|
| Tag   | 0x5028                                      |
| Type  | PropertyTagTypeShort or PropertyTagTypeLong |
| Count | Number of strips                            |

## PropertyTagThumbnailOrientation

Thumbnail image orientation in terms of rows and columns. See also [PropertyTagOrientation](#propertytagorientation).

| Property info | Value |
|-------|----------------------|
| Tag   | 0x5029               |
| Type  | PropertyTagTypeShort |
| Count | 1                    |

## PropertyTagThumbnailSamplesPerPixel

Number of color components per pixel in the thumbnail image.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x502A               |
| Type  | PropertyTagTypeShort |
| Count | 1                    |

## PropertyTagThumbnailRowsPerStrip

Number of rows per strip in the thumbnail image. See also [PropertyTagThumbnailStripBytesCount](#propertytagthumbnailstripbytescount) and [PropertyTagThumbnailStripOffsets](#propertytagthumbnailstripoffsets).

| Property info | Value |
|-------|---------------------------------------------|
| Tag   | 0x502B                                      |
| Type  | PropertyTagTypeShort or PropertyTagTypeLong |
| Count | 1                                           |

## PropertyTagThumbnailStripBytesCount

For each thumbnail image strip, the total number of bytes in that strip.

| Property info | Value |
|-------|---------------------------------------------|
| Tag   | 0x502C                                      |
| Type  | PropertyTagTypeShort or PropertyTagTypeLong |
| Count | Number of strips in the thumbnail image     |

## PropertyTagThumbnailResolutionX

Thumbnail resolution in the width direction. The resolution unit is given in [PropertyTagThumbnailResolutionUnit](#propertytagthumbnailresolutionunit).

| Property info | Value |
|-----|--------|
| Tag | 0x502D |

## PropertyTagThumbnailResolutionY

Thumbnail resolution in the height direction. The resolution unit is given in [PropertyTagThumbnailResolutionUnit](#propertytagthumbnailresolutionunit).

| Property info | Value |
|-----|--------|
| Tag | 0x502E |

## PropertyTagThumbnailPlanarConfig

Whether pixel components in the thumbnail image are recorded in chunky or planar format. See also [PropertyTagPlanarConfig](#propertytagplanarconfig).

| Property info | Value |
|-------|----------------------|
| Tag   | 0x502F               |
| Type  | PropertyTagTypeShort |
| Count | 1                    |

## PropertyTagThumbnailResolutionUnit

Unit of measure for the horizontal resolution and the vertical resolution of the thumbnail image. See also [PropertyTagResolutionUnit](#propertytagresolutionunit).

| Property info | Value |
|-------|----------------------|
| Tag   | 0x5030               |
| Type  | PropertyTagTypeShort |
| Count | 1                    |

## PropertyTagThumbnailTransferFunction

Tables that specify transfer functions for the thumbnail image. See also [PropertyTagTransferFunction](#propertytagtransferfunction).

| Property info | Value |
|-------|------------------------------------------------------|
| Tag   | 0x5031                                               |
| Type  | PropertyTagTypeShort                                 |
| Count | Total number of 16-bit words required for the tables |

## PropertyTagThumbnailSoftwareUsed

Null-terminated character string that specifies the name and version of the software or firmware of the device used to generate the thumbnail image.

| Property info | Value |
|-------|----------------------------------------------------|
| Tag   | 0x5032                                             |
| Type  | PropertyTagTypeASCII                               |
| Count | Length of the string including the NULL terminator |

## PropertyTagThumbnailDateTime

Date and time the thumbnail image was created. See also [PropertyTagDateTime](#propertytagdatetime).

| Property info | Value |
|-------|----------------------|
| Tag   | 0x5033               |
| Type  | PropertyTagTypeASCII |
| Count | 20                   |

## PropertyTagThumbnailArtist

Null-terminated character string that specifies the name of the person who created the thumbnail image.

| Property info | Value |
|-------|----------------------------------------------------|
| Tag   | 0x5034                                             |
| Type  | PropertyTagTypeASCII                               |
| Count | Length of the string including the NULL terminator |

## PropertyTagThumbnailWhitePoint

Chromaticity of the white point of the thumbnail image. See also [PropertyTagWhitePoint](#propertytagwhitepoint).

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x5035                  |
| Type  | PropertyTagTypeRational |
| Count | 2                       |

## PropertyTagThumbnailPrimaryChromaticities

For each of the three primary colors in the thumbnail image, the chromaticity of that color. See also [PropertyTagPrimaryChromaticities](#propertytagprimarychromaticities).

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x5036                  |
| Type  | PropertyTagTypeRational |
| Count | 6                       |

## PropertyTagThumbnailYCbCrCoefficients

Coefficients for transformation from RGB to YCbCr data for the thumbnail image. See also [PropertyTagYCbCrCoefficients](#propertytagycbcrcoefficients).

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x5037                  |
| Type  | PropertyTagTypeRational |
| Count | 3                       |

## PropertyTagThumbnailYCbCrSubsampling

Sampling ratio of chrominance components in relation to the luminance component for the thumbnail image. See also [PropertyTagYCbCrSubsampling](#propertytagycbcrsubsampling).

| Property info | Value |
|-------|----------------------|
| Tag   | 0x5038               |
| Type  | PropertyTagTypeShort |
| Count | 2                    |

## PropertyTagThumbnailYCbCrPositioning

Position of chrominance components in relation to the luminance component for the thumbnail image. See also [PropertyTagYCbCrPositioning](#propertytagycbcrpositioning).

| Property info | Value |
|-------|----------------------|
| Tag   | 0x5039               |
| Type  | PropertyTagTypeShort |
| Count | 1                    |

## PropertyTagThumbnailRefBlackWhite

Reference black point value and reference white point value for the thumbnail image. See also [PropertyTagREFBlackWhite](#propertytagrefblackwhite).

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x503A                  |
| Type  | PropertyTagTypeRational |
| Count | 6                       |

## PropertyTagThumbnailCopyRight

Null-terminated character string that contains copyright information for the thumbnail image.

| Property info | Value |
|-------|----------------------------------------------------|
| Tag   | 0x503B                                             |
| Type  | PropertyTagTypeASCII                               |
| Count | Length of the string including the NULL terminator |

## PropertyTagLuminanceTable

Luminance table. The luminance table and the chrominance table are used to control JPEG quality. A valid luminance or chrominance table has 64 entries of type PropertyTagTypeShort. If an image has either a luminance table or a chrominance table, then it must have both tables.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x5090               |
| Type  | PropertyTagTypeShort |
| Count | 64                   |

## PropertyTagChrominanceTable

Chrominance table. The luminance table and the chrominance table are used to control JPEG quality. A valid luminance or chrominance table has 64 entries of type PropertyTagTypeShort. If an image has either a luminance table or a chrominance table, then it must have both tables.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x5091               |
| Type  | PropertyTagTypeShort |
| Count | 64                   |

## PropertyTagFrameDelay

Time delay, in hundredths of a second, between two frames in an animated GIF image.

| Property info | Value |
|-------|-------------------------------|
| Tag   | 0x5100                        |
| Type  | PropertyTagTypeLong           |
| Count | Number of frames in the image |

## PropertyTagLoopCount

For an animated GIF image, the number of times to display the animation. A value of 0 specifies that the animation should be displayed infinitely.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x5101               |
| Type  | PropertyTagTypeShort |
| Count | 1                    |

## PropertyTagGlobalPalette

Color palette for an indexed bitmap in a GIF image.

| Property info | Value |
|-------|-------------------------------|
| Tag   | 0x5102                        |
| Type  | PropertyTagTypeByte           |
| Count | 3 x number of palette entries |

## PropertyTagIndexBackground

Index of the background color in the palette of a GIF image.

| Property info | Value |
|-------|---------------------|
| Tag   | 0x5103              |
| Type  | PropertyTagTypeByte |
| Count | 1                   |

## PropertyTagIndexTransparent

Index of the transparent color in the palette of a GIF image.

| Property info | Value |
|-------|---------------------|
| Tag   | 0x5104              |
| Type  | PropertyTagTypeByte |
| Count | 1                   |

## PropertyTagPixelUnit

Unit for PropertyTagPixelPerUnitX and PropertyTagPixelPerUnitY.

| Property info | Value |
|-------|---------------------|
| Tag   | 0x5110              |
| Type  | PropertyTagTypeByte |
| Count | 1                   |

0 - unknown

## PropertyTagPixelPerUnitX

Pixels per unit in the x direction.

| Property info | Value |
|-------|---------------------|
| Tag   | 0x5111              |
| Type  | PropertyTagTypeLong |
| Count | 1                   |

## PropertyTagPixelPerUnitY

Pixels per unit in the y direction.

| Property info | Value |
|-------|---------------------|
| Tag   | 0x5112              |
| Type  | PropertyTagTypeLong |
| Count | 1                   |

## PropertyTagPaletteHistogram

Palette histogram.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x5113                  |
| Type  | PropertyTagTypeByte     |
| Count | Length of the histogram |

## PropertyTagCopyright

Null-terminated character string that contains copyright information.

| Property info | Value |
|-------|----------------------------------------------------|
| Tag   | 0x8298                                             |
| Type  | PropertyTagTypeASCII                               |
| Count | Length of the string including the NULL terminator |

## PropertyTagExifExposureTime

Exposure time, measured in seconds.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x829A                  |
| Type  | PropertyTagTypeRational |
| Count | 1                       |

## PropertyTagExifFNumber

F number.

| Property info | Value |
|-------|----------|
| Tag   | 0x829D   |
| Type  | PropertyTagTypeRational |
| Count | 1        |

## PropertyTagExifIFD

Private tag used by GDI+. Not for public use. GDI+ uses this tag to locate Exif-specific information.

| Property info | Value |
|-------|---------------------|
| Tag   | 0x8769              |
| Type  | PropertyTagTypeLong |
| Count | 1                   |

## PropertyTagICCProfile

ICC profile embedded in the image.

| Property info | Value |
|-------|-----------------------|
| Tag   | 0x8773                |
| Type  | PropertyTagTypeByte   |
| Count | Length of the profile |

## PropertyTagExifExposureProg

Class of the program used by the camera to set exposure when the picture is taken.

| Property info | Value |
|-------|-----------------------|
| Tag   | 0x8822                |
| Type  | PropertyTagTypeShort   |
| Count | 1 |

0 - not defined <br/>1 - manual <br/>2 - normal program <br/>3 - aperture priority <br/>4 - shutter priority <br/>5 - creative program (biased toward depth of field) <br/>6 - action program (biased toward fast shutter speed) <br/>7 - portrait mode (for close-up photos with the background out of focus) <br/>8 - landscape mode (for landscape photos with the background in focus) <br/>9 to 255 - reserved

## PropertyTagExifSpectralSense

Null-terminated character string that specifies the spectral sensitivity of each channel of the camera used. The string is compatible with the standard developed by the ASTM Technical Committee.

| Property info | Value |
|-------|----------------------------------------------------|
| Tag   | 0x8824                                             |
| Type  | PropertyTagTypeASCII                               |
| Count | Length of the string including the NULL terminator |

## PropertyTagGpsIFD

Offset to a block of GPS property items. Property items whose tags have the prefix PropertyTagGps are stored in the GPS block. The GPS property items are defined in the EXIF specification. GDI+ uses this tag to locate GPS information, but GDI+ does not expose this tag for public use.

| Property info | Value |
|-------|---------------------|
| Tag   | 0x8825              |
| Type  | PropertyTagTypeLong |
| Count | 1                   |

## PropertyTagExifISOSpeed

ISO speed and ISO latitude of the camera or input device as specified in ISO 12232.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x8827               |
| Type  | PropertyTagTypeShort |
| Count | Any                  |

## PropertyTagExifOECF

Optoelectronic conversion function (OECF) specified in ISO 14524. The OECF is the relationship between the camera optical input and the image values.

| Property info | Value |
|-------|--------------------------|
| Tag   | 0x8828                   |
| Type  | PropertyTagTypeUndefined |
| Count | Any                      |

## PropertyTagExifVer

Version of the EXIF standard supported. Nonexistence of this field is taken to mean nonconformance to the standard. Conformance to the standard is indicated by recording 0210 as a 4-byte ASCII string. Because the type is PropertyTagTypeUndefined, there is no NULL terminator.

| Property info | Value |
|---------|--------------------------|
| Tag     | 0x9000                   |
| Type    | PropertyTagTypeUndefined |
| Count   | 4                        |
| Default | 0210                     |

## PropertyTagExifDTOrig

Date and time when the original image data was generated. For a DSC, the date and time when the picture was taken. The format is YYYY:MM:DD HH:MM:SS with time shown in 24-hour format and the date and time separated by one blank character (0x2000). The character string length is 20 bytes including the NULL terminator. When the field is empty, it is treated as unknown.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x9003               |
| Type  | PropertyTagTypeASCII |
| Count | 20                   |

## PropertyTagExifDTDigitized

Date and time when the image was stored as digital data. If, for example, an image was captured by DSC and at the same time the file was recorded, then DateTimeOriginal and DateTimeDigitized will have the same contents.

The format is YYYY:MM:DD HH:MM:SS with time shown in 24-hour format and the date and time separated by one blank character (0x2000). The character string length is 20 bytes including the NULL terminator. When the field is empty, it is treated as unknown.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x9004               |
| Type  | PropertyTagTypeASCII |
| Count | 20                   |

## PropertyTagExifCompConfig

Information specific to compressed data. The channels of each component are arranged in order from the first component to the fourth. For uncompressed data, the data arrangement is given in the PropertyTagPhotometricInterp tag.

However, because PropertyTagPhotometricInterp can only express the order of Y, Cb, and Cr, this tag is provided for cases when compressed data uses components other than Y, Cb, and Cr and to support other sequences.

| Property info | Value |
|-------|----------------------|
| Tag   | 0x9101               |
| Type  | PropertyTagTypeUndefined |
| Count | 4                   |

Default

4 5 6 0 (if RGB uncompressed) 1 2 3 0 (other cases)

0 - does not exist <br/>1 - Y <br/>2 - Cb <br/>3 - Cr <br/>4 - R <br/>5 - G <br/>6 - B <br/>Other - reserved

## PropertyTagExifCompBPP

Information specific to compressed data. The compression mode used for a compressed image is indicated in unit BPP.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x9102                  |
| Type  | PropertyTagTypeRational |
| Count | 1                       |

## PropertyTagExifShutterSpeed

Shutter speed. The unit is the Additive System of Photographic Exposure (APEX) value.

| Property info | Value |
|-------|--------------------------|
| Tag   | 0x9201                   |
| Type  | PropertyTagTypeSRational |
| Count | 1                        |

## PropertyTagExifAperture

Lens aperture. The unit is the APEX value.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x9202                  |
| Type  | PropertyTagTypeRational |
| Count | 1                       |

## PropertyTagExifBrightness

Brightness value. The unit is the APEX value. Ordinarily it is given in the range of -99.99 to 99.99.

| Property info | Value |
|-------|--------------------------|
| Tag   | 0x9203                   |
| Type  | PropertyTagTypeSRational |
| Count | 1                        |

## PropertyTagExifExposureBias

Exposure bias. The unit is the APEX value. Ordinarily it is given in the range -99.99 to 99.99.

| Property info | Value |
|-------|--------------------------|
| Tag   | 0x9204                   |
| Type  | PropertyTagTypeSRational |
| Count | 1                        |

## PropertyTagExifMaxAperture

Smallest F number of the lens. The unit is the APEX value. Ordinarily it is given in the range of 00.00 to 99.99, but it is not limited to this range.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x9205                  |
| Type  | PropertyTagTypeRational |
| Count | 1                       |

## PropertyTagExifSubjectDist

Distance to the subject, measured in meters.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x9206                  |
| Type  | PropertyTagTypeRational |
| Count | 1                       |

## PropertyTagExifMeteringMode

Metering mode.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x9207                  |
| Type  | PropertyTagTypeShort |
| Count | 1                       |

Default: 0

0 - unknown <br/>1 - Average <br/>2 - CenterWeightedAverage <br/>3 - Spot <br/>4 - MultiSpot <br/>5 - Pattern <br/>6 - Partial <br/>7 to 254 - reserved <br/>255 - other

## PropertyTagExifLightSource

Type of light source.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x9208                  |
| Type  | PropertyTagTypeShort |
| Count | 1                       |

Default: 0

0 - unknown <br/>1 - Daylight <br/>2 - Flourescent <br/>3 - Tungsten <br/>17 - Standard Light A <br/>18 - Standard Light B <br/>19 - Standard Light C <br/>20 - D55 <br/>21 - D65 <br/>22 - D75 <br/>23 to 254 - reserved <br/>255 - other

## PropertyTagExifFlash

Flash status. This tag is recorded when an image is taken using a strobe light (flash). Bit 0 indicates the flash firing status, and bits 1 and 2 indicate the flash return status.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x9209                  |
| Type  | PropertyTagTypeShort |
| Count | 1                       |

Values for bit 0 that indicate whether the flash fired: 0b - flash did not fire; 1b - flash fired

Values for bits 1 and 2 that indicate the status of returned light: 00b - no strobe return detection function; 01b - reserved 10b - strobe return light not detected ;11b - strobe return light detected

Resulting flash tag values: 0x0000 - flash did not fire ;0x0001 - flash fired ;0x0005 - strobe return light not detected

## PropertyTagExifFocalLength

Actual focal length, in millimeters, of the lens. Conversion is not made to the focal length of a 35 millimeter film camera.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0x920A                  |
| Type  | PropertyTagTypeRational |
| Count | 1                       |

## PropertyTagExifMakerNote

Note tag. A tag used by manufacturers of EXIF writers to record information. The contents are up to the manufacturer.

| Property info | Value |
|-------|--------------------------|
| Tag   | 0x927C                   |
| Type  | PropertyTagTypeUndefined |
| Count | Any                      |

## PropertyTagExifUserComment

Comment tag. A tag used by EXIF users to write keywords or comments about the image besides those in PropertyTagImageDescription and without the character-code limitations of the PropertyTagImageDescription tag.

| Property info | Value |
|-------|--------------------------|
| Tag   | 0x9286                   |
| Type  | PropertyTagTypeUndefined |
| Count | Any                      |

The character code used in the PropertyTagExifUserComment tag is identified based on an ID code in a fixed 8-byte area at the start of the tag data area. The unused portion of the area is padded with null characters (0). ID codes are assigned by means of registration. Because the type is not ASCII, it is not necessary to use a NULL terminator.

## PropertyTagExifDTSubsec

Null-terminated character string that specifies a fraction of a second for the PropertyTagDateTime tag.

| Property info | Value |
|-------|----------------------------------------------------|
| Tag   | 0x9290                                             |
| Type  | PropertyTagTypeASCII                               |
| Count | Length of the string including the NULL terminator |

## PropertyTagExifDTOrigSS

Null-terminated character string that specifies a fraction of a second for the PropertyTagExifDTOrig tag.

| Property info | Value |
|------|----------------------------------------------------|
| Tag  | 0x9291                                             |
| Type | PropertyTagTypeASCII                               |
| N    | Length of the string including the NULL terminator |

## PropertyTagExifDTDigSS

Null-terminated character string that specifies a fraction of a second for the PropertyTagExifDTDigitized tag.

| Property info | Value |
|------|----------------------------------------------------|
| Tag  | 0x9292                                             |
| Type | ASCII                                              |
| N    | Length of the string including the NULL terminator |

## PropertyTagExifFPXVer

FlashPix format version supported by an FPXR file. If the FPXR function supports FlashPix format version 1.0, this is indicated similarly to PropertyTagExifVer by recording 0100 as a 4-byte ASCII string. Because the type is PropertyTagTypeUndefined, there is no NULL terminator.

| Property info | Value |
|-------|----------------------------------------------------|
| Tag   | 0xA000                                             |
| Type  | PropertyTagTypeUndefined                               |
| Count | 4 |

Default: 0100

0100 - FlashPix format version 1.0 <br/>Other - reserved

## PropertyTagExifColorSpace

Color space specifier. Normally sRGB (=1) is used to define the color space based on the PC monitor conditions and environment. If a color space other than sRGB is used, Uncalibrated (=0xFFFF) is set. Image data recorded as Uncalibrated can be treated as sRGB when it is converted to FlashPix.

| Property info | Value |
|-------|----------------------------------------------------|
| Tag   | 0xA001                                             |
| Type  | PropertyTagTypeShort                               |
| Count | 1 |

0x1 - sRGB 0xFFFF - uncalibrated <br/>Other - reserved

## PropertyTagExifPixXDim

Information specific to compressed data. When a compressed file is recorded, the valid width of the meaningful image must be recorded in this tag, whether or not there is padding data or a restart marker. This tag should not exist in an uncompressed file.

| Property info | Value |
|-------|---------------------------------------------|
| Tag   | 0xA002                                      |
| Type  | PropertyTagTypeShort or PropertyTagTypeLong |
| Count | 1                                           |

## PropertyTagExifPixYDim

Information specific to compressed data. When a compressed file is recorded, the valid height of the meaningful image must be recorded in this tag whether or not there is padding data or a restart marker. This tag should not exist in an uncompressed file. Because data padding is unnecessary in the vertical direction, the number of lines recorded in this valid image height tag will be the same as that recorded in the SOF.

| Property info | Value |
|-------|---------------------------------------------|
| Tag   | 0xA003                                      |
| Type  | PropertyTagTypeShort or PropertyTagTypeLong |
| Count | 1                                           |

## PropertyTagExifRelatedWav

The name of an audio file related to the image data. The only relational information recorded is the EXIF audio file name and extension (an ASCII string that consists of 8 characters plus a period (.), plus 3 characters). The path is not recorded. When you use this tag, audio files must be recorded in conformance with the EXIF audio format. Writers can also store audio data within APP2 as FlashPix extension stream data.

| Property info | Value |
|-------|----------------------|
| Tag   | 0xA004               |
| Type  | PropertyTagTypeASCII |
| Count | 13                   |

## PropertyTagExifInterop

Offset to a block of property items that contain interoperability information.

| Property info | Value |
|-------|---------------------|
| Tag   | 0xA005              |
| Type  | PropertyTagTypeLong |
| Count | 1                   |

## PropertyTagExifFlashEnergy

Strobe energy, in Beam Candle Power Seconds (BCPS), at the time the image was captured.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0xA20B                  |
| Type  | PropertyTagTypeRational |
| Count | 1                       |

## PropertyTagExifSpatialFR

Camera or input device spatial frequency table and SFR values in the image width, image height, and diagonal direction, as specified in ISO 12233.

| Property info | Value |
|-------|--------------------------|
| Tag   | 0xA20C                   |
| Type  | PropertyTagTypeUndefined |
| Count | Any                      |

## PropertyTagExifFocalXRes

Number of pixels in the image width (x) direction per unit on the camera focal plane. The unit is specified in PropertyTagExifFocalResUnit.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0xA20E                  |
| Type  | PropertyTagTypeRational |
| Count | 1                       |

## PropertyTagExifFocalYRes

Number of pixels in the image height (y) direction per unit on the camera focal plane. The unit is specified in PropertyTagExifFocalResUnit.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0xA20F                  |
| Type  | PropertyTagTypeRational |
| Count | 1                       |

## PropertyTagExifFocalResUnit

Unit of measure for PropertyTagExifFocalXRes and PropertyTagExifFocalYRes.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0xA210                  |
| Type  | PropertyTagTypeShort |
| Count | 1                       |

2 - inch <br/>3 - centimeter

## PropertyTagExifSubjectLoc

Location of the main subject in the scene. The value of this tag represents the pixel at the center of the main subject relative to the left edge. The first value indicates the column number, and the second value indicates the row number.

| Property info | Value |
|-------|----------------------|
| Tag   | 0xA214               |
| Type  | PropertyTagTypeShort |
| Count | 2                    |

## PropertyTagExifExposureIndex

Exposure index selected on the camera or input device at the time the image was captured.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0xA215                  |
| Type  | PropertyTagTypeRational |
| Count | 1                       |

## PropertyTagExifSensingMethod

Image sensor type on the camera or input device.

| Property info | Value |
|-------|-------------------------|
| Tag   | 0xA217                  |
| Type  | PropertyTagTypeShort |
| Count | 1                       |

1 - not defined <br/>2 - one-chip color area sensor <br/>3 - two-chip color area sensor <br/>4 - three-chip color area sensor <br/>5 - color sequential area sensor <br/>7 - trilinear sensor <br/>8 - color sequential linear sensor <br/>Other - reserved

## PropertyTagExifFileSource

The image source. If a DSC recorded the image, the value of this tag is 3.

| Property info | Value |
|-------|--------------------------|
| Tag   | 0xA300                   |
| Type  | PropertyTagTypeUndefined |
| Count | 1                        |

## PropertyTagExifSceneType

The type of scene. If a DSC recorded the image, the value of this tag must be set to 1, indicating that the image was directly photographed.

| Property info | Value |
|-------|--------------------------|
| Tag   | 0xA301                   |
| Type  | PropertyTagTypeUndefined |
| Count | 1                        |

## PropertyTagExifCfaPattern

The color filter array (CFA) geometric pattern of the image sensor when a one-chip color area sensor is used. It does not apply to all sensing methods.

| Property info | Value |
|-------|--------------------------|
| Tag   | 0xA302                   |
| Type  | PropertyTagTypeUndefined |
| Count | Any                      |

## Related topics

[Image file format specifications](-gdiplus-constant-image-file-format-specifications.md)
[Image property tag constants](-gdiplus-constant-image-property-tag-constants.md)
[Image property tag type constants](-gdiplus-constant-image-property-tag-type-constants.md)
[Property tags in alphabetical oOrder](-gdiplus-constant-property-tags-in-alphabetical-order.md)
[Property tags in numerical order](-gdiplus-constant-property-tags-in-numerical-order.md)
[Reading and writing metadata](-gdiplus-reading-and-writing-metadata-use.md)
