---
title: notify attribute
description: The \ notify\ attribute instructs the MIDL compiler to generate a call to a \ notify\ procedure on the server side of the application.
ms.assetid: 24f9887b-04b7-491a-ab6e-7c078b967fbc
keywords:
- notify attribute MIDL
topic_type:
- apiref
api_name:
- notify
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# notify attribute

The **\[notify\]** attribute instructs the MIDL compiler to generate a call to a **\[notify\]** procedure on the server side of the application.

``` syntax
[notify] procedure-name();
```

## Parameters

<dl> <dt>

*procedure-name* 
</dt> <dd>

The name of the remote procedure with which the notify procedure will be associated.

</dd> </dl>

## Remarks

The **\[notify\]** procedure called as a result of the **\[notify\]** attribute is associated with a particular remote procedure on the server. It is similar in concept to a callback function. The stub calls the **\[notify\]** procedure after all the output arguments of the remote procedure with which it is associated have been marshaled and any memory associated with the parameters is freed. The **\[notify\]** routine is called if a call fails before the server routine executes. For example, if a server fails during unmarshaling due to receipt of bad data from the client, the \[notify\] routine is called.

The **\[notify\]** attribute is useful to develop applications acquiring resources in remote procedures. These resources are then freed in the **\[notify\]** procedure after the output parameters of the remote procedure are fully marshaled.

The **\[notify\]** procedure name is the name of the remote procedure suffixed by **\_notify**. The **\_notify** procedure does not require any parameters and does not return a result. A prototype of this procedure is also generated in the header file. For example, if the IDL file contains the following:

``` syntax
MyProcedure([in] short S);
```

Specify the following in the ACF for MIDL to generate the **\_notify** call:

``` syntax
[notify] MyProcedure();
```

The MIDL compiler will generate server stub code which contains the following call to the **\_notify** procedure:

``` syntax
MyProcedure_notify();
```

The header file will contain a prototype:

``` syntax
void MyProcedure_notify(void);
```

## Examples

``` syntax
[notify] MyProcedure();
```

## See also

<dl> <dt>

[Application Configuration File (ACF)](application-configuration-file-acf-.md)
</dt> </dl>

 

 




