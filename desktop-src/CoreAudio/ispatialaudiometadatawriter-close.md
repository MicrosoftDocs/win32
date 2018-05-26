---
Description: Completes any needed operations on the metadata buffer and releases the specified ISpatialAudioMetadataItems object.
ms.assetid: 2417E624-6535-49E2-9CF4-F927F731BE41
title: ISpatialAudioMetadataWriterClose method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ISpatialAudioMetadataWriter::Close method

Completes any needed operations on the metadata buffer and releases the specified [**ISpatialAudioMetadataItems**](/windows/win32/SpatialAudioMetadata/nn-spatialaudiometadata-ispatialaudiometadataitems?branch=master) object.

## Syntax


```C++
HRESULT Close();
```



## Parameters

This method has no parameters.

## Return value

If the method succeeds, it returns S\_OK. If it fails, possible return codes include, but are not limited to, the values shown in the following table.



| Return code                                                                                                                     | Description                                                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**SPTLAUD\_MD\_CLNT\_E\_NO\_ITEMS\_OPEN**</dt> </dl>            | The supplied [**ISpatialAudioMetadataItems**](/windows/win32/SpatialAudioMetadata/nn-spatialaudiometadata-ispatialaudiometadataitems?branch=master) has not been opened with a call to [**Open**](/windows/win32/SpatialAudioMetadata/nf-spatialaudiometadata-ispatialaudiometadatawriter-open?branch=master).<br/> |
| <dl> <dt>**SPTLAUD\_MD\_CLNT\_E\_NO\_ITEMS\_WRITTEN**</dt> </dl>         | No metadata items have been written to the supplied [**ISpatialAudioMetadataItems**](/windows/win32/SpatialAudioMetadata/nn-spatialaudiometadata-ispatialaudiometadataitems?branch=master).<br/>                                              |
| <dl> <dt>**SPTLAUD\_MD\_CLNT\_E\_ITEM\_MUST\_HAVE\_COMMANDS**</dt> </dl> | No metadata commands have been written to the supplied [**ISpatialAudioMetadataItems**](/windows/win32/SpatialAudioMetadata/nn-spatialaudiometadata-ispatialaudiometadataitems?branch=master).<br/>                                           |



 

## See also

<dl> <dt>

[**ISpatialAudioMetadataWriter**](/windows/win32/SpatialAudioMetadata/nn-spatialaudiometadata-ispatialaudiometadatawriter?branch=master)
</dt> </dl>

 

 




