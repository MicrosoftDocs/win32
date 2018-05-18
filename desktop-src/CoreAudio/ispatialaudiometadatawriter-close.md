---
Description: 'Completes any needed operations on the metadata buffer and releases the specified ISpatialAudioMetadataItems object.'
ms.assetid: '2417E624-6535-49E2-9CF4-F927F731BE41'
title: 'ISpatialAudioMetadataWriter::Close method'
---

# ISpatialAudioMetadataWriter::Close method

Completes any needed operations on the metadata buffer and releases the specified [**ISpatialAudioMetadataItems**](ispatialaudiometadataitems.md) object.

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
| <dl> <dt>**SPTLAUD\_MD\_CLNT\_E\_NO\_ITEMS\_OPEN**</dt> </dl>            | The supplied [**ISpatialAudioMetadataItems**](ispatialaudiometadataitems.md) has not been opened with a call to [**Open**](ispatialaudiometadatawriter-open.md).<br/> |
| <dl> <dt>**SPTLAUD\_MD\_CLNT\_E\_NO\_ITEMS\_WRITTEN**</dt> </dl>         | No metadata items have been written to the supplied [**ISpatialAudioMetadataItems**](ispatialaudiometadataitems.md).<br/>                                              |
| <dl> <dt>**SPTLAUD\_MD\_CLNT\_E\_ITEM\_MUST\_HAVE\_COMMANDS**</dt> </dl> | No metadata commands have been written to the supplied [**ISpatialAudioMetadataItems**](ispatialaudiometadataitems.md).<br/>                                           |



 

## See also

<dl> <dt>

[**ISpatialAudioMetadataWriter**](ispatialaudiometadatawriter.md)
</dt> </dl>

 

 




