---
title: WM/WMRVExpirationDate
description: Specifies the date when the license expires for a DVR-MS file. After this date, the file cannot be played.
ms.assetid: '792a724f-9a3b-40cd-b112-9f06b5016714'
keywords: ["WM/WMRVExpirationDate Microsoft TV Technologies"]
topic_type:
- apiref
api_name:
- WM/WMRVExpirationDate
api_type:
- NA
---

# WM/WMRVExpirationDate

Specifies the date when the license expires for a DVR-MS file. After this date, the file cannot be played.

## Data Type

The data type is a **DATE** type stored as a **QWORD** (STREAMBUFFER\_TYPE\_QWORD)

## Remarks

Windows Media Center sets this attribute if the file contains protected content with an expiration date. If the content never expires or is not protected, Windows Media Center either omits the attribute or sets it to the maximum **DATE** value, which is 23:59:59.9999999, December 31, 9999.

The **DATE** type is documented in the Microsoft Foundation Class (MFC) Library documentation. You can use the **COleDateTime** class in MFC to manipulate this type.

## See also

<dl> <dt>

[Detecting Content Protection in Recorded TV Files](detecting-content-protection-in-recorded-tv-files.md)
</dt> <dt>

[Stream Buffer Engine Attributes](stream-buffer-engine-attributes.md)
</dt> </dl>

 

 




