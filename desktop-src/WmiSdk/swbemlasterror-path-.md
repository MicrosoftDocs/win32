---
description: The Path\_ property of the SWbemLastError object returns an SWbemObjectPath object that represents the object path of the current class or instance. This property can be passed as a parameter to methods that require an object path.
ms.assetid: 5472e463-54cb-4ba2-8c00-08b70013e38d
ms.tgt_platform: multiple
title: SWbemLastError.Path_ property (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemLastError.Path_
- ISWbemLastError.Path_
- ISWbemLastError.get_Path_
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemLastError.Path\_ property

The **Path\_** property of the [**SWbemLastError**](swbemlasterror.md) object returns an [**SWbemObjectPath**](swbemobjectpath.md) object that represents the object path of the current class or instance. This property can be passed as a parameter to methods that require an object path.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

This property is read-only.

## Syntax


```VB
SWbemLastError.Path_ As Object
```



## Property value

## Remarks

Only the [**Class**](swbemobjectpath-class.md) property of the returned [**SWbemObjectPath**](swbemobjectpath.md) instance can be modified. If you try to modify any other property, or try to call the [**SetAsClass**](swbemobjectpath-setasclass.md) or [**SetAsSingleton**](swbemobjectpath-setassingleton.md) methods, you get an error of **wbemErrReadOnly**.

Because of this, you cannot modify the [**SWbemNamedValueSet**](swbemnamedvalueset.md) object that is the value of the [**Keys**](swbemobjectpath-keys.md) property of the returned [**SWbemObjectPath**](swbemobjectpath.md) instance. If you try to call the [**Add**](swbemnamedvalueset-add.md), [**Remove**](swbemnamedvalueset-remove.md), or [**DeleteAll**](swbemnamedvalueset-deleteall.md) methods on this value, you get a **wbemErrReadOnly** error. Furthermore, you cannot modify any [**SWbemNamedValue**](swbemnamedvalue.md) obtained from this collection. Attempts to modify the [**Value**](swbemnamedvalue-value.md) property return the same error code.

However, if you call [**SWbemObject.Clone\_**](swbemobject-clone-.md) to create a copy, the [**Path\_**](swbemobject-path-.md) property of the copy is fully modifiable.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemLastError<br/>                                                        |
| IID<br/>                      | IID\_ISWbemLastError<br/>                                                         |



 

 




