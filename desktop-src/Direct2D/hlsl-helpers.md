---
title: HLSL Helpers
description: To assist effect authors in writing linkable pixel shaders, d2d1effecthelpers.hlsli defines a set of HLSL language extensions in the form of helper methods and macros.
ms.assetid: 5D0BB99E-7C77-4D45-82E6-F038E4B752A4
ms.topic: article
ms.date: 05/31/2018
---

# HLSL Helpers

To assist effect authors in writing linkable pixel shaders, d2d1effecthelpers.hlsli defines a set of HLSL language extensions in the form of helper methods and macros.

To add d2d1effecthelpers.hlsli to your project, add an \#include statement in the HLSL file. d2d1effecthelpers.hlsli is located in the same location as other Direct2D headers such as d2d1.h; it can be referenced from the HLSL file's property page by adding the macro $(WindowsSDK\_IncludePath) to the Additional Include Directories property. Note that the \#include statement must come after any preprocessor directives such D2D\_INPUT\_COUNT have been defined.

``` syntax
#include <d2d1effecthelpers.hlsli>
```

Direct2D does not support linking compute or vertex shaders. However, if your effect uses both a vertex shader and pixel shader, the output of the pixel shader can still be linked.

## Preprocessor Directives

Preprocessor directives are required to communicate information about the effect. This includes the number of inputs and sampling type of each input. The following values should be defined in the effect shader code above the relevant shader entry point when applicable.

-   `D2D_INPUT_COUNT <N>` : Declares the number of texture inputs to the effect. If the effect has a variable number of inputs, this value must be scoped appropriately to each shader entry point. Defining this value is mandatory.
-   `D2D_INPUT<N>_SIMPLE` : Declares the Nth input to use simple sampling. If not defined, the Nth input defaults to complex. Defining this value is optional.
-   `D2D_INPUT<N>_COMPLEX` : Declares the Nth input to use complex sampling. If not defined, the Nth input defaults to complex. Defining this value is optional.
-   `D2D_REQUIRES_SCENE_POSITION` : Indicates that the shader function calls helper methods that use the scene position value (namely, the [D2DGetScenePosition](d2dgetsceneposition.md) helper function). This parameter should only be included when necessary, since only one function per linked shader can utilize this parameter. Defining this value is optional.
-   `D2D_CUSTOM_ENTRY` : Indicates that the pixel shader function consumes the output of a custom vertex shader, and thus will declare its input parameters. All custom vertex shader inputs use complex sampling, and cannot consume the output of another shader function (i.e. they are only post-linkable). Defining this value is optional.

For example:

``` syntax
#define D2D_INPUT_COUNT 3
#define D2D_INPUT0_SIMPLE
#define D2D_INPUT1_SIMPLE
#define D2D_INPUT2_COMPLEX
#include <d2d1effecthelpers.hlsli>
          
```

## Helper Functions

Helper functions are used as a replacement for some native HLSL intrinsic functions. At compile time, these helper functions are redefined by Direct2D into the appropriate version depending on the compilation target type (full shader or export function).

The helper functions:

<dl>

[D2DGetInput](d2dgetinput.md)  
[D2DSampleInput](d2dsampleinput.md)  
[D2DSampleInputAtOffset](d2dsampleinputatoffset.md)  
[D2DSampleInputAtPosition](d2dsampleinputatposition.md)  
[D2DGetInputCoordinate](d2dgetinputcoordinate.md)  
[D2DGetScenePosition](d2dgetsceneposition.md)  
[D2D\_PS\_ENTRY](d2d-ps-entry.md)  
</dl>

## Related topics

<dl> <dt>

[Effect Shader Linking](effect-shader-linking.md)
</dt> </dl>

 

 




