---
title: Assessment GetFilePath method
description: Returns the file path for the assessment.
ms.assetid: '054DDBFB-EE95-4973-949D-D1107D2700C2'
keywords: ["GetFilePath method Access Execution Engine", "GetFilePath method Access Execution Engine , Assessment interface", "Assessment interface Access Execution Engine , GetFilePath method"]
topic_type:
- apiref
api_name:
- Assessment.GetFilePath
api_location:
- AxeCore.dll
api_type:
- COM
---

# Assessment::GetFilePath method

Returns the file path for the assessment.

## Syntax


```C++
virtual HRESULT GetFilePath(
  [out, optional] LPCWSTR *assessmentPath
) const = 0;
```



## Parameters

<dl> <dt>

*assessmentPath* \[out, optional\]
</dt> <dd>

The file path.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Assessment**](assessment-inf.md)
</dt> </dl>

 

 





