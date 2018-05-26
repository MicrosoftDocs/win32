---
Description: The photo metadata policy for the System.Photo.ShutterSpeed property.
ms.assetid: f320944c-978d-4a3c-9bf8-5c5652123e29
title: System.Photo.ShutterSpeed Photo Metadata Policy
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.Photo.ShutterSpeed Photo Metadata Policy

The photo metadata policy for the [System.Photo.ShutterSpeed](http://msdn.microsoft.com/en-us/library/bb787267(VS.85).aspx) property.

### PKEY

PKEY\_Photo\_ShutterSpeed

### Containers

JPEG, TIFF

### Read-Only

Yes

### Output PROPVARIANT Type

VT\_R8

### Conflict Resolution Policy

This value is generated from System.Photo.ShutterSpeedNumerator and System.Photo.ShutterSpeedDenominator. It cannot be written directly. Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=37377} |             |
| 2     | /xmp/exif:ShutterSpeedValue   |             |



 

### Write Paths



| Order | Path                          | Disk Format |
|-------|-------------------------------|-------------|
| 1     | /app1/ifd/exif/{ushort=37377} |             |
| 2     | /xmp/exif:ShutterSpeedValue   |             |



 

### Remove Paths



| Order | Path                          |
|-------|-------------------------------|
| 1     | /app1/ifd/exif/{ushort=37377} |
| 2     | /xmp/exif:shutterspeedvalue   |



 

### TIFF Policies

### Read Paths



| Order | Path                            | Disk Format |
|-------|---------------------------------|-------------|
| 1     | /ifd/exif/{ushort=37377}        |             |
| 2     | /ifd/xmp/exif:ShutterSpeedValue |             |



 

### Write Paths



| Order | Path                            | Disk Format |
|-------|---------------------------------|-------------|
| 1     | /ifd/exif/{ushort=37377}        |             |
| 2     | /ifd/xmp/exif:ShutterSpeedValue |             |



 

### Remove Paths



| Order | Path                            |
|-------|---------------------------------|
| 1     | /ifd/exif/{ushort=37377}        |
| 2     | /ifd/xmp/exif:shutterspeedvalue |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.ShutterSpeed](http://msdn.microsoft.com/en-us/library/bb787267(VS.85).aspx)
</dt> </dl>

 

 



