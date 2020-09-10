---
title: Queued present model is being deprecated
description: Queued present model is being deprecated
ms.assetid: 271CD4F7-0992-47DB-AF5A-B77570EF681A
ms.topic: article
ms.date: 05/31/2018
---

# Queued present model is being deprecated

## Platforms

**Clients** – After Windows 8  
**Servers** – After Windows Server 2012  


## Description

In the Windows release after Windows 8, these APIs will return E\_NOTIMPL:

-   DwmSetPresentParameters
-   DwmSetDxFrameDuration
-   DwmModifyPreviousDxFrameDuration

In addition, this API will only accept the NULL value for the hwnd parameter:

-   DwmGetCompositionTimingInfo

We will stop supporting DwmGetCompositionTimingInfo with hwnd != NULL and remove associated functionality. If non-NULL value for hwnd is specified, this API will return E\_INVALIDARG.

We also discourage the use of DwmGetCompositionTimingInfo API and suggest that developers switch to the DXGI flip model and associated DX present statistics API.

## Manifestation

Applications that use the queued present model will not function correctly. The exact manifestation depends on the particular application, but can range from incorrect presentation timing to the application exiting unexpectedly). In practice, we do not expect to see many (if any) such applications. This model was used by Vista media player, which will not be used on Windows 8 (and possibly the old Zune player). At this time we don’t have info about any other applications actually using this model.

## Solution

Developers need to use the DXGI flip presentation mode instead of queued present (available in DX9 runtime since Windows 7, and on DX10 and DX11 runtimes in Windows 8).

## Tests

Run general tests to ensure that inbox Windows components and major products continue to work on the next version of Windows.

 

 




