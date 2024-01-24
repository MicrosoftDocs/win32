---
description: The photo metadata policy for the System.Photo.MakerNote property.
ms.assetid: e1018bc6-3fd2-4212-afee-6811bfe99f14
title: System.Photo.MakerNote Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.MakerNote Photo Metadata Policy

The photo metadata policy for the [System.Photo.MakerNote](../properties/props-system-photo-makernote.md) property.

### PKEY

PKEY\_Photo\_MakerNote

### Containers

JPEG, TIFF

### Read-Only

No

### Output PROPVARIANT Type

VT\_VECTOR \| VTUI1

### Input Type

Buffer

### Conflict Resolution Policy

Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=37500} |             |



 

### Write Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=37500} |             |



 

### Remove Paths



| Order | Path                          |
|-------|-------------------------------|
| 1     | /app1/ifd/exif/{ushort=37500} |



 

### TIFF Policies

### Read Paths



| Order | Path                     | Disk Format |
|-------|--------------------------|-------------|
| 1     | /ifd/exif/{ushort=37500} |             |



 

### Write Paths



| Order | Path                     | Disk Format |
|-------|--------------------------|-------------|
| 1     | /ifd/exif/{ushort=37500} |             |



 

### Remove Paths



| Order | Path                     |
|-------|--------------------------|
| 1     | /ifd/exif/{ushort=37500} |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.MakerNote](../properties/props-system-photo-makernote.md)
</dt> </dl>

 

 
