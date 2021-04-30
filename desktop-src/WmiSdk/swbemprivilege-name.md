---
description: The Name property of an SWbemPrivilege object is a string that uniquely describes a privilege.
ms.assetid: cc1cdde7-20ad-4ff7-ad49-43eb46c15df9
ms.tgt_platform: multiple
title: SWbemPrivilege.Name property (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemPrivilege.Name
- ISWbemPrivilege.Name
- ISWbemPrivilege.get_Name
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemPrivilege.Name property

The **Name** property of an [**SWbemPrivilege**](swbemprivilege.md) object is a string that uniquely describes a privilege. For example, the privilege that controls whether a user can execute the shutdown method of an object has the "SeShutdownPrivilege" string in the **SWbemPrivilege.Name** property. This property is read-only.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

This property is read-only.

## Syntax


```VB
SWbemPrivilege.Name As 
```



## Property value

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemPrivilege<br/>                                                        |
| IID<br/>                      | IID\_ISWbemPrivilege<br/>                                                         |



 

 




