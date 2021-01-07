---
description: "Learn more about: Api.JetGetSystemParameter method (JET_INSTANCE, JET_SESID, JET_param, Int32, String, Int32)"
title: Api.JetGetSystemParameter method (JET_INSTANCE, JET_SESID, JET_param, Int32, String, Int32)
TOCTitle: JetGetSystemParameter method (JET_INSTANCE, JET_SESID, JET_param, Int32, String, Int32)
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetGetSystemParameter(Microsoft.Isam.Esent.Interop.JET_INSTANCE,Microsoft.Isam.Esent.Interop.JET_SESID,Microsoft.Isam.Esent.Interop.JET_param,System.Int32@,System.String@,System.Int32)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.api.jetgetsystemparameter(v=EXCHG.10)
ms:contentKeyID: 55100727
ms.date: 07/30/2014
ms.topic: reference
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.Api.JetGetSystemParameter
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.JetGetSystemParameter method (JET_INSTANCE, JET_SESID, JET_param, Int32, String, Int32)

Gets database configuration options.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Function JetGetSystemParameter ( _
    instance As JET_INSTANCE, _
    sesid As JET_SESID, _
    paramid As JET_param, _
    ByRef paramValue As Integer, _
    <OutAttribute> ByRef paramString As String, _
    maxParam As Integer _
) As JET_wrn
'Usage
Dim instance As JET_INSTANCE
Dim sesid As JET_SESID
Dim paramid As JET_param
Dim paramValue As Integer
Dim paramString As String
Dim maxParam As Integer
Dim returnValue As JET_wrn

returnValue = Api.JetGetSystemParameter(instance, _
    sesid, paramid, paramValue, paramString, _
    maxParam)
```

``` csharp
public static JET_wrn JetGetSystemParameter(
    JET_INSTANCE instance,
    JET_SESID sesid,
    JET_param paramid,
    ref int paramValue,
    out string paramString,
    int maxParam
)
```

#### Parameters

  - instance  
    Type: [Microsoft.Isam.Esent.Interop.JET_INSTANCE](./jet-instance-structure.md)  
    
    The instance to retrieve the options from.

<!-- end list -->

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET_SESID](./jet-sesid-structure.md)  
    
    The session to use.

<!-- end list -->

  - paramid  
    Type: [Microsoft.Isam.Esent.Interop.JET_param](./jet-param-enumeration.md)  
    
    The parameter to get.

<!-- end list -->

  - paramValue  
    Type: [System.Int32](/dotnet/api/system.int32)  
    
    Returns the value of the parameter, if the value is an integer.

<!-- end list -->

  - paramString  
    Type: [System.String](/dotnet/api/system.string)  
    
    Returns the value of the parameter, if the value is a string.

<!-- end list -->

  - maxParam  
    Type: [System.Int32](/dotnet/api/system.int32)  
    
    The maximum size of the parameter string.

#### Return value

Type: [Microsoft.Isam.Esent.Interop.JET_wrn](./jet-wrn-enumeration.md)  
An ESENT warning code.  

## Remarks

[ErrorToString](./jet-param-enumeration.md) passes in the error number in the paramValue, which is why it is a ref parameter and not an out parameter.

## See also

#### Reference

[Api class](./api-class.md)

[Api members](./api-members.md)

[JetGetSystemParameter overload](./api.jetgetsystemparameter-method.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
