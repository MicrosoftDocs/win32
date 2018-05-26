---
title: MSVidFeatures
description: MSVidFeatures
ms.assetid: 19790fab-0530-4a17-8a3c-a50576fea9ca
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSVidFeatures

This topic applies to Windows XP or later.

The **MSVidFeatures** object represents a collection of features.



|                           |                                          |
|---------------------------|------------------------------------------|
| Interfaces                | [**IMSVidFeatures**](/windows/win32/segment/nn-segment-imsvidfeatures?branch=master) |
| Outgoing Event Interfaces | None.                                    |



 

## Remarks

To obtain the collection of features that are currently active, call the [**IMSVidCtl::get\_FeaturesActive**](/windows/previous-versions/msvidctl/nf-msvidctl-imsvidctl-get_featuresactive?branch=master) method. To obtain the collection of all the features that are available, call the [**IMSVidCtl::get\_FeaturesAvailable**](/windows/previous-versions/msvidctl/nf-msvidctl-imsvidctl-get_featuresavailable?branch=master) method.

To set the active features, create an empty **MSVidFeatures** object using **CoCreateInstance**. Enumerate the available features collection, and add the features that you want to activate into the new **MSVidFeatures** object. Then call the [**IMSVidCtl::put\_FeaturesActive**](/windows/previous-versions/msvidctl/nf-msvidctl-imsvidctl-put_featuresactive?branch=master) method with a pointer to your **MSVidFeatures** object.

## Related topics

<dl> <dt>

[Video Control Objects (C++)](video-control-objects--c.md)
</dt> </dl>

 

 




