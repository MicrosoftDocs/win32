---
title: DWM Registry Values
description: This section contains information about the Desktop Window Manager (DWM) registry values.
ms.assetid: 26b36617-54c2-405a-9a7d-bd86fefa94b6
keywords:
- Desktop Window Manager (DWM),reference
- DWM (Desktop Window Manager),reference
- Desktop Window Manager (DWM),structures
- DWM (Desktop Window Manager),structures
ms.topic: concept-article
ms.date: 04/15/2024
---

# DWM Registry Values

This section contains information about the Desktop Window Manager (DWM) registry values.

## In this section



| Path | Value | Data |
|------|-------|------|
| HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\Dwm | OverlayMinFPS | A DWORD. If this value is present and set to zero, the Desktop Window Manager disables its minimum frame rate requirement for assigning DirectX swap chains to overlay planes in hardware that supports overlays. This makes it more likely that a low frame rate swap chain will get assigned and stay assigned to an overlay plane, if available. This mechanism was introduced in its present form in Windows 11. This registry value may be modified or removed in future releases. |



 

 

 





