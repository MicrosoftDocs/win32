---
Description: 'The SWbemNamedValue object represents a single named value that belongs to the SWbemNamedValueSet collection object. This object cannot be created by the VBScript CreateObject call.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '3f72afcd-6e10-4200-804d-918e3eb2862f'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: SWbemNamedValue object
---

# SWbemNamedValue object

The **SWbemNamedValue** object represents a single named value that belongs to the [**SWbemNamedValueSet**](swbemnamedvalueset.md) collection object. This object cannot be created by the VBScript [**CreateObject**](creating-an-object-using-vbscript.md) call.

## Members

The **SWbemNamedValue** object has these types of members:

-   [Properties](#properties)

### Properties

The **SWbemNamedValue** object has these properties.



| Property                                          | Access type           | Description                                                                                    |
|:--------------------------------------------------|:----------------------|:-----------------------------------------------------------------------------------------------|
| [**Name**](swbemnamedvalue-name.md)<br/>   | Read-only<br/>  | Name of the **SWbemNamedValue** item.<br/>                                               |
| [**Value**](swbemnamedvalue-value.md)<br/> | Read/write<br/> | Value of the **SWbemNamedValue** item. This is the default property of this object.<br/> |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemNamedValue<br/>                                                       |
| IID<br/>                      | IID\_ISWbemNamedValue<br/>                                                        |



## See also

<dl> <dt>

[Scripting API Objects](scripting-api-objects.md)
</dt> </dl>

 

 




