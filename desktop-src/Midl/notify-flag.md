---
title: notify_flag attribute
description: The \ notify\_flag\ attribute provides notification identifying whether a server routine is called.
ms.assetid: a40b7114-d2e3-40c1-a0b1-599428188611
keywords:
- notify_flag attribute MIDL
topic_type:
- apiref
api_name:
- notify_flag
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# notify\_flag attribute

The **\[notify\_flag\]** attribute provides notification identifying whether a server routine is called.

``` syntax
[notify_flag] procedure-name();
```

## Parameters

<dl> <dt>

*procedure-name* 
</dt> <dd>

Name of the remote procedure with which the notify\_flag procedure is associated.

</dd> </dl>

## Remarks

The **\[notify\_flag\]** attribute is similar in usage to the **\[notify\]** attribute.

The **\[notify\_flag\]** procedure name is the name of the remote procedure suffixed by **\_notify\_flag**. The **\_notify\_flag** procedure does not require any parameters and does not return a result. A prototype of this procedure is also generated in the header file. For example, if the IDL file contains the following:

``` syntax
MyProcedure([in] short S);
```

Specify the following in the ACF for MIDL to generate the **\_notify\_flag** call:

``` syntax
[notify_flag] MyProcedure();
```

The MIDL compiler will generate server stub code which contains the following call to the **\_notify\_flag** procedure:

``` syntax
MyProcedure_notify_flag();
```

The header file will contain a prototype:

``` syntax
void MyProcedure_notify_flag(boolean __MIDL_NotifyFlag);
```

**\_MIDL\_NotifyFlag** is **TRUE** if the server routine is called.

## Examples

``` syntax
[notify_flag] MyProcedure();
```

## See also

<dl> <dt>

[**notify**](notify.md)
</dt> </dl>

 

 




