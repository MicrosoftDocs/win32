---
description: Encoder-Specific Registry Entries
ms.assetid: bbb78d70-bd3e-4d5a-ba59-2e17d2d1cf30
title: Encoder-Specific Registry Entries
ms.topic: article
ms.date: 05/31/2018
---

# Encoder-Specific Registry Entries


In addition to the entries listed above for encoder, you must also register your encoder under the category of Windows Imaging Component (WIC) encoders so the discovery engine can find it. You do this by making the following registry entries. The first GUID in the following entries is the category identifier (CATID) for WICBitmapEncoders.

```
HKEY_CLASSES_ROOT
   CLSID
      {AC757296-3522-4E11-9862-C17BE5A1767E}
         Instance
            {Encoder CLSID}
               CLSID = {Encoder CLSID}
               FriendlyName = {Name of Encoder}
```

## Registering a Container Format with Metadata Writers

If you create a new container format for your codec, you must also create registry entries to support metadata writers for the metadata blocks in your images. The following entries need to be created under the class identifier (CLSID) of the metadata writer for each metadata format supported in your container format. If your codec uses a Tagged Image File Format (TIFF) container, then this information is already in the registry and you don't need to create these entries.

```
HKEY_CLASSES_ROOT
   CLSID
      {Metadata Writer CLSID}
         Containers
            {Container Format GUID}
               WritePosition = Offset relative to its container
               WriteHeader = Pattern used for metadata header
               WriteOffset = Offset from beginning of header
```

If you use a TIFF-style or JPEG-style container format, you must register an association between your container and that container format. For more information, see the introduction in [Integration with Windows Photo Gallery and Windows Explorer](-wic-integrationregentries.md).

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[General Registry Entries](-wic-generalregentries.md)
</dt> <dt>

[Encoder-Specific Registry Entries](-wic-decoderregentries.md)
</dt> <dt>

[How to Write a WIC-Enabled CODEC](-wic-howtowriteacodec.md)
</dt> <dt>

[Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md)
</dt> </dl>

 

 



