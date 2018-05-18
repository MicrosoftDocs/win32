---
Description: 'The Add method of the SWbemNamedValueSet object adds an SWbemNamedValue object to the collection. If an element already exists in the collection with the same name, the new element replaces it.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '471b23f5-6c53-40e2-a2a9-0798044c9dfb'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'SWbemNamedValueSet.Add method'
---

# SWbemNamedValueSet.Add method

The **Add** method of the [**SWbemNamedValueSet**](swbemnamedvalueset.md) object adds an [**SWbemNamedValue**](swbemnamedvalue.md) object to the collection. If an element already exists in the collection with the same name, the new element replaces it.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
objNamedValue = .Add( _
  ByVal strName, _
  ByVal varVal, _
  [ ByVal iFlags ] _
)
```



## Parameters

<dl> <dt>

*strName* \[in\]
</dt> <dd>

Required. Name of the new value.

</dd> <dt>

*varVal* \[in\]
</dt> <dd>

Required. Variant that represents the new value.

</dd> <dt>

*iFlags* \[in, optional\]
</dt> <dd>

Reserved and must be set to zero if specified.

</dd> </dl>

## Return value

If successful, this method returns the newly modified or newly created [**SWbemNamedValue**](swbemnamedvalue.md) object.

## Remarks

For examples of adding and retrieving named values, see [**SWbemNamedValue.Value**](swbemnamedvalue-value.md).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemNamedValueSet<br/>                                                    |
| IID<br/>                      | IID\_ISWbemNamedValueSet<br/>                                                     |



## See also

<dl> <dt>

[**SWbemNamedValueSet**](swbemnamedvalueset.md)
</dt> </dl>

 

 




