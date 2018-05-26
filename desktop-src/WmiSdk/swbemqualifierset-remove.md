---
Description: The Remove method of the SWbemQualifierSet object deletes a named qualifier from the collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7d386858-efd1-42e6-9176-9cb4bcfc77d0
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: SWbemQualifierSet.Remove method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SWbemQualifierSet.Remove method

The **Remove** method of the [**SWbemQualifierSet**](swbemqualifierset.md) object deletes a named qualifier from the collection.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
SWbemQualifierSet.Remove( _
  ByVal strName, _
  [ ByVal iFlags ] _
)
```



## Parameters

<dl> <dt>

*strName* \[in\]
</dt> <dd>

Required. Name of the qualifier to remove.

</dd> <dt>

*iFlags* \[in, optional\]
</dt> <dd>

Reserved. The default value is 0.

</dd> </dl>

## Return value

This method does not return a value.

## Error codes

After completion of the **Remove** method, the **Err** object may contain one of the error codes in the following list.

<dl> <dt>

**wbemErrInvalidParameter** - 2147749896 (0x80041008)
</dt> <dd>

The *iFlags* parameter was not valid.

</dd> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

Unspecified error.

</dd> <dt>

**wbemErrNotFound** - 2147749890 (0x80041002)
</dt> <dd>

Specified qualifier does not exist.

</dd> <dt>

**wbemErrInvalidOperation** - 2147749910 (0x80041016)
</dt> <dd>

Removing this qualifier is illegal.

</dd> </dl>

## Remarks

You cannot iterate a collection while removing items because when you remove an element from a collection, the collection pointer is moved to the next element. For more information, see [Accessing a Collection](accessing-a-collection.md).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemQualifierSet<br/>                                                     |
| IID<br/>                      | IID\_ISWbemQualifierSet<br/>                                                      |



## See also

<dl> <dt>

[**SWbemQualifierSet**](swbemqualifierset.md)
</dt> <dt>

[**SWbemQualifierSet.Add**](swbemqualifierset-add.md)
</dt> </dl>

 

 




