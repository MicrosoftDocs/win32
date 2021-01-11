---
description: The photo metadata policy for the System.GPS.Differential property.
ms.assetid: 330d1f88-5f54-4e29-b57f-eb7112203e04
title: System.GPS.Differential Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.GPS.Differential Photo Metadata Policy

The photo metadata policy for the [System.GPS.Differential](../properties/props-system-gps-differential.md) property.

### PKEY

PKEY\_GPS\_Differential

### Containers

JPEG, TIFF

### Read-Only

No

### Output PROPVARIANT Type

VT\_UI2

### Input PROPVARIANT Type

VT\_UI1, VT\_UI2, and VT\_UI4 are all accepted.

### Conflict Resolution Policy

Values from different schemas are reconciled.

### JPEG Policies

### Read Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=30} | ushort      |
| 2     | /xmp/exif:GPSDifferential | unicode     |



 

### Write Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=30} | ushort      |
| 2     | /xmp/exif:GPSDifferential | unicode     |



 

### Remove Paths



| Order | Path                      |
|-------|---------------------------|
| 1     | /app1/ifd/gps/{ushort=30} |
| 2     | /xmp/exif:gpsdifferential |



 

### TIFF Policies

### Read Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /ifd/gps/{ushort=30}          | ushort      |
| 2     | /ifd/xmp/exif:GPSDifferential | unicode     |



 

### Write Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /ifd/gps/{ushort=30}          | ushort      |
| 2     | /ifd/xmp/exif:GPSDifferential | unicode     |



 

### Remove Paths



| Order | Path                          |
|-------|-------------------------------|
| 1     | /ifd/gps/{ushort=30}          |
| 2     | /ifd/xmp/exif:gpsdifferential |



 

## Remarks

## Related topics

<dl> <dt>

[System.GPS.Differential](../properties/props-system-gps-differential.md)
</dt> </dl>

 

 
