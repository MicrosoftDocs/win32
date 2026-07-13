---
title: Creating a Private Sensor Pool
description: Learn how to use the Windows Biometric (WinBio) Framework API to create a private sensor pool with these essential resources.
ms.assetid: 79944E30-A3D4-411D-A551-3B309DEA6FEA
ms.topic: concept-article
ms.date: 03/31/2025
# Customer intent: As a Windows developer, I want to learn how to use the Windows Biometric Framework API to create a private sensor pool.
---

# Creating a Private Sensor Pool

> [!IMPORTANT]
> For secure biometric sensors, only enrollments in the Virtual Secure Mode (VSM) authorized enrollment database will be able to authorize key release. This means that existing third-party secure biometric enrollment applications will not be able to enroll or perform Windows Biometric (WinBio) calls. 

> [!NOTE]
> The WinBio API surface is not supported for Windows Enhanced Sign-in Security (ESS) fingerprint sensors.

A private sensor pool is a collection of biometric units reserved for exclusive use by a client application. Private pools support proprietary authentication methods and enable a client application to access a biometric unit by using vendor-specified control commands.

The topics in this section contain code examples that explain how to create a private sensor pool.

## In this section

| Topic | Description |
|-------|-------------|
| [Sensor Pools](sensor-pools.md) | Describes three possible sensor pools: system, private, and unassigned. |
| [Private Pool Setup](private-pool-setup.md) | Contains the setup console project. |
| [Private Pool Identity](private-pool-identity.md) | Contains the identification console project. |
| [Private Pool Enrollment](private-pool-enrollment.md) | Contains the enrollment console project. |
| [Private Pool Helper Functions](private-pool-helper-functions.md) | Contains helper functions for the setup, identification, and enrollment console projects. |
| [Create client applications](creating-client-applications.md) | How to use the Windows Biometric Framework API to create client applications. |

## Related content

[Windows Biometric Framework API Reference](biometric-service-api-reference.md)
