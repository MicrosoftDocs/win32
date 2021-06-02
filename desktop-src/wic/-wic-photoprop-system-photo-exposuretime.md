---
description: The photo metadata policy for the System.Photo.ExposureTime property.
ms.assetid: 26f6ff27-b326-46f8-b4be-b091acbec575
title: System.Photo.ExposureTime Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.ExposureTime Photo Metadata Policy

The photo metadata policy for the [System.Photo.ExposureTime](../properties/props-system-photo-exposuretime.md) property.

### PKEY

PKEY\_Photo\_ExposureTime

### Containers

JPEG, TIFF

### Read-Only

Yes

### Output PROPVARIANT Type

VT\_R8

### Conflict Resolution Policy

This value is generated from System.Photo.ExposureTimeNumerator and System.Photo.ExposureTimeDenominator. It cannot be written directly. Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=33434} |             |
| 2     | /xmp/exif:ExposureTime        |             |



 

### Write Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=33434} |             |
| 2     | /xmp/exif:ExposureTime        |             |



 

### Remove Paths



| Order | Path                          |
|-------|-------------------------------|
| 1     | /app1/ifd/exif/{ushort=33434} |
| 2     | /xmp/exif:exposuretime        |



 

### TIFF Policies

### Read Paths



| Order | Path                       | Disk Format |
|-------|----------------------------|-------------|
| 1     | /ifd/exif/{ushort=33434}   |             |
| 2     | /ifd/xmp/exif:ExposureTime |             |



 

### Write Paths



| Order | Path                       | Disk Format |
|-------|----------------------------|-------------|
| 1     | /ifd/exif/{ushort=33434}   |             |
| 2     | /ifd/xmp/exif:ExposureTime |             |



 

### Remove Paths



| Order | Path                       |
|-------|----------------------------|
| 1     | /ifd/exif/{ushort=33434}   |
| 2     | /ifd/xmp/exif:exposuretime |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.ExposureTime](../properties/props-system-photo-exposuretime.md)
</dt> </dl>

 

 
