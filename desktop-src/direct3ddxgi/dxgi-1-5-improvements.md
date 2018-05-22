---
Description: 'The following functionality has been added to Microsoft DirectX Graphics Infrastructure (DXGI) 1.5, to support more flexible specifying and duplication of output formats.'
ms.assetid: 'DD7401E1-9991-48D8-AD23-4D34238EA4AF'
title: 'DXGI 1.5 Improvements'
---

# DXGI 1.5 Improvements

The following functionality has been added to Microsoft DirectX Graphics Infrastructure (DXGI) 1.5, to support more flexible specifying and duplication of output formats.

-   [High Dynamic Range and Wide Color Gamut](#high-dynamic-range-and-wide-color-gamut)
-   [Variable refresh rate displays](#variable-refresh-rate-displays)
-   [Duplicating output](#duplicating-output)
-   [Offering and Reclaiming Resources](#offering-and-reclaiming-resources)
-   [Related topics](#related-topics)

## High Dynamic Range and Wide Color Gamut

Refer to [High Dynamic Range and Wide Color Gamut](high-dynamic-range-and-wide-color-gamut.md).

## Variable refresh rate displays

Refer to [Variable refresh rate displays](variable-refresh-rate-displays.md).

## Duplicating output

A single interface, [**IDXGIOutput5**](idxgioutput5.md), with a single method, [**DuplicateOutput1**](idxgioutput5-duplicateoutput1.md), has been added to DXGI 1.5 to provide a more flexible and higher performance version of the original [**DuplicateOutput**](idxgioutput1-duplicateoutput.md) method. **DuplicateOutput1** allows specifying a list of supported formats for fullscreen surfaces that can be returned by the [**IDXGIOutputDuplication**](idxgioutputduplication.md) object.

## Offering and Reclaiming Resources

Updated methods, [**OfferResources1**](idxgidevice4-offerresources1.md) and [**ReclaimResources1**](idxgidevice4-reclaimresources1.md), have been added to a new interface, [**IDXGIDevice4**](idxgidevice4.md), to allow de-committing of memory in addition to discarding resources. Opting in to the new [**DXGI\_OFFER\_RESOURCE\_FLAG\_ALLOW\_DECOMMIT**](dxgi-offer-resource-flags.md) flag means the new reclaim results must be properly handled.

## Related topics

<dl> <dt>

[Programming Guide for DXGI](dx-graphics-dxgi-overviews.md)
</dt> </dl>

 

 



