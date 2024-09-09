---
UID: NN:gamechattranscription.IGameChatTranscriber
title: IGameChatTranscriber
description: Maps one-to-one to an audio stream that needs to be transcribed. Can accept encoded audio sequentially for a single audio stream.
ms.date: 07/21/2023
tech.root: winrt
targetos: Windows
prerelease: false
req.assembly: 
req.construct-type: iface
req.ddi-compliance: 
req.header: 
req.idl: 
req.include-header: 
req.max-support: 
req.namespace: 
req.redist: 
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.target-type: 
req.unicode-ansi: 
topic_type:
 - apiref
api_type:
 - COM
api_location:
 - GameChatTranscription.dll
api_name:
 - IGameChatTranscriber
f1_keywords:
 - IGameChatTranscriber
 - gamechattranscription/IGameChatTranscriber
dev_langs:
 - c++
helpviewer_keywords:
 - IGameChatTranscriber
ms.topic: reference
---

# IGameChatTranscriber interface

> [!IMPORTANT]
> This API is not available to all apps. Unless your developer account is specially provisioned by Microsoft, calls to these APIs will fail at runtime.

Maps one-to-one to an audio stream that needs to be transcribed. Can accept encoded audio sequentially for a single audio stream.

## Inheritance

The **IGameChatTranscriber** interface derives from the **IUnknown** interface.

## Methods

The **IGameChatTranscriber** interface has these methods.

| &nbsp; |
| ---- |
| [IGameChatTranscriber::ProcessEncodedAudio](./nf-gamechattranscription-igamechattranscriber-processencodedaudio.md) <br><br> Your application should call **ProcessEncodedAudio** with each sequential audio buffer to be processed for transcription. |
| [IGameChatTranscriber::EndSpokenPhrase](./nf-gamechattranscription-igamechattranscriber-endspokenphrase.md) <br><br> Your application should call **EndSpokenPhrase** when it detects a period of silence in the audio stream. |

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | N/A |
