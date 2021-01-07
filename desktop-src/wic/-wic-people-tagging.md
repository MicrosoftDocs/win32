---
description: This topic introduces the new Extensible Metadata Platform (XMP) schema and the Windows 7 photo property System.Photo.PeopleNames that enables the tagging of individuals in a digital photo.
ms.assetid: 557c3e9a-1756-4abb-8465-b12195ecbc91
title: People Tagging Overview
ms.topic: article
ms.date: 05/31/2018
---

# People Tagging Overview

This topic introduces the new Extensible Metadata Platform (XMP) schema and the Windows 7 photo property [System.Photo.PeopleNames](../properties/props-system-photo-peoplenames.md) that enables the tagging of individuals in a digital photo. This topic also discusses how to use the Windows Imaging Component (WIC) API to both read and write the metadata needed for people tagging.

This topic contains the following sections.

-   [Prerequisites](#prerequisites)
-   [Introduction](#introduction)
-   [People Tagging](#people-tagging-overview)
    -   [People Names](#people-names)
    -   [People Rectangles](#people-rectangles)
-   [Schema Reference](#schema-reference)
    -   [Microsoft Photo 1.2 Schema](#microsoft-photo-12-schema)
    -   [Microsoft Photo RegionInfo Schema](#microsoft-photo-regioninfo-schema)
    -   [Microsoft Photo Region Schema](#microsoft-photo-regioninfo-schema)
    -   [Sample Metadata](#sample-metadata)
-   [Related topics](#related-topics)

## Prerequisites

To understand this topic, you should be familiar with the WIC decoder interfaces and its related Component Object Model (COM) components, as described in the [Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md). It also helps to have a general familiarity with imaging metadata, especially XMP.

## Introduction

Microsoft has created a new XMP schema for tagging people within a digital image. This schema enables applications to store the names and locations of individuals who are in the image as metadata within the image. In addition to the new schema, the new photo property [System.Photo.PeopleNames](../properties/props-system-photo-peoplenames.md) is available in Windows 7. This new property enables applications to read the individual's names stored in the image metadata. WIC utilizes these new features by enabling applications to easily read and write people tagging metadata to digital photos.

## People Tagging

WIC provides application developers with COM components which read image data as well as image metadata. For reading and writing metadata, such as the new people tagging feature, WIC provides the [**IWICMetadataQueryReader**](/windows/desktop/api/Wincodec/nn-wincodec-iwicmetadataqueryreader) and [**IWICMetadataQueryWriter**](/windows/desktop/api/Wincodec/nn-wincodec-iwicmetadataquerywriter) interfaces. These interfaces enable applications to use the [metadata query language](-wic-codec-metadataquerylanguage.md) to write metadata to the individual frames of an image. The following section demonstrates how to read and write the people-tagging metadata into an image's metadata by using WIC query readers and writers.

### People Names

Part of the people-tagging feature is the ability to simply get a list the names of the people tagged within the image. This part of the feature is supported by the [System.Photo.PeopleNames](../properties/props-system-photo-peoplenames.md) and WIC's metadata handlers. The [**IWICMetadataQueryReader**](/windows/desktop/api/Wincodec/nn-wincodec-iwicmetadataqueryreader) interface, in conjunction with the System.Photo.PeopleNames property, are used to read the names of people identified in an image and stored in the image metadata.

The following code example demonstrates a query reader obtained from an image frame to query an image's metadata for tagged names of the [System.Photo.PeopleNames](../properties/props-system-photo-peoplenames.md) property.


```C++
// Not shown: image decoding, retrieving an image frame. 
...
PROPVARIANT value;
IWICMetadataQueryReader *pQueryReader = NULL;
...
// Get the query reader.
if (SUCCEEDED(hr))
{
    hr = pFrameDecode->GetMetadataQueryReader(&pQueryReader);
}

// Query for the System.Photo.PeopleNames property.
if (SUCCEEDED(hr))
{
    // Get the property metadata by property name.
    hr = pQueryReader->GetMetadataByName(L"System.Photo.PeopleNames", &value);
}
```



The query expression "System.Photo.PeopleNames" queries the frame for the property. If the people-tagging metadata exists and contains people's names, the [PROPVARIANT](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) value will be set to VT\_LPWSTR and the data value will contain the list of tagged names. For more information on reading image metadata, see [Overview of Reading and Writing Image Metadata](-wic-codec-readingwritingmetadata.md).

Querying for the people names tag is only useful if the image actually contains the people-tagging metadata. For this to occur, an application must first have written it. To write the people names metadata, use an [**IWICMetadataQueryWriter**](/windows/desktop/api/Wincodec/nn-wincodec-iwicmetadataquerywriter) and the explicit XMP path of the metadata. The following code example demonstrates using a query writer to write a name to the query path.


```C++
// Not shown: image encoding, retrieving/creating the image frame,
// creating the IWICImagingFactory 
...
IWICImagingFactory *pFactory = NULL;
IWICMetadataQueryWriter *pQueryWriter = NULL;
...
// Get the query writer from the image frame.
if (SUCCEEDED(hr))
{
    hr = pFrameEncode->GetMetadataQueryWriter(&pQueryWriter);
}

// A query writer specifically for this person's XMP struct
IWICMetadataQueryWriter *pXMPStructQueryWriter = NULL;

// Create a query writer specifically for an XMP Struct
hr = pFactory->CreateQueryWriter(
    GUID_MetadataFormatXMPStruct,
    NULL,
    &pXMPStructQueryWriter
    );

// Create a variant representing the structure created above
PROPVARIANT xmpStruct;
PropVariantInit(&xmpStruct);

// VT_UNKNOWN indicates that we're setting a COM object, in this case a XMPStruct
// which will hold the name and rectangle
xmpStruct.vt = VT_UNKNOWN; 
xmpStruct.punkVal = pXMPStructQueryWriter;

if(SUCCEEDED(hr))
{
    // WIC will automatically create the xmp base, the RegionInfo struct, and the Regions
    // bag (an unordered array) but structs within that bag need to be explicitly created.
    // The {ulong=0} in the query means to insert the new struct at the start of the bag,
    // {} could also be used to insert at the end of the bag.
    hr = pQueryWriter->SetMetadataByName(
        L"/xmp/<xmpstruct>MP:RegionInfo/<xmpbag>MPRI:Regions/{ulong=0}",
        &xmpStruct
        );
}

// Set up the PROPVARIANT with the name information
PROPVARIANT personName;
PropVariantInit(&personName);
personName.vt = VT_LPWSTR;
personName.pwszVal = L"John Doe";

if(SUCCEEDED(hr))
{
    // Set the name metadata
    hr = pQueryWriter->SetMetadataByName(
        L"/xmp/MP:RegionInfo/MPRI:Regions/{ulong=0}/MPReg:PersonDisplayName",
        &personName
        );  
}
```



Note the step constructing the XMP structure and setting it under `MPRI:Regions/{ulong=0}`. Without this step, the WIC can't identify where to place the `PersonDisplayName` later on. Also note that the explicit query path is used instead of [System.Photo.PeopleNames](-wic-photoprop-system-photo-peoplenames.md), whose metadata policy does not support writing metadata.

### People Rectangles

People's names however, are only part of the people-tagging feature. In addition to storing people's names in the metadata, the schema also supports region information that identifies the specific area (a rectangle) the person is shown in the image.

The rectangle information is represented by four comma-delimited decimal values, such as "0.25, 0.25, 0.25, 0.25". The first two values specify the top-left coordinate; the final two specify the height and width of the rectangle. The dimensions of the image for the purposes of defining people rectangles are normalized to 1, which means that in the "0.25, 0.25, 0.25, 0.25" example, the rectangle starts 1/4 of the distance from the top and 1/4 of the distance from the left of the image. Both the height and width of the rectangle are 1/4 of the size of their respective image dimensions.

The rectangle information that identifies individuals is written in the same way people's names are written, within the same structure. To write the rectangle metadata, use an [**IWICMetadataQueryWriter**](/windows/desktop/api/Wincodec/nn-wincodec-iwicmetadataquerywriter) and the explicit XMP path of the metadata. The following code example continues the previous example and adds a rectangle representing 'John Doe' to the image's metadata. Note that it uses the same `{ulong=0}` index to associate this rectangle with 'John Doe'.


```C++
// Set up the PROPVARIANT with the rectangle information
PROPVARIANT rectangle;
PropVariantInit(&rectangle);
rectangle.vt = VT_LPWSTR;
rectangle.pwszVal = L"0.0,0.0,0.25,0.25";

if(SUCCEEDED(hr))
{
    // Set the rectangle metadata
    hr = pQueryWriter->SetMetadataByName(
        L"/xmp/MP:RegionInfo/MPRI:Regions/{ulong=0}/MPReg:Rectangle",
        &rectangle
        );
}
```



## Schema Reference

The Microsoft XMP schemas for people tagging define a set of properties to tag individuals in digital photos.

The following sections provide the schema definitions needed for people tagging. Wherever possible, the schema definitions use the conventions provided by [Adobe's Extensible Metadata Platform (XMP) Specifications](https://www.adobe.com/devnet/xmp/). The schema definitions in this topic show the XML namespace Uniform Resource Identifier (URI) that identifies the schema and the preferred schema namespace prefix, followed by a table that lists all properties defined for the schema. Each table has the following columns:

-   **Property** - The name of the property, including the preferred namespace prefix.

-   **Value type** - The value type of the property. The people-tagging support schemas use the XMP value types whenever possible, including Date and Text. Array types are preceded by the container type: `alt`, `bag`, or `seq`.

-   **Category** - Schema properties are internal or external:

    -   Internal metadata must be set by the application.

    -   External metadata must be set by the user and is independent of the contents of the document.

-   **Description** - The description of the property.

### Microsoft Photo 1.2 Schema

The Microsoft Photo 1.2 schema provides a set of properties for image regions.

-   The schema namespace URI is `https://ns.microsoft.com/photo/1.2/`.
-   The preferred schema namespace prefix is `MP`.



| Property      | Value type | Category | Description                                                                                                                     |
|---------------|------------|----------|---------------------------------------------------------------------------------------------------------------------------------|
| MP:RegionInfo | RegionInfo | Internal | **required** : Stores the root of the people-tagging metadata. See the Microsoft Photo RegionInfo Schema section which follows. |



 

### Microsoft Photo RegionInfo Schema

The Microsoft Photo RegionInfo 1.2 schema provides a set of properties for region info.

-   The schema namespace URI is `https://ns.microsoft.com/photo/1.2/t/RegionInfo#`.
-   The preferred schema namespace prefix is `MPRI`.



| Property              | Value type | Category | Description                                                                                                    |
|-----------------------|------------|----------|----------------------------------------------------------------------------------------------------------------|
| MPRI:DateRegionsValid | Date       | External | **optional** : Date that the last region was created.                                                          |
| MPRI:Regions          | bag Region | External | **required** : Stores the people tagging regions. See the Microsoft Photo Region Schema section which follows. |



 

### Microsoft Photo Region Schema

The Microsoft Photo Region 1.2 schema provides a set of properties for image regions.

-   The schema namespace URI is `https://ns.microsoft.com/photo/1.2/t/Region#`.
-   The preferred schema namespace prefix is `MPReg`.



| MPReg:Property          | Value type | Category | Description                                                                                                                                                                                                                                                                                                     |
|-------------------------|------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MPReg:PersonDisplayName | Text       | External | **required** : Stores the name of the person in the given rectangle.                                                                                                                                                                                                                                            |
| MPReg:Rectangle         | Text       | External | **optional** : Stores the rectangle that identifies the person within the photo. The rectangle is stored as four comma-delimited decimal values. The first two values specify the top left coordinate; the final two specify the height and width of the rectangle. The decimal values must be normalized to 1. |
| MPReg:PersonEmailDigest | Text       | External | **optional** : Stores the SHA-1 encrypted message hash of the person's Live e-mail address.                                                                                                                                                                                                                     |
| MPReg:PersonLiveIdCID   | Text       | External | **optional** :Stores the signed decimal representation of the person's Live CID, a 64-bit integer that publicly identifies a Live identity.                                                                                                                                                                     |



 

### Sample Metadata

The following is a representation of the XMP metadata for people tagging.

``` syntax
<rdf:Description rdf:about="" xmlns:MP="https://ns.microsoft.com/photo/1.2/">
<MP:RegionInfo> 
<rdf:Description xmlns:MPRI="https://ns.microsoft.com/photo/1.2/t/RegionInfo#">
   <MPRI:Regions> 
       <rdf:Bag> 
          <rdf:li> 
       <rdf:Description xmlns:MPReg="https://ns.microsoft.com/photo/1.2/t/Region#"> 
           <MPReg:Rectangle>0.790650, 0.441734, 0.209350, 0.279133
           </MPReg:Rectangle>
           <MPReg:PersonDisplayName>John Doe</MPReg:PersonDisplayName> 
           <MPReg:PersonEmailDigest>2FD4E1C67A2D28FCED849EE1BB76E7391B93EB13</MPReg:PersonEmailDigest> 
           <MPReg:PersonLiveIdCID>1234567890123456789</MPReg:PersonLiveIdCID> 
       </rdf:Description> 
         </rdf:li> 
         <rdf:li>
             <rdf:Description xmlns:MPReg="https://ns.microsoft.com/photo/1.2/t/Region#">
                  <MPReg:Rectangle>0.222656, 0.302083, 0.378906, 0.505208</MPReg:Rectangle> 
                  <MPReg:PersonDisplayName>Jane Doe</MPReg:PersonDisplayName> 
              </rdf:Description> 
         </rdf:li> 
<!-- Addition Regions --> ... 
<rdf:li>...
</rdf:li> 
</rdf:Bag> 
</MPRI:Regions> </rdf:Description> </MP:RegionInfo> </rdf:Description>
```

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md)
</dt> <dt>

[WIC Metadata Overview](-wic-about-metadata.md)
</dt> <dt>

[Overview of Reading and Writing Image Metadata](-wic-codec-readingwritingmetadata.md)
</dt> <dt>

[Metadata Query Language Overview](-wic-codec-metadataquerylanguage.md)
</dt> </dl>

 

 
