---
Description: The photo metadata policy for the System.GPS.TrackRef property.
ms.assetid: e6912177-8add-4520-b396-c28060b359c7
title: System.GPS.TrackRef Photo Metadata Policy
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.GPS.TrackRef Photo Metadata Policy

The photo metadata policy for the [System.GPS.TrackRef](http://msdn.microsoft.com/en-us/library/bb760597(VS.85).aspx) property.

### PKEY

PKEY\_GPS\_TrackRef

### Containers

JPEG, TIFF

### Read-Only

No

### Output PROPVARIANT Type

VT\_LPWSTR

### Input Type

String

### Conflict Resolution Policy

Values from different schemas are reconciled.

### JPEG Policies

### Read Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=14} | ascii       |
| 2     | /xmp/exif:GPSTrackRef     | unicode     |



 

### Write Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=14} | ascii       |
| 2     | /xmp/exif:GPSTrackRef     | unicode     |



 

### Remove Paths



| Order | Path                      |
|-------|---------------------------|
| 1     | /app1/ifd/gps/{ushort=14} |
| 2     | /xmp/exif:gpstrackref     |



 

### TIFF Policies

### Read Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /ifd/gps/{ushort=14}      | ascii       |
| 2     | /ifd/xmp/exif:GPSTrackRef | unicode     |



 

### Write Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /ifd/gps/{ushort=14}      | ascii       |
| 2     | /ifd/xmp/exif:GPSTrackRef | unicode     |



 

### Remove Paths



| Order | Path                      |
|-------|---------------------------|
| 1     | /ifd/gps/{ushort=14}      |
| 2     | /ifd/xmp/exif:gpstrackref |



 

## Remarks

## Related topics

<dl> <dt>

[System.GPS.TrackRef](http://msdn.microsoft.com/en-us/library/bb760597(VS.85).aspx)
</dt> </dl>

 

 



