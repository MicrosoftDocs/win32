---
title: v1_enum attribute
description: The \ v1\_enum\ attribute directs that the specified enumerated type be transmitted as a 32-bit entity, rather than the 16-bit default.
ms.assetid: 46016131-b78e-4a7f-94c8-41ff1780b0b8
keywords:
- v1_enum attribute MIDL
topic_type:
- apiref
api_name:
- v1_enum
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# v1\_enum attribute

The **\[v1\_enum\]** attribute directs that the specified enumerated type be transmitted as a 32-bit entity, rather than the 16-bit default.

``` syntax
[v1_enum] enum 
{
    ...
};
```

## Parameters

This attribute has no parameters.

## Remarks

Using the **\[v1\_enum\]** attribute to transmit an enumerated type as a 32-bit entity increases the efficiency of marshaling and unmarshaling data when such an enumeration is embedded in structures or unions.

For improved performance, we recommend applying the **\[v1\_enum\]** attribute to enumerators in 32-bit applications. Keep in mind, however, that on 16-bit platforms the C compiler treats an enumerated type as a 16-bit [**int**](int.md). Therefore 16-bit client applications need to convert [**enum**](enum.md) types to [**long**](long.md) for remote transmission in order to avoid overwriting data or sending incorrect values.

## Examples

``` syntax
typedef [v1_enum] enum 
{
    value1, 
    value2, ...
};
```

## See also

<dl> <dt>

[**enum**](enum.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**long**](long.md)
</dt> </dl>

 

 




