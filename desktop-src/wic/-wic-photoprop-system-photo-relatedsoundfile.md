---
description: The photo metadata policy for the System.Photo.RelatedSoundFile property.
ms.assetid: 3b212d90-7ae2-4b7c-b77a-2017490aca40
title: System.Photo.RelatedSoundFile Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.RelatedSoundFile Photo Metadata Policy

The photo metadata policy for the [System.Photo.RelatedSoundFile](../properties/props-system-photo-relatedsoundfile.md) property.

### PKEY

PKEY\_Photo\_RelatedSoundFile

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



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=40964} | ascii       |
| 2     | /xmp/exif:RelatedSoundFile    | unicode     |



 

### Write Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=40964} | ascii       |
| 2     | /xmp/exif:RelatedSoundFile    | unicode     |



 

### Remove Paths



| Order | Path                          |
|-------|-------------------------------|
| 1     | /app1/ifd/exif/{ushort=40964} |
| 2     | /xmp/exif:RelatedSoundFile    |



 

### TIFF Policy

### Read Paths



| Order | Path                           | Disk Format |
|-------|--------------------------------|-------------|
| 1     | /ifd/exif/{ushort=40964}       | ascii       |
| 2     | /ifd/xmp/exif:RelatedSoundFile | unicode     |



 

### Write Paths



| Order | Path                           | Disk Format |
|-------|--------------------------------|-------------|
| 1     | /ifd/exif/{ushort=40964}       | ascii       |
| 2     | /ifd/xmp/exif:RelatedSoundFile | unicode     |



 

### Remove Paths



| Order | Path                           |
|-------|--------------------------------|
| 1     | /ifd/exif/{ushort=40964}       |
| 2     | /ifd/xmp/exif:RelatedSoundFile |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.RelatedSoundFile](../properties/props-system-photo-relatedsoundfile.md)
</dt> </dl>

 

 
