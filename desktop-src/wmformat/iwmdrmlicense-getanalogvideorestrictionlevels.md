---
title: IWMDRMLicense GetAnalogVideoRestrictionLevels method (Wmdrmsdk.h)
description: The GetAnalogVideoRestrictionLevels method retrieves all analog video restrictions set on the current license.
ms.assetid: cf0ac7c0-236d-4d60-8850-81dc6754cf01
keywords:
- GetAnalogVideoRestrictionLevels method windows Media Format
- GetAnalogVideoRestrictionLevels method windows Media Format , IWMDRMLicense interface
- IWMDRMLicense interface windows Media Format , GetAnalogVideoRestrictionLevels method
topic_type:
- apiref
api_name:
- IWMDRMLicense.GetAnalogVideoRestrictionLevels
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMLicense::GetAnalogVideoRestrictionLevels method

The **GetAnalogVideoRestrictionLevels** method retrieves all analog video restrictions set on the current license.

## Syntax


```C++
HRESULT GetAnalogVideoRestrictionLevels(
  [out]     WMDRM_ANALOG_VIDEO_RESTRICTIONS rgAnalogVideoRestrictions[],
  [in, out] DWORD                           *pcRestrictions
);
```



## Parameters

<dl> <dt>

*rgAnalogVideoRestrictions\[\]* \[out\]
</dt> <dd>

Receives an array of [**WMDRM\_ANALOG\_VIDEO\_RESTRICTIONS**](wmdrm-analog-video-restrictions.md) structures. Set to **NULL** to get the number of elements in the array in *pcResctrictions*.

</dd> <dt>

*pcRestrictions* \[in, out\]
</dt> <dd>

The number of elements in the array of restrictions. If *rgAnalogVideoRestrictions* is set to **NULL**, this value is set to the number of elements needed in the array.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

You must allocate memory for the array of restrictions. To do so, first call the method with *rgAnalogVideoRestrictions* set to **NULL**, which will set the value at *pcRestrictions* to the number of required elements.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wmdrmsdk.h</dt> </dl>   |
| Library<br/> | <dl> <dt>Wmdrmsdk.lib</dt> </dl> |



## See also

<dl> <dt>

[**IWMDRMLicense Interface**](iwmdrmlicense.md)
</dt> </dl>

 

 





