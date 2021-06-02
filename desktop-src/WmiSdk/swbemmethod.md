---
description: You can use the properties of the SWbemMethod object to inspect a single method definition of a WMI object. This object cannot be created by the VBScript CreateObject call.
ms.assetid: 461d5c41-4930-40cf-96e2-bc8cae335b60
ms.tgt_platform: multiple
title: SWbemMethod object (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemMethod
- ISWbemMethod
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemMethod object

You can use the properties of the **SWbemMethod** object to inspect a single method definition of a WMI object. This object cannot be created by the VBScript **CreateObject** call.

This object can be used to inspect the definitions of methods. To invoke the methods, you should use either direct access (see [Manipulating Class and Instance Information](manipulating-class-and-instance-information.md)) on an [**SWbemObject**](swbemobject.md) (which is the recommended mechanism) object, or the [**SWbemServices.ExecMethod**](swbemservices-execmethod.md) call.

> [!Note]  
> In this version of the API, write access to method information is not supported. If you want to define methods or modify existing method definitions, you can define the method changes in a MOF file and submit the changes using the [MOF Compiler](compiling-mof-files.md). Alternatively, use the [COM API for WMI](com-api-for-wmi.md).

 

## Members

The **SWbemMethod** object has these types of members:

-   [Properties](#properties)

### Properties

The **SWbemMethod** object has these properties.



| Property                                                      | Access type          | Description                                                                                                                        |
|:--------------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------------------------------------------------------------------|
| [**InParameters**](swbemmethod-inparameters.md)<br/>   | Read-only<br/> | An [**SWbemObject**](swbemobject.md) object whose properties define the input parameters for this method.<br/>              |
| [**Name**](swbemmethod-name.md)<br/>                   | Read-only<br/> | Name of the method.<br/>                                                                                                     |
| [**Origin**](swbemmethod-origin.md)<br/>               | Read-only<br/> | Originating class of the method.<br/>                                                                                        |
| [**OutParameters**](swbemmethod-outparameters.md)<br/> | Read-only<br/> | An [**SWbemObject**](swbemobject.md) object whose properties define the out parameters and return type of this method.<br/> |
| [**Qualifiers\_**](swbemmethod-qualifiers-.md)<br/>    | Read-only<br/> | An [**SWbemQualifierSet**](swbemqualifierset.md) object that contains the qualifiers for this method.<br/>                  |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemMethod<br/>                                                           |
| IID<br/>                      | IID\_ISWbemMethod<br/>                                                            |



## See also

<dl> <dt>

[Scripting API Objects](scripting-api-objects.md)
</dt> </dl>

 

 




