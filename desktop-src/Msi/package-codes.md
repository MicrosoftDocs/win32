---
description: The package code is a GUID identifying a particular Windows Installer package.
ms.assetid: dcb6a0d4-e28d-453d-9bda-bfe74f74579b
title: Package Codes
ms.topic: article
ms.date: 05/31/2018
---

# Package Codes

The package code is a GUID identifying a particular Windows Installer [*package*](p-gly.md). The package code associates an .msi file with an application or product and can also be used for the verification of sources. The product and package codes are not interchangeable. For details, see [Product Codes](product-codes.md).

Nonidentical .msi files should not have the same package code. It is important to change the package code because it is the primary identifier used by the installer to search for and validate the correct package for a given installation. If a package is changed without changing the package code, the installer may not use the newer package if both are still accessible to the installer.

The package code is stored in the [**Revision Number Summary**](revision-number-summary.md) Property of the [Summary Information Stream](summary-information-stream.md). Note that letters in product code and package code GUIDs must be uppercase. Utilities such as GUIDGEN generate GUIDs containing lowercase letters. The lowercase letters in these GUIDs must be changed to uppercase to be used as a product code or package code.

Although it is common to ship an application that has the same package code and product code, the two values can diverge as the application is updated. For example, including a new file with the application would require updating the installation database to install the file. If the changes are minor a developer may choose not to change the product code, however, a different .msi file is needed to install the new file and so the package code must be incremented. Conversely, a single package can be used to install more than one product. For example, the installation of a package without a language transform could install the English version of the application and the installation of the same package with a language transform could install the French version. The transform is distinct from the .msi file that determines the package code. The English and French versions could have different product codes and the same package code because they are both installed with the same .msi file.

 

 



