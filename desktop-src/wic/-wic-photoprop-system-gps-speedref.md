---
description: The photo metadata policy for the System.GPS.SpeedRef property.
ms.assetid: 45fea6be-1e63-4244-a93d-d446e315ddd4
title: System.GPS.SpeedRef Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.GPS.SpeedRef Photo Metadata Policy

The photo metadata policy for the [System.GPS.SpeedRef](../properties/props-system-gps-speedref.md) property.

### PKEY

PKEY\_GPS\_SpeedRef

### Containers

JPEG, TIFF

### Read-Only

No

### Output PROPVARIANT Type

VT\_LPWSTR

### Input PROPVARIANT Type

VT\_LPWSTR is preferred, but VT\_LPSTR is also accepted..

### Conflict Resolution Policy

Values from different schemas are reconciled.

### JPEG Policies

### Read Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=12} | ascii       |
| 2     | /xmp/exif:GPSSpeedRef     | unicode     |



 

### Write Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=12} | ascii       |
| 2     | /xmp/exif:GPSSpeedRef     | unicode     |



 

### Remove Paths



| Order | Path                      | Disk format |
|-------|---------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=12} |             |
| 2     | /xmp/exif:gpsspeedref     |             |



 

### TIFF Policies

### Read Paths



| Order | Path                      |         |
|-------|---------------------------|---------|
| 1     | /ifd/gps/{ushort=12}      | ascii   |
| 2     | /ifd/xmp/exif:GPSSpeedRef | unicode |



 

### Write Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /ifd/gps/{ushort=12}      | ascii       |
| 2     | /ifd/xmp/exif:GPSSpeedRef | unicode     |



 

### Remove Paths



| Order | Path                      |
|-------|---------------------------|
| 1     | /ifd/gps/{ushort=12}      |
| 2     | /ifd/xmp/exif:gpsspeedref |



 

## Remarks

## Related topics

<dl> <dt>

[System.GPS.SpeedRef](../properties/props-system-gps-speedref.md)
</dt> </dl>

 

 
