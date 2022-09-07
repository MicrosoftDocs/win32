---
description: "Learn more about: How the Windows Imaging Component works"
ms.assetid: c233e25b-bec6-4e67-8fbf-2bf9b70c7522
title: How the Windows Imaging Component works
ms.topic: article
ms.date: 05/31/2018
---

# How the Windows Imaging Component works

## Discovery and arbitration

Before an image can be decoded, an appropriate codec must be found that can decode that image format. In most systems, because the supported image formats are hard-coded, no discovery process is required. Because the Windows Imaging Component (WIC) platform is extensible, it’s necessary to be able to identify the format of an image and match it with an appropriate codec.

To support run-time discovery, each image format must have an identifying pattern that can be used to identify the appropriate decoder for that format. (It is strongly recommended that, for new file formats, you use a GUID for the identifying pattern, because it is guaranteed to be unique.) The identifying pattern must be embedded in each image file that conforms to that image format. Each decoder has a registry entry that specifies the identifying pattern or patterns of the image formats it can decode. When an application needs to open an image, it requests a decoder from WIC. WIC looks up the available decoders in the registry, and checks each registry entry for an identifying pattern that matches the pattern embedded in the image file. For more information on decoder registry entries, see [Encoder-Specific Registry Entries](-wic-decoderregentries.md)

When WIC finds a single decoder that matches the identifying pattern in the image, it creates an instance of the decoder and passes the image file to it. If WIC finds more than one match, it invokes a method called [**QueryCapability**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapdecoder-querycapability) on each matching decoder to arbitrate among them and find the best match. For more information, see the [QueryCapabilities](-wic-imp-iwicbitmapdecoder.md) section in the [Implementing IWICBitmapDecoder](-wic-imp-iwicbitmapdecoder.md).

## Decoding

After the appropriate decoder has been selected and instantiated, the application talks directly to the decoder. The decoder has several responsibilities, which it implements through various interfaces. These services can be classified as:

-   Container-level services
-   Frame-level services
-   Metadata enumeration services
-   Native decoder transforms
-   Progress notifications and cancellation support
-   Raw processing services

Container-level services include retrieving the top-level thumbnail (if supported), preview, color contexts, palette (if applicable), and container format, as well as providing access to the individual image frames within the container. (Some containers contain only a single frame while others, such as Tagged Image File Format (TIFF), can contain multiple frames.) This set of services also includes providing information about the decoder itself, and its capabilities with respect to a specific image file.

Individual frames have their own thumbnails, and may also have their own color contexts, palettes, and other properties, which are exposed at the frame level. The most important operation performed at the frame level, though, is the actual decoding of the image bits for that frame.

WIC provides metadata readers for the most common metadata formats (IFD, EXIF, IPTC, XMP, APP0, APP1, and other formats), and also supports extensibility for third-party metadata formats. This frees the codec of the responsibility for parsing metadata. However, the codec is responsible for enumerating the metadata blocks and requesting a metadata reader for each block. WIC performs discovery for metadata handlers the same way it does for codecs, based on a pattern in the block header matching a pattern in the metadata handler’s registry entry. For more information, see the [Encoder-Specific Registry Entries](-wic-decoderregentries.md)

Decoders are not required to natively support transform operations, but doing so enables significant performance optimizations that provide a better end-user experience. For example, an application can create a pipeline of various transforms (scaling, cropping, rotation, and pixel format conversion) to perform on an image before the image is rendered. For more information on transform pipelines, see [IWICBitmapSource](-wic-imp-iwicbitmapsource.md). After creating a transform pipeline, the application requests the final transform in the pipeline to produce the bitmap that results from applying all the transforms to the image source. At that point, if the decoder itself is able to perform transform operations, WIC asks which of the requested transforms it can perform. Any requested transforms the decoder cannot perform will be performed by WIC on the decoded image before returning it to the caller. This optimized transform pipeline provides better performance than performing each transform sequentially in memory, particularly when some or all of the transforms can be accomplished during the decoding process.

Progress notifications and cancellation support enable an application to request progress notifications for lengthy operations, and also enable the application to give the user an opportunity to cancel an operation that is taking too long. This is important because if a user cannot cancel an operation, he or she may feel the process has hung, and try to cancel it by closing the application.

These interfaces are described in detail in the section on [Implementing a WIC-enabled decoder](-wic-implementingwicdecoder.md).

Raw processing services include adjusting camera settings, such as exposure, contrast, and sharpening, or changing the color space before processing the raw bits.

## Encoding

Like decoders, encoders have responsibilities that they implement through interfaces. The services that encoders provide are complementary to the services provided by decoders, except they write out image data rather than reading it. Encoders also provide services in the following categories:

-   Container-level services
-   Frame-level services
-   Metadata enumeration and update services
-   Progress notification and cancellation support

Container-level services for an encoder include setting the top-level thumbnail (if supported), preview, and palette (if applicable), and iterating through the individual image frames so they can be serialized into the container.

Frame-level services for an encoder mirror those for the decoder, except that they write out the image data, thumbnail, and any associated palette or other component, rather than reading them.

Also, metadata enumeration services for an encoder include iterating through the metadata blocks to be written, and invoking the appropriate metadata writers to serialize the metadata to disk.

These interfaces are described in detail in the section on [Implementing a WIC-enabled encoder](-wic-implementingwicencoder.md).

## The lifetime of a codec

A WIC codec is instantiated to handle a single image, and usually has a short lifetime. It’s created when an image is loaded and is released when the image is closed. An application may use a large number of codecs simultaneously with overlapping lifetimes (think of scrolling through a directory containing hundreds of images), and multiple applications may be doing this at the same time.

Although some codecs have a lifetime that is scoped to the lifetime of the process in which they live, this is not the case with WIC codecs. The Windows Vista Photo Gallery, Windows Explorer, and Photo Viewer, as well as numerous other applications, are built on WIC and will be using your codec to display images and thumbnails. If the lifetime of your codec were scoped to the lifetime of the process, every time an image or thumbnail was displayed in the Windows Vista Explorer, the codec instantiated to decode that image would remain in memory until the next time the user restarted his or her computer. If your codec is never unloaded, its resources are, in effect, "leaked" because they can't be used by any other component in the system.

## How to WIC-enable a codec

1.  Implement a container-level decoder class and a frame-level decoder class that exposes the required WIC interfaces for decoding images and iterating through blocks of metadata. This enables all WIC-based applications to interact with your codec the same way they interact with standard image formats.
2.  Implement a container-level encoder class and a frame-level encoder class that exposes the required WIC interfaces for encoding images and serializing blocks of metadata into an image file.
3.  If your container format is not based on a TIFF or JPEG container, you may need to write metadata handlers for the common metadata formats (EXIF, XMP). However, if you use a TIFF-based or JPEG-based container format, this is not necessary because you can delegate to the system-provided metadata handlers.
4.  Embed a unique identifying pattern (we recommend a GUID) in all your image files. This enables your image format to be matched against your codec during the discovery. If you are writing a WIC wrapper for an existing image format, you must find a pattern of bits that the encoder always writes into its image files that’s unique to that image format, and use this as the identifying pattern.)
5.  Register your codec at installation time. This enables your codec to be discovered at run time by matching the identifying pattern in the registry with the pattern embedded in the image file.
6.  As of Windows 7, WIC requires that codecs be of COM apartment type "Both". This means that you must do the appropriate locking to handle cross-apartment callers and callers in multi-threaded scenarios. For more information, see the next section on multi-threaded apartment support.
7.  Support for 64-bit platforms: For Windows 7, WIC will require that third-party WIC codecs be delivered as both 32-bit and 64-bit native binaries. Further, the 32-bit form must install and run on 64-bit systems, and the third party Windows 7 codec installer must install both the 32-bit and 64-bit binaries on 64-bit systems.

## Multi-threaded apartment support in WIC

Objects within a Multi-Threaded Apartment (MTA) may be called concurrently by any number of threads within the MTA. This allows for better performance on multi-core systems and certain server scenarios. In addition, WIC codecs in an MTA can call other objects in the MTA without the marshalling cost associated with calling between threads in different STA apartments. In Windows 7, all in-box WIC codecs have been updated to support MTAs, including JPEG, TIFF, PNG, GIF, ICO, and BMP. It is highly recommended that third-party codecs be written to support MTAs. Third-party codecs that do not to support MTAs cause significant performance costs in multi-threaded applications because of marshaling. Enabling MTA support requires proper synchronization to be implemented in the third-party codec. Exact implementation of these synchronization techniques is beyond the scope of this paper. For more information on synchronizing COM objects, see [Understanding and Using COM Threading Models](/previous-versions/ms809971(v=msdn.10)).

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Introduction (how to write a WIC-enabled codec)](-wic-howtowriteacodec-intro.md)
</dt> <dt>

[Implementing a WIC-enabled decoder](-wic-implementingwicdecoder.md)
</dt> <dt>

[How to write a WIC-enabled codec](-wic-howtowriteacodec.md)
</dt> <dt>

[Windows Imaging Component overview](-wic-about-windows-imaging-codec.md)
</dt> <dt>

[WIC metadata overview](-wic-about-metadata.md)
</dt> </dl>
