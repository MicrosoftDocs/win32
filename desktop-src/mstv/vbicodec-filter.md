---
title: VBICodec Filter
description: VBICodec Filter
ms.assetid: 51d43d2e-62fd-4366-a01f-5e6b37fc55fb
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# VBICodec Filter

This topic applies to Update Rollup 2 for Microsoft Windows XP Media Center Edition 2005 and later.

The VBICodec filter slices raw digitized data from the vertical blanking interval (VBI). Connect the input pin of this filter to VBI Out pin of an analog television capture filter. The filter has several output pins for the various VBI data services. Which output pins produce data depends on the input video standard.



| VBI Service                  | Video Standard |
|------------------------------|----------------|
| Teletext                     | PAL            |
| Wide screen signalling (WSS) | PAL, NTSC(J)   |
| Video program service (VPS)  | PAL            |
| Closed captioning (CC)       | NTSC           |



 

**Pin Data**



| Pin             | Major Type               | Subtype                        |
|-----------------|--------------------------|--------------------------------|
| Input           | MEDIATYPE\_VBI           | KSDATAFORMAT\_SUBTYPE\_RAW8    |
| Teletext Output | MEDIATYPE\_VBI           | MEDIASUBTYPE\_TELETEXT         |
| WSS Output      | MEDIATYPE\_VBI           | MEDIASUBTYPE\_WSS              |
| VPS Output      | MEDIATYPE\_VBI           | MEDIASUBTYPE\_VPS              |
| CC Output (1)   | MEDIATYPE\_AUXLine21Data | MEDIASUBTYPE\_Line21\_BytePair |
| CC Output (2)   | MEDIATYPE\_AUXLine21Data | MEDIASUBTYPE\_Line21\_BytePair |



 

**Filter Data**



| Property        | Value                                                              |
|-----------------|--------------------------------------------------------------------|
| Filter CLSID    | CLSID\_CCAFilter                                                   |
| Merit           | MERIT\_NORMAL                                                      |
| Filter Category | AM\_KSCATEGORY\_VBICODEC\_MI ("Multi-Instance Capable VBI Codecs") |



 

The closed captioning output pins expose the [**ICCSubStreamFiltering**](/windows/desktop/api/bdaiface/nn-bdaiface-iccsubstreamfiltering) interface, which can be used to filter the closed captioning services.

In Windows Vista and later, this filter replaces the [CC Decoder](https://msdn.microsoft.com/library/windows/desktop/dd368976) filter and the [WST Codec](https://msdn.microsoft.com/library/windows/desktop/dd391017) filter.

## Related topics

<dl> <dt>

[BDA Filters](bda-filters.md)
</dt> <dt>

[**Line 21 Media Types**](https://msdn.microsoft.com/library/windows/desktop/dd390643)
</dt> <dt>

[VBI Media Types](https://msdn.microsoft.com/library/windows/desktop/ff384871)
</dt> </dl>

 

 




