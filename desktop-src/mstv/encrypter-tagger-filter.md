---
title: Encrypter/Tagger Filter
description: Encrypter/Tagger Filter
ms.assetid: 5687144b-f878-465e-9bc5-dce52dad8ec7
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Encrypter/Tagger Filter

This topic applies to Windows XP Service Pack 1 or later.

The Encrypter/Tagger filter encrypts media samples and tags them with ratings information from the [XDS Codec](xds-codec-filter.md) filter.



|                                            |                                                                                                                                                              |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter interfaces                          | [**IBaseFilter**](https://msdn.microsoft.com/library/windows/desktop/dd389526), [**IBroadcastEvent**](/windows/previous-versions/tuner/nn-tuner-ibroadcastevent?branch=master), [**IETFilter**](/windows/previous-versions/EncDec/nn-encdec-ietfilter?branch=master), [**IETFilterConfig**](/windows/previous-versions/EncDec/nn-encdec-ietfilterconfig?branch=master) |
| Input pin media types                      | Any                                                                                                                                                          |
| Input pin interfaces                       | [**IMemInputPin**](https://msdn.microsoft.com/library/windows/desktop/dd407073), [**IPin**](https://msdn.microsoft.com/library/windows/desktop/dd390397), [**IQualityControl**](https://msdn.microsoft.com/library/windows/desktop/dd376912)                                                 |
| Output pin media types                     | MEDIASUBTYPE\_ETDTFilter\_Tagged                                                                                                                             |
| Output pin interfaces                      | [**IPin**](https://msdn.microsoft.com/library/windows/desktop/dd390397), [**IQualityControl**](https://msdn.microsoft.com/library/windows/desktop/dd376912)                                                                                         |
| Filter CLSID                               | CLSID\_ETFilter                                                                                                                                              |
| [Merit](https://msdn.microsoft.com/library/windows/desktop/dd390674)                       | MERIT\_DO\_NOT\_USE                                                                                                                                          |
| [Filter category](https://msdn.microsoft.com/library/windows/desktop/dd375655) | CLSID\_CPCAFiltersCategory                                                                                                                                   |



 

Whether encryption is actually applied to the content depends on the copy protection policy that is set by the content owner and/or broadcaster. Microsoft Windows XP Media Center determines the copy protection policy by reading the broadcaster's copy protection flag (CGMS-A). If the flag specifies no encryption, then the resulting file will be accessible by any DirectShow-based application that uses the Stream Buffer Engine.

The output type matches the input type, except the subtype is changed to MEDIASUBTYPE\_ETDTFilter\_Tagged.

## Remarks

This filter is not available to DirectShow applications. It can only be used through the Video Control on Microsoft Windows XP Media Center Edition.

Whether encryption is actually applied to the content depends on the copy protection policy that is set by the content owner and/or broadcaster. Microsoft Windows XP Media Center determines the copy protection policy by reading the broadcaster's copy protection flag (CGMS-A). If the flag specifies no encryption, then the resulting file will be accessible by any DirectShow-based application that uses the Stream Buffer Engine.

The output type matches the input type, except the subtype is changed to MEDIASUBTYPE\_ETDTFilter\_Tagged.

## Related topics

<dl> <dt>

[Overview of the TV Ratings System](overview-of-the-tv-ratings-system.md)
</dt> <dt>

[About the Stream Buffer Engine](about-the-stream-buffer-engine.md)
</dt> </dl>

 

 




