---
title: Translating to VBScript from JScript
description: Translating to VBScript from JScript
ms.assetid: db1115e1-2abd-4b06-ad8d-c1f917cd3087
ms.topic: article
ms.date: 05/31/2018
---

# Translating to VBScript from JScript

In VBScript, the **For**...**Each** loop enumerates the members of a collection; in JScript, the **for**...**in** loop enumerates the members of a JScript object or array. To enumerate a collection in JScript, use an Enumerator object.

JScript provides the Error object, which can be used to trap and handle errors. The Error object is analogous to the VBScript Err object.

In JScript, there are several data types such as numbers, strings, Booleans, objects, and the null attribute. VBScript only uses one data type, **Variant**, which can be subtyped to represent strings, numbers, Booleans, and so on.

In JScript, arrays can be expanded dynamically by setting a new value for the array's length property. In VBScript, arrays cannot be enlarged; they must be redimensioned using the **redim** statement.

Both VBScript and JScript support functions. VBScript, however, also supports subroutines. Subroutines are similar to functions but do not return a value.

JScript is case-sensitive. VBScript is not.

JScript is supported by a wide variety of Web browsers, including both Internet Explorer and Netscape Navigator. Netscape Navigator does not support VBScript.

JScript arrays are not arrays of the variable type **VARIANT SAFEARRAY**. A JScript script must use a VBArray object to access the **VARIANT SAFEARRAY** variable. VBScript scripts can access **VARIANT SAFEARRAY** variables directly.

## Related topics

<dl> <dt>

[Translating to VBScript](translating-to-vbscript.md)
</dt> </dl>

 

 




