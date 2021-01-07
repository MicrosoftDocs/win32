---
description: The photo metadata policy for the System.Photo.Saturation property.
ms.assetid: 1dbb7515-7022-404c-928a-9eb09e43e7a7
title: System.Photo.Saturation Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.Saturation Photo Metadata Policy

The photo metadata policy for the [System.Photo.Saturation](../properties/props-system-photo-saturation.md) property.

### PKEY

PKEY\_Photo\_Saturation

### Containers

JPEG, TIFF

### Read-Only

No

### Output PROPVARIANT Type

VT\_UI4

### Input Type

UShort

### Conflict Resolution Policy

Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=41993} | ushort      |
| 2     | /xmp/exif:Saturation          | unicode     |



 

### Write Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=41993} | ushort      |
| 2     | /xmp/exif:Saturation          | unicode     |



 

### Remove Paths



| Order | Path                          |
|-------|-------------------------------|
| 1     | /app1/ifd/exif/{ushort=41993} |
| 2     | /xmp/exif:saturation          |



 

### TIFF Policies

### Read Paths



| Order | Path                     | Disk Format |
|-------|--------------------------|-------------|
| 1     | /ifd/exif/{ushort=41993} | ushort      |
| 2     | /ifd/xmp/exif:Saturation | unicode     |



 

### Write Paths



| Order | Path                     | Disk Format |
|-------|--------------------------|-------------|
| 1     | /ifd/exif/{ushort=41993} | ushort      |
| 2     | /ifd/xmp/exif:Saturation | unicode     |



 

### Remove Paths



| Order | Path                     |
|-------|--------------------------|
| 1     | /ifd/exif/{ushort=41993} |
| 2     | /ifd/xmp/exif:saturation |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.Saturation](../properties/props-system-photo-saturation.md)
</dt> </dl>

 

 
