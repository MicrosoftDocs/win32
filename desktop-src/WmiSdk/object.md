---
description: The OBJECT data type is a WMI class object use to declare weakly typed associations and embedded objects.
ms.assetid: 1ad99b92-dfd4-4147-abf5-045edceaa97d
ms.tgt_platform: multiple
title: OBJECT
ms.topic: article
ms.date: 05/31/2018
---

# OBJECT

The OBJECT data type is a WMI class object use to declare weakly typed associations and embedded objects. You do not define the specific class for a weakly typed object until you create an instance of the class. Embedded objects defined with the OBJECT data type can contain instances of any WMI class. For more information, see [Embedded Objects](embedded-objects.md).

The following example defines and creates instances of two classes, one of which contains an embedded object of type OBJECT:

``` syntax
#pragma namespace("\\\\.\\root")

instance of __Namespace
{
    Name = "WMI" ;
} ;

#pragma namespace("\\\\.\\root\\WMI")

class CompositeClass
{
    [key] string aKey;   
    object EmbObj;       // Weakly typed
};

class EmbClass

{
  [key] string aKey;
};

instance of CompositeClass
{
    aKey = "CompositeClass Key";
    EmbObj = 
        instance of EmbClass
        {
           aKey = "key for embedded object";
        };
};
```

 

 



