---
title: Disc Formats
description: IMAPI supports three file system formats ISO 9660, Joliet, and UDF.
ms.assetid: 9cd782c0-203b-452c-9d04-3464d39453b1
ms.topic: article
ms.date: 05/31/2018
---

# Disc Formats

IMAPI supports three file system formats: [ISO 9660](#iso-9660), [Joliet](#joliet), and [UDF](#universal-disk-format-udf).

## ISO 9660

The ISO 9660 format is the original standard file system for CD data discs. The format is recognized on several operating systems, including MSDOS, the Mac OS, UNIX, and the Windows operating system. The ISO 9660 format is published by the International Organization for Standardization (ISO).

The format begins at sector 16 with the volume header, CD0001; the remainder of the header follows. Other derived formats also begin at sector 16, but use another string for the volume header. For example, High Sierra discs use the string CD-ROM0001 and Compact Disc Interactive format uses CD-I0001.

The header points to areas of the disc that store the file names in ISO 9660 format. The file and directory naming convention consists of 8 characters, a period, and 3 more characters. This is the same naming convention used by the MSDOS operating system.

Additional file system headers, for formats such as Joliet and UDF, can co-exist on a disc without affecting the readability of the ISO 9660 format. After the indexes, a set of data files occupy the disc. The indexes for each file system independently reference data files on the disc.

The ISO 9660 specification defines three levels of the format:

-   Level 1 defines file names to use the 8.3 character format.
-   Level 2 permits longer file names, as found on DOS 6.xx, MacIntosh, and UNIX platforms.
-   Level 3 allows interleaved data and audio files to improve retrieval (playback) performance. This level also removes the 2GB file limit. This level is **not** supported by the Image Mastering API.

DVD discs can also use ISO 9660; however, the UDF file system is the most prevalent file system used with DVD media.

## Joliet

The Joliet format is a derivative of ISO 9660. This format writes the Joliet file system index to the disc image in addition to the ISO 9660 file system index.

The Joliet index provides the following improvements to the file system index:

-   Recognizes long file names up to 32 characters.
-   Distinguishes between upper and lower case letters in the file names.
-   Supports Unicode characters in the filename.

The Joliet format header begins at sector 17 of the disc.

Because the Joliet format preserves the ISO 9660 file system on a disc, compatibility with ISO 9660-compliant devices is retained.

## Universal Disk Format (UDF)

The Universal Disk Format (UDF) is a newer file system developed for optical media by the Optical Storage Technology Association (OSTA). UDF is a portable format that is recognized by several operating systems. UDF is replacing ISO 9660 as the new standard, especially with read/write media.

Features of UDF include the following:

-   Supports media up to 2TB in size.
-   Supports flash media, Iomega REV discs, and CD-MRW discs.
-   Stores files less than 2 KB in length in the File Entry block.
-   Supports files up to 2TB with filenames as long as 255 characters.
-   Supports a rich set of file attributes that suit various operating systems.
-   Supports a bridge format where ISO 9660, Joliet, and UDF formats all reside on the same disc. This is used in video applications, such as DVD-Video, DVD+VR, and DVD-VR.
-   Supports named streams and 'Real-Time' files.

 

 




