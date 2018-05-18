---
Description: 'Represents various objects that provide configuration options for the fax service.'
ms.assetid: '381e098b-d130-4e15-9aba-cb0048cc5b98'
title: FaxConfiguration object
---

# FaxConfiguration object

Represents various objects that provide configuration options for the fax service.

## Members

The **FaxConfiguration** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **FaxConfiguration** object has these methods.



| Method                                               | Description                      |
|:-----------------------------------------------------|:---------------------------------|
| [**Refresh**](-mfax-faxconfiguration-refresh-vb.md) | Refreshes the object.<br/> |
| [**Save**](-mfax-faxconfiguration-save-vb.md)       | Saves the object.<br/>     |



 

### Properties

The **FaxConfiguration** object has these properties.



| Property                                                                                              | Access type           | Description                                                                                                                                              |
|:------------------------------------------------------------------------------------------------------|:----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AllowPersonalCoverPages**](-mfax-faxconfiguration-allowpersonalcoverpages-vb.md)<br/>       | Read/write<br/> | Sets or retrieves a value that indicates whether personal cover pages are allowed.<br/>                                                            |
| [**ArchiveAgeLimit**](-mfax-faxconfiguration-archiveagelimit-vb.md)<br/>                       | Read/write<br/> | Sets or retrieves a value that indicates how long a fax message is kept on the server.<br/>                                                        |
| [**ArchiveLocation**](-mfax-faxconfiguration-archivelocation-vb.md)<br/>                       | Read/write<br/> | Sets or retrieves a value that indicates the location of the archive on the server.<br/>                                                           |
| [**ArchiveSizeHigh**](-mfax-faxconfiguration-archivesizehigh-vb.md)<br/>                       | Read-only<br/>  | The value that specifies the high-order 32-bit value (in bytes) for the size of the fax message archive.<br/>                                      |
| [**ArchiveSizeLow**](-mfax-faxconfiguration-archivesizelow-vb.md)<br/>                         | Read-only<br/>  | The value that specifies the low-order 32-bit value (in bytes) for the size of the fax message archive.<br/>                                       |
| [**AutoCreateAccountOnConnect**](-mfax-faxconfiguration-autocreateaccountonconnect-vb.md)<br/> | Read/write<br/> | Sets or retrieves a value that indicates whether the server automatically creates a fax account once a connection is initiated. <br/>              |
| [**Branding**](-mfax-faxconfiguration-branding-vb.md)<br/>                                     | Read/write<br/> | Sets or retrieves a value that indicates whether the fax server generates a branding mark on outgoing faxes.<br/>                                  |
| [**DiscountRateEnd**](-mfax-faxconfiguration-discountrateend-vb.md)<br/>                       | Read/write<br/> | Sets or retrieves a value that indicates the time at which the discount rate period ends.<br/>                                                     |
| [**DiscountRateStart**](-mfax-faxconfiguration-discountratestart-vb.md)<br/>                   | Read/write<br/> | Sets or retrieves a value that indicates the time at which the discount rate period begins.<br/>                                                   |
| [**HighQuotaWaterMark**](-mfax-faxconfiguration-highquotawatermark-vb.md)<br/>                 | Read/write<br/> | Sets or retrieves a value that indicates the maximum allotted size of a watermark. <br/>                                                           |
| [**IncomingFaxesArePublic**](-mfax-faxconfiguration-incomingfaxesarepublic-vb.md)<br/>         | Read/write<br/> | Indicates whether incoming faxes are either viewable by everyone or private.<br/>                                                                  |
| [**IncomingQueueBlocked**](-mfax-faxconfiguration-blockincomingqueue-vb.md)<br/>               | Read/write<br/> | Sets or retrieves a value that indicates whether the fax server queue for incoming faxes has been blocked. <br/>                                   |
| [**LowQuotaWaterMark**](-mfax-faxconfiguration-lowquotawatermark-vb.md)<br/>                   | Read/write<br/> | Sets or retrieves a value that indicates the minimum size of a watermark.<br/>                                                                     |
| [**OutgoingQueueAgeLimit**](-mfax-faxconfiguration-outgoingqueueagelimit-vb.md)<br/>           | Read/write<br/> | Sets or retrieves a value that indicates the length of time that an undeliverable fax message is kept on the fax server before it is deleted.<br/> |
| [**OutgoingQueueBlocked**](-mfax-faxconfiguration-blockoutgoingqueue-vb.md)<br/>               | Read/write<br/> | Sets or retrieves a value that indicates whether the fax server queue for outgoing faxes has been blocked. <br/>                                   |
| [**OutgoingQueuePaused**](-mfax-faxconfiguration-pauseoutgoingqueue-vb.md)<br/>                | Read/write<br/> | Sets or retrieves a value that indicates whether the outgoing queue has been paused.<br/>                                                          |
| [**Retries**](-mfax-faxconfiguration-retries-vb.md)<br/>                                       | Read/write<br/> | Sets or retrieves a value that indicates the number of redial attempts for a given fax job.<br/>                                                   |
| [**RetryDelay**](-mfax-faxconfiguration-retrydelay-vb.md)<br/>                                 | Read/write<br/> | Sets or retrieves a value that indicates the length of time the fax service should wait before retrying a failed fax transmission.<br/>            |
| [**SizeQuotaWarning**](-mfax-faxconfiguration-sizequotawarning-vb.md)<br/>                     | Read/write<br/> | Sets or retrieves a value that indicates whether the size quota warning is turned on.<br/>                                                         |
| [**UseArchive**](-mfax-faxconfiguration-usearchive-vb.md)<br/>                                 | Read/write<br/> | Sets or retrieves a value that indicates whether faxes should be archived.<br/>                                                                    |
| [**UseDeviceTSID**](-mfax-faxconfiguration-usedevicetsid-vb.md)<br/>                           | Read/write<br/> | Sets or retrieves a value that indicates whether the TSID is used. <br/>                                                                           |



 

## Remarks

![faxserver2 and faxconfiguration](images/faxconfiguation.png)

To create a **FaxConfiguration** object in Microsoft Visual Basic, call the [**Configuration**](-mfax-faxserver2-configuration-vb.md) property of the [**IFaxServer2**](-mfax-faxserver2-cpp.md) object.

To create a **FaxConfiguration** object in C++, call the [**Configuration**](-mfax-faxserver2-configuration-vb.md) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxConfiguration<br/>                                                      |



## See also

<dl> <dt>

[**IFaxConfiguration**](-mfax-ifaxconfiguration.md)
</dt> </dl>

 

 




