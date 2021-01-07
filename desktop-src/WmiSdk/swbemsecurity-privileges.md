---
description: The Privileges property is an SWbemPrivilegeSet object. This property is used to enable or disable specific Windows privileges. You may need to set one of these privileges to perform specific tasks using the Windows Management Instrumentation (WMI) API.
ms.assetid: 6e4cae22-23d6-4981-b38c-d298654e59ab
ms.tgt_platform: multiple
title: SWbemSecurity.Privileges property (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemSecurity.Privileges
- ISWbemSecurity.Privileges
- ISWbemSecurity.get_Privileges
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemSecurity.Privileges property

The **Privileges** property is an [**SWbemPrivilegeSet**](swbemprivilegeset.md) object. This property is used to enable or disable specific Windows privileges. You may need to set one of these privileges to perform specific tasks using the Windows Management Instrumentation (WMI) API.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

This property is read-only.

## Syntax


```VB
SWbemSecurity.Privileges As Object
```



## Property value

## Remarks

This setting allows you to grant or revoke privileges as part of a WMI moniker string. For the complete list of applicable values, see [**WbemPrivilegeEnum**](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemprivilegeenum) and [**Privilege Constants**](privilege-constants.md).

You can change the privileges defined for the [**SWbemServices**](swbemservices.md), [**SWbemObject**](swbemobject.md), [**SWbemObjectSet**](swbemobjectset.md), [**SWbemObjectPath**](swbemobjectpath.md), and [**SwbemLocator**](swbemlocator.md) objects by adding [**SWbemPrivilege**](swbemprivilege.md) objects to the **Privileges** property.

There are fundamental differences in how different versions of Windows handle changes to privileges. If you are developing an application that is only used on Windows platforms, you can set or revoke privileges at any time.

The following example sets the **SeDebugPrivilege** on the initial moniker connection to obtain an [**SWbemServices**](swbemservices.md) object.


```VB
Set Service = GetObject( _
    "winmgmts:{impersonationLevel=impersonate, (Debug)}")
```



For more information about how to format the security string for a moniker connection, see [**Privilege Constants**](privilege-constants.md).

The following example performs the same task, but it sets the privilege after the initial log on to WMI.


```VB
Set Service = GetObject( _
    "winmgmts:{impersonationLevel=impersonate}")
Service.Security_.Privileges.AddAsString "SeDebugPrivilege", True
```



Note that for calls to [**SwbemPrivilegeSet.AddAsString**](swbemprivilegeset-addasstring.md), you must use the full name of the security privilege, for example, "SeDebugPrivilege" instead of "Debug".

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemSecurity<br/>                                                         |
| IID<br/>                      | IID\_ISWbemSecurity<br/>                                                          |



## See also

<dl> <dt>

[**SWbemSecurity**](swbemsecurity.md)
</dt> <dt>

[Executing Privileged Operations](executing-privileged-operations.md)
</dt> <dt>

[**SWbemPrivilegeSet**](swbemprivilegeset.md)
</dt> </dl>

 

 




