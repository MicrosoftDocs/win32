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
ms.date: 05/31/2018
---

# IWMDRMProvider::CreateObject method

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

 

 





