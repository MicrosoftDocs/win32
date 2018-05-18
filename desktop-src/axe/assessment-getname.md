---
title: Assessment GetName method
description: Retrieve the localized name of the assessment.
ms.assetid: '5500A3D5-0ADD-421C-B0EF-210A7EA9C0E0'
keywords: ["GetName method Access Execution Engine", "GetName method Access Execution Engine , Assessment interface", "Assessment interface Access Execution Engine , GetName method"]
topic_type:
- apiref
api_name:
- Assessment.GetName
api_location:
- AxeCore.dll
api_type:
- COM
---

# Assessment::GetName method

Retrieve the localized name of the assessment.

## Syntax


```C++
virtual HRESULT GetName(
  [out, optional] LPCWSTR *assessmentName
) const = 0;
```



## Parameters

<dl> <dt>

*assessmentName* \[out, optional\]
</dt> <dd>

The name of the assessment.

</dd> </dl>

## Return value

If the assessment name is successfully retrieved, the method returns **S\_OK**.

If the *assessmentName* parameter is **NULL**, the method returns **E\_POINTER**.

## Remarks

Managed code uses [**Assessment.Name \| name property**](axe-assessment_name_om).

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

 

 





