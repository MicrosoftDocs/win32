---
description: Frees resources used by the IeAxiService interface.
ms.assetid: 11f5cfdc-dcdd-4b41-b02c-b19b9452509e
title: IeAxiService::Cleanup method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IeAxiService.Cleanup
api_type: 
- COM
api_location: 
---

# IeAxiService::Cleanup method

The **Cleanup** method frees resources used by the [**IeAxiService**](ieaxiservice.md) interface.

## Syntax


```C++
HRESULT Cleanup();
```



## Parameters

This method has no parameters.

## Return value

If the method succeeds, the method returns S\_OK.

If the method fails, it returns an **HRESULT** value that indicates the error. For a list of common error codes, see [Common HRESULT Values](/windows/desktop/SecCrypto/common-hresult-values).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista Business, Windows Vista Enterprise, Windows Vista Ultimate \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                                                                                 |
| IID<br/>                      | IID\_IeAxiService is defined as E9E92380-9ECD-4982-A0EB-6815A56CCF27<br/>                           |



## See also

<dl> <dt>

[**IeAxiService**](ieaxiservice.md)
</dt> </dl>

 

