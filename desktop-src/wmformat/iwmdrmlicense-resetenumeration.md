---
title: IWMDRMLicense ResetEnumeration method (Wmdrmsdk.h)
description: The ResetEnumeration method resets the license list to its original state. The active license becomes the first license in the list.
ms.assetid: cb5a31a8-ee25-44d6-81ca-746c379cb99e
keywords:
- ResetEnumeration method windows Media Format
- ResetEnumeration method windows Media Format , IWMDRMLicense interface
- IWMDRMLicense interface windows Media Format , ResetEnumeration method
topic_type:
- apiref
api_name:
- IWMDRMLicense.ResetEnumeration
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMLicense::ResetEnumeration method

The **ResetEnumeration** method resets the license list to its original state. The active license becomes the first license in the list.

## Syntax


```C++
HRESULT ResetEnumeration();
```



## Parameters

This method has no parameters.

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
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wmdrmsdk.h</dt> </dl>   |
| Library<br/> | <dl> <dt>Wmdrmsdk.lib</dt> </dl> |



## See also

<dl> <dt>

[**IWMDRMLicense Interface**](iwmdrmlicense.md)
</dt> </dl>

 

 





