---
description: A perceived type is a category of file types that lets you identify your file type to Windows (and applications) as being an image, audio, document, or other type.
title: Perceived Types (The Windows Shell)
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 56d4c495-a886-4723-88ca-5b7753398062
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Perceived Types (The Windows Shell)

A perceived type is a category of file types that lets you identify your file type to Windows (and applications) as being an image, audio, document, or other type. Perceived types are used for several purposes, including the determination of the folder type, which is then used to set the default view settings. For example, a folder full of files that are of the perceived type image is assigned a default view mode of thumbnails.

This topic is organized as follows:

-   [About Perceived Types](#about-perceived-types)
-   [Additional Resources](#additional-resources)
-   [Related topics](#related-topics)

## About Perceived Types

Perceived types, defined as PerceivedType values, are similar to file types except that they refer to broad categories of file format types rather than specific file types. For example, image, text, audio, and compressed are perceived types. File types (generally public file types) can be assigned a perceived type, and should always be assigned one whenever there is one that is appropriate. For example, the image file types .bmp, .png, .jpg, and .gif are also of perceived type image.

The default perceived types are as follows:

-   Folder
-   Text
-   Image
-   Audio
-   Video
-   Compressed
-   Document
-   System
-   Application
-   Gamemedia
-   Contacts

## Additional Resources

-   For information about how to register perceived types, see [Application Registration](app-registration.md).
-   For a list of default perceived types, see the [**PERCEIVED**](/windows/win32/api/shtypes/ne-shtypes-perceived) enumeration.
-   To retrieves a file's perceived type based on its file name extension, see the [**AssocGetPerceivedType**](/windows/desktop/api/Shlwapi/nf-shlwapi-assocgetperceivedtype) function.

## Related topics

<dl> <dt>

[Application Registration](app-registration.md)
</dt> <dt>

[File Types](fa-file-types.md)
</dt> <dt>

[How File Associations Work](fa-how-work.md)
</dt> <dt>

[Content View By File Type or Kind](prophand-content-view.md)
</dt> <dt>

[File Type Verifier](file-type-verifier.md)
</dt> <dt>

[File Type Handlers](fa-file-extensions.md)
</dt> <dt>

[Programmatic Identifiers](fa-progids.md)
</dt> <dt>

[Association Arrays](fa-associationarray.md)
</dt> </dl>

 

 



