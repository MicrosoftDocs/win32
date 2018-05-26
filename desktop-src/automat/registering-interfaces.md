---
title: Registering Interfaces
description: Applications that add interfaces need to register the interfaces so OLE can find the appropriate remoting code for interprocess communication.
ms.assetid: d7f96d58-3124-438d-9e3d-b52737d307cc
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Registering Interfaces

Applications that add interfaces need to register the interfaces so OLE can find the appropriate remoting code for interprocess communication. By default, Automation registers dispinterfaces that appear in the .odl file. It also registers remote Automation-compatible interfaces that are not registered elsewhere in the system registry under the label "ProxyStubClsid32" (or "ProxyStubClsid" on 16-bit systems).

The syntax of the information registered for an interface is as follows:


```C++
\Interface\{UUID} = InterfaceName
\Interface\{UUID}\Typelib = LIBID
\Interface\{UUID}\ProxyStubClsid[32] = CLSID
```



## Parameters

<dl> <dt>

<span id="UUID"></span><span id="uuid"></span>*UUID*
</dt> <dd>

The universally unique ID of the interface.

</dd> <dt>

<span id="InterfaceName"></span><span id="interfacename"></span><span id="INTERFACENAME"></span>*InterfaceName*
</dt> <dd>

The name of the interface.

</dd> <dt>

<span id="LIBID"></span><span id="libid"></span>*LIBID*
</dt> <dd>

The universally unique ID associated with the type library in which the interface is described.

</dd> <dt>

<span id="CLSID"></span><span id="clsid"></span>*CLSID*
</dt> <dd>

The universally unique ID associated with the proxy/stub implementation of the interface, used internally by OLE for interprocess communication. ActiveX objects use the proxy/stub implementation of [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master).

</dd> </dl>

> [!Note]  
> To obtain a universally unique identifier ID, use the Guidgen.exe utility, which is a random number generator for creating unique identifiers. For more information about this utility, refer to [Managing GUIDs](managing-guids-for-automation.md).

 

 

 




