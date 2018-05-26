---
Description: Gets additional services from the ISpatialAudioObjectRenderStreamForMetadata.
ms.assetid: 568F3D03-7296-475B-880B-E6FD0C2BD863
title: ISpatialAudioObjectRenderStreamForMetadataGetService method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ISpatialAudioObjectRenderStreamForMetadata::GetService method

Gets additional services from the [**ISpatialAudioObjectRenderStreamForMetadata**](/windows/win32/SpatialAudioMetadata/nn-spatialaudiometadata-ispatialaudioobjectrenderstreamformetadata?branch=master).

## Syntax


```C++
HRESULT GetService(
  [in]  REFIID riid,
  [out] REFIID **service
);
```



## Parameters

<dl> <dt>

*riid* \[in\]
</dt> <dd>

The interface ID for the requested service. The client should set this parameter to one of the following REFIID values:

IID\_IAudioClock

IID\_IAudioClock2

</dd> <dt>

*service* \[out\]
</dt> <dd>

Pointer to a pointer variable into which the method writes the address of an instance of the requested interface. Through this method, the caller obtains a counted reference to the interface. The caller is responsible for releasing the interface, when it is no longer needed, by calling the interface's [**Release**](com.iunknown_release) method. If the **GetService** call fails, *\*ppv* is NULL.

</dd> </dl>

## Return value

If the method succeeds, it returns S\_OK. If it fails, possible return codes include, but are not limited to, the values shown in the following table.



| Return code                                                                                                    | Description                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_POINTER**</dt> </dl>                      | Parameter *ppv* is NULL.<br/>                                                                                                                                                               |
| <dl> <dt>**AUDCLNT\_E\_DEVICE\_INVALIDATED**</dt> </dl> | The audio endpoint device has been unplugged, or the audio hardware or associated hardware resources have been reconfigured, disabled, removed, or otherwise made unavailable for use.<br/> |



 

## Remarks

The **GetService** method supports the following service interfaces:

-   [**IAudioClock**](/windows/win32/Audioclient/nn-audioclient-iaudioclock?branch=master)
-   [**IAudioClock2**](/windows/win32/audioclient/nn-audioclient-iaudioclock2?branch=master)
-   [**IAudioStreamVolume**](/windows/win32/Audioclient/nn-audioclient-iaudiostreamvolume?branch=master)

## See also

<dl> <dt>

[**ISpatialAudioObjectRenderStreamForMetadata**](/windows/win32/SpatialAudioMetadata/nn-spatialaudiometadata-ispatialaudioobjectrenderstreamformetadata?branch=master)
</dt> </dl>

 

 




