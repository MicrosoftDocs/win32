---
description: Defines terms that are used in WIC.
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: b066757a-8841-4976-b20b-989ebba5eb3b
title: Windows Imaging Component Glossary
ms.topic: article
ms.date: 05/31/2018
---

# Windows Imaging Component Glossary

## B

<dl> <dt>

**bit depth**
</dt> <dd>

The number of color values that can be assigned to a single pixel in an image. Color depth can range from 1 bit (black and white) to 32 bits (over 16.7 million colors). See also: Color Depth

</dd> <dt>

**bits per pixel (bpp)**
</dt> <dd>

The number of bits that represent the color value of each pixel in a digitized image. See also:BPP

</dd> </dl>

## C

<dl> <dt>

**clipper**
</dt> <dd>

An IWICBitmapClipper object.

</dd> <dt>

**codec**
</dt> <dd>

A filter that compresses (encodes) or decompresses (decodes) a data stream.

</dd> <dt>

**color context**
</dt> <dd>

An abstraction for a color profile. The profile can be loaded from a file (ie. "sRGB Color Space Profile.icm") or from a memory buffer obtained by reading. Color context information is defined by the IWICColorContext interface for WIC, and is retrieved with the GetColorContext method.

</dd> <dt>

**color transform**
</dt> <dd>

Mapping colors from the source color context to the destination color context in a given output pixel format.

</dd> <dt>

**CYMK color model**
</dt> <dd>

Multidimensional color space consisting of the cyan, magenta, yellow, and black intensities that make up a given color.

</dd> </dl>

## D

<dl> <dt>

**decoder**
</dt> <dd>

See Other Term: codec

</dd> </dl>

## E

<dl> <dt>

**encoder**
</dt> <dd>

See Other Term: codec

</dd> </dl>

## L

<dl> <dt>

**lossless**
</dt> <dd>

A type of compression that ensures that the original data can be recovered exactly, with no loss in image quality.

</dd> <dt>

**lossy**
</dt> <dd>

A process for compressing data in which information deemed unnecessary is removed and cannot be recovered upon decompression. Typically used with audio and visual data in which a slight degradation of quality is acceptable.

</dd> </dl>

## M

<dl> <dt>

**multithreaded apartment (MTA)**
</dt> <dd>

A form of multithreading that is supported by Component Object Model (COM). In a multithreaded apartment model, all of the threads in the process that have been initialized as free-threaded reside in a single apartment.

</dd> </dl>

## N

<dl> <dt>

**native pixel format**
</dt> <dd>

One of the pixel formats provided by WIC, wherein the memory layout of each pixel in a bitmap is described.

</dd> </dl>

## P

<dl> <dt>

**palette**
</dt> <dd>

Set of colors used by an object or application.

</dd> <dt>

**photo metadata policy**
</dt> <dd>

The windows policy for reading, writing, and removing image metadata.

</dd> <dt>

**pixel format**
</dt> <dd>

Size and arrangement of pixel color components in memory. It is specified by the total number of bits used per pixel and the number of bits used to store the red, green, blue, and alpha components of the color. For example, the RGB24 pixel format uses 24 bits to store a pixel color, with eight bits each for red, green, and blue. The ARGB32 pixel format uses 32 bits, with 24 bits of color information and 8 bits of alpha channel information.

</dd> <dt>

**progressive decoding**
</dt> <dd>

The process for decoding images that have been encoded with information about the different decoding levels.

</dd> </dl>

## S

<dl> <dt>

**stream**
</dt> <dd>

Refers to an IStream COM interface which can be used to sequentially read or write data to files, memory, or network locations.

</dd> </dl>

## T

<dl> <dt>

**tone curve**
</dt> <dd>

A graph used in digital photography that displays the tonal range of the image.

</dd> </dl>

## W

<dl> <dt>

**Windows Imaging Component (WIC)**
</dt> <dd>

An extensible platform that provides low-level API for digital images.

</dd> </dl>

 

 



