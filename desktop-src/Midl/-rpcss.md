---
title: /rpcss switch
description: The /rpcss switch, when specified, acts as though the enable\_allocate attribute was specified on all operations of the interface. The usage of this attribute is not recommended.
ms.assetid: a4507779-7d07-4517-8592-39f0d9460bc3
keywords:
- /rpcss switch MIDL
topic_type:
- apiref
api_name:
- /rpcss
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /rpcss switch

The **/rpcss** switch, when specified, acts as though the [**enable\_allocate**](enable-allocate.md) attribute was specified on all operations of the interface. The usage of this attribute is not recommended.

``` syntax
midl /rpcss
```

## Switch Options

This switch has no parameters.

## Remarks

In default mode, the RpcSs package is enabled only if either the procedure or interface has the [**enable\_allocate**](enable-allocate.md) attribute or the **/rpcss** switch is specified on the command line. In **/osf** mode, the server-side stub enables the RpcSs allocation package.

## Examples

**midl /rpcss filename.idl**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**enable\_allocate**](enable-allocate.md)
</dt> <dt>

[**/osf**](-osf.md)
</dt> </dl>

 

 




