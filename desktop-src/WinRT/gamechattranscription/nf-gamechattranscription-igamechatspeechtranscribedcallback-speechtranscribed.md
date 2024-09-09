---
UID: NF:gamechattranscription.IGameChatSpeechTranscribedCallback.SpeechTranscribed
title: IGameChatSpeechTranscribedCallback::SpeechTranscribed
description: GameChatTranscription calls your implementation of this function when transcription results are available.
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
 - IGameChatSpeechTranscribedCallback::SpeechTranscribed
f1_keywords:
 - IGameChatSpeechTranscribedCallback::SpeechTranscribed
 - gamechattranscription/IGameChatSpeechTranscribedCallback::SpeechTranscribed
dev_langs:
 - c++
helpviewer_keywords:
 - SpeechTranscribed
ms.topic: reference
---

# IGameChatSpeechTranscribedCallback::SpeechTranscribed method

> [!IMPORTANT]
> This API is not available to all apps. Unless your developer account is specially provisioned by Microsoft, calls to these APIs will fail at runtime.

GameChatTranscription calls your implementation of this function when transcription results are available.

## Syntax

```cpp
HRESULT SpeechTranscribed(
  [in] DWORD eventSourceCookie,
  [in, string] LPCWSTR transcribedText
);
```

## Parameters

`eventSourceCookie`

Opaque id unique to an **IGameChatTranscriber** object; comes as an output from **IGameChatTranscriberFactory::CreateInstance**.

`transcribedText`

Transcribed text that comes in.

## Return value

If this method succeeds, it returns **S_OK**. Otherwise, it returns an **HRESULT** error code.

## See also

[IGameChatSpeechTranscribedCallback](./nn-gamechattranscription-igamechatspeechtranscribedcallback.md)

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | N/A |
| **Library** | N/A |
| **DLL** | GameChatTranscription.dll |
