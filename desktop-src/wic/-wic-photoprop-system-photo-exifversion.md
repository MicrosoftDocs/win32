---
description: The photo metadata policy for the System.Photo.EXIFVersion property.
ms.assetid: 0f9c5ea8-918f-4101-8492-3f408145a73e
title: System.Photo.EXIFVersion Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.EXIFVersion Photo Metadata Policy

The photo metadata policy for the [System.Photo.EXIFVersion](../properties/props-system-photo-exifversion.md) property.

### PKEY

PKEY\_Photo\_EXIFVersion

### Containers

JPEG, TIFF

### Read-Only

No

### Output PROPVARIANT Type

VT\_LPWSTR

### Input Type

String.

### Conflict Resolution Policy

Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                          | Disk Format   |
|-------|-------------------------------|---------------|
| 1     | /app1/ifd/exif/{ushort=36864} | exif\_version |
| 2     | /xmp/exif:ExifVersion         | unicode       |



 

### Write Paths



| Order | Path                          | Disk Format   |
|-------|-------------------------------|---------------|
| 1     | /app1/ifd/exif/{ushort=36864} | exif\_version |
| 2     | /xmp/exif:ExifVersion         | unicode       |



 

### Remove Paths



| Order | Path                          |
|-------|-------------------------------|
| 1     | /app1/ifd/exif/{ushort=36864} |
| 2     | /xmp/exif:ExifVersion         |



 

### TIFF Policy

### Read Paths



| Order | Path                      | Disk Format   |
|-------|---------------------------|---------------|
| 1     | /ifd/exif/{ushort=36864}  | exif\_version |
| 2     | /ifd/xmp/exif:ExifVersion | unicode       |



 

### Write Paths



| Order | Path                      | Disk Format   |
|-------|---------------------------|---------------|
| 1     | /ifd/exif/{ushort=36864}  | exif\_version |
| 2     | /ifd/xmp/exif:ExifVersion | unicode       |



 

### Remove Paths



| Order | Path                      |
|-------|---------------------------|
| 1     | /ifd/exif/{ushort=36864}  |
| 2     | /ifd/xmp/exif:ExifVersion |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.EXIFVersion](../properties/props-system-photo-exifversion.md)
</dt> </dl>

 

 
