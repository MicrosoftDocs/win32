---
title: aggregatable
description: Indicates that the class supports aggregation.
ms.assetid: 'b88fe91b-5500-4d35-b873-fbfc201bc768'
---

# aggregatable

Indicates that the class supports aggregation.

## Allowed on

Coclass.

## Flags

<dl> TYPEFLAG\_FAGGREGATABLE  
</dl>

## Remarks

Indicates that the members of the class can be aggregated.

## Example


```C++
[   uuid(1e196b20-1f3c-1069-996b-00dd010fe676),
   aggregatable   
]
coclass Form
{
   [default] interface IForm;
   [default, source] interface IFormEvents;
}
```



## Related topics

<dl> <dt>

[Attribute Descriptions](attribute-descriptions.md)
</dt> </dl>

 

 




