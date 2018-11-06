---
title: The DocumentSummaryInformation and UserDefined Property Sets
description: A DocumentSummaryInformation and UserDefined property set is an extension to the Summary Information property set. Both property sets can exist simultaneously.
ms.assetid: c6d4e2bc-f7f6-429d-aa91-432d833c69d1
keywords:
- DocumentSummaryInformation
- UserDefined Property Sets
ms.topic: article
ms.date: 05/31/2018
---

# The DocumentSummaryInformation and UserDefined Property Sets

A **DocumentSummaryInformation** and **UserDefined** property set is an extension to [the Summary Information property set](the-summary-information-property-set.md). Both property sets can exist simultaneously.

The name of the stream that contains the **DocumentSummaryInformation** property set is **"\\005DocumentSummaryInformation"**. The format identifier (FMTID) for the **DocumentSummaryInformation** property set is **D5CDD502-2E9C-101B-9397-08002B2CF9AE**.

The declaration for this value is available in the provided header files as **FMTID\_DocSummaryInformation**. For more information, see [Names in IStorage](names-in-istorage.md), [The Summary Information Property Set](the-summary-information-property-set.md), [**IPropertySetStorage::Create**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-create) and [Format Identifiers](format-identifiers.md).

This stream also has a separate section for the custom-user-defined properties as in the **DocumentSummaryInformation** and **UserDefined** property sets. This section appears in the [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) interface as a separate property set, with the following FMTID (available as **FMTID\_UserDefinedProperties**): **D5CDD505-2E9C-101B-9397-08002B2CF9AE**.

These two property sets are the only ones for which a single stream can hold multiple property sets. The fact that these two property sets are in a single stream affects the behavior of the **IPropertySetStorage** interface. For more information, see [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage).

The following table lists the added properties to the **DocumentSummaryInformation** and **UserDefined** property set. As in the **SummaryInformation** property set, the names are not typically stored in the property set, but are inferred from the property identifier.



| Property name      | Property identifier     | Property identifier value | VARIANT type                      |
|--------------------|-------------------------|---------------------------|-----------------------------------|
| Category           | **PIDDSI\_CATEGORY**    | 0x00000002                | **VT\_LPSTR**                     |
| PresentationTarget | **PIDDSI\_PRESFORMAT**  | 0x00000003                | **VT\_LPSTR**                     |
| Bytes              | **PIDDSI\_BYTECOUNT**   | 0x00000004                | **VT\_I4**                        |
| Lines              | **PIDDSI\_LINECOUNT**   | 0x00000005                | **VT\_I4**                        |
| Paragraphs         | **PIDDSI\_PARCOUNT**    | 0x00000006                | **VT\_I4**                        |
| Slides             | **PIDDSI\_SLIDECOUNT**  | 0x00000007                | **VT\_I4**                        |
| Notes              | **PIDDSI\_NOTECOUNT**   | 0x00000008                | **VT\_I4**                        |
| HiddenSlides       | **PIDDSI\_HIDDENCOUNT** | 0x00000009                | **VT\_I4**                        |
| MMClips            | **PIDDSI\_MMCLIPCOUNT** | 0x0000000A                | **VT\_I4**                        |
| ScaleCrop          | **PIDDSI\_SCALE**       | 0x0000000B                | **VT\_BOOL**                      |
| HeadingPairs       | **PIDDSI\_HEADINGPAIR** | 0x0000000C                | **VT\_VARIANT** \| **VT\_VECTOR** |
| TitlesofParts      | **PIDDSI\_DOCPARTS**    | 0x0000000D                | **VT\_VECTOR** \| **VT\_LPSTR**   |
| Manager            | **PIDDSI\_MANAGER**     | 0x0000000E                | **VT\_LPSTR**                     |
| Company            | **PIDDSI\_COMPANY**     | 0x0000000F                | **VT\_LPSTR**                     |
| LinksUpToDate      | **PIDDSI\_LINKSDIRTY**  | 0x00000010                | **VT\_BOOL**                      |



 

These properties have the following uses:

<dl> <dt>

<span id="Category"></span><span id="category"></span><span id="CATEGORY"></span>Category
</dt> <dd>

A text string typed by the user that indicates what category the file belongs to (memo, proposal, and so on). It is useful for finding files of same type.

</dd> <dt>

<span id="PresentationTarget"></span><span id="presentationtarget"></span><span id="PRESENTATIONTARGET"></span>PresentationTarget
</dt> <dd>

Target format for presentation (35mm, printer, video, and so on).

</dd> <dt>

<span id="Bytes"></span><span id="bytes"></span><span id="BYTES"></span>Bytes
</dt> <dd>

Number of bytes.

</dd> <dt>

<span id="Lines"></span><span id="lines"></span><span id="LINES"></span>Lines
</dt> <dd>

Number of lines.

</dd> <dt>

<span id="Paragraphs"></span><span id="paragraphs"></span><span id="PARAGRAPHS"></span>Paragraphs
</dt> <dd>

Number of paragraphs.

</dd> <dt>

<span id="Slides"></span><span id="slides"></span><span id="SLIDES"></span>Slides
</dt> <dd>

Number of slides.

</dd> <dt>

<span id="Notes"></span><span id="notes"></span><span id="NOTES"></span>Notes
</dt> <dd>

Number of pages that contain notes.

</dd> <dt>

<span id="HiddenSlides"></span><span id="hiddenslides"></span><span id="HIDDENSLIDES"></span>HiddenSlides
</dt> <dd>

Number of slides that are hidden.

</dd> <dt>

<span id="MMClips"></span><span id="mmclips"></span><span id="MMCLIPS"></span>MMClips
</dt> <dd>

Number of sound or video clips.

</dd> <dt>

<span id="ScaleCrop"></span><span id="scalecrop"></span><span id="SCALECROP"></span>ScaleCrop
</dt> <dd>

Set to True (-1) when scaling of the thumbnail is desired. If not set, cropping is desired.

</dd> <dt>

<span id="HeadingPairs"></span><span id="headingpairs"></span><span id="HEADINGPAIRS"></span>HeadingPairs
</dt> <dd>

Internally used property indicating the grouping of different document parts and the number of items in each group. The titles of the document parts are stored in the **TitlesofParts** property. The **HeadingPairs** property is stored as a vector of variants, in repeating pairs of **VT\_LPSTR** (or **VT\_LPWSTR**) and **VT\_I4** values. The **VT\_LPSTR** value represents a heading name, and the **VT\_I4** value indicates the count of document parts under that heading.

</dd> <dt>

<span id="TitlesofParts"></span><span id="titlesofparts"></span><span id="TITLESOFPARTS"></span>TitlesofParts
</dt> <dd>

Names of document parts.

</dd> <dt>

<span id="Manager"></span><span id="manager"></span><span id="MANAGER"></span>Manager
</dt> <dd>

Manager of the project.

</dd> <dt>

<span id="Company"></span><span id="company"></span><span id="COMPANY"></span>Company
</dt> <dd>

Company name.

</dd> <dt>

<span id="LinksUpToDate"></span><span id="linksuptodate"></span><span id="LINKSUPTODATE"></span>LinksUpToDate
</dt> <dd>

Boolean value to indicate whether the custom links are hampered by excessive noise, for all applications.

> [!Note]  
> As described in 12.3. Serialized Format for Property Sets of the OLE 2.0 Design Specification, vector elements in the **HeadingPairs** and **TitlesofParts** properties should be aligned on 32 bit boundaries within the property set. However, in the **DocumentSummaryInformation** and **UserDefined** property sets, when the code page of the property set is not Unicode, these elements must be packed.

 

</dd> </dl>

The **UserDefined** property set can be used to hold any properties. Typically, it is used to store named properties created by a user.

 

 




