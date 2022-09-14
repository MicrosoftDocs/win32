---
description: Decoder-Specific Registry Entries
ms.assetid: 64ef260a-ed7f-4253-a644-bd3352b0ee41
title: Decoder-Specific Registry Entries
ms.topic: article
ms.date: 05/31/2018
---

# Decoder-Specific Registry Entries


In addition to the registry entries required for all encoders and decoders, the following registry entries are required specifically for decoders.

These entries register your decoder under the category of Windows Imaging Component (WIC) decoders. The first GUID in these entries is the category identifier (CATID) for [**WICBitmapDecoders**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapdecoder).

```
HKEY_CLASSES_ROOT
   CLSID
      {7ED96837-96F0-4812-B211-F13C24117ED3}
         Instance
            {Decoder CLSID}
               CLSID = {Decoder CLSID}
               FriendlyName = {Name of Decoder}
```

As noted in [Discovery and Arbitration](-wic-howwicworks.md) section of How The Windows Imaging Component Works, the mechanism that enables an appropriate decoder for a specific image to be discovered at run time is based on matching an identifying pattern embedded in the image file with a pattern specified in the decoder’s registry entry. To enable run-time discovery of decoders, you must register the unique identifying pattern for your image format as follows. All of these registry entries are required except for the **EndOfStream** entry, which is optional, as described in the following table.

```
HKEY_CLASSES_ROOT
   CLSID
      {Decoder CLSID}
         Patterns
            {0}
               Position = Offset in block
               Length = Length of pattern
               Pattern = Pattern to match
               Mask = FF FF FF FF
               EndOfStream = 0|1
```



| Value       | Description                                                                                                                                                                                                                                                                                                                     |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Position    | The offset into the file where the pattern can be found.                                                                                                                                                                                                                                                                        |
| Length      | The length of the pattern.                                                                                                                                                                                                                                                                                                      |
| Pattern     | The actual bits that make up the pattern. These are the bits that are matched against the identifying pattern in an image file during discovery.                                                                                                                                                                                |
| Mask        | Allows for wildcard values in patterns. The mask is applied by performing a logical AND operation on the pattern and the mask. Any bit in the pattern that corresponds to a bit in the mask with a value of 0 is ignored.                                                                                                       |
| EndOfStream | The offset of the identifying pattern should be calculated from the end of the stream, rather than the beginning. Some image formats place the identifying pattern at or near the end of the file. Because the default is to seek from the beginning, unless your pattern is near the end of the file, you can omit this entry. |



 

A codec can support more than one identifying pattern. In that case, you would repeat all of the keys under **HKEY\_CLASSES\_ROOT\\CLSID\\{Decoder CLSID}\\Patterns**, and use the numerical key (0 in the example) to distinguish between the different patterns. You must include each of the four values under the key for each pattern.

## Registering a Container Format with Metadata Readers

If you create a new container format for your codec, you must also create registry entries to support discovery of metadata readers for the metadata blocks in your images, just as you did for the metadata writers. The following entries need to be created under the class identifier (CLSID) of the metadata reader for each metadata format your container format supports. (Note that, if your codec uses a Tagged Image File Format (TIFF) container, then this information is already in the registry.)

```
HKEY_CLASSES_ROOT
   CLSID
      {Metadata Reader CLSID}
         Containers
            {Container Format GUID}
               
                  Position = Offset relative to its container
                  Pattern = Pattern used for metadata header
                  Mask = FF FF FF FF
                  DataOffset = Offset from beginning of header
```

Because the entries for metadata readers are also used for discovery, they are very similar to the entries for decoders. These entries are used by the component factory to find the metadata readers supported by your container, and to select the appropriate one, when your [**IWICMetadataBlockReader**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicmetadatablockreader) implementation requests a metadata reader.



| Value      | Description                                                                                                                                                                                                                                                                 |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Position   | The offset in the metadata block’s container where the metadata header can be found. For top-level metadata blocks, this is the offset in the file stream. For metadata blocks nested in other metadata blocks, it is the offset relative to the containing metadata block. |
| Pattern    | The actual bits that make up the pattern. These are the bits that are matched against the identifying pattern in an image file during discovery.                                                                                                                            |
| Mask       | The metadata header is generally defined by the metadata handler. You should use the standard metadata header for each reader unless, for some reason, the pattern must have a different format in your container.                                                          |
| DataOffset | The offset from the beginning of the metadata header at which the actual data begins. In cases where the metadata isn’t located at a specific offset from the header, this entry can be omitted.                                                                            |



 

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Encoder-Specific Registry Entries](-wic-encoderregentries.md)
</dt> <dt>

[Integration with Windows Photo Gallery and Windows Explorer](-wic-integrationregentries.md)
</dt> <dt>

[How to Write a WIC-Enabled CODEC](-wic-howtowriteacodec.md)
</dt> <dt>

[Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md)
</dt> </dl>

 

 



