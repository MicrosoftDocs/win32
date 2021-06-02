---
description: The Security\_ property of the SWbemLocator object is used to read or set the security settings for an SWbemLocator object. This property is an SWbemSecurity object.
ms.assetid: 75987bef-21ae-4420-b069-afab90499218
ms.tgt_platform: multiple
title: SWbemLocator.Security_ property (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemLocator.Security_
- ISWbemLocator.Security_
- ISWbemLocator.get_Security_
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemLocator.Security\_ property

The **Security\_** property of the [**SWbemLocator**](swbemlocator.md) object is used to read or set the security settings for an **SWbemLocator** object. This property is an [**SWbemSecurity**](swbemsecurity.md) object.

> [!Note]  
> Setting the **Security\_** property of an [**SWbemLocator**](swbemlocator.md) object to **NULL** grants unlimited access to everyone at all times. For more information, see [**SWbemSecurity**](swbemsecurity.md).

 

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

This property is read-only.

## Syntax


```VB
SWbemLocator.Security_ As Object
```



## Property value

## Remarks

The properties of an **SWbemLocator.Security\_** object have no default values. If you attempt to get the value of [**SWbemSecurity.AuthenticationLevel**](swbemsecurity-authenticationlevel.md) or [**SWbemSecurity.ImpersonationLevel**](swbemsecurity-impersonationlevel.md) on an [**SWbemLocator**](swbemlocator.md) object before you have set it, an [wbemErrFailed](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemerrorenum) error results.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemLocator<br/>                                                          |
| IID<br/>                      | IID\_ISWbemLocator<br/>                                                           |



## See also

<dl> <dt>

[**SWbemLocator**](swbemlocator.md)
</dt> <dt>

[Creating a WMI Application or Script](creating-a-wmi-application-or-script.md)
</dt> <dt>

[Executing Privileged Operations Using VBScript](executing-privileged-operations-using-vbscript.md)
</dt> <dt>

[Setting Client\_Application\_Process Security](setting-client-application-process-security.md)
</dt> <dt>

[**SWbemSecurity object**](swbemsecurity.md)
</dt> <dt>

[Securing a Remote WMI Connection](securing-a-remote-wmi-connection.md)
</dt> </dl>

 

 




