---
title: /app_config switch
description: The /app\_config switch selects application-configuration mode, which allows you to use some ACF keywords in the IDL file. With this MIDL compiler switch, you can omit the ACF and specify an interface in a single IDL file.
ms.assetid: 8d12a0ed-7eaa-4ebc-a961-b726aefefadc
keywords:
- /app_config switch MIDL
topic_type:
- apiref
api_name:
- /app_config
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /app\_config switch

The **/app\_config** switch selects application-configuration mode, which allows you to use some ACF keywords in the IDL file. With this MIDL compiler switch, you can omit the ACF and specify an interface in a single IDL file.

``` syntax
midl /app_config
```

## Switch Options

This switch has no parameters.

## Remarks

Microsoft RPC supports the use of the following ACF attributes in the IDL file:

-   Implicit\_handle
-   Auto\_handle
-   Explicit\_handle

Future releases of Microsoft RPC may support the use of other ACF attributes in the IDL file. The **/app\_config** option represents a Microsoft extension to the OSF-DCE specification and, as such, is mutually exclusive with the [**/osf**](-osf.md) option.

For more information related to the **/app\_config** switch, see [Application Configuration File (ACF)](application-configuration-file-acf-.md) and [Interface Definition (IDL) File](interface-definition-idl-file.md).

## Examples

**midl /app\_config filename.idl**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> </dl>

 

 




