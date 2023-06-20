---
description: The SetDynamicReconnectLevel method sets the level of dynamic reconnection during rendering.
ms.assetid: 092f3464-84a2-48b0-9647-66fe27e9706d
title: IRenderEngine::SetDynamicReconnectLevel method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IRenderEngine.SetDynamicReconnectLevel
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IRenderEngine::SetDynamicReconnectLevel method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetDynamicReconnectLevel` method sets the level of dynamic reconnection during rendering.

## Syntax


```C++
HRESULT SetDynamicReconnectLevel(
   DWORD Level
);
```



## Parameters

<dl> <dt>

*Level* 
</dt> <dd>

Combination of [**Dynamic Reconnection Flags**](dynamic-reconnection-flags.md), specifying the level of dynamic reconnection.

</dd> </dl>

## Return value

Returns one of the following **HRESULT** values:



| Return code                                                                               | Description                 |
|-------------------------------------------------------------------------------------------|-----------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | Success.<br/>         |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | Not implemented.<br/> |



 

## Remarks

By default, the basic render engine loads every source before rendering a project. This can result in a long start-up time. With dynamic reconnection, sources are loaded only when needed. This can shorten the start-up time, but possibly interfere with smooth playback. Generally, the more source clips that a project uses, the more you might benefit from dynamic reconnection.

The smart render engine does not implement this method.

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[**IRenderEngine Interface**](irenderengine.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




