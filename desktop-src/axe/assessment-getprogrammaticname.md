---
title: Assessment GetProgrammaticName method
description: Returns the programmatic name of the assessment.
ms.assetid: 6BA442FA-6BE9-44A6-9921-21474984CB3D
keywords:
- GetProgrammaticName method Access Execution Engine
- GetProgrammaticName method Access Execution Engine , Assessment interface
- Assessment interface Access Execution Engine , GetProgrammaticName method
topic_type:
- apiref
api_name:
- Assessment.GetProgrammaticName
api_location:
- AxeCore.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Assessment::GetProgrammaticName method

Returns the programmatic name of the assessment.

## Syntax


```C++
virtual HRESULT GetProgrammaticName(
  [out, optional] LPCWSTR *assessmentProgrammaticName
) const = 0;
```



## Parameters

<dl> <dt>

*assessmentProgrammaticName* \[out, optional\]
</dt> <dd>

The programmatic name.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Assessment**](assessment-inf.md)
</dt> </dl>

 

 





