---
title: IWMDRMLicense PersistLicense method (Wmdrmsdk.h)
description: The PersistLicense method saves the current license from the temporary store into the permanent local license store.
ms.assetid: 80a0f932-2800-416b-9dfe-97654a76c19b
keywords:
- PersistLicense method windows Media Format
- PersistLicense method windows Media Format , IWMDRMLicense interface
- IWMDRMLicense interface windows Media Format , PersistLicense method
topic_type:
- apiref
api_name:
- IWMDRMLicense.PersistLicense
api_location:
- Wmdrmsdk.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMLicense::PersistLicense method

The **PersistLicense** method saves the current license from the temporary store into the permanent local license store.

## Syntax


```C++
HRESULT PersistLicense();
```



## Parameters

This method has no parameters.

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

If the current license is not in the temporary store, this method will fail.

You can call [**CanPersist**](iwmdrmlicense-canpersist.md) to query whether the license is allowed to be persisted.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**IWMDRMLicense Interface**](iwmdrmlicense.md)
</dt> </dl>

 

 





