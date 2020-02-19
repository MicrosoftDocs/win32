---
title: To Find Stream Numbers and Output Numbers
description: To Find Stream Numbers and Output Numbers
ms.assetid: 531edd4a-a257-47cd-a367-b59cda3ea76c
keywords:
- Advanced Systems Format (ASF),stream numbers
- ASF (Advanced Systems Format),creating numbers
- Advanced Systems Format (ASF),finding output numbers
- ASF (Advanced Systems Format),finding output numbers
- synchronous readers,stream numbers
- synchronous readers,finding output numbers
- streams,finding numbers
ms.topic: article
ms.date: 05/31/2018
---

# To Find Stream Numbers and Output Numbers

The synchronous reader supports more simplified switching between stream and output numbers for playback than the asynchronous reader. It is therefore more important to be able to find which stream numbers equate to which output numbers, or the other way around.

To find the output number that corresponds to a stream number, call [**IWMSyncReader::GetOutputNumberForStream**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmsyncreader-getoutputnumberforstream).

To find the stream number that corresponds to an output number, call [**IWMSyncReader::GetStreamNumberForOutput**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmsyncreader-getstreamnumberforoutput)

## Related topics

<dl> <dt>

[**IWMSyncReader Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmsyncreader)
</dt> <dt>

[**Inputs, Streams and Outputs**](inputs-streams-and-outputs.md)
</dt> <dt>

[**Reading Files with the Synchronous Reader**](reading-files-with-the-synchronous-reader.md)
</dt> </dl>

 

 




