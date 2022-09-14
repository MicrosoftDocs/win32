---
description: The photo metadata policy for the System.GPS.MeasureMode property.
ms.assetid: 911a0d81-bd12-4155-b45a-ae1a18f2dd07
title: System.GPS.MeasureMode Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.GPS.MeasureMode Photo Metadata Policy

The photo metadata policy for the [System.GPS.MeasureMode](../properties/props-system-gps-measuremode.md) property.

### PKEY

PKEY\_GPS\_MeasureMode

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

### JPEG Policies

### Read Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=10} | ascii       |
| 2     | /xmp/exif:GPSMeasureMode  | unicode     |



 

### Write Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=10} | ascii       |
| 2     | /xmp/exif:GPSMeasureMode  | unicode     |



 

### Remove Paths



| Order | Path                      |
|-------|---------------------------|
| 1     | /app1/ifd/gps/{ushort=10} |
| 2     | /xmp/exif:gpsmeasuremode  |



 

### TIFF Policies

### Read Paths



| Order | Path                         | Disk Format |
|-------|------------------------------|-------------|
| 1     | /ifd/gps/{ushort=10}         | ascii       |
| 2     | /ifd/xmp/exif:GPSMeasureMode | unicode     |



 

### Write Paths



| Order | Path                         | Disk Format |
|-------|------------------------------|-------------|
| 1     | /ifd/gps/{ushort=10}         | ascii       |
| 2     | /ifd/xmp/exif:GPSMeasureMode | unicode     |



 

### Remove Paths



| Order | Path                         |
|-------|------------------------------|
| 1     | /ifd/gps/{ushort=10}         |
| 2     | /ifd/xmp/exif:gpsmeasuremode |



 

## Remarks

## Related topics

<dl> <dt>

[System.GPS.MeasureMode](../properties/props-system-gps-measuremode.md)
</dt> </dl>

 

 
