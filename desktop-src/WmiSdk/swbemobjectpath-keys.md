---
Description: The Keys property of the SWbemObjectPath object is an SWbemNamedValueSet object that contains the key value bindings. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1919403d-6dea-4d41-9bc7-a622a9c9c2c8
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: SWbemObjectPath.Keys property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SWbemObjectPath.Keys property

The **Keys** property of the [**SWbemObjectPath**](swbemobjectpath.md) object is an [**SWbemNamedValueSet**](swbemnamedvalueset.md) object that contains the key value bindings. This property is read-only.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

This property is read-only.

## Syntax


```VB
SWbemObjectPath.Keys As Object
```



## Property value

## Error codes

After you retrieve the **Keys** property, the **Err** object may contain the error code below.

<dl> <dt>

**wbemErrNotSupported** - 2147749900 (0x8004100C)
</dt> <dd>

The feature or operation is not supported. This error is returned if a script attempts to write to this property.

</dd> </dl>

## Requirements



|                                     |                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                                   |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                             |
| Header<br/>                   | <dl> <dt>Adoctint.h (include Wbemdisp.h)</dt> </dl> |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl>                    |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl>                    |
| CLSID<br/>                    | CLSID\_SWbemObjectPath<br/>                                                                          |
| IID<br/>                      | IID\_ISWbemObjectPath<br/>                                                                           |



 

 




