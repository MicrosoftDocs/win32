---
description: The Path\_ property of the SWbemObject object returns an SWbemObjectPath object that represents the object path of the current class or instance. This property can be passed as a parameter to methods that require an object path.
ms.assetid: 85a55159-5f10-49b5-bc37-39d7b4dfccd7
ms.tgt_platform: multiple
title: SWbemObject.Path_ property (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemObject.Path_
- ISWbemObject.Path_
- ISWbemObject.get_Path_
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemObject.Path\_ property

The **Path\_** property of the [**SWbemObject**](swbemobject.md) object returns an [**SWbemObjectPath**](swbemobjectpath.md) object that represents the object path of the current class or instance. This property can be passed as a parameter to methods that require an object path.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

This property is read-only.

## Syntax


```VB
SWbemObject.Path_ As Object
```



## Property value

## Remarks

Only the [**Class**](swbemobjectpath-class.md) property of the returned [**SWbemObjectPath**](swbemobjectpath.md) instance can be modified. If you try to modify any other property, or try to call the methods [**SetAsClass**](swbemobjectpath-setasclass.md) or [**SetAsSingleton**](swbemobjectpath-setassingleton.md), you will get a **wbemErrReadOnly** error.

Because of this, you cannot modify the [**SWbemNamedValueSet**](swbemnamedvalueset.md) object that is the value of the [**Keys**](swbemobjectpath-keys.md) property of the returned [**SWbemObjectPath**](swbemobjectpath.md) instance. If you try to call the [**Add**](swbemnamedvalueset-add.md), [**Remove**](swbemnamedvalueset-remove.md), or [**DeleteAll**](swbemnamedvalueset-deleteall.md) methods on this value, you will get a wbemErrReadOnly error. Furthermore, you cannot modify any [**SWbemNamedValue**](swbemnamedvalue.md) obtained from this collection. Attempts to modify the **Value** property return the same error code.

However, if you call [**SWbemObject.Clone\_**](swbemobject-clone-.md) to create a copy, the [**SWbemObjectPath.Path**](swbemobjectpath-path.md) property of the copy is fully modifiable.

## Examples

The following code sample, taken from [List All the WMI cimV2 Classes](https://Gallery.TechNet.Microsoft.Com/5649568b-074e-4f5d-be52-e8b7d8fe4517) in the TechNet Gallery, uses the Path\_ property to list all the WMI cimV2 classes.


```VB
strComputer = "." 
Set objWMIService=GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & _  
    strComputer & "\root\cimv2") 
  
For Each objclass in objWMIService.SubclassesOf() 
    Wscript.Echo objClass.Path_.Class 
Next 
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemObject<br/>                                                           |
| IID<br/>                      | IID\_ISWbemObject<br/>                                                            |



 

 




