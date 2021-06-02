---
description: The photo metadata policy for the System.GPS.ImgDirectionRef property.
ms.assetid: 74ae0989-6d53-4d72-abe9-84f40c0c884a
title: System.GPS.ImgDirectionRef Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.GPS.ImgDirectionRef Photo Metadata Policy

The photo metadata policy for the [System.GPS.ImgDirectionRef](../properties/props-system-gps-imgdirectionref.md) property.

### PKEY

PKEY\_GPS.ImgDirectionRef

### Containers

JPEG, TIFF

### Read-Only

No

### Output PROPVARIANT Type

VT\_LPWSTR

### Input Type

VT\_LPWSTR is preferred, but VT\_LPSTR is also accepted.

### Conflict Resolution Policy

Values from different schemas are reconciled.

### JPEG Policies

### Read Paths



| Order | Path                         | Disk Format |
|-------|------------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=16}    | ascii       |
| 2     | /xmp/exif:GPSImgDirectionRef | unicode     |



 

### Write Paths



| Order | Path                         | Disk Format |
|-------|------------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=16}    | ascii       |
| 2     | /xmp/exif:GPSImgDirectionRef | unicode     |



 

### Remove Paths



| Order | Path                         |
|-------|------------------------------|
| 1     | /app1/ifd/gps/{ushort=16}    |
| 2     | /xmp/exif:gpsimgdirectionref |



 

### TIFF Policies

### Read Paths



| Order | Path                             | Disk Format |
|-------|----------------------------------|-------------|
| 1     | /ifd/gps/{ushort=16}             | ascii       |
| 2     | /ifd/xmp/exif:GPSImgDirectionRef | unicode     |



 

### Write Paths



| Order | Path                             | Disk Format |
|-------|----------------------------------|-------------|
| 1     | /ifd/gps/{ushort=16}             | ascii       |
| 2     | /ifd/xmp/exif:GPSImgDirectionRef | unicode     |



 

### Remove Paths



| Order | Path                             |
|-------|----------------------------------|
| 1     | /ifd/gps/{ushort=16}             |
| 2     | /ifd/xmp/exif:gpsimgdirectionref |



 

## Remarks

## Related topics

<dl> <dt>

[System.GPS.ImgDirectionRef](../properties/props-system-gps-imgdirectionref.md)
</dt> </dl>

 

 
