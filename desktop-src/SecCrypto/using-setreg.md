---
description: The SetReg tool sets the value of the registry keys controlling the behavior of the Authenticode certificate verification process.
ms.assetid: c34c00fe-da99-4c2e-9e9a-0ef6406ae5ae
title: Using SetReg
ms.topic: article
ms.date: 05/31/2018
---

# Using SetReg

The SetReg tool sets the value of the registry keys controlling the behavior of the Authenticode certificate verification process. These keys, called the Software Publishing State Keys, control whether to trust a test root, allow offline approval of certificates, test certificate expiration dates, and perform revocation checks.

The following command lists the syntax and options for using SetReg.

**setreg -?**

The following command makes a test root trusted. By default, a test root is not trusted. After any changes in the key values are made, a list of the current value of all of the key values is displayed. If the **-q** option is used, the key values are not displayed.

**setreg 1 TRUE**

The following command makes a test root untrusted and causes all verification to check for revocation. The **-q** option is used so that the list of key values is not displayed

**setreg -q 1 FALSE 3 TRUE**

> [!Note]  
> Commands, options, and arguments are not case sensitive.

 

 

 



