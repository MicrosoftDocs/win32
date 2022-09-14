---
title: /Os switch
description: The /Os switch specifies the mixed-mode method to marshal stub code passed between client and server.
ms.assetid: dc5cafbb-dcc6-4fcb-a04f-1bc9720a13cb
keywords:
- /Os switch MIDL
topic_type:
- apiref
api_name:
- /Os
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /Os switch

The **/Os** switch specifies the mixed-mode method to marshal stub code passed between client and server.

``` syntax
midl /Os
```

## Switch Options

This switch has no parameters.

## Remarks

There are important issues to consider before deciding on the method for marshaling code. These issues concern size and performance. The MIDL compiler provides two methods for marshaling code: mixed-mode (**/Os**) and fully-interpreted ([**/Oi**](-oi.md)). The fully-interpreted method marshals data completely offline. This reduces the size of the stub code considerably, but it also results in decreased performance.

Use MIDL default mode **/Oicf** /robust for all purposes other than backward compatibility. This mode is the secure standard mode of MIDL compiler; any other mode should be used only after careful consideration to the security implication, realizing that future extensions will only be implemented for default mode. In mixed mode, the compiler marshals some parameters inline in the generated stubs. While this results in larger stub size, it also may offer increased performance.

MIDL provides full support for multidimensional arrays and multidimensional-sized pointers only in [**/Oicf**](-oi.md) mode. In **/Os** and **/Oi** modes, the compiler supports simple cases, such as fixed-size arrays. Using multidimensional arrays in **/Os** or **/Oi** modes can result in parameters that are not marshaled correctly. Microsoft recommends that you use the **/Oicf** command line switch when your interface defines parameters that are multidimensional arrays or multidimensional-sized pointers.

To further define the level of gradation in how data is marshaled, this version of RPC provides an \[[**optimize**](optimize.md)\] attribute. This attribute is used as an ACF interface attribute or operation attribute to select the marshaling mode.

## Examples

**midl /Os filename.idl**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/Oi**](-oi.md)
</dt> <dt>

[**optimize**](optimize.md)
</dt> <dt>

[**/no\_format\_opt**](-no-format-opt.md)
</dt> </dl>

 

 




