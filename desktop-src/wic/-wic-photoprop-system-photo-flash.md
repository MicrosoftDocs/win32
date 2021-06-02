---
description: The photo metadata policy for the System.Photo.Flash property.
ms.assetid: 24b400a4-f4c7-4b59-a9e3-8a20144cd52e
title: System.Photo.Flash Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.Flash Photo Metadata Policy

The photo metadata policy for the [System.Photo.Flash](../properties/props-system-photo-exposuretime.md) property.

### PKEY

PKEY\_Photo\_Flash

### Containers

JPEG, TIFF

### Read-Only

No

### Output PROPVARIANT Type

VT\_UI1 (if the source schema was XMP), or VT\_UI2 (if the source schema was EXIF)

\\lang1036

### Input Type

VT\_UI1, VTUI2, VT\_UI4

\\lang1033

### Conflict Resolution Policy

Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                             | Disk Format |
|-------|----------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=37385}    | ushort      |
| 2     | /xmp/<xmpstruct>exif:Flash |             |



 

### Write Paths



| Order | Path                             | Disk Format |
|-------|----------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=37385}    | ushort      |
| 2     | /xmp/<xmpstruct>exif:Flash |             |



 

### Remove Paths



| Order | Path                             |
|-------|----------------------------------|
| 1     | /app1/ifd/exif/{ushort=37385}    |
| 2     | /xmp/<xmpstruct>exif:flash |



 

### TIFF Policies

### Read Paths



| Order | Path                                 | Disk Format |
|-------|--------------------------------------|-------------|
| 1     | /ifd/exif/{ushort=37385}             | ushort      |
| 2     | /ifd/xmp/<xmpstruct>exif:Flash |             |



 

### Write Paths



| Order | Path                                 | Disk Format |
|-------|--------------------------------------|-------------|
| 1     | /ifd/exif/{ushort=37385}             | ushort      |
| 2     | /ifd/xmp/<xmpstruct>exif:Flash |             |



 

### Remove Paths



| Order | Path                                 |
|-------|--------------------------------------|
| 1     | /ifd/exif/{ushort=37385}             |
| 2     | /ifd/xmp/<xmpstruct>exif:flash |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.Flash](../properties/props-system-photo-exposuretime.md)
</dt> </dl>

 

 
