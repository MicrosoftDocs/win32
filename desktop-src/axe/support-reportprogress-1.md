---
title: Support ReportProgress method
description: Reports the progress of the assessment to the AXE engine and can inform the assessment if it should stop running.
ms.assetid: 187A8A09-0870-4D52-B9C5-B76D2B41BFD5
keywords:
- ReportProgress method Access Execution Engine
- ReportProgress method Access Execution Engine , Support interface
- Support interface Access Execution Engine , ReportProgress method
topic_type:
- apiref
api_name:
- Support.ReportProgress
api_location:
- AxeCore.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Support::ReportProgress method

Reports the progress of the assessment to the AXE engine and can inform the assessment if it should stop running.

## Syntax


```C++
virtual HRESULT ReportProgress(
  [in]           AxeProgressType progressType,
  [in]           UINT            progressValue,
  [in, optional] LPCWSTR         progressMessage
) const = 0;
```



## Parameters

<dl> <dt>

*progressType* \[in\]
</dt> <dd>

The type of progress data that is contained within the other parameters.

</dd> <dt>

*progressValue* \[in\]
</dt> <dd>

An integer value that is interpreted according to the *progressType* parameter.

</dd> <dt>

*progressMessage* \[in, optional\]
</dt> <dd>

A string that is interpreted according to the *progressType* parameter.

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**.

If the parameters are invalid with respect to *progressType*, the return value is **E\_INVALIDARG**.

## Remarks

The parameters to this method enable the assessment to report different types of progress to an application. Applications can display the information.

See the definition of the [**ProgressType**](progresstype.md) enumeration for restrictions and error conditions.

Managed code uses the [**Support.ReportProgress**](https://www.bing.com/search?q=**Support.ReportProgress**) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Support**](support.md)
</dt> <dt>

[**ReportProgress methods**](support-reportprogress-overl.md)
</dt> </dl>

 

 





