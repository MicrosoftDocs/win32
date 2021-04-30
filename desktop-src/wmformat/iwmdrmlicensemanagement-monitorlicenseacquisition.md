---
title: IWMDRMLicenseManagement MonitorLicenseAcquisition method (Wmdrmsdk.h)
description: The MonitorLicenseAcquisition method initiates monitoring for a license acquisition process.
ms.assetid: 725cd51a-a50b-4ff5-a880-7f551f6dba8f
keywords:
- MonitorLicenseAcquisition method windows Media Format
- MonitorLicenseAcquisition method windows Media Format , IWMDRMLicenseManagement interface
- IWMDRMLicenseManagement interface windows Media Format , MonitorLicenseAcquisition method
topic_type:
- apiref
api_name:
- IWMDRMLicenseManagement.MonitorLicenseAcquisition
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMLicenseManagement::MonitorLicenseAcquisition method

The **MonitorLicenseAcquisition** method initiates monitoring for a license acquisition process.

## Syntax


```C++
HRESULT MonitorLicenseAcquisition(
  [in]  BSTR     bstrKID,
  [in]  BSTR     bstrHeader,
  [in]  BSTR     bstrActions,
  [out] IUnknown **ppunkCancelationCookie
);
```



## Parameters

<dl> <dt>

*bstrKID* \[in\]
</dt> <dd>

Key ID (KID) of the license being acquired.

</dd> <dt>

*bstrHeader* \[in\]
</dt> <dd>

Content header that was used in the call to the [**AcquireLicense**](iwmdrmlicensemanagement-acquirelicense.md) method.

</dd> <dt>

*bstrActions* \[in\]
</dt> <dd>

String containing the actions requested in the call to the **AcquireLicense** method.

</dd> <dt>

*ppunkCancelationCookie* \[out\]
</dt> <dd>

Pointer that receives a pointer to the **IUnknown** interface of an object that identifies this asynchronous call. This interface pointer can be used to cancel the asynchronous call by calling the [**IWMDRMEventGenerator::CancelAsyncOperation**](iwmdrmeventgenerator-cancelasyncoperation.md) method.

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

[**IWMDRMLicenseManagement Interface**](iwmdrmlicensemanagement.md)
</dt> </dl>

 

 





