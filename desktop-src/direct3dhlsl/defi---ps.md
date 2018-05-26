---
title: defi - ps
description: Defines an integer constant value, which should be loaded any time a shader is set to a device.
ms.assetid: c51982a1-45b4-48db-a49a-93165d61efd3
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# defi - ps

Defines an integer constant value, which should be loaded any time a shader is set to a device.

## Syntax



| defi dst, integerValue |
|------------------------|



 

-   dst is the destination register.
-   integerValue is a constant integer value.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| defi                  |      |      |      |      |      | x    | x     | x    | x     |



 

The defi instruction defines a shader constant whose value is loaded anytime a shader is set to a device. These are called immediate constants. Immediate constants take precedence over constants set by the API method SetPixelShaderConstantB.

There are two ways to set a constant in a shader.

1.  Use defi to define the constant directly inside a shader.
2.  Use the API methods to set a constant.
    -   Use [**SetPixelShaderConstantB**](https://msdn.microsoft.com/library/windows/desktop/bb174451) to set a Boolean constant.
    -   Use [**SetPixelShaderConstantF**](https://msdn.microsoft.com/library/windows/desktop/bb174452) to set a floating-point constant.
    -   Use [**SetPixelShaderConstantI**](https://msdn.microsoft.com/library/windows/desktop/bb174453) to set an integer constant.

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




