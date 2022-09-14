---
title: version attribute
description: The \ version\ interface attribute identifies a particular version among multiple versions of an RPC interface. With the version attribute, you ensure that only compatible versions of client and server software are allowed to bind.
ms.assetid: 66ac5cf3-2230-44fd-aaf6-8013e4a4ae81
keywords:
- version attribute MIDL
topic_type:
- apiref
api_name:
- version
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# version attribute

The **\[version\]** interface attribute identifies a particular version among multiple versions of an RPC interface. With the version attribute, you ensure that only compatible versions of client and server software are allowed to bind.

``` syntax
version ( major-value[[. minor-value]] )
```

## Parameters

<dl> <dt>

*major-value* 
</dt> <dd>

Specifies a short unsigned integer between zero and 65,535, inclusive, that represents the major version number.

</dd> <dt>

*minor-value* 
</dt> <dd>

Specifies a short unsigned integer between zero and 65,535, inclusive, that represents the minor version number. The minor version value is optional. If present, the minor version value is separated from the major version number by a period character (.). If not specified, the minor version value is zero.

</dd> </dl>

## Remarks

The MIDL compiler does not support multiple versions of a COM interface. As a result, an interface attribute list that includes the **\[**[**object**](object.md)**\]** attribute cannot include the **\[version\]** attribute. To create a new version of an existing COM interface, use interface inheritance. A derived COM interface has a different UUID but inherits the interface member functions, status codes, and interface attributes of the base interface.

In combination with the **\[**[**uuid**](uuid.md)**\]** value, the **\[version\]** value uniquely identifies the interface. The run-time library passes the **\[version\]** and **\[uuid\]** values to the server when the client calls a remote function. A client can bind to a server for a given interface if:

-   The **\[uuid\]** value is the same.
-   The major version number is the same.
-   The client's minor version number is less than or equal to the server's minor version number.

It is to your benefit and your users' benefit to retain upward compatibility among versionsÂ that is, to modify the interface so that only the minor version number changes. You can retain upward compatibility when you add new data types that are not used by existing functions and when you add new functions without changing the interface specification for existing functions.

Change the major version number if any one of the following conditions apply:

-   If you change a data type that is used by an existing function.
-   If you change the interface specification for an existing function (such as adding or removing a parameter).
-   If you add callbacks that are called by existing functions.

Change the minor version number if all of the following conditions apply:

-   If you add type definitions or constants that are not used by any existing functions or callbacks.
-   If you do not change any existing functions and you add new functions to the interface.
-   If you add callbacks that are not called by any existing functions and the new callbacks follow any existing functions.

If your modifications qualify as an upward-compatible change to the interface, use the following procedure.

**To modify the interface (IDL) file**

1.  Add new constant and type definitions to the interface file.
2.  Add callback functions to the end of the interface file.
3.  Add new functions to the end of the interface file.

The **\[version\]** attribute can occur at most once in the interface header.

When the version attribute is not present, the interface has a default version of 0.0.

The period character between the major and minor numbers is a delimiter and does not represent a decimal point. The minor number is treated as an integer. Leading zeroes are not significant. Trailing zeroes are significant.

For example, the version setting 1.11 represents a major value of one and a minor value of eleven. Version 1.11 does not represent a value between 1.1 and 1.2.

## See also

<dl> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**interface**](interface.md)
</dt> <dt>

[**object**](object.md)
</dt> <dt>

[**uuid**](uuid.md)
</dt> </dl>

 

 




