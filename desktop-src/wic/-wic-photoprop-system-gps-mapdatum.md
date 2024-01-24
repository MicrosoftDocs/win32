---
description: The photo metadata policy for the System.GPS.MapDatum property.
ms.assetid: be31e98f-5114-4693-a9ef-37fea334875b
title: System.GPS.MapDatum Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.GPS.MapDatum Photo Metadata Policy

The photo metadata policy for the [System.GPS.MapDatum](../properties/props-system-gps-mapdatum.md) property.

### PKEY

PKEY\_GPS\_MapDatum

### Containers

JPEG, TIFF

### Read-Only

No

### Output PROPVARIANT Type

VT\_LPWSTR

### Input Type

VT\_LPWSTR is preferred, but VT\_LPSTR is also accepted

### Conflict Resolution Policy

Values from different schemas are reconciled.

### Precedence of Paths (JPEG)

If the file is in JPEG format, the handler will read, write, and remove the data in the following order:



| Order | Path                          | Disk Format | Required |
|-------|-------------------------------|-------------|----------|
| 1     | /xmp/exif:GPSMapDatum         | Unicode     | Yes      |
| 2     | /app1/ifd/gps/\\{ushort=18\\} | ASCII       | No       |



 

### Precedence of Paths (TIFF)

If the file is in TIFF format, the handler will read, write, and remove the data in the following order:



| Order | Path                      | Disk Format | Required |
|-------|---------------------------|-------------|----------|
| 1     | /ifd/xmp/exif:GPSMapDatum | Unicode     | Yes      |
| 2     | /ifd/gps/\\{ushort=18\\}  | ASCII       | No       |



 

## Remarks

## Related topics

<dl> <dt>

[System.GPS.MapDatum](../properties/props-system-gps-mapdatum.md)
</dt> </dl>

 

 
