---
description: The SetExternalT120Address method is called by an application to configure an external T.120 address for data exchange.
ms.assetid: 094b43b9-eb15-468a-9986-86313490e1c3
title: IH323LineEx::SetExternalT120Address method (H323priv.h)
ms.topic: reference
ms.date: 05/31/2018
---

# IH323LineEx::SetExternalT120Address method

\[**SetExternalT120Address** is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **SetExternalT120Address** method is called by an application to configure an external T.120 address for data exchange. T.120 capability will be advertised during the H.245 negotiation, and the address will be used in the open logic channel acknowledgement so that the other endpoint can set up T.120 sessions with the service listening on that address. If this function is not called, the H.323 service provider will not advertise T.120 capability.

## Syntax


```C++
HRESULT SetExternalT120Address(
  [in] BOOL  fEnable,
  [in] DWORD dwIP,
  [in] WORD  wPort
);
```



## Parameters

<dl> <dt>

*fEnable* \[in\]
</dt> <dd>

**TRUE** to enable T.120 capability; **FALSE** to disable T.120 capability.

</dd> <dt>

*dwIP* \[in\]
</dt> <dd>

**DWORD** containing the IP address in host byte order of the external T.120 service.

</dd> <dt>

*wPort* \[in\]
</dt> <dd>

**WORD** containing the port of the external T.120 service.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                          | Description                  |
|--------------------------------------------------------------------------------------|------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | Method succeeded.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>H323priv.h</dt> </dl> |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl>  |



 

 




