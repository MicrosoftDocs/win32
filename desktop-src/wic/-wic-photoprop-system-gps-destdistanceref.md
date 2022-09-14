---
description: The photo metadata policy for the System.GPS.DestDistanceRef property.
ms.assetid: eb671f34-7366-4182-b72e-0dd7830751e0
title: System.GPS.DestDistanceRef Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.GPS.DestDistanceRef Photo Metadata Policy

The photo metadata policy for the [System.GPS.DestDistanceRef](../properties/props-system-gps-destdistanceref.md) property.

### PKEY

PKEY\_DestDistanceRef

### Containers

JPEG, TIFF

### Read-Only

No

### Output PROPVARIANT Type

VT\_LPWSTR

### Input Type

VT\_LPWSTR or VT\_LPSTR are accepted.

### Conflict Resolution Policy

Values from different schemas are reconciled.

### JPEG Policies

### Read Paths



| Order | Path                         | Disk Format |
|-------|------------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=25}    | ascii       |
| 2     | /xmp/exif:GPSDestDistanceRef | unicode     |



 

### Write Paths



| Order | Path                         | Disk Format |
|-------|------------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=25}    | ascii       |
| 2     | /xmp/exif:GPSDestDistanceRef | unicode     |



 

### Remove Paths



| Order | Path                         |
|-------|------------------------------|
| 1     | /app1/ifd/gps/{ushort=25}    |
| 2     | /xmp/exif:gpsdestdistanceref |



 

### TIFF Policies

### Read Paths



| Order | Path                             | Disk Format |
|-------|----------------------------------|-------------|
| 1     | /ifd/gps/{ushort=25}             | ascii       |
| 2     | /ifd/xmp/exif:GPSDestDistanceRef | unicode     |



 

### Write Paths



| Order | Path                             | Disk Format |
|-------|----------------------------------|-------------|
| 1     | /ifd/gps/{ushort=25}             | ascii       |
| 2     | /ifd/xmp/exif:GPSDestDistanceRef | unicode     |



 

### Remove Paths



| Order | Path                             |
|-------|----------------------------------|
| 1     | /ifd/gps/{ushort=25}             |
| 2     | /ifd/xmp/exif:gpsdestdistanceref |



 

## Remarks

## Related topics

<dl> <dt>

[System.GPS.DestDistanceRef](../properties/props-system-gps-destdistanceref.md)
</dt> </dl>

 

 
