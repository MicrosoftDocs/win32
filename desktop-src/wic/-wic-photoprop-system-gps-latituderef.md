---
description: The photo metadata policy for the System.GPS.LatitudeRef property.
ms.assetid: 057015fd-38b7-4053-b611-72565975cc58
title: System.GPS.LatitudeRef Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.GPS.LatitudeRef Photo Metadata Policy

The photo metadata policy for the [System.GPS.LatitudeRef](../properties/props-system-gps-latitude.md) property.

### PKEY

PKEY\_GPS\_LatitudeRef

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

### Precedence of Paths (JPEG)

If the file is in JPEG format, the handler will read, write, and remove the data in the following order:



| Order | Path                         | Disk Format | Required |
|-------|------------------------------|-------------|----------|
| 1     | /xmp/exif:GPSLatitudeRef     | Unicode     | Yes      |
| 2     | /app1/ifd/gps/\\{ushort=1\\} | ASCII       | No       |



 

### Precedence of Paths (TIFF)

If the file is in TIFF format, the handler will read, write, and remove the data in the following order:



| Order | Path                         | Disk Format | Required |
|-------|------------------------------|-------------|----------|
| 1     | /ifd/xmp/exif:GPSLatitudeRef | Unicode     | Yes      |
| 2     | /ifd/gps/\\{ushort=1\\}      | ASCII       | No       |



 

## Remarks

## Related topics

<dl> <dt>

[System.GPS.LatitudeRef](../properties/props-system-gps-latitude.md)
</dt> </dl>

 

 
