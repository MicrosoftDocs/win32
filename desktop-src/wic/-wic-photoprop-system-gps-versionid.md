---
Description: The photo metadata policy for the System.GPS.VersionID property.
ms.assetid: d3c88243-8744-4bb3-ab47-38b5354f6f7e
title: System.GPS.VersionID Photo Metadata Policy
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.GPS.VersionID Photo Metadata Policy

The photo metadata policy for the [System.GPS.VersionID](http://msdn.microsoft.com/en-us/library/bb760599(VS.85).aspx) property.

### PKEY

PKEY\_GPS\_VersionID

### Containers

JPEG, TIFF

### Read-Only

No

### Output PROPVARIANT Type

VT\_VECTOR \| VT\_UI

### Input Type

Buffer

### Conflict Resolution Policy

Values from different schemas are reconciled.

### JPEG Policies

### Read Paths



| Order | Path                     | Disk Format |
|-------|--------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=0} |             |
| 2     | /xmp/exif:GPSVersionID   | unicode     |



 

### Write Paths



| Order | Path                     | Disk Format |
|-------|--------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=0} |             |
| 2     | /xmp/exif:GPSVersionID   | unicode     |



 

### Remove Paths



| Order | Path                     |
|-------|--------------------------|
| 1     | /app1/ifd/gps/{ushort=0} |
| 2     | /xmp/exif:gpsversionid   |



 

### TIFF Policies

### Read Paths



| Order | Path                       | Disk Format |
|-------|----------------------------|-------------|
| 1     | /ifd/gps/{ushort=0}        |             |
| 2     | /ifd/xmp/exif:GPSVersionID | unicode     |



 

### Write Paths



| Order | Path                       | Disk Format |
|-------|----------------------------|-------------|
| 1     | /ifd/gps/{ushort=0}        |             |
| 2     | /ifd/xmp/exif:GPSVersionID | unicode     |



 

### Remove Paths



| Order | Path                       |
|-------|----------------------------|
| 1     | /ifd/gps/{ushort=0}        |
| 2     | /ifd/xmp/exif:gpsversionid |



 

## Remarks

## Related topics

<dl> <dt>

[System.GPS.VersionID](http://msdn.microsoft.com/en-us/library/bb760599(VS.85).aspx)
</dt> </dl>

 

 



