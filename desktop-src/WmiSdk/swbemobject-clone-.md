---
description: The Clone\_ method of the SWbemObject object returns a new object that is a clone of the current object.
ms.assetid: d0773c94-30b5-4217-8a9a-0bceb9e75f02
ms.tgt_platform: multiple
title: SWbemObject.Clone_ method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemObject.Clone_
- ISWbemObject.Clone_
- ISWbemObject.Clone_
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemObject.Clone\_ method

The **Clone\_** method of the [**SWbemObject**](swbemobject.md) object returns a new object that is a clone of the current object.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
objWbemObject = .Clone_( _
)
```



## Parameters

This method has no parameters.

## Return value

If successful, this method returns a new [**SWbemObject**](swbemobject.md) object.

## Error codes

After completion of the **Clone\_** method, the **Err** object may contain one of the error codes below.

<dl> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

Unspecified error.

</dd> <dt>

**wbemErrInvalidParameter** - 2147749896 (0x80041008)
</dt> <dd>

**Nothing** was specified as a parameter, and it is not acceptable in this usage.

</dd> <dt>

**wbemErrOutOfMemory** - 2147749894 (0x80041006)
</dt> <dd>

Not enough memory to clone the object.

</dd> </dl>

## Remarks

Use the **Clone\_** method to duplicate a class definition or an instance. This is useful when you need the original copy of the object for backup purposes while you are modifying a new copy. Likewise, use this method to create many new instances from a single source instance. For example, use [**SWbemObject.SpawnInstance\_**](swbemobject-spawninstance-.md) to create a single starting instance, and use **SWbemObject.Clone\_** to produce 100 copies of the instance quickly. Subsequently, you can modify the objects, giving each one specific values.

It is not possible to use this method to convert a class definition to an instance, or to convert an instance to a class definition.

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



 

 




