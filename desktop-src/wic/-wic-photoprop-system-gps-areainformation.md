---
Description: The photo metadata policy for the System.GPS.AreaInformation property.
ms.assetid: d9ecb00b-1f97-4f53-909f-30231104d398
title: System.GPS.AreaInformation Photo Metadata Policy
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.GPS.AreaInformation Photo Metadata Policy

The photo metadata policy for the [System.GPS.AreaInformation](http://msdn.microsoft.com/en-us/library/bb787480(VS.85).aspx) property.

### PKEY

PKEY\_GPS\_AreaInformation

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



| Order | Path                         | Disk Format |
|-------|------------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=28}    |             |
| 2     | /xmp/exif:GPSAreaInformation | unicode     |



 

### Write Paths



| Order | Path                         | Disk Format |
|-------|------------------------------|-------------|
| 1     | /app1/ifd/gps/{ushort=28}    |             |
| 2     | /xmp/exif:GPSAreaInformation | unicode     |



 

### Remove Paths



| Order | Path                         |
|-------|------------------------------|
| 1     | /app1/ifd/gps/{ushort=28}    |
| 2     | /xmp/exif:GPSAreaInformation |



 

### TIFF Policies

### Read Paths



| Order | Path                             | Disk Format |
|-------|----------------------------------|-------------|
| 1     | /ifd/gps/{ushort=28}             |             |
| 2     | /ifd/xmp/exif:GPSAreaInformation | unicode     |



 

### Write Paths



| Order | Path                             | Disk Format |
|-------|----------------------------------|-------------|
| 1     | /ifd/gps/{ushort=28}             |             |
| 2     | /ifd/xmp/exif:GPSAreaInformation | unicode     |



 

### Remove Paths



| Order | Path                             |
|-------|----------------------------------|
| 1     | /ifd/gps/{ushort=28}             |
| 2     | /ifd/xmp/exif:GPSAreaInformation |



 

## Remarks

## Related topics

<dl> <dt>

[System.GPS.AreaInformation](http://msdn.microsoft.com/en-us/library/bb787480(VS.85).aspx)
</dt> </dl>

 

 



