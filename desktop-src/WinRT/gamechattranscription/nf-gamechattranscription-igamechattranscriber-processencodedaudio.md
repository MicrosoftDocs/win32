---
UID: NF:gamechattranscription.IGameChatTranscriber.ProcessEncodedAudio
title: IGameChatTranscriber::ProcessEncodedAudio
description: Your application should call ProcessEncodedAudio with each sequential audio buffer to be processed for transcription.
ms.date: 07/21/2023
tech.root: winrt
targetos: Windows
prerelease: false
req.assembly: 
req.construct-type: function
req.ddi-compliance: 
req.dll: 
req.header: 
req.idl: 
req.include-header: 
req.irql: 
req.kmdf-ver: 
req.lib: 
req.max-support: 
req.namespace: 
req.redist: 
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.target-type: 
req.type-library: 
req.umdf-ver: 
req.unicode-ansi: 
topic_type:
 - apiref
api_type:
 - COM
api_location:
 - GameChatTranscription.dll
api_name:
 - IGameChatTranscriber::ProcessEncodedAudio
f1_keywords:
 - IGameChatTranscriber::ProcessEncodedAudio
 - gamechattranscription/IGameChatTranscriber::ProcessEncodedAudio
dev_langs:
 - c++
helpviewer_keywords:
 - ProcessEncodedAudio
ms.topic: reference
---

# IGameChatTranscriber::ProcessEncodedAudio method

> [!IMPORTANT]
> This API is not available to all apps. Unless your developer account is specially provisioned by Microsoft, calls to these APIs will fail at runtime.

Your application should call **ProcessEncodedAudio** with each sequential audio buffer to be processed for transcription.

## Syntax

```cpp
HRESULT ProcessEncodedAudio(
  [in, size_is(audioBufferSize)] const BYTE* audioBuffer,
  [in] UINT32 audioBufferSize
);
```

## Parameters

`audioBuffer`

Audio buffer encoded using the format specified in **IGameChatTranscriberFactory::CreateInstance**.

`audioBufferSize`

Size, in bytes, of *audioBuffer*.

## Return value

If this method succeeds, it returns **S_OK**. Otherwise, it returns an **HRESULT** error code.

## See also

[IGameChatTranscriber](./nn-gamechattranscription-igamechattranscriber.md)

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | N/A |
| **Library** | N/A |
| **DLL** | GameChatTranscription.dll |
