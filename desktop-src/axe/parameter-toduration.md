---
title: Parameter ToDuration method
description: Retrieve the value of the parameter as a specific data type.
ms.assetid: 268CC612-80E1-499B-81CD-3C49EE2B0EC7
keywords:
- ToDuration method Access Execution Engine
- ToDuration method Access Execution Engine , Parameter interface
- Parameter interface Access Execution Engine , ToDuration method
topic_type:
- apiref
api_name:
- Parameter.ToDuration
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

# Parameter::ToDuration method

Retrieve the value of the parameter as a specific data type.

## Syntax


```C++
virtual HRESULT ToDuration(
  [out] LONGLONG *paramValue
) const = 0;
```



## Parameters

<dl> <dt>

*paramValue* \[out\]
</dt> <dd>

The retrieved value of the parameter. Provides a 64-bit value representing the number of 100 nanosecond intervals.

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**.

If the parameter could not be converted into the requested data type, the return value is **AXE\_E\_PARAM\_CONVERSION\_FAILED**.

## Remarks

This method returns a type safe value of a parameter. The method checks the underlying data type of the parameter and if the type is not the same as the one requested, or if there is not a mapping, the method returns an error that the conversion failed.

If this returns any error, all the bits of the output value are set to zero or to the empty string, and the value of **paramValue** is set to false. A non-zero value has a Boolean value of true and a value of zero has a Boolean value of false.

Managed code uses the [**Parameter.ToDuration**](https://www.bing.com/search?q=**Parameter.ToDuration**) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Parameter**](parameter.md)
</dt> </dl>

 

 





