---
description: The PeriodicUpdatePicture method is called by an application to configure a timer in the stream that will ask for picture updates periodically. Picture updates cause high bandwidth usage, so this method will normally be used instead of UpdatePicture.
ms.assetid: 6ae3b5e9-bc11-4f3f-972b-21c9ac299987
title: IKeyFrameControl::PeriodicUpdatePicture method (H323priv.h)
ms.topic: reference
ms.date: 05/31/2018
---

# IKeyFrameControl::PeriodicUpdatePicture method

\[**PeriodicUpdatePicture** is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **PeriodicUpdatePicture** method is called by an application to configure a timer in the stream that will ask for picture updates periodically. Picture updates cause high bandwidth usage, so this method will normally be used instead of [**UpdatePicture**](ikeyframecontrol-updatepicture.md).

If the method is called when the stream is active, the timer will start immediately. If the stream is not active, the timer will be started when the stream enters the active state.

## Syntax


```C++
HRESULT PeriodicUpdatePicture(
  [in] BOOL  fEnable,
  [in] DWORD dwInterval
);
```



## Parameters

<dl> <dt>

*fEnable* \[in\]
</dt> <dd>

**TRUE** enables the timer. **FALSE** disables it.

</dd> <dt>

*dwInterval* \[in\]
</dt> <dd>

The interval for the timer, in seconds.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                            | Description                               |
|----------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Method succeeded.<br/>              |
| <dl> <dt>**E\_FAIL**</dt> </dl> | Failed for unexpected reasons.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>H323priv.h</dt> </dl> |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl>  |



## See also

<dl> <dt>

[H323 MSP](h323-msp.md)
</dt> </dl>

 

 




