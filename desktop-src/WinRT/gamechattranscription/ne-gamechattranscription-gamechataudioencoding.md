---
UID: NE:gamechattranscription.GameChatAudioEncoding
title: GameChatAudioEncoding
description: Encoding format that will be used for input buffers passed to IGameChatTranscriber::ProcessEncodedAudio.
tech.root: winrt
ms.date: 07/21/2023
targetos: Windows
prerelease: false
req.construct-type: enumeration
req.header: 
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.typenames: GameChatAudioEncoding
req.redist: 
f1_keywords:
 - GameChatAudioEncoding
 - gamechattranscription/GameChatAudioEncoding
 - GameChatAudioEncoding
 - gamechattranscription/GameChatAudioEncoding
dev_langs:
 - c++
topic_type:
 - APIRef
 - kbSyntax
api_type:
 - HeaderDef
api_location:
 - GameChatTranscription.dll
api_name:
 - GameChatAudioEncoding
ms.topic: reference
---

# GameChatAudioEncoding enumeration

> [!IMPORTANT]
> This API is not available to all apps. Unless your developer account is specially provisioned by Microsoft, calls to these APIs will fail at runtime.

Encoding format that will be used for input buffers passed to **IGameChatTranscriber::ProcessEncodedAudio**.

## Syntax

```cpp
typedef enum {
  GameChatAudioEncoding_SILKv3 = 0
} GameChatAudioEncoding;
```

## Constants

| Name | Description |
| - | - |
| GameChatAudioEncoding_SILKv3 | SILK version 3 audio encoding. |

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | N/A |
