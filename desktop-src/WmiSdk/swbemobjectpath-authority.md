---
Description: The Authority property of the SWbemObjectPath object contains a string that defines the Authority component of the object path.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f00e5759-03b4-4333-b89e-5f54db73c3b7
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: SWbemObjectPath.Authority property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SWbemObjectPath.Authority property

The **Authority** property of the [**SWbemObjectPath**](swbemobjectpath.md) object contains a string that defines the Authority component of the object path. For more information, see the *strAuthority* parameter of the [**SWbemLocator.ConnectServer**](swbemlocator-connectserver.md) method and [Setting the Security on IWbemServices and Other Proxies](setting-the-security-on-iwbemservices-and-other-proxies.md).

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

This property is read/write.

## Syntax


```VB
SWbemObjectPath.Authority As String
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
| CLSID<br/>                    | CLSID\_SWbemObjectPath<br/>                                                       |
| IID<br/>                      | IID\_ISWbemObjectPath<br/>                                                        |



 

 




