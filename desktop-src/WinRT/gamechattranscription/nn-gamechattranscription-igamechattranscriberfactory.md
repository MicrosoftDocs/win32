---
UID: NN:gamechattranscription.IGameChatTranscriberFactory
title: IGameChatTranscriberFactory
description: Used to obtain an IGameChatTranscriber instance.
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
 - IGameChatTranscriberFactory
f1_keywords:
 - IGameChatTranscriberFactory
 - gamechattranscription/IGameChatTranscriberFactory
dev_langs:
 - c++
helpviewer_keywords:
 - IGameChatTranscriberFactory
ms.topic: reference
---

# IGameChatTranscriberFactory interface

> [!IMPORTANT]
> This API is not available to all apps. Unless your developer account is specially provisioned by Microsoft, calls to these APIs will fail at runtime.

Used to obtain an **IGameChatTranscriber** instance.

## Inheritance

The **IGameChatTranscriberFactory** interface derives from the **IUnknown** interface.

## Methods

The **IGameChatTranscriberFactory** interface has these methods.

| &nbsp; |
| ---- |
| [IGameChatTranscriberFactory::CreateInstance](./nf-gamechattranscription-igamechattranscriberfactory-createinstance.md) <br><br> Your application should call **CreateInstance** for each audio stream that it wants to process for speech transcription. Typically, your app will create this once when the audio stream is available, and destroy it when the stream ends. |

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | N/A |
