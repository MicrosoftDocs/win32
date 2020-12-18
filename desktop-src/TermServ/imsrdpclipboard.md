---
title: IMsRdpClipboard interface
description: Represents the Clipboard controller used to synchronize the local and remote clipboards if manual clipboard sync is enabled.
ms.tgt_platform: multiple
keywords:
- IMsRdpClipboard interface Remote Desktop Services
- IMsRdpClipboard interface Remote Desktop Services, described
topic_type:
- apiref
api_name:
- IMsRdpClipboard
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 12/16/2020
---

# IMsRdpClipboard interface

Represents the Clipboard controller used to synchronize the local and remote clipboards if manual clipboard sync is enabled (that is, the [ManualClipboardSyncEnabled](imsrdpextendedsettings-property.md) property value is set to **True**).

## Members

The **IMsRdpClipboard** interface inherits from **IUnknown**. **IMsRdpClipboard** also has these types of members:

- [Methods](#methods)

### Methods

The **IMsRdpClipboard** interface has these methods.


| Method        | Description      |
|:---------------|:----------------|
| [**CanSyncLocalClipboardToRemoteSession**](imsrdpclipboard-cansynclocalclipboardtoremotesession.md)       |  Indicates whether the local Clipboard can be synced to the remote session.                   |
| [**CanSyncRemoteClipboardToLocalSession**](imsrdpclipboard-cansyncremoteclipboardtolocalsession.md)       |  Indicates whether the remote Clipboard can be synced to the local session.                   |
| [**SyncLocalClipboardToRemoteSession**](imsrdpclipboard-synclocalclipboardtoremotesession.md)       |  Syncs the local Clipboard to the remote session.                   |
| [**SyncRemoteClipboardToLocalSession**](imsrdpclipboard-syncremoteclipboardtolocalsession.md)       |   Syncs the remote Clipboard to the local session.                      |

## Requirements

| Requirement | Value |
|-------------------------------------|---------------------------------------|
| Minimum supported client| Windows 10, version 1803 (build 17134)      |
| Type library            | MsTscAx.dll                        |
| DLL                  | MsTscAx.dll     |
| IID                      | IID\_IMsRdpClipboard is defined as 2E769EE8-00C7-43DC-AFD9-235D75B72A40            |

## See also

<dl> <dt>

[**IMsRdpClientNonScriptable7::Clipboard**](imsrdpclientnonscriptable7-clipboard.md)
</dt> </dl>
