---
description: The MOF compiler accepts a floating-point value specified for a nonfloating-point property. The value is rounded up or down and stored as a nonfloating-point number. This situation can cause some unexpected results.
ms.assetid: 5cf7d8e1-c29d-4b9f-8557-e656c5e83370
ms.tgt_platform: multiple
title: Compiling MOF Code with Floating-Point Values
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Compiling MOF Code with Floating-Point Values

The MOF compiler accepts a floating-point value specified for a nonfloating-point property. The value is rounded up or down and stored as a nonfloating-point number. This situation can cause some unexpected results.

The following MOF code example defines a class called **abc** in a namespace called "Test". This MOF code compiles without errors, but you cannot query for the floating-point value defined for the property **exampleUint16** in the instance this code creates.

``` syntax
#pragma namespace ("\\\\.\\Root")

instance of __Namespace
{
    Name = "Test";
};

#pragma namespace ("\\\\.\\Root\\test")

Class abc
{
        [KEY] String testID ;
        Uint16 exampleUint16;
        Real64 exampleReal64;
};

Instance of abc
{ 
        TestID ="exampleID";
        exampleUint16 = 1000.4;
};
```

If you issue the following query, you get an error code that indicates an invalid query.


```sql
SELECT * FROM abc WHERE exampleUint16 = 1000.4
```



However, the following query finds the indicated instance.


```sql
SELECT * FROM abc WHERE exampleUint16 = 1000
```



## Related topics

<dl> <dt>

[Compiling MOF Files](compiling-mof-files.md)
</dt> <dt>

[**mofcomp**](mofcomp.md)
</dt> <dt>

[Preprocessor Commands](preprocessor-commands.md)
</dt> </dl>

 

 



