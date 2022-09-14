---
title: EC_WMT_INDEX_EVENT (Windows Media Format 11 SDK)
description: EC\_WMT\_INDEX\_EVENT
ms.assetid: 46e6a011-7f25-470b-9e10-fa59f0ddbf22
keywords:
- Windows Media Format SDK,EC_WMT_INDEX_EVENT
- DirectShow,EC_WMT_INDEX_EVENT
- EC_WMT_INDEX_EVENT
- Advanced Systems Format (ASF),EC_WMT_INDEX_EVENT
- ASF (Advanced Systems Format),EC_WMT_INDEX_EVENT
ms.topic: article
ms.date: 05/31/2018
---

# EC_WMT_INDEX_EVENT (Windows Media Format 11 SDK)

Sent by the Windows Media Format SDK when an application uses the ASF Writer to index Windows Media Video files.

Parameters

*lParam1*

Can be any one of the following **WMT\_STATUS** messages.



| Message              | Description                                     |
|----------------------|-------------------------------------------------|
| WMT\_STARTED         | Indexing has begun. *lParam2* is zero.          |
| WMT\_CLOSED          | Indexing has been completed. *lParam2* is zero. |
| WMT\_INDEX\_PROGRESS | Indexing is in progress.                        |



 

*lParam2*

If *lParam1* is WMT\_CLOSED or WMT\_STARTED, then *lParam2* is zero. If *lParam1* is WMT\_INDEX\_PROGRESS, then *lParam2* is a **DWORD** that expresses the amount of progress as a percentage of the total download size.

## Related topics

<dl> <dt>

[**DirectShow QASF Reference**](directshow-qasf-reference.md)
</dt> </dl>

 

 




