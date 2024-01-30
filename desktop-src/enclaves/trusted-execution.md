---
description: Enclaves are used to create trusted execution environments. An enclave is an isolated region of code and data within the address space for an application.
ms.assetid: 72CE4682-150F-4BED-8A09-99FE5FB1BD2F
title: Secure Enclaves (Trusted Execution)
ms.topic: article
ms.date: 08/02/2023
---

# Secure Enclaves (Trusted Execution)

Enclaves are used to create trusted execution environments. An enclave is an isolated region of code and data within the address space for an application. Only code that runs within the enclave can access data within the same enclave.

The following enclave technologies (or enclave types) are currently supported:

- **Virtualization-based Security (VBS) enclaves** - a software-based technology that relies on Windows hypervisor and doesn't require any special hardware.
- **Intel Software Guard Extensions (Intel SGX) enclaves** - a hardware-based trusted execution environment technology.

## In This Section

- [Enclave Reference](trusted-execution-reference.md)
- [VBS Enclaves](vbs-enclaves.md)
- [APIs Available in VBS Enclaves](available-in-enclaves.md)
