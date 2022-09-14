---
description: The photo metadata policy for the System.GPS.DestBearing property.
ms.assetid: ccc31b3d-27fd-4a8c-a304-852cf6114ec5
title: System.GPS.DestBearing Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.GPS.DestBearing Photo Metadata Policy

The photo metadata policy for the [System.GPS.DestBearing](../properties/props-system-gps-destbearing.md) property.

### PKEY

PKEY\_GPS\_DestBearing

### Containers

JPEG, TIFF

### Read-Only

Yes

### Output PROPVARIANT Type

VT\_R8

### Conflict Resolution Policy

This value can be written by writing to System.GPS.DestBearingNumerator and System.GPS.DestBearingDenominator. It cannot be written directly. Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=24} |             |
| 2     | /xmp/exif:GPSDestBearing  |             |



 

### Write Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=24} |             |
| 2     | /xmp/exif:GPSDestBearing  |             |



 

### Remove Paths



| Order | Path                      | Disk format |
|-------|---------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=24} |             |
| 2     | /xmp/exif:gpsdestbearing  |             |



 

### TIFF Policies

### Read Paths



| Order | Path                         | Disk Format |
|-------|------------------------------|-------------|
| 1     | /ifd/gps/{ushort=24}         |             |
| 2     | /ifd/xmp/exif:GPSDestBearing |             |



 

### Write Paths



| Order | Path                         | Disk Format |
|-------|------------------------------|-------------|
| 1     | /ifd/gps/{ushort=24}         |             |
| 2     | /ifd/xmp/exif:GPSDestBearing |             |



 

### Remove Paths



| Order | Path                         |
|-------|------------------------------|
| 1     | /ifd/gps/{ushort=24}         |
| 2     | /ifd/xmp/exif:gpsdestbearing |



 

## Remarks

## Related topics

<dl> <dt>

[System.GPS.DestBearing](../properties/props-system-gps-destbearing.md)
</dt> </dl>

 

 
