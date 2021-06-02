---
title: Per-Component Math Operations
description: With HLSL, you can program shaders at an algorithm level.
ms.assetid: a919df50-2d13-489d-9011-1137c997e121
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Per-Component Math Operations

With HLSL, you can program shaders at an algorithm level. To understand the language, you will need to know how to declare variables and functions, use intrinsic functions, define custom data types and use semantics to connect shader arguments to other shaders and to the pipeline.

Once you learn how to author shaders in HLSL, you will need to learn about API calls so that you can: compile a shader for particular hardware, initialize shader constants, and initialize other pipeline state if necessary.

-   [The Vector Type](#the-vector-type)
-   [The Matrix Type](#the-matrix-type)
    -   [Matrix Ordering](#matrix-ordering)
-   [Examples](#examples)
-   [Related topics](#related-topics)

## The Vector Type

A vector is a data structure that contains between one and four components.


```
bool    bVector;   // scalar containing 1 Boolean
bool1   bVector;   // vector containing 1 Boolean
int1    iVector;   // vector containing 1 int
float3  fVector;   // vector containing 3 floats
double4 dVector;   // vector containing 4 doubles
```



The integer immediately following the data type is the number of components on the vector.

Initializers can also be included in the declarations.


```
bool    bVector = false;
int1    iVector = 1;
float3  fVector = { 0.2f, 0.3f, 0.4f };
double4 dVector = { 0.2, 0.3, 0.4, 0.5 };
```



Alternatively, the vector type can be used to make the same declarations:


```
vector <bool,   1> bVector = false;
vector <int,    1> iVector = 1;
vector <float,  3> fVector = { 0.2f, 0.3f, 0.4f };
vector <double, 4> dVector = { 0.2, 0.3, 0.4, 0.5 };
```



The vector type uses angle brackets to specify the type and number of components.

Vectors contain up to four components, each of which can be accessed using one of two naming sets:

-   The position set: x,y,z,w
-   The color set: r,g,b,a

These statements both return the value in the third component.


```
// Given
float4 pos = float4(0,0,2,1);

pos.z    // value is 2
pos.b    // value is 2
```



Naming sets can use one or more components, but they cannot be mixed.


```
// Given
float4 pos = float4(0,0,2,1);
float2 temp;

temp = pos.xy  // valid
temp = pos.rg  // valid

temp = pos.xg  // NOT VALID because the position and color sets were used.
```



Specifying one or more vector components when reading components is called swizzling. For example:


```
float4 pos = float4(0,0,2,1);
float2 f_2D;
f_2D = pos.xy;   // read two components 
f_2D = pos.xz;   // read components in any order       
f_2D = pos.zx;

f_2D = pos.xx;   // components can be read more than once
f_2D = pos.yy;
```



Masking controls how many components are written.


```
float4 pos = float4(0,0,2,1);
float4 f_4D;
f_4D    = pos;     // write four components          

f_4D.xz = pos.xz;  // write two components        
f_4D.zx = pos.xz;  // change the write order

f_4D.xzyw = pos.w; // write one component to more than one component
f_4D.wzyx = pos;
```



Assignments cannot be written to the same component more than once. So the left side of this statement is invalid:


```
f_4D.xx = pos.xy;   // cannot write to the same destination components 
```



Also, the component name spaces cannot be mixed. This is an invalid component write:


```
f_4D.xg = pos.rgrg;    // invalid write: cannot mix component name spaces 
```



Accessing a vector as a scalar will access the first component of the vector. The following two statements are equivalent.


```
f_4D.a = pos * 5.0f;
f_4D.a = pos.r * 5.0f;
```



## The Matrix Type

A matrix is a data structure that contains rows and columns of data. The data can be any of the scalar data types, however, every element of a matrix is the same data type. The number of rows and columns is specified with the row-by-column string that is appended to the data type.


```
int1x1    iMatrix;   // integer matrix with 1 row,  1 column
int2x1    iMatrix;   // integer matrix with 2 rows, 1 column
...
int4x1    iMatrix;   // integer matrix with 4 rows, 1 column
...
int1x4    iMatrix;   // integer matrix with 1 row, 4 columns
double1x1 dMatrix;   // double matrix with 1 row,  1 column
double2x2 dMatrix;   // double matrix with 2 rows, 2 columns
double3x3 dMatrix;   // double matrix with 3 rows, 3 columns
double4x4 dMatrix;   // double matrix with 4 rows, 4 columns
```



The maximum number of rows or columns is 4; the minimum number is 1.

A matrix can be initialized when it is declared:


```
float2x2 fMatrix = { 0.0f, 0.1, // row 1
                     2.1f, 2.2f // row 2
                   };   
```



Or, the matrix type can be used to make the same declarations:


```
matrix <float, 2, 2> fMatrix = { 0.0f, 0.1, // row 1
                                 2.1f, 2.2f // row 2
                               };
```



The matrix type uses the angle brackets to specify the type, the number of rows, and the number of columns. This example creates a floating-point matrix, with two rows and two columns. Any of the scalar data types can be used.

This declaration defines a matrix of float values (32-bit floating-point numbers) with two rows and three columns:


```
matrix <float, 2, 3> fFloatMatrix;
```



A matrix contains values organized in rows and columns, which can be accessed using the structure operator "." followed by one of two naming sets:

-   The zero-based row-column position:
    -   \_m00, \_m01, \_m02, \_m03
    -   \_m10, \_m11, \_m12, \_m13
    -   \_m20, \_m21, \_m22, \_m23
    -   \_m30, \_m31, \_m32, \_m33
-   The one-based row-column position:
    -   \_11, \_12, \_13, \_14
    -   \_21, \_22, \_23, \_24
    -   \_31, \_32, \_33, \_34
    -   \_41, \_42, \_43, \_44

Each naming set starts with an underscore followed by the row number and the column number. The zero-based convention also includes the letter "m" before the row and column number. Here's an example that uses the two naming sets to access a matrix:


```
// given
float2x2 fMatrix = { 1.0f, 1.1f, // row 1
                     2.0f, 2.1f  // row 2
                   }; 

float f_1D;
f_1D = matrix._m00; // read the value in row 1, column 1: 1.0
f_1D = matrix._m11; // read the value in row 2, column 2: 2.1

f_1D = matrix._11;  // read the value in row 1, column 1: 1.0
f_1D = matrix._22;  // read the value in row 2, column 2: 2.1
```



Just like vectors, naming sets can use one or more components from either naming set.


```
// Given
float2x2 fMatrix = { 1.0f, 1.1f, // row 1
                     2.0f, 2.1f  // row 2
                   };
float2 temp;

temp = fMatrix._m00_m11 // valid
temp = fMatrix._m11_m00 // valid
temp = fMatrix._11_22   // valid
temp = fMatrix._22_11   // valid
```



A matrix can also be accessed using array access notation, which is a zero-based set of indices. Each index is inside of square brackets. A 4x4 matrix is accessed with the following indices:

-   \[0\]\[0\], \[0\]\[1\], \[0\]\[2\], \[0\]\[3\]
-   \[1\]\[0\], \[1\]\[1\], \[1\]\[2\], \[1\]\[3\]
-   \[2\]\[0\], \[2\]\[1\], \[2\]\[2\], \[2\]\[3\]
-   \[3\]\[0\], \[3\]\[1\], \[3\]\[2\], \[3\]\[3\]

Here is an example of accessing a matrix:


```
float2x2 fMatrix = { 1.0f, 1.1f, // row 1
                     2.0f, 2.1f  // row 2
                   };
float temp;

temp = fMatrix[0][0] // single component read
temp = fMatrix[0][1] // single component read
```



Notice that the structure operator "." is not used to access an array. Array access notation cannot use swizzling to read more than one component.


```
float2 temp;
temp = fMatrix[0][0]_[0][1] // invalid, cannot read two components
```



However, array accessing can read a multi-component vector.


```
float2 temp;
float2x2 fMatrix;
temp = fMatrix[0] // read the first row
```



As with vectors, reading more than one matrix component is called swizzling. More than one component can be assigned, assuming only one name space is used. These are all valid assignments:


```
// Given these variables
float4x4 worldMatrix = float4( {0,0,0,0}, {1,1,1,1}, {2,2,2,2}, {3,3,3,3} );
float4x4 tempMatrix;

tempMatrix._m00_m11 = worldMatrix._m00_m11; // multiple components
tempMatrix._m00_m11 = worldMatrix.m13_m23;

tempMatrix._11_22_33 = worldMatrix._11_22_33; // any order on swizzles
tempMatrix._11_22_33 = worldMatrix._24_23_22;
```



Masking controls how many components are written.


```
// Given
float4x4 worldMatrix = float4( {0,0,0,0}, {1,1,1,1}, {2,2,2,2}, {3,3,3,3} );
float4x4 tempMatrix;

tempMatrix._m00_m11 = worldMatrix._m00_m11; // write two components
tempMatrix._m23_m00 = worldMatrix._m00_m11;
```



Assignments cannot be written to the same component more than once. So the left side of this statement is invalid:


```
// cannot write to the same component more than once
tempMatrix._m00_m00 = worldMatrix._m00_m11;
```



Also, the component name spaces cannot be mixed. This is an invalid component write:


```
// Invalid use of same component on left side
tempMatrix._11_m23 = worldMatrix._11_22; 
```



### Matrix Ordering

Matrix packing order for uniform parameters is set to column-major by default. This means each column of the matrix is stored in a single constant register. On the other hand, a row-major matrix packs each row of the matrix in a single constant register. Matrix packing can be changed with the **\#pragmapack\_matrix** directive, or with the **row\_major** or the **column\_major** keyword.

The data in a matrix is loaded into shader constant registers before a shader runs. There are two choices for how the matrix data is read: in row-major order or in column-major order. Column-major order means that each matrix column will be stored in a single constant register, and row-major order means that each row of the matrix will be stored in a single constant register. This is an important consideration for how many constant registers are used for a matrix.

A row-major matrix is laid out like the following:



|     |     |     |     |
|-----|-----|-----|-----|
| 11  | 12  | 13  | 14  |
| 21  | 22  | 23  | 24  |
| 31  | 32  | 33  | 34  |
| 41  | 42  | 43  | 44  |



 

A column-major matrix is laid out like the following:



|     |     |     |     |
|-----|-----|-----|-----|
| 11  | 21  | 31  | 41  |
| 12  | 22  | 32  | 42  |
| 13  | 23  | 33  | 43  |
| 14  | 24  | 34  | 44  |



 

Row-major and column-major matrix ordering determine the order the matrix components are read from shader inputs. Once the data is written into constant registers, matrix order has no effect on how the data is used or accessed from within shader code. Also, matrices declared in a shader body do not get packed into constant registers. Row-major and column-major packing order has no influence on the packing order of constructors (which always follows row-major ordering).

The order of the data in a matrix can be declared at compile time or the compiler will order the data at runtime for the most efficient use.

## Examples

HLSL uses two special types, a vector type and a matrix type to make programming 2D and 3D graphics easier. Each of these types contain more than one component; a vector contains up to four components, and a matrix contains up to 16 components. When vectors and matrices are used in standard HLSL equations, the math performed is designed to work per-component. For instance, HLSL implements this multiply:


```
float4 v = a*b;
```



as a four-component multiply. The result is four scalars:


```
float4 v = a*b;

v.x = a.x*b.x;
v.y = a.y*b.y;
v.z = a.z*b.z;
v.w = a.w*b.w;
```



This is four multiplications where each result is stored in a separate component of v. This is called a four-component multiply. HLSL uses component math which makes writing shaders very efficient.

This is very different from a multiply which is typically implemented as a dot product which generates a single scalar:


```
v = a.x*b.x + a.y*b.y + a.z*b.z + a.w*b.w;
```



A matrix also uses per-component operations in HLSL:


```
float3x3 mat1,mat2;
...
float3x3 mat3 = mat1*mat2;
```



The result is a per-component multiply of the two matrices (as opposed to a standard 3x3 matrix multiply). A per component matrix multiply yields this first term:


```
mat3.m00 = mat1.m00 * mat2._m00;
```



This is different from a 3x3 matrix multiply which would yield this first term:


```
// First component of a four-component matrix multiply
mat.m00 = mat1._m00 * mat2._m00 + 
          mat1._m01 * mat2._m10 + 
          mat1._m02 * mat2._m20 + 
          mat1._m03 * mat2._m30;
```



Overloaded versions of the multiply intrinsic function handle cases where one operand is a vector and the other operand is a matrix. Such as: vector \* vector, vector \* matrix, matrix \* vector, and matrix \* matrix. For instance:


```
float4x3 World;

float4 main(float4 pos : SV_POSITION) : SV_POSITION
{
    float4 val;
    val.xyz = mul(pos,World);
    val.w = 0;

    return val;
}   
```



produces the same result as:


```
float4x3 World;

float4 main(float4 pos : SV_POSITION) : SV_POSITION
{
    float4 val;
    val.xyz = (float3) mul((float1x4)pos,World);
    val.w = 0;

    return val;
}   
```



This example casts the pos vector to a column vector using the (float1x4) cast. Changing a vector by casting, or swapping the order of the arguments supplied to multiply is equivalent to transposing the matrix.

Automatic cast conversion causes the multiply and dot intrinsic functions to return the same results as used here:


```
{
  float4 val;
  return mul(val,val);
}
```



This result of the multiply is a 1x4 \* 4x1 = 1x1 vector. This is equivalent to a dot product:


```
{
  float4 val;
  return dot(val,val);
}
```



which returns a single scalar value.

## Related topics

<dl> <dt>

[Data Types (DirectX HLSL)](dx-graphics-hlsl-data-types.md)
</dt> </dl>

 

 




