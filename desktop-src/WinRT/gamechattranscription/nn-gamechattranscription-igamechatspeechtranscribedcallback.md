---
UID: NN:gamechattranscription.IGameChatSpeechTranscribedCallback
title: IGameChatSpeechTranscribedCallback
description: Your application should implement this interface in order to receive notifications about the transcription results.
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
 - IGameChatSpeechTranscribedCallback
f1_keywords:
 - IGameChatSpeechTranscribedCallback
 - gamechattranscription/IGameChatSpeechTranscribedCallback
dev_langs:
 - c++
helpviewer_keywords:
 - IGameChatSpeechTranscribedCallback
ms.topic: reference
---

# IGameChatSpeechTranscribedCallback interface

> [!IMPORTANT]
> This API is not available to all apps. Unless your developer account is specially provisioned by Microsoft, calls to these APIs will fail at runtime.

Your application should implement this interface in order to receive notifications about the transcription results.

## Inheritance

The **IGameChatSpeechTranscribedCallback** interface derives from the **IUnknown** interface.

## Methods

The **IGameChatSpeechTranscribedCallback** interface has these methods.

| &nbsp; |
| ---- |
| [IGameChatSpeechTranscribedCallback::SpeechTranscribed](./nf-gamechattranscription-igamechatspeechtranscribedcallback-speechtranscribed.md) <br><br> GameChatTranscription calls your implementation of this function when transcription results are available. |

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | N/A |
