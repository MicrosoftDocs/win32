---
title: Api.JetGetSystemParameter method (JET_INSTANCE, JET_SESID, JET_param, IntPtr, String, Int32) (Microsoft.Isam.Esent.Interop)
TOCTitle: JetGetSystemParameter method (JET_INSTANCE, JET_SESID, JET_param, IntPtr, String, Int32)
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetGetSystemParameter(Microsoft.Isam.Esent.Interop.JET_INSTANCE,Microsoft.Isam.Esent.Interop.JET_SESID,Microsoft.Isam.Esent.Interop.JET_param,System.IntPtr@,System.String@,System.Int32)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.api.jetgetsystemparameter(v=EXCHG.10)
ms:contentKeyID: 55100731
ms.date: 07/30/2014
ms.topic: article
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.Api.JetGetSystemParameter
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.JetGetSystemParameter method (JET_INSTANCE, JET_SESID, JET_param, IntPtr, String, Int32)

Gets database configuration options.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Function JetGetSystemParameter ( _
    instance As JET_INSTANCE, _
    sesid As JET_SESID, _
    paramid As JET_param, _
    ByRef paramValue As IntPtr, _
    <OutAttribute> ByRef paramString As String, _
    maxParam As Integer _
) As JET_wrn
'Usage
Dim instance As JET_INSTANCE
Dim sesid As JET_SESID
Dim paramid As JET_param
Dim paramValue As IntPtr
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
    ref IntPtr paramValue,
    out string paramString,
    int maxParam
)
```

#### Parameters

  - instance  
    Type: [Microsoft.Isam.Esent.Interop.JET_INSTANCE](hh564593\(v=exchg.10\).md)  
    
    The instance to retrieve the options from.

<!-- end list -->

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET_SESID](hh596745\(v=exchg.10\).md)  
    
    The session to use.

<!-- end list -->

  - paramid  
    Type: [Microsoft.Isam.Esent.Interop.JET_param](hh596135\(v=exchg.10\).md)  
    
    The parameter to get.

<!-- end list -->

  - paramValue  
    Type: [System.IntPtr](https://docs.microsoft.com/dotnet/api/system.intptr?redirectedfrom=MSDN)  
    
    Returns the value of the parameter, if the value is an integer.

<!-- end list -->

  - paramString  
    Type: [System.String](https://docs.microsoft.com/dotnet/api/system.string?redirectedfrom=MSDN)  
    
    Returns the value of the parameter, if the value is a string.

<!-- end list -->

  - maxParam  
    Type: [System.Int32](https://docs.microsoft.com/dotnet/api/system.int32?redirectedfrom=MSDN)  
    
    The maximum size of the parameter string.

#### Return value

Type: [Microsoft.Isam.Esent.Interop.JET_wrn](hh557250\(v=exchg.10\).md)  
An ESENT warning code.  

## Remarks

[ErrorToString](hh596135\(v=exchg.10\).md) passes in the error number in the paramValue, which is why it is a ref parameter and not an out parameter.

## See also

#### Reference

[Api class](dn292211\(v=exchg.10\).md)

[Api members](dn292213\(v=exchg.10\).md)

[JetGetSystemParameter overload](dn292183\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

