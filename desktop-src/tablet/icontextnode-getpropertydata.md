---
description: Retrieves application-specific data or other property data for the specified identifier.
ms.assetid: eaf95ff8-7b31-4c05-aa49-0c3bb9e996c0
title: IContextNode::GetPropertyData method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextNode.GetPropertyData
api_type: 
- COM
api_location: 
- IACom.dll
---

# IContextNode::GetPropertyData method

Retrieves application-specific data or other property data for the specified identifier.

## Syntax


```C++
HRESULT GetPropertyData(
  [in]      const GUID  *pPropertyDataId,
  [in, out]       ULONG *pulPropertyDataSize,
  [out]           BYTE  **ppbPropertyData
);
```



## Parameters

<dl> <dt>

*pPropertyDataId* \[in\]
</dt> <dd>

The identifier for the data.

</dd> <dt>

*pulPropertyDataSize* \[in, out\]
</dt> <dd>

The size of the data in bytes. The value that is passed in is not used.

</dd> <dt>

*ppbPropertyData* \[out\]
</dt> <dd>

A pointer to an 8-bit unsigned integer array that contains the property data.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, use [**CoTaskMemFree**](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemfree) to release the memory from \**ppbPropertyData* when you no longer need the information.

 

In addition to retrieving application-specific data that was added with [**IContextNode::AddPropertyData**](icontextnode-addpropertydata.md), this method is used to retrieve common properties that are described by the [Context Node Properties](context-node-properties.md) constants.

The string-type properties include:

-   GUID\_CNP\_RECOGNIZEDSTRING
-   GUID\_CNP\_SHAPENAME
-   GUID\_AHP\_ANALYSISHINTNAME
-   GUID\_AHP\_PREFIXTEXT
-   GUID\_AHP\_SUFFIXTEXT
-   GUID\_AHP\_FACTOID

The return value is **WCHAR\***. If you cast the \**ppbPropertyData* parameter to **WCHAR\*** its returned length is `(length of the string + 1) * sizeof(WCHAR)`.

The Boolean-type properties include:

-   GUID\_AHP\_OVERRIDELANGUAGEID
-   GUID\_AHP\_COERCETOFACTOID
-   GUID\_AHP\_WORDMODE

The return value is **VARIANT\_BOOL**. If you cast the \**ppbPropertyData* parameter to **VARIANT\_BOOL\*** its returned length is `sizeof(VARIANT_BOOL)`.

GUID\_AHP\_GUIDE is a guide-type property. The return value is **InkAnalysisRecognitionGuide\***. If you cast the \**ppbPropertyData* parameter to **InkAnalysisRecognitionGuide\*** its returned length is `sizeof(InkAnalysisRecognitionGuide)`.

Integer-type properties include:

-   GUID\_CNP\_LINENUMBER
-   GUID\_CNP\_POINTSPERINCH
-   GUID\_CNP\_CONFIDENCELEVEL
-   GUID\_CNP\_CONFIRMATION
-   GUID\_CNP\_MAXIMUMSTROKECOUNT
-   GUID\_CNP\_SEGMENTATION
-   GUID\_CNP\_ALIGNMENTLEVEL

The return value is **LONG\***. If you cast the \**ppbPropertyData* parameter to **LONG\*** its returned length is `sizeof(LONG)`.

Line metrics-type properties include:

-   GUID\_CNP\_ASCENDERS
-   GUID\_CNP\_DESCENDERS
-   GUID\_CNP\_BASELINE
-   GUID\_CNP\_MIDLINE

The return value is **LONG\***. If you cast the \**ppbPropertyData* parameter to **LONG\*** its returned length is `sizeof(LONG)*4`, signifying the (x, y) values for the starting points followed by the (x, y) values for the ending points.

GUID\_CNP\_TEXTRECOGNIZERID is a **GUID** property. The return value is **GUID\***. If you cast the \**ppbPropertyData* parameter to **GUID\*** its returned length is `sizeof(GUID)`.

GUID\_CNP\_ROTATEDBOUNDINGBOX is a rotated bounding box property. The return value is **LONG\***. If you cast the \**ppbPropertyData* parameter to **LONG\*** its returned length is `sizeof(LONG)*8`, signifying the (x, y) values for the four corners of the box.

GUID\_CNP\_HOTPOINT is a hot point property. The return value is **LONG\***. If you cast the \**ppbPropertyData* parameter to **LONG\*** its returned length is `sizeof(LONG)*2`, signifying the (x, y) values for the point.

GUID\_AHP\_WORDLIST is a word list property. The return value is **WCHAR\***. If you cast the \**ppbPropertyData* parameter to **WCHAR\*** its returned length is `n * sizeof(WCHAR)`, where `n` is the sum of the string lengths of the number of strings in the list plus 1 for each **NULL** termination character for each string.

## Examples

This example shows a method that accesses the AlignmentLevel context node property of a Paragraph context node type.


```C++
// Checks a paragraph context node's alignment level property.
// Only paragraph type context nodes contain the alignment level property.
HRESULT CMyClass::ExploreParagraphNode(
    IContextNode *pParagraphNode)
{
    // Get the AlignmentLevel property data for the paragraph.
    LONG * alignmentLevel = NULL;
    ULONG ulDataLen = 0;

    HRESULT hr = pParagraphNode->GetPropertyData(
        (const GUID*)&GUID_CNP_ALIGNMENTLEVEL,
        &ulDataLen,
        (BYTE**)&alignmentLevel);

    if( FAILED(hr) ||
        ulDataLen != sizeof(LONG) ||
        alignmentLevel == NULL )
    {
        // Insert code that handles an error here.
    }
    else
    {
        // Insert code that uses the alignment level here.
    }

    // Free the memory allocated for the property data.
    ::CoTaskMemFree(alignmentLevel);

    return hr;
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**IContextNode**](icontextnode.md)
</dt> <dt>

[**IContextNode::AddPropertyData**](icontextnode-addpropertydata.md)
</dt> <dt>

[**IContextNode::RemovePropertyData**](icontextnode-removepropertydata.md)
</dt> <dt>

[**IContextNode::GetPropertyDataIds**](icontextnode-getpropertydataids.md)
</dt> <dt>

[**IContextNode::ContainsPropertyData**](icontextnode-containspropertydata.md)
</dt> <dt>

[**IContextNode::LoadPropertiesData**](icontextnode-loadpropertiesdata.md)
</dt> <dt>

[**IContextNode::SavePropertiesData**](icontextnode-savepropertiesdata.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

