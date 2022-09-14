---
title: /no_default_epv switch
description: The /no\_default\_epv switch directs the MIDL compiler not to generate a default entry-point vector (epv). The use of this attribute is not recommended.
ms.assetid: 160b5fd3-cd9c-4f51-8c35-6cddab120021
keywords:
- /no_default_epv switch MIDL
topic_type:
- apiref
api_name:
- /no_default_epv
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /no\_default\_epv switch

The **/no\_default\_epv** switch directs the MIDL compiler not to generate a default entry-point vector (epv). The use of this attribute is not recommended.

``` syntax
midl /no_default_epv
```

## Switch Options

This switch has no parameters.

## Remarks

In this case, the application must register an epv with the [**RpcServerRegisterIf**](/windows/desktop/api/rpcdce/nf-rpcdce-rpcserverregisterif) call. Compare this switch with the [**/use\_epv**](-use-epv.md) switch.

## Examples

**midl /no\_default\_epv filename.idl**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**/use\_epv**](-use-epv.md)
</dt> <dt>

[**RpcServerRegisterIf**](/windows/desktop/api/rpcdce/nf-rpcdce-rpcserverregisterif)
</dt> </dl>

 

 