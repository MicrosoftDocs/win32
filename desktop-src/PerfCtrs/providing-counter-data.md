---
description: In Windows Vista, Performance Counters implemented a new architecture (version 2.0) for providing counter data.
ms.assetid: c17eda2f-3cf8-40d6-8be6-c1ce190d1a26
title: Providing Counter Data
ms.topic: article
ms.date: 08/17/2020
---

# Providing Counter Data

Software components that publish data via Windows Performance Counters are called performance data providers.

Windows supports two kinds of performance data providers. Legacy performance data providers (**V1 providers**) are implemented using an .INI file and a performance DLL. Modern performance data providers (**V2 providers**) use a .MAN (XML manifest) and the performance counter provider APIs.

## Manifests

Modern performance data providers use a .MAN (XML manifest) to define the counter data and use performance counter provider APIs to manage data within the context of the provider.

Providers implemented using a manifest and performance counter provider APIs are often called **V2 providers**.

Windows supports user-mode V2 providers on Windows Vista or later. For user-mode details, see [Providing Counter Data Using Version 2.0](providing-counter-data-using-version-2-0.md).

Windows supports kernel-mode V2 providers on Windows 7 or later. For kernel-mode details, see [Kernel Mode Performance Monitoring](/windows-hardware/drivers/devtest/kernel-mode-performance-monitoring).

## Performance DLL (deprecated)

In the legacy performance counter architecture, providers implemented a performance DLL to that ran in the consumer's process to collect and provide the counter data when a consumer requested it. The provider used an initialization (.INI) file and registry entries to define the counters and to configure the performance DLL.

Providers implemented using an .INI file and a performance DLL are often called **V1 providers**.

> [!CAUTION]
> Although you can still use a performance DLL to provide counter data, this architecture is deprecated due to significant performance and reliability limitations. In addition, V1 providers are often harder to implement since they require shipping a separate DLL that must run in the consumer's process.

For details, see [Providing Counter Data Using a Performance DLL](providing-counter-data-using-a-performance-dll.md).
