---
Description: 'A media pool is a logical collection of media that share some common attributes.'
ms.assetid: '1eefa52b-f490-487b-b010-263fa96d762a'
title: Media Pools
---

# Media Pools

\[[Removable Storage Manager](removable-storage-manager.md) is no longer available as of Windows 7 and Windows Server 2008 R2.\]

A *media pool* is a logical collection of media that share some common attributes. A media pool contains media of only one type, but media in the media pool can be in more than one library. Each cartridge is in a media pool. There are two classes of media pools: system and application. System media pools are created by Removable Storage Manager for its own use and include the free, import and unrecognized pools. Application media pools are created by applications to group media. Grouping media is especially important if several applications are sharing the libraries attached to a system and the media they contain.

Each media pool has access permissions that control access to the media that belong to it. While these permissions do not control access to the data contained on the media, they do control the manipulation of the media, including an application's ability to move media from the pool or to allocate it for its own use.

Media pools can be used hierarchically. A media pool can be used to hold other media pools, or it can be used to hold media. An application that needs to group media of several types into one collection can create an application media pool for the whole collection and additional media pools within it, one for each media type. Removable Storage Manager actually uses this technique for its system pools. Within the free pool, for example, is a media pool for each media type. Both sides of a two-sided cartridge are always in the same pool.

## System Pools

*System pools* are used to hold media that are not currently being used by an application. The free pool holds unused media that are available to applications, and the unrecognized and import pools are temporary holding places for media that have been newly placed in a library. For more information on how Removable Storage Manager uses these pools, especially the unrecognized and import pools, see [RSM Media Identification and Naming](rsm-media-identification-and-naming.md).

## Free Pools

*Free pools* support sharing media among applications. They contain media that are freely available to any application, and they hold no useful data. An application can draw media from the free pools when it needs additional media, and it can return media to the free pools when the media are no longer needed and should be made available to other applications.

## Unrecognized Pools

Media in the unrecognized pools might have data on them, but they are not cataloged by Removable Storage Manager nor is Removable Storage Manager able to read any data on these media. When a cartridge is placed in a library, Removable Storage Manager tries to identify it. If it has not seen this particular media before nor discerned its format or the application which last wrote data on it, Removable Storage Manager places the cartridge in the unrecognized pool for its media type. Blank media are treated this way.

## Import Pools

If Removable Storage Manager can identify the format or application associated with a cartridge that has just been placed in a library but has never been seen before, it places the cartridge in the import pool. For example, if an administrator placed a tape written by Backup on one system into a library attached to a second system, the instance of Removable Storage Manager on the second system recognizes that the tape was written using Microsoft Tape Format (MTF) and places it in the proper media type import pool.

## Application Pools

Each application that uses media managed by Removable Storage Manager uses one or more application pools. Applications can create these pools, or they can be created using the Removable Storage Manager snap-in. Permissions on application pools can be set up to allow applications to share pools, or to assign each application its own set of pools.

As mentioned earlier, a pool can either be created to hold other pools or it can be created to hold media. A pool created to hold media has additional properties that specify the actions to be taken when an application allocates or deallocates media.

The example discussed in the section [Designing an RSM Application](designing-an-rsm-application.md) shows one way in which media pools might be configured to support the needs of several client applications. The example system contains two libraries—one optical disk library and one tape library—and two data mover applications—a backup application and a document management application.

 

 



