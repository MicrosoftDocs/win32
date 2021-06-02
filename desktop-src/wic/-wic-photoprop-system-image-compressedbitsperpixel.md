---
description: The photo metadata policy for the System.Image.CompressedBitsPerPixel property.
ms.assetid: e97a5c68-6d4a-44af-8096-22680f8b16b8
title: System.Image.CompressedBitsPerPixel Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Image.CompressedBitsPerPixel Photo Metadata Policy

The photo metadata policy for the [System.Image.CompressedBitsPerPixel](../properties/props-system-image-compressedbitsperpixel.md) property.

### PKEY

PKEY\_Image\_CompressedBitsPerPixel

### Containers

JPEG, TIFF

### Read-Only

Yes

### Output PROPVARIANT Type

VT\_R8

### Conflict Resolution Policy

This value is generated from System.Image.CompressedBitsPerPixelNumerator and System.Image.CompressedBitsPerPixelDenominator. It cannot be written directly. Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                             | Disk Format |
|-------|----------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=37122}    |             |
| 2     | /xmp/exif:CompressedBitsPerPixel |             |



 

### Remove Paths



| Order | Path                             |
|-------|----------------------------------|
| 1     | /app1/ifd/exif/{ushort=37122}    |
| 2     | /xmp/exif:compressedbitsperpixel |



 

### TIFF Policies

### Read Paths



| Order | Path                                 | Disk Format |
|-------|--------------------------------------|-------------|
| 1     | /ifd/exif/{ushort=37122}             |             |
| 2     | /ifd/xmp/exif:CompressedBitsPerPixel |             |



 

### Remove Paths



| Order | Path                                 |
|-------|--------------------------------------|
| 1     | /ifd/exif/{ushort=37122}             |
| 2     | /ifd/xmp/exif:compressedbitsperpixel |



 

## Remarks

## Related topics

<dl> <dt>

[System.Image.CompressedBitsPerPixel](../properties/props-system-image-compressedbitsperpixel.md)
</dt> </dl>

 

 
