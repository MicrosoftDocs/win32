---
description: The photo metadata policy for the System.GPS.Satellites property.
ms.assetid: 5dbbbeaf-e67d-45f6-95b2-de3287202d41
title: System.GPS.Satellites Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.GPS.Satellites Photo Metadata Policy

The photo metadata policy for the [System.GPS.Satellites](../properties/props-system-gps-satellites.md) property.

### PKEY

PKEY\_GPS\_Satellites

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

### JPEG Policies

### Read Paths



| Order | Path                     | Disk Format |
|-------|--------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=8} | ascii       |
| 2     | /xmp/exif:GPSSatellites  | unicode     |



 

### Write Paths



| Order | Path                     | Disk Format |
|-------|--------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=8} | ascii       |
| 2     | /xmp/exif:GPSSatellites  | unicode     |



 

### Remove Paths



| Order | Path                     |
|-------|--------------------------|
| 1     | /app1/ifd/gps/{ushort=8} |
| 2     | /xmp/exif:gpssatellites  |



 

### TIFF Policies

### Read Paths



| Order | Path                        | Disk Format |
|-------|-----------------------------|-------------|
| 1     | /ifd/gps/{ushort=8}         | ascii       |
| 2     | /ifd/xmp/exif:GPSSatellites | unicode     |



 

### Write Paths



| Order | Path                        | Disk Format |
|-------|-----------------------------|-------------|
| 1     | /ifd/gps/{ushort=8}         | ascii       |
| 2     | /ifd/xmp/exif:GPSSatellites | unicode     |



 

### Remove Paths



| Order | Path                        |
|-------|-----------------------------|
| 1     | /ifd/gps/{ushort=8}         |
| 2     | /ifd/xmp/exif:gpssatellites |



 

## Remarks

## Related topics

<dl> <dt>

[System.GPS.Satellites](../properties/props-system-gps-satellites.md)
</dt> </dl>

 

 
