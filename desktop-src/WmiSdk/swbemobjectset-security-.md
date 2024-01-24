---
description: The Security\_ property of the SWbemObjectSet object is used to get or set the security settings for an SWbemObjectSet object. This property is an SWbemSecurity object.
ms.assetid: ee2ad6d5-c0aa-4510-ba1b-4a152d56011f
ms.tgt_platform: multiple
title: SWbemObjectSet.Security_ property (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemObjectSet.Security_
- ISWbemObjectSet.Security_
- ISWbemObjectSet.get_Security_
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemObjectSet.Security\_ property

The **Security\_** property of the [**SWbemObjectSet**](swbemobjectset.md) object is used to get or set the security settings for an **SWbemObjectSet** object. This property is an [**SWbemSecurity**](swbemsecurity.md) object.

> [!Note]  
> Setting the [**Security\_**](swbemobject-security-.md) property of an [**SWbemObjectSet**](swbemobjectset.md) object to **NULL** grants unlimited access to everyone at all times. For more information about the implications of unlimited access, see [**SWbemSecurity**](swbemsecurity.md).

 

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

This property is read-only.

## Syntax


```VB
SWbemObjectSet.Security_ As Object
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
| CLSID<br/>                    | CLSID\_SWbemObjectSet<br/>                                                        |
| IID<br/>                      | IID\_ISWbemObjectSet<br/>                                                         |



## See also

<dl> <dt>

[**SWbemObjectSet**](swbemobjectset.md)
</dt> <dt>

[Creating a WMI Application or Script](creating-a-wmi-application-or-script.md)
</dt> <dt>

[Securing Scripting Clients](securing-scripting-clients.md)
</dt> </dl>

 

 




