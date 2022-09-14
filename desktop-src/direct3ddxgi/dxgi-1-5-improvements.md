---
description: The following functionality has been added to Microsoft DirectX Graphics Infrastructure (DXGI) 1.5, to support more flexible specifying and duplication of output formats.
ms.assetid: DD7401E1-9991-48D8-AD23-4D34238EA4AF
title: DXGI 1.5 Improvements
ms.topic: article
ms.date: 03/05/2021
---

# DXGI 1.5 Improvements

The following functionality has been added to Microsoft DirectX Graphics Infrastructure (DXGI) 1.5, to support more flexible specifying and duplication of output formats.

## High Dynamic Range and Wide Color Gamut

Refer to [Using DirectX with high dynamic range displays and advanced color](../direct3darticles/high-dynamic-range.md).

## Variable refresh rate displays

Refer to [Variable refresh rate displays](variable-refresh-rate-displays.md).

## Duplicating output

A single interface, [**IDXGIOutput5**](/windows/win32/api/DXGI1_5/nn-dxgi1_5-idxgioutput5), with a single method, [**DuplicateOutput1**](/windows/win32/api/DXGI1_5/nf-dxgi1_5-idxgioutput5-duplicateoutput1), has been added to DXGI 1.5 to provide a more flexible and higher performance version of the original [**DuplicateOutput**](/windows/win32/api/DXGI1_2/nf-dxgi1_2-idxgioutput1-duplicateoutput) method. **DuplicateOutput1** allows specifying a list of supported formats for fullscreen surfaces that can be returned by the [**IDXGIOutputDuplication**](/windows/win32/api/DXGI1_2/nn-dxgi1_2-idxgioutputduplication) object, and enables capturing HDR and WCG content.

## Offering and Reclaiming Resources

Updated methods [**OfferResources1**](/windows/win32/api/dxgi1_5/nf-dxgi1_5-idxgidevice4-offerresources1) and [**ReclaimResources1**](/windows/win32/api/dxgi1_5/nf-dxgi1_5-idxgidevice4-reclaimresources1) have been added to a new interface, [**IDXGIDevice4**](/windows/win32/api/dxgi1_5/nn-dxgi1_5-idxgidevice4), to allow de-committing of memory in addition to discarding resources. Opting in to the new [**DXGI\_OFFER\_RESOURCE\_FLAG\_ALLOW\_DECOMMIT**](/windows/win32/api/dxgi1_5/ne-dxgi1_5-dxgi_offer_resource_flags) flag means the new reclaim results must be properly handled.

## Related topics

[Programming Guide for DXGI](dx-graphics-dxgi-overviews.md)
