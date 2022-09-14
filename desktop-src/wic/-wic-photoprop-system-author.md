---
description: The photo metadata policy for the System.Author property.
ms.assetid: 2de9c452-93be-40a4-a72b-5da590534dfd
title: System.Author Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Author Photo Metadata Policy

The photo metadata policy for the [System.Author](../properties/props-system-author.md) property.

### PKEY

PKEY\_Author

### Containers

JPEG, TIFF

### Read-Only

No

### Output PROPVARIANT Type

VT\_VECTOR \| VT\_LPWSTR

### Input PROPVARIANT Type

VT\_VECTOR \| VT\_LPWSTR is preferred, but VT\_LPWSTR is also accepted.

### Conflict Resolution Policy

Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                             | Disk Format    |
|-------|----------------------------------|----------------|
| 1     | /app1/ifd/{ushort=315}           | ascii          |
| 2     | /app13/irb/8bimiptc/iptc/by-line |                |
| 3     | /xmp/&lt;xmpseq&gt;dc:creator    | unicode        |
| 4     | /app13/irb/8bimiptc/iptc/by-line |                |
| 5     | /app1/ifd/{ushort=40093}         | unicode\_bytes |
| 6     | /xmp/tiff:artist                 | unicode        |



 

### Write Paths



| Order | Path                             | Disk Format    |
|-------|----------------------------------|----------------|
| 1     | /xmp/&lt;xmpseq&gt;dc:creator    | unicode        |
| 2     | /xmp/tiff:artist                 | unicode        |
| 3     | /app13/irb/8bimiptc/iptc/by-line |                |
| 4     | /app1/ifd/{ushort=315}           | ascii          |
| 5     | /app1/ifd/{ushort=40093}         | unicode\_bytes |



 

### Remove Paths



| Order | Path                             |
|-------|----------------------------------|
| 1     | /xmp/dc:creator                  |
| 2     | /xmp/tiff:artist                 |
| 3     | /app13/irb/8bimiptc/iptc/by-line |
| 4     | /app1/ifd/{ushort=315}           |
| 5     | /app1/ifd/{ushort=40093}         |



 

### TIFF Policy

### Read Paths



| Order | Path                              | Disk Format    |
|-------|-----------------------------------|----------------|
| 1     | /ifd/{ushort=315}                 | ascii          |
| 2     | /ifd/iptc/by-line                 |                |
| 3     | /ifd/xmp/&lt;xmpseq&gt;dc:creator | unicode        |
| 4     | /ifd/iptc/by-line                 |                |
| 5     | /ifd/{ushort=40093}               | unicode\_bytes |
| 6     | /ifd/irb/8bimiptc/iptc/by-line    |                |
| 7     | /ifd/xmp/tiff:artist              | unicode        |



 

### Write Paths



| Order | Path                              | Disk Format    |
|-------|-----------------------------------|----------------|
| 1     | /ifd/xmp/&lt;xmpseq&gt;dc:creator | unicode        |
| 2     | /ifd/xmp/tiff:artist              | unicode        |
| 3     | /ifd/iptc/by-line                 |                |
| 4     | /ifd/{ushort=315}                 | ascii\_vector  |
| 5     | /ifd/{ushort=40093}               | unicode\_bytes |
| 6     | /ifd/iptc/by-line                 |                |



 

### Remove Paths



| Order | Path                           |
|-------|--------------------------------|
| 1     | /ifd/xmp/dc:creator            |
| 2     | /ifd/xmp/tiff:artist           |
| 3     | /ifd/iptc/by-line              |
| 4     | /ifd/irb/8bimiptc/iptc/by-line |
| 5     | /ifd/{ushort=315}              |
| 6     | /ifd/{ushort=40093}            |



 

### Remarks

## Related topics

<dl> <dt>

[System.Author](../properties/props-system-author.md)
</dt> </dl>

 

 
