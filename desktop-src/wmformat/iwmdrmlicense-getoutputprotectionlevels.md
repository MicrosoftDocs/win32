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
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# IWMDRMLicense::GetOutputProtectionLevels method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 





