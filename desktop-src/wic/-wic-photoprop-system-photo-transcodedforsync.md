---
description: The photo metadata policy for the System.Photo.TranscodedForSync property.
ms.assetid: 1869d845-6264-425a-ab3e-e0a9f942961a
title: System.Photo.TranscodedForSync Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.TranscodedForSync Photo Metadata Policy

The photo metadata policy for the [System.Photo.TranscodedForSync](../properties/props-system-photo-transcodedforsync.md) property.

### PKEY

PKEY\_Photo\_TranscodedForSync

### Containers

JPEG, TIFF

### Read-Only

No

### Output PROPVARIANT Type

VT\_BOOL

### Input Type

Boolean.

### Conflict Resolution Policy

Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                                  | Disk Format  |
|-------|---------------------------------------|--------------|
| 1     | /app1/ifd/{ushort=18248}              | bool\_ushort |
| 2     | /xmp/MicrosoftPhoto:TranscodedForSync |              |



 

### Write Paths



| Order | Path                                  | Disk Format  |
|-------|---------------------------------------|--------------|
| 1     | /app1/ifd/{ushort=18248}              | bool\_ushort |
| 2     | /xmp/MicrosoftPhoto:TranscodedForSync |              |



 

### Remove Paths



| Order | Path                                  |
|-------|---------------------------------------|
| 1     | /app1/ifd/{ushort=18248}              |
| 2     | /xmp/microsoftphoto:transcodedforsync |



 

### TIFF Policies

### Read Paths



| Order | Path                                      | Disk Format  |
|-------|-------------------------------------------|--------------|
| 1     | /ifd/{ushort=18248}                       | bool\_ushort |
| 2     | /ifd/xmp/MicrosoftPhoto:TranscodedForSync |              |



 

### Write Paths



| Order | Path                                      | Disk Format  |
|-------|-------------------------------------------|--------------|
| 1     | /ifd/{ushort=18248}                       | bool\_ushort |
| 2     | /ifd/xmp/MicrosoftPhoto:TranscodedForSync |              |



 

### Remove Paths



| Order | Path                                      |
|-------|-------------------------------------------|
| 1     | /ifd/{ushort=18248}                       |
| 2     | /ifd/xmp/microsoftphoto:transcodedforsync |



 

## Remarks

## Related topics

<dl> <dt>

[System.Photo.TranscodedForSync](../properties/props-system-photo-transcodedforsync.md)
</dt> </dl>

 

 
