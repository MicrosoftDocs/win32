Introduction
============

The exFAT file system is the successor to FAT32 in the FAT family of
file systems. This specification describes the exFAT file system and
provides all the information necessary for implementing the exFAT file
system.

Design Goals
------------

The exFAT file system has three central design goals (see list below).

1.  *Retain the simplicity of FAT-based file systems.*

> Two of the strengths of FAT-based file systems are their relative
> simplicity and ease of implementation. In the spirit of its
> predecessors, implementers should find exFAT relatively simple and
> easy to implement.

2.  *Enable very large files and storage devices.*

> The exFAT file system uses 64 bits to describe file size, thereby
> enabling applications which depend on very large files. The exFAT file
> system also allows for clusters as large as 32MB, effectively enabling
> very large storage devices.

3.  *Incorporate extensibility for future innovation.*

> The exFAT file system incorporates extensibility into its design,
> enabling the file system to keep pace with innovations in storage and
> changes in usage.

Specific Terminology
--------------------

In the context of this specification, certain terms (see Table 1) carry
specific meaning for the design and implementation of the exFAT file
system.

**Definition of Terms Which Carry Very Specific Meaning**

<table>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><strong>Definition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Shall</td>
<td>This specification uses the term “shall” to describe a behavior which is mandatory.</td>
</tr>
<tr class="even">
<td>Should</td>
<td>This specification uses the term “should” to describe a behavior which it strongly recommends, but does not make mandatory.</td>
</tr>
<tr class="odd">
<td>May</td>
<td>This specification uses the term “may” to describe a behavior which is optional.</td>
</tr>
<tr class="even">
<td>Mandatory</td>
<td>This term describes a field or structure which an implementation shall modify and shall interpret as this specification describes.</td>
</tr>
<tr class="odd">
<td>Optional</td>
<td>This term describes a field or structure which an implementation may or may not support. If an implementation supports a given optional field or structure, it shall modify and shall interpret the field or structure as this specification describes.</td>
</tr>
<tr class="even">
<td>Undefined</td>
<td>This term describes field or structure contents which an implementation may modify as necessary (i.e. clear to zero when setting surrounding fields or structures) and shall not interpret to hold any specific meaning.</td>
</tr>
<tr class="odd">
<td>Reserved</td>
<td><p>This term describes field or structure contents which implementations:</p>
<ol type="1">
<li><p>Shall initialize to zero and should not use for any purpose</p></li>
<li><p>Should not interpret, except when computing checksums</p></li>
<li><p>Shall preserve across operations which modify surrounding fields or structures</p></li>
</ol></td>
</tr>
</tbody>
</table>

Full Text of Common Acronyms
----------------------------

This specification uses acronyms in common use in the personal computer
industry (see Table 2).

**Full Text of Common Acronyms**

| **Acronym** | **Full Text**                                      |
|-------------|----------------------------------------------------|
| ASCII       | American Standard Code for Information Interchange |
| BIOS        | Basic Input Output System                          |
| CPU         | Central Processing Unit                            |
| exFAT       | extensible File Allocation Table                   |
| FAT         | File Allocation Table                              |
| FAT12       | File Allocation Table, 12-bit cluster indices      |
| FAT16       | File Allocation Table, 16-bit cluster indices      |
| FAT32       | File Allocation Table, 32-bit cluster indices      |
| GPT         | GUID Partition Table                               |
| GUID        | Globally Unique Identifier (see Section 10.1)      |
| INT         | Interrupt                                          |
| MBR         | Master Boot Record                                 |
| texFAT      | Transaction-safe exFAT                             |
| UTC         | Coordinated Universal Time                         |

Default Field and Structure Qualifiers
--------------------------------------

Fields and structures in this specification have the following
qualifiers (see list below), unless the specification notes otherwise.

1.  Are unsigned

2.  Use decimal notation to describe values, where not otherwise noted; this specification uses the post-fix letter "h" to denote  hexadecimal numbers and encloses GUIDs in curly braces

3.  Are in little-endian format

4.  Do not require a null-terminating character for strings

Windows CE and TexFAT
---------------------

TexFAT is an extension to exFAT that adds transaction-safe operational
semantics on top of the base file system. TexFAT is used by Windows CE.
TexFAT requires the use of the two FATs and allocation bitmaps for use
in transactions. It also defines several additional structures including
padding descriptors and security descriptors. See the **exFAT 1.00
Enhanced Specification** document for details.

Volume Structure
================

A volume is the set of all file system structures and data space
necessary to store and retrieve user data. All exFAT volumes contain
four regions (see Table 3).

**Volume Structure**

<table>
<thead>
<tr class="header">
<th><strong>Sub-region Name</strong></th>
<th><p><strong>Offset</strong></p>
<p><strong>(sector)</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>(sectors)</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Main Boot Region</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Main Boot Sector</td>
<td>0</td>
<td>1</td>
<td>This sub-region is mandatory and Section 3.1 defines its contents.</td>
</tr>
<tr class="odd">
<td>Main Extended Boot Sectors</td>
<td>1</td>
<td>8</td>
<td>This sub-region is mandatory and Section 3.2 defines its contents.</td>
</tr>
<tr class="even">
<td>Main OEM Parameters</td>
<td>9</td>
<td>1</td>
<td>This sub-region is mandatory and Section 3.3 defines its contents.</td>
</tr>
<tr class="odd">
<td>Main Reserved</td>
<td>10</td>
<td>1</td>
<td>This sub-region is mandatory and its contents are reserved.</td>
</tr>
<tr class="even">
<td>Main Boot Checksum</td>
<td>11</td>
<td>1</td>
<td>This sub-region is mandatory and Section 3.4 defines its contents.</td>
</tr>
<tr class="odd">
<td><strong>Backup Boot Region</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Backup Boot Sector</td>
<td>12</td>
<td>1</td>
<td>This sub-region is mandatory and Section 3.1 defines its contents.</td>
</tr>
<tr class="odd">
<td>Backup Extended Boot Sectors</td>
<td>13</td>
<td>8</td>
<td>This sub-region is mandatory and Section 3.2 defines its contents.</td>
</tr>
<tr class="even">
<td>Backup OEM Parameters</td>
<td>21</td>
<td>1</td>
<td>This sub-region is mandatory and Section 3.3 defines its contents.</td>
</tr>
<tr class="odd">
<td>Backup Reserved</td>
<td>22</td>
<td>1</td>
<td>This sub-region is mandatory and its contents are reserved.</td>
</tr>
<tr class="even">
<td>Backup Boot Checksum</td>
<td>23</td>
<td>1</td>
<td>This sub-region is mandatory and Section 3.4 defines its contents.</td>
</tr>
<tr class="odd">
<td><strong>FAT Region</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>FAT Alignment</td>
<td>24</td>
<td>FatOffset – 24</td>
<td><p>This sub-region is mandatory and its contents, if any, are undefined.</p>
<p>Note: the Main and Backup Boot Sectors both contain the FatOffset field.</p></td>
</tr>
<tr class="odd">
<td>First FAT</td>
<td>FatOffset</td>
<td>FatLength</td>
<td><p>This sub-region is mandatory and Section 4.1 defines its contents.</p>
<p>Note: the Main and Backup Boot Sectors both contain the FatOffset and FatLength fields.</p></td>
</tr>
<tr class="even">
<td>Second FAT</td>
<td>FatOffset + FatLength</td>
<td>FatLength * (NumberOfFats – 1)</td>
<td><p>This sub-region is mandatory and Section 4.1 defines its contents, if any.</p>
<p>Note: the Main and Backup Boot Sectors both contain the FatOffset, FatLength, and NumberOfFats fields. The NumberOfFats field may only hold values 1 and 2.</p></td>
</tr>
<tr class="odd">
<td><strong>Data Region</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Cluster Heap Alignment</td>
<td>FatOffset + FatLength * NumberOfFats</td>
<td>ClusterHeapOffset – (FatOffset + FatLength * NumberOfFats)</td>
<td><p>This sub-region is mandatory and its contents, if any, are undefined.</p>
<p>Note: the Main and Backup Boot Sectors both contain the FatOffset, FatLength, NumberOfFats, and ClusterHeapOffset fields. The NumberOfFats field’s valid values are 1 and 2.</p></td>
</tr>
<tr class="odd">
<td>Cluster Heap</td>
<td>ClusterHeapOffset</td>
<td>ClusterCount * 2<sup>SectorsPerClusterShift</sup></td>
<td><p>This sub-region is mandatory and Section 5.1 defines its contents.</p>
<p>Note: the Main and Backup Boot Sectors both contain the ClusterHeapOffset, ClusterCount, and SectorsPerClusterShift fields.</p></td>
</tr>
<tr class="even">
<td>Excess Space</td>
<td>ClusterHeapOffset + ClusterCount * 2<sup>SectorsPerClusterShift</sup></td>
<td>VolumeLength – (ClusterHeapOffset + ClusterCount * 2<sup>SectorsPerClusterShift</sup>)</td>
<td><p>This sub-region is mandatory and its contents, if any, are undefined.</p>
<p>Note: the Main and Backup Boot Sectors both contain the ClusterHeapOffset, ClusterCount, SectorsPerClusterShift, and VolumeLength fields.</p></td>
</tr>
</tbody>
</table>

 Main and Backup Boot Regions
============================

The Main Boot region provides all the necessary boot-strapping
instructions, identifying information, and file system parameters to
enable an implementation to perform the following:

1.  Boot-strap a computer system from an exFAT volume.

2.  Identify the file system on the volume as exFAT.

3.  Discover the location of the exFAT file system structures.

The Backup Boot region is a backup of the Main Boot region. It aids
recovery of the exFAT volume in the advent of the Main Boot region being
in an inconsistent state. Except under infrequent circumstances, such as
updating boot-strapping instructions, implementations should not modify
the contents of the Backup Boot region.

Main and Backup Boot Sector Sub-regions
---------------------------------------

The Main Boot Sector contains code for boot-strapping from an exFAT
volume and fundamental exFAT parameters which describe the volume
structure (see Table 4). BIOS, MBR, or other boot-strapping agents may
inspect this sector and may load and execute any boot-strapping
instructions contained therein.

The Backup Boot Sector is a backup of the Main Boot Sector and has the
same structure (see Table 4). The Backup Boot Sector may aid recovery
operations; however, implementations shall treat the contents of the
VolumeFlags and PercentInUse fields as stale.

Prior to using the contents of either the Main or Backup Boot Sector,
implementations shall verify their contents by validating their
respective Boot Checksum and ensuring all their fields are within their
valid value range.

While the initial format operation will initialize the contents of both
the Main and Backup Boot Sectors, implementations may update these
sectors (and shall also update their respective Boot Checksum) as
needed. However, implementations may update either the VolumeFlags or
PercentInUse fields without updating their respective Boot Checksum (the
checksum specifically excludes these two fields).

**Main and Backup Boot Sector Structure**

<table>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><p><strong>Offset</strong></p>
<p><strong>(byte)</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>(bytes)</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>JumpBoot</td>
<td>0</td>
<td>3</td>
<td>This field is mandatory and Section 3.1.1 defines its contents.</td>
</tr>
<tr class="even">
<td>FileSystemName</td>
<td>3</td>
<td>8</td>
<td>This field is mandatory and Section 3.1.2 defines its contents.</td>
</tr>
<tr class="odd">
<td>MustBeZero</td>
<td>11</td>
<td>53</td>
<td>This field is mandatory and Section 3.1.3 defines its contents.</td>
</tr>
<tr class="even">
<td>PartitionOffset</td>
<td>64</td>
<td>8</td>
<td>This field is mandatory and Section 3.1.4 defines its contents.</td>
</tr>
<tr class="odd">
<td>VolumeLength</td>
<td>72</td>
<td>8</td>
<td>This field is mandatory and Section 3.1.5 defines its contents.</td>
</tr>
<tr class="even">
<td>FatOffset</td>
<td>80</td>
<td>4</td>
<td>This field is mandatory and Section 3.1.6 defines its contents.</td>
</tr>
<tr class="odd">
<td>FatLength</td>
<td>84</td>
<td>4</td>
<td>This field is mandatory and Section 3.1.7 defines its contents.</td>
</tr>
<tr class="even">
<td>ClusterHeapOffset</td>
<td>88</td>
<td>4</td>
<td>This field is mandatory and Section 3.1.8 defines its contents.</td>
</tr>
<tr class="odd">
<td>ClusterCount</td>
<td>92</td>
<td>4</td>
<td>This field is mandatory and Section 3.1.9 defines its contents.</td>
</tr>
<tr class="even">
<td>FirstClusterOfRootDirectory</td>
<td>96</td>
<td>4</td>
<td>This field is mandatory and Section 3.1.10 defines its contents.</td>
</tr>
<tr class="odd">
<td>VolumeSerialNumber</td>
<td>100</td>
<td>4</td>
<td>This field is mandatory and Section 3.1.11 defines its contents.</td>
</tr>
<tr class="even">
<td>FileSystemRevision</td>
<td>104</td>
<td>2</td>
<td>This field is mandatory and Section 3.1.12 defines its contents.</td>
</tr>
<tr class="odd">
<td>VolumeFlags</td>
<td>106</td>
<td>2</td>
<td>This field is mandatory and Section 3.1.13 defines its contents.</td>
</tr>
<tr class="even">
<td>BytesPerSectorShift</td>
<td>108</td>
<td>1</td>
<td>This field is mandatory and Section 3.1.14 defines its contents.</td>
</tr>
<tr class="odd">
<td>SectorsPerClusterShift</td>
<td>109</td>
<td>1</td>
<td>This field is mandatory and Section 3.1.15 defines its contents.</td>
</tr>
<tr class="even">
<td>NumberOfFats</td>
<td>110</td>
<td>1</td>
<td>This field is mandatory and Section 3.1.16 defines its contents.</td>
</tr>
<tr class="odd">
<td>DriveSelect</td>
<td>111</td>
<td>1</td>
<td>This field is mandatory and Section 3.1.17 defines its contents.</td>
</tr>
<tr class="even">
<td>PercentInUse</td>
<td>112</td>
<td>1</td>
<td>This field is mandatory and Section 3.1.18 defines its contents.</td>
</tr>
<tr class="odd">
<td>Reserved</td>
<td>113</td>
<td>7</td>
<td>This field is mandatory and its contents are reserved.</td>
</tr>
<tr class="even">
<td>BootCode</td>
<td>120</td>
<td>390</td>
<td>This field is mandatory and Section 3.1.19 defines its contents.</td>
</tr>
<tr class="odd">
<td>BootSignature</td>
<td>510</td>
<td>2</td>
<td>This field is mandatory and Section 3.1.20 defines its contents.</td>
</tr>
<tr class="even">
<td>ExcessSpace</td>
<td>512</td>
<td>2<sup>BytesPerSectorShift</sup> – 512</td>
<td><p>This field is mandatory and its contents, if any, are undefined.</p>
<p>Note: the Main and Backup Boot Sectors both contain the BytesPerSectorShift field.</p></td>
</tr>
</tbody>
</table>

### JumpBoot Field

The JumpBoot field shall contain the jump instruction for CPUs common in
personal computers, which, when executed, "jumps" the CPU to execute the
boot-strapping instructions in the BootCode field.

The valid value for this field is (in order of low-order byte to
high-order byte) EBh 76h 90h.

### FileSystemName Field

The FileSystemName field shall contain the name of the file system on
the volume.

The valid value for this field is, in ASCII characters, "EXFAT ", which
includes three trailing white spaces.

### MustBeZero Field

The MustBeZero field shall directly correspond with the range of bytes
the packed BIOS parameter block consumes on FAT12/16/32 volumes.

The valid value for this field is 0, which helps to prevent FAT12/16/32
implementations from mistakenly mounting an exFAT volume.

### PartitionOffset Field

The PartitionOffset field shall describe the media-relative sector
offset of the partition which hosts the given exFAT volume. This field
aids boot-strapping from the volume using extended INT 13h on personal
computers.

All possible values for this field are valid; however, the value 0
indicates implementations shall ignore this field.

### VolumeLength Field

The VolumeLength field shall describe the size of the given exFAT volume
in sectors.

The valid range of values for this field shall be:

-   At least 2^20^ / 2^BytesPerSectorShift^, which ensures the smallest
    > volume is no less than 1MB

-   At most 2^64^ -- 1, the largest value this field can describe

However, if the size of the Excess Space sub-region is 0, then the value
of this field is ClusterHeapOffset + (2^32^ -- 11) \*
2^SectorsPerClusterShift^.

### FatOffset Field

The FatOffset field shall describe the volume-relative sector offset of
the First FAT. This field enables implementations to align the First FAT
to the characteristics of the underlying storage media.

The valid range of values for this field shall be:

-   At least 24, which accounts for the sectors the Main Boot and Backup
    > Boot regions consume

-   At most ClusterHeapOffset -- (FatLength \* NumberOfFats), which
    > accounts for the sectors the Cluster Heap consumes

### FatLength Field

The FatLength field shall describe the length, in sectors, of each FAT
table (the volume may contain up to two FATs).

The valid range of values for this field shall be:

-   At least (ClusterCount + 2) \* 2^2^ / 2^BytesPerSectorShift^ rounded
    > up to the nearest integer, which ensures each FAT has sufficient
    > space for describing all the clusters in the Cluster Heap

-   At most (ClusterHeapOffset -- FatOffset) / NumberOfFats rounded down
    > to the nearest integer, which ensures the FATs exist before the
    > Cluster Heap

This field may contain a value in excess of its lower bound (as
described above) to enable the Second FAT, if present, to also be
aligned to the characteristics of the underlying storage media. The
contents of the space which exceeds what the FAT itself requires, if
any, are undefined.

### ClusterHeapOffset Field

The ClusterHeapOffset field shall describe the volume-relative sector
offset of the Cluster Heap. This field enables implementations to align
the Cluster Heap to the characteristics of the underlying storage media.

The valid range of values for this field shall be:

-   At least FatOffset + FatLength \* NumberOfFats, to account for the
    > sectors all the preceding regions consume

-   At most 2^32^ -- 1 or VolumeLength -- (ClusterCount \*
    > 2^SectorsPerClusterShift^), whichever calculation is less

### ClusterCount Field

The ClusterCount field shall describe the number of clusters the Cluster
Heap contains.

The valid value for this field shall be the lesser of the following:

-   (VolumeLength -- ClusterHeapOffset) / 2^SectorsPerClusterShift^
    > rounded down to the nearest integer, which is exactly the number
    > of clusters which can fit between the beginning of the Cluster
    > Heap and the end of the volume

-   2^32^ -- 11, which is the maximum number of clusters a FAT can
    > describe

The value of the ClusterCount field determines the minimum size of a
FAT. To avoid extremely large FATs, implementations can control the
number of clusters in the Cluster Heap by increasing the cluster size
(via the SectorsPerClusterShift field). This specification recommends no
more than 2^24^ -- 2 clusters in the Cluster Heap. However,
implementations shall be able to handle volumes with up to 2^32^ -- 11
clusters in the Cluster Heap.

### FirstClusterOfRootDirectory Field

The FirstClusterOfRootDirectory field shall contain the cluster index of
the first cluster of the root directory. Implementations should make
every effort to place the first cluster of the root directory in the
first non-bad cluster after the clusters the Allocation Bitmap and
Up-case Table consume.

The valid range of values for this field shall be:

-   At least 2, the index of the first cluster in the Cluster Heap

-   At most ClusterCount + 1, the index of the last cluster in the
    > Cluster Heap

### VolumeSerialNumber Field

The VolumeSerialNumber field shall contain a unique serial number. This
assists implementations to distinguish among different exFAT volumes.
Implementations should generate the serial number by combining the date
and time of formatting the exFAT volume. The mechanism for combining
date and time to form a serial number is implementation-specific.

All possible values for this field are valid.

### FileSystemRevision Field

The FileSystemRevision field shall describe the major and minor revision
numbers of the exFAT structures on the given volume.

The high-order byte is the major revision number and the low-order byte
is the minor revision number. For example, if the high-order byte
contains the value 01h and if the low-order byte contains the value 05h,
then the FileSystemRevision field describes the revision number 1.05.
Likewise, if the high-order byte contains the value 0Ah and if the
low-order byte contains the value 0Fh, then the FileSystemRevision field
describes the revision number 10.15.

The valid range of values for this field shall be:

-   At least 0 for the low-order byte and 1 for the high-order byte

-   At most 99 for the low-order byte and 99 for the high-order byte

The revision number of exFAT this specification describes is 1.00.
Implementations of this specification should mount any exFAT volume with
major revision number 1 and shall not mount any exFAT volume with any
other major revision number. Implementations shall honor the minor
revision number and shall not perform operations or create any file
system structures not described in the given minor revision number's
corresponding specification.

### VolumeFlags Field

The VolumeFlags field shall contain flags which indicate the status of
various file system structures on the exFAT volume (see Table 5).

Implementations shall not include this field when computing its
respective Main Boot or Backup Boot region checksum. When referring to
the Backup Boot Sector, implementations shall treat this field as stale.

**VolumeFlags Field Structure**

<table>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><p><strong>Offset</strong></p>
<p><strong>(bit)</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>(bits)</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ActiveFat</td>
<td>0</td>
<td>1</td>
<td>This field is mandatory and Section 3.1.13.1 defines its contents.</td>
</tr>
<tr class="even">
<td>VolumeDirty</td>
<td>1</td>
<td>1</td>
<td>This field is mandatory and Section 3.1.13.2 defines its contents.</td>
</tr>
<tr class="odd">
<td>MediaFailure</td>
<td>2</td>
<td>1</td>
<td>This field is mandatory and Section 3.1.13.3 defines its contents.</td>
</tr>
<tr class="even">
<td>ClearToZero</td>
<td>3</td>
<td>1</td>
<td>This field is mandatory and Section 3.1.13.4 defines its contents.</td>
</tr>
<tr class="odd">
<td>Reserved</td>
<td>4</td>
<td>12</td>
<td>This field is mandatory and its contents are reserved.</td>
</tr>
</tbody>
</table>

#### ActiveFat Field

The ActiveFat field shall describe which FAT and Allocation Bitmap are
active (and implementations shall use), as follows:

-   0, which means the First FAT and First Allocation Bitmap are active

-   1, which means the Second FAT and Second Allocation Bitmap are
    > active and is possible only when the NumberOfFats field contains
    > the value 2

Implementations shall consider the inactive FAT and Allocation Bitmap as
stale. Only TexFAT-aware implementations shall switch the active FAT and
Allocation Bitmaps (see Section 7.1).

#### VolumeDirty Field

The VolumeDirty field shall describe whether the volume is dirty or not,
as follows:

-   0, which means the volume is probably in a consistent state

-   1, which means the volume is probably in an inconsistent state

Implementations should set the value of this field to 1 upon
encountering file system metadata inconsistencies which they do not
resolve. If, upon mounting a volume, the value of this field is 1, only
implementations which resolve file system metadata inconsistencies may
clear the value of this field to 0. Such implementations shall only
clear the value of this field to 0 after ensuring the file system is in
a consistent state.

If, upon mounting a volume, the value of this field is 0,
implementations should set this field to 1 before updating file system
metadata and clear this field to 0 afterwards, similar to the
recommended write ordering described in Section 8.1.

#### MediaFailure Field

The MediaFailure field shall describe whether an implementation has
discovered media failures or not, as follows:

-   0, which means the hosting media has not reported failures or any
    > known failures are already recorded in the FAT as "bad" clusters

-   1, which means the hosting media has reported failures (i.e. has
    > failed read or write operations)

An implementation should set this field to 1 when:

1.  The hosting media fails access attempts to any region in the volume

2.  The implementation has exhausted access retry algorithms, if any

If, upon mounting a volume, the value of this field is 1,
implementations which scan the entire volume for media failures and
record all failures as "bad" clusters in the FAT (or otherwise resolve
media failures) may clear the value of this field to 0.

#### ClearToZero Field

The ClearToZero field does not have significant meaning in this
specification.

The valid values for this field are:

-   0, which does not have any particular meaning

-   1, which means implementations shall clear this field to 0 prior to
    > modifying any file system structures, directories, or files

### BytesPerSectorShift Field

The BytesPerSectorShift field shall describe the bytes per sector
expressed as log~2~(N), where N is the number of bytes per sector. For
example, for 512 bytes per sector, the value of this field is 9.

The valid range of values for this field shall be:

-   At least 9 (sector size of 512 bytes), which is the smallest sector
    > possible for an exFAT volume

-   At most 12 (sector size of 4096 bytes), which is the memory page
    > size of CPUs common in personal computers

### SectorsPerClusterShift Field

The SectorsPerClusterShift field shall describe the sectors per cluster
expressed as log~2~(N), where N is number of sectors per cluster. For
example, for 8 sectors per cluster, the value of this field is 3.

The valid range of values for this field shall be:

-   At least 0 (1 sector per cluster), which is the smallest cluster
    > possible

-   At most 25 -- BytesPerSectorShift, which evaluates to a cluster size
    > of 32MB

### NumberOfFats Field

The NumberOfFats field shall describe the number of FATs and Allocation
Bitmaps the volume contains.

The valid range of values for this field shall be:

-   1, which indicates the volume only contains the First FAT and First
    > Allocation Bitmap

-   2, which indicates the volume contains the First FAT, Second FAT,
    > First Allocation Bitmap, and Second Allocation Bitmap; this value
    > is only valid for TexFAT volumes

### DriveSelect Field

The DriveSelect field shall contain the extended INT 13h drive number,
which aids boot-strapping from this volume using extended INT 13h on
personal computers.

All possible values for this field are valid. Similar fields in previous
FAT-based file systems frequently contained the value 80h.

### PercentInUse Field

The PercentInUse field shall describe the percentage of clusters in the
Cluster Heap which are allocated.

The valid range of values for this field shall be:

-   Between 0 and 100 inclusively, which is the percentage of allocated
    > clusters in the Cluster Heap, rounded down to the nearest integer

-   Exactly FFh, which indicates the percentage of allocated clusters in
    > the Cluster Heap is not available

Implementations shall change the value of this field to reflect changes
in the allocation of clusters in the Cluster Heap or shall change it to
FFh.

Implementations shall not include this field when computing its
respective Main Boot or Backup Boot region checksum. When referring to
the Backup Boot Sector, implementations shall treat this field as stale.

### BootCode Field

The BootCode field shall contain boot-strapping instructions.
Implementations may populate this field with the CPU instructions
necessary for boot-strapping a computer system. Implementations which
don't provide boot-strapping instructions shall initialize each byte in
this field to F4h (the halt instruction for CPUs common in personal
computers) as part of their format operation.

### BootSignature Field

The BootSignature field shall describe whether the intent of a given
sector is for it to be a Boot Sector or not.

The valid value for this field is AA55h. Any other value in this field
invalidates its respective Boot Sector. Implementations should verify
the contents of this field prior to depending on any other field in its
respective Boot Sector.

Main and Backup Extended Boot Sectors Sub-regions
-------------------------------------------------

Each sector of the Main Extended Boot Sectors has the same structure;
however, each sector may hold distinct boot-strapping instructions (see
Table 6). Boot-strapping agents, such as the boot-strapping instructions
in the Main Boot Sector, alternate BIOS implementations, or an embedded
system's firmware, may load these sectors and execute the instructions
they contain.

The Backup Extended Boot Sectors is a backup of the Main Extended Boot
Sectors and has the same structure (see Table 6).

Prior to executing the instructions of either the Main or Backup
Extended Boot Sectors, implementations should verify their contents by
ensuring each sector's ExtendedBootSignature field contains its
prescribed value.

While the initial format operation will initialize the contents of both
the Main and Backup Extended Boot Sectors, implementations may update
these sectors (and shall also update their respective Boot Checksum) as
needed.

**Extended Boot Sector Structure**

<table>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><p><strong>Offset</strong></p>
<p><strong>(byte)</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>(bytes)</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ExtendedBootCode</td>
<td>0</td>
<td>2<sup>BytesPerSectorShift</sup> – 4</td>
<td><p>This field is mandatory and Section 3.2.1 defines its contents.</p>
<p>Note: the Main and Backup Boot Sectors both contain the BytesPerSectorShift field.</p></td>
</tr>
<tr class="even">
<td>ExtendedBootSignature</td>
<td>2<sup>BytesPerSectorShift</sup> – 4</td>
<td>4</td>
<td><p>This field is mandatory and Section 3.2.2 defines its contents.</p>
<p>Note: the Main and Backup Boot Sectors both contain the BytesPerSectorShift field.</p></td>
</tr>
</tbody>
</table>

### ExtendedBootCode Field

The ExtendedBootCode field shall contain boot-strapping instructions.
Implementations may populate this field with the CPU instructions
necessary for boot-strapping a computer system. Implementations which
don't provide boot-strapping instructions shall initialize each byte in
this field to 00h as part of their format operation.

### ExtendedBootSignature Field

The ExtendedBootSignature field shall describe whether the intent of
given sector is for it to be an Extended Boot Sector or not.

The valid value for this field is AA550000h. Any other value in this
field invalidates its respective Main or Backup Extended Boot Sector.
Implementations should verify the contents of this field prior to
depending on any other field in its respective Extended Boot Sector.

Main and Backup OEM Parameters Sub-regions
------------------------------------------

The Main OEM Parameters sub-region contains ten parameters structures
which may contain manufacturer-specific information (see Table 7). Each
of the ten parameters structures derives from the Generic Parameters
template (see Section 3.3.2). Manufacturers may derive their own custom
parameters structures from the Generic Parameters template. This
specification itself defines two parameters structures: Null Parameters
(see Section 3.3.3) and Flash Parameters (see Section 3.3.4).

The Backup OEM Parameters is a backup of the Main OEM Parameters and has
the same structure (see Table 7).

Prior to using the contents of either the Main or Backup OEM Parameters,
implementations shall verify their contents by validating their
respective Boot Checksum.

Manufacturers should populate the Main and Backup OEM Parameters with
their own custom parameters structures, if any, and any other parameter
structures. Subsequent format operations shall preserve the contents of
the Main and Backup OEM Parameters.

Implementations may update the Main and Backup OEM Parameters as needed
(and shall also update their respective Boot Checksum).

**OEM Parameters Structure**

<table>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><p><strong>Offset</strong></p>
<p><strong>(byte)</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>(bytes)</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Parameters[0]</td>
<td>0</td>
<td>48</td>
<td>This field is mandatory and Section 3.3.1 defines its contents.</td>
</tr>
<tr class="even">
<td><p>.</p>
<p>.</p>
<p>.</p></td>
<td><p>.</p>
<p>.</p>
<p>.</p></td>
<td><p>.</p>
<p>.</p>
<p>.</p></td>
<td><p>.</p>
<p>.</p>
<p>.</p></td>
</tr>
<tr class="odd">
<td>Parameters[9]</td>
<td>432</td>
<td>48</td>
<td>This field is mandatory and Section 3.3.1 defines its contents.</td>
</tr>
<tr class="even">
<td>Reserved</td>
<td>480</td>
<td>2<sup>BytesPerSectorShift</sup> – 480</td>
<td><p>This field is mandatory and its contents are reserved.</p>
<p>Note: the Main and Backup Boot Sectors both contain the BytesPerSectorShift field.</p></td>
</tr>
</tbody>
</table>

### Parameters\[0\] ... Parameters\[9\]

Each Parameters field in this array contains a parameters structure,
which derives from the Generic Parameters template (see Section 3.3.2).
Any unused Parameters field shall be described as containing a Null
Parameters structure (see Section 3.3.3).

### Generic Parameters Template

The Generic Parameters template provides the base definition of a
parameters structure (see Table 8). All parameters structures derive
from this template. Support for this Generic Parameters template is
mandatory.

**Generic Parameters Template**

<table>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><p><strong>Offset</strong></p>
<p><strong>(byte)</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>(bytes)</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ParametersGuid</td>
<td>0</td>
<td>16</td>
<td>This field is mandatory and Section 3.3.2.1 defines its contents.</td>
</tr>
<tr class="even">
<td>CustomDefined</td>
<td>16</td>
<td>32</td>
<td>This field is mandatory and the structures which derive from this template define its contents.</td>
</tr>
</tbody>
</table>

#### ParametersGuid Field

The ParametersGuid field shall describe a GUID, which determines the
layout of the remainder of the given parameters structure.

All possible values for this field are valid; however, manufacturers
should use a GUID-generating tool, such as GuidGen.exe, to select a GUID
when deriving custom parameters structures from this template.

### Null Parameters

The Null Parameters structure derives from the Generic Parameters
template (see Section 3.3.2) and shall describe an unused Parameters
field (see Table 9). When creating or updating the OEM Parameters
structure, implementations shall populate unused Parameters fields with
the Null Parameters structure. Also, when creating or updating the OEM
Parameters structure, implementations should consolidate Null Parameters
structures at the end of the array, thereby leaving all other Parameters
structures at the beginning of the OEM Parameters structure.

Support for the Null Parameters structure is mandatory.

**Null Parameters Structure**

<table>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><p><strong>Offset</strong></p>
<p><strong>(byte)</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>(bytes)</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ParametersGuid</td>
<td>0</td>
<td>16</td>
<td>This field is mandatory and Section 3.3.3.1 defines its contents.</td>
</tr>
<tr class="even">
<td>Reserved</td>
<td>16</td>
<td>32</td>
<td>This field is mandatory and its contents are reserved.</td>
</tr>
</tbody>
</table>

#### ParametersGuid Field

The ParametersGuid field shall conform to the definition provided by the
Generic Parameters template (see Section 3.3.2.1).

The valid value for this field, in GUID notation, is
{00000000-0000-0000-0000-000000000000}.

### Flash Parameters

The Flash Parameter structure derives from the Generic Parameters
template (see Section 3.3.2) and contains parameters for flash media
(see Table 10). Manufacturers of flash-based storage devices may
populate a Parameters field (preferably the Parameters\[0\] field) with
this parameters structure. Implementations may use the information in
the Flash Parameters structure to optimize access operations during
reads/writes and for alignment of file system structures durning
formatting of the media.

Support for the Flash Parameters structure is optional.

**Flash Parameters Structure**

<table>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><p><strong>Offset</strong></p>
<p><strong>(byte)</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>(bytes)</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ParametersGuid</td>
<td>0</td>
<td>16</td>
<td>This field is mandatory and Section 3.3.4.1 defines its contents.</td>
</tr>
<tr class="even">
<td>EraseBlockSize</td>
<td>16</td>
<td>4</td>
<td>This field is mandatory and Section 3.3.4.2 defines its contents.</td>
</tr>
<tr class="odd">
<td>PageSize</td>
<td>20</td>
<td>4</td>
<td>This field is mandatory and Section 3.3.4.3 defines its contents.</td>
</tr>
<tr class="even">
<td>SpareSectors</td>
<td>24</td>
<td>4</td>
<td>This field is mandatory and Section 3.3.4.4 defines its contents.</td>
</tr>
<tr class="odd">
<td>RandomAccessTime</td>
<td>28</td>
<td>4</td>
<td>This field is mandatory and Section 3.3.4.5 defines its contents.</td>
</tr>
<tr class="even">
<td>ProgrammingTime</td>
<td>32</td>
<td>4</td>
<td>This field is mandatory and Section 3.3.4.6 defines its contents.</td>
</tr>
<tr class="odd">
<td>ReadCycle</td>
<td>36</td>
<td>4</td>
<td>This field is mandatory and Section 3.3.4.7 defines its contents.</td>
</tr>
<tr class="even">
<td>WriteCycle</td>
<td>40</td>
<td>4</td>
<td>This field is mandatory and Section 3.3.4.8 defines its contents.</td>
</tr>
<tr class="odd">
<td>Reserved</td>
<td>44</td>
<td>4</td>
<td>This field is mandatory and its contents are reserved.</td>
</tr>
</tbody>
</table>

All possible values for all Flash Parameters fields, except for the
ParametersGuid field, are valid. However, the value 0 indicates the
field is actually meaningless (implementations shall ignore the given
field).

#### ParametersGuid Field

The ParametersGuid field shall conform to the definition provided in the
Generic Parameters template (see Section 3.3.2.1).

The valid value for this field, in GUID notation, is
{0A0C7E46-3399-4021-90C8-FA6D389C4BA2}.

#### EraseBlockSize Field

The EraseBlockSize field shall describe the size, in bytes, of the flash
media's erase block.

#### PageSize Field

The PageSize field shall describe the size, in bytes of the flash
media's page.

#### SpareSectors Field

The SpareSectors field shall describe the number of sectors the flash
media has available for its internal sparing operations.

#### RandomAccessTime Field

The RandomAccessTime field shall describe the flash media's average
random access time, in nanoseconds.

#### ProgrammingTime Field

The ProgrammingTime field shall describe the flash media's average
programming time, in nanoseconds.

#### ReadCycle Field

The ReadCycle field shall describe the flash media's average read cycle
time, in nanoseconds.

#### WriteCycle Field

The WriteCycle field shall describe the average write cycle time, in
nanoseconds.

Main and Backup Boot Checksum Sub-regions
-----------------------------------------

The Main and Backup Boot Checksums each contain a repeating pattern of
the four-byte checksum of the contents of all other sub-regions in their
respective Boot regions. The checksum calculation shall not include the
VolumeFlags and PercentInUse fields in their respective Boot Sector (see
Figure 1). The repeating pattern of the four-byte checksum fills its
respective Boot Checksum sub-region from the beginning to the end of the
sub-region.

Prior to using the contents of any of the other sub-regions in either
the Main or Backup Boot regions, implementations shall verify their
contents by validating their respective Boot Checksum.

While the initial format operation will populate both the Main and
Backup Boot Checksums with the repeating checksum pattern,
implementations shall update these sectors as the contents of the other
sectors in their respective Boot regions change.

**Boot Checksum Computation**

<table>
<tbody>
<tr class="odd">
<td><p>UInt32 BootChecksum</p>
<p>(</p>
<p>UCHAR * Sectors, // points to an in-memory copy of the 11 sectors</p>
<p>USHORT BytesPerSector</p>
<p>)</p>
<p>{</p>
<p>UInt32 NumberOfBytes = (UInt32)BytesPerSector * 11;</p>
<p>UInt32 Checksum = 0;</p>
<p>UInt32 Index;</p>
<p>for (Index = 0; Index &lt; NumberOfBytes; Index++)</p>
<p>{</p>
<p>if ((Index == 106) || (Index == 107) || (Index == 112))</p>
<p>{</p>
<p>continue;</p>
<p>}</p>
<p>Checksum = ((Checksum&amp;1) ? 0x80000000 : 0) + (Checksum&gt;&gt;1) + (UInt32)Sectors[Index];</p>
<p>}</p>
<p>return Checksum;</p>
<p>}</p></td>
</tr>
</tbody>
</table>

 File Allocation Table Region
============================

The File Allocation Table (FAT) region may contain up to two FATs, one
in the First FAT sub-region and another in the Second FAT sub-region.
The NumberOfFats field describes how many FATs this region contains. The
valid values for the NumberOfFats field are 1 and 2. Therefore, the
First FAT sub-region always contains a FAT. If the NumberOfFats field is
two, then the Second FAT sub-region also contains a FAT.

The ActiveFat field of the VolumeFlags field describes which FAT is
active. Only the VolumeFlags field in the Main Boot Sector is current.
Implementations shall treat the FAT which is not active as stale. Use of
the inactive FAT and switching between FATs is implementation specific.

First and Second FAT Sub-regions
--------------------------------

A FAT shall describe cluster chains in the Cluster Heap (see Table 11).
A cluster chain is a series of clusters which provides space for
recording the contents of files, directories, and other file system
structures. A FAT represents a cluster chain as a singly-linked list of
cluster indices. With the exception of the first two entries, every
entry in a FAT represents exactly one cluster.

**File Allocation Table Structure**

<table>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><p><strong>Offset</strong></p>
<p><strong>(byte)</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>(bytes)</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FatEntry[0]</td>
<td>0</td>
<td>4</td>
<td>This field is mandatory and Section 4.1.1 defines its contents.</td>
</tr>
<tr class="even">
<td>FatEntry[1]</td>
<td>4</td>
<td>4</td>
<td>This field is mandatory and Section 4.1.2 defines its contents.</td>
</tr>
<tr class="odd">
<td>FatEntry[2]</td>
<td>8</td>
<td>4</td>
<td>This field is mandatory and Section 4.1.3 defines its contents.</td>
</tr>
<tr class="even">
<td><p>.</p>
<p>.</p>
<p>.</p></td>
<td><p>.</p>
<p>.</p>
<p>.</p></td>
<td><p>.</p>
<p>.</p>
<p>.</p></td>
<td><p>.</p>
<p>.</p>
<p>.</p></td>
</tr>
<tr class="odd">
<td>FatEntry[ClusterCount+1]</td>
<td>(ClusterCount + 1) * 4</td>
<td>4</td>
<td><p>This field is mandatory and Section 4.1.3 defines its contents.</p>
<p>ClusterCount + 1 can never exceed FFFFFFF6h.</p>
<p>Note: the Main and Backup Boot Sectors both contain the ClusterCount field.</p></td>
</tr>
<tr class="even">
<td>ExcessSpace</td>
<td>(ClusterCount + 2) * 4</td>
<td>(FatLength * 2<sup>BytesPerSectorShift</sup>) – ((ClusterCount + 2) * 4)</td>
<td><p>This field is mandatory and its contents, if any, are undefined.</p>
<p>Note: the Main and Backup Boot Sectors both contain the ClusterCount, FatLength, and BytesPerSectorShift fields.</p></td>
</tr>
</tbody>
</table>

### FatEntry\[0\] Field

The FatEntry\[0\] field shall describe the media type in the first byte
(the lowest order byte) and shall contain FFh in the remaining three
bytes.

The media type (the first byte) should be F8h.

### FatEntry\[1\] Field

The FatEntry\[1\] field only exists due to historical precedence and
does not describe anything of interest.

The valid value for this field is FFFFFFFFh. Implementations shall
initialize this field to its prescribed value and should not use this
field for any purpose. Implementations should not interpret this field
and shall preserve its contents across operations which modify
surrounding fields.

### FatEntry\[2\] ... FatEntry\[ClusterCount+1\] Fields

Each FatEntry field in this array shall represent a cluster in the
Cluster Heap. FatEntry\[2\] represents the first cluster in the Cluster
Heap and FatEntry\[ClusterCount+1\] represents the last cluster in the
Cluster Heap.

The valid range of values for these fields shall be:

-   Between 2 and ClusterCount + 1, inclusively, which points to the
    > next FatEntry in the given cluster chain; the given FatEntry shall
    > not point to any FatEntry which precedes it in the given cluster
    > chain

-   Exactly FFFFFFF7h, which marks the given FatEntry's corresponding
    > cluster as "bad"

-   Exactly FFFFFFFFh, which marks the given FatEntry's corresponding
    > cluster as the last cluster of a cluster chain; this is the only
    > valid value for the last FatEntry of any given cluster chain

 Data Region
===========

The Data region contains the Cluster Heap, which provides managed space
for file system structures, directories, and files.

Cluster Heap Sub-region
-----------------------

The Cluster Heap's structure is very simple (see Table 12); each
consecutive series of sectors describes one cluster, as the
SectorsPerClusterShift field defines. Importantly, the first cluster of
the Cluster Heap has index two, which directly corresponds to the index
of FatEntry\[2\].

In an exFAT volume, an Allocation Bitmap (see Section 7.1.5) maintains
the record of the allocation state of all clusters. This is a
significant difference from exFAT's predecessors (FAT12, FAT16, and
FAT32), in which a FAT maintained a record of the allocation state of
all clusters in the Cluster Heap.

**Cluster Heap Structure**

<table>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><p><strong>Offset</strong></p>
<p><strong>(sector)</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>(sectors)</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Cluster[2]</td>
<td>ClusterHeapOffset</td>
<td>2<sup>SectorsPerClusterShift</sup></td>
<td><p>This field is mandatory and Section 5.1.1 defines its contents.</p>
<p>Note: the Main and Backup Boot Sectors both contain the ClusterHeapOffset and SectorsPerClusterShift fields.</p></td>
</tr>
<tr class="even">
<td><p>.</p>
<p>.</p>
<p>.</p></td>
<td><p>.</p>
<p>.</p>
<p>.</p></td>
<td><p>.</p>
<p>.</p>
<p>.</p></td>
<td><p>.</p>
<p>.</p>
<p>.</p></td>
</tr>
<tr class="odd">
<td>Cluster[ClusterCount+1]</td>
<td>ClusterHeapOffset + (ClusterCount – 1) * 2<sup>SectorsPerClusterShift</sup></td>
<td>2<sup>SectorsPerClusterShift</sup></td>
<td><p>This field is mandatory and Section 5.1.1 defines its contents.</p>
<p>Note: the Main and Backup Boot Sectors both contain the ClusterCount, ClusterHeapOffset, and SectorsPerClusterShift fields.</p></td>
</tr>
</tbody>
</table>

### Cluster\[2\] ... Cluster\[ClusterCount+1\] Fields

Each Cluster field in this array is a series of contiguous sectors,
whose size is defined by the SectorsPerClusterShift field.

 Directory Structure
===================

The exFAT file system uses a directory tree approach to manage the file
system structures and files which exist in the Cluster Heap. Directories
have a one-to-many relationship between parent and child in the
directory tree.

The directory to which the FirstClusterOfRootDirectory field refers is
the root of the directory tree. All other directories descend from the
root directory in a singly-linked fashion.

Each directory consists of a series of directory entries (see Table 13).

One or more directory entries combine into a directory entry set which
describes something of interest, such as a file system structure,
sub-directory, or file.

**Directory Structure**

<table>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><p><strong>Offset</strong></p>
<p><strong>(byte)</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>(byte)</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DirectoryEntry[0]</td>
<td>0</td>
<td>32</td>
<td>This field is mandatory and Section 6.1 defines its contents.</td>
</tr>
<tr class="even">
<td><p>.</p>
<p>.</p>
<p>.</p></td>
<td><p>.</p>
<p>.</p>
<p>.</p></td>
<td><p>.</p>
<p>.</p>
<p>.</p></td>
<td><p>.</p>
<p>.</p>
<p>.</p></td>
</tr>
<tr class="odd">
<td>DirectoryEntry[N–1]</td>
<td>(N – 1) * 32</td>
<td>32</td>
<td><p>This field is mandatory and Section 6.1 defines its contents.</p>
<p>N, the number of DirectoryEntry fields, is the size, in bytes, of the cluster chain which contains the given directory, divided by the size of a DirectoryEntry field, 32 bytes.</p></td>
</tr>
</tbody>
</table>

DirectoryEntry\[0\] ... DirectoryEntry\[N--1\]
----------------------------------------------

Each DirectoryEntry field in this array derives from the Generic
DirectoryEntry template (see Section 6.2).

Generic DirectoryEntry Template
-------------------------------

The Generic DirectoryEntry template provides the base definition for
directory entries (see Table 14). All directory entry structures derive
from this template and only Microsoft-defined directory entry structures
are valid (exFAT does not have provisions for manufacturer-defined
directory entry structures except as defined in section 7.8 and section
7.9). The ability to interpret the Generic DirectoryEntry template is
mandatory.

**Generic DirectoryEntry Template**

<table>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><p><strong>Offset</strong></p>
<p><strong>(byte)</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>(byte)</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>EntryType</td>
<td>0</td>
<td>1</td>
<td>This field is mandatory and Section 6.2.1 defines its contents.</td>
</tr>
<tr class="even">
<td>CustomDefined</td>
<td>1</td>
<td>19</td>
<td>This field is mandatory and structures which derive from this template may define its contents.</td>
</tr>
<tr class="odd">
<td>FirstCluster</td>
<td>20</td>
<td>4</td>
<td>This field is mandatory and Section 6.2.2 defines its contents.</td>
</tr>
<tr class="even">
<td>DataLength</td>
<td>24</td>
<td>8</td>
<td>This field is mandatory and Section 6.2.3 defines its contents.</td>
</tr>
</tbody>
</table>

### EntryType Field

The EntryType field has three modes of usage which the value of the
field defines (see list below).

-   00h, which is an end-of-directory marker and the following
    conditions apply:

    -   All other fields in the given DirectoryEntry are actually
        reserved

    -   All subsequent directory entries in the given directory also are
        end-of-directory markers

    -   End-of-directory markers are only valid outside directory entry
        sets

    -   Implementations may overwrite end-of-directory markers as
        necessary

-   Between 01h and 7Fh inclusively, which is an unused-directory-entry
    marker and the following conditions apply:

    -   All other fields in the given DirectoryEntry are actually
        undefined

    -   Unused directory entries are only valid outside of directory
        entry sets

    -   Implementations may overwrite unused directory entries as
        necessary

    -   This range of values corresponds to the InUse field (see Section
        6.2.1.4) containing the value 0

-   Between 81h and FFh inclusively, which is a regular directory entry
    and the following conditions apply:

    -   The contents of the EntryType field (see Table 15) determine the
        layout of the remainder of the DirectoryEntry structure

    -   This range of values, and only this range of values, are valid
        inside a directory entry set

    -   This range of values directly corresponds to the InUse field
        (see Section 6.2.1.4) containing the value 1

To prevent modifications to the InUse field (see Section 6.2.1.4)
erroneously resulting in an end-of-directory marker, the value 80h is
invalid.

**Generic EntryType Field Structure**

<table>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><p><strong>Offset</strong></p>
<p><strong>(bit)</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>(bits)</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>TypeCode</td>
<td>0</td>
<td>5</td>
<td>This field is mandatory and Section 6.2.1.1 defines its contents.</td>
</tr>
<tr class="even">
<td>TypeImportance</td>
<td>5</td>
<td>1</td>
<td>This field is mandatory and Section 6.2.1.2 defines its contents.</td>
</tr>
<tr class="odd">
<td>TypeCategory</td>
<td>6</td>
<td>1</td>
<td>This field is mandatory and Section 6.2.1.3 defines its contents.</td>
</tr>
<tr class="even">
<td>InUse</td>
<td>7</td>
<td>1</td>
<td>This field is mandatory and Section 6.2.1.4 defines its contents.</td>
</tr>
</tbody>
</table>

#### TypeCode Field

The TypeCode field partially describes the specific type of the given
directory entry. This field, plus the TypeImportance and TypeCategory
fields (see Sections 6.2.1.2 and 6.2.1.3, respectively) uniquely
identify the type of the given directory entry.

All possible values of this field are valid, unless the TypeImportance
and TypeCategory fields both contain the value 0; in that case, the
value 0 is invalid for this field.

#### TypeImportance Field

The TypeImportance field shall describe the importance of the given
directory entry.

The valid values for this field shall be:

-   0, which means the given directory entry is critical (see Sections
    6.3.1.2.1 and 6.4.1.2.1 for critical primary and critical secondary
    directory entries, respectively)

-   1, which means the given directory entry is benign (see Sections
    6.3.1.2.2 and 6.4.1.2.2 for benign primary and benign secondary
    directory entries, respectively)

#### TypeCategory Field

The TypeCategory field shall describe the category of the given
directory entry.

The valid values for this field shall be:

-   0, which means the given directory entry is primary (see Section
    6.3)

-   1, which means the given directory entry is secondary (see Section
    6.4)

#### InUse Field

The InUse field shall describe whether the given directory entry in use
or not.

The valid values for this field shall be:

-   0, which means the given directory entry is not in use; this means
    the given structure actually is an unused directory entry

-   1, which means the given directory entry is in use; this means the
    given structure is a regular directory entry

### FirstCluster Field

The FirstCluster field shall contain the index of the first cluster of
an allocation in the Cluster Heap associated with the given directory
entry.

The valid range of values for this field shall be:

-   Exactly 0, which means no cluster allocation exists

-   Between 2 and ClusterCount + 1, which is the range of valid cluster
    indices

Structures which derive from this template may redefine both the
FirstCluster and DataLength fields, if a cluster allocation is not
compatible with the derivative structure.

### DataLength Field

The DataLength field describes the size, in bytes, of the data the
associated cluster allocation contains.

The valid range of value for this field is:

-   At least 0; if the FirstCluster field contains the value 0, then
    this field's only valid value is 0

-   At most ClusterCount \* 2^SectorsPerClusterShift^ \*
    2^BytesPerSectorShift^

Structures which derive from this template may redefine both the
FirstCluster and DataLength fields, if a cluster allocation is not
possible for the derivative structure.

Generic Primary DirectoryEntry Template
---------------------------------------

The first directory entry in a directory entry set shall be a primary
directory entry. All subsequent directory entries, if any, in the
directory entry set shall be secondary directory entries (see Section
6.4).

The ability to interpret the Generic Primary DirectoryEntry template is
mandatory.

All primary directory entry structures derive from the Generic Primary
DirectoryEntry template (see Table 16), which derives from the Generic
DirectoryEntry template (see Section 6.2).

**Generic Primary DirectoryEntry Template**

<table>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><p><strong>Offset</strong></p>
<p><strong>(byte)</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>(byte)</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>EntryType</td>
<td>0</td>
<td>1</td>
<td>This field is mandatory and Section 6.3.1 defines its contents.</td>
</tr>
<tr class="even">
<td>SecondaryCount</td>
<td>1</td>
<td>1</td>
<td>This field is mandatory and Section 6.3.2 defines its contents.</td>
</tr>
<tr class="odd">
<td>SetChecksum</td>
<td>2</td>
<td>2</td>
<td>This field is mandatory and Section 6.3.3 defines its contents.</td>
</tr>
<tr class="even">
<td>GeneralPrimaryFlags</td>
<td>4</td>
<td>2</td>
<td>This field is mandatory and Section 6.3.4 defines its contents.</td>
</tr>
<tr class="odd">
<td>CustomDefined</td>
<td>6</td>
<td>14</td>
<td>This field is mandatory and structures which derive from this template define its contents.</td>
</tr>
<tr class="even">
<td>FirstCluster</td>
<td>20</td>
<td>4</td>
<td>This field is mandatory and Section 6.3.5 defines its contents.</td>
</tr>
<tr class="odd">
<td>DataLength</td>
<td>24</td>
<td>8</td>
<td>This field is mandatory and Section 6.3.6 defines its contents.</td>
</tr>
</tbody>
</table>

### EntryType Field

The EntryType field shall conform to the definition provided in the
Generic DirectoryEntry template (see Section 6.2.1).

#### TypeCode Field

The TypeCode field shall conform to the definition provided in the
Generic DirectoryEntry template (see Section 6.2.1.1).

#### TypeImportance Field

The TypeImportance field shall conform to the definition provided in the
Generic DirectoryEntry template (see Section 6.2.1.2).

##### Critical Primary Directory Entries

Critical primary directory entries contain information which is critical
to the proper management of an exFAT volume. Only the root directory
contains critical primary directory entries (File directory entries are
an exception, see Section 7.4).

The definition of critical primary directory entries correlates to the
major exFAT revision number. Implementations shall support all critical
primary directory entries and shall only record the critical primary
directory entry structures this specification defines.

##### Benign Primary Directory Entries

Benign primary directory entries contain additional information which
may be useful for managing an exFAT volume. Any directory may contain
benign primary directory entries.

The definition of benign primary directory entries correlates to the
minor exFAT revision number. Support for any benign primary directory
entry this specification, or any subsequent specification, defines is
optional. An unrecognized benign primary directory entry renders the
entire directory entry set as unrecognized (beyond the definition of the
applicable directory entry templates).

#### TypeCategory Field

The TypeCategory field shall conform to the definition provided in the
Generic DirectoryEntry template (see Section 6.2.1.3).

For this template, the valid value for this field shall be 0.

#### InUse Field

The InUse field shall conform to the definition provided in the Generic
DirectoryEntry template (see Section 6.2.1.4).

### SecondaryCount Field

The SecondaryCount field shall describe the number of secondary
directory entries which immediately follow the given primary directory
entry. These secondary directory entries, along with the given primary
directory entry, comprise the directory entry set.

The valid range of values for this field shall be:

-   At least 0, which means this primary directory entry is the only
    entry in the directory entry set

-   At most 255, which means the next 255 directory entries and this
    primary directory entry comprise the directory entry set

Critical primary directory entry structures which derive from this
template may redefine both the SecondaryCount and SetChecksum fields.

### SetChecksum Field

The SetChecksum field shall contain the checksum of all directory
entries in the given directory entry set. However, the checksum excludes
this field (see Figure 2). Implementations shall verify the contents of
this field are valid prior to using any other directory entry in the
given directory entry set.

Critical primary directory entry structures which derive from this
template may redefine both the SecondaryCount and SetChecksum fields.

**EntrySetChecksum Computation**

<table>
<tbody>
<tr class="odd">
<td><p>UInt16 EntrySetChecksum</p>
<p>(</p>
<p>UCHAR * Entries, // points to an in-memory copy of the directory entry set</p>
<p>UCHAR SecondaryCount</p>
<p>)</p>
<p>{</p>
<p>UInt16 NumberOfBytes = ((UInt16)SecondaryCount + 1) * 32;</p>
<p>UInt16 Checksum = 0;</p>
<p>UInt16 Index;</p>
<p>for (Index = 0; Index &lt; NumberOfBytes; Index++)</p>
<p>{</p>
<p>if ((Index == 2) || (Index == 3))</p>
<p>{</p>
<p>continue;</p>
<p>}</p>
<p>Checksum = ((Checksum&amp;1) ? 0x8000 : 0) + (Checksum&gt;&gt;1) + (UInt16)Entries[Index];</p>
<p>}</p>
<p>return Checksum;</p>
<p>}</p></td>
</tr>
</tbody>
</table>

### GeneralPrimaryFlags Field

The GeneralPrimaryFlags field contains flags (see Table 17).

Critical primary directory entry structures which derive from this
template may redefine this field.

**Generic GeneralPrimaryFlags Field Structure**

<table>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><p><strong>Offset</strong></p>
<p><strong>(bit)</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>(bits)</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AllocationPossible</td>
<td>0</td>
<td>1</td>
<td>This field is mandatory and Section 6.3.4.1 defines its contents.</td>
</tr>
<tr class="even">
<td>NoFatChain</td>
<td>1</td>
<td>1</td>
<td>This field is mandatory and Section 6.3.4.2 defines its contents.</td>
</tr>
<tr class="odd">
<td>CustomDefined</td>
<td>2</td>
<td>14</td>
<td>This field is mandatory and structures which derive from this template may define this field.</td>
</tr>
</tbody>
</table>

#### AllocationPossible Field

The AllocationPossible field shall describe whether or not an allocation
in the Cluster Heap is possible for the given directory entry.

The valid values for this field shall be:

-   0, which means an associated allocation of clusters is not possible
    and the FirstCluster and DataLength fields are actually undefined
    (structures which derive from this template may redefine those
    fields)

-   1, which means an associated allocation of clusters is possible and
    the FirstCluster and DataLength fields are as defined

#### NoFatChain Field

The NoFatChain field shall indicate whether or not the active FAT
describes the given allocation's cluster chain.

The valid values for this field shall be:

-   0, which means the corresponding FAT entries for the allocation's
    cluster chain are valid and implementations shall interpret them; if
    the AllocationPossible field contains the value 0, or if the
    AllocationPossible field contains the value 1 and the FirstCluster
    field contains the value 0, then this field's only valid value is 0

-   1, which means the associated allocation is one contiguous series of
    clusters; the corresponding FAT entries for the clusters are invalid
    and implementations shall not interpret them; implementations may
    use the following equation to calculate the size of the associated
    allocation:

> DataLength / (2^SectorsPerClusterShift^ \* 2^BytesPerSectorShift^)
> rounded up to the nearest integer

If critical primary directory entry structures which derive from this
template redefine the GeneralPrimaryFlags field, then the corresponding
FAT entries for any associated allocation's cluster chain are valid.

### FirstCluster Field

The FirstCluster field shall conform to the definition provided in the
Generic DirectoryEntry template (see Section 6.2.2).

If the NoFatChain bit is 1 then FirstCluster must point to a valid
cluster in the cluster heap.

Critical primary directory entry structures which derive from this
template may redefine the FirstCluster and DataLength fields. Other
structures which derive from this template may redefine the FirstCluster
and DataLength fields only if the AllocationPossible field contains the
value 0.

### DataLength Field

The DataLength field shall conform to the definition provided in the
Generic DirectoryEntry template (see Section 6.2.3).

If the NoFatChain bit is 1 then DataLength must not be zero. If the
FirstCluster field is zero, then DataLength must also be zero.

Critical primary directory entry structures which derive from this
template may redefine the FirstCluster and DataLength fields. Other
structures which derive from this template may redefine the FirstCluster
and DataLength fields only if the AllocationPossible field contains the
value 0.

Generic Secondary DirectoryEntry Template
-----------------------------------------

The central purpose of secondary directory entries is to provide
additional information about a directory entry set. The ability to
interpret the Generic Secondary DirectoryEntry template is mandatory.

The definition of both critical and benign secondary directory entries
correlates to the minor exFAT revision number. Support for any critical
or benign secondary directory entry this specification, or subsequent
specifications, defines is optional.

All secondary directory entry structures derive from the Generic
Secondary DirectoryEntry template (see Table 18), which derives from the
Generic DirectoryEntry template (see Section 6.2).

**Generic Secondary DirectoryEntry Template**

<table>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><p><strong>Offset</strong></p>
<p><strong>(byte)</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>(byte)</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>EntryType</td>
<td>0</td>
<td>1</td>
<td>This field is mandatory and Section 6.4.1 defines its contents.</td>
</tr>
<tr class="even">
<td>GeneralSecondaryFlags</td>
<td>1</td>
<td>1</td>
<td>This field is mandatory and Section 6.4.2 defines its contents.</td>
</tr>
<tr class="odd">
<td>CustomDefined</td>
<td>2</td>
<td>18</td>
<td>This field is mandatory and structures which derive from this template define its contents.</td>
</tr>
<tr class="even">
<td>FirstCluster</td>
<td>20</td>
<td>4</td>
<td>This field is mandatory and Section 6.4.3 defines its contents.</td>
</tr>
<tr class="odd">
<td>DataLength</td>
<td>24</td>
<td>8</td>
<td>This field is mandatory and Section 6.4.4 defines its contents.</td>
</tr>
</tbody>
</table>

### EntryType Field

The EntryType field shall conform to the definition provided in the
Generic DirectoryEntry template (see Section 6.2.1)

#### TypeCode Field

The TypeCode field shall conform to the definition provided in the
Generic DirectoryEntry template (see Section 6.2.1.1).

#### TypeImportance Field

The TypeImportance field shall conform to the definition provided in the
Generic DirectoryEntry template (see Section 6.2.1.2).

##### Critical Secondary Directory Entries

Critical secondary directory entries contain information which is
critical to the proper management of its containing directory entry set.
While support for any specific critical secondary directory entry is
optional, an unrecognized critical directory entry renders the entire
directory entry set as unrecognized (beyond the definition of the
applicable directory entry templates).

However, if a directory entry set contains at least one critical
secondary directory entry which an implementation does not recognize,
then the implementation shall at most interpret the templates of the
directory entries in the directory entry set and not the data any
allocation associated with any directory entry in the directory entry
set contains (File directory entries are an exception, see Section 7.4).

##### Benign Secondary Directory Entries

Benign secondary directory entries contain additional information which
may be useful for managing its containing directory entry set. Support
for any specific benign secondary directory entry is optional.
Unrecognized benign secondary directory entries do not render the entire
directory entry set as unrecognized.

Implementations may ignore any benign secondary entry it does not
recognize.

#### TypeCategory Field

The TypeCategory field shall conform to the definition provided in the
Generic DirectoryEntry template (see Section 6.2.1.3).

For this template, the valid value for this field is 1.

#### InUse Field

The InUse field shall conform to the definition provided in the Generic
DirectoryEntry template (see Section 6.2.1.4).

### GeneralSecondaryFlags Field

The GeneralSecondaryFlags field contains flags (see Table 19).

**Generic GeneralSecondaryFlags Field Structure**

<table>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><p><strong>Offset</strong></p>
<p><strong>(bit)</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>(bits)</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AllocationPossible</td>
<td>0</td>
<td>1</td>
<td>This field is mandatory and Section 6.4.2.1 defines its contents.</td>
</tr>
<tr class="even">
<td>NoFatChain</td>
<td>1</td>
<td>1</td>
<td>This field is mandatory and Section 6.4.2.2 defines its contents.</td>
</tr>
<tr class="odd">
<td>CustomDefined</td>
<td>2</td>
<td>6</td>
<td>This field is mandatory and structures which derive from this template may define this field.</td>
</tr>
</tbody>
</table>

#### AllocationPossible Field

The AllocationPossible field shall have the same definition as the
same-named field in the Generic Primary DirectoryEntry template (see
Section 6.3.4.1).

#### NoFatChain Field

The NoFatChain field shall have the same definition as the same-named
field in the Generic Primary DirectoryEntry template (see Section
6.3.4.2).

### FirstCluster Field

The FirstCluster field shall conform to the definition provided in the
Generic DirectoryEntry template (see Section 6.2.2).

If the NoFatChain bit is 1 then FirstCluster must point to a valid
cluster in the cluster heap.

### DataLength Field

The DataLength field shall conform to the definition provided in the
Generic DirectoryEntry template (see Section 6.2.3).

If the NoFatChain bit is 1 then DataLength must not be zero. If the
FirstCluster field is zero, then DataLength must also be zero.

 Directory Entry Definitions
===========================

Revision 1.00 of the exFAT file system defines the following directory
entries:

-   Critical primary

    -   Allocation Bitmap (Section 7.1)

    -   Up-case Table (Section 7.2)

    -   Volume Label (Section 7.3)

    -   File (Section 7.4)

-   Benign primary

    -   Volume GUID (Section 7.5)

    -   TexFAT Padding (Section 7.10)

<!-- -->

-   Critical secondary

    -   Stream Extension (Section 7.6)

    -   File Name (Section 7.7)

-   Benign secondary

    -   Vendor Extension (Section 7.8)

    -   Vendor Allocation (Section 7.9)

Allocation Bitmap Directory Entry
---------------------------------

In the exFAT file system, a FAT does not describe the allocation state
of clusters; rather, an Allocation Bitmap does. Allocation Bitmaps exist
in the Cluster Heap (see Section 7.1.5) and have corresponding critical
primary directory entries in the root directory (see Table 20).

The NumberOfFats field determines the number of valid Allocation Bitmap
directory entries in the root directory. If the NumberOfFats field
contains the value 1, then the only valid number of Allocation Bitmap
directory entries is 1. Further, the one Allocation Bitmap directory
entry is only valid if it describes the First Allocation Bitmap (see
Section 7.1.2.1). If the NumberOfFats field contains the value 2, then
the only valid number of Allocation Bitmap directory entries is 2.
Further, the two Allocation Bitmap directory entries are only valid if
one describes the First Allocation Bitmap and the other describes the
Second Allocation Bitmap.

**Allocation Bitmap DirectoryEntry Structure**

<table>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><p><strong>Offset</strong></p>
<p><strong>(byte)</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>(byte)</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>EntryType</td>
<td>0</td>
<td>1</td>
<td>This field is mandatory and Section 7.1.1 defines its contents.</td>
</tr>
<tr class="even">
<td>BitmapFlags</td>
<td>1</td>
<td>1</td>
<td>This field is mandatory and Section 7.1.2 defines its contents.</td>
</tr>
<tr class="odd">
<td>Reserved</td>
<td>2</td>
<td>18</td>
<td>This field is mandatory and its contents are reserved.</td>
</tr>
<tr class="even">
<td>FirstCluster</td>
<td>20</td>
<td>4</td>
<td>This field is mandatory and Section 7.1.3 defines its contents.</td>
</tr>
<tr class="odd">
<td>DataLength</td>
<td>24</td>
<td>8</td>
<td>This field is mandatory and Section 7.1.4 defines its contents.</td>
</tr>
</tbody>
</table>

### EntryType Field

The EntryType field shall conform to the definition provided in the
Generic Primary DirectoryEntry template (see Section 6.3.1).

#### TypeCode Field

The TypeCode field shall conform to the definition provided in the
Generic Primary DirectoryEntry template (see Section 6.3.1.1).

For an Allocation Bitmap directory entry, the valid value for this field
is 1.

#### TypeImportance Field

The TypeImportance field shall conform to the definition provided in the
Generic Primary DirectoryEntry template (see Section 6.3.1.2).

For an Allocation Bitmap directory entry, the valid value for this field
is 0.

#### TypeCategory Field

The TypeCategory field shall conform to the definition provided in the
Generic Primary DirectoryEntry template (see Section 6.3.1.3).

#### InUse Field

The InUse field shall conform to the definition provided in the Generic
Primary DirectoryEntry template (see Section 6.3.1.4).

### BitmapFlags Field

The BitmapFlags field contains flags (see Table 21).

**BitmapFlags Field Structure**

<table>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><p><strong>Offset</strong></p>
<p><strong>(bit)</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>(bits)</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>BitmapIdentifier</td>
<td>0</td>
<td>1</td>
<td>This field is mandatory and Section 7.1.2.1 defines its contents.</td>
</tr>
<tr class="even">
<td>Reserved</td>
<td>1</td>
<td>7</td>
<td>This field is mandatory and its contents are reserved.</td>
</tr>
</tbody>
</table>

#### BitmapIdentifier Field

The BitmapIdentifier field shall indicate which Allocation Bitmap the
given directory entry describes. Implementations shall use the First
Allocation Bitmap in conjunction with the First FAT and shall use the
Second Allocation Bitmap in conjunction with the Second FAT. The
ActiveFat field describes which FAT and Allocation Bitmap are active.

The valid values for this field shall be:

-   0, which means the given directory entry describes the First
    Allocation Bitmap

-   1, which means the given directory entry describes the Second
    Allocation Bitmap and is possible only when NumberOfFats contains
    the value 2

### FirstCluster Field

The FirstCluster field shall conform to the definition provided in the
Generic Primary DirectoryEntry template (see Section 6.3.5).

This field contains the index of the first cluster of the cluster chain,
as the FAT describes, which hosts the Allocation Bitmap.

### DataLength Field

The DataCluster field shall conform to the definition provided in the
Generic Primary DirectoryEntry template (see Section 6.3.6).

### Allocation Bitmap

An Allocation Bitmap records the allocation state of the clusters in the
Cluster Heap. Each bit in an Allocation Bitmap indicates whether its
corresponding cluster is available for allocation or not.

An Allocation Bitmap represents clusters from lowest to highest index
(see Table 22). For historical reasons, the first cluster has index 2.
Note: the first bit in the bitmap is the lowest-order bit of the first
byte.

**Allocation Bitmap Structure**

<table>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><p><strong>Offset</strong></p>
<p><strong>(bit)</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>(bits)</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>BitmapEntry[2]</td>
<td>0</td>
<td>1</td>
<td>This field is mandatory and Section 7.1.5.1 defines its contents.</td>
</tr>
<tr class="even">
<td><p>.</p>
<p>.</p>
<p>.</p></td>
<td><p>.</p>
<p>.</p>
<p>.</p></td>
<td><p>.</p>
<p>.</p>
<p>.</p></td>
<td><p>.</p>
<p>.</p>
<p>.</p></td>
</tr>
<tr class="odd">
<td>BitmapEntry[ClusterCount+1]</td>
<td>ClusterCount - 1</td>
<td>1</td>
<td><p>This field is mandatory and Section 7.1.5.1 defines its contents.</p>
<p>Note: the Main and Backup Boot Sectors both contain the ClusterCount field.</p></td>
</tr>
<tr class="even">
<td>Reserved</td>
<td>ClusterCount</td>
<td>(DataLength * 8) – ClusterCount</td>
<td><p>This field is mandatory and its contents, if any, are reserved.</p>
<p>Note: the Main and Backup Boot Sectors both contain the ClusterCount field.</p></td>
</tr>
</tbody>
</table>

#### BitmapEntry\[2\] ... BitmapEntry\[ClusterCount+1\] Fields

Each BitmapEntry field in this array represents a cluster in the Cluster
Heap. BitmapEntry\[2\] represents the first cluster in the Cluster Heap
and BitmapEntry\[ClusterCount+1\] represents the last cluster in the
Cluster Heap.

The valid values for these fields shall be:

-   0, which describes the corresponding cluster as available for
    allocation

-   1, which describes the corresponding cluster as not available for
    allocation (a cluster allocation may already consume the
    corresponding cluster or the active FAT may describe the
    corresponding cluster as bad)

Up-case Table Directory Entry
-----------------------------

The Up-case Table defines the conversion from lower-case to upper-case
characters. This is important due to the File Name directory entry (see
Section 7.7) using Unicode characters and the exFAT file system being
case insensitive and case preserving. The Up-case Table exists in the
Cluster Heap (see Section 7.2.5) and has a corresponding critical
primary directory entry in the root directory (see Table 23). The valid
number of Up-case Table directory entries is 1.

Due to the relationship between the Up-case Table and file names,
implementations should not modify the Up-case Table, except as a result
of format operations.

**Up-case Table DirectoryEntry Structure**

<table>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><p><strong>Offset</strong></p>
<p><strong>(byte)</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>(byte)</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>EntryType</td>
<td>0</td>
<td>1</td>
<td>This field is mandatory and Section 7.2.1 defines its contents.</td>
</tr>
<tr class="even">
<td>Reserved1</td>
<td>1</td>
<td>3</td>
<td>This field is mandatory and its contents are reserved.</td>
</tr>
<tr class="odd">
<td>TableChecksum</td>
<td>4</td>
<td>4</td>
<td>This field is mandatory and Section 7.2.2 defines its contents.</td>
</tr>
<tr class="even">
<td>Reserved2</td>
<td>8</td>
<td>12</td>
<td>This field is mandatory and its contents are reserved.</td>
</tr>
<tr class="odd">
<td>FirstCluster</td>
<td>20</td>
<td>4</td>
<td>This field is mandatory and Section 7.2.3 defines its contents.</td>
</tr>
<tr class="even">
<td>DataLength</td>
<td>24</td>
<td>8</td>
<td>This field is mandatory and Section 7.2.4 defines its contents.</td>
</tr>
</tbody>
</table>

### EntryType Field

The EntryType field shall conform to the definition provided in the
Generic Primary DirectoryEntry template (see Section 6.3.1).

#### TypeCode Field

The TypeCode field shall conform to the definition provided in the
Generic Primary DirectoryEntry template (see Section 6.3.1.1).

For the Up-case Table directory entry, the valid value for this field is
2.

#### TypeImportance Field

The TypeImportance field shall conform to the definition provided in the
Generic Primary DirectoryEntry template (see Section 6.3.1.2).

For the Up-case Table directory entry, the valid value for this field is
0.

#### TypeCategory Field

The TypeCategory field shall conform to the definition provided in the
Generic Primary DirectoryEntry template (see Section 6.3.1.3).

#### InUse Field

The InUse field shall conform to the definition provided in the Generic
Primary DirectoryEntry template (see Section 6.3.1.4).

### TableChecksum Field

The TableChecksum field contains the checksum of the Up-case Table
(which the FirstCluster and DataLength fields describe). Implementations
shall verify the contents of this field are valid prior to using the
Up-case Table.

[]{#_Toc219626627 .anchor}Figure 3 TableChecksum Computation

<table>
<tbody>
<tr class="odd">
<td><p>UInt32 TableChecksum</p>
<p>(</p>
<p>UCHAR * Table, // points to an in-memory copy of the up-case table</p>
<p>UInt64 DataLength</p>
<p>)</p>
<p>{</p>
<p>UInt32 Checksum = 0;</p>
<p>UInt64 Index;</p>
<p>for (Index = 0; Index &lt; DataLength; Index++)</p>
<p>{</p>
<p>Checksum = ((Checksum&amp;1) ? 0x80000000 : 0) + (Checksum&gt;&gt;1) + (UInt32)Table[Index];</p>
<p>}</p>
<p>return Checksum;</p>
<p>}</p></td>
</tr>
</tbody>
</table>

### FirstCluster Field

The FirstCluster field shall conform to the definition provided in the
Generic Primary DirectoryEntry template (see Section 6.3.5).

This field contains the index of the first cluster of the cluster chain,
as the FAT describes, which hosts the Up-case Table.

### DataLength Field

The DataCluster field shall conform to the definition provided in the
Generic Primary DirectoryEntry template (see Section 6.3.6).

### Up-case Table

An up-case table is a series of Unicode character mappings. A character
mapping consists of a 2-byte field, with the index of the field in the
up-case table representing the Unicode character to be up-cased, and the
2-byte field representing the up-cased Unicode character.

The first 128 Unicode characters have mandatory mappings (see Table 24).
An up-case table which has any other character mapping for any of the
first 128 Unicode characters is invalid.

Implementations which only support characters from the mandatory mapping
range may ignore the mappings of the rest of the up-case table. Such
implementations shall only use characters from the mandatory mapping
range when creating or renaming files (via the File Name directory
entry, see Section 7.7). When up-casing existing file names, such
implementations shall not up-case characters from the non-mandatory
mapping range, but shall leave them intact in the resulting up-cased
file name (this is a partial up-casing). When comparing file names, such
implementations shall treat file names which differ from the name under
comparison only by Unicode characters from the non-mandatory mapping
range as equivalent. While such file names are only potentially
equivalent, such implementations cannot ensure the fully up-cased file
name does not collide with the name under comparison.

**Mandatory First 128 Up-case Table Entries**

<table>
<thead>
<tr class="header">
<th><strong>Table Index</strong></th>
<th><strong>Table Entries</strong></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><strong>+ 0</strong></td>
<td><strong>+ 1</strong></td>
<td><strong>+ 2</strong></td>
<td><strong>+ 3</strong></td>
<td><strong>+ 4</strong></td>
<td><strong>+ 5</strong></td>
<td><strong>+ 6</strong></td>
<td><strong>+ 7</strong></td>
</tr>
<tr class="even">
<td><strong>0000h</strong></td>
<td>0000h</td>
<td>0001h</td>
<td>0002h</td>
<td>0003h</td>
<td>0004h</td>
<td>0005h</td>
<td>0006h</td>
<td>0007h</td>
</tr>
<tr class="odd">
<td><strong>0008h</strong></td>
<td>0008h</td>
<td>0009h</td>
<td>000Ah</td>
<td>000Bh</td>
<td>000Ch</td>
<td>000Dh</td>
<td>000Eh</td>
<td>000Fh</td>
</tr>
<tr class="even">
<td><strong>0010h</strong></td>
<td>0010h</td>
<td>0011h</td>
<td>0012h</td>
<td>0013h</td>
<td>0014h</td>
<td>0015h</td>
<td>0016h</td>
<td>0017h</td>
</tr>
<tr class="odd">
<td><strong>0018h</strong></td>
<td>0018h</td>
<td>0019h</td>
<td>001Ah</td>
<td>001Bh</td>
<td>001Ch</td>
<td>001Dh</td>
<td>001Eh</td>
<td>001Fh</td>
</tr>
<tr class="even">
<td><strong>0020h</strong></td>
<td>0020h</td>
<td>0021h</td>
<td>0022h</td>
<td>0023h</td>
<td>0024h</td>
<td>0025h</td>
<td>0026h</td>
<td>0027h</td>
</tr>
<tr class="odd">
<td><strong>0028h</strong></td>
<td>0028h</td>
<td>0029h</td>
<td>002Ah</td>
<td>002Bh</td>
<td>002Ch</td>
<td>002Dh</td>
<td>002Eh</td>
<td>002Fh</td>
</tr>
<tr class="even">
<td><strong>0030h</strong></td>
<td>0030h</td>
<td>0031h</td>
<td>0032h</td>
<td>0033h</td>
<td>0034h</td>
<td>0035h</td>
<td>0036h</td>
<td>0037h</td>
</tr>
<tr class="odd">
<td><strong>0038h</strong></td>
<td>0038h</td>
<td>0039h</td>
<td>003Ah</td>
<td>003Bh</td>
<td>003Ch</td>
<td>003Dh</td>
<td>003Eh</td>
<td>003Fh</td>
</tr>
<tr class="even">
<td><strong>0040h</strong></td>
<td>0040h</td>
<td>0041h</td>
<td>0042h</td>
<td>0043h</td>
<td>0044h</td>
<td>0045h</td>
<td>0046h</td>
<td>0047h</td>
</tr>
<tr class="odd">
<td><strong>0048h</strong></td>
<td>0048h</td>
<td>0049h</td>
<td>004Ah</td>
<td>004Bh</td>
<td>004Ch</td>
<td>004Dh</td>
<td>004Eh</td>
<td>004Fh</td>
</tr>
<tr class="even">
<td><strong>0050h</strong></td>
<td>0050h</td>
<td>0051h</td>
<td>0052h</td>
<td>0053h</td>
<td>0054h</td>
<td>0055h</td>
<td>0056h</td>
<td>0057h</td>
</tr>
<tr class="odd">
<td><strong>0058h</strong></td>
<td>0058h</td>
<td>0059h</td>
<td>005Ah</td>
<td>005Bh</td>
<td>005Ch</td>
<td>005Dh</td>
<td>005Eh</td>
<td>005Fh</td>
</tr>
<tr class="even">
<td><strong>0060h</strong></td>
<td>0060h</td>
<td><strong>0041h</strong></td>
<td><strong>0042h</strong></td>
<td><strong>0043h</strong></td>
<td><strong>0044h</strong></td>
<td><strong>0045h</strong></td>
<td><strong>0046h</strong></td>
<td><strong>0047h</strong></td>
</tr>
<tr class="odd">
<td><strong>0068h</strong></td>
<td><strong>0048h</strong></td>
<td><strong>0049h</strong></td>
<td><strong>004Ah</strong></td>
<td><strong>004Bh</strong></td>
<td><strong>004Ch</strong></td>
<td><strong>004Dh</strong></td>
<td><strong>004Eh</strong></td>
<td><strong>004Fh</strong></td>
</tr>
<tr class="even">
<td><strong>0070h</strong></td>
<td><strong>0050h</strong></td>
<td><strong>0051h</strong></td>
<td><strong>0052h</strong></td>
<td><strong>0053h</strong></td>
<td><strong>0054h</strong></td>
<td><strong>0055h</strong></td>
<td><strong>0056h</strong></td>
<td><strong>0057h</strong></td>
</tr>
<tr class="odd">
<td><strong>0078h</strong></td>
<td><strong>0058h</strong></td>
<td><strong>0059h</strong></td>
<td><strong>005Ah</strong></td>
<td>007Bh</td>
<td>007Ch</td>
<td>007Dh</td>
<td>007Eh</td>
<td>007Fh</td>
</tr>
</tbody>
</table>

**(Note: entries with non-identity up-case mappings are in bold)**

Upon formatting a volume, implementations may generate an up-case table
in a compressed format using identity-mapping compression, since a large
portion of the Unicode character space has no concept of case (which
means the "lower-case" and "upper-case" characters are equivalent).
Implementations compress an up-case table by representing a series of
identity mappings with the value FFFFh followed with the number of
identity mappings.

For example, an implementation may represent the first 100 (64h)
character mappings with the following eight entries of a compressed
up-case table:

> FFFFh, 0061h, 0041h, 0042h, 0043h

The first two entries indicate the first 97 (61h) characters (from 0000h
to 0060h) have identity mappings. The subsequent characters, 0061h
through 0063h, map to characters 0041h through 0043h, respectively.

The ability to provide a compressed up-case table upon formatting a
volume is optional. However, the ability to interpret both an
uncompressed and a compressed up-case table is mandatory. The value of
the TableChecksum field always conforms to how the up-case table exists
on the volume, which may be in either compressed or uncompressed format.

#### Recommended Up-case Table

When formatting a volume, implementations should record the recommended
up-case table in compressed format (see Table 25), for which the value
of the TableChecksum field is E619D30Dh.

If an implementation defines its own up-case table, either compressed or
uncompressed, then that table shall cover the complete Unicode character
range (from character codes 0000h to FFFFh inclusive).

**Recommended Up-case Table in Compressed Format**
<table>
<thead>
<tr class="header">
<th><strong>Raw Offset</strong></th>
<th><strong>Compressed Table Entries</strong></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><strong>+ 0</strong></td>
<td><strong>+ 1</strong></td>
<td><strong>+ 2</strong></td>
<td><strong>+ 3</strong></td>
<td><strong>+ 4</strong></td>
<td><strong>+ 5</strong></td>
<td><strong>+ 6</strong></td>
<td><strong>+ 7</strong></td>
</tr>
<tr class="even">
<td><strong>0000h</strong></td>
<td>0000h</td>
<td>0001h</td>
<td>0002h</td>
<td>0003h</td>
<td>0004h</td>
<td>0005h</td>
<td>0006h</td>
<td>0007h</td>
</tr>
<tr class="odd">
<td><strong>0008h</strong></td>
<td>0008h</td>
<td>0009h</td>
<td>000Ah</td>
<td>000Bh</td>
<td>000Ch</td>
<td>000Dh</td>
<td>000Eh</td>
<td>000Fh</td>
</tr>
<tr class="even">
<td><strong>0010h</strong></td>
<td>0010h</td>
<td>0011h</td>
<td>0012h</td>
<td>0013h</td>
<td>0014h</td>
<td>0015h</td>
<td>0016h</td>
<td>0017h</td>
</tr>
<tr class="odd">
<td><strong>0018h</strong></td>
<td>0018h</td>
<td>0019h</td>
<td>001Ah</td>
<td>001Bh</td>
<td>001Ch</td>
<td>001Dh</td>
<td>001Eh</td>
<td>001Fh</td>
</tr>
<tr class="even">
<td><strong>0020h</strong></td>
<td>0020h</td>
<td>0021h</td>
<td>0022h</td>
<td>0023h</td>
<td>0024h</td>
<td>0025h</td>
<td>0026h</td>
<td>0027h</td>
</tr>
<tr class="odd">
<td><strong>0028h</strong></td>
<td>0028h</td>
<td>0029h</td>
<td>002Ah</td>
<td>002Bh</td>
<td>002Ch</td>
<td>002Dh</td>
<td>002Eh</td>
<td>002Fh</td>
</tr>
<tr class="even">
<td><strong>0030h</strong></td>
<td>0030h</td>
<td>0031h</td>
<td>0032h</td>
<td>0033h</td>
<td>0034h</td>
<td>0035h</td>
<td>0036h</td>
<td>0037h</td>
</tr>
<tr class="odd">
<td><strong>0038h</strong></td>
<td>0038h</td>
<td>0039h</td>
<td>003Ah</td>
<td>003Bh</td>
<td>003Ch</td>
<td>003Dh</td>
<td>003Eh</td>
<td>003Fh</td>
</tr>
<tr class="even">
<td><strong>0040h</strong></td>
<td>0040h</td>
<td>0041h</td>
<td>0042h</td>
<td>0043h</td>
<td>0044h</td>
<td>0045h</td>
<td>0046h</td>
<td>0047h</td>
</tr>
<tr class="odd">
<td><strong>0048h</strong></td>
<td>0048h</td>
<td>0049h</td>
<td>004Ah</td>
<td>004Bh</td>
<td>004Ch</td>
<td>004Dh</td>
<td>004Eh</td>
<td>004Fh</td>
</tr>
<tr class="even">
<td><strong>0050h</strong></td>
<td>0050h</td>
<td>0051h</td>
<td>0052h</td>
<td>0053h</td>
<td>0054h</td>
<td>0055h</td>
<td>0056h</td>
<td>0057h</td>
</tr>
<tr class="odd">
<td><strong>0058h</strong></td>
<td>0058h</td>
<td>0059h</td>
<td>005Ah</td>
<td>005Bh</td>
<td>005Ch</td>
<td>005Dh</td>
<td>005Eh</td>
<td>005Fh</td>
</tr>
<tr class="even">
<td><strong>0060h</strong></td>
<td>0060h</td>
<td>0041h</td>
<td>0042h</td>
<td>0043h</td>
<td>0044h</td>
<td>0045h</td>
<td>0046h</td>
<td>0047h</td>
</tr>
<tr class="odd">
<td><strong>0068h</strong></td>
<td>0048h</td>
<td>0049h</td>
<td>004Ah</td>
<td>004Bh</td>
<td>004Ch</td>
<td>004Dh</td>
<td>004Eh</td>
<td>004Fh</td>
</tr>
<tr class="even">
<td><strong>0070h</strong></td>
<td>0050h</td>
<td>0051h</td>
<td>0052h</td>
<td>0053h</td>
<td>0054h</td>
<td>0055h</td>
<td>0056h</td>
<td>0057h</td>
</tr>
<tr class="odd">
<td><strong>0078h</strong></td>
<td>0058h</td>
<td>0059h</td>
<td>005Ah</td>
<td>007Bh</td>
<td>007Ch</td>
<td>007Dh</td>
<td>007Eh</td>
<td>007Fh</td>
</tr>
<tr class="even">
<td><strong>0080h</strong></td>
<td>0080h</td>
<td>0081h</td>
<td>0082h</td>
<td>0083h</td>
<td>0084h</td>
<td>0085h</td>
<td>0086h</td>
<td>0087h</td>
</tr>
<tr class="odd">
<td><strong>0088h</strong></td>
<td>0088h</td>
<td>0089h</td>
<td>008Ah</td>
<td>008Bh</td>
<td>008Ch</td>
<td>008Dh</td>
<td>008Eh</td>
<td>008Fh</td>
</tr>
<tr class="even">
<td><strong>0090h</strong></td>
<td>0090h</td>
<td>0091h</td>
<td>0092h</td>
<td>0093h</td>
<td>0094h</td>
<td>0095h</td>
<td>0096h</td>
<td>0097h</td>
</tr>
<tr class="odd">
<td><strong>0098h</strong></td>
<td>0098h</td>
<td>0099h</td>
<td>009Ah</td>
<td>009Bh</td>
<td>009Ch</td>
<td>009Dh</td>
<td>009Eh</td>
<td>009Fh</td>
</tr>
<tr class="even">
<td><strong>00A0h</strong></td>
<td>00A0h</td>
<td>00A1h</td>
<td>00A2h</td>
<td>00A3h</td>
<td>00A4h</td>
<td>00A5h</td>
<td>00A6h</td>
<td>00A7h</td>
</tr>
<tr class="odd">
<td><strong>00A8h</strong></td>
<td>00A8h</td>
<td>00A9h</td>
<td>00AAh</td>
<td>00ABh</td>
<td>00ACh</td>
<td>00ADh</td>
<td>00AEh</td>
<td>00AFh</td>
</tr>
<tr class="even">
<td><strong>00B0h</strong></td>
<td>00B0h</td>
<td>00B1h</td>
<td>00B2h</td>
<td>00B3h</td>
<td>00B4h</td>
<td>00B5h</td>
<td>00B6h</td>
<td>00B7h</td>
</tr>
<tr class="odd">
<td><strong>00B8h</strong></td>
<td>00B8h</td>
<td>00B9h</td>
<td>00BAh</td>
<td>00BBh</td>
<td>00BCh</td>
<td>00BDh</td>
<td>00BEh</td>
<td>00BFh</td>
</tr>
<tr class="even">
<td><strong>00C0h</strong></td>
<td>00C0h</td>
<td>00C1h</td>
<td>00C2h</td>
<td>00C3h</td>
<td>00C4h</td>
<td>00C5h</td>
<td>00C6h</td>
<td>00C7h</td>
</tr>
<tr class="odd">
<td><strong>00C8h</strong></td>
<td>00C8h</td>
<td>00C9h</td>
<td>00CAh</td>
<td>00CBh</td>
<td>00CCh</td>
<td>00CDh</td>
<td>00CEh</td>
<td>00CFh</td>
</tr>
<tr class="even">
<td><strong>00D0h</strong></td>
<td>00D0h</td>
<td>00D1h</td>
<td>00D2h</td>
<td>00D3h</td>
<td>00D4h</td>
<td>00D5h</td>
<td>00D6h</td>
<td>00D7h</td>
</tr>
<tr class="odd">
<td><strong>00D8h</strong></td>
<td>00D8h</td>
<td>00D9h</td>
<td>00DAh</td>
<td>00DBh</td>
<td>00DCh</td>
<td>00DDh</td>
<td>00DEh</td>
<td>00DFh</td>
</tr>
<tr class="even">
<td><strong>00E0h</strong></td>
<td>00C0h</td>
<td>00C1h</td>
<td>00C2h</td>
<td>00C3h</td>
<td>00C4h</td>
<td>00C5h</td>
<td>00C6h</td>
<td>00C7h</td>
</tr>
<tr class="odd">
<td><strong>00E8h</strong></td>
<td>00C8h</td>
<td>00C9h</td>
<td>00CAh</td>
<td>00CBh</td>
<td>00CCh</td>
<td>00CDh</td>
<td>00CEh</td>
<td>00CFh</td>
</tr>
<tr class="even">
<td><strong>00F0h</strong></td>
<td>00D0h</td>
<td>00D1h</td>
<td>00D2h</td>
<td>00D3h</td>
<td>00D4h</td>
<td>00D5h</td>
<td>00D6h</td>
<td>00F7h</td>
</tr>
<tr class="odd">
<td><strong>00F8h</strong></td>
<td>00D8h</td>
<td>00D9h</td>
<td>00DAh</td>
<td>00DBh</td>
<td>00DCh</td>
<td>00DDh</td>
<td>00DEh</td>
<td>0178h</td>
</tr>
<tr class="even">
<td><strong>0100h</strong></td>
<td>0100h</td>
<td>0100h</td>
<td>0102h</td>
<td>0102h</td>
<td>0104h</td>
<td>0104h</td>
<td>0106h</td>
<td>0106h</td>
</tr>
<tr class="odd">
<td><strong>0108h</strong></td>
<td>0108h</td>
<td>0108h</td>
<td>010Ah</td>
<td>010Ah</td>
<td>010Ch</td>
<td>010Ch</td>
<td>010Eh</td>
<td>010Eh</td>
</tr>
<tr class="even">
<td><strong>0110h</strong></td>
<td>0110h</td>
<td>0110h</td>
<td>0112h</td>
<td>0112h</td>
<td>0114h</td>
<td>0114h</td>
<td>0116h</td>
<td>0116h</td>
</tr>
<tr class="odd">
<td><strong>0118h</strong></td>
<td>0118h</td>
<td>0118h</td>
<td>011Ah</td>
<td>011Ah</td>
<td>011Ch</td>
<td>011Ch</td>
<td>011Eh</td>
<td>011Eh</td>
</tr>
<tr class="even">
<td><strong>0120h</strong></td>
<td>0120h</td>
<td>0120h</td>
<td>0122h</td>
<td>0122h</td>
<td>0124h</td>
<td>0124h</td>
<td>0126h</td>
<td>0126h</td>
</tr>
<tr class="odd">
<td><strong>0128h</strong></td>
<td>0128h</td>
<td>0128h</td>
<td>012Ah</td>
<td>012Ah</td>
<td>012Ch</td>
<td>012Ch</td>
<td>012Eh</td>
<td>012Eh</td>
</tr>
<tr class="even">
<td><strong>0130h</strong></td>
<td>0130h</td>
<td>0131h</td>
<td>0132h</td>
<td>0132h</td>
<td>0134h</td>
<td>0134h</td>
<td>0136h</td>
<td>0136h</td>
</tr>
<tr class="odd">
<td><strong>0138h</strong></td>
<td>0138h</td>
<td>0139h</td>
<td>0139h</td>
<td>013Bh</td>
<td>013Bh</td>
<td>013Dh</td>
<td>013Dh</td>
<td>013Fh</td>
</tr>
<tr class="even">
<td><strong>0140h</strong></td>
<td>013Fh</td>
<td>0141h</td>
<td>0141h</td>
<td>0143h</td>
<td>0143h</td>
<td>0145h</td>
<td>0145h</td>
<td>0147h</td>
</tr>
<tr class="odd">
<td><strong>0148h</strong></td>
<td>0147h</td>
<td>0149h</td>
<td>014Ah</td>
<td>014Ah</td>
<td>014Ch</td>
<td>014Ch</td>
<td>014Eh</td>
<td>014Eh</td>
</tr>
<tr class="even">
<td><strong>0150h</strong></td>
<td>0150h</td>
<td>0150h</td>
<td>0152h</td>
<td>0152h</td>
<td>0154h</td>
<td>0154h</td>
<td>0156h</td>
<td>0156h</td>
</tr>
<tr class="odd">
<td><strong>0158h</strong></td>
<td>0158h</td>
<td>0158h</td>
<td>015Ah</td>
<td>015Ah</td>
<td>015Ch</td>
<td>015Ch</td>
<td>015Eh</td>
<td>015Eh</td>
</tr>
<tr class="even">
<td><strong>0160h</strong></td>
<td>0160h</td>
<td>0160h</td>
<td>0162h</td>
<td>0162h</td>
<td>0164h</td>
<td>0164h</td>
<td>0166h</td>
<td>0166h</td>
</tr>
<tr class="odd">
<td><strong>0168h</strong></td>
<td>0168h</td>
<td>0168h</td>
<td>016Ah</td>
<td>016Ah</td>
<td>016Ch</td>
<td>016Ch</td>
<td>016Eh</td>
<td>016Eh</td>
</tr>
<tr class="even">
<td><strong>0170h</strong></td>
<td>0170h</td>
<td>0170h</td>
<td>0172h</td>
<td>0172h</td>
<td>0174h</td>
<td>0174h</td>
<td>0176h</td>
<td>0176h</td>
</tr>
<tr class="odd">
<td><strong>0178h</strong></td>
<td>0178h</td>
<td>0179h</td>
<td>0179h</td>
<td>017Bh</td>
<td>017Bh</td>
<td>017Dh</td>
<td>017Dh</td>
<td>017Fh</td>
</tr>
<tr class="even">
<td><strong>0180h</strong></td>
<td>0243h</td>
<td>0181h</td>
<td>0182h</td>
<td>0182h</td>
<td>0184h</td>
<td>0184h</td>
<td>0186h</td>
<td>0187h</td>
</tr>
<tr class="odd">
<td><strong>0188h</strong></td>
<td>0187h</td>
<td>0189h</td>
<td>018Ah</td>
<td>018Bh</td>
<td>018Bh</td>
<td>018Dh</td>
<td>018Eh</td>
<td>018Fh</td>
</tr>
<tr class="even">
<td><strong>0190h</strong></td>
<td>0190h</td>
<td>0191h</td>
<td>0191h</td>
<td>0193h</td>
<td>0194h</td>
<td>01F6h</td>
<td>0196h</td>
<td>0197h</td>
</tr>
<tr class="odd">
<td><strong>0198h</strong></td>
<td>0198h</td>
<td>0198h</td>
<td>023Dh</td>
<td>019Bh</td>
<td>019Ch</td>
<td>019Dh</td>
<td>0220h</td>
<td>019Fh</td>
</tr>
<tr class="even">
<td><strong>01A0h</strong></td>
<td>01A0h</td>
<td>01A0h</td>
<td>01A2h</td>
<td>01A2h</td>
<td>01A4h</td>
<td>01A4h</td>
<td>01A6h</td>
<td>01A7h</td>
</tr>
<tr class="odd">
<td><strong>01A8h</strong></td>
<td>01A7h</td>
<td>01A9h</td>
<td>01AAh</td>
<td>01ABh</td>
<td>01ACh</td>
<td>01ACh</td>
<td>01AEh</td>
<td>01AFh</td>
</tr>
<tr class="even">
<td><strong>01B0h</strong></td>
<td>01AFh</td>
<td>01B1h</td>
<td>01B2h</td>
<td>01B3h</td>
<td>01B3h</td>
<td>01B5h</td>
<td>01B5h</td>
<td>01B7h</td>
</tr>
<tr class="odd">
<td><strong>01B8h</strong></td>
<td>01B8h</td>
<td>01B8h</td>
<td>01BAh</td>
<td>01BBh</td>
<td>01BCh</td>
<td>01BCh</td>
<td>01BEh</td>
<td>01F7h</td>
</tr>
<tr class="even">
<td><strong>01C0h</strong></td>
<td>01C0h</td>
<td>01C1h</td>
<td>01C2h</td>
<td>01C3h</td>
<td>01C4h</td>
<td>01C5h</td>
<td>01C4h</td>
<td>01C7h</td>
</tr>
<tr class="odd">
<td><strong>01C8h</strong></td>
<td>01C8h</td>
<td>01C7h</td>
<td>01CAh</td>
<td>01CBh</td>
<td>01CAh</td>
<td>01CDh</td>
<td>01CDh</td>
<td>01CFh</td>
</tr>
<tr class="even">
<td><strong>01D0h</strong></td>
<td>01CFh</td>
<td>01D1h</td>
<td>01D1h</td>
<td>01D3h</td>
<td>01D3h</td>
<td>01D5h</td>
<td>01D5h</td>
<td>01D7h</td>
</tr>
<tr class="odd">
<td><strong>01D8h</strong></td>
<td>01D7h</td>
<td>01D9h</td>
<td>01D9h</td>
<td>01DBh</td>
<td>01DBh</td>
<td>018Eh</td>
<td>01DEh</td>
<td>01DEh</td>
</tr>
<tr class="even">
<td><strong>01E0h</strong></td>
<td>01E0h</td>
<td>01E0h</td>
<td>01E2h</td>
<td>01E2h</td>
<td>01E4h</td>
<td>01E4h</td>
<td>01E6h</td>
<td>01E6h</td>
</tr>
<tr class="odd">
<td><strong>01E8h</strong></td>
<td>01E8h</td>
<td>01E8h</td>
<td>01EAh</td>
<td>01EAh</td>
<td>01ECh</td>
<td>01ECh</td>
<td>01EEh</td>
<td>01EEh</td>
</tr>
<tr class="even">
<td><strong>01F0h</strong></td>
<td>01F0h</td>
<td>01F1h</td>
<td>01F2h</td>
<td>01F1h</td>
<td>01F4h</td>
<td>01F4h</td>
<td>01F6h</td>
<td>01F7h</td>
</tr>
<tr class="odd">
<td><strong>01F8h</strong></td>
<td>01F8h</td>
<td>01F8h</td>
<td>01FAh</td>
<td>01FAh</td>
<td>01FCh</td>
<td>01FCh</td>
<td>01FEh</td>
<td>01FEh</td>
</tr>
<tr class="even">
<td><strong>0200h</strong></td>
<td>0200h</td>
<td>0200h</td>
<td>0202h</td>
<td>0202h</td>
<td>0204h</td>
<td>0204h</td>
<td>0206h</td>
<td>0206h</td>
</tr>
<tr class="odd">
<td><strong>0208h</strong></td>
<td>0208h</td>
<td>0208h</td>
<td>020Ah</td>
<td>020Ah</td>
<td>020Ch</td>
<td>020Ch</td>
<td>020Eh</td>
<td>020Eh</td>
</tr>
<tr class="even">
<td><strong>0210h</strong></td>
<td>0210h</td>
<td>0210h</td>
<td>0212h</td>
<td>0212h</td>
<td>0214h</td>
<td>0214h</td>
<td>0216h</td>
<td>0216h</td>
</tr>
<tr class="odd">
<td><strong>0218h</strong></td>
<td>0218h</td>
<td>0218h</td>
<td>021Ah</td>
<td>021Ah</td>
<td>021Ch</td>
<td>021Ch</td>
<td>021Eh</td>
<td>021Eh</td>
</tr>
<tr class="even">
<td><strong>0220h</strong></td>
<td>0220h</td>
<td>0221h</td>
<td>0222h</td>
<td>0222h</td>
<td>0224h</td>
<td>0224h</td>
<td>0226h</td>
<td>0226h</td>
</tr>
<tr class="odd">
<td><strong>0228h</strong></td>
<td>0228h</td>
<td>0228h</td>
<td>022Ah</td>
<td>022Ah</td>
<td>022Ch</td>
<td>022Ch</td>
<td>022Eh</td>
<td>022Eh</td>
</tr>
<tr class="even">
<td><strong>0230h</strong></td>
<td>0230h</td>
<td>0230h</td>
<td>0232h</td>
<td>0232h</td>
<td>0234h</td>
<td>0235h</td>
<td>0236h</td>
<td>0237h</td>
</tr>
<tr class="odd">
<td><strong>0238h</strong></td>
<td>0238h</td>
<td>0239h</td>
<td>2C65h</td>
<td>023Bh</td>
<td>023Bh</td>
<td>023Dh</td>
<td>2C66h</td>
<td>023Fh</td>
</tr>
<tr class="even">
<td><strong>0240h</strong></td>
<td>0240h</td>
<td>0241h</td>
<td>0241h</td>
<td>0243h</td>
<td>0244h</td>
<td>0245h</td>
<td>0246h</td>
<td>0246h</td>
</tr>
<tr class="odd">
<td><strong>0248h</strong></td>
<td>0248h</td>
<td>0248h</td>
<td>024Ah</td>
<td>024Ah</td>
<td>024Ch</td>
<td>024Ch</td>
<td>024Eh</td>
<td>024Eh</td>
</tr>
<tr class="even">
<td><strong>0250h</strong></td>
<td>0250h</td>
<td>0251h</td>
<td>0252h</td>
<td>0181h</td>
<td>0186h</td>
<td>0255h</td>
<td>0189h</td>
<td>018Ah</td>
</tr>
<tr class="odd">
<td><strong>0258h</strong></td>
<td>0258h</td>
<td>018Fh</td>
<td>025Ah</td>
<td>0190h</td>
<td>025Ch</td>
<td>025Dh</td>
<td>025Eh</td>
<td>025Fh</td>
</tr>
<tr class="even">
<td><strong>0260h</strong></td>
<td>0193h</td>
<td>0261h</td>
<td>0262h</td>
<td>0194h</td>
<td>0264h</td>
<td>0265h</td>
<td>0266h</td>
<td>0267h</td>
</tr>
<tr class="odd">
<td><strong>0268h</strong></td>
<td>0197h</td>
<td>0196h</td>
<td>026Ah</td>
<td>2C62h</td>
<td>026Ch</td>
<td>026Dh</td>
<td>026Eh</td>
<td>019Ch</td>
</tr>
<tr class="even">
<td><strong>0270h</strong></td>
<td>0270h</td>
<td>0271h</td>
<td>019Dh</td>
<td>0273h</td>
<td>0274h</td>
<td>019Fh</td>
<td>0276h</td>
<td>0277h</td>
</tr>
<tr class="odd">
<td><strong>0278h</strong></td>
<td>0278h</td>
<td>0279h</td>
<td>027Ah</td>
<td>027Bh</td>
<td>027Ch</td>
<td>2C64h</td>
<td>027Eh</td>
<td>027Fh</td>
</tr>
<tr class="even">
<td><strong>0280h</strong></td>
<td>01A6h</td>
<td>0281h</td>
<td>0282h</td>
<td>01A9h</td>
<td>0284h</td>
<td>0285h</td>
<td>0286h</td>
<td>0287h</td>
</tr>
<tr class="odd">
<td><strong>0288h</strong></td>
<td>01AEh</td>
<td>0244h</td>
<td>01B1h</td>
<td>01B2h</td>
<td>0245h</td>
<td>028Dh</td>
<td>028Eh</td>
<td>028Fh</td>
</tr>
<tr class="even">
<td><strong>0290h</strong></td>
<td>0290h</td>
<td>0291h</td>
<td>01B7h</td>
<td>0293h</td>
<td>0294h</td>
<td>0295h</td>
<td>0296h</td>
<td>0297h</td>
</tr>
<tr class="odd">
<td><strong>0298h</strong></td>
<td>0298h</td>
<td>0299h</td>
<td>029Ah</td>
<td>029Bh</td>
<td>029Ch</td>
<td>029Dh</td>
<td>029Eh</td>
<td>029Fh</td>
</tr>
<tr class="even">
<td><strong>02A0h</strong></td>
<td>02A0h</td>
<td>02A1h</td>
<td>02A2h</td>
<td>02A3h</td>
<td>02A4h</td>
<td>02A5h</td>
<td>02A6h</td>
<td>02A7h</td>
</tr>
<tr class="odd">
<td><strong>02A8h</strong></td>
<td>02A8h</td>
<td>02A9h</td>
<td>02AAh</td>
<td>02ABh</td>
<td>02ACh</td>
<td>02ADh</td>
<td>02AEh</td>
<td>02AFh</td>
</tr>
<tr class="even">
<td><strong>02B0h</strong></td>
<td>02B0h</td>
<td>02B1h</td>
<td>02B2h</td>
<td>02B3h</td>
<td>02B4h</td>
<td>02B5h</td>
<td>02B6h</td>
<td>02B7h</td>
</tr>
<tr class="odd">
<td><strong>02B8h</strong></td>
<td>02B8h</td>
<td>02B9h</td>
<td>02BAh</td>
<td>02BBh</td>
<td>02BCh</td>
<td>02BDh</td>
<td>02BEh</td>
<td>02BFh</td>
</tr>
<tr class="even">
<td><strong>02C0h</strong></td>
<td>02C0h</td>
<td>02C1h</td>
<td>02C2h</td>
<td>02C3h</td>
<td>02C4h</td>
<td>02C5h</td>
<td>02C6h</td>
<td>02C7h</td>
</tr>
<tr class="odd">
<td><strong>02C8h</strong></td>
<td>02C8h</td>
<td>02C9h</td>
<td>02CAh</td>
<td>02CBh</td>
<td>02CCh</td>
<td>02CDh</td>
<td>02CEh</td>
<td>02CFh</td>
</tr>
<tr class="even">
<td><strong>02D0h</strong></td>
<td>02D0h</td>
<td>02D1h</td>
<td>02D2h</td>
<td>02D3h</td>
<td>02D4h</td>
<td>02D5h</td>
<td>02D6h</td>
<td>02D7h</td>
</tr>
<tr class="odd">
<td><strong>02D8h</strong></td>
<td>02D8h</td>
<td>02D9h</td>
<td>02DAh</td>
<td>02DBh</td>
<td>02DCh</td>
<td>02DDh</td>
<td>02DEh</td>
<td>02DFh</td>
</tr>
<tr class="even">
<td><strong>02E0h</strong></td>
<td>02E0h</td>
<td>02E1h</td>
<td>02E2h</td>
<td>02E3h</td>
<td>02E4h</td>
<td>02E5h</td>
<td>02E6h</td>
<td>02E7h</td>
</tr>
<tr class="odd">
<td><strong>02E8h</strong></td>
<td>02E8h</td>
<td>02E9h</td>
<td>02EAh</td>
<td>02EBh</td>
<td>02ECh</td>
<td>02EDh</td>
<td>02EEh</td>
<td>02EFh</td>
</tr>
<tr class="even">
<td><strong>02F0h</strong></td>
<td>02F0h</td>
<td>02F1h</td>
<td>02F2h</td>
<td>02F3h</td>
<td>02F4h</td>
<td>02F5h</td>
<td>02F6h</td>
<td>02F7h</td>
</tr>
<tr class="odd">
<td><strong>02F8h</strong></td>
<td>02F8h</td>
<td>02F9h</td>
<td>02FAh</td>
<td>02FBh</td>
<td>02FCh</td>
<td>02FDh</td>
<td>02FEh</td>
<td>02FFh</td>
</tr>
<tr class="even">
<td><strong>0300h</strong></td>
<td>0300h</td>
<td>0301h</td>
<td>0302h</td>
<td>0303h</td>
<td>0304h</td>
<td>0305h</td>
<td>0306h</td>
<td>0307h</td>
</tr>
<tr class="odd">
<td><strong>0308h</strong></td>
<td>0308h</td>
<td>0309h</td>
<td>030Ah</td>
<td>030Bh</td>
<td>030Ch</td>
<td>030Dh</td>
<td>030Eh</td>
<td>030Fh</td>
</tr>
<tr class="even">
<td><strong>0310h</strong></td>
<td>0310h</td>
<td>0311h</td>
<td>0312h</td>
<td>0313h</td>
<td>0314h</td>
<td>0315h</td>
<td>0316h</td>
<td>0317h</td>
</tr>
<tr class="odd">
<td><strong>0318h</strong></td>
<td>0318h</td>
<td>0319h</td>
<td>031Ah</td>
<td>031Bh</td>
<td>031Ch</td>
<td>031Dh</td>
<td>031Eh</td>
<td>031Fh</td>
</tr>
<tr class="even">
<td><strong>0320h</strong></td>
<td>0320h</td>
<td>0321h</td>
<td>0322h</td>
<td>0323h</td>
<td>0324h</td>
<td>0325h</td>
<td>0326h</td>
<td>0327h</td>
</tr>
<tr class="odd">
<td><strong>0328h</strong></td>
<td>0328h</td>
<td>0329h</td>
<td>032Ah</td>
<td>032Bh</td>
<td>032Ch</td>
<td>032Dh</td>
<td>032Eh</td>
<td>032Fh</td>
</tr>
<tr class="even">
<td><strong>0330h</strong></td>
<td>0330h</td>
<td>0331h</td>
<td>0332h</td>
<td>0333h</td>
<td>0334h</td>
<td>0335h</td>
<td>0336h</td>
<td>0337h</td>
</tr>
<tr class="odd">
<td><strong>0338h</strong></td>
<td>0338h</td>
<td>0339h</td>
<td>033Ah</td>
<td>033Bh</td>
<td>033Ch</td>
<td>033Dh</td>
<td>033Eh</td>
<td>033Fh</td>
</tr>
<tr class="even">
<td><strong>0340h</strong></td>
<td>0340h</td>
<td>0341h</td>
<td>0342h</td>
<td>0343h</td>
<td>0344h</td>
<td>0345h</td>
<td>0346h</td>
<td>0347h</td>
</tr>
<tr class="odd">
<td><strong>0348h</strong></td>
<td>0348h</td>
<td>0349h</td>
<td>034Ah</td>
<td>034Bh</td>
<td>034Ch</td>
<td>034Dh</td>
<td>034Eh</td>
<td>034Fh</td>
</tr>
<tr class="even">
<td><strong>0350h</strong></td>
<td>0350h</td>
<td>0351h</td>
<td>0352h</td>
<td>0353h</td>
<td>0354h</td>
<td>0355h</td>
<td>0356h</td>
<td>0357h</td>
</tr>
<tr class="odd">
<td><strong>0358h</strong></td>
<td>0358h</td>
<td>0359h</td>
<td>035Ah</td>
<td>035Bh</td>
<td>035Ch</td>
<td>035Dh</td>
<td>035Eh</td>
<td>035Fh</td>
</tr>
<tr class="even">
<td><strong>0360h</strong></td>
<td>0360h</td>
<td>0361h</td>
<td>0362h</td>
<td>0363h</td>
<td>0364h</td>
<td>0365h</td>
<td>0366h</td>
<td>0367h</td>
</tr>
<tr class="odd">
<td><strong>0368h</strong></td>
<td>0368h</td>
<td>0369h</td>
<td>036Ah</td>
<td>036Bh</td>
<td>036Ch</td>
<td>036Dh</td>
<td>036Eh</td>
<td>036Fh</td>
</tr>
<tr class="even">
<td><strong>0370h</strong></td>
<td>0370h</td>
<td>0371h</td>
<td>0372h</td>
<td>0373h</td>
<td>0374h</td>
<td>0375h</td>
<td>0376h</td>
<td>0377h</td>
</tr>
<tr class="odd">
<td><strong>0378h</strong></td>
<td>0378h</td>
<td>0379h</td>
<td>037Ah</td>
<td>03FDh</td>
<td>03FEh</td>
<td>03FFh</td>
<td>037Eh</td>
<td>037Fh</td>
</tr>
<tr class="even">
<td><strong>0380h</strong></td>
<td>0380h</td>
<td>0381h</td>
<td>0382h</td>
<td>0383h</td>
<td>0384h</td>
<td>0385h</td>
<td>0386h</td>
<td>0387h</td>
</tr>
<tr class="odd">
<td><strong>0388h</strong></td>
<td>0388h</td>
<td>0389h</td>
<td>038Ah</td>
<td>038Bh</td>
<td>038Ch</td>
<td>038Dh</td>
<td>038Eh</td>
<td>038Fh</td>
</tr>
<tr class="even">
<td><strong>0390h</strong></td>
<td>0390h</td>
<td>0391h</td>
<td>0392h</td>
<td>0393h</td>
<td>0394h</td>
<td>0395h</td>
<td>0396h</td>
<td>0397h</td>
</tr>
<tr class="odd">
<td><strong>0398h</strong></td>
<td>0398h</td>
<td>0399h</td>
<td>039Ah</td>
<td>039Bh</td>
<td>039Ch</td>
<td>039Dh</td>
<td>039Eh</td>
<td>039Fh</td>
</tr>
<tr class="even">
<td><strong>03A0h</strong></td>
<td>03A0h</td>
<td>03A1h</td>
<td>03A2h</td>
<td>03A3h</td>
<td>03A4h</td>
<td>03A5h</td>
<td>03A6h</td>
<td>03A7h</td>
</tr>
<tr class="odd">
<td><strong>03A8h</strong></td>
<td>03A8h</td>
<td>03A9h</td>
<td>03AAh</td>
<td>03ABh</td>
<td>0386h</td>
<td>0388h</td>
<td>0389h</td>
<td>038Ah</td>
</tr>
<tr class="even">
<td><strong>03B0h</strong></td>
<td>03B0h</td>
<td>0391h</td>
<td>0392h</td>
<td>0393h</td>
<td>0394h</td>
<td>0395h</td>
<td>0396h</td>
<td>0397h</td>
</tr>
<tr class="odd">
<td><strong>03B8h</strong></td>
<td>0398h</td>
<td>0399h</td>
<td>039Ah</td>
<td>039Bh</td>
<td>039Ch</td>
<td>039Dh</td>
<td>039Eh</td>
<td>039Fh</td>
</tr>
<tr class="even">
<td><strong>03C0h</strong></td>
<td>03A0h</td>
<td>03A1h</td>
<td>03A3h</td>
<td>03A3h</td>
<td>03A4h</td>
<td>03A5h</td>
<td>03A6h</td>
<td>03A7h</td>
</tr>
<tr class="odd">
<td><strong>03C8h</strong></td>
<td>03A8h</td>
<td>03A9h</td>
<td>03AAh</td>
<td>03ABh</td>
<td>038Ch</td>
<td>038Eh</td>
<td>038Fh</td>
<td>03CFh</td>
</tr>
<tr class="even">
<td><strong>03D0h</strong></td>
<td>03D0h</td>
<td>03D1h</td>
<td>03D2h</td>
<td>03D3h</td>
<td>03D4h</td>
<td>03D5h</td>
<td>03D6h</td>
<td>03D7h</td>
</tr>
<tr class="odd">
<td><strong>03D8h</strong></td>
<td>03D8h</td>
<td>03D8h</td>
<td>03DAh</td>
<td>03DAh</td>
<td>03DCh</td>
<td>03DCh</td>
<td>03DEh</td>
<td>03DEh</td>
</tr>
<tr class="even">
<td><strong>03E0h</strong></td>
<td>03E0h</td>
<td>03E0h</td>
<td>03E2h</td>
<td>03E2h</td>
<td>03E4h</td>
<td>03E4h</td>
<td>03E6h</td>
<td>03E6h</td>
</tr>
<tr class="odd">
<td><strong>03E8h</strong></td>
<td>03E8h</td>
<td>03E8h</td>
<td>03EAh</td>
<td>03EAh</td>
<td>03ECh</td>
<td>03ECh</td>
<td>03EEh</td>
<td>03EEh</td>
</tr>
<tr class="even">
<td><strong>03F0h</strong></td>
<td>03F0h</td>
<td>03F1h</td>
<td>03F9h</td>
<td>03F3h</td>
<td>03F4h</td>
<td>03F5h</td>
<td>03F6h</td>
<td>03F7h</td>
</tr>
<tr class="odd">
<td><strong>03F8h</strong></td>
<td>03F7h</td>
<td>03F9h</td>
<td>03FAh</td>
<td>03FAh</td>
<td>03FCh</td>
<td>03FDh</td>
<td>03FEh</td>
<td>03FFh</td>
</tr>
<tr class="even">
<td><strong>0400h</strong></td>
<td>0400h</td>
<td>0401h</td>
<td>0402h</td>
<td>0403h</td>
<td>0404h</td>
<td>0405h</td>
<td>0406h</td>
<td>0407h</td>
</tr>
<tr class="odd">
<td><strong>0408h</strong></td>
<td>0408h</td>
<td>0409h</td>
<td>040Ah</td>
<td>040Bh</td>
<td>040Ch</td>
<td>040Dh</td>
<td>040Eh</td>
<td>040Fh</td>
</tr>
<tr class="even">
<td><strong>0410h</strong></td>
<td>0410h</td>
<td>0411h</td>
<td>0412h</td>
<td>0413h</td>
<td>0414h</td>
<td>0415h</td>
<td>0416h</td>
<td>0417h</td>
</tr>
<tr class="odd">
<td><strong>0418h</strong></td>
<td>0418h</td>
<td>0419h</td>
<td>041Ah</td>
<td>041Bh</td>
<td>041Ch</td>
<td>041Dh</td>
<td>041Eh</td>
<td>041Fh</td>
</tr>
<tr class="even">
<td><strong>0420h</strong></td>
<td>0420h</td>
<td>0421h</td>
<td>0422h</td>
<td>0423h</td>
<td>0424h</td>
<td>0425h</td>
<td>0426h</td>
<td>0427h</td>
</tr>
<tr class="odd">
<td><strong>0428h</strong></td>
<td>0428h</td>
<td>0429h</td>
<td>042Ah</td>
<td>042Bh</td>
<td>042Ch</td>
<td>042Dh</td>
<td>042Eh</td>
<td>042Fh</td>
</tr>
<tr class="even">
<td><strong>0430h</strong></td>
<td>0410h</td>
<td>0411h</td>
<td>0412h</td>
<td>0413h</td>
<td>0414h</td>
<td>0415h</td>
<td>0416h</td>
<td>0417h</td>
</tr>
<tr class="odd">
<td><strong>0438h</strong></td>
<td>0418h</td>
<td>0419h</td>
<td>041Ah</td>
<td>041Bh</td>
<td>041Ch</td>
<td>041Dh</td>
<td>041Eh</td>
<td>041Fh</td>
</tr>
<tr class="even">
<td><strong>0440h</strong></td>
<td>0420h</td>
<td>0421h</td>
<td>0422h</td>
<td>0423h</td>
<td>0424h</td>
<td>0425h</td>
<td>0426h</td>
<td>0427h</td>
</tr>
<tr class="odd">
<td><strong>0448h</strong></td>
<td>0428h</td>
<td>0429h</td>
<td>042Ah</td>
<td>042Bh</td>
<td>042Ch</td>
<td>042Dh</td>
<td>042Eh</td>
<td>042Fh</td>
</tr>
<tr class="even">
<td><strong>0450h</strong></td>
<td>0400h</td>
<td>0401h</td>
<td>0402h</td>
<td>0403h</td>
<td>0404h</td>
<td>0405h</td>
<td>0406h</td>
<td>0407h</td>
</tr>
<tr class="odd">
<td><strong>0458h</strong></td>
<td>0408h</td>
<td>0409h</td>
<td>040Ah</td>
<td>040Bh</td>
<td>040Ch</td>
<td>040Dh</td>
<td>040Eh</td>
<td>040Fh</td>
</tr>
<tr class="even">
<td><strong>0460h</strong></td>
<td>0460h</td>
<td>0460h</td>
<td>0462h</td>
<td>0462h</td>
<td>0464h</td>
<td>0464h</td>
<td>0466h</td>
<td>0466h</td>
</tr>
<tr class="odd">
<td><strong>0468h</strong></td>
<td>0468h</td>
<td>0468h</td>
<td>046Ah</td>
<td>046Ah</td>
<td>046Ch</td>
<td>046Ch</td>
<td>046Eh</td>
<td>046Eh</td>
</tr>
<tr class="even">
<td><strong>0470h</strong></td>
<td>0470h</td>
<td>0470h</td>
<td>0472h</td>
<td>0472h</td>
<td>0474h</td>
<td>0474h</td>
<td>0476h</td>
<td>0476h</td>
</tr>
<tr class="odd">
<td><strong>0478h</strong></td>
<td>0478h</td>
<td>0478h</td>
<td>047Ah</td>
<td>047Ah</td>
<td>047Ch</td>
<td>047Ch</td>
<td>047Eh</td>
<td>047Eh</td>
</tr>
<tr class="even">
<td><strong>0480h</strong></td>
<td>0480h</td>
<td>0480h</td>
<td>0482h</td>
<td>0483h</td>
<td>0484h</td>
<td>0485h</td>
<td>0486h</td>
<td>0487h</td>
</tr>
<tr class="odd">
<td><strong>0488h</strong></td>
<td>0488h</td>
<td>0489h</td>
<td>048Ah</td>
<td>048Ah</td>
<td>048Ch</td>
<td>048Ch</td>
<td>048Eh</td>
<td>048Eh</td>
</tr>
<tr class="even">
<td><strong>0490h</strong></td>
<td>0490h</td>
<td>0490h</td>
<td>0492h</td>
<td>0492h</td>
<td>0494h</td>
<td>0494h</td>
<td>0496h</td>
<td>0496h</td>
</tr>
<tr class="odd">
<td><strong>0498h</strong></td>
<td>0498h</td>
<td>0498h</td>
<td>049Ah</td>
<td>049Ah</td>
<td>049Ch</td>
<td>049Ch</td>
<td>049Eh</td>
<td>049Eh</td>
</tr>
<tr class="even">
<td><strong>04A0h</strong></td>
<td>04A0h</td>
<td>04A0h</td>
<td>04A2h</td>
<td>04A2h</td>
<td>04A4h</td>
<td>04A4h</td>
<td>04A6h</td>
<td>04A6h</td>
</tr>
<tr class="odd">
<td><strong>04A8h</strong></td>
<td>04A8h</td>
<td>04A8h</td>
<td>04AAh</td>
<td>04AAh</td>
<td>04ACh</td>
<td>04ACh</td>
<td>04AEh</td>
<td>04AEh</td>
</tr>
<tr class="even">
<td><strong>04B0h</strong></td>
<td>04B0h</td>
<td>04B0h</td>
<td>04B2h</td>
<td>04B2h</td>
<td>04B4h</td>
<td>04B4h</td>
<td>04B6h</td>
<td>04B6h</td>
</tr>
<tr class="odd">
<td><strong>04B8h</strong></td>
<td>04B8h</td>
<td>04B8h</td>
<td>04BAh</td>
<td>04BAh</td>
<td>04BCh</td>
<td>04BCh</td>
<td>04BEh</td>
<td>04BEh</td>
</tr>
<tr class="even">
<td><strong>04C0h</strong></td>
<td>04C0h</td>
<td>04C1h</td>
<td>04C1h</td>
<td>04C3h</td>
<td>04C3h</td>
<td>04C5h</td>
<td>04C5h</td>
<td>04C7h</td>
</tr>
<tr class="odd">
<td><strong>04C8h</strong></td>
<td>04C7h</td>
<td>04C9h</td>
<td>04C9h</td>
<td>04CBh</td>
<td>04CBh</td>
<td>04CDh</td>
<td>04CDh</td>
<td>04C0h</td>
</tr>
<tr class="even">
<td><strong>04D0h</strong></td>
<td>04D0h</td>
<td>04D0h</td>
<td>04D2h</td>
<td>04D2h</td>
<td>04D4h</td>
<td>04D4h</td>
<td>04D6h</td>
<td>04D6h</td>
</tr>
<tr class="odd">
<td><strong>04D8h</strong></td>
<td>04D8h</td>
<td>04D8h</td>
<td>04DAh</td>
<td>04DAh</td>
<td>04DCh</td>
<td>04DCh</td>
<td>04DEh</td>
<td>04DEh</td>
</tr>
<tr class="even">
<td><strong>04E0h</strong></td>
<td>04E0h</td>
<td>04E0h</td>
<td>04E2h</td>
<td>04E2h</td>
<td>04E4h</td>
<td>04E4h</td>
<td>04E6h</td>
<td>04E6h</td>
</tr>
<tr class="odd">
<td><strong>04E8h</strong></td>
<td>04E8h</td>
<td>04E8h</td>
<td>04EAh</td>
<td>04EAh</td>
<td>04ECh</td>
<td>04ECh</td>
<td>04EEh</td>
<td>04EEh</td>
</tr>
<tr class="even">
<td><strong>04F0h</strong></td>
<td>04F0h</td>
<td>04F0h</td>
<td>04F2h</td>
<td>04F2h</td>
<td>04F4h</td>
<td>04F4h</td>
<td>04F6h</td>
<td>04F6h</td>
</tr>
<tr class="odd">
<td><strong>04F8h</strong></td>
<td>04F8h</td>
<td>04F8h</td>
<td>04FAh</td>
<td>04FAh</td>
<td>04FCh</td>
<td>04FCh</td>
<td>04FEh</td>
<td>04FEh</td>
</tr>
<tr class="even">
<td><strong>0500h</strong></td>
<td>0500h</td>
<td>0500h</td>
<td>0502h</td>
<td>0502h</td>
<td>0504h</td>
<td>0504h</td>
<td>0506h</td>
<td>0506h</td>
</tr>
<tr class="odd">
<td><strong>0508h</strong></td>
<td>0508h</td>
<td>0508h</td>
<td>050Ah</td>
<td>050Ah</td>
<td>050Ch</td>
<td>050Ch</td>
<td>050Eh</td>
<td>050Eh</td>
</tr>
<tr class="even">
<td><strong>0510h</strong></td>
<td>0510h</td>
<td>0510h</td>
<td>0512h</td>
<td>0512h</td>
<td>0514h</td>
<td>0515h</td>
<td>0516h</td>
<td>0517h</td>
</tr>
<tr class="odd">
<td><strong>0518h</strong></td>
<td>0518h</td>
<td>0519h</td>
<td>051Ah</td>
<td>051Bh</td>
<td>051Ch</td>
<td>051Dh</td>
<td>051Eh</td>
<td>051Fh</td>
</tr>
<tr class="even">
<td><strong>0520h</strong></td>
<td>0520h</td>
<td>0521h</td>
<td>0522h</td>
<td>0523h</td>
<td>0524h</td>
<td>0525h</td>
<td>0526h</td>
<td>0527h</td>
</tr>
<tr class="odd">
<td><strong>0528h</strong></td>
<td>0528h</td>
<td>0529h</td>
<td>052Ah</td>
<td>052Bh</td>
<td>052Ch</td>
<td>052Dh</td>
<td>052Eh</td>
<td>052Fh</td>
</tr>
<tr class="even">
<td><strong>0530h</strong></td>
<td>0530h</td>
<td>0531h</td>
<td>0532h</td>
<td>0533h</td>
<td>0534h</td>
<td>0535h</td>
<td>0536h</td>
<td>0537h</td>
</tr>
<tr class="odd">
<td><strong>0538h</strong></td>
<td>0538h</td>
<td>0539h</td>
<td>053Ah</td>
<td>053Bh</td>
<td>053Ch</td>
<td>053Dh</td>
<td>053Eh</td>
<td>053Fh</td>
</tr>
<tr class="even">
<td><strong>0540h</strong></td>
<td>0540h</td>
<td>0541h</td>
<td>0542h</td>
<td>0543h</td>
<td>0544h</td>
<td>0545h</td>
<td>0546h</td>
<td>0547h</td>
</tr>
<tr class="odd">
<td><strong>0548h</strong></td>
<td>0548h</td>
<td>0549h</td>
<td>054Ah</td>
<td>054Bh</td>
<td>054Ch</td>
<td>054Dh</td>
<td>054Eh</td>
<td>054Fh</td>
</tr>
<tr class="even">
<td><strong>0550h</strong></td>
<td>0550h</td>
<td>0551h</td>
<td>0552h</td>
<td>0553h</td>
<td>0554h</td>
<td>0555h</td>
<td>0556h</td>
<td>0557h</td>
</tr>
<tr class="odd">
<td><strong>0558h</strong></td>
<td>0558h</td>
<td>0559h</td>
<td>055Ah</td>
<td>055Bh</td>
<td>055Ch</td>
<td>055Dh</td>
<td>055Eh</td>
<td>055Fh</td>
</tr>
<tr class="even">
<td><strong>0560h</strong></td>
<td>0560h</td>
<td>0531h</td>
<td>0532h</td>
<td>0533h</td>
<td>0534h</td>
<td>0535h</td>
<td>0536h</td>
<td>0537h</td>
</tr>
<tr class="odd">
<td><strong>0568h</strong></td>
<td>0538h</td>
<td>0539h</td>
<td>053Ah</td>
<td>053Bh</td>
<td>053Ch</td>
<td>053Dh</td>
<td>053Eh</td>
<td>053Fh</td>
</tr>
<tr class="even">
<td><strong>0570h</strong></td>
<td>0540h</td>
<td>0541h</td>
<td>0542h</td>
<td>0543h</td>
<td>0544h</td>
<td>0545h</td>
<td>0546h</td>
<td>0547h</td>
</tr>
<tr class="odd">
<td><strong>0578h</strong></td>
<td>0548h</td>
<td>0549h</td>
<td>054Ah</td>
<td>054Bh</td>
<td>054Ch</td>
<td>054Dh</td>
<td>054Eh</td>
<td>054Fh</td>
</tr>
<tr class="even">
<td><strong>0580h</strong></td>
<td>0550h</td>
<td>0551h</td>
<td>0552h</td>
<td>0553h</td>
<td>0554h</td>
<td>0555h</td>
<td>0556h</td>
<td>FFFFh</td>
</tr>
<tr class="odd">
<td><strong>0588h</strong></td>
<td>17F6h</td>
<td>2C63h</td>
<td>1D7Eh</td>
<td>1D7Fh</td>
<td>1D80h</td>
<td>1D81h</td>
<td>1D82h</td>
<td>1D83h</td>
</tr>
<tr class="even">
<td><strong>0590h</strong></td>
<td>1D84h</td>
<td>1D85h</td>
<td>1D86h</td>
<td>1D87h</td>
<td>1D88h</td>
<td>1D89h</td>
<td>1D8Ah</td>
<td>1D8Bh</td>
</tr>
<tr class="odd">
<td><strong>0598h</strong></td>
<td>1D8Ch</td>
<td>1D8Dh</td>
<td>1D8Eh</td>
<td>1D8Fh</td>
<td>1D90h</td>
<td>1D91h</td>
<td>1D92h</td>
<td>1D93h</td>
</tr>
<tr class="even">
<td><strong>05A0h</strong></td>
<td>1D94h</td>
<td>1D95h</td>
<td>1D96h</td>
<td>1D97h</td>
<td>1D98h</td>
<td>1D99h</td>
<td>1D9Ah</td>
<td>1D9Bh</td>
</tr>
<tr class="odd">
<td><strong>05A8h</strong></td>
<td>1D9Ch</td>
<td>1D9Dh</td>
<td>1D9Eh</td>
<td>1D9Fh</td>
<td>1DA0h</td>
<td>1DA1h</td>
<td>1DA2h</td>
<td>1DA3h</td>
</tr>
<tr class="even">
<td><strong>05B0h</strong></td>
<td>1DA4h</td>
<td>1DA5h</td>
<td>1DA6h</td>
<td>1DA7h</td>
<td>1DA8h</td>
<td>1DA9h</td>
<td>1DAAh</td>
<td>1DABh</td>
</tr>
<tr class="odd">
<td><strong>05B8h</strong></td>
<td>1DACh</td>
<td>1DADh</td>
<td>1DAEh</td>
<td>1DAFh</td>
<td>1DB0h</td>
<td>1DB1h</td>
<td>1DB2h</td>
<td>1DB3h</td>
</tr>
<tr class="even">
<td><strong>05C0h</strong></td>
<td>1DB4h</td>
<td>1DB5h</td>
<td>1DB6h</td>
<td>1DB7h</td>
<td>1DB8h</td>
<td>1DB9h</td>
<td>1DBAh</td>
<td>1DBBh</td>
</tr>
<tr class="odd">
<td><strong>05C8h</strong></td>
<td>1DBCh</td>
<td>1DBDh</td>
<td>1DBEh</td>
<td>1DBFh</td>
<td>1DC0h</td>
<td>1DC1h</td>
<td>1DC2h</td>
<td>1DC3h</td>
</tr>
<tr class="even">
<td><strong>05D0h</strong></td>
<td>1DC4h</td>
<td>1DC5h</td>
<td>1DC6h</td>
<td>1DC7h</td>
<td>1DC8h</td>
<td>1DC9h</td>
<td>1DCAh</td>
<td>1DCBh</td>
</tr>
<tr class="odd">
<td><strong>05D8h</strong></td>
<td>1DCCh</td>
<td>1DCDh</td>
<td>1DCEh</td>
<td>1DCFh</td>
<td>1DD0h</td>
<td>1DD1h</td>
<td>1DD2h</td>
<td>1DD3h</td>
</tr>
<tr class="even">
<td><strong>05E0h</strong></td>
<td>1DD4h</td>
<td>1DD5h</td>
<td>1DD6h</td>
<td>1DD7h</td>
<td>1DD8h</td>
<td>1DD9h</td>
<td>1DDAh</td>
<td>1DDBh</td>
</tr>
<tr class="odd">
<td><strong>05E8h</strong></td>
<td>1DDCh</td>
<td>1DDDh</td>
<td>1DDEh</td>
<td>1DDFh</td>
<td>1DE0h</td>
<td>1DE1h</td>
<td>1DE2h</td>
<td>1DE3h</td>
</tr>
<tr class="even">
<td><strong>05F0h</strong></td>
<td>1DE4h</td>
<td>1DE5h</td>
<td>1DE6h</td>
<td>1DE7h</td>
<td>1DE8h</td>
<td>1DE9h</td>
<td>1DEAh</td>
<td>1DEBh</td>
</tr>
<tr class="odd">
<td><strong>05F8h</strong></td>
<td>1DECh</td>
<td>1DEDh</td>
<td>1DEEh</td>
<td>1DEFh</td>
<td>1DF0h</td>
<td>1DF1h</td>
<td>1DF2h</td>
<td>1DF3h</td>
</tr>
<tr class="even">
<td><strong>0600h</strong></td>
<td>1DF4h</td>
<td>1DF5h</td>
<td>1DF6h</td>
<td>1DF7h</td>
<td>1DF8h</td>
<td>1DF9h</td>
<td>1DFAh</td>
<td>1DFBh</td>
</tr>
<tr class="odd">
<td><strong>0608h</strong></td>
<td>1DFCh</td>
<td>1DFDh</td>
<td>1DFEh</td>
<td>1DFFh</td>
<td>1E00h</td>
<td>1E00h</td>
<td>1E02h</td>
<td>1E02h</td>
</tr>
<tr class="even">
<td><strong>0610h</strong></td>
<td>1E04h</td>
<td>1E04h</td>
<td>1E06h</td>
<td>1E06h</td>
<td>1E08h</td>
<td>1E08h</td>
<td>1E0Ah</td>
<td>1E0Ah</td>
</tr>
<tr class="odd">
<td><strong>0618h</strong></td>
<td>1E0Ch</td>
<td>1E0Ch</td>
<td>1E0Eh</td>
<td>1E0Eh</td>
<td>1E10h</td>
<td>1E10h</td>
<td>1E12h</td>
<td>1E12h</td>
</tr>
<tr class="even">
<td><strong>0620h</strong></td>
<td>1E14h</td>
<td>1E14h</td>
<td>1E16h</td>
<td>1E16h</td>
<td>1E18h</td>
<td>1E18h</td>
<td>1E1Ah</td>
<td>1E1Ah</td>
</tr>
<tr class="odd">
<td><strong>0628h</strong></td>
<td>1E1Ch</td>
<td>1E1Ch</td>
<td>1E1Eh</td>
<td>1E1Eh</td>
<td>1E20h</td>
<td>1E20h</td>
<td>1E22h</td>
<td>1E22h</td>
</tr>
<tr class="even">
<td><strong>0630h</strong></td>
<td>1E24h</td>
<td>1E24h</td>
<td>1E26h</td>
<td>1E26h</td>
<td>1E28h</td>
<td>1E28h</td>
<td>1E2Ah</td>
<td>1E2Ah</td>
</tr>
<tr class="odd">
<td><strong>0638h</strong></td>
<td>1E2Ch</td>
<td>1E2Ch</td>
<td>1E2Eh</td>
<td>1E2Eh</td>
<td>1E30h</td>
<td>1E30h</td>
<td>1E32h</td>
<td>1E32h</td>
</tr>
<tr class="even">
<td><strong>0640h</strong></td>
<td>1E34h</td>
<td>1E34h</td>
<td>1E36h</td>
<td>1E36h</td>
<td>1E38h</td>
<td>1E38h</td>
<td>1E3Ah</td>
<td>1E3Ah</td>
</tr>
<tr class="odd">
<td><strong>0648h</strong></td>
<td>1E3Ch</td>
<td>1E3Ch</td>
<td>1E3Eh</td>
<td>1E3Eh</td>
<td>1E40h</td>
<td>1E40h</td>
<td>1E42h</td>
<td>1E42h</td>
</tr>
<tr class="even">
<td><strong>0650h</strong></td>
<td>1E44h</td>
<td>1E44h</td>
<td>1E46h</td>
<td>1E46h</td>
<td>1E48h</td>
<td>1E48h</td>
<td>1E4Ah</td>
<td>1E4Ah</td>
</tr>
<tr class="odd">
<td><strong>0658h</strong></td>
<td>1E4Ch</td>
<td>1E4Ch</td>
<td>1E4Eh</td>
<td>1E4Eh</td>
<td>1E50h</td>
<td>1E50h</td>
<td>1E52h</td>
<td>1E52h</td>
</tr>
<tr class="even">
<td><strong>0660h</strong></td>
<td>1E54h</td>
<td>1E54h</td>
<td>1E56h</td>
<td>1E56h</td>
<td>1E58h</td>
<td>1E58h</td>
<td>1E5Ah</td>
<td>1E5Ah</td>
</tr>
<tr class="odd">
<td><strong>0668h</strong></td>
<td>1E5Ch</td>
<td>1E5Ch</td>
<td>1E5Eh</td>
<td>1E5Eh</td>
<td>1E60h</td>
<td>1E60h</td>
<td>1E62h</td>
<td>1E62h</td>
</tr>
<tr class="even">
<td><strong>0670h</strong></td>
<td>1E64h</td>
<td>1E64h</td>
<td>1E66h</td>
<td>1E66h</td>
<td>1E68h</td>
<td>1E68h</td>
<td>1E6Ah</td>
<td>1E6Ah</td>
</tr>
<tr class="odd">
<td><strong>0678h</strong></td>
<td>1E6Ch</td>
<td>1E6Ch</td>
<td>1E6Eh</td>
<td>1E6Eh</td>
<td>1E70h</td>
<td>1E70h</td>
<td>1E72h</td>
<td>1E72h</td>
</tr>
<tr class="even">
<td><strong>0680h</strong></td>
<td>1E74h</td>
<td>1E74h</td>
<td>1E76h</td>
<td>1E76h</td>
<td>1E78h</td>
<td>1E78h</td>
<td>1E7Ah</td>
<td>1E7Ah</td>
</tr>
<tr class="odd">
<td><strong>0688h</strong></td>
<td>1E7Ch</td>
<td>1E7Ch</td>
<td>1E7Eh</td>
<td>1E7Eh</td>
<td>1E80h</td>
<td>1E80h</td>
<td>1E82h</td>
<td>1E82h</td>
</tr>
<tr class="even">
<td><strong>0690h</strong></td>
<td>1E84h</td>
<td>1E84h</td>
<td>1E86h</td>
<td>1E86h</td>
<td>1E88h</td>
<td>1E88h</td>
<td>1E8Ah</td>
<td>1E8Ah</td>
</tr>
<tr class="odd">
<td><strong>0698h</strong></td>
<td>1E8Ch</td>
<td>1E8Ch</td>
<td>1E8Eh</td>
<td>1E8Eh</td>
<td>1E90h</td>
<td>1E90h</td>
<td>1E92h</td>
<td>1E92h</td>
</tr>
<tr class="even">
<td><strong>06A0h</strong></td>
<td>1E94h</td>
<td>1E94h</td>
<td>1E96h</td>
<td>1E97h</td>
<td>1E98h</td>
<td>1E99h</td>
<td>1E9Ah</td>
<td>1E9Bh</td>
</tr>
<tr class="odd">
<td><strong>06A8h</strong></td>
<td>1E9Ch</td>
<td>1E9Dh</td>
<td>1E9Eh</td>
<td>1E9Fh</td>
<td>1EA0h</td>
<td>1EA0h</td>
<td>1EA2h</td>
<td>1EA2h</td>
</tr>
<tr class="even">
<td><strong>06B0h</strong></td>
<td>1EA4h</td>
<td>1EA4h</td>
<td>1EA6h</td>
<td>1EA6h</td>
<td>1EA8h</td>
<td>1EA8h</td>
<td>1EAAh</td>
<td>1EAAh</td>
</tr>
<tr class="odd">
<td><strong>06B8h</strong></td>
<td>1EACh</td>
<td>1EACh</td>
<td>1EAEh</td>
<td>1EAEh</td>
<td>1EB0h</td>
<td>1EB0h</td>
<td>1EB2h</td>
<td>1EB2h</td>
</tr>
<tr class="even">
<td><strong>06C0h</strong></td>
<td>1EB4h</td>
<td>1EB4h</td>
<td>1EB6h</td>
<td>1EB6h</td>
<td>1EB8h</td>
<td>1EB8h</td>
<td>1EBAh</td>
<td>1EBAh</td>
</tr>
<tr class="odd">
<td><strong>06C8h</strong></td>
<td>1EBCh</td>
<td>1EBCh</td>
<td>1EBEh</td>
<td>1EBEh</td>
<td>1EC0h</td>
<td>1EC0h</td>
<td>1EC2h</td>
<td>1EC2h</td>
</tr>
<tr class="even">
<td><strong>06D0h</strong></td>
<td>1EC4h</td>
<td>1EC4h</td>
<td>1EC6h</td>
<td>1EC6h</td>
<td>1EC8h</td>
<td>1EC8h</td>
<td>1ECAh</td>
<td>1ECAh</td>
</tr>
<tr class="odd">
<td><strong>06D8h</strong></td>
<td>1ECCh</td>
<td>1ECCh</td>
<td>1ECEh</td>
<td>1ECEh</td>
<td>1ED0h</td>
<td>1ED0h</td>
<td>1ED2h</td>
<td>1ED2h</td>
</tr>
<tr class="even">
<td><strong>06E0h</strong></td>
<td>1ED4h</td>
<td>1ED4h</td>
<td>1ED6h</td>
<td>1ED6h</td>
<td>1ED8h</td>
<td>1ED8h</td>
<td>1EDAh</td>
<td>1EDAh</td>
</tr>
<tr class="odd">
<td><strong>06E8h</strong></td>
<td>1EDCh</td>
<td>1EDCh</td>
<td>1EDEh</td>
<td>1EDEh</td>
<td>1EE0h</td>
<td>1EE0h</td>
<td>1EE2h</td>
<td>1EE2h</td>
</tr>
<tr class="even">
<td><strong>06F0h</strong></td>
<td>1EE4h</td>
<td>1EE4h</td>
<td>1EE6h</td>
<td>1EE6h</td>
<td>1EE8h</td>
<td>1EE8h</td>
<td>1EEAh</td>
<td>1EEAh</td>
</tr>
<tr class="odd">
<td><strong>06F8h</strong></td>
<td>1EECh</td>
<td>1EECh</td>
<td>1EEEh</td>
<td>1EEEh</td>
<td>1EF0h</td>
<td>1EF0h</td>
<td>1EF2h</td>
<td>1EF2h</td>
</tr>
<tr class="even">
<td><strong>0700h</strong></td>
<td>1EF4h</td>
<td>1EF4h</td>
<td>1EF6h</td>
<td>1EF6h</td>
<td>1EF8h</td>
<td>1EF8h</td>
<td>1EFAh</td>
<td>1EFBh</td>
</tr>
<tr class="odd">
<td><strong>0708h</strong></td>
<td>1EFCh</td>
<td>1EFDh</td>
<td>1EFEh</td>
<td>1EFFh</td>
<td>1F08h</td>
<td>1F09h</td>
<td>1F0Ah</td>
<td>1F0Bh</td>
</tr>
<tr class="even">
<td><strong>0710h</strong></td>
<td>1F0Ch</td>
<td>1F0Dh</td>
<td>1F0Eh</td>
<td>1F0Fh</td>
<td>1F08h</td>
<td>1F09h</td>
<td>1F0Ah</td>
<td>1F0Bh</td>
</tr>
<tr class="odd">
<td><strong>0718h</strong></td>
<td>1F0Ch</td>
<td>1F0Dh</td>
<td>1F0Eh</td>
<td>1F0Fh</td>
<td>1F18h</td>
<td>1F19h</td>
<td>1F1Ah</td>
<td>1F1Bh</td>
</tr>
<tr class="even">
<td><strong>0720h</strong></td>
<td>1F1Ch</td>
<td>1F1Dh</td>
<td>1F16h</td>
<td>1F17h</td>
<td>1F18h</td>
<td>1F19h</td>
<td>1F1Ah</td>
<td>1F1Bh</td>
</tr>
<tr class="odd">
<td><strong>0728h</strong></td>
<td>1F1Ch</td>
<td>1F1Dh</td>
<td>1F1Eh</td>
<td>1F1Fh</td>
<td>1F28h</td>
<td>1F29h</td>
<td>1F2Ah</td>
<td>1F2Bh</td>
</tr>
<tr class="even">
<td><strong>0730h</strong></td>
<td>1F2Ch</td>
<td>1F2Dh</td>
<td>1F2Eh</td>
<td>1F2Fh</td>
<td>1F28h</td>
<td>1F29h</td>
<td>1F2Ah</td>
<td>1F2Bh</td>
</tr>
<tr class="odd">
<td><strong>0738h</strong></td>
<td>1F2Ch</td>
<td>1F2Dh</td>
<td>1F2Eh</td>
<td>1F2Fh</td>
<td>1F38h</td>
<td>1F39h</td>
<td>1F3Ah</td>
<td>1F3Bh</td>
</tr>
<tr class="even">
<td><strong>0740h</strong></td>
<td>1F3Ch</td>
<td>1F3Dh</td>
<td>1F3Eh</td>
<td>1F3Fh</td>
<td>1F38h</td>
<td>1F39h</td>
<td>1F3Ah</td>
<td>1F3Bh</td>
</tr>
<tr class="odd">
<td><strong>0748h</strong></td>
<td>1F3Ch</td>
<td>1F3Dh</td>
<td>1F3Eh</td>
<td>1F3Fh</td>
<td>1F48h</td>
<td>1F49h</td>
<td>1F4Ah</td>
<td>1F4Bh</td>
</tr>
<tr class="even">
<td><strong>0750h</strong></td>
<td>1F4Ch</td>
<td>1F4Dh</td>
<td>1F46h</td>
<td>1F47h</td>
<td>1F48h</td>
<td>1F49h</td>
<td>1F4Ah</td>
<td>1F4Bh</td>
</tr>
<tr class="odd">
<td><strong>0758h</strong></td>
<td>1F4Ch</td>
<td>1F4Dh</td>
<td>1F4Eh</td>
<td>1F4Fh</td>
<td>1F50h</td>
<td>1F59h</td>
<td>1F52h</td>
<td>1F5Bh</td>
</tr>
<tr class="even">
<td><strong>0760h</strong></td>
<td>1F54h</td>
<td>1F5Dh</td>
<td>1F56h</td>
<td>1F5Fh</td>
<td>1F58h</td>
<td>1F59h</td>
<td>1F5Ah</td>
<td>1F5Bh</td>
</tr>
<tr class="odd">
<td><strong>0768h</strong></td>
<td>1F5Ch</td>
<td>1F5Dh</td>
<td>1F5Eh</td>
<td>1F5Fh</td>
<td>1F68h</td>
<td>1F69h</td>
<td>1F6Ah</td>
<td>1F6Bh</td>
</tr>
<tr class="even">
<td><strong>0770h</strong></td>
<td>1F6Ch</td>
<td>1F6Dh</td>
<td>1F6Eh</td>
<td>1F6Fh</td>
<td>1F68h</td>
<td>1F69h</td>
<td>1F6Ah</td>
<td>1F6Bh</td>
</tr>
<tr class="odd">
<td><strong>0778h</strong></td>
<td>1F6Ch</td>
<td>1F6Dh</td>
<td>1F6Eh</td>
<td>1F6Fh</td>
<td>1FBAh</td>
<td>1FBBh</td>
<td>1FC8h</td>
<td>1FC9h</td>
</tr>
<tr class="even">
<td><strong>0780h</strong></td>
<td>1FCAh</td>
<td>1FCBh</td>
<td>1FDAh</td>
<td>1FDBh</td>
<td>1FF8h</td>
<td>1FF9h</td>
<td>1FEAh</td>
<td>1FEBh</td>
</tr>
<tr class="odd">
<td><strong>0788h</strong></td>
<td>1FFAh</td>
<td>1FFBh</td>
<td>1F7Eh</td>
<td>1F7Fh</td>
<td>1F88h</td>
<td>1F89h</td>
<td>1F8Ah</td>
<td>1F8Bh</td>
</tr>
<tr class="even">
<td><strong>0790h</strong></td>
<td>1F8Ch</td>
<td>1F8Dh</td>
<td>1F8Eh</td>
<td>1F8Fh</td>
<td>1F88h</td>
<td>1F89h</td>
<td>1F8Ah</td>
<td>1F8Bh</td>
</tr>
<tr class="odd">
<td><strong>0798h</strong></td>
<td>1F8Ch</td>
<td>1F8Dh</td>
<td>1F8Eh</td>
<td>1F8Fh</td>
<td>1F98h</td>
<td>1F99h</td>
<td>1F9Ah</td>
<td>1F9Bh</td>
</tr>
<tr class="even">
<td><strong>07A0h</strong></td>
<td>1F9Ch</td>
<td>1F9Dh</td>
<td>1F9Eh</td>
<td>1F9Fh</td>
<td>1F98h</td>
<td>1F99h</td>
<td>1F9Ah</td>
<td>1F9Bh</td>
</tr>
<tr class="odd">
<td><strong>07A8h</strong></td>
<td>1F9Ch</td>
<td>1F9Dh</td>
<td>1F9Eh</td>
<td>1F9Fh</td>
<td>1FA8h</td>
<td>1FA9h</td>
<td>1FAAh</td>
<td>1FABh</td>
</tr>
<tr class="even">
<td><strong>07B0h</strong></td>
<td>1FACh</td>
<td>1FADh</td>
<td>1FAEh</td>
<td>1FAFh</td>
<td>1FA8h</td>
<td>1FA9h</td>
<td>1FAAh</td>
<td>1FABh</td>
</tr>
<tr class="odd">
<td><strong>07B8h</strong></td>
<td>1FACh</td>
<td>1FADh</td>
<td>1FAEh</td>
<td>1FAFh</td>
<td>1FB8h</td>
<td>1FB9h</td>
<td>1FB2h</td>
<td>1FBCh</td>
</tr>
<tr class="even">
<td><strong>07C0h</strong></td>
<td>1FB4h</td>
<td>1FB5h</td>
<td>1FB6h</td>
<td>1FB7h</td>
<td>1FB8h</td>
<td>1FB9h</td>
<td>1FBAh</td>
<td>1FBBh</td>
</tr>
<tr class="odd">
<td><strong>07C8h</strong></td>
<td>1FBCh</td>
<td>1FBDh</td>
<td>1FBEh</td>
<td>1FBFh</td>
<td>1FC0h</td>
<td>1FC1h</td>
<td>1FC2h</td>
<td>1FC3h</td>
</tr>
<tr class="even">
<td><strong>07D0h</strong></td>
<td>1FC4h</td>
<td>1FC5h</td>
<td>1FC6h</td>
<td>1FC7h</td>
<td>1FC8h</td>
<td>1FC9h</td>
<td>1FCAh</td>
<td>1FCBh</td>
</tr>
<tr class="odd">
<td><strong>07D8h</strong></td>
<td>1FC3h</td>
<td>1FCDh</td>
<td>1FCEh</td>
<td>1FCFh</td>
<td>1FD8h</td>
<td>1FD9h</td>
<td>1FD2h</td>
<td>1FD3h</td>
</tr>
<tr class="even">
<td><strong>07E0h</strong></td>
<td>1FD4h</td>
<td>1FD5h</td>
<td>1FD6h</td>
<td>1FD7h</td>
<td>1FD8h</td>
<td>1FD9h</td>
<td>1FDAh</td>
<td>1FDBh</td>
</tr>
<tr class="odd">
<td><strong>07E8h</strong></td>
<td>1FDCh</td>
<td>1FDDh</td>
<td>1FDEh</td>
<td>1FDFh</td>
<td>1FE8h</td>
<td>1FE9h</td>
<td>1FE2h</td>
<td>1FE3h</td>
</tr>
<tr class="even">
<td><strong>07F0h</strong></td>
<td>1FE4h</td>
<td>1FECh</td>
<td>1FE6h</td>
<td>1FE7h</td>
<td>1FE8h</td>
<td>1FE9h</td>
<td>1FEAh</td>
<td>1FEBh</td>
</tr>
<tr class="odd">
<td><strong>07F8h</strong></td>
<td>1FECh</td>
<td>1FEDh</td>
<td>1FEEh</td>
<td>1FEFh</td>
<td>1FF0h</td>
<td>1FF1h</td>
<td>1FF2h</td>
<td>1FF3h</td>
</tr>
<tr class="even">
<td><strong>0800h</strong></td>
<td>1FF4h</td>
<td>1FF5h</td>
<td>1FF6h</td>
<td>1FF7h</td>
<td>1FF8h</td>
<td>1FF9h</td>
<td>1FFAh</td>
<td>1FFBh</td>
</tr>
<tr class="odd">
<td><strong>0808h</strong></td>
<td>1FF3h</td>
<td>1FFDh</td>
<td>1FFEh</td>
<td>1FFFh</td>
<td>2000h</td>
<td>2001h</td>
<td>2002h</td>
<td>2003h</td>
</tr>
<tr class="even">
<td><strong>0810h</strong></td>
<td>2004h</td>
<td>2005h</td>
<td>2006h</td>
<td>2007h</td>
<td>2008h</td>
<td>2009h</td>
<td>200Ah</td>
<td>200Bh</td>
</tr>
<tr class="odd">
<td><strong>0818h</strong></td>
<td>200Ch</td>
<td>200Dh</td>
<td>200Eh</td>
<td>200Fh</td>
<td>2010h</td>
<td>2011h</td>
<td>2012h</td>
<td>2013h</td>
</tr>
<tr class="even">
<td><strong>0820h</strong></td>
<td>2014h</td>
<td>2015h</td>
<td>2016h</td>
<td>2017h</td>
<td>2018h</td>
<td>2019h</td>
<td>201Ah</td>
<td>201Bh</td>
</tr>
<tr class="odd">
<td><strong>0828h</strong></td>
<td>201Ch</td>
<td>201Dh</td>
<td>201Eh</td>
<td>201Fh</td>
<td>2020h</td>
<td>2021h</td>
<td>2022h</td>
<td>2023h</td>
</tr>
<tr class="even">
<td><strong>0830h</strong></td>
<td>2024h</td>
<td>2025h</td>
<td>2026h</td>
<td>2027h</td>
<td>2028h</td>
<td>2029h</td>
<td>202Ah</td>
<td>202Bh</td>
</tr>
<tr class="odd">
<td><strong>0838h</strong></td>
<td>202Ch</td>
<td>202Dh</td>
<td>202Eh</td>
<td>202Fh</td>
<td>2030h</td>
<td>2031h</td>
<td>2032h</td>
<td>2033h</td>
</tr>
<tr class="even">
<td><strong>0840h</strong></td>
<td>2034h</td>
<td>2035h</td>
<td>2036h</td>
<td>2037h</td>
<td>2038h</td>
<td>2039h</td>
<td>203Ah</td>
<td>203Bh</td>
</tr>
<tr class="odd">
<td><strong>0848h</strong></td>
<td>203Ch</td>
<td>203Dh</td>
<td>203Eh</td>
<td>203Fh</td>
<td>2040h</td>
<td>2041h</td>
<td>2042h</td>
<td>2043h</td>
</tr>
<tr class="even">
<td><strong>0850h</strong></td>
<td>2044h</td>
<td>2045h</td>
<td>2046h</td>
<td>2047h</td>
<td>2048h</td>
<td>2049h</td>
<td>204Ah</td>
<td>204Bh</td>
</tr>
<tr class="odd">
<td><strong>0858h</strong></td>
<td>204Ch</td>
<td>204Dh</td>
<td>204Eh</td>
<td>204Fh</td>
<td>2050h</td>
<td>2051h</td>
<td>2052h</td>
<td>2053h</td>
</tr>
<tr class="even">
<td><strong>0860h</strong></td>
<td>2054h</td>
<td>2055h</td>
<td>2056h</td>
<td>2057h</td>
<td>2058h</td>
<td>2059h</td>
<td>205Ah</td>
<td>205Bh</td>
</tr>
<tr class="odd">
<td><strong>0868h</strong></td>
<td>205Ch</td>
<td>205Dh</td>
<td>205Eh</td>
<td>205Fh</td>
<td>2060h</td>
<td>2061h</td>
<td>2062h</td>
<td>2063h</td>
</tr>
<tr class="even">
<td><strong>0870h</strong></td>
<td>2064h</td>
<td>2065h</td>
<td>2066h</td>
<td>2067h</td>
<td>2068h</td>
<td>2069h</td>
<td>206Ah</td>
<td>206Bh</td>
</tr>
<tr class="odd">
<td><strong>0878h</strong></td>
<td>206Ch</td>
<td>206Dh</td>
<td>206Eh</td>
<td>206Fh</td>
<td>2070h</td>
<td>2071h</td>
<td>2072h</td>
<td>2073h</td>
</tr>
<tr class="even">
<td><strong>0880h</strong></td>
<td>2074h</td>
<td>2075h</td>
<td>2076h</td>
<td>2077h</td>
<td>2078h</td>
<td>2079h</td>
<td>207Ah</td>
<td>207Bh</td>
</tr>
<tr class="odd">
<td><strong>0888h</strong></td>
<td>207Ch</td>
<td>207Dh</td>
<td>207Eh</td>
<td>207Fh</td>
<td>2080h</td>
<td>2081h</td>
<td>2082h</td>
<td>2083h</td>
</tr>
<tr class="even">
<td><strong>0890h</strong></td>
<td>2084h</td>
<td>2085h</td>
<td>2086h</td>
<td>2087h</td>
<td>2088h</td>
<td>2089h</td>
<td>208Ah</td>
<td>208Bh</td>
</tr>
<tr class="odd">
<td><strong>0898h</strong></td>
<td>208Ch</td>
<td>208Dh</td>
<td>208Eh</td>
<td>208Fh</td>
<td>2090h</td>
<td>2091h</td>
<td>2092h</td>
<td>2093h</td>
</tr>
<tr class="even">
<td><strong>08A0h</strong></td>
<td>2094h</td>
<td>2095h</td>
<td>2096h</td>
<td>2097h</td>
<td>2098h</td>
<td>2099h</td>
<td>209Ah</td>
<td>209Bh</td>
</tr>
<tr class="odd">
<td><strong>08A8h</strong></td>
<td>209Ch</td>
<td>209Dh</td>
<td>209Eh</td>
<td>209Fh</td>
<td>20A0h</td>
<td>20A1h</td>
<td>20A2h</td>
<td>20A3h</td>
</tr>
<tr class="even">
<td><strong>08B0h</strong></td>
<td>20A4h</td>
<td>20A5h</td>
<td>20A6h</td>
<td>20A7h</td>
<td>20A8h</td>
<td>20A9h</td>
<td>20AAh</td>
<td>20ABh</td>
</tr>
<tr class="odd">
<td><strong>08B8h</strong></td>
<td>20ACh</td>
<td>20ADh</td>
<td>20AEh</td>
<td>20AFh</td>
<td>20B0h</td>
<td>20B1h</td>
<td>20B2h</td>
<td>20B3h</td>
</tr>
<tr class="even">
<td><strong>08C0h</strong></td>
<td>20B4h</td>
<td>20B5h</td>
<td>20B6h</td>
<td>20B7h</td>
<td>20B8h</td>
<td>20B9h</td>
<td>20BAh</td>
<td>20BBh</td>
</tr>
<tr class="odd">
<td><strong>08C8h</strong></td>
<td>20BCh</td>
<td>20BDh</td>
<td>20BEh</td>
<td>20BFh</td>
<td>20C0h</td>
<td>20C1h</td>
<td>20C2h</td>
<td>20C3h</td>
</tr>
<tr class="even">
<td><strong>08D0h</strong></td>
<td>20C4h</td>
<td>20C5h</td>
<td>20C6h</td>
<td>20C7h</td>
<td>20C8h</td>
<td>20C9h</td>
<td>20CAh</td>
<td>20CBh</td>
</tr>
<tr class="odd">
<td><strong>08D8h</strong></td>
<td>20CCh</td>
<td>20CDh</td>
<td>20CEh</td>
<td>20CFh</td>
<td>20D0h</td>
<td>20D1h</td>
<td>20D2h</td>
<td>20D3h</td>
</tr>
<tr class="even">
<td><strong>08E0h</strong></td>
<td>20D4h</td>
<td>20D5h</td>
<td>20D6h</td>
<td>20D7h</td>
<td>20D8h</td>
<td>20D9h</td>
<td>20DAh</td>
<td>20DBh</td>
</tr>
<tr class="odd">
<td><strong>08E8h</strong></td>
<td>20DCh</td>
<td>20DDh</td>
<td>20DEh</td>
<td>20DFh</td>
<td>20E0h</td>
<td>20E1h</td>
<td>20E2h</td>
<td>20E3h</td>
</tr>
<tr class="even">
<td><strong>08F0h</strong></td>
<td>20E4h</td>
<td>20E5h</td>
<td>20E6h</td>
<td>20E7h</td>
<td>20E8h</td>
<td>20E9h</td>
<td>20EAh</td>
<td>20EBh</td>
</tr>
<tr class="odd">
<td><strong>08F8h</strong></td>
<td>20ECh</td>
<td>20EDh</td>
<td>20EEh</td>
<td>20EFh</td>
<td>20F0h</td>
<td>20F1h</td>
<td>20F2h</td>
<td>20F3h</td>
</tr>
<tr class="even">
<td><strong>0900h</strong></td>
<td>20F4h</td>
<td>20F5h</td>
<td>20F6h</td>
<td>20F7h</td>
<td>20F8h</td>
<td>20F9h</td>
<td>20FAh</td>
<td>20FBh</td>
</tr>
<tr class="odd">
<td><strong>0908h</strong></td>
<td>20FCh</td>
<td>20FDh</td>
<td>20FEh</td>
<td>20FFh</td>
<td>2100h</td>
<td>2101h</td>
<td>2102h</td>
<td>2103h</td>
</tr>
<tr class="even">
<td><strong>0910h</strong></td>
<td>2104h</td>
<td>2105h</td>
<td>2106h</td>
<td>2107h</td>
<td>2108h</td>
<td>2109h</td>
<td>210Ah</td>
<td>210Bh</td>
</tr>
<tr class="odd">
<td><strong>0918h</strong></td>
<td>210Ch</td>
<td>210Dh</td>
<td>210Eh</td>
<td>210Fh</td>
<td>2110h</td>
<td>2111h</td>
<td>2112h</td>
<td>2113h</td>
</tr>
<tr class="even">
<td><strong>0920h</strong></td>
<td>2114h</td>
<td>2115h</td>
<td>2116h</td>
<td>2117h</td>
<td>2118h</td>
<td>2119h</td>
<td>211Ah</td>
<td>211Bh</td>
</tr>
<tr class="odd">
<td><strong>0928h</strong></td>
<td>211Ch</td>
<td>211Dh</td>
<td>211Eh</td>
<td>211Fh</td>
<td>2120h</td>
<td>2121h</td>
<td>2122h</td>
<td>2123h</td>
</tr>
<tr class="even">
<td><strong>0930h</strong></td>
<td>2124h</td>
<td>2125h</td>
<td>2126h</td>
<td>2127h</td>
<td>2128h</td>
<td>2129h</td>
<td>212Ah</td>
<td>212Bh</td>
</tr>
<tr class="odd">
<td><strong>0938h</strong></td>
<td>212Ch</td>
<td>212Dh</td>
<td>212Eh</td>
<td>212Fh</td>
<td>2130h</td>
<td>2131h</td>
<td>2132h</td>
<td>2133h</td>
</tr>
<tr class="even">
<td><strong>0940h</strong></td>
<td>2134h</td>
<td>2135h</td>
<td>2136h</td>
<td>2137h</td>
<td>2138h</td>
<td>2139h</td>
<td>213Ah</td>
<td>213Bh</td>
</tr>
<tr class="odd">
<td><strong>0948h</strong></td>
<td>213Ch</td>
<td>213Dh</td>
<td>213Eh</td>
<td>213Fh</td>
<td>2140h</td>
<td>2141h</td>
<td>2142h</td>
<td>2143h</td>
</tr>
<tr class="even">
<td><strong>0950h</strong></td>
<td>2144h</td>
<td>2145h</td>
<td>2146h</td>
<td>2147h</td>
<td>2148h</td>
<td>2149h</td>
<td>214Ah</td>
<td>214Bh</td>
</tr>
<tr class="odd">
<td><strong>0958h</strong></td>
<td>214Ch</td>
<td>214Dh</td>
<td>2132h</td>
<td>214Fh</td>
<td>2150h</td>
<td>2151h</td>
<td>2152h</td>
<td>2153h</td>
</tr>
<tr class="even">
<td><strong>0960h</strong></td>
<td>2154h</td>
<td>2155h</td>
<td>2156h</td>
<td>2157h</td>
<td>2158h</td>
<td>2159h</td>
<td>215Ah</td>
<td>215Bh</td>
</tr>
<tr class="odd">
<td><strong>0968h</strong></td>
<td>215Ch</td>
<td>215Dh</td>
<td>215Eh</td>
<td>215Fh</td>
<td>2160h</td>
<td>2161h</td>
<td>2162h</td>
<td>2163h</td>
</tr>
<tr class="even">
<td><strong>0970h</strong></td>
<td>2164h</td>
<td>2165h</td>
<td>2166h</td>
<td>2167h</td>
<td>2168h</td>
<td>2169h</td>
<td>216Ah</td>
<td>216Bh</td>
</tr>
<tr class="odd">
<td><strong>0978h</strong></td>
<td>216Ch</td>
<td>216Dh</td>
<td>216Eh</td>
<td>216Fh</td>
<td>2160h</td>
<td>2161h</td>
<td>2162h</td>
<td>2163h</td>
</tr>
<tr class="even">
<td><strong>0980h</strong></td>
<td>2164h</td>
<td>2165h</td>
<td>2166h</td>
<td>2167h</td>
<td>2168h</td>
<td>2169h</td>
<td>216Ah</td>
<td>216Bh</td>
</tr>
<tr class="odd">
<td><strong>0988h</strong></td>
<td>216Ch</td>
<td>216Dh</td>
<td>216Eh</td>
<td>216Fh</td>
<td>2180h</td>
<td>2181h</td>
<td>2182h</td>
<td>2183h</td>
</tr>
<tr class="even">
<td><strong>0990h</strong></td>
<td>2183h</td>
<td>FFFFh</td>
<td>034Bh</td>
<td>24B6h</td>
<td>24B7h</td>
<td>24B8h</td>
<td>24B9h</td>
<td>24BAh</td>
</tr>
<tr class="odd">
<td><strong>0998h</strong></td>
<td>24BBh</td>
<td>24BCh</td>
<td>24BDh</td>
<td>24BEh</td>
<td>24BFh</td>
<td>24C0h</td>
<td>24C1h</td>
<td>24C2h</td>
</tr>
<tr class="even">
<td><strong>09A0h</strong></td>
<td>24C3h</td>
<td>24C4h</td>
<td>24C5h</td>
<td>24C6h</td>
<td>24C7h</td>
<td>24C8h</td>
<td>24C9h</td>
<td>24CAh</td>
</tr>
<tr class="odd">
<td><strong>09A8h</strong></td>
<td>24CBh</td>
<td>24CCh</td>
<td>24CDh</td>
<td>24CEh</td>
<td>24CFh</td>
<td>FFFFh</td>
<td>0746h</td>
<td>2C00h</td>
</tr>
<tr class="even">
<td><strong>09B0h</strong></td>
<td>2C01h</td>
<td>2C02h</td>
<td>2C03h</td>
<td>2C04h</td>
<td>2C05h</td>
<td>2C06h</td>
<td>2C07h</td>
<td>2C08h</td>
</tr>
<tr class="odd">
<td><strong>09B8h</strong></td>
<td>2C09h</td>
<td>2C0Ah</td>
<td>2C0Bh</td>
<td>2C0Ch</td>
<td>2C0Dh</td>
<td>2C0Eh</td>
<td>2C0Fh</td>
<td>2C10h</td>
</tr>
<tr class="even">
<td><strong>09C0h</strong></td>
<td>2C11h</td>
<td>2C12h</td>
<td>2C13h</td>
<td>2C14h</td>
<td>2C15h</td>
<td>2C16h</td>
<td>2C17h</td>
<td>2C18h</td>
</tr>
<tr class="odd">
<td><strong>09C8h</strong></td>
<td>2C19h</td>
<td>2C1Ah</td>
<td>2C1Bh</td>
<td>2C1Ch</td>
<td>2C1Dh</td>
<td>2C1Eh</td>
<td>2C1Fh</td>
<td>2C20h</td>
</tr>
<tr class="even">
<td><strong>09D0h</strong></td>
<td>2C21h</td>
<td>2C22h</td>
<td>2C23h</td>
<td>2C24h</td>
<td>2C25h</td>
<td>2C26h</td>
<td>2C27h</td>
<td>2C28h</td>
</tr>
<tr class="odd">
<td><strong>09D8h</strong></td>
<td>2C29h</td>
<td>2C2Ah</td>
<td>2C2Bh</td>
<td>2C2Ch</td>
<td>2C2Dh</td>
<td>2C2Eh</td>
<td>2C5Fh</td>
<td>2C60h</td>
</tr>
<tr class="even">
<td><strong>09E0h</strong></td>
<td>2C60h</td>
<td>2C62h</td>
<td>2C63h</td>
<td>2C64h</td>
<td>2C65h</td>
<td>2C66h</td>
<td>2C67h</td>
<td>2C67h</td>
</tr>
<tr class="odd">
<td><strong>09E8h</strong></td>
<td>2C69h</td>
<td>2C69h</td>
<td>2C6Bh</td>
<td>2C6Bh</td>
<td>2C6Dh</td>
<td>2C6Eh</td>
<td>2C6Fh</td>
<td>2C70h</td>
</tr>
<tr class="even">
<td><strong>09F0h</strong></td>
<td>2C71h</td>
<td>2C72h</td>
<td>2C73h</td>
<td>2C74h</td>
<td>2C75h</td>
<td>2C75h</td>
<td>2C77h</td>
<td>2C78h</td>
</tr>
<tr class="odd">
<td><strong>09F8h</strong></td>
<td>2C79h</td>
<td>2C7Ah</td>
<td>2C7Bh</td>
<td>2C7Ch</td>
<td>2C7Dh</td>
<td>2C7Eh</td>
<td>2C7Fh</td>
<td>2C80h</td>
</tr>
<tr class="even">
<td><strong>0A00h</strong></td>
<td>2C80h</td>
<td>2C82h</td>
<td>2C82h</td>
<td>2C84h</td>
<td>2C84h</td>
<td>2C86h</td>
<td>2C86h</td>
<td>2C88h</td>
</tr>
<tr class="odd">
<td><strong>0A08h</strong></td>
<td>2C88h</td>
<td>2C8Ah</td>
<td>2C8Ah</td>
<td>2C8Ch</td>
<td>2C8Ch</td>
<td>2C8Eh</td>
<td>2C8Eh</td>
<td>2C90h</td>
</tr>
<tr class="even">
<td><strong>0A10h</strong></td>
<td>2C90h</td>
<td>2C92h</td>
<td>2C92h</td>
<td>2C94h</td>
<td>2C94h</td>
<td>2C96h</td>
<td>2C96h</td>
<td>2C98h</td>
</tr>
<tr class="odd">
<td><strong>0A18h</strong></td>
<td>2C98h</td>
<td>2C9Ah</td>
<td>2C9Ah</td>
<td>2C9Ch</td>
<td>2C9Ch</td>
<td>2C9Eh</td>
<td>2C9Eh</td>
<td>2CA0h</td>
</tr>
<tr class="even">
<td><strong>0A20h</strong></td>
<td>2CA0h</td>
<td>2CA2h</td>
<td>2CA2h</td>
<td>2CA4h</td>
<td>2CA4h</td>
<td>2CA6h</td>
<td>2CA6h</td>
<td>2CA8h</td>
</tr>
<tr class="odd">
<td><strong>0A28h</strong></td>
<td>2CA8h</td>
<td>2CAAh</td>
<td>2CAAh</td>
<td>2CACh</td>
<td>2CACh</td>
<td>2CAEh</td>
<td>2CAEh</td>
<td>2CB0h</td>
</tr>
<tr class="even">
<td><strong>0A30h</strong></td>
<td>2CB0h</td>
<td>2CB2h</td>
<td>2CB2h</td>
<td>2CB4h</td>
<td>2CB4h</td>
<td>2CB6h</td>
<td>2CB6h</td>
<td>2CB8h</td>
</tr>
<tr class="odd">
<td><strong>0A38h</strong></td>
<td>2CB8h</td>
<td>2CBAh</td>
<td>2CBAh</td>
<td>2CBCh</td>
<td>2CBCh</td>
<td>2CBEh</td>
<td>2CBEh</td>
<td>2CC0h</td>
</tr>
<tr class="even">
<td><strong>0A40h</strong></td>
<td>2CC0h</td>
<td>2CC2h</td>
<td>2CC2h</td>
<td>2CC4h</td>
<td>2CC4h</td>
<td>2CC6h</td>
<td>2CC6h</td>
<td>2CC8h</td>
</tr>
<tr class="odd">
<td><strong>0A48h</strong></td>
<td>2CC8h</td>
<td>2CCAh</td>
<td>2CCAh</td>
<td>2CCCh</td>
<td>2CCCh</td>
<td>2CCEh</td>
<td>2CCEh</td>
<td>2CD0h</td>
</tr>
<tr class="even">
<td><strong>0A50h</strong></td>
<td>2CD0h</td>
<td>2CD2h</td>
<td>2CD2h</td>
<td>2CD4h</td>
<td>2CD4h</td>
<td>2CD6h</td>
<td>2CD6h</td>
<td>2CD8h</td>
</tr>
<tr class="odd">
<td><strong>0A58h</strong></td>
<td>2CD8h</td>
<td>2CDAh</td>
<td>2CDAh</td>
<td>2CDCh</td>
<td>2CDCh</td>
<td>2CDEh</td>
<td>2CDEh</td>
<td>2CE0h</td>
</tr>
<tr class="even">
<td><strong>0A60h</strong></td>
<td>2CE0h</td>
<td>2CE2h</td>
<td>2CE2h</td>
<td>2CE4h</td>
<td>2CE5h</td>
<td>2CE6h</td>
<td>2CE7h</td>
<td>2CE8h</td>
</tr>
<tr class="odd">
<td><strong>0A68h</strong></td>
<td>2CE9h</td>
<td>2CEAh</td>
<td>2CEBh</td>
<td>2CECh</td>
<td>2CEDh</td>
<td>2CEEh</td>
<td>2CEFh</td>
<td>2CF0h</td>
</tr>
<tr class="even">
<td><strong>0A70h</strong></td>
<td>2CF1h</td>
<td>2CF2h</td>
<td>2CF3h</td>
<td>2CF4h</td>
<td>2CF5h</td>
<td>2CF6h</td>
<td>2CF7h</td>
<td>2CF8h</td>
</tr>
<tr class="odd">
<td><strong>0A78h</strong></td>
<td>2CF9h</td>
<td>2CFAh</td>
<td>2CFBh</td>
<td>2CFCh</td>
<td>2CFDh</td>
<td>2CFEh</td>
<td>2CFFh</td>
<td>10A0h</td>
</tr>
<tr class="even">
<td><strong>0A80h</strong></td>
<td>10A1h</td>
<td>10A2h</td>
<td>10A3h</td>
<td>10A4h</td>
<td>10A5h</td>
<td>10A6h</td>
<td>10A7h</td>
<td>10A8h</td>
</tr>
<tr class="odd">
<td><strong>0A88h</strong></td>
<td>10A9h</td>
<td>10AAh</td>
<td>10ABh</td>
<td>10ACh</td>
<td>10ADh</td>
<td>10AEh</td>
<td>10AFh</td>
<td>10B0h</td>
</tr>
<tr class="even">
<td><strong>0A90h</strong></td>
<td>10B1h</td>
<td>10B2h</td>
<td>10B3h</td>
<td>10B4h</td>
<td>10B5h</td>
<td>10B6h</td>
<td>10B7h</td>
<td>10B8h</td>
</tr>
<tr class="odd">
<td><strong>0A98h</strong></td>
<td>10B9h</td>
<td>10BAh</td>
<td>10BBh</td>
<td>10BCh</td>
<td>10BDh</td>
<td>10BEh</td>
<td>10BFh</td>
<td>10C0h</td>
</tr>
<tr class="even">
<td><strong>0AA0h</strong></td>
<td>10C1h</td>
<td>10C2h</td>
<td>10C3h</td>
<td>10C4h</td>
<td>10C5h</td>
<td>FFFFh</td>
<td>D21Bh</td>
<td>FF21h</td>
</tr>
<tr class="odd">
<td><strong>0AA8h</strong></td>
<td>FF22h</td>
<td>FF23h</td>
<td>FF24h</td>
<td>FF25h</td>
<td>FF26h</td>
<td>FF27h</td>
<td>FF28h</td>
<td>FF29h</td>
</tr>
<tr class="even">
<td><strong>0AB0h</strong></td>
<td>FF2Ah</td>
<td>FF2Bh</td>
<td>FF2Ch</td>
<td>FF2Dh</td>
<td>FF2Eh</td>
<td>FF2Fh</td>
<td>FF30h</td>
<td>FF31h</td>
</tr>
<tr class="odd">
<td><strong>0AB8h</strong></td>
<td>FF32h</td>
<td>FF33h</td>
<td>FF34h</td>
<td>FF35h</td>
<td>FF36h</td>
<td>FF37h</td>
<td>FF38h</td>
<td>FF39h</td>
</tr>
<tr class="even">
<td><strong>0AC0h</strong></td>
<td>FF3Ah</td>
<td>FF5Bh</td>
<td>FF5Ch</td>
<td>FF5Dh</td>
<td>FF5Eh</td>
<td>FF5Fh</td>
<td>FF60h</td>
<td>FF61h</td>
</tr>
<tr class="odd">
<td><strong>0AC8h</strong></td>
<td>FF62h</td>
<td>FF63h</td>
<td>FF64h</td>
<td>FF65h</td>
<td>FF66h</td>
<td>FF67h</td>
<td>FF68h</td>
<td>FF69h</td>
</tr>
<tr class="even">
<td><strong>0AD0h</strong></td>
<td>FF6Ah</td>
<td>FF6Bh</td>
<td>FF6Ch</td>
<td>FF6Dh</td>
<td>FF6Eh</td>
<td>FF6Fh</td>
<td>FF70h</td>
<td>FF71h</td>
</tr>
<tr class="odd">
<td><strong>0AD8h</strong></td>
<td>FF72h</td>
<td>FF73h</td>
<td>FF74h</td>
<td>FF75h</td>
<td>FF76h</td>
<td>FF77h</td>
<td>FF78h</td>
<td>FF79h</td>
</tr>
<tr class="even">
<td><strong>0AE0h</strong></td>
<td>FF7Ah</td>
<td>FF7Bh</td>
<td>FF7Ch</td>
<td>FF7Dh</td>
<td>FF7Eh</td>
<td>FF7Fh</td>
<td>FF80h</td>
<td>FF81h</td>
</tr>
<tr class="odd">
<td><strong>0AE8h</strong></td>
<td>FF82h</td>
<td>FF83h</td>
<td>FF84h</td>
<td>FF85h</td>
<td>FF86h</td>
<td>FF87h</td>
<td>FF88h</td>
<td>FF89h</td>
</tr>
<tr class="even">
<td><strong>0AF0h</strong></td>
<td>FF8Ah</td>
<td>FF8Bh</td>
<td>FF8Ch</td>
<td>FF8Dh</td>
<td>FF8Eh</td>
<td>FF8Fh</td>
<td>FF90h</td>
<td>FF91h</td>
</tr>
<tr class="odd">
<td><strong>0AF8h</strong></td>
<td>FF92h</td>
<td>FF93h</td>
<td>FF94h</td>
<td>FF95h</td>
<td>FF96h</td>
<td>FF97h</td>
<td>FF98h</td>
<td>FF99h</td>
</tr>
<tr class="even">
<td><strong>0B00h</strong></td>
<td>FF9Ah</td>
<td>FF9Bh</td>
<td>FF9Ch</td>
<td>FF9Dh</td>
<td>FF9Eh</td>
<td>FF9Fh</td>
<td>FFA0h</td>
<td>FFA1h</td>
</tr>
<tr class="odd">
<td><strong>0B08h</strong></td>
<td>FFA2h</td>
<td>FFA3h</td>
<td>FFA4h</td>
<td>FFA5h</td>
<td>FFA6h</td>
<td>FFA7h</td>
<td>FFA8h</td>
<td>FFA9h</td>
</tr>
<tr class="even">
<td><strong>0B10h</strong></td>
<td>FFAAh</td>
<td>FFABh</td>
<td>FFACh</td>
<td>FFADh</td>
<td>FFAEh</td>
<td>FFAFh</td>
<td>FFB0h</td>
<td>FFB1h</td>
</tr>
<tr class="odd">
<td><strong>0B18h</strong></td>
<td>FFB2h</td>
<td>FFB3h</td>
<td>FFB4h</td>
<td>FFB5h</td>
<td>FFB6h</td>
<td>FFB7h</td>
<td>FFB8h</td>
<td>FFB9h</td>
</tr>
<tr class="even">
<td><strong>0B20h</strong></td>
<td>FFBAh</td>
<td>FFBBh</td>
<td>FFBCh</td>
<td>FFBDh</td>
<td>FFBEh</td>
<td>FFBFh</td>
<td>FFC0h</td>
<td>FFC1h</td>
</tr>
<tr class="odd">
<td><strong>0B28h</strong></td>
<td>FFC2h</td>
<td>FFC3h</td>
<td>FFC4h</td>
<td>FFC5h</td>
<td>FFC6h</td>
<td>FFC7h</td>
<td>FFC8h</td>
<td>FFC9h</td>
</tr>
<tr class="even">
<td><strong>0B30h</strong></td>
<td>FFCAh</td>
<td>FFCBh</td>
<td>FFCCh</td>
<td>FFCDh</td>
<td>FFCEh</td>
<td>FFCFh</td>
<td>FFD0h</td>
<td>FFD1h</td>
</tr>
<tr class="odd">
<td><strong>0B38h</strong></td>
<td>FFD2h</td>
<td>FFD3h</td>
<td>FFD4h</td>
<td>FFD5h</td>
<td>FFD6h</td>
<td>FFD7h</td>
<td>FFD8h</td>
<td>FFD9h</td>
</tr>
<tr class="even">
<td><strong>0B40h</strong></td>
<td>FFDAh</td>
<td>FFDBh</td>
<td>FFDCh</td>
<td>FFDDh</td>
<td>FFDEh</td>
<td>FFDFh</td>
<td>FFE0h</td>
<td>FFE1h</td>
</tr>
<tr class="odd">
<td><strong>0B48h</strong></td>
<td>FFE2h</td>
<td>FFE3h</td>
<td>FFE4h</td>
<td>FFE5h</td>
<td>FFE6h</td>
<td>FFE7h</td>
<td>FFE8h</td>
<td>FFE9h</td>
</tr>
<tr class="even">
<td><strong>0B50h</strong></td>
<td>FFEAh</td>
<td>FFEBh</td>
<td>FFECh</td>
<td>FFEDh</td>
<td>FFEEh</td>
<td>FFEFh</td>
<td>FFF0h</td>
<td>FFF1h</td>
</tr>
<tr class="odd">
<td><strong>0B58h</strong></td>
<td>FFF2h</td>
<td>FFF3h</td>
<td>FFF4h</td>
<td>FFF5h</td>
<td>FFF6h</td>
<td>FFF7h</td>
<td>FFF8h</td>
<td>FFF9h</td>
</tr>
<tr class="even">
<td><strong>0B60h</strong></td>
<td>FFFAh</td>
<td>FFFBh</td>
<td>FFFCh</td>
<td>FFFDh</td>
<td>FFFEh</td>
<td>FFFFh</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Volume Label Directory Entry
----------------------------

The Volume Label is a Unicode string which enables end users to
distinguish their storage volumes. In the exFAT file system, the Volume
Label exists as a critical primary directory entry in the root directory
(see Table 26). The valid number of Volume Label directory entries
ranges from 0 to 1.

**Volume Label DirectoryEntry Structure**

<table>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><p><strong>Offset</strong></p>
<p><strong>(byte)</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>(byte)</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>EntryType</td>
<td>0</td>
<td>1</td>
<td>This field is mandatory and Section 7.3.1 defines its contents.</td>
</tr>
<tr class="even">
<td>CharacterCount</td>
<td>1</td>
<td>1</td>
<td>This field is mandatory and Section 7.3.2 defines its contents.</td>
</tr>
<tr class="odd">
<td>VolumeLabel</td>
<td>2</td>
<td>22</td>
<td>This field is mandatory and Section 7.3.3 defines its contents.</td>
</tr>
<tr class="even">
<td>Reserved</td>
<td>24</td>
<td>8</td>
<td>This field is mandatory and its contents are reserved.</td>
</tr>
</tbody>
</table>

### EntryType Field

The EntryType field shall conform to the definition provided in the
Generic Primary DirectoryEntry template (see Section 6.3.1).

#### TypeCode Field

The TypeCode field shall conform to the definition provided in the
Generic Primary DirectoryEntry template (see Section 6.3.1.1).

For the Volume Label directory entry, the valid value for this field is
3.

#### TypeImportance Field

The TypeImportance field shall conform to the definition provided in the
Generic Primary DirectoryEntry template (see Section 6.3.1.2).

For the Volume Label directory entry, the valid value for this field is
0.

#### TypeCategory Field

The TypeCategory field shall conform to the definition provided in the
Generic Primary DirectoryEntry template (see Section 6.3.1.3).

#### InUse Field

The InUse field shall conform to the definition provided in the Generic
Primary DirectoryEntry template (see Section 6.3.1.4).

### CharacterCount Field

The CharacterCount field shall contain the length of the Unicode string
the VolumeLabel field contains.

The valid range of values for this field shall be:

-   At least 0, which means the Unicode string is 0 characters long
    (which is the equivalent of no volume label)

-   At most 11, which means the Unicode string is 11 characters long

### VolumeLabel Field

The VolumeLabel field shall contain a Unicode string, which is the
user-friendly name of the volume. The VolumeLabel field has the same set
of invalid characters as the FileName field of the File Name directory
entry (see Section 7.7.3).

File Directory Entry
--------------------

File directory entries describe files and directories. They are critical
primary directory entries and any directory may contain zero or more
File directory entries (see Table 27). For a File directory entry to be
valid, exactly one Stream Extension directory entry and at least one
File Name directory entry must immediately follow the File directory
entry (see Sections 7.6 and 7.7, respectively).

**File DirectoryEntry**

<table>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><p><strong>Offset</strong></p>
<p><strong>(byte)</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>(byte)</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>EntryType</td>
<td>0</td>
<td>1</td>
<td>This field is mandatory and Section 7.4.1 defines its contents.</td>
</tr>
<tr class="even">
<td>SecondaryCount</td>
<td>1</td>
<td>1</td>
<td>This field is mandatory and Section 7.4.2 defines its contents.</td>
</tr>
<tr class="odd">
<td>SetChecksum</td>
<td>2</td>
<td>2</td>
<td>This field is mandatory and Section 7.4.3 defines its contents.</td>
</tr>
<tr class="even">
<td>FileAttributes</td>
<td>4</td>
<td>2</td>
<td>This field is mandatory and Section 7.4.4 defines its contents.</td>
</tr>
<tr class="odd">
<td>Reserved1</td>
<td>6</td>
<td>2</td>
<td>This field is mandatory and its contents are reserved.</td>
</tr>
<tr class="even">
<td>CreateTimestamp</td>
<td>8</td>
<td>4</td>
<td>This field is mandatory and Section 7.4.5 defines its contents.</td>
</tr>
<tr class="odd">
<td>LastModifiedTimestamp</td>
<td>12</td>
<td>4</td>
<td>This field is mandatory and Section 7.4.6 defines its contents.</td>
</tr>
<tr class="even">
<td>LastAccessedTimestamp</td>
<td>16</td>
<td>4</td>
<td>This field is mandatory and Section 7.4.7 defines its contents.</td>
</tr>
<tr class="odd">
<td>Create10msIncrement</td>
<td>20</td>
<td>1</td>
<td>This field is mandatory and Section 7.4.5 defines its contents.</td>
</tr>
<tr class="even">
<td>LastModified10msIncrement</td>
<td>21</td>
<td>1</td>
<td>This field is mandatory and Section 7.4.6 defines its contents.</td>
</tr>
<tr class="odd">
<td>CreateUtcOffset</td>
<td>22</td>
<td>1</td>
<td>This field is mandatory and Section 7.4.5 defines its contents.</td>
</tr>
<tr class="even">
<td>LastModifiedUtcOffset</td>
<td>23</td>
<td>1</td>
<td>This field is mandatory and Section 7.4.6 defines its contents.</td>
</tr>
<tr class="odd">
<td>LastAccessedUtcOffset</td>
<td>24</td>
<td>1</td>
<td>This field is mandatory and Section 7.4.7 defines its contents.</td>
</tr>
<tr class="even">
<td>Reserved2</td>
<td>25</td>
<td>7</td>
<td>This field is mandatory and its contents are reserved.</td>
</tr>
</tbody>
</table>

### EntryType Field

The EntryType field shall conform to the definition provided in the
Generic Primary DirectoryEntry template (see Section 6.3.1).

#### TypeCode Field

The TypeCode field shall conform to the definition provided in the
Generic Primary DirectoryEntry template (see Section 6.3.1.1).

For a File directory entry, the valid value for this field is 5.

#### TypeImportance Field

The TypeImportance field shall conform to the definition provided in the
Generic Primary DirectoryEntry template (see Section 6.3.1.2).

For a File directory entry, the valid value for this field is 0.

#### TypeCategory Field

The TypeCategory field shall conform to the definition provided in the
Generic Primary DirectoryEntry template (see Section 6.3.1.3).

#### InUse Field

The InUse field shall conform to the definition provided in the Generic
Primary DirectoryEntry template (see Section 6.3.1.4).

### SecondaryCount Field

The SecondaryCount field shall conform to the definition provided in the
Generic Primary DirectoryEntry template (see Section 6.3.2).

### SetChecksum Field

The SetChecksum field shall conform to the definition provided in the
Generic Primary DirectoryEntry template (see Section 6.3.3).

### FileAttributes Field

The FileAttributes field contains flags (see Table 28).

**FileAttributes Field Structure**

<table>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><p><strong>Offset</strong></p>
<p><strong>(bit)</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>(bits)</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ReadOnly</td>
<td>0</td>
<td>1</td>
<td>This field is mandatory and conforms to the MS-DOS definition.</td>
</tr>
<tr class="even">
<td>Hidden</td>
<td>1</td>
<td>1</td>
<td>This field is mandatory and conforms to the MS-DOS definition.</td>
</tr>
<tr class="odd">
<td>System</td>
<td>2</td>
<td>1</td>
<td>This field is mandatory and conforms to the MS-DOS definition.</td>
</tr>
<tr class="even">
<td>Reserved1</td>
<td>3</td>
<td>1</td>
<td>This field is mandatory and its contents are reserved.</td>
</tr>
<tr class="odd">
<td>Directory</td>
<td>4</td>
<td>1</td>
<td>This field is mandatory and conforms to the MS-DOS definition.</td>
</tr>
<tr class="even">
<td>Archive</td>
<td>5</td>
<td>1</td>
<td>This field is mandatory and conforms to the MS-DOS definition.</td>
</tr>
<tr class="odd">
<td>Reserved2</td>
<td>6</td>
<td>10</td>
<td>This field is mandatory and its contents are reserved.</td>
</tr>
</tbody>
</table>

### CreateTimestamp, Create10msIncrement, and CreateUtcOffset Fields

In combination, the CreateTimestamp and CreateTime10msIncrement fields
shall describe the local date and time the given file/directory was
created. The CreateUtcOffset field describes the offset of local date
and time from UTC. Implementations shall set these fields upon creation
of the given directory entry set.

These fields shall conform to the definitions of the Timestamp,
10msIncrement, and UtcOffset fields (see Sections 7.4.8, 7.4.9, and
7.4.10, respectively).

### LastModifiedTimestamp, LastModified10msIncrement, and LastModifiedUtcOffset Fields

In combination, the LastModifiedTimestamp and
LastModifiedTime10msIncrement fields shall describe the local date and
time the contents of any of the clusters associated with the given
Stream Extension directory entry were last modified. The
LastModifiedUtcOffset field describes the offset of local date and time
from UTC. Implementations shall update these fields:

1.  After modifying the contents of any of the clusters associated with
    the given Stream Extension directory entry (except for contents
    which exist beyond the point the ValidDataLength field describes)

2.  Upon changing the values of either the ValidDataLength or DataLength
    fields

These fields shall conform to the definitions of the Timestamp,
10msIncrement, and UtcOffset fields (see Sections 7.4.8, 7.4.9, and
7.4.10, respectively).

### LastAccessedTimestamp and LastAccessedUtcOffset Fields

The LastAccessedTimestamp field shall describe the local date and time
the contents of any of the clusters associated with the given Stream
Extension directory entry were last accessed. The LastAccessedUtcOffset
field describes the offset of local date and time from UTC.
Implementations shall update these fields:

1.  After modifying the contents of any of the clusters associated with
    the given Stream Extension directory entry (except for contents
    which exist beyond the ValidDataLength)

2.  Upon changing the values of either the ValidDataLength or DataLength
    fields

Implementations should update these fields after reading the contents of
any of the clusters associated with the given Stream Extension directory
entry.

These fields shall conform to the definitions of the Timestamp and
UtcOffset fields (see Sections 7.4.8 and 7.4.10, respectively).

### Timestamp Fields

Timestamp fields describe both local date and time, down to a two-second
resolution (see Table 29).

**Timestamp Field Structure**

<table>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><p><strong>Offset</strong></p>
<p><strong>(bit)</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>(bits)</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DoubleSeconds</td>
<td>0</td>
<td>5</td>
<td>This field is mandatory and Section 7.4.8.1 defines its contents.</td>
</tr>
<tr class="even">
<td>Minute</td>
<td>5</td>
<td>6</td>
<td>This field is mandatory and Section 7.4.8.2 defines its contents.</td>
</tr>
<tr class="odd">
<td>Hour</td>
<td>11</td>
<td>5</td>
<td>This field is mandatory and Section 7.4.8.3 defines its contents.</td>
</tr>
<tr class="even">
<td>Day</td>
<td>16</td>
<td>5</td>
<td>This field is mandatory and Section 7.4.8.4 defines its contents.</td>
</tr>
<tr class="odd">
<td>Month</td>
<td>21</td>
<td>4</td>
<td>This field is mandatory and Section 7.4.8.5 defines its contents.</td>
</tr>
<tr class="even">
<td>Year</td>
<td>25</td>
<td>7</td>
<td>This field is mandatory and Section 7.4.8.6 defines its contents.</td>
</tr>
</tbody>
</table>

#### DoubleSeconds Field

The DoubleSeconds field shall describe the seconds portion of the
Timestamp field, in two-second multiples.

The valid range of values for this field shall be:

-   0, which represents 0 seconds

-   29, which represents 58 seconds

#### Minute Field

The Minute field shall describe the minutes portion of the Timestamp
field.

The valid range of values for this field shall be:

-   0, which represents 0 minutes

-   59, which represents 59 minutes

#### Hour Field

The Hour field shall describe the hours portion of the Timestamp field.

The valid range of values for this field shall be:

-   0, which represents 00:00 hours

-   23, which represents 23:00 hours

#### Day Field

The Day field shall describe the day portion of the Timestamp field.

The valid range of values for this field shall be:

-   1, which is the first day of the given month

-   The last day of the given month (the given month defines the number
    of valid days)

#### Month Field

The Month field shall describe the month portion of the Timestamp field.

The valid range of values for this field shall be:

-   At least 1, which represents January

-   At most 12, which represents December

#### Year Field

The Year field shall describe the year portion of the Timestamp field,
relative to the year 1980. This field represents the year 1980 with the
value 0 and the year 2107 with the value 127.

All possible values for this field are valid.

### 10msIncrement Fields

10msIncrement fields shall provide additional time resolution to their
corresponding Timestamp fields in ten-millisecond multiples.

The valid range of values for these fields shall be:

-   At least 0, which represents 0 milliseconds

-   At most 199, which represents 1990 milliseconds

### UtcOffset Fields

UtcOffset fields (see Table 30) shall describe the offset from UTC to
the local date and time their corresponding Timestamp and 10msIncrement
fields describe. The offset from UTC to the local date and time includes
the effects of time zones and other date-time adjustments, such as
daylight saving and regional summer time changes.

**UtcOffset Field Structure**

<table>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><p><strong>Offset</strong></p>
<p><strong>(bit)</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>(bits)</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>OffsetFromUtc</td>
<td>0</td>
<td>7</td>
<td>This field is mandatory and Section 7.4.10.1 defines its contents.</td>
</tr>
<tr class="even">
<td>OffsetValid</td>
<td>7</td>
<td>1</td>
<td>This field is mandatory and Section 7.4.10.2 defines its contents.</td>
</tr>
</tbody>
</table>

#### OffsetFromUtc Field

The OffsetFromUtc field shall describe the offset from UTC of the local
date and time the related Timestamp and 10msIncrement fields contains.
This field describes the offset from UTC in 15 minute intervals (see
Table 31).

**Meaning of the Values of the OffsetFromUtc Field**

<table>
<thead>
<tr class="header">
<th><strong>Value</strong></th>
<th><strong>Signed Decimal Equivalent</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>3Fh</td>
<td>63</td>
<td>Local date and time is UTC + 15:45</td>
</tr>
<tr class="even">
<td>3Eh</td>
<td>62</td>
<td>Local date and time is UTC + 15:30</td>
</tr>
<tr class="odd">
<td><p>.</p>
<p>.</p>
<p>.</p></td>
<td><p>.</p>
<p>.</p>
<p>.</p></td>
<td><p>.</p>
<p>.</p>
<p>.</p></td>
</tr>
<tr class="even">
<td>01h</td>
<td>1</td>
<td>Local date and time is UTC + 00:15</td>
</tr>
<tr class="odd">
<td>00h</td>
<td>0</td>
<td>Local date and time is UTC</td>
</tr>
<tr class="even">
<td>7Fh</td>
<td>-1</td>
<td>Local date and time is UTC – 00:15</td>
</tr>
<tr class="odd">
<td><p>.</p>
<p>.</p>
<p>.</p></td>
<td><p>.</p>
<p>.</p>
<p>.</p></td>
<td><p>.</p>
<p>.</p>
<p>.</p></td>
</tr>
<tr class="even">
<td>41h</td>
<td>-63</td>
<td>Local date and time is UTC – 15:45</td>
</tr>
<tr class="odd">
<td>40h</td>
<td>-64</td>
<td>Local date and time is UTC – 16:00</td>
</tr>
</tbody>
</table>

As the table above indicates, all possible values for this field are
valid. However, implementations should only record the value 00h for
this field when:

1.  Local date and time are actually the same as UTC, in which case the
    value of the OffsetValid field shall be 1

2.  Local date and time are not known, in which case the value of the
    OffsetValid field shall be 1 and implementations shall consider UTC
    to be local date and time

3.  UTC is not known, in which case the value of the OffsetValid field
    shall be 0

If the local date and time offset from UTC happens to not be a multiple
of 15 minute intervals, then implementations shall record 00h in the
OffsetFromUtc field and shall consider UTC to be local date and time.

#### OffsetValid Field

The OffsetValid field shall describe whether the contents of the
OffsetFromUtc field are valid or not, as follows:

-   0, which means the contents of the OffsetFromUtc field are invalid
    > and shall be 00h

-   1, which means the contents of the OffsetFromUtc field are valid

Implementations should only set this field to the value 0 when UTC is
not available for computing the value of the OffsetFromUtc field. If
this field contains the value 0, then implementations shall treat the
Timestamp and 10msIncrement fields as having the same UTC offset as the
current local date and time.

Volume GUID Directory Entry
---------------------------

The Volume GUID directory entry contains a GUID which enables
implementations to uniquely and programmatically distinguish volumes.
The Volume GUID exists as a benign primary directory entry in the root
directory (see Table 32). The valid number of Volume GUID directory
entries ranges from 0 to 1.

**Volume GUID DirectoryEntry**

<table>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><p><strong>Offset</strong></p>
<p><strong>(byte)</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>(byte)</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>EntryType</td>
<td>0</td>
<td>1</td>
<td>This field is mandatory and Section 7.5.1 defines its contents.</td>
</tr>
<tr class="even">
<td>SecondaryCount</td>
<td>1</td>
<td>1</td>
<td>This field is mandatory and Section 7.5.2 defines its contents.</td>
</tr>
<tr class="odd">
<td>SetChecksum</td>
<td>2</td>
<td>2</td>
<td>This field is mandatory and Section 7.5.3 defines its contents.</td>
</tr>
<tr class="even">
<td>GeneralPrimaryFlags</td>
<td>4</td>
<td>2</td>
<td>This field is mandatory and Section 7.5.4 defines its contents.</td>
</tr>
<tr class="odd">
<td>VolumeGuid</td>
<td>6</td>
<td>16</td>
<td>This field is mandatory and Section 7.5.5 defines its contents.</td>
</tr>
<tr class="even">
<td>Reserved</td>
<td>22</td>
<td>10</td>
<td>This field is mandatory and its contents are reserved.</td>
</tr>
</tbody>
</table>

### EntryType Field

The EntryType field shall conform to the definition provided in the
Generic Primary DirectoryEntry template (see Section 6.3.1).

#### TypeCode Field

The TypeCode field shall conform to the definition provided in the
Generic Primary DirectoryEntry template (see Section 6.3.1.1).

For the Volume GUID directory entry, the valid value for this field is
0.

#### TypeImportance Field

The TypeImportance field shall conform to the definition provided in the
Generic Primary DirectoryEntry template (see Section 6.3.1.2).

For the Volume GUID directory entry, the valid value for this field is
1.

#### TypeCategory Field

The TypeCategory field shall conform to the definition provided in the
Generic Primary DirectoryEntry template (see Section 6.3.1.3).

#### InUse Field

The InUse field shall conform to the definition provided in the Generic
Primary DirectoryEntry template (see Section 6.3.1.4).

### SecondaryCount Field

The SecondaryCount field shall conform to the definition provided in the
Generic Primary DirectoryEntry template (see Section 6.3.2).

For the Volume GUID directory entry, the valid value for this field is
0.

### SetChecksum Field

The SetChecksum field shall conform to the definition provided in the
Generic Primary DirectoryEntry template (see Section 6.3.3).

### GeneralPrimaryFlags Field

The GeneralPrimaryFlags field shall conform to the definition provided
in the Generic Primary DirectoryEntry template (see Section 6.3.4) and
defines the contents of the CustomDefined field to be reserved.

#### AllocationPossible Field

The AllocationPossible field shall conform to the definition provided in
the Generic Primary DirectoryEntry template (see Section 6.3.4).

For the Volume GUID directory entry, the valid value for this field is
0.

#### NoFatChain Field

The NoFatChain field shall conform to the definition provided in the
Generic Primary DirectoryEntry template (see Section 6.3.4).

### VolumeGuid Field

The VolumeGuid field shall contain a GUID which uniquely identifies the
given volume.

All possible values for this field are valid, except the null GUID,
which is {00000000-0000-0000-0000-000000000000}.

Stream Extension Directory Entry
--------------------------------

The Stream Extension directory entry is a critical secondary directory
entry in File directory entry sets (see Table 33). The valid number of
Stream Extension directory entries in a File directory entry set is 1.
Further, this directory entry is valid only if it immediately follows
the File directory entry.

**Stream Extension DirectoryEntry**

<table>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><p><strong>Offset</strong></p>
<p><strong>(byte)</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>(byte)</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>EntryType</td>
<td>0</td>
<td>1</td>
<td>This field is mandatory and Section 7.6.1 defines its contents.</td>
</tr>
<tr class="even">
<td>GeneralSecondaryFlags</td>
<td>1</td>
<td>1</td>
<td>This field is mandatory and Section 7.6.2 defines its contents.</td>
</tr>
<tr class="odd">
<td>Reserved1</td>
<td>2</td>
<td>1</td>
<td>This field is mandatory and its contents are reserved.</td>
</tr>
<tr class="even">
<td>NameLength</td>
<td>3</td>
<td>1</td>
<td>This field is mandatory and Section 7.6.3 defines its contents.</td>
</tr>
<tr class="odd">
<td>NameHash</td>
<td>4</td>
<td>2</td>
<td>This field is mandatory and Section 7.6.4 defines its contents.</td>
</tr>
<tr class="even">
<td>Reserved2</td>
<td>6</td>
<td>2</td>
<td>This field is mandatory and its contents are reserved.</td>
</tr>
<tr class="odd">
<td>ValidDataLength</td>
<td>8</td>
<td>8</td>
<td>This field is mandatory and Section 7.6.5 defines its contents.</td>
</tr>
<tr class="even">
<td>Reserved3</td>
<td>16</td>
<td>4</td>
<td>This field is mandatory and its contents are reserved.</td>
</tr>
<tr class="odd">
<td>FirstCluster</td>
<td>20</td>
<td>4</td>
<td>This field is mandatory and Section 7.6.6 defines its contents.</td>
</tr>
<tr class="even">
<td>DataLength</td>
<td>24</td>
<td>8</td>
<td>This field is mandatory and Section 7.6.7 defines its contents.</td>
</tr>
</tbody>
</table>

### EntryType Field

The EntryType field shall conform to the definition provided in the
Generic Secondary DirectoryEntry template (see Section 6.4.1).

#### TypeCode Field

The TypeCode field shall conform to the definition provided in the
Generic Secondary DirectoryEntry template (see Section 6.4.1.1).

For the Stream Extension directory entry, the valid value for this field
is 0.

#### TypeImportance Field

The TypeImportance field shall conform to the definition provided in the
Generic Secondary DirectoryEntry template (see Section 6.4.1.2).

For the Stream Extension directory entry, the valid value for this field
is 0.

#### TypeCategory Field

The TypeCategory field shall conform to the definition provided in the
Generic Secondary DirectoryEntry template (see Section 6.4.1.3).

#### InUse Field

The InUse field shall conform to the definition provided in the Generic
Secondary DirectoryEntry template (see Section 6.4.1.4).

### GeneralSecondaryFlags Field

The GeneralSecondaryFlags field shall conform to the definition provided
in the Generic Secondary DirectoryEntry template (see Section 6.4.2) and
defines the contents of the CustomDefined field to be reserved.

#### AllocationPossible Field

The AllocationPossible field shall conform to the definition provided in
the Generic Secondary DirectoryEntry template (see Section 6.4.2.1).

For the Stream Extension directory entry, the valid value for this field
is 1.

#### NoFatChain Field

The NoFatChain field shall conform to the definition provided in the
Generic Secondary DirectoryEntry template (see Section 6.4.2.2).

### NameLength Field

The NameLength field shall contain the length of the Unicode string the
subsequent File Name directory entries (see Section 7.7) collectively
contain.

The valid range of values for this field shall be:

-   At least 1, which is the shortest possible file name

-   At most 255, which is the longest possible file name

The value of the NameLength field also affects the number File Name
Directory Entries (see Section 7.7).

### NameHash Field

The NameHash field shall contain a 2-byte hash (see Figure 4) of the
up-cased file name. This enables implementations to perform a quick
comparison when searching for a file by name. Importantly, the NameHash
provides a sure verification of a mismatch. Implementations shall verify
all NameHash matches with a comparison of the up-cased file name.

**NameHash Computation**

<table>
<tbody>
<tr class="odd">
<td><p>UInt16 NameHash</p>
<p>(</p>
<p>WCHAR * FileName, // points to an in-memory copy of the up-cased file name</p>
<p>UCHAR NameLength</p>
<p>)</p>
<p>{</p>
<p>UCHAR * Buffer = (UCHAR *)FileName;</p>
<p>UInt16 NumberOfBytes = (UInt16)NameLength * 2;</p>
<p>UInt16 Hash = 0;</p>
<p>UInt16 Index;</p>
<p>for (Index = 0; Index &lt; NumberOfBytes; Index++)</p>
<p>{</p>
<p>Hash = ((Hash&amp;1) ? 0x8000 : 0) + (Hash&gt;&gt;1) + (UInt16)Buffer[Index];</p>
<p>}</p>
<p>return Hash;</p>
<p>}</p></td>
</tr>
</tbody>
</table>

### ValidDataLength Field

The ValidDataLength field shall describe how far into the data stream
user data has been written. Implementations shall update this field as
they write data further out into the data stream. On the storage media,
the data between the valid data length and the data length of the data
stream is undefined. Implementations shall return zeroes for read
operations beyond the valid data length.

If the corresponding File directory entry describes a directory, then
the only valid value for this field is equal to the value of the
DataLength field. Otherwise, the range of valid values for this field
shall be:

-   At least 0, which means no user data has been written out to the
    data stream

-   At most DataLength, which means user data has been written out to
    the entire length of the data stream

### FirstCluster Field

The FirstCluster field shall conform to the definition provided in the
Generic Secondary DirectoryEntry template (see Section 6.4.3).

This field shall contain the index of the first cluster of the data
stream, which hosts the user data.

### DataLength Field

The DataLength field shall conform to the definition provided in the
Generic Secondary DirectoryEntry template (see Section 6.4.4).

If the corresponding File directory entry describes a directory, then
the valid value for this field is the entire size of the associated
allocation, in bytes, which may be 0. Further, for directories, the
maximum value for this field is 256MB.

File Name Directory Entry
-------------------------

File Name directory entries are critical secondary directory entries in
File directory entry sets (see Table 34). The valid number of File Name
directory entries in a File directory entry set is NameLength / 15,
rounded up to the nearest integer. Further, File Name directory entries
are valid only if they immediately follow the Stream Extension directory
entry as a consecutive series. File Name directory entries combine to
form the file name for the File directory entry set.

All children of a given directory entry shall have unique File Name
Directory Entry Sets. That is to say there can be no duplicate file or
directory names after up-casing within any one directory.

**File Name DirectoryEntry**

<table>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><p><strong>Offset</strong></p>
<p><strong>(byte)</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>(byte)</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>EntryType</td>
<td>0</td>
<td>1</td>
<td>This field is mandatory and Section 7.7.1 defines its contents.</td>
</tr>
<tr class="even">
<td>GeneralSecondaryFlags</td>
<td>1</td>
<td>1</td>
<td>This field is mandatory and Section 7.7.2 defines its contents.</td>
</tr>
<tr class="odd">
<td>FileName</td>
<td>2</td>
<td>30</td>
<td>This field is mandatory and Section 7.7.3 defines its contents.</td>
</tr>
</tbody>
</table>

### EntryType Field

The EntryType field shall conform to the definition provided in the
Generic Secondary DirectoryEntry template (see Section 6.4.1).

#### TypeCode Field

The TypeCode field shall conform to the definition provided in the
Generic Secondary DirectoryEntry template (see Section 6.4.1.1).

For the Stream Extension directory entry, the valid value for this field
is 1.

#### TypeImportance Field

The TypeImportance field shall conform to the definition provided in the
Generic Secondary DirectoryEntry template (see Section 6.4.1.2).

For the Stream Extension directory entry, the valid value for this field
is 0.

#### TypeCategory Field

The TypeCategory field shall conform to the definition provided in the
Generic Secondary DirectoryEntry template (see Section 6.4.1.3).

#### InUse Field

The InUse field shall conform to the definition provided in the Generic
Secondary DirectoryEntry template (see Section 6.4.1.4).

### GeneralSecondaryFlags Field

The GeneralSecondaryFlags field shall conform to the definition provided
in the Generic Secondary DirectoryEntry template (see Section 6.4.2) and
defines the contents of the CustomDefined field to be reserved.

#### AllocationPossible Field

The AllocationPossible field shall conform to the definition provided in
the Generic Secondary DirectoryEntry template (see Section 6.4.2.1).

For the Stream Extension directory entry, the valid value for this field
is 0.

#### NoFatChain Field

The NoFatChain field shall conform to the definition provided in the
Generic Secondary DirectoryEntry template (see Section 6.4.2.2).

### FileName Field

The FileName field shall contain a Unicode string, which is a portion of
the file name. In the order File Name directory entries exist in a File
directory entry set, FileName fields concatenate to form the file name
for the File directory entry set. Given the length of the FileName
field, 15 characters, and the maximum number of File Name directory
entries, 17, the maximum length of the final, concatenated file name is
255.

The concatenated file name has the same set of illegal characters as
other FAT-based file systems (see Table 35). Implementations should set
the unused characters of FileName fields to the value 0000h.

**Invalid FileName Characters**

| **Character Code** | **Description** | **Character Code** | **Description**   | **Character Code** | **Description** |
|--------------------|-----------------|--------------------|-------------------|--------------------|-----------------|
| 0000h              | Control code    | 0001h              | Control code      | 0002h              | Control code    |
| 0003h              | Control code    | 0004h              | Control code      | 0005h              | Control code    |
| 0006h              | Control code    | 0007h              | Control code      | 0008h              | Control code    |
| 0009h              | Control code    | 000Ah              | Control code      | 000Bh              | Control code    |
| 000Ch              | Control code    | 000Dh              | Control code      | 000Eh              | Control code    |
| 000Fh              | Control code    | 0010h              | Control code      | 0011h              | Control code    |
| 0012h              | Control code    | 0013h              | Control code      | 0014h              | Control code    |
| 0015h              | Control code    | 0016h              | Control code      | 0017h              | Control code    |
| 0018h              | Control code    | 0019h              | Control code      | 001Ah              | Control code    |
| 001Bh              | Control code    | 001Ch              | Control code      | 001Dh              | Control code    |
| 001Eh              | Control code    | 001Fh              | Control code      | 0022h              | Quotation mark  |
| 002Ah              | Asterisk        | 002Fh              | Forward slash     | 003Ah              | Colon           |
| 003Ch              | Less-than sign  | 003Eh              | Greater-than sign | 003Fh              | Question mark   |
| 005Ch              | Back slash      | 007Ch              | Vertical bar      |                    |                 |

The file names "." and ".." have the special meaning of "this directory"
and "containing directory", respectively. Implementations shall not
record either of these reserved file names in the FileName field.
However, implementations may generate these two file names in directory
listings to refer to the directory being listed and the containing
directory.

Implementations may wish to restrict file and directory names to just
the ASCII character set. If so they should limit their character use to
the range of valid characters in the first 128 Unicode entries. They
must still store file and directory names in Unicode on the volume and
translate to/from ASCII/Unicode when interfacing with the user.

Vendor Extension Directory Entry
--------------------------------

The Vendor Extension directory entry is a benign secondary directory
entry in File directory entry sets (see Table 36). A File directory
entry set may contain any number of Vendor Extension directory entries,
up to the limit of secondary directory entries, less the number of other
secondary directory entries. Further, Vendor Extension directory entries
are valid only if they do not precede the required Stream Extension and
File Name directory entries.

Vendor Extension directory entries enable vendors to have unique,
vendor-specific directory entries in individual File directory entry
sets via the VendorGuid field (see Table 36). Unique directory entries
effectively enable vendors to extend the exFAT file system. Vendors may
define the contents of the VendorDefined field (see Table 36). Vendor
implementations may maintain the contents of the VendorDefined field and
may provide vendor-specific functionality.

Implementations which do not recognize the GUID of a Vendor Extension
directory entry shall treat the directory entry the same as any other
unrecognized benign secondary directory entry (see Section 8.2).

**Vendor Extension DirectoryEntry**

<table>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><p><strong>Offset</strong></p>
<p><strong>(byte)</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>(byte)</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>EntryType</td>
<td>0</td>
<td>1</td>
<td>This field is mandatory and Section 7.8.1 defines its contents.</td>
</tr>
<tr class="even">
<td>GeneralSecondaryFlags</td>
<td>1</td>
<td>1</td>
<td>This field is mandatory and Section 7.8.2 defines its contents.</td>
</tr>
<tr class="odd">
<td>VendorGuid</td>
<td>2</td>
<td>16</td>
<td>This field is mandatory and Section 7.8.3 defines its contents.</td>
</tr>
<tr class="even">
<td>VendorDefined</td>
<td>18</td>
<td>14</td>
<td>This field is mandatory and vendors may define its contents.</td>
</tr>
</tbody>
</table>

### EntryType Field

The EntryType field shall conform to the definition provided in the
Generic Secondary DirectoryEntry template (see Section 6.4.1).

#### TypeCode Field

The TypeCode field shall conform to the definition provided in the
Generic Secondary DirectoryEntry template (see Section 6.4.1.1).

For the Vendor Extension directory entry, the valid value for this field
is 0.

#### TypeImportance Field

The TypeImportance field shall conform to the definition provided in the
Generic Secondary DirectoryEntry template (see Section 6.4.1.2).

For the Vendor Extension directory entry, the valid value for this field
is 1.

#### TypeCategory Field

The TypeCategory field shall conform to the definition provided in the
Generic Secondary DirectoryEntry template (see Section 6.4.1.3).

#### InUse Field

The InUse field shall conform to the definition provided in the Generic
Secondary DirectoryEntry template (see Section 6.4.1.4).

### GeneralSecondaryFlags Field

The GeneralSecondaryFlags field shall conform to the definition provided
in the Generic Secondary DirectoryEntry template (see Section 6.4.2) and
defines the contents of the CustomDefined field to be reserved.

#### AllocationPossible Field

The AllocationPossible field shall conform to the definition provided in
the Generic Secondary DirectoryEntry template (see Section 6.4.2.1).

For the Vendor Extension directory entry, the valid value for this field
is 0.

#### NoFatChain Field

The NoFatChain field shall conform to the definition provided in the
Generic Secondary DirectoryEntry template (see Section 6.4.2.2).

### VendorGuid Field

The VendorGuid field shall contain a GUID which uniquely identifies the
given Vendor Extension.

All possible values for this field are valid, except the null GUID,
which is {00000000-0000-0000-0000-000000000000}. However, vendors should
use a GUID-generating tool, such as GuidGen.exe, to select a GUID when
defining their extensions.

The value of this field determines the vendor-specific structure of the
VendorDefined field.

Vendor Allocation Directory Entry
---------------------------------

The Vendor Allocation directory entry is a benign secondary directory
entry in File directory entry sets (see Table 37). A File directory
entry set may contain any number of Vendor Allocation directory entries,
up to the limit of secondary directory entries, less the number of other
secondary directory entries. Further, Vendor Allocation directory
entries are valid only if they do not precede the required Stream
Extension and File Name directory entries.

Vendor Allocation directory entries enable vendors to have unique,
vendor-specific directory entries in individual File directory entry
sets via the VendorGuid field (see Table 37). Unique directory entries
effectively enable vendors to extend the exFAT file system. Vendors may
define the contents of the associated clusters, if any exist. Vendor
implementations may maintain the contents of the associated clusters, if
any, and may provide vendor-specific functionality.

Implementations which do not recognize the GUID of a Vendor Allocation
directory entry shall treat the directory entry the same as any other
unrecognized benign secondary directory entry (see Section 8.2).

**Vendor Allocation DirectoryEntry**

<table>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><p><strong>Offset</strong></p>
<p><strong>(byte)</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>(byte)</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>EntryType</td>
<td>0</td>
<td>1</td>
<td>This field is mandatory and Section 7.9.1 defines its contents.</td>
</tr>
<tr class="even">
<td>GeneralSecondaryFlags</td>
<td>1</td>
<td>1</td>
<td>This field is mandatory and Section 7.9.2 defines its contents.</td>
</tr>
<tr class="odd">
<td>VendorGuid</td>
<td>2</td>
<td>16</td>
<td>This field is mandatory and Section 7.9.3 defines its contents.</td>
</tr>
<tr class="even">
<td>VendorDefined</td>
<td>18</td>
<td>2</td>
<td>This field is mandatory and vendors may define its contents.</td>
</tr>
<tr class="odd">
<td>FirstCluster</td>
<td>20</td>
<td>4</td>
<td>This field is mandatory and Section 7.9.4 defines its contents.</td>
</tr>
<tr class="even">
<td>DataLength</td>
<td>24</td>
<td>8</td>
<td>This field is mandatory and Section 7.9.5 defines its contents.</td>
</tr>
</tbody>
</table>

### EntryType Field

The EntryType field shall conform to the definition provided in the
Generic Secondary DirectoryEntry template (see Section 6.4.1).

#### TypeCode Field

The TypeCode field shall conform to the definition provided in the
Generic Secondary DirectoryEntry template (see Section 6.4.1.1).

For the Vendor Allocation directory entry, the valid value for this
field is 1.

#### TypeImportance Field

The TypeImportance field shall conform to the definition provided in the
Generic Secondary DirectoryEntry template (see Section 6.4.1.2).

For the Vendor Allocation directory entry, the valid value for this
field is 1.

#### TypeCategory Field

The TypeCategory field shall conform to the definition provided in the
Generic Secondary DirectoryEntry template (see Section 6.4.1.3).

#### InUse Field

The InUse field shall conform to the definition provided in the Generic
Secondary DirectoryEntry template (see Section 6.4.1.4).

### GeneralSecondaryFlags Field

The GeneralSecondaryFlags field shall conform to the definition provided
in the Generic Secondary DirectoryEntry template (see Section 6.4.2) and
defines the contents of the CustomDefined field to be reserved.

#### AllocationPossible Field

The AllocationPossible field shall conform to the definition provided in
the Generic Secondary DirectoryEntry template (see Section 6.4.2.1).

For the Vendor Allocation directory entry, the valid value for this
field is 1.

#### NoFatChain Field

The NoFatChain field shall conform to the definition provided in the
Generic Secondary DirectoryEntry template (see Section 6.4.2.2).

### VendorGuid Field

The VendorGuid field shall contain a GUID which uniquely identifies the
given Vendor Allocation.

All possible values for this field are valid, except the null GUID,
which is {00000000-0000-0000-0000-000000000000}. However, vendors should
use a GUID-generating tool, such as GuidGen.exe, to select a GUID when
defining their extensions.

The value of this field determines the vendor-specific structure of the
contents of the associated clusters, if any exist.

### FirstCluster Field

The FirstCluster field shall conform to the definition provided in the
Generic Secondary DirectoryEntry template (see Section 6.4.3).

### DataLength Field

The DataLength field shall conform to the definition provided in the
Generic Secondary DirectoryEntry template (see Section 6.4.4).

TexFAT Padding Directory Entry
------------------------------

This specification, exFAT Revision 1.00 File System Basic Specification,
does not define the TexFAT Padding directory entry. However, its type
code is 1 and its type importance is 1. Implementations of this
specification shall treat TexFAT Padding directory entries the same as
any other unrecognized benign primary directory entries, implementations
shall not move TexFAT Padding directory entries.

 Implementation Notes
====================

Recommended Write Ordering
--------------------------

Implementations should ensure the volume is as resilient as possible to
power faults and other unavoidable failures. When creating new directory
entries or modifying cluster allocations, implementations should
generally follow this writing order:

1.  Set the value of the VolumeDirty field to 1

2.  Update the active FAT, if necessary

3.  Update the active Allocation Bitmap

4.  Create or update the directory entry, if necessary

5.  Clear the value of the VolumeDirty field to 0, if its value prior to
    the first step was 0

When deleting directory entries or freeing cluster allocations,
implementations should follow this writing order:

1.  Set the value of the VolumeDirty field to 1

2.  Delete or update the directory entry, if necessary

3.  Update the active FAT, if necessary

4.  Update the active Allocation Bitmap

5.  Clear the value of the VolumeDirty field to 0, if its value prior to
    the first step was 0

Implications of Unrecognized Directory Entries
----------------------------------------------

Future exFAT specifications of the same major revision number, 1, and
minor revision number higher than 0, may define new benign primary,
critical secondary, and benign secondary directory entries. Only exFAT
specifications of a higher major revision number may define new critical
primary directory entries. Implementations of this specification, exFAT
Revision 1.00 File System Basic Specification, should be able to mount
and access any exFAT volume of major revision number 1 and any minor
revision number. This presents scenarios in which an implementation may
encounter directory entries which it does not recognize. The following
describe implications of these scenarios:

1.  The presence of unrecognized critical primary directory entries in
    the root directory renders the volume invalid. The presence of any
    critical primary directory entry, except File directory entries, in
    any non-root directory, renders the hosting directory invalid.

2.  Implementations shall not modify unrecognized benign primary
    directory entries or their associated cluster allocations. However,
    when deleting a directory, and only when deleting a directory,
    implementations shall delete unrecognized benign primary directory
    entries and free all associated cluster allocations, if any.

3.  Implementations shall not modify unrecognized critical secondary
    directory entries or their associated cluster allocations. The
    presence of one or more unrecognized critical secondary directory
    entries in a directory entry set renders the entire directory entry
    set unrecognized. When deleting a directory entry set which contains
    one or more unrecognized critical secondary directory entries,
    implementations shall free all cluster allocations, if any,
    associated with unrecognized critical secondary directory entries.
    Further, if the directory entry set describes a directory,
    implementations may:

    -   Traverse into the directory

    -   Enumerate the directory entries it contains

    -   Delete contained directory entries

    -   Move contained directory entries to a different directory

> However, implementations shall not:

-   Modify contained directory entries, except delete, as noted

-   Create new contained directory entries

-   Open contained directory entries, except traverse and enumerate, as
    noted

4.  Implementations shall not modify unrecognized benign secondary
    directory entries or their associated cluster allocations.
    Implementations should ignore unrecognized benign secondary
    directory entries. When deleting a directory entry set,
    implementations shall free all cluster allocations, if any,
    associated with unrecognized benign secondary directory entries.

 File System Limits
==================

Sector Size Limits
------------------

The BytesPerSectorShift field defines the lower and upper sector size
limits (which evaluates to **lower limit: 512 bytes; upper limit: 4,096
bytes**).

Cluster Size Limits
-------------------

The SectorsPerClusterShift field defines the lower and upper cluster
size limits (**lower limit: 1 sector; upper limit: 25 --
BytesPerSectorShift sectors**, which evaluates to 32MB).

Cluster Heap Size Limits
------------------------

The Cluster Heap shall contain at least enough space to host the
following basic file system structures: the root directory, all
Allocation Bitmaps, and the Up-case Table.

The lower Cluster Heap size limit is a function of the lower size limit
of each of the basic file system structures which reside in the Cluster
Heap. Even given the smallest possible cluster (512 bytes), each of the
basic file system structures needs no more than one cluster. Therefore,
the **lower limit is: 2 + NumberOfFats clusters**, which evaluates to
either 3 or 4 clusters, depending on the value the NumberOfFats field.

The upper Cluster Heap size limit is a simple function of the maximum
possible number of clusters, which the ClusterCount field defines
(**upper limit: 2^32^ -- 11 clusters**). Regardless of the cluster size,
such a cluster heap has enough space to at least host the basic file
system structures.

Volume Size Limits
------------------

The VolumeLength field defines the lower and upper volume size limits
(lower limit: **2^20^ / 2^BytesPerSectorShift^ sectors**, which
evaluates to 1MB; **upper limit: 2^64^ -- 1 sectors**, which, given the
largest possible sector size, evaluates to approximately 64ZB). However,
this specification recommends no more than 2^24^ -- 2 clusters in the
Cluster Heap (see Section 3.1.9). Therefore, the recommended upper limit
of a volume is: ClusterHeapOffset + (2^24^ -- 2) \*
2^SectorsPerClusterShift^. Given the largest possible cluster size,
32MB, and assuming ClusterHeapOffset is 96MB (enough space for the Main
and Backup Boot regions and only the First FAT), the recommended upper
limit of a volume evaluates to approximately 512TB.

Directory Size Limits
---------------------

The DataLength field of the Stream Extension directory entry defines the
lower and upper directory size limits (**lower limit: 0 bytes; upper
limit: 256MB**). This means a directory may host up to 8,388,608
directory entries (each directory entry consumes 32 bytes). Given the
smallest possible File directory entry set, three directory entries, a
directory may host up to 2,796,202 files.

Appendix
========

Globally Unique Identifiers (GUIDs)
-----------------------------------

A GUID is the Microsoft implementation of a universally unique
identifier. A GUID is a 128-bit value consisting of one group of 8
hexadecimal digits, followed by three groups of 4 hexadecimal digits
each, and followed by one group of 12 hexadecimal digits, for example
{6B29FC40-CA47-1067-B31D-00DD010662DA}, (see Table 38).

**GUID Structure**

<table>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><p><strong>Offset</strong></p>
<p><strong>(byte)</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>(bytes)</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Data1</td>
<td>0</td>
<td>4</td>
<td>This field is mandatory and contains the four bytes from the first group of the GUID (6B29FC40h from the example).</td>
</tr>
<tr class="even">
<td>Data2</td>
<td>4</td>
<td>2</td>
<td>This field is mandatory and contains the two bytes from the second group of the GUID (CA47h from the example).</td>
</tr>
<tr class="odd">
<td>Data3</td>
<td>6</td>
<td>2</td>
<td>This field is mandatory and contains the two bytes from the third group of the GUID (1067h from the example).</td>
</tr>
<tr class="even">
<td>Data4[0]</td>
<td>8</td>
<td>1</td>
<td>This field is mandatory and contains the most significant byte from fourth group of the GUID (B3h from the example).</td>
</tr>
<tr class="odd">
<td>Data4[1]</td>
<td>9</td>
<td>1</td>
<td>This field is mandatory and contains the least significant byte from the fourth group of the GUID (1Dh from the example).</td>
</tr>
<tr class="even">
<td>Data4[2]</td>
<td>10</td>
<td>1</td>
<td>This field is mandatory and contains the first byte from the fifth group of the GUID (00h from the example).</td>
</tr>
<tr class="odd">
<td>Data4[3]</td>
<td>11</td>
<td>1</td>
<td>This field is mandatory and contains the second byte from the fifth group of the GUID (DDh from the example).</td>
</tr>
<tr class="even">
<td>Data4[4]</td>
<td>12</td>
<td>1</td>
<td>This field is mandatory and contains the third byte from the fifth group of the GUID (01h from the example).</td>
</tr>
<tr class="odd">
<td>Data4[5]</td>
<td>13</td>
<td>1</td>
<td>This field is mandatory and contains the fourth byte from the fifth group of the GUID (06h from the example).</td>
</tr>
<tr class="even">
<td>Data4[6]</td>
<td>14</td>
<td>1</td>
<td>This field is mandatory and contains the fifth byte from the fifth group of the GUID (62h from the example).</td>
</tr>
<tr class="odd">
<td>Data4[7]</td>
<td>15</td>
<td>1</td>
<td>This field is mandatory and contains the sixth byte from the fifth group of the GUID (DAh from the example).</td>
</tr>
</tbody>
</table>

Partition Tables
----------------

To ensure interoperability of exFAT volumes in a broad set of usage
scenarios, implementations should use partition type 07h for MBR
partitioned storage and partition GUID
{EBD0A0A2-B9E5-4433-87C0-68B6B72699C7} for GPT partitioned storage.

Documentation Change History
============================

Table 39 describes the history of releases of, corrections to, additions
to, removals from, and clarifications of this document.

**Documentation Change History**

<table>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Description of Change</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>08-Jan-2008</td>
<td><p>First release of the Basic Specification, which includes:</p>
<blockquote>
<p>Section 1, Introduction</p>
<p>Section 2,<br />
Volume Structure</p>
<p>Section 3, Main and Backup Boot Regions</p>
<p>Section 4, File Allocation Table Region</p>
<p>Section 5, Data Region</p>
<p>Section 6, Directory Structure</p>
<p>Section 7, Directory Entry Definitions</p>
<p>Section 8, Implementation Notes</p>
<p>Section 9, File System Limits</p>
<p>Section 10, Appendix</p>
</blockquote></td>
</tr>
<tr class="even">
<td>08-Jun-2008</td>
<td><p>Second release of the Basic Specification, which includes the following changes:</p>
<blockquote>
<p>Addition of Section 11,<br />
Documentation Change History</p>
<p>Addition of the Vendor Extension and Vendor Allocation directory entries in Sections 7.8 and 7.9</p>
<p>Addition of the recommended up-case table in Sections 7.2.5 and 7.2.5.1</p>
<p>Addition of the UtcOffset fields in Section 7.4 and addition of the UTC acronym in Section 1.3</p>
<p>Correction of the size of the CustomDefined field in Table 19</p>
<p>Correction of the valid range of NameLength values in Section 7.6.3</p>
<p>Correction and clarification of the Timestamp and 10msIncrement fields in Section 7.4</p>
<p>Clarification of the Null Parameters structure in Section 3.3</p>
<p>Clarification of the meaning of the values of the NoFatChain field in Section 6.3.4.2</p>
<p>Clarification of the meaning of the values of the DataLength field in Section 6.2.3</p>
<p>Clarification of the VolumeDirty field in Section 3.1.13.2 and recommended write ordering in Section 8.1</p>
<p>Clarification of the MediaFailure field in Section 3.1.13.3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>01-Oct-2008</td>
<td><p>Third release of the Basic Specification, which includes the following changes:</p>
<blockquote>
<p>Addition of SHALL, SHOULD and MAY to field explanations</p>
<p>Addition of UTC definition in Table 2 Section 1.3</p>
<p>Modified sections 1.5, to ensure alignment with the TexFAT specification document.</p>
<p>Clarified the restriction that only Microsoft may define the layout of Directory Entries in Section 6.2</p>
<p>Added clarification that FirstCluster Field shall be zero if the DataLength is zero and NoFatChain is set to Section 6.3.5 and Section 6.4.3</p>
<p>Clarified requirements for valid file directory entries in Section 7.4</p>
<p>Added requirement for unique file and directory names to Section 7.7</p>
<p>Added implementation note for ASCII to the end of Section 7.7.3</p>
</blockquote></td>
</tr>
<tr class="even">
<td>01-Jan-2009</td>
<td><p>Fourth release of the Basic Specification, which includes the following changes:</p>
<blockquote>
<p>Removed references to Windows CE Access Control entries</p>
<p>Added clarification to Section 7.2.5.1 to explicitly require a full up-case table</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>02-Sep-2009</td>
<td><p>Fifth release of the Basic Specification, which includes the following changes:</p>
<blockquote>
<p>Document formatting changes to allow better PDF conversion</p>
</blockquote></td>
</tr>
<tr class="even">
<td>24-Feb-2010</td>
<td><p>Sixth release of the Basic Specification, which includes the following changes:</p>
<blockquote>
<p>Amended incorrect statement: “FirstCluster Field shall be zero if the DataLength is zero and NoFatChain is set” in Section 6.3.5 and Section 6.4.3 to “If the NoFatChain bit is 1 then FirstCluster must point to a valid cluster in the cluster heap“ to clarify that there must be valid allocation if the NoFatChain bit is set.</p>
<p>Added “If the NoFatChain bit is 1 then DataLength must not be zero. If the FirstCluster field is zero, then DataLength must also be zero” to Section 6.3.6 and Section 6.4.4 to clarify that there must be valid allocation if the NoFatChain bit is set.</p>
<p>Updated copyright notice to 2010</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>26-Aug-2019</td>
<td><p>Seventh release of the Basic Specification, which includes the following changes:</p>
<blockquote>
<p>Updated legal terms pertaining to the specification, including:</p>
<p>Removal of Microsoft Confidential notice</p>
<p>Removal of Microsoft Corporation Technical Documentation License Agreement section</p>
<p>Updated copyright notice to 2019</p>
</blockquote></td>
</tr>
</tbody>
</table>
