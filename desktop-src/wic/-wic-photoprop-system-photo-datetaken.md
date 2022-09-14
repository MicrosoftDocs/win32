---
description: The photo metadata policy for the System.Photo.DateTaken property.
ms.assetid: 800aa01b-6064-45df-a40e-6537819df4d7
title: System.Photo.DateTaken Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.DateTaken Photo Metadata Policy

The photo metadata policy for the [System.Photo.DateTaken](../properties/props-system-photo-datetaken.md) property.

### PKEY

PKEY\_Photo\_DateTaken

### Containers

JPEG, TIFF

### Read-Only

No

### Output PROPVARIANT Type

VT\_FILETIME

### Input Type

DateTime

### Conflict Resolution Policy

Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                                  | Disk Format |
|-------|---------------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=36867}         | ascii       |
| 2     | /app13/irb/8bimiptc/iptc/date created | unicode     |
| 3     | /xmp/xmp:CreateDate                   | unicode     |
| 4     | /app1/ifd/exif/{ushort=36868}         | ascii       |
| 5     | /app13/irb/8bimiptc/iptc/date created | unicode     |
| 6     | /xmp/exif:DateTimeOriginal            | unicode     |



 

### Write Paths



| Order | Path                                  | Disk Format |
|-------|---------------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=36867}         | ascii       |
| 2     | /app13/irb/8bimiptc/iptc/date created | unicode     |
| 3     | /xmp/xmp:CreateDate                   | unicode     |
| 4     | /app1/ifd/exif/{ushort=36868}         | ascii       |
| 5     | /xmp/exif:DateTimeOriginal            | unicode     |



 

### Remove Paths



| Order | Path                                  |
|-------|---------------------------------------|
| 1     | /app1/ifd/exif/{ushort=36867}         |
| 2     | /app1/ifd/exif/{ushort=37521}         |
| 3     | /app1/ifd/exif/{ushort=36868}         |
| 4     | /app1/ifd/exif/{ushort=37522}         |
| 5     | /xmp/exif:DateTimeOriginal            |
| 6     | /xmp/xmp:CreateDate                   |
| 7     | /app13/irb/8bimiptc/iptc/date created |
| 8     | /app13/irb/8bimiptc/iptc/time created |



 

### TIFF Policy

### Read Paths



| Order | Path                                | Disk Format |
|-------|-------------------------------------|-------------|
| 1     | /ifd/exif/{ushort=36867}            | ascii       |
| 2     | /ifd/iptc/date created              | unicode     |
| 3     | /ifd/xmp/xmp:CreateDate             | unicode     |
| 4     | /ifd/exif/{ushort=36868}            | ascii       |
| 5     | /ifd/iptc/date created              | unicode     |
| 6     | /ifd/irb/8bimiptc/iptc/date created | unicode     |
| 7     | /ifd/xmp/exif:DateTimeOriginal      | unicode     |



 

### Write Paths



| Order | Path                                | Disk Format |
|-------|-------------------------------------|-------------|
| 1     | /ifd/exif/{ushort=36867}            | ascii       |
| 2     | /ifd/iptc/date created              | unicode     |
| 3     | /ifd/xmp/xmp:CreateDate             | unicode     |
| 4     | /ifd/exif/{ushort=36868}            | ascii       |
| 5     | /ifd/irb/8bimiptc/iptc/date created | unicode     |
| 6     | /ifd/xmp/exif:DateTimeOriginal      | unicode     |



 

### Remove Paths



| Order | Path                                |
|-------|-------------------------------------|
| 1     | /ifd/exif/{ushort=36867}            |
| 2     | /ifd/exif/{ushort=37521}            |
| 3     | /ifd/exif/{ushort=36868}            |
| 4     | /ifd/exif/{ushort=37522}            |
| 5     | /ifd/xmp/exif:DateTimeOriginal      |
| 6     | /ifd/xmp/xmp:CreateDate             |
| 7     | /ifd/iptc/date created              |
| 8     | /ifd/iptc/time created              |
| 9     | /ifd/irb/8bimiptc/iptc/date created |
| 10    | /ifd/irb/8bimiptc/iptc/time created |



 

### PNG Policy

### Read Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /\[\*\]tEXt/Creation Time | ascii       |



 

### Write Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 2     | /\[\*\]tEXt/Creation Time | ascii       |



 

### Remove Paths



| Order | Path                      |
|-------|---------------------------|
| 3     | /\[\*\]tEXt/Creation Time |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.DateTaken](../properties/props-system-photo-datetaken.md)
</dt> </dl>

 

 
