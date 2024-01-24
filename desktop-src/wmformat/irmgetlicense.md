---
title: IRMGetLicense interface
description: The IRMGetLicense interface is implemented in a run-time library that is installed as part of the Windows Media Format SDK.
ms.assetid: 95a8cf57-72a4-496d-8d25-d094b47c3a57
keywords:
- IRMGetLicense interface windows Media Format
- IRMGetLicense interface windows Media Format , described
topic_type:
- apiref
api_name:
- IRMGetLicense
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# IRMGetLicense interface

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

\[**IRMGetLicense** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use [Microsoft PlayReady](https://www.microsoft.com/PlayReady/). \]

The **IRMGetLicense** interface is implemented in a run-time library that is installed as part of the Windows Media Format SDK. It enables client-side license acquisition. Because this method is used by license issuers through Web-based applications, it is documented in the Windows Media Rights Manager SDK documentation.

## Members

The **IRMGetLicense** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface but does not have additional members.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

[**Interfaces**](interfaces.md)
</dt> </dl>

 

