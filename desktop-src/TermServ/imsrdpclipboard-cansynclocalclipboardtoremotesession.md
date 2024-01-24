---
title: IMsRdpClipboard CanSyncLocalClipboardToRemoteSession method
description: Indicates whether the local Clipboard can be synced to the remote session.
ms.tgt_platform: multiple
keywords:
- CanSyncLocalClipboardToRemoteSession method Remote Desktop Services
- CanSyncLocalClipboardToRemoteSession method Remote Desktop Services, IMsRdpClipboard interface
- IMsRdpClipboard interface Remote Desktop Services, CanSyncLocalClipboardToRemoteSession method
topic_type:
- apiref
api_name:
- IMsRdpClipboard.CanSyncLocalClipboardToRemoteSession
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 12/16/2020
---

# IMsRdpClipboard::CanSyncLocalClipboardToRemoteSession method

Indicates whether the local Clipboard can be synced to the remote session.

## Syntax

```C++
HRESULT CanSyncLocalClipboardToRemoteSession(
  [out, retval] VARIANT_BOOL* pfSync
);
```

## Parameters

**TRUE** if the local Clipboard can be synced to the remote session; otherwise, **FALSE**.

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