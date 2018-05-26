---
Description: Reset a stopped audio stream.
ms.assetid: 3C2DFBFA-E5A3-43BC-B9EF-19CCDAA6BD0D
title: ISpatialAudioObjectRenderStreamForMetadataReset method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ISpatialAudioObjectRenderStreamForMetadata::Reset method

Reset a stopped audio stream.

## Syntax


```C++
HRESULT Reset();
```



## Parameters

This method has no parameters.

## Return value

If the method succeeds, it returns S\_OK. If it fails, possible return codes include, but are not limited to, the values shown in the following table.



| Return code                                                                                                         | Description                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**SPTLAUDCLNT\_E\_STREAM\_NOT\_STOPPED**</dt> </dl> | The audio stream has not been stopped. Stop the stream by calling [**Stop**](/windows/win32/Audioclient/nf-audioclient-iaudioclient-stop?branch=master).<br/> |



 

## Remarks

Resetting the audio stream flushes all pending data and resets the audio clock stream position to 0. Resetting the stream also causes all active [**ISpatialAudioObjectForMetadataCommands**](/windows/win32/spatialaudiometadata/nn-spatialaudiometadata-ispatialaudioobjectformetadatacommands?branch=master) or [**ISpatialAudioObjectForMetadataItems**](/windows/win32/spatialaudiometadata/nn-spatialaudiometadata-ispatialaudioobjectformetadataitems?branch=master) instances to be revoked. A subsequent call to [**Start**](ispatialaudioobjectrenderstreamformetadata-start.md) causes the stream to start from 0 position.

The stream must have been previously stopped with a call to [**Stop**](ispatialaudioobjectrenderstreamformetadata-stop.md) or the method will fail and return SPTLAUDCLNT\_E\_STREAM\_NOT\_STOPPED.

## See also

<dl> <dt>

[**ISpatialAudioObjectRenderStreamForMetadata**](/windows/win32/SpatialAudioMetadata/nn-spatialaudiometadata-ispatialaudioobjectrenderstreamformetadata?branch=master)
</dt> </dl>

 

 




