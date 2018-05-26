---
title: WM/WMRVContentProtectedPercent
description: Specifies the percentage of a DVR-MS file that is protected.
ms.assetid: 4760c4c4-6c3b-489c-b4e1-88b821e1f9c9
keywords:
- WM/WMRVContentProtectedPercent Microsoft TV Technologies
topic_type:
- apiref
api_name:
- WM/WMRVContentProtectedPercent
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WM/WMRVContentProtectedPercent

Specifies the percentage of a DVR-MS file that is protected.

## Data Type

**DWORD** (STREAMBUFFER\_TYPE\_DWORD)

## Remarks

Windows Media Center sets this attribute if the file contains any protected content. The value of this attribute is a number from 0 to 100, indicating the percentage of the file that is protected.

> [!Note]  
> The value might exceed 100. Treat any values over 100 as equivalent to 100 percent.

 

## See also

<dl> <dt>

[Detecting Content Protection in Recorded TV Files](detecting-content-protection-in-recorded-tv-files.md)
</dt> <dt>

[Stream Buffer Engine Attributes](stream-buffer-engine-attributes.md)
</dt> </dl>

 

 




