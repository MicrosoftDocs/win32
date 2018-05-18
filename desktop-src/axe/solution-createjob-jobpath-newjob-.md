---
title: Solution CreateJob method
description: Load a job from an XML file.
ms.assetid: 'E49EAB8D-C328-4BF3-9434-C70F5A4BD6DE'
keywords: ["CreateJob method Access Execution Engine", "CreateJob method Access Execution Engine , Solution interface", "Solution interface Access Execution Engine , CreateJob method"]
topic_type:
- apiref
api_name:
- Solution.CreateJob
api_location:
- AxeCore.dll
api_type:
- COM
---

# Solution::CreateJob method

Load a job from an XML file.

## Syntax


```C++
virtual HRESULT CreateJob(
  [in]  LPCWSTR jobPath,
  [out] Job     **newJob
) = 0;
```



## Parameters

<dl> <dt>

*jobPath* \[in\]
</dt> <dd>

A string containing the path to an XML file that adheres to the job manifest schema.

</dd> <dt>

*newJob* \[out\]
</dt> <dd>

A double pointer to receive a pointer to the newly created [**Job**](job-if.md) object.

</dd> </dl>

## Return value

If AXE parses and validates the job successfully, this method returns **S\_OK**.

If the XML does not adhere to the job manifest or assessment manifest schema, this method returns **AXE\_E\_BAD\_MANIFEST**.

If there is insufficient memory available to create a [**Job**](job-if.md) object, this method returns **E\_OUTOFMEMORY**.

If the job file does not exist, the method returns the **HRESULT** version of **ERROR\_NOT\_FOUND** (0x80070002).

## Remarks

Managed code uses [**Solution.CreateJob \| createJob**](axe-solution_createjob_om) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Solution**](solution-inf.md)
</dt> <dt>

[**Solution::CreateJob methods**](solution-createjob-ovl.md)
</dt> </dl>

 

 





