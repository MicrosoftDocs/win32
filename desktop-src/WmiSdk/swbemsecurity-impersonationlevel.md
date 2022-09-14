---
description: The ImpersonationLevel property is an integer that defines the COM impersonation level that is assigned to this object.
ms.assetid: cf57620b-7827-4552-a969-d25e5eb13a89
ms.tgt_platform: multiple
title: SWbemSecurity.ImpersonationLevel property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemSecurity.ImpersonationLevel
- ISWbemSecurity.ImpersonationLevel
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemSecurity.ImpersonationLevel property

The **ImpersonationLevel** property is an integer that defines the COM impersonation level that is assigned to this object. This setting determines if processes owned by Windows Management Instrumentation (WMI) can detect or use your security credentials when making calls to other processes. For more information about impersonation levels, see [Setting Client\_Application\_Process Security](setting-client-application-process-security.md).

If you do not set the impersonation level specifically in either a moniker, or by setting the **SWBemSecurity.ImpersonationLevel** property on a securable object, WMI sets the default impersonation level to the value specified in the [default impersonation level registry key](setting-the-default-process-security-level-using-vbscript.md). If this setting is not sufficient, the provider does not service your request, and the call to the WMI API can fail with an error code of **wbemErrAccessDenied** (2147749891/0x80041003).

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

This property is read/write.

## Syntax


```VB
SWbemSecurity.ImpersonationLevel As Integer
```



## Property value

## Remarks

As a DCOM impersonation level, this property can be set to one of the following values:



| Value           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Anonymous**   | Hides the credentials of the caller. WMI does not actually support this impersonation level; if a script specifies impersonationLevel=Anonymous, WMI will silently upgrade the impersonation level to Identify. This is in some ways a meaningless exercise, however, because scripts using the Identify level are likely to fail.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Identify**    | Enables objects to query the credentials of the caller. Scripts using this impersonation level are likely to fail; the Identify level typically lets you do no more than check access control lists. You will not be able to run scripts against remote computers using Identify.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Impersonate** | Enables objects to use the credentials of the caller. It is recommended that you use this impersonation level with WMI scripts. When you do so, the WMI script will use your user credentials; as a result, it will be able to perform any tasks that you are able to perform.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Delegate**    | Enables objects to permit other objects to use the credentials of the caller. Delegation allows a script to use your credentials on a remote computer and then enables that remote computer to use your credentials on another remote computer. While you can use this impersonation level within WMI scripts, you should do so only if necessary because it might pose a security risk.<br/> You cannot use the Delegate impersonation level unless all the user accounts and computer accounts involved in the transaction have all been marked as Trusted for delegation in Active Directory. This helps minimize the security risks. Although a remote computer can use your credentials, it can do so only if both it and any other computers involved in the transaction are trusted for delegation.<br/> |



 

As noted, Anonymous impersonation hides your credentials and Identify permits a remote object to query your credentials, but the remote object cannot impersonate your security context. (In other words, although the remote object knows who you are, it cannot "pretend" to be you.) WMI scripts accessing remote computers using one of these two settings will generally fail. In fact, most scripts run on the local computer using one of these two settings will also fail.

Impersonate permits the remote WMI service to use your security context to perform the requested operation. A remote WMI request that uses the Impersonate setting typically succeeds, provided your credentials have sufficient privileges to perform the intended operation. In other words, you cannot use WMI to perform an action (remotely or otherwise) that you do not have permission to perform outside WMI.

Setting impersonationLevel to Delegate permits the remote WMI service to pass your credentials on to other objects and is generally considered a security risk.

You can set the impersonation level of an [**SWbemServices**](swbemservices.md), [**SWbemObject**](swbemobject.md), [**SWbemObjectSet**](swbemobjectset.md), [**SWbemObjectPath**](swbemobjectpath.md), and [**SwbemLocator**](swbemlocator.md) object by setting the **ImpersonationLevel** property to the desired value. The following example shows you how to set the impersonation level for an **SWbemObject** object:


```VB
objinstance.Security_.ImpersonationLevel = _
    wbemImpersonationLevelImpersonate
```



You can also specify impersonation levels as part of a moniker. The following example sets the authentication level and the impersonation level, and retrieves an instance of [**Win32\_Service**](/windows/desktop/CIMWin32Prov/win32-service).


```VB
Set objinst = GetObject("WinMgmts:{impersonationLevel=impersonate,"& _
                         "authenticationLevel=pktPrivacy}"& _
                         "!root/cimv2:Win32_service='ALERTER'")
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemSecurity<br/>                                                         |
| IID<br/>                      | IID\_ISWbemSecurity<br/>                                                          |



## See also

<dl> <dt>

[**SWbemSecurity**](swbemsecurity.md)
</dt> <dt>

[Setting Client\_Application\_Process Security](setting-client-application-process-security.md)
</dt> <dt>

[**WbemImpersonationLevelEnum**](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemimpersonationlevelenum)
</dt> </dl>

 

