---
title: Interpreting Binding Information
description: Microsoft RPC enables your client and server programs access to and interpret the information in a binding handle.
ms.assetid: 0116b7a1-85f8-4860-8fba-4aa1960c6799
keywords:
- Remote Procedure Call RPC , tasks, interpreting binding
ms.topic: article
ms.date: 05/31/2018
---

# Interpreting Binding Information

Microsoft RPC enables your client and server programs access to and interpret the information in a binding handle. This does not mean that you can or should try to access the contents of a binding handle directly. Microsoft RPC provides functions that set and retrieve the information in binding handles.

To get the information in a binding handle, pass the handle to [**RpcBindingToStringBinding**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingtostringbinding). It returns the binding information as a string. For every call to **RpcBindingToStringBinding**, you must have a corresponding call to the function [**RpcStringFree**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcstringfree).

You can call the function [**RpcStringBindingParse**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcstringbindingparse) to parse the string you obtain from [**RpcBindingToStringBinding**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingtostringbinding). This function allocates strings to contain the information it parses. If you do not want it to parse a particular piece of binding information, pass a **NULL** as the value of that parameter. Be sure to call [**RpcStringFree**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcstringfree) for each of the strings it allocates.

The following code fragment illustrates how an application might call these functions.


```C++
RPC_STATUS status;
UCHAR *lpzStringBinding;
UCHAR *lpzProtocolSequence;
UCHAR *lpzNetworkAddress;
UCHAR *lpzEndpoint;
UCHAR *NetworkOptions;
 
// The variable hBindingHandle is a valid binding handle.
 
status = RpcBindingToStringBinding(hBindingHandle,&lpzStringBinding);
// Code to check the status goes here.
 
status = RpcStringBindingParse(
    lpzStringBinding,
    NULL,
    &lpzProtocolSequence;
    &lpzNetworkAddress;
    &lpzEndpoint;
    &NetworkOptions);
// Code to check the status goes here.
 
// Code to analyze and alter the binding information in the strings
// goes here.
 
status = RpcStringFree(&lpzStringBinding);
// Code to check the status goes here.
 
status = RpcStringFree(&lpzProtocolSequence);
// Code to check the status goes here.
 
status = RpcStringFree(&lpzNetworkAddress);
// Code to check the status goes here.
 
status = RpcStringFree(&NetworkOptions);
// Code to check the status goes here.
```



The preceding sample code calls the functions [**RpcBindingToStringBinding**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingtostringbinding) and [**RpcStringBindingParse**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcstringbindingparse) to get and parse the information in a valid binding handle. Note that the value **NULL** was passed as the second parameter to **RpcStringBindingParse**. This causes that function to skip parsing the object UUID. Since it does not parse the UUID, **RpcStringBindingParse** will not allocate a string for it. This technique enables your application to only allocate memory for the information you are interested in parsing and analyzing.

 

 




