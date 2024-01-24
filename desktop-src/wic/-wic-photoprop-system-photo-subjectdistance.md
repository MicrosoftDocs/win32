---
description: The photo metadata policy for the System.Photo.SubjectDistance property.
ms.assetid: 8d5acd7e-7227-4a79-890a-43e6dace3864
title: System.Photo.SubjectDistance Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.SubjectDistance Photo Metadata Policy

The photo metadata policy for the [System.Photo.SubjectDistance](../properties/props-system-photo-subjectdistance.md) property.

### PKEY

PKEY\_Photo\_SubjectDistance

### Containers

JPEG, TIFF

### Read-Only

Yes

### Output PROPVARIANT Type

VT\_R8

### Conflict Resolution Policy

This value is generated from System.Photo.SubjectDistanceNumerator and System.Photo.SubjectDistanceDenominator. It cannot be written directly. Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=37382} |             |
| 2     | /xmp/exif:SubjectDistance     |             |



 

### Write Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=37382} |             |
| 2     | /xmp/exif:SubjectDistance     |             |



 

### Remove Paths



| Order | Path                          |
|-------|-------------------------------|
| 1     | /app1/ifd/exif/{ushort=37382} |
| 2     | /xmp/exif:subjectdistance     |



 

### TIFF Policies

### Read Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /ifd/exif/{ushort=37382}      |             |
| 2     | /ifd/xmp/exif:SubjectDistance |             |



 

### Write Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /ifd/exif/{ushort=37382}      |             |
| 2     | /ifd/xmp/exif:SubjectDistance |             |



 

### Remove Paths



| Order | Path                          |
|-------|-------------------------------|
| 1     | /ifd/exif/{ushort=37382}      |
| 2     | /ifd/xmp/exif:subjectdistance |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.SubjectDistance](../properties/props-system-photo-subjectdistance.md)
</dt> </dl>

 

 
