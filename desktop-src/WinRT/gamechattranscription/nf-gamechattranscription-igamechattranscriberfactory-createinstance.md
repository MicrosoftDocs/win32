---
UID: NF:gamechattranscription.IGameChatTranscriberFactory.CreateInstance
title: IGameChatTranscriberFactory::CreateInstance
description: Your application should call CreateInstance for each audio stream that it wants to process for speech transcription.
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
 - IGameChatTranscriberFactory::CreateInstance
f1_keywords:
 - IGameChatTranscriberFactory::CreateInstance
 - gamechattranscription/IGameChatTranscriberFactory::CreateInstance
dev_langs:
 - c++
helpviewer_keywords:
 - CreateInstance
ms.topic: reference
---

# IGameChatTranscriberFactory::CreateInstance method

> [!IMPORTANT]
> This API is not available to all apps. Unless your developer account is specially provisioned by Microsoft, calls to these APIs will fail at runtime.

Your application should call **CreateInstance** for each audio stream that it wants to process for speech transcription. Typically, your app will create this once when the audio stream is available, and destroy it when the stream ends.

## Syntax

```cpp
HRESULT CreateInstance(
  [in] LPCWSTR xboxUserId,
  [in] GameChatAudioEncoding encoding,
  [in] BOOL audioDataCollectionAllowed,
  [in] IGameChatSpeechTranscribedCallback* handler,
  [out] DWORD* eventSourceCookie,
  [in] REFIID riid,
  [out, iid_is(riid)] LPVOID* ppvObject
);
```

## Parameters

`xboxUserId`

User ID of the local user (used for authentication).

`encoding`

Audio encoding format that will be used for input buffers passed to **IGameChatTranscriber::ProcessEncodedAudio**.

`audioDataCollectionAllowed`

`true` if the Xbox user consents to have audio data collected for audio data improvement; otherwise, `false`.

`handler`

Callback handler.

`eventSourceCookie`

Opaque ID unique for callbacks sourced from this instance (identifies the source audio stream).

`riid`

The IID of **IGameChatTranscriber**.

`ppvObject`

On success, points to an **IGameChatTranscriber** instance.

## Return value

If this method succeeds, it returns **S_OK**. Otherwise, it returns an **HRESULT** error code.

## See also

[IGameChatTranscriberFactory](./nn-gamechattranscription-igamechattranscriberfactory.md)

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | N/A |
| **Library** | N/A |
| **DLL** | GameChatTranscription.dll |
