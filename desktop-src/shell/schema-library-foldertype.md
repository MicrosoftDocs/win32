---
description: The <folderType> element specifies a GUID for the folder type. This element is required if the <templateInfo> element exists, otherwise it is optional. This element has no attributes and no child elements.
title: folderType Element (Library Schema)
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 240550F0-B6AC-470e-8BF1-DB5A4068226B
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# folderType Element (Library Schema)

The <folderType> element specifies a GUID for the folder type. This element is required if the <templateInfo> element exists, otherwise it is optional. This element has no attributes and no child elements.

## Syntax


```
<!-- folderType -->
    <xs:element name="templateInfo" minOccurs="0">
      <xs:complexType>
        <xs:all>
          <xs:element name="folderType" minOccurs="0"/>
        </xs:all>
      </xs:complexType>
    </xs:element>
```



## Element Information



| Parent Element                                                           | Child Elements |
|--------------------------------------------------------------------------|----------------|
| [templateInfo Element (Library Schema)](schema-library-templateinfo.md) |                |



 

## Remarks

Setting a folder type determines the columns and details that appear in Windows Explorer by default. Folder type identifiers ([**FOLDERTYPEID**](foldertypeid.md)) are GUIDs defined in Shlguid.h. The following table lists the GUIDs of common folder types.



| Folder Type      | GUID                                   |
|------------------|----------------------------------------|
| Generic Library  | {5f4eab9a-6833-4f61-899d-31cf46979d49} |
| Users Libraries  | {C4D98F09-6124-4fe0-9942-826416082DA9} |
| Documents Folder | {7D49D726-3C21-4F05-99AA-FDC2C9474656} |
| Pictures Folder  | {B3690E58-E961-423B-B687-386EBFD83239} |
| Videos Folder    | {5fa96407-7e77-483c-ac93-691d05850de8} |
| Games Folder     | {b689b0d0-76d3-4cbb-87f7-585d0e0ce070} |
| Music Folder     | {94d6ddcc-4a68-4175-a374-bd584a510b78} |
| Contacts         | {DE2B70EC-9BF7-4A93-BD3D-243F7881D492} |



 

## Related topics

<dl> <dt>

[iconReference Element (Library Schema)](schema-library-iconreference.md)
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

 

 



