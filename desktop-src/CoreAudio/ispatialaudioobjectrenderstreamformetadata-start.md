---
Description: Starts the spatial audio stream.
ms.assetid: 554F1C09-4DA4-4F60-8940-4C3170314A9F
title: ISpatialAudioObjectRenderStreamForMetadata::Start method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ISpatialAudioObjectRenderStreamForMetadata::Start method

Starts the spatial audio stream.

## Syntax


```C++
HRESULT Start();
```



## Parameters

This method has no parameters.

## Return value

If the method succeeds, it returns S\_OK. If it fails, possible return codes include, but are not limited to, the values shown in the following table.



| Return code                                                                                                         | Description                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**SPTLAUDCLNT\_E\_STREAM\_NOT\_STOPPED**</dt> </dl> | The audio stream has not been stopped. Stop the stream by calling [**Stop**](/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-stop).<br/> |



 

## Remarks

Starting the stream causes data flow between the endpoint buffer and the audio engine. The first time this method is called, the stream's audio clock position will be at 0. Otherwise, the clock resumes from its position at the time that the stream was last paused with a call to [**Stop**](ispatialaudioobjectrenderstreamformetadata-stop.md). Call [**Reset**](ispatialaudioobjectrenderstreamformetadata-reset.md) to reset the clock position to 0 and cause all active [**ISpatialAudioObjectForMetadataCommands**](/windows/desktop/api/spatialaudiometadata/nn-spatialaudiometadata-ispatialaudioobjectformetadatacommands) or [**ISpatialAudioObjectForMetadataItems**](/windows/desktop/api/spatialaudiometadata/nn-spatialaudiometadata-ispatialaudioobjectformetadataitems) instances to be revoked.

The stream must have been previously stopped with a call to [**Stop**](ispatialaudioobjectrenderstreamformetadata-stop.md) or the method will fail and return SPTLAUDCLNT\_E\_STREAM\_NOT\_STOPPED.

## See also

<dl> <dt>

[**ISpatialAudioObjectRenderStreamForMetadata**](/windows/desktop/api/SpatialAudioMetadata/nn-spatialaudiometadata-ispatialaudioobjectrenderstreamformetadata)
</dt> </dl>

 

 




