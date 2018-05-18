---
title: GetTSAudioEndpointEnumeratorForSession callback function
description: Returns a reference to an audio endpoint enumerator for the specified session ID.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '9dd95ef7-f83f-43be-a8b2-e2b0e4a47a42'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["GetTSAudioEndpointEnumeratorForSession callback function Remote Desktop Services"]
topic_type:
- apiref
api_name:
- GetTSAudioEndpointEnumeratorForSession
api_type:
- UserDefined
---

# GetTSAudioEndpointEnumeratorForSession callback function

Returns a reference to an audio endpoint enumerator for the specified session ID. Consumers of this audio endpoint enumerator, such as MMDevAPI.dll, call this function to retrieve an audio endpoint enumerator in a Remote Desktop Services session.

## Syntax


```C++
HRESULT GetTSAudioEndpointEnumeratorForSession(
  _In_  DWORD               SessionId,
  _Out_ IMMDeviceEnumerator **ppEndpointEnumerator
);
```



## Parameters

<dl> <dt>

*SessionId* \[in\]
</dt> <dd>

The identifier of the Remote Desktop Services session.

</dd> <dt>

*ppEndpointEnumerator* \[out\]
</dt> <dd>

The address of a pointer to an [**IMMDeviceEnumerator**](https://msdn.microsoft.com/library/windows/desktop/dd371399) interface.

</dd> </dl>

## Return value

If the method succeeds, it returns **S\_OK**.

## Remarks

This function is not defined in a header file. You should implement and export this function in your custom endpoint enumerator and use the signature shown in the syntax block earlier in this topic.

## Requirements



|                                     |                                   |
|-------------------------------------|-----------------------------------|
| Minimum supported client<br/> | None supported<br/>         |
| Minimum supported server<br/> | Windows Server 2008 R2<br/> |



## See also

<dl> <dt>

[Implementing a Custom Audio Endpoint Enumerator](implementing-an-audio-endpoint-enumerator.md)
</dt> <dt>

[**IMMDeviceEnumerator**](https://msdn.microsoft.com/library/windows/desktop/dd371399)
</dt> </dl>

 

 





