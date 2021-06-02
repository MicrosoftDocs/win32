---
description: The <iconReference> element specifies a custom icon for this library. This element is optional and has no attributes or child elements.
title: iconReference Element (Library Schema)
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 7A35B014-1E01-4da2-AA64-4CFC3436C6D9
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# iconReference Element (Library Schema)

The <iconReference> element specifies a custom icon for this library. This element is optional and has no attributes or child elements.

## Syntax


```
<!-- iconReference -->
    <xs:element name="iconReference" type="xs:string" minOccurs="0"/>
```



## Element Information



| Parent Element                                                               | Child Elements |
|------------------------------------------------------------------------------|----------------|
| [libraryDescription Element (Library Schema)](schema-librarydescription.md) |                |



 

## Remarks

The icon reference must be specified in a form suitable for the [**PathParseIconLocation**](/windows/desktop/api/Shlwapi/nf-shlwapi-pathparseiconlocationa) function. For example: `ModuleFileName,IconResourceIndex`.

## Related topics

<dl> <dt>

[folderType Element (Library Schema)](schema-library-foldertype.md)
</dt> <dt>

[isLibraryPinned Element (Library Schema)](schema-library-islibrarypinned.md)
</dt> <dt>

[libraryDescription Element (Library Schema)](schema-librarydescription.md)
</dt> <dt>

[name Element (Library Schema)](schema-library-name.md)
</dt> <dt>

[ownerSID Element (Library Schema)](schema-library-ownersid.md)
</dt> <dt>

[propertyStore Element (Library Schema)](schema-library-propertystore.md)
</dt> <dt>

[searchConnectorDescription Element (Library Schema)](schema-library-searchconnectordescription.md)
</dt> <dt>

[searchConnectorDescriptionList Element (Library Schema)](schema-library-searchconnectordescriptionlist.md)
</dt> <dt>

[templateInfo Element (Library Schema)](schema-library-templateinfo.md)
</dt> <dt>

[version Element (Library Schema)](schema-library-version.md)
</dt> </dl>

 

 



