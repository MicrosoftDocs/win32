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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# EC_WMT_INDEX_EVENT (Windows Media Format 11 SDK)

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




