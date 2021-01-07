---
description: Parental Controls SKU Availability
ms.assetid: 5fbf6c4a-3897-4a12-bef6-19478fdb48aa
title: Parental Controls SKU Availability
ms.topic: article
ms.date: 05/31/2018
---

# Parental Controls SKU Availability

The Parental Controls user interfaces, features, and APIs described in this section are currently planned to be available only on consumer-focused SKUs such as:

-   Windows Vista Starter
-   Windows Vista Home Basic
-   Windows Vista Home Premium
-   Windows Vista Ultimate

Parental Controls only installs on these SKUs. Solutions having a requirement to deploy onto business SKUs will need to either:

-   Detect and not provide parental controls functionality on business SKUs.
-   Detect and provide an alternative means of configuration, logging, and restrictions.

It is recommended that solutions detect availability of the Parental Controls Infrastructure by checking for success of COM CoCreateInstance on the Compliance API.

Parental Controls-aware applications depending on the Windows Vista infrastructure may also want to suppress any of their own UI exposing settings or other functionality when Parental Controls UI is suppressed on a supported SKU. A function is provided for visibility determination that covers cases such as domain-joined suppression.

 

 



