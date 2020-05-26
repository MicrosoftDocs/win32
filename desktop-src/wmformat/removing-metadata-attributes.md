---
title: Removing Metadata Attributes
description: Removing Metadata Attributes
ms.assetid: 44546091-406f-4ae6-914a-942d1b89e0e4
keywords:
- Windows Media Format SDK,removing metadata attributes
- Advanced Systems Format (ASF),removing metadata attributes
- ASF (Advanced Systems Format),removing metadata attributes
- metadata,removing attributes
ms.topic: article
ms.date: 05/31/2018
---

# Removing Metadata Attributes

You can remove a metadata attribute by passing its index and stream number to the [**IWMHeaderInfo3::DeleteAttribute**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo3-deleteattribute) method. The order in which the remaining attributes are indexed after removing an attribute does not change; all remaining attributes that originally had an index value greater than the one removed have their index values reduced by one. When removing multiple attributes, do so in descending order by index to avoid having to calculate the adjustment in indexing.

For convenience in removing values, the [**IWMHeaderInfo3::GetAttributeIndices**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo3-getattributeindices) method returns the index values in descending order.

> [!Note]  
> Index values obtained by using the methods of [**IWMHeaderInfo3**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo3) are not compatible with index values obtained by using the methods of [**IWMHeaderInfo**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo). If you use the methods of one interface to change attributes in a file, you should assume that any index values previously retrieved from the other interface are no longer valid and must be obtained again. You should avoid using the methods of **IWMHeaderInfo** if possible.

 

## Related topics

<dl> <dt>

[**Working with Metadata**](working-with-metadata.md)
</dt> </dl>

 

 




