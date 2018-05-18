---
title: Creating Separate Type Libraries
description: For each supported language, write and register a separate type library.
ms.assetid: '7a66764e-6f5a-4f27-a64f-aa3c5e058eef'
---

# Creating Separate Type Libraries

For each supported language, write and register a separate type library. The type libraries use the same DISPIDs and globally unique identifiers, but you should localize names and Help strings based on the language. You must also define the LCIDs for the supported languages.

The following registration file example includes entries for U.S. English and German.


```C++
// Type library registration information.
HKEY_CLASSES_ROOT\TypeLib\{F37C8060-4AD5-101B-B826-00DD01103DE1}
HKEY_CLASSES_ROOT\TypeLib\{F37C8060-4AD5-101B-B826-00DD01103DE1}\2.0 =Hello 2.0 Type Library
HKEY_CLASSES_ROOT\TypeLib\{F37C8060-4AD5-101B-B826-00DD01103DE1}\2.0\HELPDIR
=
// U.S. English.
HKEY_CLASSES_ROOT\TypeLib\{F37C8060-4AD5-101B-B826-00DD01103DE1}\2.0\409\win32 = helloeng.tlb
// German.
HKEY_CLASSES_ROOT\TypeLib\{F37C8060-4AD5-101B-B826-00DD01103DE1}\2.0\407\win32 = helloger.tlb
 
```



 

 




