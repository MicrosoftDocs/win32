---
description: Notifies the system that the app has saved its data and is ready to be suspended.
ms.assetid: 5C79AFBA-34E6-4C0B-95A0-731E10D8A17A
title: ISuspendingDeferral::Complete method (Windows.ApplicationModel.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISuspendingDeferral.Complete
api_type: 
- COM
api_location: 
- Windows.ApplicationModel.h
---

# ISuspendingDeferral::Complete method

Notifies the system that the app has saved its data and is ready to be suspended.

## Syntax


```C++
HRESULT Complete();
```



## Parameters

This method has no parameters.

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

[**ISuspendingDeferral**](isuspendingdeferral.md)
</dt> </dl>

 

 




