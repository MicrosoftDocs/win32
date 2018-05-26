---
Description: The Origin property of the SWbemMethod object returns the name of the class in which this method was introduced.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: da98393b-af95-47ad-b589-663063f65afb
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: SWbemMethod.Origin property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SWbemMethod.Origin property

The **Origin** property of the [**SWbemMethod**](swbemmethod.md) object returns the name of the class in which this method was introduced. For classes with deep inheritance hierarchies, it is often desirable to know which methods were declared in which classes. This property is read-only.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

This property is read-only.

## Syntax


```VB
SWbemMethod.Origin As String
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
| CLSID<br/>                    | CLSID\_SWbemMethod<br/>                                                           |
| IID<br/>                      | IID\_ISWbemMethod<br/>                                                            |



 

 




