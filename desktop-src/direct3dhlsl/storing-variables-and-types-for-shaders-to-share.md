---
title: Storing Variables and Types for Shaders to Share
description: The class linkage object is a namespace for variables and types that multiple shaders can share.
ms.assetid: 8b61677b-a466-4646-b0b2-19097669f8c3
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Storing Variables and Types for Shaders to Share

The class linkage object is a namespace for variables and types that multiple shaders can share. When you pass a class linkage object in a call to create a shader, the runtime gathers a list of variables and types that can implement each interface in the shader and stores the names of those variables and types in the class linkage object.

Therefore, when you call the [**ID3D11ClassLinkage::GetClassInstance**](/windows/desktop/api/d3d11/nf-d3d11-id3d11classlinkage-getclassinstance) method to generate class instances from the class linkage object, the runtime can retrieve the variable or type that corresponds to the name that is provided in each shader (if that name is valid for a given shader) and that is created with the given class linkage object.

For example, suppose you have a **Light** class that implements a **Color** interface, and you use this class in your vertex shader and pixel shader. When you create a shader (for example, by calling [**ID3D11Device::CreatePixelShader**](/windows/desktop/api/d3d11/nf-d3d11-id3d11device-createpixelshader)), the runtime determines that the **Light** class type is available in both vertex and pixel shaders and adds the **Light** class type to the class linkage object. You can then create a **Light** instance at a location that you want, bind the resources for both shaders, and pass this instance in the class instances array when you set the shader to the device (for example, by calling [**ID3D11DeviceContext::PSSetShader**](/windows/desktop/api/d3d11/nf-d3d11-id3d11devicecontext-pssetshader)). The runtime then performs the following sequence:

1.  Verifies that the instance was created with the same class linkage object.
2.  Verifies that the **Light** class type is availabe in both vertex and pixel shaders.
3.  Selects the correct function tables, which can be different for the vertex and pixel shaders.
4.  Sends down the offsets that the instance provides.

The class linkage object is ultimately a repository of type and variable names. The maximum number of names available for each item (type and variable) is 64K. The longer the type and variable names are, the higher the storage requirement is for the interface metadata that is stored per shader. This is because the runtime must store a mapping for these names for each shader.

## Related Topics

[Dynamic Linking](overviews-direct3d-11-hlsl-dynamic-linking.md)


## Related topics

<dl> <dt>

[Dynamic Linking](overviews-direct3d-11-hlsl-dynamic-linking.md)
</dt> </dl>

 

 