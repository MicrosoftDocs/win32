---
Description: Removable Storage Manager manages two classes of physical locations libraries and the offline library.
ms.assetid: 57616e99-f625-4e53-980c-e6e83e72412e
title: Libraries
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Libraries

\[[Removable Storage Manager](removable-storage-manager.md) is no longer available as of Windows 7 and Windows Server 2008 R2.\]

Removable Storage Manager manages two classes of physical locations: libraries and the offline library. *Libraries* include both data storage media and the means to read and write the media. The set of all physical locations includes the libraries and the offline library.

Libraries are composed of the following: slots, drives, transports, bar-code readers, doors, and insert/eject ports.

A CD-ROM drive with a disc inserted is a simple library with one drive, no slots, and no transport. A more complex example of a library is a robotic-based tape library, which holds several (up to several thousand) tapes, has one or more tape drives, and has a mechanical means to move tapes into and out of the drives.

Like a library, a *robotic library* is composed of slots, drives, transports, bar-code readers, doors, and insert/eject ports. At a minimum, a robotic library has some media, slots to hold the media, one or more drives, a transport, and either a door or an insert/eject port. Robotic libraries are sometimes referred to as changers or jukeboxes. No human intervention is required to place a cartridge in a library in one of its drives.

A *stand-alone drive library* or stand-alone drive is a special kind of library. A cartridge must be manually placed in a drive. The CD-ROM drive found on most desktop computers is a stand-alone drive library. Removable Storage Manager treats stand-alone drives as libraries with one drive and an insert/eject port. Removable Storage Manager models these drives as libraries to make its program interfaces simpler. For this reason, an application need not know whether a cartridge is mounted by a transport or a human.

## Slots

*Slots* are storage locations in the library. For example, a tape library has one slot for each tape that the library can hold. A stand-alone drive library has no slots. However, most libraries have at least four slots. Sometimes slots are organized into collections of slots called magazines. Magazines are usually removable.

## Drives

A *drive* is a device that can read or write to a cartridge. An Iomega Jaz drive, for example, can read and write to an inserted Jaz cartridge. A library has at least one drive.

## Transports

A *transport* is the robotic device that moves a cartridge from its slot to a drive and back again. Robotic libraries usually have only one transport.

## Bar Code Readers

A label with a bar code is attached to the outside of a cartridge that is both human readable and computer readable. Libraries that hold 0media with bar codes attached might have a bar code reader. There is only one reader, which is usually mounted on the transport.

## Doors

A *door* is a means to gain unconstrained access to the media in a library. On larger libraries a door might resemble an actual door. When the door is open, an administrator can add and remove media from the library. Doors on smaller libraries might not always look exactly like doors, but they still provide the same functionality. For example, some small changers have all their slots in a magazine. When an administrator instructs Removable Storage Manager to open the door, the changer pushes the magazine out through the front. The administrator can add, replace, or remove media and then reinsert the magazine into the changer. When an administrator adds media to a library, the media are placed directly into a slot. Some libraries have no doors, while others have several.

## Insert/Eject Ports

While doors provide unconstrained access to the media in a library, an insert/eject (IE) port provides very controlled access. When an administrator adds media to a library through an insert/eject port, the media are not placed directly into a slot. Instead, the media are placed in the insert/eject port and then the library uses the transport to move the media from the insert/eject port to a slot. Some libraries have no insert/eject ports, while others have several. Also called "mailslots," some insert/eject ports handle only one cartridge at a time, while others may handle several.

## Offline Library

The *offline library* is a special holder for media that is cataloged by Removable Storage, but does not reside in a library. Media that are not in any library, such as archived backup tapes on a shelf, are offline media and reside in the offline library. When a user or administrator moves an offline cartridge into a library, Removable Storage Manager changes its physical location to be the library into which it was placed. When a cartridge is taken out of a library, Removable Storage Manager notes that it now resides in the offline library.

 

 



