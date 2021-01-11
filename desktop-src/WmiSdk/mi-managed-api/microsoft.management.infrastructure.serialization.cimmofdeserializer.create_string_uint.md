---
description: "Learn more about: CimMofDeserializer.Create method (String, UInt32)"
title: CimMofDeserializer.Create method (String, UInt32) (Microsoft.Management.Infrastructure.Serialization)
TOCTitle: CimMofDeserializer.Create method (String, UInt32) (Microsoft.Management.Infrastructure.Serialization)
ms:assetid: M:Microsoft.Management.Infrastructure.Serialization.CimMofDeserializer.Create(System.String,System.UInt32)
ms.date: 11/13/2019
mtps_version: v=VS.85
f1_keywords:
- Microsoft.Management.Infrastructure.Serialization.CimMofDeserializer.Create
- Microsoft::Management::Infrastructure::.Serialization::CimMofDeserializer::Create
dev_langs:
- CSharp
- C++
- VB
- FSharp
api_location:
- Microsoft.Management.Infrastructure.dll
api_name:
- Microsoft.Management.Infrastructure.Serialization.CimMofDeserializer.Create
api_type:
- Assembly
topic_type:
- apiref
product_family_name: VS
ms.topic: reference
---

# CimMofDeserializer.Create method (String, UInt32)

Creates and initializes a custom deserializer, based on the specified format and flags.

**Namespace:**   [Microsoft.Management.Infrastructure.Serialization](/previous-versions/windows/desktop/wmi_v2/mi-managed-api/hh832966(v=vs.85))  
**Assembly:**  Microsoft.Management.Infrastructure (in Microsoft.Management.Infrastructure.dll)  

## Syntax

``` csharp
public static CimMofDeserializer Create(
    string format,
    uint flags
)
```

``` c++
public:
static CimMofDeserializer^ Create(
    String^ format,
    unsigned int flags
)
```

``` fsharp
static member Create : 
        format:string *
        flags:uint32 -> CimMofDeserializer
```

``` vb
Public Shared Function Create (
    format As String,
    flags As UInteger
) As CimMofDeserializer
```

#### Parameters

  - format  
    Type: [System.String](/dotnet/api/system.string?view=netframework-4.8)
    
    The serialization format. Only "MI_XML" is supported.

<!-- end list -->

  - flags  
    Type: [System.UInt32](/dotnet/api/system.uint32?view=netframework-4.8)
    
    The serialization flags. Must be 0.

#### Return value

Type: [Microsoft.Management.Infrastructure.Serialization.CimMofDeserializer](microsoft.management.infrastructure.serialization.cimmofdeserializer.md)

The newly created deserializer object.

## See also

[CimMofDeserializer class](microsoft.management.infrastructure.serialization.cimmofdeserializer.md)
[Microsoft.Management.Infrastructure.Serialization namespace](/previous-versions/windows/desktop/wmi_v2/mi-managed-api/hh832966(v=vs.85))
