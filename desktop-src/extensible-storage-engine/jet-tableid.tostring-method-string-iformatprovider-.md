---
title: JET_TABLEID.ToString method (String, IFormatProvider)
TOCTitle: ToString method (String, IFormatProvider)
ms:assetid: M:Microsoft.Isam.Esent.Interop.JET_TABLEID.ToString(System.String,System.IFormatProvider)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_tableid.tostring(v=EXCHG.10)
ms:contentKeyID: 39510805
ms.date: 07/30/2014
ms.topic: reference
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.JET_TABLEID.ToString
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_TABLEID.ToString method (String, IFormatProvider)

Formats the value of the current instance using the specified format.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Function ToString ( _
    format As String, _
    formatProvider As IFormatProvider _
) As String
'Usage
Dim instance As JET_TABLEID
Dim format As String
Dim formatProvider As IFormatProvider
Dim returnValue As String

returnValue = instance.ToString(format, _
    formatProvider)
```

``` csharp
public string ToString(
    string format,
    IFormatProvider formatProvider
)
```

#### Parameters

  - format  
    Type: [System.String](https://docs.microsoft.com/dotnet/api/system.string?redirectedfrom=MSDN)  
    
    The [String](https://docs.microsoft.com/dotnet/api/system.string?redirectedfrom=MSDN) specifying the format to use; or, null to use the default format defined for the type of the [IFormattable](https://docs.microsoft.com/dotnet/api/system.iformattable?redirectedfrom=MSDN) implementation.

<!-- end list -->

  - formatProvider  
    Type: [System.IFormatProvider](https://docs.microsoft.com/dotnet/api/system.iformatprovider?redirectedfrom=MSDN)  
    
    The [IFormatProvider](https://docs.microsoft.com/dotnet/api/system.iformatprovider?redirectedfrom=MSDN) to use to format the value; or, null to obtain the numeric format information from the current locale setting of the operating system.

#### Return value

Type: [System.String](https://docs.microsoft.com/dotnet/api/system.string?redirectedfrom=MSDN)  
A [String](https://docs.microsoft.com/dotnet/api/system.string?redirectedfrom=MSDN) containing the value of the current instance in the specified format.  

#### Implements

[IFormattable.ToString(String, IFormatProvider)](https://docs.microsoft.com/dotnet/api/system.iformattable.tostring?redirectedfrom=MSDN#System_IFormattable_ToString_System_String_System_IFormatProvider_)  

## See also

#### Reference

[JET_TABLEID structure](hh566310\(v=exchg.10\).md)

[JET_TABLEID members](hh596310\(v=exchg.10\).md)

[ToString overload](hh596553\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

