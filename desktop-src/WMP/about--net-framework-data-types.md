---
title: About .NET Framework Data Types
description: About .NET Framework Data Types
ms.assetid: 8683888b-889f-4ab2-8eab-dbb79735f13f
keywords:
- Windows Media Player,.NET Framework
- Windows Media Player object model,.NET Framework
- object model,.NET Framework
- Windows Media Player Mobile,.NET Framework
- Windows Media Player ActiveX control,.NET Framework
- Windows Media Player Mobile ActiveX control,.NET Framework
- ActiveX control,.NET Framework
- .NET Framework,data types
ms.topic: article
ms.date: 05/31/2018
---

# About .NET Framework Data Types

This section contains the information you need to translate the script-oriented Object Model Reference into Microsoft .NET Framework base data types. The Windows Media Player script reference has almost all the information you need to use the Windows Media Player control in a .NET Framework-based program, and in most cases, the syntax will be similar to that of other scripting languages such as Microsoft JScript.

The Windows Media Player reference provides the JScript data type and, if necessary, the C++ conversion. For example, a **Number** might be returned by a method. JScript treats all numbers in the same way, but other languages distinguish between different types of numbers (integer, floating point, and so on). The reference gives the C++ conversion for number data types because numbers can be processed differently by C++. For example, C++ uses the **int** data type for integer arithmetic and **float** for floating point.

The .NET Framework uses a slightly different system of base data types. The following table shows the differences in the common data types you are likely to use. For more information on .NET Framework base data types and the conversion to other data type systems, see the .NET Framework Developer's Guide discussion of System Namespace base data types.

This table gives the .NET Framework class name and the C# data type. Data types for other languages are defined for each language in their respective language references.



| Script data type | C++ data type     | .NET Framework class (C# data type ) |
|------------------|-------------------|---------------------------------------|
| **Number**       | **int**           | **Int32** (**int**)                   |
| **Number**       | **long**          | **Int32** (**int**)                   |
| **Number**       | **double**        | **Double** (**double**)               |
| **Number**       | **float**         | **Single** (**float**)                |
| **String**       | **BSTR**          | **String** (**string**)               |
| **Boolean**      | **VARIANT\_BOOL** | **Boolean** (**bool**)                |
| **Object**       | **Object**        | **Object** (**object**)               |



 

If you are using Visual Studio, you can use the Microsoft IntelliSense technology to determine what data type is expected for a specific function.

## Related topics

<dl> <dt>

[**Embedding the Windows Media Player Control in a .NET Framework Solution**](using-the-windows-media-player-control-in-a--net-framework-solution.md)
</dt> <dt>

[**Object Model Reference for Scripting**](object-model-reference-for-scripting.md)
</dt> </dl>

 

 




