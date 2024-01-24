---
description: Contains the path of the icon file for the connection.
ms.assetid: 9daf4916-914b-4326-9933-b433cc00b4c1
title: ICONFilePath (MBNProfile) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ICONFilePath
api_type: 
- Schema
---

# ICONFilePath (MBNProfile) Element

The **ICONFilePath (MBNProfile)** element contains the path of the icon file for the connection.

The operating system connection UI will display this icon when a connection is made using this element.

When passing the XML for creating the profile in the [**CreateConnectionProfile**](/windows/desktop/api/mbnapi/nf-mbnapi-imbnconnectionprofilemanager-createconnectionprofile) method of the [**IMbnConnectionProfileManager**](/windows/desktop/api/mbnapi/nn-mbnapi-imbnconnectionprofilemanager) interface, this path should point to the source location of the icon file. On successful creation of [**IMbnConnectionProfile**](/windows/desktop/api/mbnapi/nn-mbnapi-imbnconnectionprofile) object, the Mobile Broadband service will copy the icon file in it's internal store and the profile path will be modified to reflect this.

The icon file should be in .bmp format with 32X32 pixel dimension.

This element is a string of length up to 1024 characters, containing an absolute file path.

The element is optional.

``` syntax
<xs:element name="ICONFilePath"
    type="iconFileType"
 />
```

The **ICONFilePath** element is defined by the [**MBNProfile**](schema-mbnprofile-element.md) element.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/> |
| Minimum supported server<br/> | None supported<br/>                         |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**MBNProfile**](schema-mbnprofile-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**MBNProfile**](schema-mbnprofile-element.md)
</dt> </dl>

 

 




