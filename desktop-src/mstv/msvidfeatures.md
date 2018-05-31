---
title: MSVidFeatures
description: MSVidFeatures
ms.assetid: 19790fab-0530-4a17-8a3c-a50576fea9ca
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSVidFeatures

This topic applies to Windows XP or later.

The **MSVidFeatures** object represents a collection of features.



|                           |                                          |
|---------------------------|------------------------------------------|
| Interfaces                | [**IMSVidFeatures**](/windows/desktop/api/segment/nn-segment-imsvidfeatures) |
| Outgoing Event Interfaces | None.                                    |



 

## Remarks

To obtain the collection of features that are currently active, call the [**IMSVidCtl::get\_FeaturesActive**](/previous-versions/windows/desktop/api/msvidctl/nf-msvidctl-imsvidctl-get_featuresactive) method. To obtain the collection of all the features that are available, call the [**IMSVidCtl::get\_FeaturesAvailable**](/previous-versions/windows/desktop/api/msvidctl/nf-msvidctl-imsvidctl-get_featuresavailable) method.

To set the active features, create an empty **MSVidFeatures** object using **CoCreateInstance**. Enumerate the available features collection, and add the features that you want to activate into the new **MSVidFeatures** object. Then call the [**IMSVidCtl::put\_FeaturesActive**](/previous-versions/windows/desktop/api/msvidctl/nf-msvidctl-imsvidctl-put_featuresactive) method with a pointer to your **MSVidFeatures** object.

## Related topics

<dl> <dt>

[Video Control Objects (C++)](video-control-objects--c.md)
</dt> </dl>

 

 




