---
title: Using Shaders in Direct3D 10
description: Using Shaders in Direct3D 10
ms.assetid: cff6f901-cb9b-44d5-a75b-9a4029a37215
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Using Shaders in Direct3D 10

The pipeline has three shader stages and each one is programmed with an HLSL shader. All Direct3D 10 shaders are written in HLSL, targeting shader model 4.


Differences between Direct3D 9 and Direct3D 10:

- Unlike Direct3D 9 shader models which could be authored in an intermediate assembly language, shader model 4.0 shaders are only authored in HLSL. Offline compilation of shaders into device-consumable bytecode is still supported, and recommended for most scenarios.



 

This example uses only a vertex shader. Because all shaders are built from the common shader core, learning how to use a vertex shader is very similar to using a geometry or pixel shader.

Once you have authored an HLSL shader (this example uses the vertex shader HLSLWithoutFX.vsh), you will need to prepare it for the particular pipeline stage that will use it. To do this you need to:

-   [Compile a Shader](#compile-a-shader)
-   [Create a Shader Object](#create-a-shader-object)
-   [Set the Shader Object](#set-the-shader-object)
-   [Repeat for all 3 Shader Stages](#repeat-for-all-3-shader-stages)

These steps need to be repeated for each shader in the pipeline.

## Compile a Shader

The first step is to compile the shader, to check to see that you have coded the HLSL statements correctly. This is done by calling D3D10CompileShader and supplying it with several parameters as shown here:


```
    IPD3D10Blob * pBlob;
    
        
    // Compile the vertex shader from the file
    D3D10CompileShader( strPath, strlen( strPath ), "HLSLWithoutFX.vsh", 
        NULL, NULL, "Ripple", "vs_4_0", dwShaderFlags, &pBlob, NULL );
```



This function takes the following parameters:

-   The name of the file ( and length of the name string in bytes ) that contains the shader. This example uses a vertex shader only (in the file HLSLWithoutFX.vsh file where the file extension .vsh is an abbreviation for vertex shader).
-   The shader function name. This example compiles a vertex shader from the Ripple function which takes a single input and returns an output struct (the function is from the HLSLWithoutFX sample):
    ```
    VS_OUTPUT Ripple( in float2 vPosition : POSITION )
    ```

    

-   A pointer to all macros used by the shader. Use D3D10\_SHADER\_MACRO to help define your macros; simply create a name string that contains all the macro names (with each name separated by a space) and a definition string (with each macro body separated by a space). Both strings need to be NULL terminated.
-   A pointer to any other files that you need included to get your shaders to compile. This uses the ID3D10Include interface which has two user-implemented methods: Open and Close. To make this work, you will need to implement the body of the Open and Close methods; in the Open method add the code you would use to open whatever include files you want, in the Close function add the code to close the files when you are done with them.
-   The name of the shader function to compile. This shader compiles the Ripple function.
-   The shader profile to target when compiling. Since you can compile a function into a vertex, geometry, or pixel shader, the profile tells the compiler which type of shader and which shader model to compare the code against.
-   Shader compiler flags. These flags tell the compiler what information to put into the compiled output and how you want the output code optimized: for speed, for debug, etc. See [Effect Constants (Direct3D 10)](/windows/desktop/direct3d10/d3d10-graphics-reference-effect-constants) for a listing of the available flags. The sample contains some code you can use to set the compiler flag values for your project - this is mainly a question of whether or not you want to generate debug information.
-   A pointer to the buffer that contains the compiled shader code. The buffer also contains any embedded debug and symbol table information requested by the compiler flags.
-   A pointer to a buffer that contains a listing of errors and warnings that were encountered during the compile, which are the same messages you would see in the debug output if you were running the debugger while compiling the shader. **NULL** is an acceptable value when you don't want the errors returned to a buffer.

If the shader compiles successfully, a pointer to the shader code is returned as a ID3D10Blob interface. It is called the Blob interface because the pointer is to a location in memory that is made up of an array of DWORD's. The interface is provided so that you can get a pointer to the compiled shader which you will need in the next step.

Beginning with the December 2006 SDK, the DirectX 10 HLSL compiler is now the default compiler in both DirectX 9 and DirectX 10. See [Effect-Compiler Tool](/windows/desktop/direct3dtools/fxc) for details.

### Get a Pointer to a Compiled Shader

Several API methods require a pointer to a compiled shader. This argument is usually called *pShaderBytecode* because it points to a compiled shader represented as a sequence of byte codes. To get a pointer to a compiled shader, first compile the shader by calling [**D3D10CompileShader**](/windows/desktop/api/d3d10shader/nf-d3d10shader-d3d10compileshader) or a similar function. If compilation is successful, the compiled shader is returned in an [**ID3D10Blob**](/windows/desktop/api/d3dcommon/nn-d3dcommon-id3d10blob) interface. Finally, use the [**GetBufferPointer**](/windows/desktop/api/d3dcommon/nf-d3dcommon-id3d10blob-getbufferpointer) method to return the pointer.

## Create a Shader Object

Once the shader is compiled, call CreateVertexShader to create the shader object:


```
    ID3D10VertexShader ** ppVertexShader
    ID3D10Blob pBlob;


    // Create the vertex shader
    hr = pd3dDevice->CreateVertexShader( (DWORD*)pBlob->GetBufferPointer(),
        pBlob->GetBufferSize(), &ppVertexShader );

    // Release the pointer to the compiled shader once you are done with it
    pBlob->Release();
```



To create the shader object, pass the pointer to the compiled shader into CreateVertexShader. Since you had to successfully compile the shader first, this call will almost certainly pass, unless you have a memory problem on your machine.

You can create as many shader objects as you like and simply keep pointers to them. This same mechanism works for geometry and pixel shaders assuming you match the shader profiles (when you call the compile method) to the interface names (when you call the create method).

## Set the Shader Object

The last step is set the shader to the pipeline stage. Since there are three shader stages in the pipeline, you will need to make three API calls, one for each stage.


```
    // Set a vertex shader
    pd3dDevice->VSSetShader( g_pVS10 );
```



The call to VSSetShader takes the pointer to the vertex shader created in step 1. This sets the shader in the device. The vertex shader stage is now initialized with its vertex shader code, all that remains is initializing any shader variables.

## Repeat for all 3 Shader Stages

Repeat these same set of steps to build any vertex or pixel shader or even a geometry shader that outputs to the pixel shader.

## Related Topics

[Compiling Shaders](dx-graphics-hlsl-part1.md)


## Related topics

<dl> <dt>

[Programming Guide for HLSL](dx-graphics-hlsl-pguide.md)
</dt> </dl>

 

