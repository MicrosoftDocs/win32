---
description: Several image file formats enable you to store metadata along with an image.
ms.assetid: 1eba4b91-bbf4-4f82-b2d7-65f331a84859
title: Image Property Tag Constants
ms.topic: article
ms.date: 05/31/2018
---

# Image Property Tag Constants

Several image file formats enable you to store metadata along with an image. Metadata is information about an image, for example, title, width, camera model, and artist. Windows GDI+ provides a uniform way of storing and retrieving metadata from image files in the Tagged Image File Format (TIFF), JPEG, Portable Network Graphics (PNG), and Exchangeable Image File (EXIF) formats.

In GDI+, a piece of metadata is called a *property item*, and an individual property item is identified by a numerical constant called a *property tag*. You can store and retrieve metadata by calling the [**Image::SetPropertyItem**](/windows/desktop/api/Gdiplusheaders/nf-gdiplusheaders-image-setpropertyitem) and [**Image::GetPropertyItem**](/windows/desktop/api/Gdiplusheaders/nf-gdiplusheaders-image-getpropertyitem) methods of the [**Image**](/windows/desktop/api/gdiplusheaders/nl-gdiplusheaders-image) class, and you don't have to be concerned with the details of how a particular file format stores that metadata.

The following topics list and describe the property items supported by GDI+. The descriptions are brief and general so that they apply to a variety of file formats. For a detailed description of how a property item is used in a particular file format, see the specification for that file format. For links to several file format specifications, see [Image File Format Specifications](-gdiplus-constant-image-file-format-specifications.md). For more information about metadata, see [Reading and Writing Metadata](-gdiplus-reading-and-writing-metadata-use.md) and [**Image Property Tag Type Constants**](-gdiplus-constant-image-property-tag-type-constants.md).

-   [Property Tags in Numerical Order](-gdiplus-constant-property-tags-in-numerical-order.md)
-   [Property Tags in Alphabetical Order](-gdiplus-constant-property-tags-in-alphabetical-order.md)
-   [Property Item Descriptions](-gdiplus-constant-property-item-descriptions.md)

 

 



