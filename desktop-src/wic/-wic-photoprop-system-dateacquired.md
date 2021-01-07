---
description: The photo metadata policy for the System.DateAcquired property.
ms.assetid: 04a61ecc-d168-4f93-b143-3e6ba8aaf322
title: System.DateAcquired Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.DateAcquired Photo Metadata Policy

The photo metadata policy for the [System.DateAcquired](../properties/props-system-dateacquired.md) property.

### PKEY

PKEY\_DateAcquired

### Containers

JPEG, TIFF

### Read-Only

No

### Output PROPVARIANT Type

VT\_FILETIME

### Input PROPVARIANT Type

VT\_FILETIME

### Conflict Resolution Policy

Values from different schemas are reconciled.

### Precedence of Paths (JPEG)

If the file is in JPEG format, the handler searches for the data in the following order:



| Order | Path                             | Disk Format                        | Required |
|-------|----------------------------------|------------------------------------|----------|
| 1     | /xmp/MicrosoftPhoto:DateAcquired | Unicode string in XMP date format. | Yes      |



 

### Precedence of Paths (TIFF)

If the file is in TIFF format, the handler searches for the data in the following order:



| Order | Path                                 | Disk Format                        | Required |
|-------|--------------------------------------|------------------------------------|----------|
| 1     | /ifd/xmp/MicrosoftPhoto:DateAcquired | Unicode string in XMP date format. | Yes      |



 

## Remarks

## Related topics

<dl> <dt>

[System.DateAcquired](../properties/props-system-dateacquired.md)
</dt> </dl>

 

 
