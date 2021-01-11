---
description: This topic provides an overview of the metadata query language queries for reading and writing metadata supported by GIF, PNG, TIFF and JPEG images.
ms.assetid: a6ab1708-dd82-4960-b908-f1daef7374ef
title: Native Image Format Metadata Queries
ms.topic: article
ms.date: 05/31/2018
---

# Native Image Format Metadata Queries

This topic provides an overview of the [metadata query language](-wic-codec-metadataquerylanguage.md) queries for reading and writing metadata supported by GIF, PNG, TIFF and JPEG images.It includes metadata that is specific to each image format, as well as metadata that is supported by multiple formats.

This topic contains the following sections.

-   [Prerequisites](#prerequisites)
-   [Photo Metadata Policy Expression](#photo-metadata-policy-expression)
-   [File Format Specific Metadata](#file-format-specific-metadata)
    -   [GIF Metadata](#gif-metadata)
    -   [PNG Metadata](#png-metadata)
    -   [TIFF Metadata](#tiff-metadata)
    -   [JPEG Metadata](#jpeg-metadata)
-   [File Format Independent Metadata](#file-format-independent-metadata)
    -   [IFD Metadata](#ifd-metadata)
    -   [EXIF Metadata](#exif-metadata)
    -   [GPS Metadata](#gps-metadata)
    -   [XMP Metadata](#xmp-metadata)
-   [Related topics](#related-topics)

## Prerequisites

To understand this topic, you should be familiar with the Windows Imaging Component (WIC) metadata system as described in the [WIC Metadata Overview](-wic-about-metadata.md). You should also be familiar with the query language used to read and write metadata, as described in [Metadata Query Language Overview](-wic-codec-metadataquerylanguage.md).

## Photo Metadata Policy Expression

In addition to supporting the metadata query language, [WIC](-wic-api.md) also accepts canonical property names from the [Windows Property System](../properties/windows-properties-system.md). WIC supports a subset of the Windows property namespace that is relevant to image formats, as described in [Photo Metadata Policies](photo-metadata-policies.md). A Windows property that is used as a WIC metadata query is referred to as a photo metadata policy expression.

For example, the photo metadata policy expression for the EXIF orientation flag is:

-   [System.Photo.Orientation](-wic-photoprop-system-photo-orientation.md)

In general, policy expressions are recommended over native metadata queries for common image metadata items that are covered by the Windows property namespace. The metadata query language is best suited for cases where low-level access to specific image metadata items is needed, or for custom or advanced metadata items that are not supported by the Windows property system. For more information, see [Photo Metadata Policy Expressions](-wic-codec-metadataquerylanguage.md).

## File Format Specific Metadata

The following sections contain tables that list the available metadata queries for each image file type. Each table has the following columns:

-   **Path** - The query path used to retrieve the metadata item.
-   **Name** - The name of the metadata item.
-   **Type** - The type of the metadata item retrieved from the query path. Metadata retrieved by [WIC](-wic-api.md) is returned in the form of PROPVARIANT, which reports the data type using the VARTYPE enumeration.on.

The query paths are used by the WIC metadata API to access the embedded metadata of an image. The following example code demonstrates using an [**IWICMetadataQueryReader**](/windows/desktop/api/Wincodec/nn-wincodec-iwicmetadataqueryreader) to query for a JPEG's IFD metadata block.


```
// Not shown: image decoding 
IWICMetadataQueryReader *pQueryReader = NULL;
IWICMetadataQueryReader *pIFDReader = NULL;

// Get the query reader.
if (SUCCEEDED(hr))
{
    hr = pFrameDecode->GetMetadataQueryReader(&pQueryReader);
}

if (SUCCEEDED(hr))
{
    // Get the nested IFD reader.
    hr = pQueryReader->GetMetadataByName(L"/app1/ifd", &value);
    if (value.vt == VT_UNKNOWN)
    {
        hr = value.punkVal->QueryInterface(IID_IWICMetadataQueryReader, (void **)&pIFDReader);
    }
    PropVariantClear(&value); // Clear value for new query.
}
```



### GIF Metadata

The Graphics Interchange Format (GIF) image format supports both global and frame level metadata. The following two sections provide the metadata query paths available for GIF's global and frame level metadata.

> [!Note]  
> For a full list of GIF metadata along with more detailed information, see the [GIF standard](https://www.w3.org/Graphics/GIF/spec-gif89a.txt) on the W3C website.

 

### Global Metadata

The following table provides the available metadata query paths that can be used to access global GIF metadata.



| Path                                               | Name                       | Type                                |
|----------------------------------------------------|----------------------------|-------------------------------------|
| /commentext or /\[\*\]commentext where \* = 0 to N | Comment Extension          | VT\_UNKNOWN - A query reader/writer |
| /commentext/TextEntry                              |                            | VT\_LPSTR                           |
| /logscrdesc                                        | Logical Screen Description | VT\_UNKNOWN - A query reader/writer |
| /logscrdesc/Signature                              |                            | VT\_UI1 \| VT\_VECTOR               |
| /logscrdesc/Width                                  |                            | VT\_UI2                             |
| /logscrdesc/Height                                 |                            | VT\_UI2                             |
| /logscrdesc/GlobalColorTableFlag                   |                            | VT\_BOOL                            |
| /logscrdesc/ColorResolution                        |                            | VT\_UI1                             |
| /logscrdesc/SortFlag                               |                            | VT\_BOOL                            |
| /logscrdesc/GlobalColorTableSize                   |                            | VT\_UI1                             |
| /logscrdesc/BackgroundColorIndex                   |                            | VT\_UI1                             |
| /logscrdesc/PixelAspectRatio                       |                            | VT\_UI1                             |
| /appext or /\[\*\]appext where \* = 0 to N         | Application Extension      | VT\_UNKNOWN - A query reader/writer |
| /appext/Application                                |                            | VT\_UI1 \| VT\_VECTOR               |
| /appext/Data                                       |                            | VT\_UI1 \| VT\_VECTOR               |



 

### Frame Metadata

The following table provides the available metadata query paths that can be used to access frame level GIF metadata.



| Path                            | Name                      | Type                              |
|---------------------------------|---------------------------|-----------------------------------|
| /grctlext                       | Graphic Control Extension | VT\_UNKNOWN - query reader/writer |
| /grctlext/Disposal              |                           | VT\_UI1                           |
| /grctlext/UserInputFlag         |                           | VT\_BOOL                          |
| /grctlext/TransparencyFlag      |                           | VT\_BOOL                          |
| /grctlext/Delay                 |                           | VT\_UI2                           |
| /grctlext/TransparentColorIndex |                           | VT\_UI1                           |
| /imgdesc                        | Image Descriptor          | VT\_UNKNOWN - query reader/writer |
| /imgdesc/Left                   |                           | VT\_UI2                           |
| /imgdesc/Top                    |                           | VT\_UI2                           |
| /imgdesc/Width                  |                           | VT\_UI2                           |
| /imgdesc/Height                 |                           | VT\_UI2                           |
| /imgdesc/LocalColorTableFlag    |                           | VT\_BOOL                          |
| /imgdesc/InterlaceFlag          |                           | VT\_BOOL                          |
| /imgdesc/SortFlag               |                           | VT\_BOOL                          |
| /imgdesc/LocalColorTableSize    |                           | VT\_UI1                           |



 

### PNG Metadata

The Portable Network Graphics (PNG) image format supports frame level metadata.

> [!Note]  
> For a full list of PNG metadata along with more detailed information, see the [PNG standard](https://www.w3.org/TR/PNG/) on the W3C website.

 

### Frame Metadata

The following table provides the available metadata query paths that can be used to access frame level PNG metadata.



| Path                                                   | Name             | Type                                      |
|--------------------------------------------------------|------------------|-------------------------------------------|
| /tEXt or /\[\*\]tEXt where \* = 0 to N                 | Text Chunk       | VT\_UNKNOWN - tEXt query reader/writer    |
| /tEXt/{str=\*} where \* = identifying keyword for text |                  | VT\_LPSTR                                 |
| /gAMA                                                  | Gama Chunk       | VT\_UNKNOWN - gAMA query reader/writer    |
| /gAMA/ImageGamma                                       |                  | VT\_UI4                                   |
| /iTXt or /\[\*\]iTXt where \* = 0 to N                 | IText Chunk      | VT\_UNKNOWN - iTXt query reader/writer    |
| /iTXt/Keyword                                          |                  | VT\_LPSTR                                 |
| /iTXt/CompressionFlag                                  |                  | VT\_UI1                                   |
| /iTXt/LanguageTag                                      |                  | LPSTR                                     |
| /iTXt/TranslatedKeyword                                |                  | LPWSTR                                    |
| /iTXt/TextEntry                                        |                  | LPWSTR                                    |
| /cHRM                                                  | HRM Chunk        | VT\_UNKNOWN - cHRM query reader/writer    |
| /cHRM/WhitePointX                                      |                  | VT\_UI4                                   |
| /cHRM/WhitePointY                                      |                  | VT\_UI4                                   |
| /cHRM/RedX                                             |                  | VT\_UI4                                   |
| /cHRM/RedY                                             |                  | VT\_UI4                                   |
| /cHRM/GreenX                                           |                  | VT\_UI4                                   |
| /cHRM/GreenY                                           |                  | VT\_UI4                                   |
| /cHRM/BlueX                                            |                  | VT\_UI4                                   |
| /cHRM/BlueY                                            |                  | VT\_UI4                                   |
| /sRGB                                                  | sRGB Chuck       | VT\_UNKNOWN - sRGB query reader/writer    |
| /sRGB/RenderingIntent                                  |                  | VT\_UI1                                   |
| /tIME                                                  | Time Chunk       | VT\_UNKNOWN - tIME query reader/writer    |
| /tIME/Year                                             |                  | VT\_UI2                                   |
| /tIME/Month                                            |                  | VT\_UI1                                   |
| /tIME/Day                                              |                  | VT\_UI1                                   |
| /tIME/Hour                                             |                  | VT\_UI1                                   |
| /tIME/Minute                                           |                  | VT\_UI1                                   |
| /tIME/Second                                           |                  | VT\_UI1                                   |
| /bKGD                                                  | Background Chunk | VT\_UNKNOWN - bKGB query reader/writer    |
| /bKGD/BackgroundColor                                  |                  | VT\_UI1, VT\_UI2 or VT\_UI2 \| VT\_VECTOR |
| /hIST                                                  | hIST Chunk       | VT\_UNKNOWN - hIST query reader/writer    |
| /hIST/Frequencies                                      |                  | VT\_VECTOR \| VT\_UI2                     |
| /iCCP                                                  | iCCP Chunk       | VT\_UNKNOWN - iCCP query reader/writer    |
| /iCCP/ProfileName                                      |                  | VT\_LPSTR                                 |
| /iCCP/ProfileData                                      |                  | VT\_VECTOR \| VT\_UI1                     |



 

### TIFF Metadata

The Tagged Image File Format (TIFF) image format supports frame level metadata.

> [!Note]  
> For a full list of TIFF metadata along with more detailed information, see [the TIFF standard](https://www.adobe.io/content/dam/udp/en/open/standards/tiff/TIFF6.pdf).

 

### Frame Metadata

The following table provides the available metadata query paths that can be used to access frame level TIFF metadata.



| Path                                          | Name            | Type                                |
|-----------------------------------------------|-----------------|-------------------------------------|
| /ifd                                          | 0 IFD           | VT\_UNKNOWN - A query reader/writer |
| /ifd/{ushort=\*} where \* = 0 to 65535        | IFD Entry by ID | Variable                            |
| /ifd/thumb or /ifd/{ushort=330}               | Thumbnail IFD   | VT\_UNKNOWN - A query reader/writer |
| /ifd/xmp or /ifd/{ushort=700}                 | XMP             | VT\_UNKNOWN - A query reader/writer |
| /ifd/exif or /ifd/{ushort=34665}              | EXIF            | VT\_UNKNOWN - A query reader/writer |
| /ifd/gps or /ifd/{ushort=34853}               | GPS             | VT\_UNKNOWN - A query reader/writer |
| /ifd/exif/interop or /ifd/exif/{ushort=40965} | Interop         | VT\_UNKNOWN - A query reader/writer |
| /ifd/iptc or /ifd/{ushort=33723}              | IPTC            | VT\_UNKNOWN - A query reader/writer |
| /ifd/iptc/{str=\*} where \* = IPTC keyword    | IPTC Entry      | Variable                            |
| /ifd/irb/8bimiptc/iptc                        | IPTC            | VT\_UNKNOWN - A query reader/writer |
| /ifd/irb/8bimiptc/iptc/{str=\*}               | IPTC Entry      | Variable                            |



 

### JPEG Metadata

The JPEG image format supports frame level metadata.

> [!Note]  
> For full list of JPEG metadata along with more detailed information, see the [EXIF JPEG standard](http://www.cipa.jp/std/documents/e/DC-008-2010_E.pdf).

 

### Frame Metadata

The following table provides the available metadata query paths that can be used to access frame level JPEG metadata.



| Path                                                               | Name                 | Type                                          |
|--------------------------------------------------------------------|----------------------|-----------------------------------------------|
| /app0                                                              | App0                 | VT\_UNKNOWN - App0 Query Reader/Writer        |
| /app0/{ushort=0}                                                   | Version              | VT\_UI2                                       |
| /app0/{ushort=1}                                                   | Units                | VT\_UI1                                       |
| /app0/{ushort=2}                                                   | DpiX                 | VT\_UI2                                       |
| /app0/{ushort=3}                                                   | DpiY                 | VT\_UI2                                       |
| /app0/{ushort=4}                                                   | Xthumbnail           | VT\_UI1                                       |
| /app0/{ushort=5}                                                   | Ythumbnail           | VT\_UI1                                       |
| /app0/{ushort=6}                                                   | ThumbnailData        | VT\_BLOB                                      |
| /app1                                                              | App1                 | VT\_UNKNOWN - App1 Query Reader/Writer        |
| /app1/ifd or /app1/{ushort=0}                                     | 0 IFD                | VT\_UNKNOWN - IFD Query Reader/Writer         |
| /app1/ifd/exif or /app1/ifd/{ushort=34665}                         | EXIF IFD             | VT\_UNKNOWN – EXIF Query Reader/Writer        |
| /app1/thumb or /app1/{ushort=1}                                   | Thumbnail IFD        | VT\_UNKNOWN - SubIFD Query Reader/Writer      |
| /app13                                                             | App13                | VT\_UNKNOWN - App13 Query Reader/Writer       |
| /app13/irb or /app13/{ushort=0}                                    | IRB                  | VT\_UNKNOWN - IRB Query Reader/Writer         |
| /app13/irb/{ulonglong=\*} where \* = IRB Identifier (see IRB spec) | IRB Entry            | VT\_UNKNOWN - Unknown Query Reader/Writer     |
| /app13/irb/{ulonglong=\*}/{}                                       | IRB Entry Contents   | VT\_BLOB                                      |
| /app13/irb/8bimiptc or /app13/irb/{ulonglong=61857348781060}       | 8BIMIPTC             | VT\_UNKNOWN - 8BIMIPTC Query Reader/Writer    |
| /app13/irb/8bimiptc/iptc                                           | IPTC                 | VT\_UNKNOWN - IPTC Query Reader/Writer        |
| /app13/irb/8bimiptc/iptc/{str=\*}                                  | IPTC Entry           | Variable                                      |
| /app13/irb/8bimResInfo or /app13/irb/{ulonglong=61857348781037}    | 8BIM Resolution Info | VT\_UNKNOWN - Query Reader/Writer             |
| /app13/irb/8bimResInfo/PString                                     |                      | VT\_LPSTR                                     |
| /app13/irb/8bimResInfo/HResolution                                 |                      | VT\_UI4                                       |
| /app13/irb/8bimResInfo/VResolution                                 |                      | VT\_UI4                                       |
| /app13/irb/8bimResInfo/WidthUnit                                   |                      | VT\_UI2                                       |
| /app13/irb/8bimResInfo/HeightUnit                                  |                      | VT\_UI2                                       |
| /app13/irb/8bimResInfo/HResolutionUnit                             |                      | VT\_UI2                                       |
| /app13/irb/8bimResInfo/VResolutionUnit                             |                      | VT\_UI2                                       |
| /com                                                               | JPEG Comment         | VT\_UNKNOWN - Comment Query Reader/Writer     |
| /com/TextEntry                                                     |                      | LPSTR                                         |
| /luminance                                                         | Luminance            | VT\_UNKNOWN - Luminance Query Reader/Writer   |
| /luminance/TableEntry                                              |                      | VT\_UI1 \| VT\_VECTOR                         |
| /chrominance                                                       | Chrominance          | VT\_UNKNOWN - Chrominance Query Reader/Writer |
| /chrominance/TableEntry                                            |                      | VT\_UI1 \| VT\_VECTOR                         |
| /xmp                                                               | XMP                  | VT\_UNKNOWN - XMP Query Reader/Writer         |



 

## File Format Independent Metadata

The following sections contain information concerning metadata formats that are supported by multiple image formats. Each table has the following columns:

-   **Relative Path** - The query path used to retrieve the metadata item, relative to the metadata block.
-   **Name** - The name of the metadata item.
-   **Type** - The type of the metadata item retrieved from the query path. Metadata retrieved by [WIC](-wic-api.md) is returned in the form of PROPVARIANT, which reports the data type using the VARTYPE enumeration.

> [!Note]  
> The tables here only provide the relative path to access a metadata item within the particular metadata format. To get the fully qualified metadata query, append this relative path to the metadata block query for the particular metadata format.

 

For example, to access the [Orientation](-wic-photoprop-system-photo-orientation.md) flag in a JPEG file, use the following expression:

-   /app1/ifd/{ushort=274}

In a TIFF file, use the following expression:

-   /ifd/{ushort=274}

In this example, note that different image formats may store a particular metadata block differently, and so the fully qualified metadata query to access a particular metadata item may be image format specific. See each format’s table to find the appropriate metadata query to access a particular metadata block.

### IFD Metadata

An IFD, or Image File Directory, is a data structure defined in the TIFF standard that can contain image metadata. It identifies each metadata item using a tag of type ushort. JPEG, TIFF, and JPEG-XR support IFD metadata. Third party formats, like some camera raw formats, may also support IFD metadata.

The table here provides relative metadata query paths to access some commonly used IFD metadata items. The IFD data structure allows for third party extensibility and this table is not an exhaustive list. See the TIFF standard for more information.

> [!Note]  
> Although JPEG and other formats support the IFD data structure, they may not use all of the metadata items that it defines. Refer to each format’s standard for more information.

 

> [!Note]  
> Certain metadata items in the table here require additional interpretation or information to properly use, refer to the TIFF standard. For example, the [PhotometricInterpretation](-wic-photoprop-system-photo-photometricinterpretation.md) metadata item returns a PROPVARIANT of type VT\_UI2. However, according to the TIFF standard it is interpreted as an enumeration. See the TIFF standard for more information.

 



| Relative Path   | Name                      | Type                                           |
|-----------------|---------------------------|------------------------------------------------|
| /{ushort=256}   | ImageWidth                | VT\_UI2 or VT\_UI4                             |
| /{ushort=257}   | ImageLength               | VT\_UI2 or VT\_UI4                             |
| /{ushort=258}   | BitsPerSample             | VT\_UI2                                        |
| /{ushort=259}   | Compression               | VT\_UI2                                        |
| /{ushort=262}   | PhotometricInterpretation | VT\_UI2                                        |
| /{ushort=274}   | Orientation               | VT\_UI2                                        |
| /{ushort=277}   | SamplesPerPixel           | VT\_UI2                                        |
| /{ushort=284}   | PlanarConfiguration       | VT\_UI2                                        |
| /{ushort=530}   | YCbCrSubSampling          | VT\_VECTOR \| VT\_UI2                          |
| /{ushort=531}   | YCbCrPositioning          | VT\_UI2                                        |
| /{ushort=282}   | XResolution               | VT\_UI8                                        |
| /{ushort=283}   | YResolution               | VT\_UI8                                        |
| /{ushort=296}   | ResolutionUnit            | VT\_UI2                                        |
| /{ushort=306}   | DateTime                  | VT\_LPSTR                                      |
| /{ushort=270}   | ImageDescription          | VT\_LPSTR                                      |
| /{ushort=271}   | Make                      | VT\_LPSTR                                      |
| /{ushort=272}   | Model                     | VT\_LPSTR                                      |
| /{ushort=305}   | Software                  | VT\_LPSTR                                      |
| /{ushort=315}   | Artist                    | VT\_LPSTR                                      |
| /{ushort=33432} | Copyright                 | VT\_LPSTR                                      |
| /{ushort=338}   | ExtraSamples              | VT\_UI2                                        |
| /{ushort=254}   | NewSubfileType            | VT\_UI4                                        |
| /{ushort=278}   | RowsPerStrip              | VT\_UI2 or VT\_UI4                             |
| /{ushort=279}   | StripByteCounts           | VT\_VECTOR \| VT\_UI2 or VT\_VECTOR \| VT\_UI4 |
| /{ushort=273}   | StripOffsets              | VT\_VECTOR \| VT\_UI2 or VT\_VECTOR \| VT\_UI4 |



 

### EXIF Metadata

EXIF metadata is defined as part of the EXIF JPEG specification. EXIF metadata is based on the IFD data structure as defined in the TIFF standard, and provides additional attributes such as information about the devices and photographic attributes used to create the image. It identifies each metadata item using a tag of type ushort. JPEG, TIFF, and JPEG-XR support EXIF metadata. Third party formats, such as some camera raw formats, may also support EXIF metadata.

The following table provides relative metadata query paths to access some commonly used EXIF metadata items. The EXIF data structure allows for third party extensibility and this table is not an exhaustive list; refer to the EXIF standard for more information.

> [!Note]  
> Many EXIF metadata items are defined in the EXIF standard as type "RATIONAL" or "SRATIONAL". A "RATIONAL" consists of a numerator and denominator, both of which are 32 bit unsigned integers. The numerator is contained in the high 32 bits, and the denominator in the low 32 bits. In [WIC](-wic-api.md), these are returned as PROPVARIANT with a type of VT\_UI8 or VT\_I8, respectively; the actual value is stored as ULARGE\_INTEGER or LARGE\_INTEGER, respectively. To access the numerator and denominator, read the HighPart and LowPart members of the ULARGE\_INTEGER or LARGE\_INTEGER value.

 

> [!Note]  
> Certain metadata items in the below table require additional interpretation or information to properly use. For example, the [ColorSpace](-wic-photoprop-system-image-colorspace.md) metadata item returns a PROPVARIANT of type VT\_UI2. However, according to the EXIF standard it is interpreted as an enumeration. See the EXIF standard for more information.

 



| Relative Path   | Name                      | Type                  |
|-----------------|---------------------------|-----------------------|
| /{ushort=36864} | ExifVersion               | VT\_BLOB              |
| /{ushort=40960} | FlashpixVersion           | VT\_BLOB              |
| /{ushort=40961} | ColorSpace                | VT\_UI2               |
| /{ushort=40962} | PixelXDimension           | VT\_UI2 or VT\_UI4    |
| /{ushort=40963} | PixelYDimension           | VT\_UI2 or VT\_UI4    |
| /{ushort=37500} | MakerNote                 | VT\_BLOB              |
| /{ushort=37510} | UserComment               | VT\_LPWSTR            |
| /{ushort=36867} | DateTimeOriginal          | VT\_LPSTR             |
| /{ushort=36868} | DateTimeDigitized         | VT\_LPSTR             |
| /{ushort=42016} | ImageUniqueID             | VT\_LPSTR             |
| /{ushort=42032} | CameraOwnerName           | VT\_LPSTR             |
| /{ushort=42033} | BodySerialNumber          | VT\_LPSTR             |
| /{ushort=42034} | LensSpecification         | VT\_VECTOR \| VT\_UI8 |
| /{ushort=42035} | LensMake                  | VT\_LPSTR             |
| /{ushort=42036} | LensModel                 | VT\_LPSTR             |
| /{ushort=42037} | LensSerialNumber          | VT\_LPSTR             |
| /{ushort=33434} | ExposureTime              | VT\_UI8               |
| /{ushort=33437} | FNumber                   | VT\_UI8               |
| /{ushort=34850} | ExposureProgram           | VT\_UI2               |
| /{ushort=34852} | SpectralSensitivity       | VT\_LPSTR             |
| /{ushort=34855} | PhotographicSensitivity   | VT\_VECTOR \| VT\_UI2 |
| /{ushort=34856} | OECF                      | VT\_BLOB              |
| /{ushort=34864} | SensitivityType           | VT\_UI2               |
| /{ushort=34865} | StandardOutputSensitivity | VT\_UI4               |
| /{ushort=34866} | RecommendedExposureIndex  | VT\_UI4               |
| /{ushort=34867} | ISOSpeed                  | VT\_UI4               |
| /{ushort=34868} | ISOSpeedLatitudeyyy       | VT\_UI4               |
| /{ushort=34869} | ISOSpeedLatitudezzz       | VT\_UI4               |
| /{ushort=37377} | ShutterSpeedValue         | VT\_I8                |
| /{ushort=37378} | ApertureValue             | VT\_UI8               |
| /{ushort=37379} | BrightnessValue           | VT\_I8                |
| /{ushort=37380} | ExposureBiasValue         | VT\_I8                |
| /{ushort=37381} | MaxApertureValue          | VT\_UI8               |
| /{ushort=37382} | SubjectDistance           | VT\_UI8               |
| /{ushort=37383} | MeteringMode              | VT\_UI2               |
| /{ushort=37384} | LightSource               | VT\_UI2               |
| /{ushort=37385} | Flash                     | VT\_UI2               |
| /{ushort=37386} | FocalLength               | VT\_UI8               |
| /{ushort=37396} | SubjectArea               | VT\_VECTOR \| VT\_UI2 |
| /{ushort=41483} | FlashEnergy               | VT\_UI8               |
| /{ushort=41484} | SpatialFrequencyResponse  | VT\_BLOB              |
| /{ushort=41486} | FocalPlaneXResolution     | VT\_UI8               |
| /{ushort=41487} | FocalPlaneYResolution     | VT\_UI8               |
| /{ushort=41488} | FocalPlaneResolutionUnit  | VT\_UI2               |
| /{ushort=41492} | SubjectLocation           | VT\_VECTOR \| VT\_UI2 |
| /{ushort=41493} | ExposureIndex             | VT\_UI8               |
| /{ushort=41495} | SensingMethod             | VT\_UI2               |
| /{ushort=41728} | FileSource                | VT\_BLOB              |
| /{ushort=41729} | SceneType                 | VT\_BLOB              |
| /{ushort=41730} | CFAPattern                | VT\_BLOB              |
| /{ushort=41985} | CustomRendered            | VT\_UI2               |
| /{ushort=41986} | ExposureMode              | VT\_UI2               |
| /{ushort=41987} | WhiteBalance              | VT\_UI2               |
| /{ushort=41988} | DigitalZoomRatio          | VT\_UI8               |
| /{ushort=41989} | FocalLengthIn35mmFilm     | VT\_UI2               |
| /{ushort=41990} | SceneCaptureType          | VT\_UI2               |
| /{ushort=41991} | GainControl               | VT\_UI8               |
| /{ushort=41992} | Contrast                  | VT\_UI2               |
| /{ushort=41993} | Saturation                | VT\_UI2               |
| /{ushort=41994} | Sharpness                 | VT\_UI2               |
| /{ushort=41995} | DeviceSettingDescription  | VT\_BLOB              |
| /{ushort=41996} | SubjectDistanceRange      | VT\_UI2               |



 

### GPS Metadata

GPS metadata contains geolocation information and is defined as part of the EXIF JPEG specification. It identifies each metadata item using a tag of type ushort. JPEG, TIFF, and JPEG-XR support GPS metadata; third party formats, like some camera raw formats, may also support GPS metadata.

The following table provides relative metadata query paths to access some commonly used GPS metadata items. This table is not an exhaustive list; refer to the EXIF standard for more information.

> [!Note]  
> Many GPS metadata items are defined in the EXIF standard as type "RATIONAL". A "RATIONAL" consists of a numerator and denominator, both of which are 32 bit unsigned integers. The numerator is contained in the high 32 bits, and the denominator in the low 32 bits. In [WIC](-wic-api.md), these are returned as PROPVARIANT with a type of VT\_UI8. The actual value is stored as ULARGE\_INTEGER. To access the numerator and denominator, read the HighPart and LowPart members of the ULARGE\_INTEGER value.

 

> [!Note]  
> Certain metadata items in the table here require additional interpretation or information to properly use. For example, the GPSLatitudeRef metadata item returns a PROPVARIANT of type VT\_LPSTR. According to the EXIF standard this string is either "N" or "S", representing North or South latitude. See the EXIF standard for more information.

 



| Relative Path | Name            | Type                                          |
|---------------|-----------------|-----------------------------------------------|
| {ushort=0}    | GPSVersionID    | VT\_VECTOR \| VT\_UI1                         |
| {ushort=1}    | GPSLatitudeRef  | VT\_LPSTR                                     |
| {ushort=2}    | GPSLatitude     | VT\_VECTOR \| VT\_UI8                         |
| {ushort=3}    | GPSLongitudeRef | VT\_LPSTR                                     |
| {ushort=4}    | GPSLongitude    | {ushort=4} GPSLongitude VT\_VECTOR \| VT\_UI8 |
| {ushort=5}    | GPSAltitudeRef  | VT\_UI1                                       |
| {ushort=6}    | GPSAltitude     | VT\_UI8                                       |
| {ushort=7}    | GPSTimeStamp    | VT\_VECTOR \| VT\_UI8                         |
| {ushort=8}    | GPSSatellites   | VT\_LPSTR                                     |
| {ushort=9}    | GPSStatus       | VT\_LPSTR                                     |
| {ushort=10}   | GPSMeasureMode  | VT\_LPSTR                                     |
| {ushort=11}   | GPSDOP          | VT\_UI8                                       |
| {ushort=12}   | GPSSpeedRef     | VT\_LPSTR                                     |
| {ushort=13}   | GPSSpeed        | VT\_UI8                                       |
| {ushort=14}   | GPSTrackRef     | VT\_LPSTR                                     |
| {ushort=15}   | GPSTrack        | VT\_UI8                                       |



 

### XMP Metadata

XMP is an XML-based, extensible metadata standard. Metadata items can be hierarchical and contain complex data structures. JPEG, TIFF, and JPEG-XR support XMP metadata. Third party formats, like some camera raw formats, may also support XMP metadata.

The XMP standard can be obtained from: <https://www.adobe.com/devnet/xmp.html>.

XMP and allows third party entities to publish their own schemas, or namespaces, which allow them to define new metadata items without having to modify the XMP standard. An XMP schema is uniquely identified by a URL, but [WIC](-wic-api.md) provides a set of friendly identifiers for well-known schemas.

XMP metadata items are identified by a string name as well as a schema identifier. As a best practice, every XMP metadata query should specify both the schema and name. If the schema identifier is missing, then JPEG will attempt to match the metadata name across all of the namespaces present within the XMP metadata packet.

For example, to obtain the Rating property as defined by the XMP schema in a JPEG image, use the following query:

-   /xmp/{wstr=https://ns.adobe.com/xap/1.0/}:Rating

The first part, "/xmp", retrieves the XMP metadata reader/writer for the image. "https://ns.adobe.com/xap/1.0/" is the URL of the XMP schema, as defined in the XMP standard. The URL is enclosed in a data expression to allow the use of characters such as a forward slash (/). Finally, "Rating" is the actual metadata item name as defined by the XMP schema and it is separated from the schema identifier by a colon (:).

In this example, WIC provides a friendly identifier for the XMP schema which can be used in place of the full URL. So, the previous query can be rewritten as:

-   /xmp/xmp:Rating

[WIC](-wic-api.md) provides friendly schema prefixes for the following commonly used schemas:



| Schema Prefix  | Schema URL                                        | Link to Standard                                         |
|----------------|---------------------------------------------------|----------------------------------------------------------|
| rdf            | https://www.w3.org/1999/02/22-rdf-syntax-ns\#      | <https://www.w3.org/TR/REC-rdf-syntax/>                   |
| dc             | https://purl.org/dc/elements/1.1/                  | <https://www.adobe.com/devnet/xmp.html>                   |
| xmp            | https://ns.adobe.com/xap/1.0/                      | <https://www.adobe.com/devnet/xmp.html>                   |
| xmpidq         | https://ns.adobe.com/xmp/Identifier/qual/1.0/      | <https://www.adobe.com/devnet/xmp.html>                   |
| xmpRights      | https://ns.adobe.com/xap/1.0/rights/               | <https://www.adobe.com/devnet/xmp.html>                   |
| xmpMM          | https://ns.adobe.com/xap/1.0/mm/                   | <https://www.adobe.com/devnet/xmp.html>                   |
| xmpBJ          | https://ns.adobe.com/xap/1.0/bj/                   | <https://www.adobe.com/devnet/xmp.html>                   |
| xmpTPg         | https://ns.adobe.com/xap/1.0/t/pg/                 | <https://www.adobe.com/devnet/xmp.html>                   |
| pdf            | https://ns.adobe.com/pdf/1.3/                      | <https://www.adobe.com/devnet/xmp.html>                   |
| photoshop      | https://ns.adobe.com/photoshop/1.0/                | <https://www.adobe.com/devnet/xmp.html>                   |
| tiff           | https://ns.adobe.com/tiff/1.0/                     | <https://www.adobe.com/devnet/xmp.html>                   |
| exif           | https://ns.adobe.com/exif/1.0/                     | <https://www.adobe.com/devnet/xmp.html>                   |
| stDim          | https://ns.adobe.com/xap/1.0/sType/Dimensions\#    | <https://www.adobe.com/devnet/xmp.html>                   |
| xapGImg        | https://ns.adobe.com/xap/1.0/g/img/                | <https://www.adobe.com/devnet/xmp.html>                   |
| stEvt          | https://ns.adobe.com/xap/1.0/sType/ResourceEvent\# | <https://www.adobe.com/devnet/xmp.html>                   |
| stRef          | https://ns.adobe.com/xap/1.0/sType/ResourceRef\#   | <https://www.adobe.com/devnet/xmp.html>                   |
| stVer          | https://ns.adobe.com/xap/1.0/sType/Version\#       | <https://www.adobe.com/devnet/xmp.html>                   |
| stJob          | https://ns.adobe.com/xap/1.0/sType/Job\#           | <https://www.adobe.com/devnet/xmp.html>                   |
| aux            | https://ns.adobe.com/exif/1.0/aux/                 | <https://www.adobe.com/devnet/xmp.html>                   |
| crs            | https://ns.adobe.com/camera-raw-settings/1.0/      | <https://www.adobe.com/devnet/xmp.html>                   |
| xmpDM          | https://ns.adobe.com/xmp/1.0/DynamicMedia/         | <https://www.adobe.com/devnet/xmp.html>                   |
| Iptc4xmpCore   | https://iptc.org/std/Iptc4xmpCore/1.0/xmlns/       | <https://www.iptc.org/cms/site/index.html?channel=CH0099> |
| MicrosoftPhoto | https://ns.microsoft.com/photo/1.0/                | [People Tagging Overview](-wic-people-tagging.md)       |
| MP             | https://ns.microsoft.com/photo/1.2/                | [People Tagging Overview](-wic-people-tagging.md)       |
| MPRI           | https://ns.microsoft.com/photo/1.2/t/RegionInfo\#  | [People Tagging Overview](-wic-people-tagging.md)       |
| MPReg          | https://ns.microsoft.com/photo/1.2/t/Region\#      | [People Tagging Overview](-wic-people-tagging.md)       |



 

If there is no friendly schema prefix for a particular schema, for example if an image contains XMP metadata using a custom third party schema, the metadata query should use the full schema URL.

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md)
</dt> <dt>

[WIC Metadata Overview](-wic-about-metadata.md)
</dt> <dt>

[Metadata Query Language Overview](-wic-codec-metadataquerylanguage.md)
</dt> <dt>

[Metadata Extensibility Overview](-wic-codec-metadatahandlers.md)
</dt> <dt>

[How-to: Re-encode a JPEG Image with Metadata](-wic-codec-jpegmetadataencoding.md)
</dt> </dl>

 

 
