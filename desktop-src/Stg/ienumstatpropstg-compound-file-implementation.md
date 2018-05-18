---
title: IEnumSTATPROPSTG-Compound File Implementation
description: The compound file implementation of the IEnumSTATPROPSTG interface is used to enumerate properties, resulting in STATPROPSTG structures, which contain statistical property data.
ms.assetid: '8fa536f4-cce6-47e4-a860-2f43e48fa469'
keywords: ["IEnumSTATPROPSTG Strctd Stg , compound file implementation"]
---

# IEnumSTATPROPSTG-Compound File Implementation

The compound file implementation of the [**IEnumSTATPROPSTG**](ienumstatpropstg.md) interface is used to enumerate properties, resulting in [**STATPROPSTG**](statpropstg.md) structures, which contain statistical property data. The implementation of [**IPropertyStorage**](ipropertystorage.md) manages the statistical data and is associated with a current compound file storage object.

The constructor in the COM implementation of [**IEnumSTATPROPSTG**](ienumstatpropstg.md) creates a class that reads the entire property set, and creates a static array which can be shared when **IEnumSTATPROPSTG::Clone** is called.

## When to Use

Call the compound file implementation of [**IEnumSTATPROPSTG**](ienumstatpropstg.md) to enumerate the [**STATPROPSTG**](statpropstg.md) structures that contain data about the properties within the current property set. When using the compound file implementation of the property storage interfaces, call [**IPropertyStorage::Enum**](ipropertystorage-enum.md) to return a pointer to **IEnumSTATPROPSTG** to manage the property storage object and the elements within it.

## Remarks

<dl> <dt>

<span id="IEnumSTATPROPSTG__Next"></span><span id="ienumstatpropstg__next"></span><span id="IENUMSTATPROPSTG__NEXT"></span>[**IEnumSTATPROPSTG::Next**](ienumstatpropstg.md)
</dt> <dd>

Gets the next one or more [**STATPROPSTG**](statpropstg.md) structures (the number is specified by the *celt* parameter). Returns S\_OK if successful.

</dd> <dt>

<span id="IEnumSTATPROPSTG__Skip"></span><span id="ienumstatpropstg__skip"></span><span id="IENUMSTATPROPSTG__SKIP"></span>[**IEnumSTATPROPSTG::Skip**](ienumstatpropstg.md)
</dt> <dd>

Skips the number of elements specified in *celt*. The next element to be enumerated through a call to Next then becomes the element after the skipped elements. Returns S\_OK if *celt* elements were skipped; returns S\_FALSE if fewer than *celt* elements were skipped.

</dd> <dt>

<span id="IEnumSTATPROPSTG__Reset"></span><span id="ienumstatpropstg__reset"></span><span id="IENUMSTATPROPSTG__RESET"></span>[**IEnumSTATPROPSTG::Reset**](ienumstatpropstg.md)
</dt> <dd>

Sets the cursor to the beginning of the enumeration. If successful, returns S\_OK, otherwise, returns STG\_E\_INVALIDHANDLE.

</dd> <dt>

<span id="IEnumSTATPROPSTG__Clone"></span><span id="ienumstatpropstg__clone"></span><span id="IENUMSTATPROPSTG__CLONE"></span>[**IEnumSTATPROPSTG::Clone**](ienumstatpropstg.md)
</dt> <dd>

Uses the constructor for the [**IEnumSTATPROPSTG**](ienumstatpropstg.md) to create a copy of the array. Because the class that constructs the static array actually contains the object, this function mainly adds to the reference count.

</dd> </dl>

## Related topics

<dl> <dt>

[**STATPROPSTG**](statpropstg.md)
</dt> <dt>

[**IPropertyStorage::Enum**](ipropertystorage-enum.md)
</dt> </dl>

 

 




