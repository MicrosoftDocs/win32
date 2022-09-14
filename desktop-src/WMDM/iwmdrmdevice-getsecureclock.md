---
title: IWMDRMDevice GetSecureClock method
description: The GetSecureClock method retrieves the secure clock, so time-based licenses can be enforced.
ms.assetid: 6de9b7ce-9c2a-44e5-9de7-40cfbaf4d92c
keywords:
- GetSecureClock method windows Media Device Manager
- GetSecureClock method windows Media Device Manager , IWMDRMDevice interface
- IWMDRMDevice interface windows Media Device Manager , GetSecureClock method
topic_type:
- apiref
api_name:
- IWMDRMDevice.GetSecureClock
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMDevice::GetSecureClock method

The **GetSecureClock** method retrieves the secure clock, so time-based licenses can be enforced.

## Syntax


```C++
HRESULT GetSecureClock(
  [out] BYTE  **ppbSecureClock,
  [out] DWORD *pcbSecureClock,
  [out] DWORD *pdwFlags
);
```



## Parameters

<dl> <dt>

*ppbSecureClock* \[out\]
</dt> <dd>

Retrieved secure clock.

</dd> <dt>

*pcbSecureClock* \[out\]
</dt> <dd>

Size of the secure clock, in bytes.

</dd> <dt>

*pdwFlags* \[out\]
</dt> <dd>

Device status flags. This value must be one of the following flags.



| Flag                     | Description                            |
|--------------------------|----------------------------------------|
| WMDRM\_DEVICE\_ISWMDRM   | The device supports Windows Media DRM. |
| WMDRM\_DEVICE\_NEEDCLOCK | The device needs clock.                |
| WMDRM\_DEVICE\_REVOKED   | The device has been revoked.           |



 

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>WMDDRMSP.idl</dt> </dl> |
| Library<br/> | <dl> <dt>Mssachlp.lib</dt> </dl> |



## See also

<dl> <dt>

[**GetSecureClockChallenge**](iwmdrmdevice-getsecureclockchallenge.md)
</dt> <dt>

[**IWMDRMDevice Interface**](iwmdrmdevice.md)
</dt> <dt>

[**SetSecureClockResponse**](iwmdrmdevice-setsecureclockresponse.md)
</dt> </dl>

 

 





