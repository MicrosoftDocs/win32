---
title: XDS Codec Filter
description: XDS Codec Filter
ms.assetid: 5b04314e-76e4-48af-911f-707a5db2100c
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# XDS Codec Filter

This topic applies to Windows XP Service Pack 1 or later.

The XDS Codec filter supports third-party software that decodes TV ratings information from the extended data services (XDS) channel of line 21.

This filter receives XDS data from the CC Decoder filter or some other source. It passes this data to the [XDSToRat](xdstorat-object.md) object, which is responsible for parsing the data into content ratings. The **XDSToRat** object returns the decoded ratings to the XDS Codec filter.



|                                            |                                                                                                                  |
|--------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Filter interfaces                          | [**IBaseFilter**](https://msdn.microsoft.com/library/windows/desktop/dd389526), [**IBroadcastEvent**](/windows/previous-versions/tuner/nn-tuner-ibroadcastevent?branch=master), [**IXDSCodec**](/windows/previous-versions/EncDec/nn-encdec-ixdscodec?branch=master) |
| Input pin media types                      | Major type: MEDIATYPE\_AUXLine21DataSubtype: MEDIASUBTYPE\_Line21\_BytePair<br/>                           |
| Input pin interfaces                       | [**IMemInputPin**](https://msdn.microsoft.com/library/windows/desktop/dd407073), [**IPin**](https://msdn.microsoft.com/library/windows/desktop/dd390397), [**IQualityControl**](https://msdn.microsoft.com/library/windows/desktop/dd376912)     |
| Output pin media types                     | Not applicable                                                                                                   |
| Output pin interfaces                      | Not applicable                                                                                                   |
| Filter CLSID                               | CLSID\_XDSCodec                                                                                                  |
| [Merit](https://msdn.microsoft.com/library/windows/desktop/dd390674)                       | MERIT\_DO\_NOT\_USE                                                                                              |
| [Filter category](https://msdn.microsoft.com/library/windows/desktop/dd375655) | CLSID\_CPCAFiltersCategory                                                                                       |



 

## Related topics

<dl> <dt>

[Overview of the TV Ratings System](overview-of-the-tv-ratings-system.md)
</dt> <dt>

[About the Stream Buffer Engine](about-the-stream-buffer-engine.md)
</dt> </dl>

 

 





