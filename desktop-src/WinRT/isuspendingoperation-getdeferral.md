---
description: Requests that the app suspending operation be delayed.
ms.assetid: 5AB84652-165D-4173-A047-541B05848871
title: ISuspendingOperation::GetDeferral method (Windows.ApplicationModel.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISuspendingOperation.GetDeferral
api_type: 
- COM
api_location: 
- Windows.ApplicationModel.h
---

# ISuspendingOperation::GetDeferral method

Requests that the app suspending operation be delayed.

## Syntax


```C++
HRESULT GetDeferral(
  [out, retval] ISuspendingDeferral **deferral
);
```



## Parameters

<dl> <dt>

*deferral* \[out, retval\]
</dt> <dd>

The deferral suspension.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                          |
| Header<br/>                   | <dl> <dt>Windows.ApplicationModel.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Windows.ApplicationModel.idl</dt> </dl> |



## See also

<dl> <dt>

[**ISuspendingOperation**](isuspendingoperation.md)
</dt> </dl>

 

 




