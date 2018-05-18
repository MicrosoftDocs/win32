---
title: Solution ReadLogFile method
description: Read a log file.
ms.assetid: 'e2146b74-9914-436b-a339-8778e162bedc'
keywords: ["ReadLogFile method Access Execution Engine", "ReadLogFile method Access Execution Engine , Solution interface", "Solution interface Access Execution Engine , ReadLogFile method"]
topic_type:
- apiref
api_name:
- Solution.ReadLogFile
api_location:
- AxeCore.dll
api_type:
- COM
---

# Solution::ReadLogFile method

Read a log file.

## Syntax


```C++
virtual HRESULT ReadLogFile(
  [in] LPCWSTR            logPath,
  [in] ILogReaderCallback *callback
) = 0;
```



## Parameters

<dl> <dt>

*logPath* \[in\]
</dt> <dd>

A path to the log file.

</dd> <dt>

*callback* \[in\]
</dt> <dd>

A pointer to an **ILogReaderCallback** interface.

</dd> </dl>

## Return value

If AXE can read the session log file successfully, this method returns **S\_OK**.

If an internal log processing object could not be created due to available memory limitations, this method returns **E\_OUTOFMEMORY**.

## Remarks

Managed code uses the [**Solution.ReadLogFile \| readLogFile**](axe-solution_readlogfile_om) method.

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
</dt> </dl>

 

 





