---
title: IWMDRMLicense CreateDecryptor method (Wmdrmsdk.h)
description: The CreateDecryptor method creates a decryptor object using the settings of the current license.
ms.assetid: 69b7f96b-a0d6-455e-8ef9-0faf9690cef1
keywords:
- CreateDecryptor method windows Media Format
- CreateDecryptor method windows Media Format , IWMDRMLicense interface
- IWMDRMLicense interface windows Media Format , CreateDecryptor method
topic_type:
- apiref
api_name:
- IWMDRMLicense.CreateDecryptor
api_location:
- Wmdrmsdk.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMLicense::CreateDecryptor method

The **CreateDecryptor** method creates a decryptor object using the settings of the current license.

## Syntax


```C++
HRESULT CreateDecryptor(
  [out] IWMDRMDecrypt **ppDecryptor
);
```



## Parameters

<dl> <dt>

*ppDecryptor* \[out\]
</dt> <dd>

Receives a pointer to the [**IWMDRMDecrypt**](iwmdrmdecrypt.md) interface of the newly created object.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                                | Description                                              |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>**NS\_E\_DRM\_RIV\_TOO\_SMALL**</dt> </dl> | An updated content revocation list is needed.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>                       | The method succeeded.<br/>                         |



 

## Remarks

None.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**CreateEncryptor**](iwmdrmlicense-createencryptor.md)
</dt> <dt>

[**IWMDRMLicense Interface**](iwmdrmlicense.md)
</dt> </dl>

 

 





