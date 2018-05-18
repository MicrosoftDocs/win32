---
Description: 'On-media identifiers (OMIDs) are electronically recorded labels on each medium side in a Removable Storage Manager system.'
ms.assetid: '751f0b93-33f2-4106-b99b-ea60f632b91b'
title: 'On-media Identifiers'
---

# On-media Identifiers

\[[Removable Storage Manager](removable-storage-manager.md) is no longer available as of Windows 7 and Windows Server 2008 R2.\]

*On-media identifiers* (OMIDs) are electronically recorded labels on each medium side in a Removable Storage Manager system. Each label is composed of at least two parts: a type and an ID. A label type identifies the format used to record information on the medium. A label ID is an identifier that uniquely identifies each medium.

Different media types have different types of labels. Media sides with file systems (optical disk and Jaz cartridges, for example) have file system labels. An NTFS-formatted Jaz cartridge, for example, has an NTFS label type, and the ID is the volume serial number. Tapes using MTF have a label type of MTF and the ID is derived from various fields in the MTF header.

On-media identifiers are handled somewhat differently for CD-ROM and DVD-ROM media. Serial numbers for instances of these media might not be unique — a library can hold multiple copies of the same CD-ROM title, for example, with each having the same serial number — so Removable Storage Manager allows non-unique label IDs in this case. This does not degrade the media identification objectives of Removable Storage; any of the CD-ROMs with identical IDs can be used interchangeably since their contents are identical and cannot be changed.

 

 



