---
description: Extends the functionality of SWbemServices.
ms.assetid: def514a9-eca4-41de-87cd-c9f964a71f68
ms.tgt_platform: multiple
title: SWbemServicesEx object (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemServicesEx
- ISWbemServicesEx
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemServicesEx object

The **SWbemServicesEx** object extends the functionality of [**SWbemServices**](swbemservices.md). The [**Put**](swbemservicesex-put.md) and [**PutAsync**](swbemservicesex-putasync.md) methods allow a class or an instance to be saved to multiple namespaces or to a different namespace than the one where an instance was created. This object cannot be created by the VBScript [CreateObject](/previous-versions//xzysf6hc(v=vs.85)) call.

## Members

The **SWbemServicesEx** object has these types of members:

-   [Methods](#methods)

### Methods

The **SWbemServicesEx** object has these methods.



| Method                                       | Description                                                                                                                                                                                                               |
|:---------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Put**](swbemservicesex-put.md)           | Saves the object to the namespace bound to the **SWbemServicesEx** object and returns an [**SWbemObjectPath**](swbemobjectpath.md) object that contains the path of the object to which the data was written.<br/> |
| [**PutAsync**](swbemservicesex-putasync.md) | Saves an object asynchronously to a namespace.<br/>                                                                                                                                                                 |



 

## Remarks

The methods in this class can be called in either the semisynchronous mode or the asynchronous mode. For more information, see [Calling a Method](calling-a-method.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_ISWbemServicesEx<br/>                                                      |
| IID<br/>                      | IID\_ISWbemServicesEx<br/>                                                        |



## See also

<dl> <dt>

[Scripting API Objects](scripting-api-objects.md)
</dt> <dt>

[Calling a Method](calling-a-method.md)
</dt> </dl>

 

