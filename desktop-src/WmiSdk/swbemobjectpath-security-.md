---
description: The Security property of the SWbemObjectPath object is used to get or set the security components of an object path.
ms.assetid: 26e5e990-3b78-41b6-83c4-ba0d8b0d2f00
ms.tgt_platform: multiple
title: SWbemObjectPath.Security_ property (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemObjectPath.Security_
- ISWbemObjectPath.Security_
- ISWbemObjectPath.get_Security_
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemObjectPath.Security\_ property

The **Security** property of the [**SWbemObjectPath**](swbemobjectpath.md) object is used to get or set the security components of an object path. Note that it is not used to set security attributes of the **SWbemObjectPath** object itself. It is used only to represent the security components of the path for an [**SWbemLocator**](swbemlocator.md) object. This property is an [**SWbemSecurity**](swbemsecurity.md) object.

> [!Note]  
> Setting the [**Security\_**](swbemobject-security-.md) property of an [**SWbemObjectPath**](swbemobjectset.md) object to **NULL** grants unlimited access to everyone at all times. For more information, see [**SWbemSecurity**](swbemsecurity.md).

 

For more information, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

This property is read-only.

## Syntax


```VB
SWbemObjectPath.Security_ As Object
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
| CLSID<br/>                    | CLSID\_SWbemObjectPath<br/>                                                       |
| IID<br/>                      | IID\_ISWbemObjectPath<br/>                                                        |



## See also

<dl> <dt>

[**SWbemObjectPath**](swbemobjectpath.md)
</dt> <dt>

[Creating a WMI Application or Script](creating-a-wmi-application-or-script.md)
</dt> <dt>

[Setting Client\_Application\_Process Security](setting-client-application-process-security.md)
</dt> </dl>

 

 




