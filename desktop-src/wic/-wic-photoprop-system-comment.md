---
description: The photo metadata policy for the System.Comment property.
ms.assetid: 02a6ac18-ad69-4880-a267-8330d648c0d9
title: System.Comment Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Comment Photo Metadata Policy

The photo metadata policy for the [System.Comment](../properties/props-system-comment.md) property.

### PKEY

PKEY\_Comment

### Containers

JPEG, TIFF

### Read-Only

No

### Output PROPVARIANT Type

VT\_LPWSTR

### Input PROPVARIANT Type

VT\_LPWSTR or VT\_LPSTR

### Conflict Resolution Policy

Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                                | Disk Format    |
|-------|-------------------------------------|----------------|
| 1     | /app1/ifd/{ushort=40092}            | unicode\_bytes |
| 2     | /app1/ifd/{ushort=37510}            | unicode        |
| 3     | /xmp/<xmpalt>exif:UserComment | unicode        |



 

### Write Paths



| Order | Path                     | Disk Format    |
|-------|--------------------------|----------------|
| 1     | /app1/ifd/{ushort=40092} | unicode\_bytes |



 

### Remove Paths



| Order | Path                          |
|-------|-------------------------------|
| 1     | /app1/ifd/{ushort=40092}      |
| 2     | /app1/ifd/exif/{ushort=37510} |
| 3     | /xmp/exif:UserComment         |



 

### TIFF Policy

### Read Paths



| Order | Path                                    | Disk Format    |
|-------|-----------------------------------------|----------------|
| 1     | /ifd/{ushort=40092}                     | unicode\_bytes |
| 2     | /ifd/{ushort=37510}                     | unicode        |
| 3     | /ifd/xmp/<xmpalt>exif:UserComment | unicode        |



 

### Write Paths



| Order | Path                | Disk Format    |
|-------|---------------------|----------------|
| 1     | /ifd/{ushort=40092} | unicode\_bytes |



 

### Remove Paths



| Order | Path                      |
|-------|---------------------------|
| 1     | /ifd/{ushort=40092}       |
| 2     | /ifd/{ushort=37510}       |
| 3     | /ifd/xmp/exif:UserComment |



 

## Remarks

## Related topics

<dl> <dt>

[System.Comment](../properties/props-system-comment.md)
</dt> </dl>

 

 
