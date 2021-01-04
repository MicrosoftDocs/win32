---
title: IMsRdpClipboard SyncRemoteClipboardToLocalSession method
description: Syncs the remote Clipboard to the local session.
ms.tgt_platform: multiple
keywords:
- SyncRemoteClipboardToLocalSession method Remote Desktop Services
- SyncRemoteClipboardToLocalSession method Remote Desktop Services, IMsRdpClipboard interface
- IMsRdpClipboard interface Remote Desktop Services, SyncRemoteClipboardToLocalSession method
topic_type:
- apiref
api_name:
- IMsRdpClipboard.SyncRemoteClipboardToLocalSession
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 12/16/2020
---

# IMsRdpClipboard::SyncRemoteClipboardToLocalSession method

Syncs the remote Clipboard to the local session.

## Syntax

```C++
HRESULT SyncRemoteClipboardToLocalSession();
```

## Parameters

This method has no parameters.

## Return value

Return **S\_OK** if successful.

## Requirements

| Requirement | Value |
|-------------------------------------|---------------------------------------|
| Minimum supported client| Windows 10, version 1803 (build 17134)      |
| Type library            | MsTscAx.dll                        |
| DLL                  | MsTscAx.dll     |
| IID                      | IID\_IMsRdpClipboard is defined as 2E769EE8-00C7-43DC-AFD9-235D75B72A40          |

## See also

<dl> <dt>

[**IMsRdpClipboard**](imsrdpclipboard.md)
</dt> </dl>