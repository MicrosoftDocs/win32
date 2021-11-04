---
description: The photo metadata policy for the System.Title property.
ms.assetid: 84da345e-ec03-48fe-8fda-043b706e4e1c
title: System.Title Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Title Photo Metadata Policy

The photo metadata policy for the [System.Title](../properties/props-system-title.md) property.

### PKEY

PKEY\_Title

### Containers

JPEG, TIFF

### Read-Only

No

### Output PROPVARIANT Type

VT\_LPWSTR

### Input PROPVARIANT Type

Either VT\_LPWSTR or VT\_LPSTR

### Conflict Resolution Policy

Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                                | Disk Format    |
|-------|-------------------------------------|----------------|
| 1     | /app1/ifd/{ushort=40091}            | unicode\_bytes |
| 2     | /xmp/&lt;xmpalt&gt;dc:title         | unicode        |
| 3     | /xmp/dc:title                       | unicode        |
| 4     | /app1/ifd/exif/{ushort=37510}       | unicode        |
| 5     | /app1/ifd/{ushort=270}              | ascii          |
| 6     | /app13/irb/8bimiptc/iptc/caption    |                |
| 7     | /xmp/&lt;xmpalt&gt;dc:description   | unicode        |
| 8     | /xmp/dc:description                 | unicode        |
| 9     | /app13/irb/8bimiptc/iptc/caption    |                |
| 10    | /xmp/&lt;xmpalt&gt;exif:UserComment | unicode        |



 

### Write Paths



| Order | Path                                | Disk Format    |
|-------|-------------------------------------|----------------|
| 1     | /app1/ifd/{ushort=40091}            | unicode\_bytes |
| 2     | /xmp/dc:title                       | unicode        |
| 3     | /xmp/&lt;xmpalt&gt;dc:title         | unicode        |
| 4     | /app1/ifd/exif/{ushort=37510}       | unicode        |
| 5     | /xmp/&lt;xmpalt&gt;exif:UserComment | unicode        |
| 6     | /app1/ifd/{ushort=270}              | ascii          |
| 7     | /app13/irb/8bimiptc/iptc/caption    |                |
| 8     | /xmp/dc:description                 | unicode        |
| 9     | /xmp/&lt;xmpalt&gt;dc:description   | unicode        |



 

### Remove Paths



| Order | Path                                |
|-------|-------------------------------------|
| 1     | /app1/ifd/{ushort=40091}            |
| 2     | /xmp/dc:title                       |
| 3     | /app1/ifd/exif/{ushort=37510}       |
| 4     | /xmp/&lt;xmpalt&gt;exif:UserComment |
| 5     | /app1/ifd/{ushort=270}              |
| 6     | /app13/irb/8bimiptc/iptc/caption    |
| 7     | /xmp/dc:description                 |



 

### TIFF Policy

### Read Paths



| Order | Path                                    | Disk Format    |
|-------|-----------------------------------------|----------------|
| 1     | /ifd/{ushort=40091}                     | unicode\_bytes |
| 2     | /ifd/xmp/&lt;xmpalt&gt;dc:title         | unicode        |
| 3     | /ifd/xmp/dc:title                       | unicode        |
| 4     | /ifd/exif/{ushort=37510}                | unicode        |
| 5     | /ifd/{ushort=270}                       | ascii          |
| 6     | /ifd/iptc/caption                       |                |
| 7     | /ifd/xmp/&lt;xmpalt&gt;dc:description   | unicode        |
| 8     | /ifd/xmp/dc:description                 | unicode        |
| 9     | /ifd/iptc/caption                       |                |
| 10    | /ifd/irb/8bimiptc/iptc/caption          |                |
| 11    | /ifd/xmp/&lt;xmpalt&gt;exif:UserComment | unicode        |



 

### Write Paths



| Order | Path                                    | Disk Format    |
|-------|-----------------------------------------|----------------|
| 1     | /ifd/{ushort=40091}                     | unicode\_bytes |
| 2     | /ifd/xmp/dc:title                       | unicode        |
| 3     | /ifd/xmp/&lt;xmpalt&gt;dc:title         | unicode        |
| 4     | /ifd/exif/{ushort=37510}                | unicode        |
| 5     | /ifd/xmp/&lt;xmpalt&gt;exif:UserComment | unicode        |
| 6     | /ifd/{ushort=270}                       | ascii          |
| 7     | /ifd/iptc/caption                       |                |
| 8     | /ifd/irb/8bimiptc/iptc/caption          |                |
| 9     | /ifd/xmp/dc:description                 | unicode        |
| 10    | /ifd/xmp/&lt;xmpalt&gt;dc:description   | unicode        |



 

### Remove Paths



| Order | Path                                    |
|-------|-----------------------------------------|
| 1     | /ifd/{ushort=40091}                     |
| 2     | /ifd/xmp/dc:title                       |
| 3     | /ifd/exif/{ushort=37510}                |
| 4     | /ifd/xmp/&lt;xmpalt&gt;exif:UserComment |
| 5     | /ifd/{ushort=270}                       |
| 6     | /ifd/iptc/caption                       |
| 7     | /ifd/irb/8bimiptc/iptc/caption          |
| 8     | /ifd/xmp/dc:description                 |



 

## Remarks

## Related topics

<dl> <dt>

[System.Title](../properties/props-system-title.md)
</dt> </dl>

 

 
