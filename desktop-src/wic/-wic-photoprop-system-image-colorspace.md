---
description: The photo metadata policy for the System.Image.ColorSpace property.
ms.assetid: 10770f16-8db2-4719-bce3-452f578002ec
title: System.Image.ColorSpace Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Image.ColorSpace Photo Metadata Policy

The photo metadata policy for the [System.Image.ColorSpace](../properties/props-system-image-colorspace.md) property.

### PKEY

PKEY\_Image\_ColorSpace

### Containers

JPEG, TIFF

### Read-Only

Yes

### Output PROPVARIANT Type

VT\_UI2

### Input Type

UShort

### Conflict Resolution Policy

Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=40961} | ushort      |
| 2     | /xmp/exif:ColorSpace          | unicode     |



 

### Write Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=40961} | ushort      |
| 2     | /xmp/exif:ColorSpace          | unicode     |



 

### Remove Paths



| Order | Path                          |
|-------|-------------------------------|
| 1     | /app1/ifd/exif/{ushort=40961} |
| 2     | /xmp/exif:colorspace          |



 

### TIFF Policies

### Read Paths



| Order | Path                     | Disk Format |
|-------|--------------------------|-------------|
| 1     | /ifd/exif/{ushort=40961} | ushort      |
| 2     | /ifd/xmp/exif:ColorSpace | unicode     |



 

### Write Paths



| Order | Path                     | Disk Format |
|-------|--------------------------|-------------|
| 1     | /ifd/exif/{ushort=40961} | ushort      |
| 2     | /ifd/xmp/exif:ColorSpace | unicode     |



 

### Remove Paths



| Order | Path                     |
|-------|--------------------------|
| 1     | /ifd/exif/{ushort=40961} |
| 2     | /ifd/xmp/exif:colorspace |



 

## Remarks

## Related topics

<dl> <dt>

[System.Image.ColorSpace](../properties/props-system-image-colorspace.md)
</dt> </dl>

 

 
