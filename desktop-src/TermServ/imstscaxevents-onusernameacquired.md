---
title: IMsTscAxEvents OnUserNameAcquired method
description: Called when the user name has been acquired by the control.
ms.assetid: 0653B28B-2D46-429F-8A36-5656786C0B26
ms.tgt_platform: multiple
keywords:
- OnUserNameAcquired method Remote Desktop Services
- OnUserNameAcquired method Remote Desktop Services , IMsTscAxEvents interface
- IMsTscAxEvents interface Remote Desktop Services , OnUserNameAcquired method
topic_type:
- apiref
api_name:
- IMsTscAxEvents.OnUserNameAcquired
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAxEvents::OnUserNameAcquired method

Called when the user name has been acquired by the control.

## Syntax


```C++
void OnUserNameAcquired(
   BSTR bstrUserName
);
```



## Parameters

<dl> <dt>

*bstrUserName* 
</dt> <dd>

The user name.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IMsTscAxEvents is defined as 336d5562-efa8-482e-8cb3-c5c0fc7a7db6<br/>           |



## See also

<dl> <dt>

[**IMsTscAxEvents**](imstscaxevents-interface.md)
</dt> </dl>

 

 





