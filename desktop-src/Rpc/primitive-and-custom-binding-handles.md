---
title: Primitive and Custom Binding Handles
description: All handles declared with the handle\_t or RPC\_BINDING\_HANDLE types are primitive binding handles.
ms.assetid: 7a948aad-02fa-421d-b32c-f5dab071bd04
ms.topic: article
ms.date: 05/31/2018
---

# Primitive and Custom Binding Handles

All handles declared with the [handle\_t](/windows/desktop/Midl/handle-t) or [**RPC\_BINDING\_HANDLE**](rpc-binding-handle.md) types are primitive binding handles. You can extend the [handle\_t](/windows/desktop/Midl/handle-t) or [**RPC\_BINDING\_HANDLE**](rpc-binding-handle.md) types to include more or different information than the primitive handle type contains. When you do, you create a custom binding handle.

To make a custom binding handle for your distributed application, you will need to create your own data type and specify the \[ [handle](/windows/desktop/Midl/handle)\] attribute on a type definition in your IDL file. Ultimately, the stub files map custom binding handles to primitive handles.

If you do create your own binding handle type, you must also supply bind and unbind routines that the client stub uses to map a custom handle to a primitive handle. The stub calls your bind and unbind routines at the beginning and end of each remote procedure call. The bind and unbind routines must conform to the following function prototypes.



| Function prototype                     | Description       |
|----------------------------------------|-------------------|
| handle\_t type\_bind(*type*)           | Binding routine   |
| void type\_unbind(*type*, *handle\_t*) | Unbinding routine |



 

The following example shows how a custom binding handle can be defined in the IDL file:

``` syntax
/* usrdef.idl */
[
  uuid(20B309B1-015C-101A-B308-02608C4C9B53),
  version(1.0),
  pointer_default(unique)
]
interface usrdef
{
  typedef struct _DATA_TYPE 
  {
      unsigned char * pszUuid;
      unsigned char * pszProtocolSequence;
      unsigned char * pszNetworkAddress;
      unsigned char * pszEndpoint;
      unsigned char * pszOptions;
  } DATA_TYPE;
 
  typedef [handle] DATA_TYPE * DATA_HANDLE_TYPE;
  void UsrdefProc([in] DATA_HANDLE_TYPE  hBinding,
                  [in, string] unsigned char *   pszString);
 
  void Shutdown([in] DATA_HANDLE_TYPE hBinding);
}
```

If the bind routine encounters an error, it should raise an exception using the [**RpcRaiseException**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcraiseexception) function. The client stub will then clean up, and let the exception filter through to the exception block surrounding the remote procedure call on the client side. If the bind routine simply returns **NULL**, the client code gets error RPC\_S\_INVALID\_BINDING. While this might be acceptable in certain situations, other situations (such as being out of memory) do not respond well. The unbind routine should be designed so that it does not fail. The unbind routine should not raise exceptions.

The programmer-defined bind and unbind routines appear in the client application. In the following example, the bind routine calls [**RpcBindingFromStringBinding**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingfromstringbinding) to convert the string-binding information to a binding handle. The unbind routine calls [**RpcBindingFree**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingfree) to free the binding handle.

The name of the programmer-defined binding handle, DATA\_HANDLE\_TYPE, appears as part of the name of the functions. It is also used as the parameter type in the function parameters.

``` syntax
/* The client stub calls this _bind routine at the */
/* beginning of each remote procedure call                */
 
RPC_BINDING_HANDLE __RPC_USER DATA_HANDLE_TYPE_bind(
    DATA_HANDLE_TYPE dh1)
{
    RPC_BINDING_HANDLE hBinding;
    RPC_STATUS status;
 
    unsigned char *pszStringBinding;
 
    status = RpcStringBindingCompose(
          dh1.pszUuid,
          dh1.pszProtocolSequence,
          dh1.pszNetworkAddress,
          dh1.pszEndpoint,
          dh1.pszOptions,
          &pszStringBinding);
          ...
 
    status = RpcBindingFromStringBinding(
          pszStringBinding,
          &hBinding);
          ...
 
    status = RpcStringFree(&pszStringBinding); 
    ...
 
    return(hBinding);
}
 
/* The client stub calls this _unbind routine */
/* after each remote procedure call.                            */
void __RPC_USER DATA_HANDLE_TYPE_unbind(
    DATA_HANDLE_TYPE dh1, 
    RPC_BINDING_HANDLE h1)
{
    RPC_STATUS status;
    status = RpcBindingFree(&h1); 
    ...
}
```

Both implicit and explicit binding handles can either be primitive or custom handles. That is, a handle may be:

-   Primitive and implicit
-   Custom and implicit
-   Primitive and explicit
-   Custom and explicit

 

 