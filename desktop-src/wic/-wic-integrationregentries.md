---
description: This topic applies to Windows Vista and later.
ms.assetid: 4d88806a-68a6-4394-a704-c7a47a0fdc70
title: Integration with Windows Photo Gallery and Windows Explorer
ms.topic: article
ms.date: 05/31/2018
---

# Integration with Windows Photo Gallery and Windows Explorer

This topic applies to Windows Vista and later. It contains the following sections:

-   [Introduction](#introduction)
-   [Integration with the Windows Property Store](#integration-with-the-windows-property-store)
-   [Integration with the Windows Photo Gallery](#integration-with-the-windows-photo-gallery)
-   [Integration with the Windows Thumbnail Cache](#integration-with-the-windows-thumbnail-cache)
-   [Related topics](#related-topics)

## Introduction

To enable Windows Photo Gallery and Windows Explorer to display thumbnails and search and update standard image metadata, a codec must have an implementation of the [IThumbnailProvider](/windows/win32/api/thumbcache/nn-thumbcache-ithumbnailprovider) and [IPropertyStore](/windows/win32/api/propsys/nn-propsys-ipropertystore) interfaces associated with it. The IThumbnailProvider interface is used to retrieve thumbnails and populate the thumbnail cache, and the IPropertyStore interface is used for searching and updating metadata associated with a file. As of Windows Vista, all file types have thumbnails and metadata, but different file types require different implementations of these interfaces to retrieve or generate the thumbnails and metadata for them. The system provides default implementations of these interfaces. The default implementation of IThumbnailProvider can be used for any Windows Imaging Component (WIC)–enabled image format. The default implementation of IPropertyStore can be used with any WIC-enabled image format that is based on a Tagged Image File Format (TIFF) or JPEG container. To associate your image format with the default implementations of both of these interfaces, you must add just a few registry entries.

The following entries indicate to the Windows Photo Gallery and Windows Explorer that a file name extension (.ext) and its associated MIME type are associated with an image format.

The following entry indicates to Windows and applications that use content type (also known as mime type) that a file with a given extension (.ext) is an image format. The file type owner needs to choose a `<image sub type value>` that uniquely identifies the file format and this content type value needs to be register with IANA.

```
HKEY_CLASSES_ROOT
   {.ext}
      ContentType = image/<image sub type>
```

The following entry indicates to Windows, Windows search and applications that use [System.Kind](../properties/props-system-kind.md) that a file name extension (.ext) should be treated as a picture. Specifically, it indicates that the file extension’s System.Kind property should be set to Picture.

```
HKEY_LOCAL_MACHINE
   Software
      Microsoft
         Windows
            CurrentVersion
               Explorer
                  KindMap
                     {.ext} = Picture
```

## Integration with the Windows Property Store

Sometimes the same metadata properties are exposed in different metadata schemas, often with different property names. When one of these properties is updated, but the others are not, the metadata within the file can get out of sync. The photo property handler provides the default **IPropertyStore** implementation for images, and is used by applications as well as by the Windows Photo Gallery and Windows Explorer to ensure that all the metadata in an image stays in sync, and that the properties displayed by applications are consistent with those displayed by the Windows Photo Gallery and Windows Explorer. When the photo property handler updates metadata, it makes sure that these properties are updated consistently across all the common metadata formats that are present in the file.

The photo property handler must understand the container format and how to locate the various properties within it. In general, it isn’t possible for the photo property handler to know how the various metadata blocks are laid out in a proprietary container format. However, if the metadata in your container format is laid out the same way as the metadata in either a TIFF container format or a JPEG container format, the photo property handler can take advantage of that knowledge to update metadata consistently in your container format as well.

You can register this association by creating the following registry entry. This entry notifies the photo property handler that the container format identified by this GUID understands the same metadata query language paths as the container format with the GUID 163bcc30-e2e9-4f0b-961d-a3e9fdb788a3. (163bcc30-e2e9-4f0b-961d-a3e9fdb788a3 is the GUID for the TIFF container format.)

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Microsoft
         Windows
            CurrentVersion
               PhotoPropertyHandler
                  ContainerAssociations
                     {Container Format GUID} = {163bcc30-e2e9-4f0b-961d-a3e9fdb788a3}
```

The following entry associates the photo property handler’s default implementation of **IPropertyStore** with files that have the extension ".ext". The first GUID is the IID of the **IPropertyStore** interface, and the second is the GUID of the photo property handler’s implementation of it.

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Microsoft
         Windows
            CurrentVersion
               PhotoPropertyHandler
                  {.ext}
                     (Default) = {a38b883c-1682-497e-97b0-0a3a9e801682}
```

Codecs that use a proprietary format that is not compatible with either the TIFF or JPEG container format must write their own **IPropertyStore** implementation.

## Integration with the Windows Photo Gallery

Windows Photo Gallery is built on WIC and can display any WIC-enabled image format for which the codec is installed. To notify the system that your image format can be opened in Windows Photo Gallery, you need to create a file association by creating the following registry entries.

```
HKEY_CLASSES_ROOT
   {.ext}
      (Default) = {ProgID} for example, jpegfile)
      OpenWithProgids
         {ProgID}
      OpenWithList
         PhotoViewer.dll
      ShellEx
         ContextMenuHandlers
            ShellImagePreview
               (Default) = {FFE2A43C-56B9-4bf5-9A79-CC6D4285608A}
   SystemFileAssociations
      {.ext}
         OpenWithList
            PhotoViewer.dll
         ShellEx
            ContextMenuHandlers
               ShellImagePreview
                  (Default) = {FFE2A43C-56B9-4bf5-9A79-CC6D4285608A}
   {Image Format ProgID}
      (Default) = Name of Image Format
      DefaultIcon
         (Default) = Path to icon for type, icon index
      shell
         open
            MuiVerb = @%PROGRAMFILES%\Windows Photo Gallery\photoviewer.dll,-3043
            command
               (Default) = %SystemRoot%\System32\rundll32.exe "%ProgramFiles%\Windows Photo Gallery\PhotoViewer.dll", ImageView_Fullscreen %1
            DropTarget
               Clsid = {FFE2A43C-56B9-4bf5-9A79-CC6D4285608A}
         printo
            command
               (Default) = %SystemRoot%\System32\rundll32.exe "%SystemRoot%\System32\shimgvw.dll", ImageView_PrintTo /pt "%1" "%2" "%3" "%4"
```

The ProgID is usually the file name extension appended with the word "file". (For example, if the file name extension is .txt, the ProgID would usually be "txtfile".)

There are other standard registry entries you may need to create to support file associations; however, because the’y are not specific to WIC, they are beyond the scope of this topic.

## Integration with the Windows Thumbnail Cache

The following two entries indicate that the standard WIC thumbnail provider implementation can be used to retrieve thumbnails for files with this extension. The first GUID is the IID of the [IThumbnailProvider](/windows/win32/api/thumbcache/nn-thumbcache-ithumbnailprovider) interface, and the second is the GUID of the standard system implementation of this interface. (All entries under HKCR\\.ext\\ShellEx\\ are repeated under HKCR\\SystemFileAssociations\\.ext\\ShellEx\\.)

```
HKEY_CLASSES_ROOT
   SystemFileAssociations
      {.ext}
         ShellEx
            {e357fccd-a995-4576-b01f-234630154e96}
               (Default) = {C7657C4A-9F68-40fa-A4DF-96BC08EB3551}
```

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Encoder-Specific Registry Entries](-wic-decoderregentries.md)
</dt> <dt>

[CODEC Installation and Registration](-wic-codecinstallandreg.md)
</dt> <dt>

[How to Write a WIC-Enabled CODEC](-wic-howtowriteacodec.md)
</dt> <dt>

[Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md)
</dt> </dl>

 

 
