---
Description: 'The photo metadata policy for the System.Photo.CameraManufacturer property.'
ms.assetid: '6710161c-4835-4385-9d4c-566acc000925'
title: 'System.Photo.CameraManufacturer Photo Metadata Policy'
---

# System.Photo.CameraManufacturer Photo Metadata Policy

The photo metadata policy for the [System.Photo.CameraManufacturer](http://msdn.microsoft.com/en-us/library/bb760379(VS.85).aspx) property.

### PKEY

PKEY\_Photo\_CameraManufacturer

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

### JPEG Policy

### Read Paths



| Order | Path                   | Disk Format |
|-------|------------------------|-------------|
| 1     | /app1/ifd/{ushort=271} | ascii       |
| 2     | /xmp/tiff:Make         | unicode     |
| 3     | /xmp/tiff:make         | unicode     |



 

### Write Paths



| Order | Path                   | Disk Format |
|-------|------------------------|-------------|
| 1     | /app1/ifd/{ushort=271} | ascii       |
| 2     | /xmp/tiff:Make         | unicode     |
| 3     | /xmp/tiff:make         | unicode     |



 

### Remove Paths



| Order | Path                   |
|-------|------------------------|
| 1     | /app1/ifd/{ushort=271} |
| 2     | /xmp/tiff:Make         |
| 3     | /xmp/tiff:make         |



 

### TIFF Policy

### Read Paths



| Order | Path               | Disk Format |
|-------|--------------------|-------------|
| 1     | /ifd/{ushort=271}  | ascii       |
| 2     | /ifd/xmp/tiff:Make | unicode     |
| 3     | /ifd/xmp/tiff:make | unicode     |



 

### Write Paths



| Order | Path               | Disk Format |
|-------|--------------------|-------------|
| 1     | /ifd/{ushort=271}  | ascii       |
| 2     | /ifd/xmp/tiff:Make | unicode     |
| 3     | /ifd/xmp/tiff:make | unicode     |



 

### Remove Paths



| Order | Path               |
|-------|--------------------|
| 1     | /ifd/{ushort=271}  |
| 2     | /ifd/xmp/tiff:Make |
| 3     | /ifd/xmp/tiff:make |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.CameraManufacturer](http://msdn.microsoft.com/en-us/library/bb760379(VS.85).aspx)
</dt> </dl>

 

 



