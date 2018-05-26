---
Description: The Security\_ property of the SWbemObject object is used to read, or set the security settings for an SWbemObject object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: add77267-d62f-4ee4-a0ff-8ca06a6bf7cd
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: SWbemObject.Security\_ property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SWbemObject.Security\_ property

The **Security\_** property of the [**SWbemObject**](swbemobject.md) object is used to read, or set the security settings for an **SWbemObject** object. This property is an [**SWbemSecurity**](swbemsecurity.md) object. The security settings in this object do not indicate the authentication, impersonation, or privilege settings made on a connection to Windows Management Instrumentation (WMI), or the security in effect for the proxy when an object is delivered to a sink in an asynchronous call. For more information, see [Maintaining WMI Security](maintaining-wmi-security.md).

> [!Note]  
> Setting the **Security\_** property of an [**SWbemObject**](swbemobject.md) object to **NULL** grants unlimited access to everyone all the time. For more information, see [**SWbemSecurity**](swbemsecurity.md).

 

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

This property is read-only.

## Syntax


```VB
SWbemObject.Security_ As Object
```



## Property value

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemObject<br/>                                                           |
| IID<br/>                      | IID\_ISWbemObject<br/>                                                            |



## See also

<dl> <dt>

[**SWbemObject**](swbemobject.md)
</dt> <dt>

[Creating a WMI Application or Script](creating-a-wmi-application-or-script.md)
</dt> <dt>

[Setting Client\_Application\_Process Security](setting-client-application-process-security.md)
</dt> <dt>

[**SWbemSecurity**](swbemsecurity.md)
</dt> <dt>

[**WbemAuthenticationLevelEnum**](/windows/win32/Wbemdisp/ne-wbemdisp-wbemauthenticationlevelenum?branch=master)
</dt> <dt>

[**WbemImpersonationLevelEnum**](/windows/win32/Wbemdisp/ne-wbemdisp-wbemimpersonationlevelenum?branch=master)
</dt> <dt>

[**WbemPrivilegeEnum**](/windows/win32/Wbemdisp/ne-wbemdisp-wbemprivilegeenum?branch=master)
</dt> <dt>

[**Privilege Constants**](privilege-constants.md)
</dt> </dl>

 

 




