---
description: Learn how to use the Cert2SPC tool to create test Software Publisher Certificates from X.509 certificates in the Windows SDK for development purposes.
ms.assetid: d05df388-c19d-47a5-9ede-11cf06c29fc8
title: Cert2SPC Tool - Create Test Software Publisher
ms.topic: reference
ms.date: 08/21/2025
---

# Cert2SPC

The Cert2SPC tool creates test [Software Publisher Certificates](../secgloss/s-gly.md) (SPCs) from existing [X.509](../secgloss/x-gly.md) [certificates](../secgloss/c-gly.md), enabling developers to generate test certificates for code signing during development. Cert2SPC can wrap multiple X.509 certificates into a [PKCS \#7](../secgloss/p-gly.md) signed-data object. The tool is installed in the \\Bin folder of the Microsoft Windows Software Development Kit (SDK) installation path.

Cert2SPC is available as part of the Windows SDK, which you can download [here](https://developer.microsoft.com/windows/downloads/windows-sdk/).

> [!NOTE]
> This tool is for test purposes only. A valid SPC is obtained from a [certification authority](../secgloss/c-gly.md).

## Syntax

Use the following syntax to create a test SPC:

**Cert2SPC** *Cert1.cer Cert2.cer* … *Output.spc*

## Parameters

The following parameters are required:

| Parameters | Description |
|------------|-------------|
| *Cert1.cer Cert2.cer* … | Names of the X.509 certificates to include in the SPC. Each certificate name ends with the .cer extension. |
| *Output.spc* | Name of the PKCS \#7 object that contains the X.509 certificates to be created. The output file name ends with the .spc extension. |

## Related content

- [X.509 Certificates](../secgloss/x-gly.md)
- [PKCS \#7](../secgloss/p-gly.md)
- [Software Publisher Certificates](../secgloss/s-gly.md)
