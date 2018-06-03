---
title: Solution GetErrorText method
description: Retrieve the text for a specified error code.
ms.assetid: 714faf39-27ea-4688-ab7d-2259792c2217
keywords:
- GetErrorText method Access Execution Engine
- GetErrorText method Access Execution Engine , Solution interface
- Solution interface Access Execution Engine , GetErrorText method
topic_type:
- apiref
api_name:
- Solution.GetErrorText
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

# Solution::GetErrorText method

Retrieve the text for a specified error code.

## Syntax


```C++
virtual HRESULT GetErrorText(
  [in]  HRESULT   axeError,
  [out] ErrorList **errorList
) = 0;
```



## Parameters

<dl> <dt>

*axeError* \[in\]
</dt> <dd>

An **HRESULT** that was returned by an Axe API.

</dd> <dt>

*errorList* \[out\]
</dt> <dd>

An error list that contains a single [**AxeErrorInfo**](axeerrorinfo.md) object with all of the information about the requested error.

</dd> </dl>

## Return value

If AXE retrieves the text successfully, this method returns **S\_OK**.

If no string can be found for the specified error, this method returns **E\_FAIL**.

If an [**ErrorList**](errorlist.md) or [**AxeErrorInfo**](axeerrorinfo.md) object could not be created due to available memory limitations, this method returns **E\_OUTOFMEMORY**.

## Remarks

A solution application can use this API to convert an error code reported by the AXE engine into a human-readable error text to display to the user. The information about the error is returned in an [**AxeErrorInfo**](axeerrorinfo.md) object that is contained within an [**ErrorList**](errorlist.md).

Managed code uses the [**Solution.GetErrorText \| getErrorText**](https://www.bing.com/search?q=**Solution.GetErrorText \| getErrorText**) method

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Solution**](solution-inf.md)
</dt> </dl>

 

 





