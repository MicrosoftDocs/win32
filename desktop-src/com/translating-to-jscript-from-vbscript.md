---
title: Translating to JScript from VBScript
description: Translating to JScript from VBScript
ms.assetid: cdf04a01-8bc3-4f37-872b-3a0aae962f26
ms.topic: article
ms.date: 05/31/2018
---

# Translating to JScript from VBScript

In VBScript, the **For**...**Each** loop enumerates the members of a collection; in JScript, the **for**...**in** loop enumerates the members of a JScript object or array. To enumerate a collection in JScript, use an Enumerator object.

In JScript, there are several data types such as numbers, strings, Booleans, objects, and the null attribute. VBScript only uses one data type, **Variant**, which can be subtyped to represent strings, numbers, Booleans, and so on.

In JScript, arrays can be expanded dynamically by setting a new value for the array's length property. In VBScript, arrays cannot be enlarged; they must be redimensioned using the **redim** statement.

Both VBScript and JScript support functions. VBScript, however, also supports subroutines. Subroutines are similar to functions but do not return a value.

JScript is case-sensitive. VBScript is not.

JScript is supported by both Internet Explorer and Netscape Navigator. Netscape Navigator does not support VBScript.

JScript provides the Error object, which can be used to trap and handle errors. The Error object is analogous to the VBScript Err object.

JScript arrays are not arrays of the variable type **VARIANT SAFEARRAY**. If your script receives a **VARIANT SAFEARRAY** variable from a COM object or VBScript script, it must use a VBArray object to access the **VARIANT SAFEARRAY** variable.

## Related topics

<dl> <dt>

[Translating to JScript](translating-to-jscript.md)
</dt> </dl>

 

 




