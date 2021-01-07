---
description: The photo metadata policy for the System.Photo.WhiteBalance property.
ms.assetid: 7b3a31e6-a929-41e4-b7f0-c5b3beac2519
title: System.Photo.WhiteBalance Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.WhiteBalance Photo Metadata Policy

The photo metadata policy for the [System.Photo.WhiteBalance](../properties/props-system-photo-whitebalance.md) property.

### PKEY

PKEY\_Photo\_WhiteBalance

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
| 1     | /app1/ifd/exif/{ushort=41987} | ushort      |
| 2     | /xmp/exif:WhiteBalance        | unicode     |



 

### Write Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=41987} | ushort      |
| 2     | /xmp/exif:WhiteBalance        | unicode     |



 

### Remove Paths



| Order | Path                          |
|-------|-------------------------------|
| 1     | /app1/ifd/exif/{ushort=41987} |
| 2     | /xmp/exif:whitebalance        |



 

### TIFF Policies

### Read Paths



| Order | Path                       | Disk Format |
|-------|----------------------------|-------------|
| 1     | /ifd/exif/{ushort=41987}   | ushort      |
| 2     | /ifd/xmp/exif:WhiteBalance | unicode     |



 

### Write Paths



| Order | Path                       | Disk Format |
|-------|----------------------------|-------------|
| 1     | /ifd/exif/{ushort=41987}   | ushort      |
| 2     | /ifd/xmp/exif:WhiteBalance | unicode     |



 

### Remove Paths



| Order | Path                       |
|-------|----------------------------|
| 1     | /ifd/exif/{ushort=41987}   |
| 2     | /ifd/xmp/exif:whitebalance |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.WhiteBalance](../properties/props-system-photo-whitebalance.md)
</dt> </dl>

 

 
