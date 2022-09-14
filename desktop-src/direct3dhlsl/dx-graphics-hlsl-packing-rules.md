---
title: Packing Rules for Constant Variables
description: Packing rules dictate how tightly data can be arranged when it is stored.
ms.assetid: 5c399342-06e1-47d2-8ecf-e093ed04be50
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Packing Rules for Constant Variables

Packing rules dictate how tightly data can be arranged when it is stored. HLSL implements packing rules for VS output data, GS input and output data, and PS input and output data. (Data is not packed for VS inputs because the IA stage cannot unpack data.)

HLSL packing rules are similar to performing a **\#pragma pack 4** with Visual Studio, which packs data into 4-byte boundaries. Additionally, HLSL packs data so that it does not cross a 16-byte boundary. Variables are packed into a given four-component vector until the variable will straddle a 4-vector boundary; the next variables will be bounced to the next four-component vector.

Each structure forces the next variable to start on the next four-component vector. This sometimes generates padding for arrays of structures. The resulting size of any structure will always be evenly divisible by **sizeof**(*four-component vector*).

Arrays are not packed in HLSL by default. To avoid forcing the shader to take on ALU overhead for offset computations, every element in an array is stored in a four-component vector. Note that you can achieve packing for arrays (and incur the addressing calculations) by using casting.

Following are examples of structures and their corresponding packed sizes (given: a **float1** occupies 4 bytes):


```
//  2 x 16byte elements
cbuffer IE
{
    float4 Val1;
    float2 Val2;  // starts a new vector
    float2 Val3;
};

//  3 x 16byte elements
cbuffer IE
{
    float2 Val1;
    float4 Val2;  // starts a new vector
    float2 Val3;  // starts a new vector
};

//  1 x 16byte elements
cbuffer IE
{
    float1 Val1;
    float1 Val2;
    float2 Val3;
};

//  1 x 16byte elements
cbuffer IE
{
    float1 Val1;
    float2 Val2;
    float1 Val3;
};

//  2 x 16byte elements
cbuffer IE
{
    float1 Val1;
    float1 Val1;
    float1 Val1;
    float2 Val2;    // starts a new vector
};


//  1 x 16byte elements
cbuffer IE
{
    float3 Val1;
    float1 Val2;
};

//  1 x 16byte elements
cbuffer IE
{
    float1 Val1;
    float3 Val2;
};

//  2 x 16byte elements
cbuffer IE
{
    float1 Val1;
    float1 Val1;
    float3 Val2;        // starts a new vector
};


// 3 x 16byte elements
cbuffer IE
{
    float1 Val1;

    struct     {
        float4 SVal1;    // starts a new vector
        float1 SVal2;    // starts a new vector
    } Val2;
};

// 3 x 16byte elements
cbuffer IE
{
    float1 Val1;  
    struct     {
        float1 SVal1;     // starts a new vector
        float4 SVal2;     // starts a new vector
    } Val2;
};

// 3 x 16byte elements
cbuffer IE
{
    struct     {
        float4 SVal1;
        float1 SVal2;    // starts a new vector
    } Val1;

    float1 Val2; 
};
```



## More Aggressive Packing

You could pack an array more aggressively. For instance, given an array of float variables:


```
float4 array[16];
```



You could choose to pack it like this, without any spaces in the array:


```
static float2 aggressivePackArray[32] = (float2[32])array;  
```



The tighter packing is a trade off versus the need for additional shader instructions for address computation.

## Related topics

<dl> <dt>

[Shader Model 4](dx-graphics-hlsl-sm4.md)
</dt> </dl>

 

 




