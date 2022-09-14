---
title: Interfaces and Classes
description: Dynamic shader linkage makes use of high-level shader language (HLSL) interfaces and classes that are syntactically similar to their C++ counterparts.
ms.assetid: 124a358d-30ab-4efe-88ed-1ff277d17b25
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Interfaces and classes

Dynamic shader linkage makes use of high-level shader language (HLSL) interfaces and classes that are syntactically similar to their C++ counterparts. This allows shaders to reference abstract interface instances at compile time and leave resolution of those instances to concrete classes for the application at runtime.

The following sections detail how to setup a shader to use interfaces and classes and how to initialize interface instances in application code.

-   [Declaring Interfaces](#declaring-interfaces)
-   [Declaring Classes](#declaring-classes)
-   [Interface Instance Declarations in a Shader](#interface-instance-declarations-in-a-shader)
-   [Class Instance Declarations in a Shader](#class-instance-declarations-in-a-shader)
-   [Initializing Interface Instances in an Application](#initializing-interface-instances-in-an-application)
-   [Related topics](#related-topics)

## Declaring interfaces

An interface functions in a similar manner to an abstract base class in C++. An interface is declared in a shader using the interface keyword and only contains method declarations. The methods declared in an interface will all be virtual methods in any classes derived from the interface. Derived classes must implement all methods declared in an interface. Note that interfaces are the only way to declare virtual methods, there is no virtual keyword as in C++, and classes connot declare virtual methods.

The following example shader code declares two interfaces.


```
interface iBaseLight
{
   float3 IlluminateAmbient(float3 vNormal);
   float3 IlluminateDiffuse(float3 vNormal);
   float3 IlluminateSpecular(float3 vNormal, int specularPower );
};       

interface iBaseMaterial
{
   float3 GetAmbientColor(float2 vTexcoord);
   
   float3 GetDiffuseColor(float2 vTexcoord);

   int GetSpecularPower();

};
      
```



## Declaring Classes

A class behaves in a similar manner to classes in C++. A class is declared with the class keyword and can contain member variables and methods. A class can inherit from zero or one class and zero or more interfaces. Classes must implement or inherit implementations for all interfaces in its inheritance chain or the class cannot be instantiated.

The following example shader code illustrates deriving a class from an interface and from another class.


```
class cAmbientLight : iBaseLight
{
   float3            m_vLightColor;     
   bool     m_bEnable;
   float3 IlluminateAmbient(float3 vNormal);
   float3 IlluminateDiffuse(float3 vNormal);
   float3 IlluminateSpecular(float3 vNormal, int specularPower );
};

class cHemiAmbientLight : cAmbientLight
{
   float4   m_vGroundColor;
   float4   m_vDirUp;
   float3 IlluminateAmbient(float3 vNormal);
};        
      
```



## Interface Instance Declarations in a Shader

An interface instance acts as a place holder for class instances that provide an implementation of the interface's methods. Using an instance of an interface allows shader code to call a method without knowing which implementation of that method will be invoked. Shader code declares one or more instances for each interface it defines. These instances are used in shader code in a similar manner to C++ base class pointers.

The following example shader code illustrates declaring several interface instances and using them in shader code.


```
// Declare interface instances
iBaseLight     g_abstractAmbientLighting;
iBaseLight     g_abstractDirectLighting;
iBaseMaterial  g_abstractMaterial;

struct PS_INPUT
{
    float4 vPosition : SV_POSITION;
    float3 vNormal   : NORMAL;
    float2 vTexcoord : TEXCOORD0;
};

float4 PSMain( PS_INPUT Input ) : SV_TARGET
{ 
    float3 Ambient = (float3)0.0f;       
    Ambient = g_abstractMaterial.GetAmbientColor( Input.vTexcoord ) *         
        g_abstractAmbientLighting.IlluminateAmbient( Input.vNormal );

    float3 Diffuse = (float3)0.0f;  
    Diffuse += g_abstractMaterial.GetDiffuseColor( Input.vTexcoord ) * 
        g_abstractDirectLighting.IlluminateDiffuse( Input.vNormal );

    float3 Specular = (float3)0.0f;   
    Specular += g_abstractDirectLighting.IlluminateSpecular( Input.vNormal, 
        g_abstractMaterial.GetSpecularPower() );
     
    float3 Lighting = saturate( Ambient + Diffuse + Specular );
     
    return float4(Lighting,1.0f); 
}
```



## Class Instance Declarations in a Shader

Each class that will be used in place of an interface instance must either be declared as a variable in a constant buffer or created by the application at runtime using the [**ID3D11ClassLinkage::CreateClassInstance**](/windows/desktop/api/d3d11/nf-d3d11-id3d11classlinkage-createclassinstance) method. Interface instances will be pointed at class instances in the application code. Class instances can be referenced in shader code like any other variable, but a class that is derived from an interface will typically only be used with an interface instance and will not be referenced by shader code directly.

The following example shader code illustrates declaring several class instances.


```
cbuffer cbPerFrame : register( b0 )
{
   cAmbientLight     g_ambientLight;
   cHemiAmbientLight g_hemiAmbientLight;
   cDirectionalLight g_directionalLight;
   cEnvironmentLight g_environmentLight;
   float4            g_vEyeDir;   
};        
      
```



## Initializing Interface Instances in an Application

Interface instances are initialized in application code by passing a dynamic linkage array containing interface assignments to one of the [**ID3D11DeviceContext**](/windows/desktop/api/d3d11/nn-d3d11-id3d11devicecontext) SetShader methods.

To create a dynamic linkage array use the following steps

1.  Create a class linkage object using [**CreateClassLinkage**](/windows/win32/api/d3d11/nf-d3d11-id3d11device-createclasslinkage).
    ```
    ID3D11ClassLinkage* g_pPSClassLinkage = NULL;            
    pd3dDevice->CreateClassLinkage( &g_pPSClassLinkage );
              
    ```

    

2.  Create the shader that will be using dynamic class linking, passing the class linkage object as a parameter to the shader's create function.
    ```
    pd3dDevice->CreatePixelShader( pPixelShaderBuffer->GetBufferPointer(),
        pPixelShaderBuffer->GetBufferSize(), g_pPSClassLinkage, &g_pPixelShader ) );            
              
    ```

    

3.  Create a [**ID3D11ShaderReflection**](/windows/desktop/api/d3d11shader/nn-d3d11shader-id3d11shaderreflection) object using the [**D3DReflect**](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dreflect) function.
    ```
    ID3D11ShaderReflection* pReflector = NULL; 
    D3DReflect( pPixelShaderBuffer->GetBufferPointer(),                  
        pPixelShaderBuffer->GetBufferSize(), 
        IID_ID3D11ShaderReflection, (void**) &pReflector) );            
              
    ```

    

4.  Use the shader reflection object to get the number of interface instances in the shader using the [**ID3D11ShaderReflection::GetNumInterfaceSlots**](/windows/desktop/api/d3d11shader/nf-d3d11shader-id3d11shaderreflection-getnuminterfaceslots) method.
    ```
    g_iNumPSInterfaces = pReflector->GetNumInterfaceSlots();             
              
    ```

    

5.  Create an array large enough to hold the number of interface instances in the shader.
    ```
    ID3D11ClassInstance** g_dynamicLinkageArray = NULL;            
    g_dynamicLinkageArray = 
        (ID3D11ClassInstance**) malloc( sizeof(ID3D11ClassInstance*) * g_iNumPSInterfaces );            
              
    ```

    

6.  Determine the index in the array that corresponds to each interface instance using [**ID3D11ShaderReflection::GetVariableByName**](/windows/desktop/api/d3d11shader/nf-d3d11shader-id3d11shaderreflection-getvariablebyname) and [**ID3D11ShaderReflectionVariable::GetInterfaceSlot**](/windows/desktop/api/d3d11shader/nf-d3d11shader-id3d11shaderreflectionvariable-getinterfaceslot).
    ```
    ID3D11ShaderReflectionVariable* pAmbientLightingVar = 
        pReflector->GetVariableByName("g_abstractAmbientLighting");
        g_iAmbientLightingOffset = pAmbientLightingVar->GetInterfaceSlot(0);            
              
    ```

    

7.  Get a class instance for each class object derived from an interface in the shader using [**ID3D11ClassLinkage::GetClassInstance**](/windows/desktop/api/d3d11/nf-d3d11-id3d11classlinkage-getclassinstance).
    ```
    g_pPSClassLinkage->GetClassInstance( "g_hemiAmbientLight", 0, 
        &g_pHemiAmbientLightClass );            
              
    ```

    

8.  Set interface instances to class instances by setting the corresponding entry in the dynamic linkage array.
    ```
    g_dynamicLinkageArray[g_iAmbientLightingOffset] = g_pHemiAmbientLightClass;            
              
    ```

    

9.  Pass the dynamic linkage array as a parameter to a SetShader call.
    ```
    pd3dImmediateContext->PSSetShader( g_pPixelShader, g_dynamicLinkageArray, g_iNumPSInterfaces );            
              
    ```

    

## Related topics

[Dynamic Linking](overviews-direct3d-11-hlsl-dynamic-linking.md)