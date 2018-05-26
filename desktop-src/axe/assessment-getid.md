---
title: Assessment GetId method
description: Returns the ID of the assessment, a GUID.
ms.assetid: 2DA8C60D-C15D-406E-8DDF-59A313C5B333
keywords:
- GetId method Access Execution Engine
- GetId method Access Execution Engine , Assessment interface
- Assessment interface Access Execution Engine , GetId method
topic_type:
- apiref
api_name:
- Assessment.GetId
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

# Assessment::GetId method

Returns the ID of the assessment, a GUID.

## Syntax


```C++
virtual HRESULT GetId(
  [out] const GUID **guidAssessment
) const = 0;
```



## Parameters

<dl> <dt>

*guidAssessment* \[out\]
</dt> <dd>

The ID of the assessment, a GUID.

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

 

 





