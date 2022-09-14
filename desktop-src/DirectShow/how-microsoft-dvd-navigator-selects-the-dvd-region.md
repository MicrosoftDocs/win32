---
description: How Microsoft DVD Navigator Selects the DVD Region
ms.assetid: 407619c6-2d4b-4f7f-a861-42ee0f462ecd
title: How Microsoft DVD Navigator Selects the DVD Region
ms.topic: article
ms.date: 05/31/2018
---

# How Microsoft DVD Navigator Selects the DVD Region

The Microsoft DVD Navigator uses the following algorithm to determine region match while playing DVD discs on a PC:

1.  The DVD Navigator gets the disc region, drive region, and decoder region.
2.  If the disc region is "all regions," the DVD Navigator plays the disc.
3.  If the disc is not marked for all regions, the DVD Navigator checks whether the decoder has a preset region.
4.  If the decoder has a preset region and it does not match the disc region, the DVD Navigator returns an error indicating that it cannot play the disc on the current DVD configuration. (Exit)
5.  If the decoder region is not set, or is the same as the disc region, the DVD Navigator checks whether the drive region is the same as the disc region.
6.  If the drive region matches the disc region, the DVD Navigator plays the title.
7.  Otherwise, if the driver region does not match the disc region, the DVD Navigator invokes the code to change the drive's region. If the allowed number of region changes has been exhausted, the region change attempt fails and the title cannot be played on that system.

## Related topics

<dl> <dt>

[DVD Region Change Support in Windows](dvd-region-change-support-in-windows.md)
</dt> </dl>

 

 



