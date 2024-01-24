---
description: The photo metadata policy for the System.GPS.ImgDirection property.
ms.assetid: c9a0f5de-4010-4251-a5d5-8728b7ae6d33
title: System.GPS.ImgDirection Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.GPS.ImgDirection Photo Metadata Policy

The photo metadata policy for the [System.GPS.ImgDirection](../properties/props-system-gps-imgdirection.md) property.

### PKEY

PKEY\_GPS\_ImgDirection

### Containers

JPEG, TIFF

### Read-Only

Yes

### Output PROPVARIANT Type

VT\_R8

### Conflict Resolution Policy

This value can be written by writing to System.GPS.ImgDirectionNumerator and System.GPS.ImgDirectionDenominator. It cannot be written directly. Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=17} |             |
| 2     | /xmp/exif:GPSImgDirection |             |



 

### Write Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=17} |             |
| 2     | /xmp/exif:GPSImgDirection |             |



 

### Remove Paths



| Order | Path                      |
|-------|---------------------------|
| 1     | /app1/ifd/gps/{ushort=17} |
| 2     | /xmp/exif:gpsimgdirection |



 

### TIFF Policies

### Read Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /ifd/gps/{ushort=17}          |             |
| 2     | /ifd/xmp/exif:GPSImgDirection |             |



 

### Write Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /ifd/gps/{ushort=17}          |             |
| 2     | /ifd/xmp/exif:GPSImgDirection |             |



 

### Remove Paths



| Order | Path                          |
|-------|-------------------------------|
| 1     | /ifd/gps/{ushort=17}          |
| 2     | /ifd/xmp/exif:gpsimgdirection |



 

## Remarks

## Related topics

<dl> <dt>

[System.GPS.ImgDirection](../properties/props-system-gps-imgdirection.md)
</dt> </dl>

 

 
