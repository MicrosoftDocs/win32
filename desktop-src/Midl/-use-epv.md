---
title: /use_epv switch
description: The /use\_epv switch directs the MIDL compiler to generate server stub code that calls the server application routine through an entry-point vector (epv), rather than by a static call. The use of this attribute is not recommended.
ms.assetid: 2853d836-ded3-412a-916b-1143968123a2
keywords:
- /use_epv switch MIDL
topic_type:
- apiref
api_name:
- /use_epv
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /use\_epv switch

The **/use\_epv** switch directs the MIDL compiler to generate server stub code that calls the server application routine through an entry-point vector (epv), rather than by a static call. The use of this attribute is not recommended.

``` syntax
midl /use_epv
```

## Switch Options

This switch has no parameters.

## Remarks

Typically, applications require static linkage to the server application routine. The MIDL compiler generates such a call by default. However, if an application requires the server stub to call the server application routine by using the epv, the **/use\_epv** switch must be specified. When the **/use\_epv** switch is specified, the MIDL compiler generates a default epv. This default epv is then used if the application does not register another epv through the [**RpcServerRegisterIf**](/windows/desktop/api/rpcdce/nf-rpcdce-rpcserverregisterif) call.

## Examples

**midl /use\_epv** *filename***.idl**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**/no\_default\_epv**](-no-default-epv.md)
</dt> <dt>

[**RpcServerRegisterIf**](/windows/desktop/api/rpcdce/nf-rpcdce-rpcserverregisterif)
</dt> </dl>

 

 