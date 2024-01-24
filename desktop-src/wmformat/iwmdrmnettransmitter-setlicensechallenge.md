---
title: IWMDRMNetTransmitter SetLicenseChallenge method (Wmdrmsdk.h)
description: The SetLicenseChallenge method processes a license challenge sent by a Windows Media DRM for Network Devices receiver.
ms.assetid: 3d4cd029-a8f5-49fc-ba8c-d8615ff94366
keywords:
- SetLicenseChallenge method windows Media Format
- SetLicenseChallenge method windows Media Format , IWMDRMNetTransmitter interface
- IWMDRMNetTransmitter interface windows Media Format , SetLicenseChallenge method
topic_type:
- apiref
api_name:
- IWMDRMNetTransmitter.SetLicenseChallenge
api_location:
- Wmdrmsdk.h
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMDRMNetTransmitter::SetLicenseChallenge method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **SetLicenseChallenge** method processes a license challenge sent by a Windows Media DRM for Network Devices receiver.

## Syntax


```C++
HRESULT SetLicenseChallenge(
  [in] BYTE  *pbLicenseChallenge,
  [in] DWORD cbLicenseChallenge
);
```



## Parameters

<dl> <dt>

*pbLicenseChallenge* \[in\]
</dt> <dd>

Pointer to the license challenge data that was sent by a receiver.

</dd> <dt>

*cbLicenseChallenge* \[in\]
</dt> <dd>

Size of license challenge in bytes.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

If this method succeeds, subsequent calls to the other methods of **IWMDRMNetTransmitter** will use the information in the processed challenge.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**IWMDRMNetTransmitter Interface**](iwmdrmnettransmitter.md)
</dt> </dl>

 

 





