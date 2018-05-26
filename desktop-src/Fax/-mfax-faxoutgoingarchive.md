---
Description: The FaxOutgoingArchive configuration object is used by a fax client application to access and configure the archive of outbound fax messages transmitted successfully by the fax service.
ms.assetid: ffed51b3-0a07-4667-8d8d-5054362489c4
title: FaxOutgoingArchive object
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutgoingArchive object

The **FaxOutgoingArchive** configuration object is used by a fax client application to access and configure the archive of outbound fax messages transmitted successfully by the fax service. You can also use the **FaxOutgoingArchive** object to retrieve a message from the archive using its message ID.

## Members

The **FaxOutgoingArchive** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **FaxOutgoingArchive** object has these methods.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Method</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">[<strong>GetMessage</strong>](-mfax-faxoutgoingarchive-getmessage.md)</td>
<td style="text-align: left;">The [<strong>GetMessage</strong>](-mfax-faxoutgoingarchive-getmessage.md) method returns a fax message from the archive of outbound faxes by using the fax message ID.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>GetMessages</strong>](-mfax-faxoutgoingarchive-getmessages.md)</td>
<td style="text-align: left;">The [<strong>GetMessages</strong>](-mfax-faxoutgoingarchive-getmessages.md) method returns a new iterator (archive cursor) for the archive of outbound fax messages. For more information, see [<strong>FaxOutgoingMessageIterator</strong>](-mfax-faxoutgoingmessageiterator.md).<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>Refresh</strong>](-mfax-faxoutgoingarchive-refresh-vb.md)</td>
<td style="text-align: left;">The [<strong>Refresh</strong>](-mfax-faxoutgoingarchive-refresh-vb.md) method refreshes <strong>FaxOutgoingArchive</strong> object information from the fax server. When the <strong>Refresh</strong> method is called, any configuration changes made after the last [<strong>Save</strong>](-mfax-faxoutgoingarchive-save-vb.md) method call are lost.<br/>
<blockquote>
[!Note]<br />
In Windows Vista, Windows Server 2008, and later versions of Windows, this method is not supported and returns an error.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>Save</strong>](-mfax-faxoutgoingarchive-save-vb.md)</td>
<td style="text-align: left;">The [<strong>Save</strong>](-mfax-faxoutgoingarchive-save-vb.md) method saves the <strong>FaxOutgoingArchive</strong> object data.<br/>
<blockquote>
[!Note]<br />
In Windows Vista, Windows Server 2008, and later versions of Windows, this method is not supported and returns an error.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

### Properties

The **FaxOutgoingArchive** object has these properties.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Access type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">[<strong>AgeLimit</strong>](-mfax-faxoutgoingarchive-agelimit-vb.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">The [<strong>AgeLimit</strong>](-mfax-faxoutgoingarchive-agelimit-vb.md) property is a value that indicates the number of days that the fax service retains fax messages in the archive of outbound faxes. The fax service deletes messages from the outbound archive when they exceed the age limit. If the value of this property is zero, the fax service does not enforce an age limit.<br/>
<blockquote>
[!Note]<br />
This property is not supported in Windows Vista, Windows Server 2008, and later versions of Windows. To access this property in Windows Vista, Windows Server 2008, and later versions of Windows, get the [<strong>FaxConfiguration.ArchiveAgeLimit</strong>](-mfax-faxconfiguration-archiveagelimit-vb.md) property from the [<strong>FaxServer</strong>](-mfax-faxserver.md) object.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>ArchiveFolder</strong>](-mfax-faxoutgoingarchive-archivefolder-vb.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">The [<strong>ArchiveFolder</strong>](-mfax-faxoutgoingarchive-archivefolder-vb.md) property is a null-terminated string that specifies the folder location on the fax server for archived outbound faxes.<br/>
<blockquote>
[!Note]<br />
This property is not supported in Windows Vista, Windows Server 2008, and later versions of Windows. To access this property in Windows Vista, Windows Server 2008, and later versions of Windows, get the [<strong>FaxConfiguration.ArchiveLocation</strong>](-mfax-faxconfiguration-archivelocation-vb.md) property from the [<strong>FaxServer</strong>](-mfax-faxserver.md) object.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>HighQuotaWaterMark</strong>](-mfax-faxoutgoingarchive-highquotawatermark-vb.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">The [<strong>HighQuotaWaterMark</strong>](-mfax-faxoutgoingarchive-highquotawatermark-vb.md) property is a value that specifies the upper threshold for the size of the archive of inbound fax messages, in megabytes. If the archived fax messages in the archive exceed this value, and the [<strong>SizeQuotaWarning</strong>](-mfax-faxoutgoingarchive-sizequotawarning-vb.md) property is equal to <strong>True</strong>, the fax service issues a warning in the event log.<br/>
<blockquote>
[!Note]<br />
This property is not supported in Windows Vista, Windows Server 2008, and later versions of Windows. To access this property in Windows Vista, Windows Server 2008, and later versions of Windows, get the [<strong>FaxConfiguration.HighQuotaWaterMark</strong>](-mfax-faxconfiguration-highquotawatermark-vb.md) property from the [<strong>FaxServer</strong>](-mfax-faxserver.md) object.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>LowQuotaWaterMark</strong>](-mfax-faxoutgoingarchive-lowquotawatermark-vb.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">The [<strong>LowQuotaWaterMark</strong>](-mfax-faxoutgoingarchive-lowquotawatermark-vb.md) property is a value that specifies the lower threshold for the archive of outbound fax messages, in megabytes. If the fax service has issued a warning in the event log, the service does not issue additional warnings until the size of the outbound archive drops below this value. <br/>
<blockquote>
[!Note]<br />
This property is not supported in Windows Vista, Windows Server 2008, and later versions of Windows. To access this property in Windows Vista, Windows Server 2008, and later versions of Windows, get the [<strong>FaxConfiguration.LowQuotaWaterMark</strong>](-mfax-faxconfiguration-lowquotawatermark-vb.md) property from the [<strong>FaxServer</strong>](-mfax-faxserver.md) object.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>SizeHigh</strong>](-mfax-faxoutgoingarchive-sizehigh-vb.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">The [<strong>SizeHigh</strong>](-mfax-faxoutgoingarchive-sizehigh-vb.md) property is a value that specifies the high 32-bit value (in bytes) for the size of the archive of outgoing fax messages.<br/>
<blockquote>
[!Note]<br />
This property is not supported in Windows Vista, Windows Server 2008, and later versions of Windows. To access this property in Windows Vista, Windows Server 2008, and later versions of Windows, get the [<strong>FaxConfiguration.ArchiveSizeHigh</strong>](-mfax-faxconfiguration-archivesizehigh-vb.md) property from the [<strong>FaxServer</strong>](-mfax-faxserver.md) object.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>SizeLow</strong>](-mfax-faxoutgoingarchive-sizelow-vb.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">The [<strong>SizeLow</strong>](-mfax-faxoutgoingarchive-sizelow-vb.md) property is a value that specifies the low 32-bit value (in bytes) for the size of the archive of outgoing fax messages.<br/>
<blockquote>
[!Note]<br />
This property is not supported in Windows Vista, Windows Server 2008, and later versions of Windows. To access this property in Windows Vista, Windows Server 2008, and later versions of Windows, get the [<strong>FaxConfiguration.ArchiveSizeLow</strong>](-mfax-faxconfiguration-archivesizelow-vb.md) property from the [<strong>FaxServer</strong>](-mfax-faxserver.md) object.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>SizeQuotaWarning</strong>](-mfax-faxoutgoingarchive-sizequotawarning-vb.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">The [<strong>SizeQuotaWarning</strong>](-mfax-faxoutgoingarchive-sizequotawarning-vb.md) property is a Boolean value that indicates whether the fax service issues a warning in the event log when the size of the outbound archive exceeds the limit defined by the [<strong>HighQuotaWaterMark</strong>](-mfax-faxoutgoingarchive-highquotawatermark-vb.md) property.<br/>
<blockquote>
[!Note]<br />
This property is not supported in Windows Vista, Windows Server 2008, and later versions of Windows. To access this property in Windows Vista, Windows Server 2008, and later versions of Windows, get the [<strong>FaxConfiguration.SizeQuotaWarning</strong>](-mfax-faxconfiguration-sizequotawarning-vb.md) property from the [<strong>FaxServer</strong>](-mfax-faxserver.md) object.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>UseArchive</strong>](-mfax-faxoutgoingarchive-usearchive-vb.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">The [<strong>UseArchive</strong>](-mfax-faxoutgoingarchive-usearchive-vb.md) property is a Boolean value that indicates whether the fax service archives outbound fax messages. If this parameter is equal to <strong>True</strong>, the fax service archives outbound fax messages. If this parameter is equal to <strong>False</strong>, the fax service does not archive outbound faxes.<br/>
<blockquote>
[!Note]<br />
This property is not supported in Windows Vista, Windows Server 2008, and later versions of Windows. To access this property in Windows Vista, Windows Server 2008, and later versions of Windows, get the [<strong>FaxConfiguration.UseArchive</strong>](-mfax-faxconfiguration-usearchive-vb.md) property from the [<strong>FaxServer</strong>](-mfax-faxserver.md) object.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

## Remarks

A **FaxOutgoingArchive** object is accessed through a [**FaxFolders**](-mfax-faxfolders.md) object.

![faxfolders and faxoutgoingarchive objects](images/faxoutgoingarchive.png)

To create a **FaxOutgoingArchive** object in Microsoft Visual Basic, retrieve the [**OutgoingArchive**](-mfax-faxfolders-outgoingarchive-vb.md) property of the [**FaxFolders**](-mfax-faxfolders.md) object.

To create a **FaxOutgoingArchive** object in C++, call the [**OutgoingArchive**](-mfax-faxfolders-outgoingarchive-vb.md) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxOutgoingArchive<br/>                                                    |



 

 




