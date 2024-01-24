---
title: IWMDRMProvider CreateObject method (Wmdrmsdk.h)
description: The CreateObject method retrieves a pointer to a specified interface, creating the implementing object if needed.
ms.assetid: d408f7f3-9e49-4747-ac8f-d39db31d1240
keywords:
- CreateObject method windows Media Format
- CreateObject method windows Media Format , IWMDRMProvider interface
- IWMDRMProvider interface windows Media Format , CreateObject method
topic_type:
- apiref
api_name:
- IWMDRMProvider.CreateObject
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMDRMProvider::CreateObject method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **CreateObject** method retrieves a pointer to a specified interface, creating the implementing object if needed.

## Syntax


```C++
HRESULT CreateObject(
  [in]  REFIID riid,
  [out] void   **ppvObject
);
```



## Parameters

<dl> <dt>

*riid* \[in\]
</dt> <dd>

Identifier of the interface to be created. Set to one of the following values.

-   IID\_IWMDRMLicenseManagement
-   IID\_IWMDRMLicenseQuery
-   IID\_IWMDRMNetReceiver
-   IID\_IWMDRMNetTransmitter
-   IID\_IWMDRMSecurity

</dd> <dt>

*ppvObject* \[out\]
</dt> <dd>

Address of a pointer that receives the address of the requested interface.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

None.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wmdrmsdk.h</dt> </dl>   |
| Library<br/> | <dl> <dt>Wmdrmsdk.lib</dt> </dl> |



## See also

<dl> <dt>

[**IWMDRMProvider Interface**](iwmdrmprovider.md)
</dt> <dt>

[**IWMDRMLicenseManagement Interface**](iwmdrmlicensemanagement.md)
</dt> <dt>

[**IWMDRMLicenseQuery Interface**](iwmdrmlicensequery.md)
</dt> <dt>

[**IWMDRMNetReceiver Interface**](iwmdrmnetreceiver.md)
</dt> <dt>

[**IWMDRMNetTransmitter Interface**](iwmdrmnettransmitter.md)
</dt> <dt>

[**IWMDRMSecurity Interface**](iwmdrmsecurity.md)
</dt> </dl>

 

 





