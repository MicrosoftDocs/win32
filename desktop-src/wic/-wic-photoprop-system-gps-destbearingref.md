---
description: The photo metadata policy for the System.GPS.DestBearingRef property.
ms.assetid: d1c8b3cc-ed52-43ca-a0ba-045a2c5fe274
title: System.GPS.DestBearingRef Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.GPS.DestBearingRef Photo Metadata Policy

The photo metadata policy for the [System.GPS.DestBearingRef](../properties/props-system-gps-destbearingref.md) property.

### PKEY

PKEY\_GPS\_DestBearingRef

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



| Order | Path                        | Disk Format |
|-------|-----------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=23}   | ascii       |
| 2     | /xmp/exif:GPSDestBearingRef | unicode     |



 

### Write Paths



| Order | Path                        | Disk Format |
|-------|-----------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=23}   | ascii       |
| 2     | /xmp/exif:GPSDestBearingRef | unicode     |



 

### Remove Paths



| Order | Path                        |
|-------|-----------------------------|
| 1     | /app1/ifd/gps/{ushort=23}   |
| 2     | /xmp/exif:gpsdestbearingref |



 

### TIFF Policies

### Read Paths



| Order | Path                            | Disk Format |
|-------|---------------------------------|-------------|
| 1     | /ifd/gps/{ushort=23}            | ascii       |
| 2     | /ifd/xmp/exif:GPSDestBearingRef | unicode     |



 

### Write Paths



| Order | Path                            | Disk Format |
|-------|---------------------------------|-------------|
| 1     | /ifd/gps/{ushort=23}            | ascii       |
| 2     | /ifd/xmp/exif:GPSDestBearingRef | unicode     |



 

### Remove Paths



| order | path                            |
|-------|---------------------------------|
| 1     | /ifd/gps/{ushort=23}            |
| 2     | /ifd/xmp/exif:gpsdestbearingref |



 

## Remarks

## Related topics

<dl> <dt>

[System.GPS.DestBearingRef](../properties/props-system-gps-destbearingref.md)
</dt> </dl>

 

 
