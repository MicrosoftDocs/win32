---
Description: Stops a running audio stream.
ms.assetid: 0E129803-9DCE-4398-83C7-AA099450168D
title: ISpatialAudioObjectRenderStreamForMetadataStop method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ISpatialAudioObjectRenderStreamForMetadata::Stop method

Stops a running audio stream.

## Syntax


```C++
HRESULT Stop();
```



## Parameters

This method has no parameters.

## Return value

If the method succeeds, it returns S\_OK. If the stream is not running when this method is called, it returns S\_FALSE.

## Remarks

Stopping stream causes data to stop flowing between the endpoint buffer and the audio engine. You can consider this operation to pause the stream because it leaves the stream's audio clock at its current stream position and does not reset it to 0. A subsequent call to [**Start**](ispatialaudioobjectrenderstreamformetadata-start.md) causes the stream to resume running from the current position. Call [**Reset**](/windows/win32/Audioclient/nf-audioclient-iaudioclient-reset?branch=master) to reset the clock position to 0 and cause all active [**ISpatialAudioObjectForMetadataCommands**](/windows/win32/spatialaudiometadata/nn-spatialaudiometadata-ispatialaudioobjectformetadatacommands?branch=master) or [**ISpatialAudioObjectForMetadataItems**](/windows/win32/spatialaudiometadata/nn-spatialaudiometadata-ispatialaudioobjectformetadataitems?branch=master) instances to be revoked.

## See also

<dl> <dt>

[**ISpatialAudioObjectRenderStreamForMetadata**](/windows/win32/SpatialAudioMetadata/nn-spatialaudiometadata-ispatialaudioobjectrenderstreamformetadata?branch=master)
</dt> </dl>

 

 



