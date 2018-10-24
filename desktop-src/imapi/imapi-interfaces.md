---
title: IMAPI Interfaces
description: The following tables identify and briefly describe the interfaces used C/C++ developers and the associated scripting object. Prefix the object name in the table with \ 0034;IMAPI2. \ 0034; to fully qualify the object name when creating the object in script.
ms.assetid: dba81a45-34a8-4b49-9ccb-d61a7e7ee1f6
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
<li><a href="/windows/desktop/api/imapi2/nn-imapi2-dwriteengine2events"><strong>DWriteEngine2Events</strong></a></li>
<li><a href="/windows/desktop/api/imapi2/nn-imapi2-iwriteengine2"><strong>IWriteEngine2</strong></a></li>
<li><a href="/windows/desktop/api/imapi2/nn-imapi2-iwriteengine2eventargs"><strong>IWriteEngine2EventArgs</strong></a></li>
</ul></td>
<td>MsftWriteEngine2</td>
</tr>
<tr class="odd">
<td>Main image writer.
<ul>
<li><a href="/windows/desktop/api/imapi2/nn-imapi2-ddiscformat2dataevents"><strong>DDiscFormat2DataEvents</strong></a></li>
<li><a href="/windows/desktop/api/imapi2/nn-imapi2-idiscformat2data"><strong>IDiscFormat2Data</strong></a></li>
<li><a href="/windows/desktop/api/imapi2/nn-imapi2-idiscformat2dataeventargs"><strong>IDiscFormat2DataEventArgs</strong></a></li>
</ul></td>
<td>MsftDiscFormat2Data</td>
</tr>
<tr class="even">
<td>Disc eraser.
<ul>
<li><a href="/windows/desktop/api/imapi2/nn-imapi2-ddiscformat2eraseevents"><strong>DDiscFormat2EraseEvents</strong></a></li>
<li><a href="/windows/desktop/api/imapi2/nn-imapi2-idiscformat2erase"><strong>IDiscFormat2Erase</strong></a></li>
</ul></td>
<td>MsftDiscFormat2Erase</td>
</tr>
<tr class="odd">
<td>Raw image writer.
<ul>
<li><a href="/windows/desktop/api/imapi2/nn-imapi2-ddiscformat2rawcdevents"><strong>DDiscFormat2RawCDEvents</strong></a></li>
<li><a href="/windows/desktop/api/imapi2/nn-imapi2-idiscformat2rawcd"><strong>IDiscFormat2RawCD</strong></a></li>
<li><a href="/windows/desktop/api/imapi2/nn-imapi2-idiscformat2rawcdeventargs"><strong>IDiscFormat2RawCDEventArgs</strong></a></li>
</ul></td>
<td>MsftDiscFormat2RawCD</td>
</tr>
<tr class="even">
<td>Track-At-Once image writer.
<ul>
<li><a href="/windows/desktop/api/imapi2/nn-imapi2-ddiscformat2trackatonceevents"><strong>DDiscFormat2TrackAtOnceEvents</strong></a></li>
<li><a href="/windows/desktop/api/imapi2/nn-imapi2-idiscformat2trackatonce"><strong>IDiscFormat2TrackAtOnce</strong></a></li>
<li><a href="/windows/desktop/api/imapi2/nn-imapi2-idiscformat2trackatonceeventargs"><strong>IDiscFormat2TrackAtOnceEventArgs</strong></a></li>
</ul></td>
<td>MsftDiscFormat2TrackAtOnce</td>
</tr>
<tr class="odd">
<td>Enumeration of disc devices in the system hardware list.
<ul>
<li><a href="/windows/desktop/api/imapi2/nn-imapi2-idiscmaster2"><strong>IDiscMaster2</strong></a></li>
</ul></td>
<td>MsftDiscMaster2</td>
</tr>
<tr class="even">
<td>Notification delegate for the MsftDiscMaster2 object.
<ul>
<li><a href="/windows/desktop/api/imapi2/nn-imapi2-ddiscmaster2events"><strong>DDiscMaster2Events</strong></a></li>
</ul></td>
<td>DDiscMaster2Events</td>
</tr>
<tr class="odd">
<td>Individual recording device.
<ul>
<li><a href="/windows/desktop/api/imapi2/nn-imapi2-idiscrecorder2"><strong>IDiscRecorder2</strong></a></li>
<li><a href="/windows/desktop/api/imapi2/nn-imapi2-idiscrecorder2ex"><strong>IDiscRecorder2Ex</strong></a></li>
</ul></td>
<td>MsftDiscRecorder2</td>
</tr>
<tr class="even">
<td>Device writing attributes, including the media type, writing speed, and type of angular velocity control.
<ul>
<li><a href="/windows/desktop/api/imapi2/nn-imapi2-iwritespeeddescriptor"><strong>IWriteSpeedDescriptor</strong></a></li>
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
<li><a href="/windows/desktop/api/imapi2fs/nn-imapi2fs-ibootoptions"><strong>IBootOptions</strong></a></li>
</ul></td>
<td>BootOptions</td>
</tr>
<tr class="odd">
<td>File system image and properties. This object includes all tracks, and references to the boot image and result image.
<ul>
<li><a href="/windows/desktop/api/imapi2fs/nn-imapi2fs-dfilesystemimageevents"><strong>DFileSystemImageEvents</strong></a></li>
<li><a href="/windows/desktop/api/imapi2fs/nn-imapi2fs-dfilesystemimageimportevents"><strong>DFileSystemImageImportEvents</strong></a></li>
<li><a href="/windows/desktop/api/imapi2fs/nn-imapi2fs-ifilesystemimage"><strong>IFileSystemImage</strong></a></li>
<li><a href="/windows/desktop/api/imapi2fs/nn-imapi2fs-ifilesystemimage2"><strong>IFileSystemImage2</strong></a></li>
<li><a href="/windows/desktop/api/imapi2fs/nn-imapi2fs-ifilesystemimage3"><strong>IFileSystemImage3</strong></a></li>
</ul></td>
<td>CFileSystemImage</td>
</tr>
<tr class="even">
<td>Container of the data stream provided by the file system object.
<ul>
<li><a href="/windows/desktop/api/imapi2fs/nn-imapi2fs-ifilesystemimageresult"><strong>IFileSystemImageResult</strong></a></li>
</ul></td>
<td>FileSystemImageResult</td>
</tr>
<tr class="odd">
<td>Directory item in the file system image.
<ul>
<li><a href="/windows/desktop/api/imapi2fs/nn-imapi2fs-ifsidirectoryitem"><strong>IFsiDirectoryItem</strong></a></li>
<li><a href="/windows/desktop/api/imapi2fs/nn-imapi2fs-ifsidirectoryitem2"><strong>IFsiDirectoryItem2</strong></a></li>
</ul></td>
<td>FsiDirectoryItem</td>
</tr>
<tr class="even">
<td>File item in the file system image.
<ul>
<li><a href="/windows/desktop/api/imapi2fs/nn-imapi2fs-ifsifileitem"><strong>IFsiFileItem</strong></a></li>
<li><a href="/windows/desktop/api/imapi2fs/nn-imapi2fs-ifsifileitem2"><strong>IFsiFileItem2</strong></a></li>
</ul></td>
<td>FsiFileItem</td>
</tr>
<tr class="odd">
<td>Interface containing properties common to both file and directory items.
<ul>
<li><a href="/windows/desktop/api/imapi2fs/nn-imapi2fs-ifsiitem"><strong>IFsiItem</strong></a></li>
</ul></td>
<td>FsiItem</td>
</tr>
<tr class="even">
<td>RAW CD image creation.
<ul>
<li><a href="/windows/desktop/api/imapi2/nn-imapi2-irawcdimagecreator"><strong>IRawCDImageCreator</strong></a></li>
<li><a href="/windows/desktop/api/imapi2/nn-imapi2-irawcdimagetrackinfo"><strong>IRawCDImageTrackInfo</strong></a></li>
</ul></td>
<td>MsftRawCDImageCreator</td>
</tr>
<tr class="odd">
<td>Stream object helper object to concatenate multiple streams.
<ul>
<li><a href="/windows/desktop/api/imapi2/nn-imapi2-istreamconcatenate"><strong>IStreamConcatenate</strong></a></li>
</ul></td>
<td>MsftStreamConcatenate</td>
</tr>
<tr class="even">
<td>Interleaved stream to add to the disc image.
<ul>
<li><a href="/windows/desktop/api/imapi2/nn-imapi2-istreaminterleave"><strong>IStreamInterleave</strong></a></li>
</ul></td>
<td>MsftStreamInterleave</td>
</tr>
<tr class="odd">
<td>Pseudo-random generated stream.
<ul>
<li><a href="/windows/desktop/api/imapi2/nn-imapi2-istreampseudorandombased"><strong>IStreamPseudoRandomBased</strong></a></li>
</ul></td>
<td>MsftStreamPrgn001</td>
</tr>
<tr class="even">
<td>The <strong>MsftStreamZero</strong> scripting object is not implemented as an interface.</td>
<td><a href="msftstreamzero"><strong>MsftStreamZero</strong></a></td>
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
<li><a href="/windows/desktop/api/imapi2/nn-imapi2-iblockrange"><strong>IBlockRange</strong></a></li>
<li><a href="/windows/desktop/api/imapi2/nn-imapi2-iblockrangelist"><strong>IBlockRangeList</strong></a></li>
</ul></td>
<td>No corresponding object</td>
</tr>
<tr class="odd">
<td>Burn verification support.
<ul>
<li><a href="/windows/desktop/api/imapi2/nn-imapi2-iburnverification"><strong>IBurnVerification</strong></a></li>
</ul></td>
<td>No corresponding object</td>
</tr>
<tr class="even">
<td>Enumerator of FsiItems for C/C++ applications.
<ul>
<li><a href="/windows/desktop/api/imapi2fs/nn-imapi2fs-ienumfsiitems"><strong>IEnumFsiItems</strong></a></li>
</ul></td>
<td>EnumFsiItems</td>
</tr>
<tr class="odd">
<td>Enumerator of ProgressItems for C/C++ applications.
<ul>
<li><a href="/windows/desktop/api/imapi2fs/nn-imapi2fs-ienumprogressitems"><strong>IEnumProgressItems</strong></a></li>
</ul></td>
<td>EnumProgressItems</td>
</tr>
<tr class="even">
<td><ul>
<li><a href="/windows/desktop/api/imapi2fs/nn-imapi2fs-ifsinamedstreams"><strong>IFsiNamedStreams</strong></a></li>
</ul></td>
<td>FsiFileItem2</td>
</tr>
<tr class="odd">
<td>.iso image verification support.
<ul>
<li><a href="/windows/desktop/api/imapi2fs/nn-imapi2fs-iisoimagemanager"><strong>IIsoImageManager</strong></a></li>
</ul></td>
<td>No corresponding object</td>
</tr>
<tr class="even">
<td>Multiple session support.
<ul>
<li><a href="/windows/desktop/api/imapi2/nn-imapi2-imultisession"><strong>IMultisession</strong></a></li>
</ul></td>
<td>No corresponding object</td>
</tr>
<tr class="odd">
<td>Sequential multiple session support.
<ul>
<li><a href="/windows/desktop/api/imapi2/nn-imapi2-imultisessionsequential"><strong>IMultisessionSequential</strong></a></li>
<li><a href="/windows/desktop/api/imapi2/nn-imapi2-imultisessionsequential2"><strong>IMultisessionSequential2</strong></a></li>
</ul></td>
<td>MsftMultisessionSequential</td>
</tr>
<tr class="even">
<td>File name and associated blocks in the result image.
<ul>
<li><a href="/windows/desktop/api/imapi2fs/nn-imapi2fs-iprogressitem"><strong>IProgressItem</strong></a></li>
</ul></td>
<td>ProgressItem</td>
</tr>
<tr class="odd">
<td>Result image listing, broken down by file name and associated blocks.
<ul>
<li><a href="/windows/desktop/api/imapi2fs/nn-imapi2fs-iprogressitems"><strong>IProgressItems</strong></a></li>
</ul></td>
<td>ProgressItems</td>
</tr>
</tbody>
</table>



 

 

 




