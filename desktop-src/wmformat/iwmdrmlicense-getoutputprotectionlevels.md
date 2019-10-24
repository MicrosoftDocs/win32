---
title: IWMDRMLicense GetOutputProtectionLevels method
description: The GetOutputProtectionLevels method retrieves information about all output protection levels (OPLs) assigned to the license.
ms.assetid: 6596171a-67ac-42cd-80d9-f77507fc58eb
keywords:
- GetOutputProtectionLevels method windows Media Format
- GetOutputProtectionLevels method windows Media Format , IWMDRMLicense interface
- IWMDRMLicense interface windows Media Format , GetOutputProtectionLevels method
topic_type:
- apiref
api_name:
- IWMDRMLicense.GetOutputProtectionLevels
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IWMDRMLicense::GetOutputProtectionLevels method

The **GetOutputProtectionLevels** method retrieves information about all output protection levels (OPLs) assigned to the license.

## Syntax


```C++
HRESULT GetOutputProtectionLevels(
  [out] WMDRM_OUTPUT_PROTECTION_LEVELS *pOPLs
);
```



## Parameters

<dl> <dt>

*pOPLs* \[out\]
</dt> <dd>

Pointer to a [**WMDRM\_OUTPUT\_PROTECTION\_LEVELS**](wmdrm-output-protection-levels.md) structure that receives the OPL information.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

None.

## See also

<dl> <dt>

[**IWMDRMLicense Interface**](iwmdrmlicense.md)
</dt> </dl>

 

 





