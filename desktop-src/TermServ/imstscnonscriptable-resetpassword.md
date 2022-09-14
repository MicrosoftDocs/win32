---
title: IMsTscNonScriptable ResetPassword method
description: Resets all password states in the Remote Desktop ActiveX control.
ms.assetid: 889c4d41-fadf-4a5c-b4a8-0b349fd6db54
ms.tgt_platform: multiple
keywords:
- ResetPassword method Remote Desktop Services
- ResetPassword method Remote Desktop Services , IMsTscNonScriptable interface
- IMsTscNonScriptable interface Remote Desktop Services , ResetPassword method
topic_type:
- apiref
api_name:
- IMsTscNonScriptable.ResetPassword
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscNonScriptable::ResetPassword method

Resets all password states in the Remote Desktop ActiveX control. You can call this method to clear passwords that are stored in any one of the three supported formats: plaintext, portable encoded, or binary (nonportable) encoded. Note that encoded passwords should not be considered securely encrypted.

## Syntax


```C++
HRESULT ResetPassword();
```



## Parameters

This method has no parameters.

## Return value

Return **S\_OK** if successful.

## Remarks

You can call this method to reset the control's password after disconnecting. This ensures that subsequent connections that use the same instance of the control do not automatically log on with a previously set password.

You can only call this method when the Remote Desktop ActiveX control is not in the connected state. This method returns **E\_FAIL** if called when the control is connected. To check for the connected state, call the [**get\_Connected**](imstscax-connected.md) method through the [**IMsTscAx**](imstscax-interface.md) interface or one of the interfaces that inherits from it.

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IID\_IMsTscNonScriptable is defined as c1e6743a-41c1-4a74-832a-0dd06c1c7a0e<br/> |



## See also

<dl> <dt>

[**IMsTscNonScriptable**](imstscnonscriptable-interface.md)
</dt> </dl>

 

 





