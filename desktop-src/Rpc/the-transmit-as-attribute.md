---
title: The transmit_as Attribute
description: The \ transmit\_as\ attribute offers a way to control data marshaling without worrying about marshaling data at a low level \ 8212;that is, without worrying about data sizes or byte swapping in a heterogeneous environment.
ms.assetid: 04e670c9-b091-457d-aeca-058cf5b664e8
keywords:
- Remote Procedure Call RPC , attributes, transmit_as
- transmit_as
ms.topic: article
ms.date: 05/31/2018
---

# The transmit\_as Attribute

The **\[**[**transmit\_as**](/windows/desktop/Midl/transmit-as)**\]** attribute offers a way to control data marshaling without worrying about marshaling data at a low level—that is, without worrying about data sizes or byte swapping in a heterogeneous environment. By letting you reduce the amount of data transmitted over the network, the **\[transmit\_as\]** attribute can make your application more efficient.

You use the **\[transmit\_as\]** attribute to specify a data type that the RPC stubs will transmit over the network instead of using the data type provided by the application. You supply routines that convert the data type to and from the type that is used for transmission. You must also supply routines to free the memory used for the data type and the transmitted type. For example, the following defines **xmit\_type** as the data type transmitted for all application data specified as being of type **type\_spec**:

``` syntax
typedef [transmit_as (xmit_type)] type_spec type;
```

The following table describes the four programmer-supplied routine names. **Type** is the data type known to the application, and **xmit\_type** is the data type used for transmission.



| Routine                                                 | Description                                                                                                                                     |
|---------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [**type\_to\_xmit**](the-type-to-xmit-function.md)     | Allocates an object of the transmitted type and converts from application type to type transmitted over the network (caller and object called). |
| [**Type\_from\_xmit**](the-type-from-xmit-function.md) | Converts from transmitted type to application type (caller and object called).                                                                  |
| [**Type\_free\_inst**](the-type-free-inst-function.md) | Frees resources used by the application type (object called only).                                                                              |
| [**Type\_free\_xmit**](the-type-free-xmit-function.md) | Frees storage returned by the **type***\_***to\_xmit** routine (caller and object called).                                                      |



 

Other than by these four programmer-supplied functions, the transmitted type is not manipulated by the application. The transmitted type is defined only to move data over the network. After the data is converted to the type used by the application, the memory used by the transmitted type is freed.

These programmer-supplied routines are provided by either the client or the server application based on the directional attributes. If the parameter is **\[**[**in**](/windows/desktop/Midl/in)**\]** only, the client transmits to the server. The client needs the **type\_to\_xmit** and **type\_free\_xmit** functions. The server needs the **type\_from\_xmit** and **type\_free\_inst** functions. For an **\[**[**out**](/windows/desktop/Midl/out-idl)**\]**-only parameter, the server transmits to the client. The server application must implement the **type\_to\_xmit** and **type\_free\_xmit** functions, while the client program must supply the **type\_from\_xmit** function. For the temporary **xmit\_type** objects, the stub will call **type***\_***free\_xmit** to free any memory allocated by a call to **type\_to\_xmit**.

Certain guidelines apply to the application type instance. If the application type is a pointer or contains a pointer, then the **type**\_**from\_xmit** routine must allocate memory for the data that the pointers point to (the application type object itself is manipulated by the stub in the usual way).

For **\[out\]** and **\[in, out\] out\]** parameters, or one of their components, of a type that contains the **\[transmit\_as\]** attribute, the **type**\_**free\_inst** routine is automatically called for the data objects that have the attribute. For **in** parameters, the **type**\_**free\_inst** routine is called only if the **\[transmit\_as\]** attribute has been applied to the parameter. If the attribute has been applied to the components of the parameter, the **type**\_**free\_inst** routine is not called. There are no freeing calls for the embedded data and at-most-one call (related to the top-level attribute) for an **in** only parameter.

Effective with MIDL 2.0, both client and server must supply all four functions. For example, a linked list can be transmitted as a sized array. The **type\_to\_xmit** routine walks the linked list and copies the ordered data into an array. The array elements are ordered so that the many pointers associated with the list structure do not have to be transmitted. The **type\_from\_xmit** routine reads the array and puts its elements into a linked-list structure.

The double-linked list (DOUBLE\_LINK\_LIST) includes data and pointers to the previous and next list elements:

``` syntax
typedef struct _DOUBLE_LINK_LIST 
{
    short sNumber;
    struct _DOUBLE_LINK_LIST * pNext;
    struct _DOUBLE_LINK_LIST * pPrevious;
} DOUBLE_LINK_LIST;
```

Rather than shipping the complex structure, the **\[**[**transmit\_as**](/windows/desktop/Midl/transmit-as)**\]** attribute can be used to send it over the network as an array. The sequence of items in the array retains the ordering of the elements in the list at a lower cost:

``` syntax
typedef struct _DOUBLE_XMIT_TYPE 
{
    short sSize;
    [size_is(sSize)] short asNumber[];
} DOUBLE_XMIT_TYPE;
```

The **\[transmit\_as\]** attribute appears in the IDL file:

``` syntax
typedef [transmit_as(DOUBLE_XMIT_TYPE)]  DOUBLE_LINK_LIST DOUBLE_LINK_TYPE;
```

In the following example, **ModifyListProc** defines the parameter of type DOUBLE\_LINK\_TYPE as an **\[in, out\]** parameter:

``` syntax
void ModifyListProc([in, out] DOUBLE_LINK_TYPE * pHead)
```

The four programmer-defined functions use the name of the type in the function names, and use the presented and transmitted types as parameter types, as required:

``` syntax
void __RPC_USER DOUBLE_LINK_TYPE_to_xmit ( 
    DOUBLE_LINK_TYPE __RPC_FAR * pList, 
    DOUBLE_XMIT_TYPE __RPC_FAR * __RPC_FAR * ppArray);

void __RPC_USER DOUBLE_LINK_TYPE_from_xmit ( 
    DOUBLE_XMIT_TYPE __RPC_FAR * pArray,
    DOUBLE_LINK_TYPE __RPC_FAR * pList);

void __RPC_USER DOUBLE_LINK_TYPE_free_inst ( 
    DOUBLE_LINK_TYPE __RPC_FAR * pList);

void __RPC_USER DOUBLE_LINK_TYPE_free_xmit ( 
    DOUBLE_XMIT_TYPE __RPC_FAR * pArray);
```

 

 