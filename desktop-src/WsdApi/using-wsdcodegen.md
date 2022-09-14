---
description: Describes the process of building a WSDAPI application using WsdCodeGen.
ms.assetid: 8f172e2c-4cd1-4108-9c8d-01a731aca83b
title: Using WsdCodeGen
ms.topic: article
ms.date: 05/31/2018
---

# Using WsdCodeGen

**To build a WSDAPI application using WsdCodeGen**

1.  Define the functional contract for the device host in a WSDL file.
2.  Generate a configuration file using WsdCodeGen. For more information, see [WsdCodeGen Configuration File](wsdcodegen-configuration-file.md) and [WsdCodeGen Command Line Syntax](wsdcodegen-command-line-syntax.md).
3.  Open the generated configuration file and modify the file as required. If you are building a client application, little or no modification is required. If you are building a host application, change the user-specific configuration elements (such as [**manufacturer**](manufacturer.md) and [**modelName**](modelname.md)).
4.  Generate code using WsdCodeGen, providing the configuration file as input. For more information, see [WsdCodeGen Command Line Syntax](wsdcodegen-command-line-syntax.md).
5.  Use the generated code to build a client, host, or both.

The Windows SDK includes some sample WSDL files, WsdCodeGen configuration files, and generated code. For more information, see [WSDAPI Samples](wsdapi-samples.md).

## Related topics

<dl> <dt>

[WSDAPI Samples](wsdapi-samples.md)
</dt> </dl>

 

 



