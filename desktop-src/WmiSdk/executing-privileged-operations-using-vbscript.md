---
description: If you use the scripting API for WMI, you can set specific security privileges.
ms.assetid: 65b923d5-5244-498d-9644-d4978fb84f85
ms.tgt_platform: multiple
title: Executing Privileged Operations Using VBScript
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Executing Privileged Operations Using VBScript

If you use the scripting API for WMI, you can set specific security privileges. For example, you can set the security privileges to request an operating system shutdown, or to examine the security event log. For more information, see [Running with Special Privileges](/windows/desktop/SecBP/running-with-special-privileges).

You only need to set privileges when you are accessing WMI on your computer. When you are accessing a remote host, COM RPC automatically sets the privileges. To determine all the required privileges, consult the documentation for the specific WMI classes that you want to access, such as [**Win32\_OperatingSystem**](/windows/desktop/CIMWin32Prov/win32-operatingsystem). For more information, see [WbemPrivilegeEnum](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemprivilegeenum)

The following sections are discussed in this topic:

-   [Setting a Privilege from the Security\_ Object](/windows)
-   [Setting a Privilege as Part of a Moniker](#setting-a-privilege-as-part-of-a-moniker)
-   [Revoking and Resetting Privileges](#revoking-and-resetting-privileges)
-   [Related topics](#related-topics)

## Setting a Privilege from the Security\_ Object

Use the following procedure to set security privileges in Visual Basic.

**To set privileges in Visual Basic**

1.  Create an object of type [**SWbemLocator**](swbemlocator.md).
2.  Add the new privilege to the [**SWbemLocator.Security\_**](swbemlocator-security-.md) object.

    The [**Security\_**](swbemlocator-security-.md) object contains an [**SWbemObjectSet**](swbemobjectset.md) collection. The objects in the set are [**SWbemSecurity**](swbemsecurity.md) objects. For more information, see [Accessing a Collection](accessing-a-collection.md).

3.  Log on to WMI and retrieve an [**SWbemServices**](swbemservices.md) object.

    The [**SWbemServices**](swbemservices.md) object inherits the privilege that is set in the previous step.

You can also set a privilege using the [**SWbemPrivilegeSet.AddAsString**](swbemprivilegeset-addasstring.md) method.

## Setting a Privilege as Part of a Moniker

You can set a privilege as part of a moniker.

The following example shows you how to add a debug privilege to a moniker.


```VB
Set Service = GetObject("winmgmts:{impersonationLevel=impersonate, (Debug)}")
```



## Revoking and Resetting Privileges

The following example shows you how to set the **SeDebugPrivilege** privilege, and revoke the **SeRemoteShutdownPrivilege** privilege.


```VB
Set Service = GetObject("winmgmts:{impersonate,(Debug,!RemoteShutdown)}")
```



## Related topics

<dl> <dt>

[**Privilege Constants**](privilege-constants.md)
</dt> <dt>

[Executing Privileged Operations](executing-privileged-operations.md)
</dt> </dl>

 

 
