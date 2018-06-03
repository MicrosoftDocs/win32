---
title: IMAPI Interfaces
description: The following tables identify and briefly describe the interfaces used C/C++ developers and the associated scripting object. Prefix the object name in the table with \ 0034;IMAPI2. \ 0034; to fully qualify the object name when creating the object in script.
ms.assetid: dba81a45-34a8-4b49-9ccb-d61a7e7ee1f6
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMAPI Interfaces

The following tables identify and briefly describe the interfaces used C/C++ developers and the associated scripting object. Prefix the object name in the table with "IMAPI2." to fully qualify the object name when creating the object in script.

The following table lists the interfaces associated with devices, the burn engine, and the format writers and eraser.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Interface</td>
<td>Object</td>
</tr>
<tr class="even">
<td>Low-level burn engine.
<ul>
<li>[<strong>DWriteEngine2Events</strong>](/windows/desktop/api/imapi2/nn-imapi2-dwriteengine2events)</li>
<li>[<strong>IWriteEngine2</strong>](/windows/desktop/api/imapi2/nn-imapi2-iwriteengine2)</li>
<li>[<strong>IWriteEngine2EventArgs</strong>](/windows/desktop/api/imapi2/nn-imapi2-iwriteengine2eventargs)</li>
</ul></td>
<td>MsftWriteEngine2</td>
</tr>
<tr class="odd">
<td>Main image writer.
<ul>
<li>[<strong>DDiscFormat2DataEvents</strong>](/windows/desktop/api/imapi2/nn-imapi2-ddiscformat2dataevents)</li>
<li>[<strong>IDiscFormat2Data</strong>](/windows/desktop/api/imapi2/nn-imapi2-idiscformat2data)</li>
<li>[<strong>IDiscFormat2DataEventArgs</strong>](/windows/desktop/api/imapi2/nn-imapi2-idiscformat2dataeventargs)</li>
</ul></td>
<td>MsftDiscFormat2Data</td>
</tr>
<tr class="even">
<td>Disc eraser.
<ul>
<li>[<strong>DDiscFormat2EraseEvents</strong>](/windows/desktop/api/imapi2/nn-imapi2-ddiscformat2eraseevents)</li>
<li>[<strong>IDiscFormat2Erase</strong>](/windows/desktop/api/imapi2/nn-imapi2-idiscformat2erase)</li>
</ul></td>
<td>MsftDiscFormat2Erase</td>
</tr>
<tr class="odd">
<td>Raw image writer.
<ul>
<li>[<strong>DDiscFormat2RawCDEvents</strong>](/windows/desktop/api/imapi2/nn-imapi2-ddiscformat2rawcdevents)</li>
<li>[<strong>IDiscFormat2RawCD</strong>](/windows/desktop/api/imapi2/nn-imapi2-idiscformat2rawcd)</li>
<li>[<strong>IDiscFormat2RawCDEventArgs</strong>](/windows/desktop/api/imapi2/nn-imapi2-idiscformat2rawcdeventargs)</li>
</ul></td>
<td>MsftDiscFormat2RawCD</td>
</tr>
<tr class="even">
<td>Track-At-Once image writer.
<ul>
<li>[<strong>DDiscFormat2TrackAtOnceEvents</strong>](/windows/desktop/api/imapi2/nn-imapi2-ddiscformat2trackatonceevents)</li>
<li>[<strong>IDiscFormat2TrackAtOnce</strong>](/windows/desktop/api/imapi2/nn-imapi2-idiscformat2trackatonce)</li>
<li>[<strong>IDiscFormat2TrackAtOnceEventArgs</strong>](/windows/desktop/api/imapi2/nn-imapi2-idiscformat2trackatonceeventargs)</li>
</ul></td>
<td>MsftDiscFormat2TrackAtOnce</td>
</tr>
<tr class="odd">
<td>Enumeration of disc devices in the system hardware list.
<ul>
<li>[<strong>IDiscMaster2</strong>](/windows/desktop/api/imapi2/nn-imapi2-idiscmaster2)</li>
</ul></td>
<td>MsftDiscMaster2</td>
</tr>
<tr class="even">
<td>Notification delegate for the MsftDiscMaster2 object.
<ul>
<li>[<strong>DDiscMaster2Events</strong>](/windows/desktop/api/imapi2/nn-imapi2-ddiscmaster2events)</li>
</ul></td>
<td>DDiscMaster2Events</td>
</tr>
<tr class="odd">
<td>Individual recording device.
<ul>
<li>[<strong>IDiscRecorder2</strong>](/windows/desktop/api/imapi2/nn-imapi2-idiscrecorder2)</li>
<li>[<strong>IDiscRecorder2Ex</strong>](/windows/desktop/api/imapi2/nn-imapi2-idiscrecorder2ex)</li>
</ul></td>
<td>MsftDiscRecorder2</td>
</tr>
<tr class="even">
<td>Device writing attributes, including the media type, writing speed, and type of angular velocity control.
<ul>
<li>[<strong>IWriteSpeedDescriptor</strong>](/windows/desktop/api/imapi2/nn-imapi2-iwritespeeddescriptor)</li>
</ul></td>
<td>MsftWriteSpeedDescriptor</td>
</tr>
</tbody>
</table>



 

The following table lists the file system interfaces.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Interface</td>
<td>Object</td>
</tr>
<tr class="even">
<td>Boot image stream and properties for integrating the bootable image in the disc image.
<ul>
<li>[<strong>IBootOptions</strong>](/windows/desktop/api/imapi2fs/nn-imapi2fs-ibootoptions)</li>
</ul></td>
<td>BootOptions</td>
</tr>
<tr class="odd">
<td>File system image and properties. This object includes all tracks, and references to the boot image and result image.
<ul>
<li>[<strong>DFileSystemImageEvents</strong>](/windows/desktop/api/imapi2fs/nn-imapi2fs-dfilesystemimageevents)</li>
<li>[<strong>DFileSystemImageImportEvents</strong>](/windows/desktop/api/imapi2fs/nn-imapi2fs-dfilesystemimageimportevents)</li>
<li>[<strong>IFileSystemImage</strong>](/windows/desktop/api/imapi2fs/nn-imapi2fs-ifilesystemimage)</li>
<li>[<strong>IFileSystemImage2</strong>](/windows/desktop/api/imapi2fs/nn-imapi2fs-ifilesystemimage2)</li>
<li>[<strong>IFileSystemImage3</strong>](/windows/desktop/api/imapi2fs/nn-imapi2fs-ifilesystemimage3)</li>
</ul></td>
<td>CFileSystemImage</td>
</tr>
<tr class="even">
<td>Container of the data stream provided by the file system object.
<ul>
<li>[<strong>IFileSystemImageResult</strong>](/windows/desktop/api/imapi2fs/nn-imapi2fs-ifilesystemimageresult)</li>
</ul></td>
<td>FileSystemImageResult</td>
</tr>
<tr class="odd">
<td>Directory item in the file system image.
<ul>
<li>[<strong>IFsiDirectoryItem</strong>](/windows/desktop/api/imapi2fs/nn-imapi2fs-ifsidirectoryitem)</li>
<li>[<strong>IFsiDirectoryItem2</strong>](/windows/desktop/api/imapi2fs/nn-imapi2fs-ifsidirectoryitem2)</li>
</ul></td>
<td>FsiDirectoryItem</td>
</tr>
<tr class="even">
<td>File item in the file system image.
<ul>
<li>[<strong>IFsiFileItem</strong>](/windows/desktop/api/imapi2fs/nn-imapi2fs-ifsifileitem)</li>
<li>[<strong>IFsiFileItem2</strong>](/windows/desktop/api/imapi2fs/nn-imapi2fs-ifsifileitem2)</li>
</ul></td>
<td>FsiFileItem</td>
</tr>
<tr class="odd">
<td>Interface containing properties common to both file and directory items.
<ul>
<li>[<strong>IFsiItem</strong>](/windows/desktop/api/imapi2fs/nn-imapi2fs-ifsiitem)</li>
</ul></td>
<td>FsiItem</td>
</tr>
<tr class="even">
<td>RAW CD image creation.
<ul>
<li>[<strong>IRawCDImageCreator</strong>](/windows/desktop/api/imapi2/nn-imapi2-irawcdimagecreator)</li>
<li>[<strong>IRawCDImageTrackInfo</strong>](/windows/desktop/api/imapi2/nn-imapi2-irawcdimagetrackinfo)</li>
</ul></td>
<td>MsftRawCDImageCreator</td>
</tr>
<tr class="odd">
<td>Stream object helper object to concatenate multiple streams.
<ul>
<li>[<strong>IStreamConcatenate</strong>](/windows/desktop/api/imapi2/nn-imapi2-istreamconcatenate)</li>
</ul></td>
<td>MsftStreamConcatenate</td>
</tr>
<tr class="even">
<td>Interleaved stream to add to the disc image.
<ul>
<li>[<strong>IStreamInterleave</strong>](/windows/desktop/api/imapi2/nn-imapi2-istreaminterleave)</li>
</ul></td>
<td>MsftStreamInterleave</td>
</tr>
<tr class="odd">
<td>Pseudo-random generated stream.
<ul>
<li>[<strong>IStreamPseudoRandomBased</strong>](/windows/desktop/api/imapi2/nn-imapi2-istreampseudorandombased)</li>
</ul></td>
<td>MsftStreamPrgn001</td>
</tr>
<tr class="even">
<td>The <strong>MsftStreamZero</strong> scripting object is not implemented as an interface.</td>
<td>[<strong>MsftStreamZero</strong>](msftstreamzero.md)</td>
</tr>
</tbody>
</table>



 

The following table lists helper interfaces.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Interface</td>
<td>Object</td>
</tr>
<tr class="even">
<td>Collection of sector ranges within a file system image.
<ul>
<li>[<strong>IBlockRange</strong>](/windows/desktop/api/imapi2/nn-imapi2-iblockrange)</li>
<li>[<strong>IBlockRangeList</strong>](/windows/desktop/api/imapi2/nn-imapi2-iblockrangelist)</li>
</ul></td>
<td>No corresponding object</td>
</tr>
<tr class="odd">
<td>Burn verification support.
<ul>
<li>[<strong>IBurnVerification</strong>](/windows/desktop/api/imapi2/nn-imapi2-iburnverification)</li>
</ul></td>
<td>No corresponding object</td>
</tr>
<tr class="even">
<td>Enumerator of FsiItems for C/C++ applications.
<ul>
<li>[<strong>IEnumFsiItems</strong>](/windows/desktop/api/imapi2fs/nn-imapi2fs-ienumfsiitems)</li>
</ul></td>
<td>EnumFsiItems</td>
</tr>
<tr class="odd">
<td>Enumerator of ProgressItems for C/C++ applications.
<ul>
<li>[<strong>IEnumProgressItems</strong>](/windows/desktop/api/imapi2fs/nn-imapi2fs-ienumprogressitems)</li>
</ul></td>
<td>EnumProgressItems</td>
</tr>
<tr class="even">
<td><ul>
<li>[<strong>IFsiNamedStreams</strong>](/windows/desktop/api/imapi2fs/nn-imapi2fs-ifsinamedstreams)</li>
</ul></td>
<td>FsiFileItem2</td>
</tr>
<tr class="odd">
<td>.iso image verification support.
<ul>
<li>[<strong>IIsoImageManager</strong>](/windows/desktop/api/imapi2fs/nn-imapi2fs-iisoimagemanager)</li>
</ul></td>
<td>No corresponding object</td>
</tr>
<tr class="even">
<td>Multiple session support.
<ul>
<li>[<strong>IMultisession</strong>](/windows/desktop/api/imapi2/nn-imapi2-imultisession)</li>
</ul></td>
<td>No corresponding object</td>
</tr>
<tr class="odd">
<td>Sequential multiple session support.
<ul>
<li>[<strong>IMultisessionSequential</strong>](/windows/desktop/api/imapi2/nn-imapi2-imultisessionsequential)</li>
<li>[<strong>IMultisessionSequential2</strong>](/windows/desktop/api/imapi2/nn-imapi2-imultisessionsequential2)</li>
</ul></td>
<td>MsftMultisessionSequential</td>
</tr>
<tr class="even">
<td>File name and associated blocks in the result image.
<ul>
<li>[<strong>IProgressItem</strong>](/windows/desktop/api/imapi2fs/nn-imapi2fs-iprogressitem)</li>
</ul></td>
<td>ProgressItem</td>
</tr>
<tr class="odd">
<td>Result image listing, broken down by file name and associated blocks.
<ul>
<li>[<strong>IProgressItems</strong>](/windows/desktop/api/imapi2fs/nn-imapi2fs-iprogressitems)</li>
</ul></td>
<td>ProgressItems</td>
</tr>
</tbody>
</table>



 

 

 




