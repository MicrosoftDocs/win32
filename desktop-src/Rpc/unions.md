---
title: union keyword (RPC)
description: Unions require special MIDL keywords to support their use with Remote Procedure Call (RPC).
ms.assetid: e7c8296c-893d-4df7-913a-f969733e1917
ms.topic: article
ms.date: 05/31/2018
---

# union keyword (RPC)

Some features of the C language, such as unions, require special MIDL keywords to support their use in remote procedure calls. A union in the C language is a variable that holds objects of different types and sizes. The developer usually creates a variable to keep track of the types stored in the union. To operate correctly in a distributed environment, the variable that indicates the type of the union, or the *discriminant*, must also be available to the remote computer. MIDL provides the \[[**switch\_type**](/windows/desktop/Midl/switch-type)\] and \[[**switch\_is**](/windows/desktop/Midl/switch-is)\] keywords to identify the discriminant type and name.

MIDL requires that the discriminant be transmitted with the union in one of two ways:

-   The union and the discriminant must be provided as parameters.
-   The union and the discriminant must be packaged in a structure.

Two fundamental types of discriminated unions are provided by MIDL: [**nonencapsulated\_union**](/windows/desktop/Midl/nonencapsulated-unions) and [**encapsulated\_union**](/windows/desktop/Midl/encapsulated-unions). The discriminant of a nonencapsulated union is another parameter if the union is a parameter. It is another field if the union is a field of a structure. The definition of an encapsulated union is turned into a structure definition whose first field is the discriminant and whose second and last fields are the union. The following example demonstrates how to provide the union and discriminant as parameters:

``` syntax
typedef [switch_type(short)] union 
{
    [case(0)]    short     sVal;
    [case(1)]    float     fVal;
    [case(2)]    char      chVal;
    [default]    ;
} DISCRIM_UNION_PARAM_TYPE;
 
short UnionParamProc(
    [in, switch_is(sUtype)] DISCRIM_UNION_PARAM_TYPE Union,
    [in] short sUtype);
```

The union in the preceding example can contain a single value: either **short**, **float**, or **char**. The type definition for the union includes the MIDL **switch\_type** attribute that specifies the type of the discriminant. Here, \[switch\_type(short)\] specifies that the discriminant is of type **short**. The switch must be an integer type.

If the union is a member of a structure, then the discriminant must be a member of the same structure. If the union is a parameter, then the discriminant must be another parameter. The prototype for the function **UnionParamProc** in the preceding example shows the discriminant *sUtype* as the last parameter of the call. (The discriminant can appear in any position in the call.) The type of the parameter specified in the **\[switch\_is\]** attribute must match the type specified in the **\[switch\_type\]** attribute.

The following example demonstrates the use of a single structure that packages the discriminant with the union:

``` syntax
typedef struct 
{
    short utype;  /* discriminant can precede or follow union */
    [switch_is(utype)] union 
    {
       [case(0)]   short     sVal;
       [case(1)]   float     fVal;
       [case(2)]   char      chVal;
       [default]   ;
    } u;
} DISCRIM_UNION_STRUCT_TYPE;
 
short UnionStructProc(
    [in] DISCRIM_UNION_STRUCT_TYPE u1);
```

The Microsoft RPC MIDL compiler allows union declarations outside of [**typedef**](/windows/desktop/Midl/typedef) constructs. This feature is an extension to DCE IDL. For more information, see [**union**](/windows/desktop/Midl/union).

 

 