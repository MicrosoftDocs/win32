---
title: MIDL Compiler Errors and Warnings
description: When using the MIDL compiler, errors and warnings can be caused by improper use of the command-line switches or by the content of the IDL and ACF files.
ms.assetid: 5c8d5a28-e559-4893-932f-b2306aefa932
keywords:
- Microsoft Interface Definition Language MIDL , reference
- MIDL compiler MIDL , errors
- compiler MIDL , errors
- errors MIDL
ms.topic: article
ms.date: 05/31/2018
---

# MIDL Compiler Errors and Warnings

When using the MIDL compiler, errors and warnings can be caused by improper use of the command-line switches or by the content of the IDL and ACF files. If the error is due to improperly entering the command-line switches, an error or warning message may specify the name of one or more MIDL compiler mode switches. For example, you can include certain ACF attributes in an IDL file when you use the /**app\_config** switch, but that IDL file will generate an error if you compile without using the /**app\_config** switch.

Errors in the IDL and ACF files fall into two categories: errors caught by the preprocessor and errors recognized by the compiler. This section lists the MIDL preprocessor and compiler error messages. It also describes their formats and causes.

-   [Error and Warning Message Formats](error-and-warning-message-formats.md)
-   [Preprocessor Errors](preprocessor-errors.md)
-   [Compiler Errors](compiler-errors.md)

 

 




