---
title: Registering Node Type
description: It is important to register the node type of the Active Directory Users and Computers snap-in.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'fcbd5a9b-90f9-4f8e-940a-90700f33f69e'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
---

# Registering Node Type

It is important to register the node type of the Active Directory Users and Computers snap-in. Be aware that the Active Directory Manager does not register all the possible node types that it can display because the schema for the Active Directory Manager is extensible.

For Active Directory Manager, the GUID for the node type is the GUID stored in the schemaIDGUID property of the classSchema object that represents the type of object that you want to extend. For example, to add a context menu item to the context menu of user objects in Active Directory Users and Computers, you would use the COM string representation of the GUID stored in the schemaIDGUID property of the user classSchema object as the node type GUID.

If the node type you want to extend is not registered, you must add the appropriate node type keys to the registry. The following keys must exist for the node type.


```C++
HKEY_LOCAL_MACHINE\Software\Microsoft\MMC\NodeTypes\{nodetype}
 
HKEY_LOCAL_MACHINE\Software\Microsoft\MMC\SnapIns\{snapinCLSID}\NodeTypes\{nodetype}
```



> \[!Important\]
>
> These keys are protected system resources. They are owned by the NT SERVICE\\TrustedInstaller group. You must acquire ownership before you can extend them. It is important that you restore ownership to TrustedInstaller after making your changes.

 

For Active Directory Manager, the {nodetype} key is the schemaIDGUID of the object class whose node you want to extend. The {snapinCLSID} key is the CLSID of the Active Directory Users and Computers snap-in, which is {E355E538-1C2E-11D0-8C37-00C04FD8FE93}.

For example, the following registry entries must exist for a context menu extension snap-in (with CLSID of {6707A300-264F-4BA3-9537-70E304EED9BA}) to extend the user objects.


```C++
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\MMC\NodeTypes\
    {BF967ABA-0DE6-11D0-A285-00AA003049E2}\
        Extensions\
            ContextMenu
                {6707A300-264F-4BA3-9537-70E304EED9BA} = 
                REG_SZ "ATL-based DSAdmin Extension Snap-in Sample"
 
HKEY_LOCAL_MACHINE\Software\Microsoft\MMC\SnapIns\
    {E355E538-1C2E-11D0-8C37-00C04FD8FE93}\
        NodeTypes\
            {BF967ABA-0DE6-11D0-A285-00AA003049E2}
```



 

 




