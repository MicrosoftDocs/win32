---
title: How To Instance a Geometry Shader
description: Geometry shader instancing allows multiple executions of the same geometry shader to be executed per primitive.
ms.assetid: e3d8616b-7129-40e9-99fc-2852914a80b0
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# How To: Instance a Geometry Shader

Geometry shader instancing allows multiple executions of the same geometry shader to be executed per primitive. To instance a geometry shader, add an instance attribute to the main shader function and identify an instance index parameter in the shader function body.

To Instance a Geometry Shader:

1.  Add the [instance attribute](sm5-attributes-instance.md) to the main function.

    ```
    [instance(24)]
    ```

    

    This defines the number of instances (a maximum of 32) to be run for each primitive.

2.  Attach the [SV\_GSInstanceID](sv-gsinstanceid.md) system value to a variable in the function parameter list that can be used to track the ID of the instance being executed.
    ```
    uint InstanceID : SV_GSInstanceID
    ```

    

3.  Compile and create the shader just as you would any other geometry shader.

Other details include:

-   The maximum instance count is 32.
-   The maximum vertex count is a per-instance maximum vertex count.
-   Each instance invocation (like any geometry shader invocation) increases the invocation count and generates an implicit RestartStrip().

## Related topics

<dl> <dt>

[Geometry Shader Features](overviews-direct3d-11-hlsl-gs-features.md)
</dt> </dl>

 

 




