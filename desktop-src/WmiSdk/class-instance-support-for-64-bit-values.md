---
description: Provides restrictions for the use of 64-bit values as part of a path.
ms.assetid: 63f4f6c5-7803-425d-912f-bb1dd716e617
ms.tgt_platform: multiple
title: Class Instance Support for 64-Bit Values
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Class Instance Support for 64-Bit Values

You can use a 64-bit key value as part of a path, with the following restrictions:

-   As long as you do not exceed the 32-bit range, you can assign and retrieve values from the key as you would a 32-bit property.
-   After you exceed the integer value of 0x7FFFFFFF (for signed types), 0x80000000 (for unsigned types), or 32 bits, you must use quotation marks.
-   The only valid path for a 64-bit value is located in the **\_\_RELPATH** or **\_\_PATH** properties of the instance. As such, WMI does not support the hexadecimal notation for the equivalent value.
-   If WMI records the instance key as a negative number, then you must use the original number to retrieve the instance.

Query semantics are unaffected and behave as expected. This behavior only affects the object path, [**GetObject**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobject), and [**GetObjectAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobjectasync) operations.

The following example shows that class instances can have 64-bit key values.

``` syntax
class MyBig
{
  [key] sint64 k;
  sint64 p;
};

instance of MyBig
{
  k = 2;
  p = 3;
};
```

 

 



