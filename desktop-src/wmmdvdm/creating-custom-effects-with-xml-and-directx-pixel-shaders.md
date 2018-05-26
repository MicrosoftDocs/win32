---
title: Creating Custom Effects with XML and DirectX Pixel Shaders
description: Creating Custom Effects with XML and DirectX Pixel Shaders
ms.assetid: be2c5440-80d7-4a34-bdc2-452588ba5023
keywords:
- Windows Movie Maker,XML pixel shaders
- Movie Maker,XML pixel shaders
- programming guide,XML pixel shaders
- creating custom effects using pixel shaders
- XML,effects
- XML,pixel shaders
- custom effects,XML pixel shaders
- Windows Movie Maker,DirectX pixel shaders
- Movie Maker,DirectX pixel shaders
- programming guide,DirectX pixel shaders
- creating custom effects using pixel shaders
- custom effects,DirectX pixel shaders
- DirectX,effects
- DirectX,pixel shaders
- effects,custom
- pixel shaders
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating Custom Effects with XML and DirectX Pixel Shaders

**Note** This section refers solely to Windows Movie Maker, but any effects you create will also be available for use in Windows DVD Maker.

A DirectX effect enables the integration of vertex and pixel shaders with graphics pipeline state to render objects. A DirectX effect is written using High-Level Shader Language (HLSL), and is encapsulated into an effect file (.fx). For more information on DirectX effects, see [Effects](http://go.microsoft.com/fwlink/p/?linkid=82166) in the DirectX SDK on MSDN.

Using XML and an .fx file, you can create a Windows Movie Maker effect without having to write any C++ code. Do this with the following steps:

1.  Create the XML file for your effect, as described in step 1 of [Making Your Own XML File](making-your-own-xml-file.md). Add the following two parameters to your effect, where "MyShader.fx" is the name of your effect file.

    ```C++
    <Param name="Animation" value="FX" />
    <Param name="FXFile" value="MyShader.fx" />
    ```

    

    When you use your own .fx file, the value of the "Animation" parameter must be set to "FX". Windows Movie Maker will automatically implement any "FX" animations.

2.  Write your DirectX effect in your shader (.fx) file. DirectX effect rendering options are controlled by adding techniques and passes. For more information, see the DirectX SDK. Write a technique that implements your Windows Movie Maker effect. Then add the following tag to your XML file, where "MyTechnique" is the technique you just wrote.

    ```C++
    <Param name="Technique" value="MyTechnique" />
    ```

    

    **Note** "Passes" are handled differently in Windows Movie Maker effects than they are in conventional shaders. In conventional shaders, the second pass means that a new set of shaders is run on the same mesh, but the second pass is rendered to the same render target as the first pass. In Windows Movie Maker effects, passes are interpreted as a chained rendering, where pass 0 is rendered to a texture and pass 1 is rendered to a new render target. The first input to pass 1 is the output of pass 0. The texture with the "LastTexture" semantic in the file Common.fxh (located in %ProgramFiles%\\MovieMaker\\Shared) is set to the input of the previous pass. So for pass 1, TexLast is set to the original input to pass 0.

3.  Use global variables marked by semantics to pass input to your shader from the XML file. For example, to pass a float as input, define a variable in your shader file as follows:

    ```C++
    float fMyInput : 

        MyInput
    
    ```

    

    Now, in the XML file, add "MyInput" as a parameter under your effect. Make sure that it is enclosed inside a `<Semantics/>` tag. For example, see the following:

    ```C++
    <Semantics>
        <
    MyInput evaluation="Step" type="float">
            <Point time="0.0" value="0.0"/>
            <Point time="1.0" value="10.0"/>
        </
    MyInput>
    </Semantics>
    ```

    

4.  After writing your shader, put it in the folder %ProgramFiles%\\MovieMaker\\Shared. Your shader (.fx) file must include the file Common.fxh (which is also located in %ProgramFiles%\\MovieMaker\\Shared).

    The following global variables have already been defined for you in Common.fxh:

    ```C++
    float4x4 mWorld : World;  //World Matrix
    float4x4 mView : View;  //View Matrix
    float4x4 mProjection : Projection;  //Projection Matrix

    float3x3 mTex0 : TextureMatrix0;  //Texture tranform matrix

    float fTime : Time;  //Current time
    float2 f2szPix : PixelSize;  //Size of a pixel

    texture Tex0 : InputTexture0;  //The input texture on which the effect has to be applied
    texture TexLast : LastTexture;  //The texture from the previous pass
    ```

    

    There are also helper functions that have been defined in Common.fxh. For more information, open Common.fxh using Visual Studio or any text editor.

## The Brightness Sample Effect

The rest of this section is devoted to a complete sample effect that increases the brightness level as the video clip progresses.

To create this effect, first define a global variable called "BrightnessPercent" that gradually increases from 0.0 to 1.0. The values for "BrightnessPercent" will be passed in through XML. Create an XML file called MyShader.xml and put it in one of the locations described in Step 1 of [Making Your Own XML File](making-your-own-xml-file.md). Paste the following into the XML file:


```C++
<TransitionsAndEffects Version="2.8">
    <Effects>
        <EffectDLL guid="TFX">
            <Effect name="MyShaderEffect" iconid="0" guid="MyShaderEffect" comment="" shadermodel="2">
                <Param name="Animation" value="FX" />
                <Param name="FXFile" value="MyShader.fx" />
                <Param name="Technique" value="FadeIn" />
                <Semantics>
                  <BrightnessPercent evaluation="Linear" type="float">
                    <Point time="0.0" value="0.0"/>
                    <Point time="1.0" value="1.0"/>
                  </BrightnessPercent>
                </Semantics>
            </Effect>
        </EffectDLL>
    </Effects>
</TransitionsAndEffects> 
```



Now create a file called MyShader.fx, paste the following code into the file, and save it in the same location as MyShader.xml. This file defines the technique "FadeIn".


```C++
#include "common.fxh"

float g_f4BrightnessPercent : BrightnessPercent;

sampler s = sampler_state
{
    Texture   = (Tex0);
    MipFilter = Linear;
    MinFilter = Anisotropic;
    MagFilter = LINEAR;
};

float4 PS_FadeIn(float2 f2TexCoord  : TEXCOORD0) : COLOR
{
    float4 f4TexColor = tex2D( s , f2TexCoord);
    float4 f4OutColor = g_f4BrightnessPercent * f4TexColor;

return f4OutColor;
}

/// <summary>
///      Fade
///      
///      Technique to fade to or from a color
/// </summary>

technique FadeIn
{
    pass P0
    {          
        VertexShader = compile vs_2_0 VS_Basic();
        PixelShader  = compile ps_2_0 PS_FadeIn(); 
    }
} 
```



**Note** The function **VS\_Basic** is defined in Common.fxh. It is a simple vertex shader the applies the World, View, and Projection transforms and passes the texture coordinate unmodified.

Your effect is now ready to be used in Windows Movie Maker. If Windows Movie Maker was running while you created the files, you must exit and restart it before your new effect can be used.

## Related topics

<dl> <dt>

[**Programming Guide**](programming-guide.md)
</dt> </dl>

 

 




