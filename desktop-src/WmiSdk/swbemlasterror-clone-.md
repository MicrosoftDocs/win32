---
description: The Clone\_ method of the SWbemLastError object returns a new object that is a clone of the current SWbemLastError object.
ms.assetid: 577be060-309f-40a2-a4db-c0a477c21f11
ms.tgt_platform: multiple
title: SWbemLastError.Clone_ method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemLastError.Clone_
- ISWbemLastError.Clone_
- ISWbemLastError.Clone_
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemLastError.Clone\_ method

The **Clone\_** method of the [**SWbemLastError**](swbemlasterror.md) object returns a new object that is a clone of the current **SWbemLastError** object.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
objWbemObject = .Clone_( _
)
```



## Parameters

This method has no parameters.

## Return value

If the **Clone\_** method is successful, it returns a new [**SWbemLastError**](swbemlasterror.md) object.

## Error codes

Upon the completion of the **Clone\_** method, the **Err** object may contain one of the error codes below.

<dl> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

Unspecified error.

</dd> <dt>

**wbemErrInvalidParameter** - 2147749896 (0x80041008)
</dt> <dd>

A specified parameter is not valid.

</dd> <dt>

**wbemErrOutOfMemory** - 2147749894 (0x80041006)
</dt> <dd>

Not enough memory to complete the operation.

</dd> </dl>

## Remarks

Use the **Clone\_** method to duplicate a class definition or instance. This method is useful when you need to back up the original copy of the object while you modify a new copy. Also, use this method to create many new instances from a single source instance. For example, use [**SWbemObject.SpawnInstance\_**](swbemobject-spawninstance-.md) to create a single starting instance and use **SWbemLastError.Clone\_** to produce 100 copies of the instance quickly. Subsequently, you can modify the objects, giving specific values to each object.

It is not possible to use this method to convert a class definition to an instance or to convert an instance to a class definition.

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



 

 




