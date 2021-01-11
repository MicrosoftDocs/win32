---
description: The SetAsSingleton method of the SWbemObjectPath object forces the path to address a singleton WMI instance of a class. A singleton class is a class that can never have more than one instance.
ms.assetid: 7ec53954-2aac-494c-87c7-6a14592d8bd5
ms.tgt_platform: multiple
title: SWbemObjectPath.SetAsSingleton method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemObjectPath.SetAsSingleton
- ISWbemObjectPath.SetAsSingleton
- ISWbemObjectPath.SetAsSingleton
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemObjectPath.SetAsSingleton method

The **SetAsSingleton** method of the [**SWbemObjectPath**](swbemobjectpath.md) object forces the path to address a singleton WMI instance of a class. A singleton class is a class that can never have more than one instance.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md). SWbemObjectPath

## Syntax


```VB
SWbemObjectPath.SetAsSingleton()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Error codes

Upon completion of the **SetAsSingleton** method, the **Err** object may contain the error code below.

<dl> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

Unspecified error.

</dd> </dl>

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



 

 




