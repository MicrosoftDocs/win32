---
Description: The DeleteAll method of the SWbemNamedValueSet object removes all named values from the collection, thus emptying it.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: db5d2e68-028e-4902-ad42-0b46e1a96bcb
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: SWbemNamedValueSet.DeleteAll method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SWbemNamedValueSet.DeleteAll method

The **DeleteAll** method of the [**SWbemNamedValueSet**](swbemnamedvalueset.md) object removes all named values from the collection, thus emptying it.

## Syntax


```VB
SWbemNamedValueSet.DeleteAll()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Error codes

Upon completion of the **DeleteAll** method, the **Err** object may contain the error code below.

<dl> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

Unspecified error.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemNamedValueSet<br/>                                                    |
| IID<br/>                      | IID\_ISWbemNamedValueSet<br/>                                                     |



## See also

<dl> <dt>

[**SWbemNamedValueSet**](swbemnamedvalueset.md)
</dt> <dt>

[**SWbemNamedValueSet.Remove**](swbemnamedvalueset-remove.md)
</dt> </dl>

 

 




