---
description: "Learn more about: Conversions.ConvertDoubleToDateTime method"
title: Conversions.ConvertDoubleToDateTime method 
TOCTitle: 'ConvertDoubleToDateTime method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Conversions.ConvertDoubleToDateTime(System.Double)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.conversions.convertdoubletodatetime(v=EXCHG.10)
ms:contentKeyID: 55101133
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Conversions.ConvertDoubleToDateTime
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Conversions.ConvertDoubleToDateTime
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Conversions.ConvertDoubleToDateTime method

Convert a double (OA date time format) to a DateTime. Unlike DateTime.FromOADate this doesn't throw exceptions.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Function ConvertDoubleToDateTime ( _
    d As Double _
) As DateTime
'Usage
Dim d As Double
Dim returnValue As DateTime

returnValue = Conversions.ConvertDoubleToDateTime(d)
```

``` csharp
public static DateTime ConvertDoubleToDateTime(
    double d
)
```

#### Parameters

  - d  
    Type: [System.Double](/dotnet/api/system.double)  
    
    The double value.

#### Return value

Type: [System.DateTime](/dotnet/api/system.datetime)  
A DateTime.  

## See also

#### Reference

[Conversions class](./conversions-class.md)

[Conversions members](./conversions-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
