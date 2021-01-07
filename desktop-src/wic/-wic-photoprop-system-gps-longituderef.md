---
description: The photo metadata policy for the System.GPS.LongitudeRef property.
ms.assetid: 6e7b3b87-70e5-4c6a-a9b3-959eab38f1f0
title: System.GPS.LongitudeRef Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.GPS.LongitudeRef Photo Metadata Policy

The photo metadata policy for the [System.GPS.LongitudeRef](../properties/props-system-gps-longituderef.md) property.

### PKEY

PKEY\_GPS\_LongitudeRef

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

### Precedence of Paths (JPEG)

If the file is in JPEG format, the handler will read, write, and remove the data in the following order:



| Order | Path                         | Disk Format | Required |
|-------|------------------------------|-------------|----------|
| 1     | /xmp/exif:GPSLongitudeRef    | Unicode     | Yes      |
| 2     | /app1/ifd/gps/\\{ushort=3\\} | ASCII       | No       |



 

### Precedence of Paths (TIFF)

If the file is in TIFF format, the handler will read, write, and remove the data in the following order:



| Order | Path                          | Disk Format | Required |
|-------|-------------------------------|-------------|----------|
| 1     | /ifd/xmp/exif:GPSLongitudeRef | Unicode     | Yes      |
| 2     | /ifd/gps/\\{ushort=3\\}       | ASCII       | No       |



 

## Remarks

## Related topics

<dl> <dt>

[System.GPS.LongitudeRef](../properties/props-system-gps-longituderef.md)
</dt> </dl>

 

 
