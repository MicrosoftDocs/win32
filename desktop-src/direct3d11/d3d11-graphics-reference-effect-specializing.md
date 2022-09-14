---
title: Specializing Interfaces (Direct3D 11)
description: ID3DX11EffectVariable has a number of methods for casting the interface into the particular type of interface you need.
ms.assetid: 20892af0-7d4a-4a89-b8d7-4ef225400697
ms.topic: article
ms.date: 05/31/2018
---

# Specializing Interfaces (Direct3D 11)

[**ID3DX11EffectVariable**](id3dx11effectvariable.md) has a number of methods for casting the interface into the particular type of interface you need. The methods are of the form *AsType* and include a method for each type of effect variable (such as AsBlend, AsConstantBuffer etc..)

For example, suppose you have an effect with two global variables: time and a world transform.


```
float    g_fTime;
float4x4 g_mWorld;
```



Here is an example that gets these variables:


```
ID3DX11EffectVariable* g_pVariable;
ID3DX11EffectMatrixVariable* g_pmWorld;
ID3DX11EffectScalarVariable* g_pfTime;

g_pVariable = g_pEffect11->GetVariableByName("g_mWorld");
g_pmWorld = g_pVariable->AsMatrix();
g_pVariable = g_pEffect11->GetVariableByName("g_fTime");
g_pfTime = g_pVariable->AsScalar();
```



By specializing the interfaces, you could reduce the code to a single call.


```
g_pmWorld = (g_pEffect11->GetVariableByName("g_mWorld"))->AsMatrix();
g_pfTime = (g_pEffect11->GetVariableByName("g_fTime"))->AsScalar();
```



Interfaces that inherit from [**ID3DX11EffectVariable**](id3dx11effectvariable.md) also have these methods, but they have been designed to return invalid objects; only calls from **ID3DX11EffectVariable** return valid objects. Applications can test the returned object to see if it is valid by calling [**ID3DX11EffectVariable::IsValid**](id3dx11effectvariable-isvalid.md).

## Related topics

<dl> <dt>

[Effects (Direct3D 11)](d3d11-graphics-programming-guide-effects.md)
</dt> </dl>

 

 




