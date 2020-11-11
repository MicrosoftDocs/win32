---
title: IEnumSTATPROPSETSTG-Compound File Implementation
description: The compound file implementation of the IEnumSTATPROPSETSTG interface is used to enumerate an array of STATPROPSETSTG structures that contain statistical property data.
ms.assetid: 1ce36e40-518c-411b-be5a-835a2dd0995e
keywords:
- IEnumSTATPROPSETSTG Strctd Stg , compound file implementation
ms.topic: article
ms.date: 05/31/2018
---

# IEnumSTATPROPSETSTG-Compound File Implementation

The compound file implementation of the [**IEnumSTATPROPSETSTG**](/windows/win32/api/propidlbase/nn-propidlbase-ienumstatpropsetstg) interface is used to enumerate an array of [**STATPROPSETSTG**](/windows/win32/api/propidlbase/nn-propidlbase-ienumstatpropsetstg) structures that contain statistical property data. The [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) implementation manages the statistical data and is associated with a current compound file storage object.

## When to Use

Call the methods of [**IEnumSTATPROPSETSTG**](/windows/win32/api/propidlbase/nn-propidlbase-ienumstatpropsetstg) to enumerate [**STATPROPSETSTG**](/windows/win32/api/propidlbase/nn-propidlbase-ienumstatpropsetstg) structures, each of which provide data about one of the property sets associated with the compound file storage object.

## Remarks

<dl> <dt>

<span id="IEnumSTATPROPSETSTG__Next"></span><span id="ienumstatpropsetstg__next"></span><span id="IENUMSTATPROPSETSTG__NEXT"></span>[**IEnumSTATPROPSETSTG::Next**](/windows/win32/api/propidlbase/nn-propidlbase-ienumstatpropstg)
</dt> <dd>

Gets the next one or more [**STATPROPSETSTG**](/windows/win32/api/propidlbase/nn-propidlbase-ienumstatpropsetstg) structures (the number is specified by the *celt* parameter). The **STATPROPSETSTG** elements provided through a call to the compound file implementation of [**IEnumSTATPROPSETSTG::Next**](/windows/win32/api/propidlbase/nn-propidlbase-ienumstatpropstg) follow these rules:

-   If [**IEnumSTATPROPSETSTG::Next**](/windows/win32/api/propidlbase/nn-propidlbase-ienumstatpropstg) cannot provide STATPROPSETSTG.fmtid, zeros are written to that member. This occurs when the property set does not have a predefined name (such as \\005SummaryInformation) and is not a legal value.
-   The DocumentSummaryInformation and UserDefined property set is special, in that it may have two property set sections. This property set is described in the section [The DocumentSummaryInformation and UserDefined Property Sets](the-documentsummaryinformation-and-userdefined-property-sets.md). The second section is referred to as the User-Defined Properties. Each section is identified with a unique format identifier (FMTID). When [**IPropertySetStorage::Enum**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-enum) is used to enumerate property sets, the User-Defined property set will not be enumerated.

> [!Note]  
> If you always create a property set using [**IPropertySetStorage::Create**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-create), then, because a "Character GUID" is created for the storage name, [**IEnumSTATPROPSETSTG::Next**](/windows/win32/api/propidlbase/nn-propidlbase-ienumstatpropstg) will return a nonzero, valid FMTID for the property set \[STATPROPSETSTG.fmtid\].

 

-   The STATPROPSETSTG.grfFlags member does not necessarily reflect whether the property set is ANSI or not. If PROPSETFLAG\_ANSI is set, the property set is definitely ANSI. If PROPSETFLAG\_ANSI is clear, the property set could be either Unicode or non-Unicode, because it is not possible to tell whether it is ANSI without opening it.
-   The STATPROPSETSTG.grfFlags member does reflect whether the property set is simple or not, so the setting of the PROPSETFLAG\_NONSIMPLE flag is always valid.
-   If [**IEnumSTATPROPSETSTG::Next**](/windows/win32/api/propidlbase/nn-propidlbase-ienumstatpropstg) cannot provide STATPROPSETSTG.clsid, it is set to all zeroes (CLSID\_NULL). In the COM compound file implementation, this occurs when the property set is simple (the PROPSETFLAG\_NONSIMPLE flag is not set), or is nonsimple, but the CLSID was not explicitly set. For nonsimple property sets, the CLSID that is received is the one that is maintained by the underlying [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage).
-   If [**IEnumSTATPROPSETSTG::Next**](/windows/win32/api/propidlbase/nn-propidlbase-ienumstatpropstg) cannot provide the time fields \[**ctime**, **mtime**, **atime**\], each non-supported time will be set to zeroes. In the COM compound file implementation, getting these values depends on retrieving them from the underlying [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) implementation.

</dd> <dt>

<span id="IEnumSTATPROPSETSTG__Skip"></span><span id="ienumstatpropsetstg__skip"></span><span id="IENUMSTATPROPSETSTG__SKIP"></span>[**IEnumSTATPROPSETSTG::Skip**](/windows/win32/api/propidlbase/nn-propidlbase-ienumstatpropsetstg)
</dt> <dd>

Skips the number of elements specified in *celt*. Returns S\_OK if the specified number of elements are skipped, returns S\_FALSE if fewer elements than requested are skipped. In any other case, returns the appropriate error.

</dd> <dt>

<span id="IEnumSTATPROPSETSTG__Reset"></span><span id="ienumstatpropsetstg__reset"></span><span id="IENUMSTATPROPSETSTG__RESET"></span>[**IEnumSTATPROPSETSTG::Reset**](/windows/win32/api/propidlbase/nn-propidlbase-ienumstatpropsetstg)
</dt> <dd>

Sets the cursor to the beginning of the enumeration. If successful, returns S\_OK, otherwise, returns STG\_E\_INVALIDHANDLE.

</dd> <dt>

<span id="IEnumSTATPROPSETSTG__Clone"></span><span id="ienumstatpropsetstg__clone"></span><span id="IENUMSTATPROPSETSTG__CLONE"></span>[**IEnumSTATPROPSETSTG::Clone**](/windows/win32/api/propidlbase/nn-propidlbase-ienumstatpropsetstg)
</dt> <dd>

Copies the current enumeration state of this enumerator.

</dd> </dl>

 

 