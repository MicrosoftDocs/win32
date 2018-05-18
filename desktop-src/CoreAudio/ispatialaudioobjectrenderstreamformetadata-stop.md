---
Description: 'Stops a running audio stream.'
ms.assetid: '0E129803-9DCE-4398-83C7-AA099450168D'
title: 'ISpatialAudioObjectRenderStreamForMetadata::Stop method'
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

Stopping stream causes data to stop flowing between the endpoint buffer and the audio engine. You can consider this operation to pause the stream because it leaves the stream's audio clock at its current stream position and does not reset it to 0. A subsequent call to [**Start**](ispatialaudioobjectrenderstreamformetadata-start.md) causes the stream to resume running from the current position. Call [**Reset**](iaudioclient-reset.md) to reset the clock position to 0 and cause all active [**ISpatialAudioObjectForMetadataCommands**](ispatialaudioobjectformetadatacommands.md) or [**ISpatialAudioObjectForMetadataItems**](ispatialaudioobjectformetadataitems.md) instances to be revoked.

## See also

<dl> <dt>

[**ISpatialAudioObjectRenderStreamForMetadata**](ispatialaudioobjectrenderstreamformetadata.md)
</dt> </dl>

 

 



