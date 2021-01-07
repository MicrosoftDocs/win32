---
description: The photo metadata policy for the System.GPS.ProcessingMethod property.
ms.assetid: 840021a8-ec1d-4916-93b2-7cc1803e2d8c
title: System.GPS.ProcessingMethod Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.GPS.ProcessingMethod Photo Metadata Policy

The photo metadata policy for the [System.GPS.ProcessingMethod](../properties/props-system-gps-processingmethod.md) property.

### PKEY

PKEY\_GPS\_ProcessingMethod

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



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=27}     |             |
| 2     | /xmp/exif:GPSProcessingMethod | unicode     |



 

### Write Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=27}     |             |
| 2     | /xmp/exif:GPSProcessingMethod | unicode     |



 

### Remove Paths



| Order | Path                          |
|-------|-------------------------------|
| 1     | /app1/ifd/gps/{ushort=27}     |
| 2     | /xmp/exif:gpsprocessingmethod |



 

### TIFF Policies

### Read Paths



| Order | Path                              | Disk Format |
|-------|-----------------------------------|-------------|
| 1     | /ifd/xmp/exif:GPSProcessingMethod | unicode     |
| 2     | /ifd/gps/{ushort=27}              |             |



 

### Write Paths



| Order | Path                              | Disk Format |
|-------|-----------------------------------|-------------|
| 1     | /ifd/xmp/exif:GPSProcessingMethod | unicode     |
| 2     | /ifd/gps/{ushort=27}              |             |



 

### Remove Paths



| Order | Path                              |
|-------|-----------------------------------|
| 1     | /ifd/xmp/exif:gpsprocessingmethod |
| 2     | /ifd/gps/{ushort=27}              |



 

## Remarks

## Related topics

<dl> <dt>

[System.GPS.ProcessingMethod](../properties/props-system-gps-processingmethod.md)
</dt> </dl>

 

 
