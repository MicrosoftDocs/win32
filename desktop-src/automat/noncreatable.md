---
title: noncreatable
description: Indicates that the class does not support creation at the top level (for example, through ITypeInfo CreateInstance or CoCreateInstance). An object of such a class is usually obtained through a method call on another object.
ms.assetid: '38b4ce41-595b-4905-bd92-f98348278024'
---

# noncreatable

Indicates that the class does not support creation at the top level (for example, through [**ITypeInfo::CreateInstance**](itypeinfo-createinstance.md) or CoCreateInstance). An object of such a class is usually obtained through a method call on another object.

## Allowed on

Coclass.

## Flags

<dl> TYPEFLAG\_FCANCREATE  
</dl>

## Example


```C++
[
   uuid(1e196b20-1fc3-1069-996b-00dd010ef671),
   helpstring("This is Dynaset"),
   noncreatable
]
coclass Dynaset
{
   [default] interface IDynaset;
   [default, source] interface IDynasetEvents;
}
```



## Related topics

<dl> <dt>

[Attribute Descriptions](attribute-descriptions.md)
</dt> </dl>

 

 




