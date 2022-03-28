---
description: Library description files are XML files that define libraries.
ms.assetid: 12F6E6AE-2776-408c-B9AC-E885BE93C27F
title: Library Description Schema
ms.topic: article
ms.date: 05/31/2018
---

# Library Description Schema

Library description files are XML files that define libraries. Libraries aggregate items from local and remote storage locations into a single view in Windows Explorer. Library description files follow the Library Description schema and are saved as \*.library-ms files.

This topic contains the following sections:

- [Overview of the Library Description Schema](#overview-of-the-library-description-schema)
- [Namespace Versioning](#namespace-versioning)
- [Example of a Library Description File](#example-of-a-library-description-file)
- [Related topics](#related-topics)

## Overview of the Library Description Schema

Libraries contain files that are stored in one or more storage locations. Libraries do not actually store these files; instead, they monitor the folders that contain the files, and let users access and arrange the files in different ways. For example, a user can have music files in multiple folders on a local hard disk and also on an external hard disk. Using the **Music Library**, the user can access all of those files at the same time and sort them all by artist name or album title as a single group.

The Library Description schema consists of three major parts, described in the following table:



| Part                        | Description                                                                                                                                                |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| General library information | Information about the library, such as name, owner, version, icon, that Windows Explorer can use when it displays the library to a user.                   |
| Library properties          | One or more properties that describe the library. These custom properties are specific to the library.                                                     |
| Library locations           | One or more search connectors that identify storage locations to include in the library. Each of these locations can also have a unique set of properties. |



 

Library files in Windows 7 are stored in the known folder, FOLDERID\_Libraries. By default, the FOLDERID\_Libraries folder is located at %USERPROFILE%\\AppData\\Roaming\\Microsoft\\Windows\\Libraries.

## Namespace Versioning

Versions of the Library Description file format (\*.library-ms) are tracked by changing the namespace. For Windows 7, the file format has the following default namespace: `https://schemas.microsoft.com/windows/2009/library`.

Versions of the library contents, however, are tracked by using the [&lt;version&gt;](schema-library-version.md) element in a specific Library Description file.

## Example of a Library Description File

The following is an example of a Library Description file that defines a library for document files.


```
<?xml version="1.0" encoding="UTF-8"?>
<libraryDescription xmlns="http://schemas.microsoft.com/windows/2009/library">
    <name>@shell32.dll,-34575</name>
    <ownerSID>S-1-5-21-379071477-2495173225-776587366-1000</ownerSID>
    <version>1</version>
    <isLibraryPinned>true</isLibraryPinned>
    <iconReference>imageres.dll,-1002</iconReference>
    <templateInfo>
        <folderType>{7d49d726-3c21-4f05-99aa-fdc2c9474656}</folderType>
    </templateInfo>
    <searchConnectorDescriptionList>
        <searchConnectorDescription publisher="Microsoft" product="Windows">
            <description>@shell32.dll,-34577</description>
            <isDefaultSaveLocation>true</isDefaultSaveLocation>
            <simpleLocation>
                <url>knownfolder:{FDD39AD0-238F-46AF-ADB4-6C85480369C7}</url>
                <serialized>MBAAAEAFCAAA...MFNVAAAAAA</serialized>
            </simpleLocation>
        </searchConnectorDescription>
        <searchConnectorDescription publisher="Microsoft" product="Windows">
            <description>@shell32.dll,-34579</description>
            <isDefaultNonOwnerSaveLocation>true</isDefaultNonOwnerSaveLocation>
            <simpleLocation>
                <url>knownfolder:{ED4824AF-DCE4-45A8-81E2-FC7965083634}</url>
                <serialized>MBAAAEAFCAAA...HJIfK9AAAAAA</serialized>
            </simpleLocation>
        </searchConnectorDescription>
    </searchConnectorDescriptionList>
</libraryDescription>
```



## Related topics

<dl> <dt>

[folderType Element (Library Schema)](schema-library-foldertype.md)
</dt> <dt>

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

[property Element (Library Schema)](schema-library-property.md)
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
</dt> <dt>

[Search Connector Description Schema](../search/search-sconn-desc-schema-entry.md)
</dt> </dl>

 

 
