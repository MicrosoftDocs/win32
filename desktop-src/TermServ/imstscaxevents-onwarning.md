---
title: IMsTscAxEvents OnWarning method
description: Called when the client control encounters an error condition that is not fatal.
ms.assetid: af43d3aa-0ae8-4721-b85d-bb043b20dc40
ms.tgt_platform: multiple
keywords:
- OnWarning method Remote Desktop Services
- OnWarning method Remote Desktop Services , IMsTscAxEvents interface
- IMsTscAxEvents interface Remote Desktop Services , OnWarning method
topic_type:
- apiref
api_name:
- IMsTscAxEvents.OnWarning
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAxEvents::OnWarning method

Called when the client control encounters an error condition that is not fatal.

## Syntax


```C++
void OnWarning(
  [in] long warningCode
);
```



## Parameters

<dl> <dt>

*warningCode* \[in\]
</dt> <dd>

The error code.

<dt>

<span id="1"></span>

<span id="1"></span>**1**


</dt> <dd>

Bitmap cache is corrupt.

</dd> </dl> </dd> </dl>

## Return value

This method does not return a value.

## Remarks

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

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

 

 





