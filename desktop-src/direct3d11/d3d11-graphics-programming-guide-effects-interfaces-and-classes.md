---
title: Interfaces and Classes in Effects
description: There are many ways to use classes and interfaces in Effects 11.
ms.assetid: 526d477b-fc1f-4bd0-a620-ce9b78147f68
ms.topic: article
ms.date: 05/31/2018
---

# Interfaces and Classes in Effects

There are many ways to use classes and interfaces in Effects 11. For interface and class syntax, see [Interfaces and Classes](/windows/desktop/direct3dhlsl/overviews-direct3d-11-hlsl-dynamic-linking-class).

The following sections detail how to specify class instances to a shader which uses interfaces. We will use the following interface and classes in the examples:


```
interface IColor
{
  float4 GetColor();
};

class CRed : IColor
{
  float4 GetColor() { return float4(1,0,0,1); }
};
class CGreen : IColor
{
  float4 GetColor() { return float4(0,1,0,1); }
};

CRed pRed;
CGreen pGreen;
IColor pIColor;
IColor pIColor2 = pRed;
```



Note that interface instances can be initialized to class instances. Arrays of class and interface instances are also supported and they can be initialized as in the following example:


```
CRed pRedArray[2];
IColor pIColor3 = pRedArray[1];
IColor pIColorArray[2] = {pRed, pGreen};
IColor pIColorArray2[2] = pRedArray;
```



## Uniform Interface Parameters

Just like other uniform data types, uniform interface parameters must be specified in the CompileShader call. Interface parameters can be assigned to global interface instances or global class instances. When assigned to a global interface instance, the shader will have a dependency on the interface instance, which means that it must be set to a class instance. When assigned to global class instances, the compiler specializes the shader (as with other uniform data types) to use that class. This is important for two scenarios:

1.  Shaders with a 4\_x target can use interface parameters if these parameters are uniform and assigned to global class instances (so no dynamic linkage is used).
2.  Users can decide to have many compiled, specialized shaders with no dynamic linkage or few compiled shaders with dynamic linkage.


```
float4 PSUniform( uniform IColor color ) : SV_Target
{
  return color;
}

technique11
{
  pass
  {
    SetPixelShader( CompileShader( ps_4_0, PSUniform(pRed) ) );
  }
  pass
  {
    SetPixelShader( CompileShader( ps_5_0, PSUniform(pIColor2) ) );
  }
}
```



If pIColor2 remains unchanged through the API, then the previous two passes are functionally equivalent, but the first uses a ps\_4\_0 static shader while the second uses a ps\_5\_0 shader with dynamic linkage. If pIColor2 is changed through the effects API (see Setting Class Instances below), then the behavior of the pixel shader in the second pass may change.

## Non-Uniform Interface Parameters

Non-uniform interface parameters create interface dependencies for the shaders. When applying a shader with interface parameters, these parameters must be assigned in with the BindInterfaces call. Global interface instances and global class instances can be specified in the BindInterfaces call.


```
float4 PSAbstract( IColor color ) : SV_Target
{
  return color;
}

PixelShader pPSAbstract = CompileShader( ps_5_0, PSAbstract(pRed) );

technique11
{
  pass
  {
    SetPixelShader( BindInterfaces( pPSAbstract, pRed ) );
  }
  pass
  {
    SetPixelShader( BindInterfaces( pPSAbstract, pIColor2 ) );
  }
}
```



If pIColor2 remains unchanged through the API, then the previous two passes are functionally equivalent and both use dynamic linkage. If pIColor2 is changed through the effects API (see Setting Class Instances below), then the behavior of the pixel shader in the second pass may change.

## Setting Class Instances

When setting a shader with dynamic shader linkage to the Direct3D 11 device, class instances must also be specified. It is an error to set such a shader with a **NULL** class instance. Therefore, all interface instances which a shader references must have an associated class instance.

The following example shows how to get a class instance variable from an effect and set it to an interface variable:


```
ID3DX11EffectPass* pPass = pEffect->GetTechniqueByIndex(0)->GetPassByIndex(1);

ID3DX11EffectInterfaceVariable* pIface = pEffect->GetVariableByName( "pIColor2" )->AsInterface();
ID3DX11EffectClassInstanceVariable* pCI = pEffect->GetVariableByName( "pGreen" )->AsClassInstance();
pIface->SetClassInstance( pCI );
pPass->Apply( 0, pDeviceContext );

// Apply the same pass with a different class instance
pCI = pEffect->GetVariableByName( "pRedArray" )->GetElement(1)->AsClassInstance();
pIface->SetClassInstance( pCI );
pPass->Apply( 0, pDeviceContext );
```



## Related topics

<dl> <dt>

[Effects (Direct3D 11)](d3d11-graphics-programming-guide-effects.md)
</dt> </dl>

 

 