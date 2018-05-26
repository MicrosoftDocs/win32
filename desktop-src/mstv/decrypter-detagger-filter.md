---
title: Decrypter/Detagger Filter
description: Decrypter/Detagger Filter
ms.assetid: a16eac70-49d7-4ff3-baaf-9f29c3efef0f
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Decrypter/Detagger Filter

This topic applies to Windows XP Service Pack 1 or later.

The Decrypter/Detagger filter conditionally decrypts samples that are encrypted by the [Encrypter/Tagger](encrypter-tagger-filter.md) filter.

This filter reads ratings information from the encrypted samples and passes them to the [EvalRat](evalrat-object.md) object. The **EvalRat** object determines whether the content is allowed. If so, the Decrypter/Detagger filter decrypts the samples and passes them downstream for rendering.



|                                            |                                                                                                                                                              |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter interfaces                          | [**IBaseFilter**](https://msdn.microsoft.com/library/windows/desktop/dd389526), [**IDTFilter**](/windows/previous-versions/EncDec/nn-encdec-idtfilter?branch=master), [**IDTFilterConfig**](/windows/previous-versions/EncDec/nn-encdec-idtfilterconfig?branch=master), [**IBroadcastEvent**](/windows/previous-versions/tuner/nn-tuner-ibroadcastevent?branch=master) |
| Input pin media types                      | MEDIASUBTYPE\_ETDTFilter\_Tagged                                                                                                                             |
| Input pin interfaces                       | [**IKsPropertySet**](https://msdn.microsoft.com/library/windows/desktop/dd390144), [**IMemInputPin**](https://msdn.microsoft.com/library/windows/desktop/dd407073), [**IPin**](https://msdn.microsoft.com/library/windows/desktop/dd390397), [**IQualityControl**](https://msdn.microsoft.com/library/windows/desktop/dd376912)     |
| Output pin media types                     | See Remarks                                                                                                                                                  |
| Output pin interfaces                      | [**IPin**](https://msdn.microsoft.com/library/windows/desktop/dd390397), [**IQualityControl**](https://msdn.microsoft.com/library/windows/desktop/dd376912)                                                                                         |
| Filter CLSID                               | CLSID\_DTFilter                                                                                                                                              |
| [Merit](https://msdn.microsoft.com/library/windows/desktop/dd390674)                       | MERIT\_DO\_NOT\_USE                                                                                                                                          |
| [Filter category](https://msdn.microsoft.com/library/windows/desktop/dd375655) | CLSID\_CPCAFiltersCategory                                                                                                                                   |



 

The output type matches the original input type received by the Encrypter/Tagger filter.

## Remarks

This filter is not available to DirectShow applications except to get parental ratings on an unencrypted file. It can be used for content decryption only through the Video Control on Microsoft Windows XP Media Center Edition.

The output type matches the original input type received by the Encrypter/Tagger filter.

## Related topics

<dl> <dt>

[Overview of the TV Ratings System](overview-of-the-tv-ratings-system.md)
</dt> <dt>

[About the Stream Buffer Engine](about-the-stream-buffer-engine.md)
</dt> </dl>

 

 




