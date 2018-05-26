---
title: IMAPI Interfaces
description: The following tables identify and briefly describe the interfaces used C/C++ developers and the associated scripting object. Prefix the object name in the table with \ 0034;IMAPI2. \ 0034; to fully qualify the object name when creating the object in script.
ms.assetid: dba81a45-34a8-4b49-9ccb-d61a7e7ee1f6
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
<li>[<strong>DWriteEngine2Events</strong>](/windows/win32/imapi2/nn-imapi2-dwriteengine2events?branch=master)</li>
<li>[<strong>IWriteEngine2</strong>](/windows/win32/imapi2/nn-imapi2-iwriteengine2?branch=master)</li>
<li>[<strong>IWriteEngine2EventArgs</strong>](/windows/win32/imapi2/nn-imapi2-iwriteengine2eventargs?branch=master)</li>
</ul></td>
<td>MsftWriteEngine2</td>
</tr>
<tr class="odd">
<td>Main image writer.
<ul>
<li>[<strong>DDiscFormat2DataEvents</strong>](/windows/win32/imapi2/nn-imapi2-ddiscformat2dataevents?branch=master)</li>
<li>[<strong>IDiscFormat2Data</strong>](/windows/win32/imapi2/nn-imapi2-idiscformat2data?branch=master)</li>
<li>[<strong>IDiscFormat2DataEventArgs</strong>](/windows/win32/imapi2/nn-imapi2-idiscformat2dataeventargs?branch=master)</li>
</ul></td>
<td>MsftDiscFormat2Data</td>
</tr>
<tr class="even">
<td>Disc eraser.
<ul>
<li>[<strong>DDiscFormat2EraseEvents</strong>](/windows/win32/imapi2/nn-imapi2-ddiscformat2eraseevents?branch=master)</li>
<li>[<strong>IDiscFormat2Erase</strong>](/windows/win32/imapi2/nn-imapi2-idiscformat2erase?branch=master)</li>
</ul></td>
<td>MsftDiscFormat2Erase</td>
</tr>
<tr class="odd">
<td>Raw image writer.
<ul>
<li>[<strong>DDiscFormat2RawCDEvents</strong>](/windows/win32/imapi2/nn-imapi2-ddiscformat2rawcdevents?branch=master)</li>
<li>[<strong>IDiscFormat2RawCD</strong>](/windows/win32/imapi2/nn-imapi2-idiscformat2rawcd?branch=master)</li>
<li>[<strong>IDiscFormat2RawCDEventArgs</strong>](/windows/win32/imapi2/nn-imapi2-idiscformat2rawcdeventargs?branch=master)</li>
</ul></td>
<td>MsftDiscFormat2RawCD</td>
</tr>
<tr class="even">
<td>Track-At-Once image writer.
<ul>
<li>[<strong>DDiscFormat2TrackAtOnceEvents</strong>](/windows/win32/imapi2/nn-imapi2-ddiscformat2trackatonceevents?branch=master)</li>
<li>[<strong>IDiscFormat2TrackAtOnce</strong>](/windows/win32/imapi2/nn-imapi2-idiscformat2trackatonce?branch=master)</li>
<li>[<strong>IDiscFormat2TrackAtOnceEventArgs</strong>](/windows/win32/imapi2/nn-imapi2-idiscformat2trackatonceeventargs?branch=master)</li>
</ul></td>
<td>MsftDiscFormat2TrackAtOnce</td>
</tr>
<tr class="odd">
<td>Enumeration of disc devices in the system hardware list.
<ul>
<li>[<strong>IDiscMaster2</strong>](/windows/win32/imapi2/nn-imapi2-idiscmaster2?branch=master)</li>
</ul></td>
<td>MsftDiscMaster2</td>
</tr>
<tr class="even">
<td>Notification delegate for the MsftDiscMaster2 object.
<ul>
<li>[<strong>DDiscMaster2Events</strong>](/windows/win32/imapi2/nn-imapi2-ddiscmaster2events?branch=master)</li>
</ul></td>
<td>DDiscMaster2Events</td>
</tr>
<tr class="odd">
<td>Individual recording device.
<ul>
<li>[<strong>IDiscRecorder2</strong>](/windows/win32/imapi2/nn-imapi2-idiscrecorder2?branch=master)</li>
<li>[<strong>IDiscRecorder2Ex</strong>](/windows/win32/imapi2/nn-imapi2-idiscrecorder2ex?branch=master)</li>
</ul></td>
<td>MsftDiscRecorder2</td>
</tr>
<tr class="even">
<td>Device writing attributes, including the media type, writing speed, and type of angular velocity control.
<ul>
<li>[<strong>IWriteSpeedDescriptor</strong>](/windows/win32/imapi2/nn-imapi2-iwritespeeddescriptor?branch=master)</li>
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
<li>[<strong>IBootOptions</strong>](/windows/win32/imapi2fs/nn-imapi2fs-ibootoptions?branch=master)</li>
</ul></td>
<td>BootOptions</td>
</tr>
<tr class="odd">
<td>File system image and properties. This object includes all tracks, and references to the boot image and result image.
<ul>
<li>[<strong>DFileSystemImageEvents</strong>](/windows/win32/imapi2fs/nn-imapi2fs-dfilesystemimageevents?branch=master)</li>
<li>[<strong>DFileSystemImageImportEvents</strong>](/windows/win32/imapi2fs/nn-imapi2fs-dfilesystemimageimportevents?branch=master)</li>
<li>[<strong>IFileSystemImage</strong>](/windows/win32/imapi2fs/nn-imapi2fs-ifilesystemimage?branch=master)</li>
<li>[<strong>IFileSystemImage2</strong>](/windows/win32/imapi2fs/nn-imapi2fs-ifilesystemimage2?branch=master)</li>
<li>[<strong>IFileSystemImage3</strong>](/windows/win32/imapi2fs/nn-imapi2fs-ifilesystemimage3?branch=master)</li>
</ul></td>
<td>CFileSystemImage</td>
</tr>
<tr class="even">
<td>Container of the data stream provided by the file system object.
<ul>
<li>[<strong>IFileSystemImageResult</strong>](/windows/win32/imapi2fs/nn-imapi2fs-ifilesystemimageresult?branch=master)</li>
</ul></td>
<td>FileSystemImageResult</td>
</tr>
<tr class="odd">
<td>Directory item in the file system image.
<ul>
<li>[<strong>IFsiDirectoryItem</strong>](/windows/win32/imapi2fs/nn-imapi2fs-ifsidirectoryitem?branch=master)</li>
<li>[<strong>IFsiDirectoryItem2</strong>](/windows/win32/imapi2fs/nn-imapi2fs-ifsidirectoryitem2?branch=master)</li>
</ul></td>
<td>FsiDirectoryItem</td>
</tr>
<tr class="even">
<td>File item in the file system image.
<ul>
<li>[<strong>IFsiFileItem</strong>](/windows/win32/imapi2fs/nn-imapi2fs-ifsifileitem?branch=master)</li>
<li>[<strong>IFsiFileItem2</strong>](/windows/win32/imapi2fs/nn-imapi2fs-ifsifileitem2?branch=master)</li>
</ul></td>
<td>FsiFileItem</td>
</tr>
<tr class="odd">
<td>Interface containing properties common to both file and directory items.
<ul>
<li>[<strong>IFsiItem</strong>](/windows/win32/imapi2fs/nn-imapi2fs-ifsiitem?branch=master)</li>
</ul></td>
<td>FsiItem</td>
</tr>
<tr class="even">
<td>RAW CD image creation.
<ul>
<li>[<strong>IRawCDImageCreator</strong>](/windows/win32/imapi2/nn-imapi2-irawcdimagecreator?branch=master)</li>
<li>[<strong>IRawCDImageTrackInfo</strong>](/windows/win32/imapi2/nn-imapi2-irawcdimagetrackinfo?branch=master)</li>
</ul></td>
<td>MsftRawCDImageCreator</td>
</tr>
<tr class="odd">
<td>Stream object helper object to concatenate multiple streams.
<ul>
<li>[<strong>IStreamConcatenate</strong>](/windows/win32/imapi2/nn-imapi2-istreamconcatenate?branch=master)</li>
</ul></td>
<td>MsftStreamConcatenate</td>
</tr>
<tr class="even">
<td>Interleaved stream to add to the disc image.
<ul>
<li>[<strong>IStreamInterleave</strong>](/windows/win32/imapi2/nn-imapi2-istreaminterleave?branch=master)</li>
</ul></td>
<td>MsftStreamInterleave</td>
</tr>
<tr class="odd">
<td>Pseudo-random generated stream.
<ul>
<li>[<strong>IStreamPseudoRandomBased</strong>](/windows/win32/imapi2/nn-imapi2-istreampseudorandombased?branch=master)</li>
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
<li>[<strong>IBlockRange</strong>](/windows/win32/imapi2/nn-imapi2-iblockrange?branch=master)</li>
<li>[<strong>IBlockRangeList</strong>](/windows/win32/imapi2/nn-imapi2-iblockrangelist?branch=master)</li>
</ul></td>
<td>No corresponding object</td>
</tr>
<tr class="odd">
<td>Burn verification support.
<ul>
<li>[<strong>IBurnVerification</strong>](/windows/win32/imapi2/nn-imapi2-iburnverification?branch=master)</li>
</ul></td>
<td>No corresponding object</td>
</tr>
<tr class="even">
<td>Enumerator of FsiItems for C/C++ applications.
<ul>
<li>[<strong>IEnumFsiItems</strong>](/windows/win32/imapi2fs/nn-imapi2fs-ienumfsiitems?branch=master)</li>
</ul></td>
<td>EnumFsiItems</td>
</tr>
<tr class="odd">
<td>Enumerator of ProgressItems for C/C++ applications.
<ul>
<li>[<strong>IEnumProgressItems</strong>](/windows/win32/imapi2fs/nn-imapi2fs-ienumprogressitems?branch=master)</li>
</ul></td>
<td>EnumProgressItems</td>
</tr>
<tr class="even">
<td><ul>
<li>[<strong>IFsiNamedStreams</strong>](/windows/win32/imapi2fs/nn-imapi2fs-ifsinamedstreams?branch=master)</li>
</ul></td>
<td>FsiFileItem2</td>
</tr>
<tr class="odd">
<td>.iso image verification support.
<ul>
<li>[<strong>IIsoImageManager</strong>](/windows/win32/imapi2fs/nn-imapi2fs-iisoimagemanager?branch=master)</li>
</ul></td>
<td>No corresponding object</td>
</tr>
<tr class="even">
<td>Multiple session support.
<ul>
<li>[<strong>IMultisession</strong>](/windows/win32/imapi2/nn-imapi2-imultisession?branch=master)</li>
</ul></td>
<td>No corresponding object</td>
</tr>
<tr class="odd">
<td>Sequential multiple session support.
<ul>
<li>[<strong>IMultisessionSequential</strong>](/windows/win32/imapi2/nn-imapi2-imultisessionsequential?branch=master)</li>
<li>[<strong>IMultisessionSequential2</strong>](/windows/win32/imapi2/nn-imapi2-imultisessionsequential2?branch=master)</li>
</ul></td>
<td>MsftMultisessionSequential</td>
</tr>
<tr class="even">
<td>File name and associated blocks in the result image.
<ul>
<li>[<strong>IProgressItem</strong>](/windows/win32/imapi2fs/nn-imapi2fs-iprogressitem?branch=master)</li>
</ul></td>
<td>ProgressItem</td>
</tr>
<tr class="odd">
<td>Result image listing, broken down by file name and associated blocks.
<ul>
<li>[<strong>IProgressItems</strong>](/windows/win32/imapi2fs/nn-imapi2fs-iprogressitems?branch=master)</li>
</ul></td>
<td>ProgressItems</td>
</tr>
</tbody>
</table>



 

 

 




