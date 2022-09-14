---
description: Windows Portable Devices supports the following email properties.
ms.assetid: c886622e-57e7-4bd1-b645-0e979ee7b66a
title: Email Properties (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Email
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# Email Properties

Windows Portable Devices supports the following email properties.



| Property                         | VarType        | Description                                                                                                                               |
|----------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| **WPD\_EMAIL\_BCC\_LINE**        | **VT\_LPWSTR** | The BCC recipients of the e-mail message. BCC recipients receive a copy of the e-mail, but their names are not displayed as recipients.   |
| **WPD\_EMAIL\_CC\_LINE**         | **VT\_LPWSTR** | The CC recipients of the e-mail message. CC recipients receive a copy of the e-mail message, and their names are displayed as recipients. |
| **WPD\_EMAIL\_HAS\_ATTACHMENTS** | **VT\_BOOL**   | A Boolean value that specifies whether this e-mail message has attachments.                                                               |
| **WPD\_EMAIL\_HAS\_BEEN\_READ**  | **VT\_BOOL**   | A Boolean value that specifies whether this e-mail message has been read.                                                                 |
| **WPD\_EMAIL\_RECEIVED\_TIME**   | **VT\_DATE**   | A value that specifies when the e-mail message was received.                                                                              |
| **WPD\_EMAIL\_SENDER\_ADDRESS**  | **VT\_LPWSTR** | The e-mail address of the sender.                                                                                                         |
| **WPD\_EMAIL\_TO\_LINE**         | **VT\_LPWSTR** | The main recipients of the e-mail message.                                                                                                |



 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**WPD Properties and Attributes**](properties-and-attributes.md)
</dt> </dl>

 

 




