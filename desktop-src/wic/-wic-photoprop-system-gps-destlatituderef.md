---
description: The photo metadata policy for the System.GPS.DestLatitudeRef property.
ms.assetid: 8a13642a-0d29-4193-9784-f716bc428c72
title: System.GPS.DestLatitudeRef Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.GPS.DestLatitudeRef Photo Metadata Policy

The photo metadata policy for the [System.GPS.DestLatitudeRef](../properties/props-system-gps-destlatituderef.md) property.

### PKEY

PKEY\_GPS\_DestLatitudeRef

### Containers

JPEG, TIFF

### Read-Only

No

### Output PROPVARIANT Type

VT\_LPWSTR

### Input Type

VT\_LPWSTR is preferred, but VT\_LPSTR is accepted.

### Conflict Resolution Policy

Values from different schemas are reconciled.

### Precedence of Paths (JPEG)

If the file is in JPEG format, the handler will read, write, and remove the data in the following order:



| Order | Path                          | Disk Format | Required |
|-------|-------------------------------|-------------|----------|
| 1     | /xmp/exif:GPSDestLatitudeRef  | Unicode     | Yes      |
| 2     | /app1/ifd/gps/\\{ushort=19\\} | ASCII       | No       |



 

### Precedence of Paths (TIFF)

If the file is in TIFF format, the handler will read, write, and remove the data in the following order:



| Order | Path                             | Disk Format | Required |
|-------|----------------------------------|-------------|----------|
| 1     | /ifd/xmp/exif:GPSDestLatitudeRef | Unicode     | Yes      |
| 2     | /ifd/gps/\\{ushort=19\\}         | ASCII       | No       |



 

## Remarks

## Related topics

<dl> <dt>

[System.GPS.DestLatitudeRef](../properties/props-system-gps-destlatituderef.md)
</dt> </dl>

 

 
