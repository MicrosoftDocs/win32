---
description: The photo metadata policy for the System.Image.Compression property.
ms.assetid: 0fada41f-f6f8-43b3-ad65-79785e859c9c
title: System.Image.Compression Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Image.Compression Photo Metadata Policy

The photo metadata policy for the [System.Image.Compression](../properties/props-system-image-compression.md) property.

### PKEY

PKEY\_Image\_Compression

### Containers

JPEG, TIFF

### Read-Only

Yes

### Output PROPVARIANT Type

VT\_UI2

### Input Type

UShort

### Conflict Resolution Policy

Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                   | Disk Format |
|-------|------------------------|-------------|
| 1     | /app1/ifd/{ushort=259} | ushort      |
| 2     | /xmp/tiff:Compression  | unicode     |



 

### Write Paths



| Order | Path                   | Disk Format |
|-------|------------------------|-------------|
| 1     | /app1/ifd/{ushort=259} | ushort      |
| 2     | /xmp/tiff:Compression  | unicode     |



 

### Remove Paths



| Order | Path                   |
|-------|------------------------|
| 1     | /app1/ifd/{ushort=259} |
| 2     | /xmp/tiff:compression  |



 

### TIFF Policies

### Read Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /ifd/{ushort=259}         | ushort      |
| 2     | /ifd/xmp/tiff:Compression | unicode     |



 

### Write Paths



| Order | Path                      | Disk Format |
|-------|---------------------------|-------------|
| 1     | /ifd/{ushort=259}         | ushort      |
| 2     | /ifd/xmp/tiff:Compression | unicode     |



 

### Remove Paths



| Order | Path                      |
|-------|---------------------------|
| 1     | /ifd/{ushort=259}         |
| 2     | /ifd/xmp/tiff:compression |



 

## Remarks

## Related topics

<dl> <dt>

[System.Image.Compression](../properties/props-system-image-compression.md)
</dt> </dl>

 

 
