---
title: EC_WMT_EVENT (Windows Media Format 11 SDK)
description: EC\_WMT\_EVENT
ms.assetid: 51d51659-8e7d-49b7-83f2-a80e99d39d78
keywords:
- Windows Media Format SDK,EC_WMT_EVENT
- DirectShow,EC_WMT_EVENT
- EC_WMT_EVENT
- digital rights management (DRM),EC_WMT_EVENT
- DRM (digital rights management),EC_WMT_EVENT
- Advanced Systems Format (ASF),EC_WMT_EVENT
- ASF (Advanced Systems Format),EC_WMT_EVENT
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# EC_WMT_EVENT (Windows Media Format 11 SDK)

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Sent by the Windows Media Format SDK when an application uses the ASF Reader filter to play ASF files protected by digital rights management (DRM).

Parameters

*lParam1*

Can be one of the following WMT\_STATUS values.



| WMT\_STATUS Message           | Description                                                                                                                    |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| WMT\_NO\_RIGHTS               | The file is protected with DRM version 1 and the application has no rights to perform the requested action.                    |
| WMT\_ACQUIRE\_LICENSE         | The license acquisition process has been completed. (This does not necessarily mean that a license was successfully acquired.) |
| WMT\_NO\_RIGHTS\_EX           | The file is protected with DRM version 7 and the application has no rights to perform the requested action.                    |
| WMT\_NEEDS\_INDIVIDUALIZATION | The license allows only individualized applications to perform the requested action.                                           |
| WMT\_INDIVIDUALIZE            | The individualization process is now being performed or has been completed.                                                    |



 

*lParam2*

Pointer to an **AM\_WMT\_EVENT\_DATA** structure that contains information about the event in the **pData** member pointer, as well as an **HRESULT** status code sent by the Windows Media Format SDK. The value of *lParam2* depends on the value of *lParam1*, as described in the following table. (The "WM\_" structures are defined in the Windows Media Format SDK.)



| If lParam1 is...              | AM\_WMT\_EVENT\_DATA.pData is...                            |
|-------------------------------|-------------------------------------------------------------|
| WMT\_NO\_RIGHTS               | A pointer to a **WCHAR** string containing a challenge URL. |
| WMT\_ACQUIRE\_LICENSE         | A pointer to a **WM\_GET\_LICENSE\_DATA** structure.        |
| WMT\_NO\_RIGHTS\_EX           | A pointer to a **WM\_GET\_LICENSE\_DATA** structure.        |
| WMT\_NEEDS\_INDIVIDUALIZATION | NULL.                                                       |
| WMT\_INDIVIDUALIZE            | A pointer to a **WM\_INDIVIDUALIZE\_STATUS** structure.     |



 

## Related topics

<dl> <dt>

[**Digital Rights Management Features**](digital-rights-management-features.md)
</dt> <dt>

[**DirectShow QASF Reference**](directshow-qasf-reference.md)
</dt> <dt>

[**Enabling DRM Support**](enabling-drm-support.md)
</dt> </dl>

 

 




