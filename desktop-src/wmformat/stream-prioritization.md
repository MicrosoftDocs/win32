---
title: Stream Prioritization
description: Stream Prioritization
ms.assetid: '6b3e9b03-62ef-422b-97ab-197d1cd15beb'
keywords: ["Windows Media Format SDK,stream prioritization", "Advanced Systems Format (ASF),stream prioritization", "ASF (Advanced Systems Format),stream prioritization", "Windows Media Format SDK,priority order for streams", "Advanced Systems Format (ASF),priority order for streams", "ASF (Advanced Systems Format),priority order for streams", "streams,prioritization"]
---

# Stream Prioritization

When you create an ASF file, you can specify a priority order for its constituent streams. If you stream a prioritized file and the available bandwidth is not enough to deliver all of the streams, the reader will drop streams in reverse priority order. In this way you can guarantee that the most important streams in your file will not be dropped due to network difficulties.

Stream prioritization is configured with a stream prioritization object and added to the profile. A profile can contain only one stream prioritization object.

## Related topics

<dl> <dt>

[**ASF File Features**](asf-file-features.md)
</dt> <dt>

[**IWMProfile3::CreateNewStreamPrioritization**](iwmprofile3-createnewstreamprioritization.md)
</dt> <dt>

[**IWMProfile3::GetStreamPrioritization**](iwmprofile3-getstreamprioritization.md)
</dt> <dt>

[**IWMProfile3::RemoveStreamPrioritization**](iwmprofile3-removestreamprioritization.md)
</dt> <dt>

[**IWMProfile3::SetStreamPrioritization**](iwmprofile3-setstreamprioritization.md)
</dt> <dt>

[**IWMStreamPrioritization Interface**](iwmstreamprioritization.md)
</dt> <dt>

[**Using Stream Prioritization**](using-stream-prioritization.md)
</dt> </dl>

 

 




