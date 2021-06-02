---
description: The photo metadata policy for the System.GPS.DestLongitudeRef property.
ms.assetid: 2a0abb9b-41e3-49ba-a60b-3096d9c032bd
title: System.GPS.DestLongitudeRef Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.GPS.DestLongitudeRef Photo Metadata Policy

The photo metadata policy for the [System.GPS.DestLongitudeRef](../properties/props-system-gps-destlongituderef.md) property.

### PKEY

PKEY\_GPS.DestLongitudeRef

### Containers

JPEG, TIFF

### Read-Only

No

### Output PROPVARIANT Type

VT\_LPWSTR

### Input PROPVARIANT Type

VT\_LPWSTR is preferred, but VT\_LPSTR is also accepted.

### Conflict Resolution Policy

Values from different schemas are reconciled.

### Precedence of Paths (JPEG)

If the file is in JPEG format, the handler will read, write, and remove the data in the following order:



| Order | Path                          | Disk Format | Required |
|-------|-------------------------------|-------------|----------|
| 1     | /xmp/exif:GPSDestLongitudeRef | Unicode     | Yes      |
| 2     | /app1/ifd/gps/\\{ushort=21\\} | ASCII       | No       |



 

### Precedence of Paths (TIFF)

If the file is in TIFF format, the handler will read, write, and remove the data in the following order:



| Order | Path                              | Disk Format | Required |
|-------|-----------------------------------|-------------|----------|
| 1     | /ifd/xmp/exif:GPSDestLongitudeRef | Unicode     | Yes      |
| 2     | /ifd/gps/\\{ushort=21\\}          | ASCII       | No       |



 

## Remarks

## Related topics

<dl> <dt>

[System.GPS.DestLongitudeRef](../properties/props-system-gps-destlongituderef.md)
</dt> </dl>

 

 
