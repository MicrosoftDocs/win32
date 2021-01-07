---
description: The photo metadata policy for the System.Copyright property.
ms.assetid: 84d2f55b-5ca4-4912-b038-c18a72e6fc34
title: System.Copyright Photo Metadata Policy
ms.topic: article
ms.date: 05/31/2018
---

# System.Copyright Photo Metadata Policy

The photo metadata policy for the [System.Copyright](../properties/props-system-copyright.md) property.

### PKEY

PKEY\_Copyright

### Containers

JPEG, TIFF

### Read-Only

No

### Output PROPVARIANT Type

VT\_LPWSTR

### Input PROPVARIANT Type

String

### Conflict Resolution Policy

Values from different schemas are reconciled.

### JPEG Policy

### Read Paths



| Order | Path                                      | Disk Format |
|-------|-------------------------------------------|-------------|
|       | /app1/ifd/{ushort=33432}                  | ascii       |
|       | /app13/irb/8bimiptc/iptc/copyright notice |             |
|       | /xmp/<xmpalt>dc:rights              | unicode     |
|       | /xmp/dc:rights                            | unicode     |
|       | /app13/irb/8bimiptc/iptc/copyright notice |             |



 

### Write Paths



| Order | Path                                      | Disk Format |
|-------|-------------------------------------------|-------------|
|       | /xmp/dc:rights                            | unicode     |
|       | /xmp/<xmpalt>dc:rights              | unicode     |
|       | /app13/irb/8bimiptc/iptc/copyright notice |             |
|       | /app1/ifd/{ushort=33432}                  | ascii       |



 

### Remove Paths



| Order | Path                                      |
|-------|-------------------------------------------|
|       | /xmp/dc:rights                            |
|       | /app13/irb/8bimiptc/iptc/copyright notice |
|       | /app1/ifd/{ushort=33432}                  |



 

### TIFF Policy

### Read Paths



| Order | Path                                    | Disk Format |
|-------|-----------------------------------------|-------------|
|       | /ifd/{ushort=33432}                     | ascii       |
|       | /ifd/iptc/copyright notice              |             |
|       | /ifd/xmp/<xmpalt>dc:rights        | unicode     |
|       | /ifd/xmp/dc:rights                      | unicode     |
|       | /ifd/iptc/copyright notice              |             |
|       | /ifd/irb/8bimiptc/iptc/copyright notice |             |



 

### Write Paths



| Order | Path                                    | Disk Format |
|-------|-----------------------------------------|-------------|
|       | /ifd/xmp/dc:rights                      | unicode     |
|       | /ifd/xmp/<xmpalt>dc:rights        | unicode     |
|       | /ifd/iptc/copyright notice              |             |
|       | /ifd/irb/8bimiptc/iptc/copyright notice |             |
|       | /ifd/{ushort=33432}                     | ascii       |



 

### Remove Paths



| Order | Path                                    |
|-------|-----------------------------------------|
|       | /ifd/xmp/dc:rights                      |
|       | /ifd/iptc/copyright notice              |
|       | /ifd/irb/8bimiptc/iptc/copyright notice |
|       | /ifd/{ushort=33432}                     |



 

## Remarks

## Related topics

<dl> <dt>

[System.Copyright](../properties/props-system-copyright.md)
</dt> </dl>

 

 
