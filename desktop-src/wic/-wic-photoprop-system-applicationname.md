---
description: The photo metadata policy for the System.ApplicationName property.
ms.assetid: bf4b310a-7e63-45c5-a327-2638fb31d676
title: System.ApplicationName Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.ApplicationName Photo Metadata Policy

The photo metadata policy for the [System.ApplicationName](../properties/props-system-applicationname.md) property.

### PKEY

PKEY\_ApplicationName

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

### JPEG Policy

### Read Paths



| Order | Path                                         | Disk Format |
|-------|----------------------------------------------|-------------|
|       | /app1/ifd/{ushort=305}                       | ascii       |
|       | /app13/irb/8bimiptc/iptc/Originating Program |             |
|       | /xmp/xmp:CreatorTool                         | unicode     |
|       | /xmp/xmp:creatortool                         | unicode     |
|       | /xmp/tiff:Software                           | unicode     |
|       | /xmp/tiff:software                           | unicode     |
|       | /app13/irb/8bimiptc/iptc/Originating Program |             |



 

### Write Paths



| Order | Path                                         | Disk Format |
|-------|----------------------------------------------|-------------|
|       | /app1/ifd/{ushort=305}                       | ascii       |
|       | /xmp/xmp:CreatorTool                         | unicode     |
|       | /xmp/xmp:creatortool                         | unicode     |
|       | /xmp/tiff:Software                           | unicode     |
|       | /xmp/tiff:software                           | unicode     |
|       | /app13/irb/8bimiptc/iptc/Originating Program |             |



 

### Remove Paths



| Order | Path                                         |
|-------|----------------------------------------------|
|       | /app1/ifd/{ushort=305}                       |
|       | /xmp/xmp:CreatorTool                         |
|       | /xmp/xmp:creatortool                         |
|       | /xmp/tiff:Software                           |
|       | /xmp/tiff:software                           |
|       | /app13/irb/8bimiptc/iptc/Originating Program |



 

### TIFF Policy

### Read Paths



| Order | Path                                       | Disk Format |
|-------|--------------------------------------------|-------------|
|       | /ifd/{ushort=305}                          | ascii       |
|       | /ifd/iptc/Originating Program              |             |
|       | /ifd/xmp/xmp:CreatorTool                   | unicode     |
|       | /ifd/xmp/xmp:creatortool                   | unicode     |
|       | /ifd/xmp/tiff:Software                     | unicode     |
|       | /ifd/xmp/tiff:software                     | unicode     |
|       | /ifd/iptc/Originating Program              |             |
|       | /ifd/irb/8bimiptc/iptc/Originating Program |             |



 

### Write Paths



| Order | Path                                       | Disk Format |
|-------|--------------------------------------------|-------------|
|       | /ifd/{ushort=305}                          | ascii       |
|       | /ifd/xmp/xmp:CreatorTool                   | unicode     |
|       | /ifd/xmp/xmp:creatortool                   | unicode     |
|       | /ifd/xmp/tiff:Software                     | unicode     |
|       | /ifd/xmp/tiff:software                     | unicode     |
|       | /ifd/iptc/Originating Program              |             |
|       | /ifd/irb/8bimiptc/iptc/Originating Program |             |



 

### Remove Paths



| Order | Path                                       |
|-------|--------------------------------------------|
|       | /ifd/{ushort=305}                          |
|       | /ifd/xmp/xmp:CreatorTool                   |
|       | /ifd/xmp/xmp:creatortool                   |
|       | /ifd/xmp/tiff:Software                     |
|       | /ifd/xmp/tiff:software                     |
|       | /ifd/iptc/Originating Program              |
|       | /ifd/irb/8bimiptc/iptc/Originating Program |



 

## Remarks

## Related topics

<dl> <dt>

[System.ApplicationName](../properties/props-system-applicationname.md)
</dt> </dl>

 

 
